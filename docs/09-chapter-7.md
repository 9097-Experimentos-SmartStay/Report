# Capítulo VII: DevOps Practices

## 7.1. Continuous Integration

La Integración Continua (CI) en la plataforma SmartStay constituye el conjunto de prácticas, mecanismos de automatización y herramientas orientadas a validar, compilar y verificar la calidad de cada incremento de código desarrollado por el equipo. Dado que la arquitectura de la solución involucra múltiples componentes heterogéneos —Backend RESTful en ASP.NET Core, Frontend Web en Vue.js, Landing Page en HTML/CSS/JS y la Aplicación Móvil nativa en Android (Kotlin)—, el flujo de CI se diseñó para ejecutarse de forma distribuida y desatendida sobre los repositorios de GitHub bajo el flujo de trabajo GitFlow.


![ContinousIntegration1](../assets/chapter-7/ContinuousIntegration/ContinuousIntegration1.jpeg)

---

### 7.1.1. Tools and Practices

Para garantizar que el código integrado sea funcional, seguro y conforme a los lineamientos arquitectónicos, se establecieron las siguientes herramientas y prácticas operativas:

#### 1. Herramientas de Integración Continua

* **GitHub Actions:** Orquestador principal de automatización. Gestiona los flujos de trabajo (*workflows*) declarados en archivos YAML dentro de `.github/workflows/` (tales como `docker-publish.yml` y flujos de integración continua específicos por componente).

* **Entornos de Ejecución (.NET SDK, Node.js y JDK):**
  * Para el Backend: **.NET SDK 8.0** con la herramienta de configuración global `.config/dotnet-tools.json` para estandarizar el conjunto de herramientas de compilación y pruebas.
  * Para el Frontend Web y Landing Page: **Node.js (LTS)** con gestor de paquetes `npm`.
  * Para la Aplicación Móvil: **OpenJDK 17** y **Gradle** en Android Studio para la compilación de módulos Kotlin.

* **Herramientas de Análisis Estático y Linters:**
  * **ESLint y Prettier:** Verificación de formato, sintaxis limpia y cumplimiento de buenas prácticas de JavaScript y Vue.js.
  * **Roslyn Analyzers / C# Coding Conventions:** Validación del código en el backend siguiendo las convenciones de Microsoft ASP.NET Core (nombres en PascalCase, contratos explícitos e inyección de dependencias).
  * **Android Lint / ktlint:** Comprobación de estándares de código limpio y optimización de recursos XML y Kotlin en la aplicación móvil.

#### 2. Prácticas de Ingeniería Aplicadas

* **Integración Diaria y Commits Semánticos:** Los desarrolladores integran ramas de funcionalidad (`feature/`) hacia la rama base de integración (`develop`) de forma frecuente mediante *Pull Requests*. Los mensajes de confirmación respetan las convenciones estándar (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`) para facilitar la trazabilidad y la generación de registros de cambios.

* **Protección de Ramas (Branch Protection Rules):** La rama principal de producción (`main`) y la rama de integración (`develop`) se encuentran protegidas. No se permiten *direct pushes*; toda fusión exige:
  1. Aprobación obligatoria por revisión de código entre pares (*Peer Review*).
  2. Ejecución satisfactoria y sin errores de los flujos de GitHub Actions correspondientes.

* **Compilación Limpia (Zero-Warning Build):** El proceso de compilación automática está configurado para fallar si se detectan errores de sintaxis, dependencias circulares o advertencias de compilación no resueltas.

* **Auditoría de Dependencias Vulnerables:** Se ejecutan comandos automatizados de escaneo de librerías (`dotnet list package --vulnerable` y `npm audit`) antes de autorizar la compilación de paquetes productivos.

---

### 7.1.2. Build & Test Suite Pipeline Components

El pipeline de construcción y verificación de pruebas automatizadas está estructurado en componentes y etapas secuenciales. Cada vez que se crea un *Pull Request* o se realiza un *push* sobre `develop`, el pipeline orquesta las siguientes fases:

![PipelineComponents](../assets/chapter-7/BuildTest/PipelineComponents.jpeg)

#### 1. Componentes del Pipeline por Plataforma

* **Backend (`backend-aw-smartstay`):**
  * *Restauración y Compilación:* Se ejecutan `dotnet restore` sobre la solución `backend-aw-smartstay.sln` y posteriormente `dotnet build --configuration Release --no-restore`.
  * *Ejecución de Pruebas Unitarias y de Dominio:* Mediante el ejecutable `dotnet test` se corren todas las clases del proyecto `BackendAwSmartstay.API.Tests`, aplicando el patrón **Arrange-Act-Assert (AAA)**:
    * Pruebas de Dominio e Identidad: `GuestProfileTests.cs`, `StaffProfileTests.cs` y `StaffAssignmentTests.cs`.
    * Pruebas de Reservas y Transacciones: `BookingTests.cs`, verificando transiciones de estado de reserva y cálculo de tarifas.
    * Pruebas de Integración y Fachadas ACL: `BookingCommandServiceAclIntegrationTests.cs` y `AccommodationsContextFacadeTests.cs`.
    * Pruebas de Persistencia y Concurrencia en MySQL: `ProfilesMySqlConcurrencyIntegrationTests.cs` y `BookingsPersistenceTests.cs`.
    * Pruebas de Controladores REST: `GuestsControllerTests.cs` y `StaffControllerTests.cs`.

* **Landing Page y Frontend Web:**
  * *Compilación y Bundle:* Ejecución de `npm ci` seguido de `npm run build` para generar los bundles estáticos minificados de producción en el directorio `dist/`.
  * *Suite de Pruebas de UI:* Ejecución de `npm test` mediante Jest para validar el renderizado del home, el correcto direccionamiento de los botones CTA y la operatividad de los diccionarios de internacionalización (`languages.js`).

* **Móvil Android:**
  * *Compilación y Pruebas Locales:* Se ejecuta `./gradlew testDebugUnitTest` para comprobar los modelos de datos, la gestión de sesiones en `TokenManager` y la lógica de presentación de los ViewModels.

#### 2. Declaración del Workflow de Integración (Ejemplo de Configuración de CI)

A continuación, se documenta la estructura del pipeline de CI automatizado en GitHub Actions para el backend del sistema (`.github/workflows/ci-backend.yml`):

```yaml
name: SmartStay Backend CI Pipeline

on:
  push:
    branches: [ develop, main ]
  pull_request:
    branches: [ develop, main ]

jobs:
  build-and-test:
    name: Build, Static Analysis and Unit Testing
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Source Code
      uses: actions/checkout@v4

    - name: Setup .NET SDK
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: '8.0.x'

    - name: Restore NuGet Dependencies
      run: dotnet restore backend-aw-smartstay.sln

    - name: Compile Backend Solution
      run: dotnet build backend-aw-smartstay.sln --configuration Release --no-restore

    - name: Execute Test Suite (Domain, ACL & Persistence)
      run: >
        dotnet test backend-aw-smartstay.sln
        --configuration Release
        --no-build
        --verbosity normal
        --logger "trx;LogFileName=test_results.trx"
        --collect:"XPlat Code Coverage"

    - name: Upload Test Results
      if: always()
      uses: actions/upload-artifact@v4
      with:
        name: test-results
        path: "**/test_results.trx"
```

El resultado de este pipeline garantiza que ningún incremento con pruebas fallidas o errores de compilación pueda ser fusionado al código base, garantizando la estabilidad operativa del sistema previo a las etapas de entrega y despliegue.

## 7.2. Continuous Delivery

### 7.2.1. Tools and Practices.

### 7.2.2. Stages Deployment Pipeline Components.

## 7.3. Continuous deployment

### 7.3.1. Tools and Practices.

### 7.3.2. Production Deployment Pipeline Components.
