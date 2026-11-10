# Capítulo VI: Product Verification & Validation

## 6.1. Testing Suites & Validation

La estrategia de validación de SmartStay cubre los tres servicios principales: **el backend, la aplicación web y la aplicación móvil.** 

El backend cuenta con pruebas unitarias, de integración y de comportamiento (BDD) automatizadas; la aplicación móvil, con pruebas de Flutter; y la aplicación web, con una prueba funcional manual de Selenium sobre el inicio de sesión. La landing page no tiene pruebas automatizadas.

### 6.1.1. Core Entities Unit Tests.

El backend de SmartStay cuenta con dos proyectos de pruebas de entidades y reglas de negocio: `BackendAwSmartstay.API.UnitTests`, que cubre Bookings (dominio) y Payments, y `BackendAwSmartstay.API.Tests`, que organiza las pruebas de los módulos Accommodations, Bookings y Profiles. Su estructura separa las áreas de aplicación, dominio e infraestructura, y contempla pruebas de compatibilidad e interfaces en el módulo de perfiles.

| Módulo | Proyecto de pruebas | Áreas presentes |
|---|---|---|
| Accommodations | `API.Tests` | Application, con una sección ACL. |
| Bookings | `API.UnitTests` y `API.Tests` | Domain en ambos; Application e Infrastructure en `API.Tests`. |
| Profiles | `API.Tests` | Application, Compatibility, Domain, Infrastructure e Interfaces. |
| Payments | `API.UnitTests` | Application, Domain e Infrastructure. |

<br>
*Test de persistencia de Payments*

![payments-bc-test](../assets/chapter-6/core-entities-tests/payments-bc-test.png)
![payments-test-suceed](../assets/chapter-6/core-entities-tests/payments-test-suceed.png)

Esta organización permite ubicar las pruebas según el módulo y la responsabilidad del componente evaluado. Las áreas de dominio corresponden a las entidades y reglas de negocio; las de aplicación, a la coordinación de operaciones; y las de infraestructura, a mecanismos como la persistencia. Las secciones de compatibilidad, interfaces y ACL permiten organizar verificaciones relacionadas con la interacción entre componentes.

![testing-backend-project](../assets/chapter-6/testing-suites/testing-backend-project.png)

![pass-test](../assets/chapter-6/testing-suites/pass-test.png)

### Validación funcional del inicio de sesión del frontend

Se ejecutó una prueba funcional automatizada con Selenium sobre el formulario de inicio de sesión de SmartStay. La ejecución se realizó en Chrome, en modo visible, utilizando el frontend local en `http://localhost:5173/login`.

La prueba consistió en dejar vacíos el correo electrónico y la contraseña e intentar enviar el formulario. Se verificó que ambos campos permanecieran vacíos, que la aplicación conservara la ruta de inicio de sesión y que mostrara una validación comprensible.

| Caso evaluado | Resultado esperado | Resultado observado | Estado |
|---|---|---|---|
| Enviar el formulario de inicio de sesión con correo y contraseña vacíos. | Impedir continuar y mostrar una validación para ambos campos obligatorios. | La aplicación permaneció en `/login` y mostró «Este campo es obligatorio.» debajo del correo y de la contraseña. | Aprobado |

El resultado confirma la validación de campos obligatorios en este escenario. No se utilizaron credenciales ni se crearon cuentas, reservas o pagos.

El alcance de esta prueba se limita al envío del formulario vacío. No verifica la autenticación con credenciales, la autorización por roles ni los demás flujos del frontend.

![testing-frontend](../assets/chapter-6/testing-suites/testing-frontend.png)

### 6.1.2. Core Integration Tests.

El backend incluye pruebas de persistencia con Entity Framework en memoria y pruebas de colaboración que utilizan repositorios y fachadas simulados. Estas pruebas permiten evaluar parte de la interacción entre componentes, aunque no reproducen todas las restricciones ni el comportamiento concurrente de MySQL. Existe una prueba de concurrencia contra MySQL real (`ProfilesMySqlConcurrencyIntegrationTests`) que termina sin evaluar nada cuando no hay una base MySQL disponible, como ocurre en el pipeline de CI; por eso se cuenta como superada pero no aporta evidencia de concurrencia hasta que se ejecute con `TEST_MYSQL_CONNECTION` configurada.

![integration1](../assets/chapter-6/integration-tests/integration1.png)
![integration2](../assets/chapter-6/integration-tests/integration2.png)

### 6.1.3. Core Behavior-Driven Development

Para verificar el comportamiento del software desde la perspectiva del negocio y del usuario final, se implementó una suite de pruebas automatizadas bajo el enfoque **Behavior-Driven Development (BDD)**. Se creó el proyecto dedicado `BackendAwSmartstay.API.BddTests` integrado a la solución backend sobre **.NET 9**, utilizando **Reqnroll (v2.3.0)** sobre **NUnit (v4.2.2)**, **FluentAssertions (v7.2.0)** y aislamiento de persistencia en memoria mediante `Microsoft.EntityFrameworkCore.InMemory`.

#### 1. Cobertura de User Stories y Escenarios BDD

Se implementaron y validaron **28 escenarios** en sintaxis Gherkin (en español), distribuidos en las **9 User Stories** centrales del Product Backlog:

| User Story ID | Título de la Historia | Módulo / Contexto | Escenarios Implementados | Estado |
| --- | --- | --- | --- | --- |
| **US-01** | Registro de usuario con validación | IAM | 3 | Aprobado |
| **US-02** | Inicio de sesión seguro | IAM | 3 | Aprobado |
| **US-03** | Gestión de perfiles y roles | IAM / Profiles | 3 | Aprobado |
| **US-04** | Recuperación de contraseña | IAM | 3 | Aprobado |
| **US-52** | Autenticación 2FA para staff | IAM | 3 | Aprobado |
| **US-06** | Gestión de habitaciones y estados | Accommodations | 3 | Aprobado |
| **US-53** | Configuración de hotel y habitaciones | Accommodations | 3 | Aprobado |
| **US-07** | Gestión centralizada de reservas | Bookings | 3 | Aprobado |
| **US-51** | Reserva de habitación por huésped | Bookings | 4 | Aprobado |
| **Total** | **9 Historias de Usuario** | **3 Contextos Delimitados** | **28 Escenarios** | **100% Pass** |

#### 2. Especificación de Escenarios Gherkin (`.feature`)

Los archivos `.feature` capturan los criterios de aceptación en lenguaje ubicuo mediante la estructura `Given-When-Then`. Las palabras clave de Gherkin están en inglés y los textos de cada paso, en español. Los siguientes fragmentos corresponden a los archivos del repositorio `backend`.

##### Archivo: `US51_ReservaHabitacionPorHuesped.feature` (Contexto Bookings)

```gherkin
@US-51
@Bookings
Feature: Reserva de habitación por huésped

  Como huésped del hotel SmartStay
  Quiero reservar una habitación disponible para mis fechas de estadía
  Para asegurar mi alojamiento de forma confiable

  @US-51
  @happy-path
  Scenario: Registrar una reserva para una habitación disponible
    Given que existe un hotel registrado y operativo
    And existe una habitación "101" de tipo "Double" disponible con precio por noche de 150.00 soles
    And existe un huésped registrado con correo "juan.perez@smartstay.pe" y nombre "Juan Perez"
    When el huésped solicita registrar una reserva desde "2026-11-01" hasta "2026-11-05"
    Then la reserva debe crearse exitosamente
    And el estado inicial de la reserva debe ser "Pending"
    And la reserva debe contener un código de reserva generado
    And la reserva debe estar asociada a la habitación "101"

  @US-51
  @negative
  Scenario: Rechazar una reserva que se superpone con otra reserva existente
    Given que existe un hotel registrado y operativo
    And existe una habitación "102" de tipo "Single" disponible con precio por noche de 100.00 soles
    And existe una reserva activa para la habitación "102" del "2026-11-10" al "2026-11-15"
    When otro huésped intenta registrar una reserva para la habitación "102" del "2026-11-12" al "2026-11-14"
    Then la solicitud de reserva debe ser rechazada indicando que la habitación no está disponible
```

##### Archivo: `US06_GestionHabitacionesYEstados.feature` (Contexto Accommodations)

```gherkin
@US-06
@Accommodations
Feature: Gestión de habitaciones y estados

  Como personal del hotel (Staff / Housekeeping / Maintenance)
  Quiero actualizar el estado operativo de una habitación
  Para reflejar con precisión su disponibilidad y control en el sistema

  @US-06
  @happy-path
  Scenario: Cambiar el estado de una habitación de Disponible a Mantenimiento
    Given que existe una habitación "301" en estado "Available"
    When el personal solicita cambiar el estado de la habitación "301" a "Maintenance"
    Then el estado de la habitación "301" debe actualizarse a "Maintenance"

  @US-06
  @negative
  Scenario: Rechazar una transición de estado no permitida para la habitación
    Given que existe una habitación "303" en estado "Occupied"
    When el personal solicita cambiar el estado de la habitación "303" a "Available"
    Then la solicitud de cambio de estado debe ser rechazada por transición no permitida
```

#### 3. Implementación de Step Definitions en C# (.NET 9)

La vinculación entre los pasos Gherkin y los servicios del backend se implementa mediante clases decoradas con el atributo `[Binding]` de Reqnroll. Cada User Story tiene su clase de pasos, y los escenarios se ejecutan contra el servicio de aplicación real y una base de datos en memoria. El siguiente fragmento es de `US51_ReservaHabitacionStepDefinitions.cs`:

```csharp
[Binding]
public class US51_ReservaHabitacionStepDefinitions
{
    private readonly ScenarioContext _context;
    private Booking? _createdBooking;
    private Exception? _caughtException;

    [When(@"el huésped solicita registrar una reserva desde ""(.*)"" hasta ""(.*)""")]
    public async Task WhenElHuespedSolicitaRegistrarUnaReservaDesdeHasta(string checkIn, string checkOut)
    {
        try
        {
            var service = CreateService();
            var command = new CreateBookingCommand(
                Requester: BookingRequester.Guest(_guestUserId, _guestEmail),
                RoomId: _roomId,
                GuestName: _guestName,
                GuestEmail: _guestEmail,
                CheckInDate: DateTime.Parse(checkIn),
                CheckOutDate: DateTime.Parse(checkOut),
                UserId: _guestUserId);

            _createdBooking = await service.Handle(command);
        }
        catch (Exception ex)
        {
            _caughtException = ex;
        }
    }

    [Then(@"la reserva debe crearse exitosamente")]
    public void ThenLaReservaDebeCrearseExitosamente()
    {
        _caughtException.Should().BeNull();
        _createdBooking.Should().NotBeNull();
    }

    [Then(@"el estado inicial de la reserva debe ser ""(.*)""")]
    public void ThenElEstadoInicialDeLaReservaDebeSer(string status)
    {
        _createdBooking!.Status.ToString().Should().Be(status);
    }
}
```

#### 4. Resultados de Ejecución

Los resultados corresponden a la ejecución de `dotnet test` dentro del job *Build & test* del workflow `ci-backend.yml` sobre la rama `develop` (ejecución #7 del 07/10/2026, tras fusionar el pull request #13), que corre las tres suites en un mismo paso:

```text
Passed!  - Failed: 0, Passed:  87, Skipped: 0, Total:  87, Duration: 397 ms - BackendAwSmartstay.API.UnitTests.dll (net9.0)
Passed!  - Failed: 0, Passed: 150, Skipped: 0, Total: 150, Duration: 6 s    - BackendAwSmartstay.API.Tests.dll (net9.0)
Passed!  - Failed: 0, Passed:  28, Skipped: 0, Total:  28, Duration: 12 s   - BackendAwSmartstay.API.BddTests.dll (net9.0)
```

| Suite de Pruebas | Framework / Versión | Tipo de Prueba | Total | Aprobados | Fallidos |
| --- | --- | --- | ---: | ---: | ---: |
| `BackendAwSmartstay.API.UnitTests` | NUnit 4.2.2 / .NET 9 | Unitarias de Bookings y Payments | 87 | 87 | 0 |
| `BackendAwSmartstay.API.Tests` | NUnit 4.2.2 / .NET 9 | Unitarias e integración de Accommodations, Bookings y Profiles | 150 | 150 | 0 |
| `BackendAwSmartstay.API.BddTests` | Reqnroll 2.3.0 + NUnit 4.2.2 | Comportamiento (BDD / Gherkin) | 28 | 28 | 0 |
| **Total consolidado** | **.NET 9 Test Platform** | **Verificación completa** | **265** | **265** | **0** |

![guerkin-test](../assets/chapter-6/testing-suites/guerkin-test.png)

### 6.1.4. Core System Tests

Se ejecutó una prueba funcional automatizada con Selenium sobre el formulario de inicio de sesión del frontend. Se utilizó Chrome visible y la instancia local del frontend en `http://localhost:5173/login`. El caso dejó vacíos el correo electrónico y la contraseña y trató de enviar el formulario.

| Aplicación | Caso | Resultado esperado | Resultado observado | Estado |
|---|---|---|---|---|
| Frontend web | Enviar el inicio de sesión con ambos campos vacíos | Impedir el envío y mostrar una validación en cada campo obligatorio | La ruta se mantuvo en `/login` y aparecieron dos mensajes «Este campo es obligatorio.» | Aprobado |
| Backend | Pruebas del controlador de staff (`StaffControllerTests`, 14 pruebas en `BackendAwSmartstay.API.Tests`) | El controlador de staff responde correctamente a los casos de prueba | Superadas en la ejecución de CI del 07/10/2026 | Aprobado |
| Mobile | Pruebas de Flutter de los modelos de staff, del cliente de reservas del huésped y de la plantilla de widget (`staff_models_test.dart`, `guest_booking_api_test.dart` y `widget_test.dart`, 16 casos) | Los modelos, los roles y las llamadas a la API de reservas se comportan según lo esperado | Sin ejecución registrada: el repositorio `mobile` no tiene pipeline de CI y las pruebas no se ejecutaron en este avance | Pendiente |

Esta ejecución solo confirma la validación de campos vacíos en ese formulario. No verifica autenticación con credenciales, permisos por rol, conexión con el backend, ni otros flujos de la aplicación web. No se guardó una captura ni un reporte de Selenium.

Para el backend, se validó el comportamiento del controlador de staff con datos de prueba.

Por ejemplo, la prueba `StaffControllerTest` verifica el comportamiento del controlador de staff con datos de prueba.

![StaffControllerTest](../assets/chapter-6/core-system-tests/StaffControllerTest.png)

En el frontend, se validó el login/registro con campos de prueba y los resultados fueron los esperados.

![testing-frontend](../assets/chapter-6/testing-suites/testing-frontend.png)

## 6.2. Static testing & Verification

La verificación estática revisa el código sin ejecutarlo. En SmartStay se aplicó sobre los cuatro repositorios de la solución (`backend`, `frontend`, `mobile` y `landing-page`) en dos frentes: el cumplimiento de estándares de codificación y la calidad y seguridad del código y de sus dependencias. Las mediciones de esta sección se ejecutaron el **09/11/2026** sobre la rama `main` de los repositorios JavaScript y sobre `develop` en el backend, que es donde reside su pipeline de CI, y se indica de forma explícita cuando una verificación está definida en el pipeline pero no pudo ejecutarse en el equipo donde se redactó este informe.

### 6.2.1. Static Code Analysis

#### 6.2.1.1. Coding standard & Code conventions

El equipo definió en el apartado 5.1.3 las convenciones de codificación por lenguaje. Para comprobar que el código las cumple se asignó una herramienta a cada repositorio:

| Repositorio | Lenguaje | Herramienta de verificación | Configuración | Dónde se ejecuta |
| :--- | :--- | :--- | :--- | :--- |
| `backend` | C# (.NET 9) | `dotnet format --verify-no-changes` | Reglas de formato por defecto del SDK de .NET; `Nullable` habilitado en el proyecto | Job **Lint** de `ci-backend.yml` en cada *push* y *pull request* |
| `frontend` | JavaScript y Vue 3 | ESLint 8.57 con `plugin:vue/vue3-essential` | `.eslintrc.cjs` y script `npm run lint:ci` | Workflow `ci.yml` propuesto en la rama `feature/av2-ci` (pendiente de fusión) y ejecución local |
| `mobile` | Dart (Flutter) | `flutter analyze` con `flutter_lints` 6.0 | `analysis_options.yaml` | Workflow `ci.yml` propuesto en la rama `feature/av2-ci` (pendiente de fusión) |
| `landing-page` | HTML, CSS y JavaScript | Ninguna | No aplica | No aplica |

**Resultado en el frontend web.** El script `lint` que existía en `package.json` no podía ejecutarse, porque ESLint no figuraba entre las dependencias ni había un archivo de configuración. El equipo agregó ESLint 8.57.1, `eslint-plugin-vue` 9.33.0, el archivo `.eslintrc.cjs` y el script `lint:ci`, que verifica sin modificar los archivos (el script `lint` anterior usa `--fix`). La primera ejecución sobre el código del repositorio analizó **205 archivos** y reportó **25 errores y 0 advertencias**.

```text
$ npm run lint:ci
205 archivos analizados · 25 errores · 0 advertencias
```

| Regla de ESLint | Errores | Archivos principales | Interpretación |
| :--- | :---: | :--- | :--- |
| `vue/no-mutating-props` | 15 | `HotelForm.vue` (9), `RoomForm.vue` (6) | Los formularios modifican directamente una *prop* recibida del componente padre. Rompe el flujo de datos de un solo sentido de Vue y debe resolverse con `v-model` sobre una copia local o con eventos `update:`. |
| `no-unused-vars` | 9 | `problem-details.js` (5), `GuestHotels.vue`, `search-availability.query.js`, `booking.entity.js`, `mfa.assembler.js` | Variables o importaciones sin uso. No afectan el comportamiento, pero aumentan el ruido del código. |
| `no-useless-escape` | 1 | `account-rules.js` | Escape innecesario dentro de una expresión regular de validación de contraseña. |

El paso de lint del workflow propuesto para el frontend está configurado con `continue-on-error`. Mientras estos 25 errores estén abiertos, el pipeline los muestra en cada ejecución sin bloquear la integración. Una vez corregidos, la opción se retira para que el lint sea obligatorio.

**Resultado en el backend, el móvil y la landing page.**

- En el **backend**, la verificación de formato forma parte del job *Lint* de `ci-backend.yml`, y el commit `09c2fae` (`style: apply dotnet format whitespace rules`) normalizó el código del repositorio para que el job pasara. Además, el job de compilación usa `--warnaserror`, de modo que cualquier advertencia del compilador detiene el pipeline.
- En la aplicación **móvil**, `analysis_options.yaml` incluye el conjunto `flutter_lints` y solo desactiva la regla `prefer_const_constructors`.
- En la **landing page** no existe ningún linter ni formateador configurado. Se registra como una brecha de verificación y se propone incorporar ESLint con la misma configuración base del frontend.

> **Limitación de esta medición:** el equipo donde se redactó el informe no tiene instalados el SDK de .NET ni el de Flutter, por lo que `dotnet format` y `flutter analyze` no se ejecutaron localmente en esta ocasión. Su resultado queda en el historial de GitHub Actions de cada repositorio, y el de ESLint es el único presentado con números propios.

#### 6.2.1.2. Code Quality & Code Security

La calidad y la seguridad se revisaron en tres niveles: seguridad de las dependencias, higiene de los secretos y calidad estructural del código.

**Seguridad de las dependencias.** Se ejecutó `npm audit` el 09/11/2026 sobre los dos repositorios JavaScript:

| Repositorio | Dependencias analizadas | Vulnerabilidades altas | Vulnerabilidades moderadas | Vulnerabilidades críticas | Corrección disponible |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `frontend` | 288 | 18 | 1 | 0 | Sí, para todas |
| `landing-page` | 79 | 2 | 0 | 0 | Sí, para todas |

En el frontend, los paquetes afectados incluyen `axios`, `follow-redirects`, `form-data`, `@vue/server-renderer` y la familia `@intlify`. En la landing page, `vite` y `source-map-js`. Ninguna es crítica y todas tienen versión corregida, por lo que la acción pendiente es actualizar las dependencias y volver a medir.

En el **backend** el control ya está automatizado: el job *Dependency audit* de `ci-backend.yml` ejecuta `dotnet list package --vulnerable --include-transitive` y falla si encuentra paquetes vulnerables. El commit `f875916` (`fix(deps): patch vulnerable packages and drop unused sqlite provider`) corrigió los paquetes que ese control detectó y eliminó un proveedor de SQLite sin uso.

**Higiene de secretos.** Los repositorios publican únicamente archivos `.env.example` con nombres de variables y sin valores reales, `.env` figura en el `.gitignore` de `backend`, `frontend` y `landing-page` (el de `mobile` aún no lo ignora y debe corregirse), y el `render.yaml` del backend declara los secretos con `sync: false`, de modo que Render los solicita al crear el servicio y no se versionan.

**Calidad estructural.** No se configuró SonarQube ni SonarCloud, porque requieren una cuenta de organización. En su lugar, el equipo se apoyó en controles que no dependen de un servicio externo: tipos anulables habilitados en C#, compilación sin advertencias en CI, análisis de `flutter_lints` y las suites de pruebas automatizadas del backend descritas en 6.1. La incorporación de SonarCloud, con medición de complejidad ciclomática, duplicación y cobertura, queda como mejora recomendada y no se presenta como realizada.

### 6.2.2. Reviews

Las revisiones del equipo se realizan mediante *pull requests* sobre `develop` y `main`, siguiendo GitFlow. La tabla resume el estado real de los *pull requests* de cada repositorio al 09/11/2026, consultado con la API de GitHub:

| Repositorio | Pull requests | Fusionados | Cerrados sin fusionar | Abiertos | Con al menos una revisión registrada |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `backend` | 13 | 12 | 1 | 0 | 1 |
| `frontend` | 6 | 6 | 0 | 0 | 0 |
| `mobile` | 1 | 0 | 0 | 1 | 0 |
| `landing-page` | 4 | 4 | 0 | 0 | 0 |
| `Report` | 2 | 1 | 0 | 1 | 0 |

**Hallazgos de la revisión.**

1. Los *pull requests* se usan de forma consistente para integrar `develop` en `main` (`chore(release): merge develop into main`), pero la revisión entre pares dentro de GitHub es escasa: solo uno de los 26 *pull requests* tiene una revisión registrada. Gran parte de la revisión ocurrió en las reuniones del equipo y no quedó como evidencia en la plataforma.
2. Los controles automáticos sí quedaron como barrera: desde el *pull request* #13 del backend, `render.yaml` usa `autoDeployTrigger: checksPass`, de modo que Render solo despliega a producción después de que los *checks* de CI pasan en `main`.
3. **Acción correctiva acordada:** activar la regla de revisión obligatoria de al menos un integrante en las ramas `develop` y `main` de los cuatro repositorios, para que la revisión entre pares quede registrada en GitHub.

---

<div style="page-break-after: always;"></div>

## 6.3. Validation Interviews

Las entrevistas de validación comprueban con usuarios de los segmentos objetivo si el Landing Page y las aplicaciones permiten completar sus tareas. A diferencia de las entrevistas del Capítulo II, que buscaban entender el problema, estas se realizan con el producto funcionando y miden si las soluciones construidas lo resuelven.

### 6.3.1. Diseño de Entrevistas

**Elementos incluidos en la sesión.** Cada sesión se realiza con el producto desplegado, no con prototipos, para que la evidencia corresponda a lo que el usuario realmente recibirá:

| Elemento | URL |
| :--- | :--- |
| Landing Page | https://smartstay-movildev-landing.vercel.app/ |
| Aplicación web (administrador y huésped) | https://smartstay-movildev-web.vercel.app |
| Aplicación móvil (huésped y staff) | APK de la última versión publicada en el repositorio `mobile` |
| Documentación de la API | https://smartstay-movildev-api.onrender.com/scalar/ |

**Segmento 1: Staff operativo y administradores de hoteles.** Participan de 3 a 5 personas que administren o trabajen en un hotel boutique o pequeño. Los *user flows* a evaluar son:

| # | Tarea | Producto | User Story relacionada |
| :-: | :--- | :--- | :--- |
| 1 | Iniciar sesión como staff con segundo factor de autenticación | Web y móvil | US-02, US-52 |
| 2 | Registrar el hotel y configurar tipos de habitación, habitaciones y precios | Web | US-53 |
| 3 | Cambiar el estado de una habitación a mantenimiento y volverla a disponible | Web | US-06 |
| 4 | Revisar las reservas del día y cancelar una reserva sin pago | Web | US-07 |
| 5 | Crear un usuario de recepción y asignarle su rol | Web | US-03 |
| 6 | Solicitar una demostración desde la landing page | Landing | US-27 |

**Segmento 2: Huéspedes de hoteles boutique.** Participan de 3 a 5 personas que hayan reservado un alojamiento en los últimos doce meses. Los *user flows* a evaluar son:

| # | Tarea | Producto | User Story relacionada |
| :-: | :--- | :--- | :--- |
| 1 | Crear una cuenta y confirmar el correo | Web y móvil | US-01 |
| 2 | Recuperar la contraseña por correo | Web y móvil | US-04 |
| 3 | Buscar una habitación disponible por fechas y reservarla | Web y móvil | US-51 |
| 4 | Pagar la reserva con tarjeta y consultar su estado | Móvil | US-51 |
| 5 | Cancelar una reserva | Móvil | US-07 |
| 6 | Encontrar información de la empresa y testimonios en la landing page | Landing | US-24, US-26, US-28 |

**Guion de la sesión.** Cada sesión dura aproximadamente 30 minutos y se registra en video con el consentimiento expreso del entrevistado:

1. **Apertura (3 min):** el entrevistador explica que se evalúa el producto y no a la persona, y solicita el consentimiento para grabar.
2. **Perfil (3 min):** nombre, edad, distrito, frecuencia de viaje o rol en el hotel, y dispositivos que usa.
3. **Tareas guiadas (15 min):** el entrevistado realiza las tareas de su segmento, pensando en voz alta. El entrevistador no ayuda salvo bloqueo total. En cada tarea se anota si la completó, cuánto tardó y los errores que cometió.
4. **Preguntas de cierre (6 min):** ¿qué fue lo más difícil?, ¿qué esperabas que ocurriera y no ocurrió?, ¿qué cambiarías?, ¿lo usarías en tu día a día?
5. **Cierre (3 min):** el entrevistado califica de 1 a 5 la facilidad de uso y puede añadir comentarios libres.

**Métricas por tarea:** tasa de finalización sin ayuda, tiempo en completarla y número de errores. Los hallazgos se clasifican con la escala de severidad del formato de evaluación heurística de 6.3.3.

### 6.3.2. Registro de Entrevistas

> **Pendiente:** al momento de este avance el equipo no ha realizado las entrevistas de validación con usuarios de los segmentos objetivo, por lo que no se presentan registros. Para cada entrevista realizada se completará la siguiente ficha, con el video grabado, un cuadro del video y un resumen de las apreciaciones del entrevistado.

| Campo | Contenido a registrar |
| :--- | :--- |
| Segmento | Staff operativo / Huésped |
| Entrevistado | Apellidos y nombres, edad y distrito |
| Video | URL del video en Microsoft Stream, minuto de inicio de la entrevista y duración |
| Captura | Cuadro representativo del video |
| Tareas realizadas | Tarea, ¿completada sin ayuda?, tiempo y errores |
| Resumen | Apreciaciones principales del entrevistado sobre las tareas asignadas |

### 6.3.3. Evaluaciones según heurísticas

> **Pendiente:** esta evaluación se completa a partir de las sesiones de 6.3.2. Se utilizará el formato **UX Heuristics & Principles Evaluation** del Anexo D del enunciado del trabajo final, que se estructura como sigue.

| Sección del formato | Contenido |
| :--- | :--- |
| Encabezado | Carrera, curso, NRC, profesores, auditor (SmartStay Team) y clientes que participan en la sesión |
| Site o app a evaluar | Landing Page, aplicación web y aplicación móvil de SmartStay |
| Tareas a evaluar | Las tareas de 6.3.1; quedan fuera del alcance los flujos del Sprint 3 aún no desplegados |
| Escala de severidad | 1 = problema superficial, 2 = problema menor, 3 = problema mayor, 4 = problema muy grave |
| Tabla resumen | Problema encontrado, severidad y heurística o principio violado (usabilidad, diseño inclusivo o arquitectura de información) |
| Detalle por problema | Tarea, descripción, evidencia en captura y recomendación |

---

<div style="page-break-after: always;"></div>

## 6.4. Auditoría de Experiencias de Usuario

La auditoría de experiencias de usuario es una evaluación cruzada entre grupos: SmartStay audita el producto de otro grupo y recibe la auditoría de un tercero sobre el suyo. Cada auditoría evalúa los productos desplegados con el formato de evaluación heurística del Anexo D del enunciado.

> **Pendiente:** al momento de este avance el grupo no tiene asignado un grupo auditado ni ha recibido una auditoría. Las secciones siguientes se completan cuando se coordine el intercambio, y no se presentan datos de auditoría hasta contar con ellos.

### 6.4.1. Auditoría realizada

#### 6.4.1.1. Información del grupo auditado

Se registrará el nombre de la startup auditada, el nombre de su producto, sus integrantes y las URL de los productos evaluados.

#### 6.4.1.2. Cronograma de auditoría realizada

Se registrará la fecha, la hora, la modalidad y los participantes de cada sesión de auditoría.

#### 6.4.1.3. Contenido de auditoría realizada

Se incluirá el formato de evaluación heurística completo con las tareas evaluadas, los problemas encontrados, su severidad y la heurística o principio violado.

### 6.4.2. Auditoría recibida

#### 6.4.2.1. Información del grupo auditor

Se registrará el nombre del grupo que audita a SmartStay, sus integrantes y el contacto de coordinación.

#### 6.4.2.2. Cronograma de auditoría recibida

Se registrará la fecha, la hora, la modalidad y los participantes de cada sesión.

#### 6.4.2.3. Contenido de auditoría recibida

Se incluirá el formato de evaluación heurística recibido, con los problemas reportados sobre el Landing Page y las aplicaciones de SmartStay.

#### 6.4.2.4. Resumen de modificaciones para subsanar hallazgos

Se presentará una tabla que relacione cada hallazgo recibido con el cambio realizado en el producto, el commit que lo implementó y el estado de la corrección.
