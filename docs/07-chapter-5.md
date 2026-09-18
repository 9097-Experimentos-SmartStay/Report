# Capítulo V: Product Implementation

## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

### Project Management
Para la gestión del proyecto se emplearon diversas herramientas de comunicación, planificación y control de versiones. Se creó una organización en GitHub para centralizar el repositorio del código fuente y coordinar el trabajo colaborativo del equipo. La comunicación interna se realizó mediante Discord y WhatsApp, mientras que la planificación ágil de tareas se gestionó a través de Trello.

- **Organización del trabajo:** GitHub
- **Reuniones:** Discord
- **Comunicación:** WhatsApp
- **Planificación y asignación de tareas:** Trello
- **Control de versiones:** Git con GitFlow workflow
- **Gestión de Product Backlog y Sprint Backlog:** Trello

**Enlaces**  
-**GitHub:** [GitHub](https://github.com/)  
-**Discord:** [Discord](https://discord.com/)  
-**Trello:** [Trello](https://trello.com/)

### Herramienta de soporte a Agile Development - Trello

**Trello** se utiliza como la herramienta principal para la gestión ágil del proyecto, soportando la metodología Scrum mediante tableros Kanban personalizados.

**Configuración del tablero Trello para Smart Stay:**

**Estructura de listas (columnas):**
1. **Product Backlog:** User Stories priorizadas pendientes de asignación
2. **Sprint Backlog:** User Stories seleccionadas para el Sprint actual
3. **To Do:** Engineering Tasks listas para comenzar
4. **In Process:** Tasks en desarrollo activo
5. **To Review:** Tasks completadas pendientes de revisión
6. **Done:** Tasks completadas y revisadas

**Elementos de las tarjetas (cards):**
- **Título:** Identificador de la User Story o Engineering Task (ej: US-24, UT-01)
- **Descripción:** Detalle completo de la funcionalidad o tarea
- **Labels (etiquetas):**
  - `Frontend` - Tareas de desarrollo frontend
  - `Backend` - Tareas de desarrollo backend
  - `Documentation` - Tareas de documentación
  - `Bug` - Correcciones de errores
  - `Enhancement` - Mejoras de funcionalidades existentes
  - `High Priority` - Tareas de alta prioridad
- **Miembros asignados:** Responsables de la tarea
- **Checklist:** Subtareas o criterios de aceptación
- **Estimación:** Horas estimadas (4-8 horas por Engineering Task)
- **Due date:** Fecha límite de entrega
- **Attachments:** Mockups, diagramas, enlaces relacionados

**Workflow de gestión:**

1. **Sprint Planning:**
   - Se mueven User Stories del Product Backlog al Sprint Backlog
   - Se descomponen en Engineering Tasks específicas
   - Se asignan responsables y se estiman en horas (4-8 horas máximo)

2. **Daily Development:**
   - Los miembros mueven sus tasks de To Do → In Process al comenzar
   - Actualizan el progreso mediante comentarios
   - Marcan subtareas completadas en checklists

3. **Code Review:**
   - Al completar, se mueve a To Review
   - Otro miembro del equipo revisa y valida
   - Si aprueba, se mueve a Done
   - Si requiere cambios, regresa a In Process

4. **Sprint Review:**
   - Se verifica que todas las tasks del Sprint estén en Done
   - Se documenta el resultado del Sprint
   - Se prepara el siguiente Sprint Backlog

**Integración con GitHub:**
- Enlaces en tarjetas Trello hacia Pull Requests relacionados
- Referencia de números de issue en descripciones
- Sincronización manual de estados entre Trello y GitHub Projects

**Métricas de seguimiento:**
- **Burndown chart:** Seguimiento manual del progreso del Sprint
- **Velocity:** Calculado al finalizar cada Sprint
- **Task completion rate:** Porcentaje de tasks completadas vs planificadas

**Evidencia de uso:**
![Tablero de Trello del sprint](../assets/chapter-5/project-management/trello-board.jpg)
*Tablero Trello del Sprint 1 mostrando la organización de tareas*

![Detalle del tablero de Trello](../assets/chapter-5/project-management/trello-board-detail.jpg)
*Tablero Trello del Sprint 2 con Engineering Tasks en progreso*


### Requirement Management
Para la fase de levantamiento y priorización de requisitos, se implementaron herramientas que facilitaron la recolección, análisis y documentación de información. Trello fue empleado para la gestión visual de tareas mediante tableros personalizados.  
Además, se utilizó **UXPressia** para el desarrollo de *User Personas*, *Empathy Maps*, *Journey Maps* y *Lean UX Canvas*, mientras que **Miro** sirvió para construir los escenarios *As-Is* y *To-Be* de los procesos del sistema.

**Enlaces**  
-**Trello:** [Trello](https://trello.com/)  
-**UXPressia:** [UXPressia](https://uxpressia.com/)  
-**Miro:** [Miro](https://miro.com/es/)



### Product UX/UI Design
Durante el diseño de la experiencia e interfaz de usuario, el equipo utilizó **Figma** para crear *wireframes*, *mockups* y *prototipos interactivos*, lo cual permitió validar las propuestas de diseño antes de su implementación final.  
Asimismo, se aplicaron principios de usabilidad y diseño centrado en el usuario para garantizar una navegación fluida y consistente.

**Enlaces**  
-**Figma:** [Figma](https://www.figma.com/)



### Software Development
Para el desarrollo de la aplicación se utilizaron distintas herramientas y entornos de programación enfocados en el desarrollo backend y móvil.  

El backend fue implementado con **ASP.NET Core (C#)** empleando el IDE **JetBrains Rider**, permitiendo gestionar la lógica de negocio y los servicios del sistema mediante APIs REST.  

Por otro lado, el desarrollo móvil se realizó utilizando **Android Studio**, **Kotlin** y **Flutter**, tecnologías empleadas para implementar las aplicaciones dirigidas al huésped y al staff operativo. Asimismo, se utilizó **Firebase** para servicios de autenticación y notificaciones móviles.  

Adicionalmente, se empleó **MySQL** como sistema de gestión de base de datos y **Azure** para el despliegue y administración de los servicios backend.  

Finalmente, el proyecto se apoyó en herramientas de control de versiones como **Git y GitHub**, mientras que la instalación y mantenimiento de las IDEs se realizó mediante **JetBrains ToolBox**.

**Enlaces**  
- **JetBrains ToolBox:** [JetBrains ToolBox](https://www.jetbrains.com/toolbox-app/)  
- **JetBrains Rider:** [JetBrains Rider](https://www.jetbrains.com/rider/)  
- **Android Studio:** [Android Studio](https://developer.android.com/studio)  
- **Flutter:** [Flutter](https://flutter.dev/)  
- **Kotlin:** [Kotlin](https://kotlinlang.org/)  
- **Firebase:** [Firebase](https://firebase.google.com/)  
- **MySQL:** [MySQL](https://www.mysql.com/)  
- **Azure:** [Azure](https://azure.microsoft.com/)  
- **GitHub:** [GitHub](https://github.com/)


### Software Documentation
Para la documentación técnica y la gestión del repositorio, se utilizó **GitHub** siguiendo la metodología de trabajo **GitFlow**.  
Esta estrategia permitió un control de versiones eficiente mediante el uso de ramas específicas para funcionalidades, correcciones y despliegues del proyecto.  
Toda la documentación se redactó en formato **Markdown (.md)**, debido a su legibilidad, simplicidad y compatibilidad con GitHub.

**Enlaces**  
- **GitHub:** [GitHub](https://github.com/)

### Software Deployment
El despliegue de los servicios backend se realizó mediante **Microsoft Azure**, permitiendo alojar las APIs REST y garantizar la comunicación entre las aplicaciones móviles, la base de datos y los servicios IoT del sistema Smart Stay.  
Asimismo, las aplicaciones móviles fueron ejecutadas y validadas utilizando **Android Studio Emulator** y dispositivos físicos Android para verificar el correcto funcionamiento de las funcionalidades desarrolladas.

**Enlaces**  
- **Azure:** [Azure](https://azure.microsoft.com/)  
- **Android Studio:** [Android Studio](https://developer.android.com/studio)



### 5.1.2. Source Code Management

### Repositorios del proyecto
El proyecto está organizado dentro de una **organización en GitHub**, donde cada módulo cuenta con su propio repositorio según su propósito y tecnología.

**Repositorios individuales de control de versiones:**

- **Aplicación Móvil:**  
  - **Tecnología:** Kotlin (Android Native)
  - **IDE:** Android Studio
  - **URL del repositorio:** https://github.com/9097-Experimentos-SmartStay/mobile
  - **Plataforma de despliegue:** Android Studio Emulator / APK Testing

- **Web Services (Backend):**  
  - **Tecnología:** ASP.NET Core (C#)
  - **URL del repositorio:** https://github.com/9097-Experimentos-SmartStay/backend
  - **Arquitectura:** RESTful API
  - **Plataforma de despliegue:** Render

- **Frontend Web:**
  - **Tecnología:** Vue.js
  - **URL del repositorio:** https://github.com/9097-Experimentos-SmartStay/frontend
  - **Plataforma de despliegue:** Vercel

- **Landing Page**
  - **Tecnología:** HTML, CSS, JavaScript
  - **URL del repositorio:** https://github.com/9097-Experimentos-SmartStay/landing-page
  - **IDE:** WebStorm
  - **Plataforma de despliegue:** Vercel

Todos los repositorios implementan el modelo **GitFlow** como flujo de trabajo de colaboración y branching, garantizando un desarrollo ordenado y trazable.

---

### Flujo de trabajo de GitFlow
El flujo de trabajo del proyecto se basa en el modelo **“A Successful Git Branching Model”**, el cual organiza el proceso de desarrollo mediante ramas específicas para cada funcionalidad o corrección.  
Este enfoque permite un control de versiones ordenado y un desarrollo paralelo seguro.

**Diagrama del flujo GitFlow implementado:**

```text
main (producción)
 |
 |---- release/v1.0.0
 |          |
develop    |
 |         |
 |---- feature/user-authentication
 |         |
 |         (desarrollo)
 |         |
 |<-------- (merge)
 |
 |---- feature/room-management
 |         |
 |         (desarrollo)
 |         |
 |<-------- (merge)
 |
 |---- hotfix/critical-bug
 |         |
 |         (corrección)
 |         |
 |<-------- (merge a develop)
 |         |
main <---- (merge a main)
```
---
### Proceso de trabajo con GitFlow

1. **Desarrollo de nuevas funcionalidades:**
   - Se crea una rama `feature/<nombre-funcionalidad>` desde `develop`
   - Se desarrolla y prueba la funcionalidad
   - Se realiza merge a `develop` mediante Pull Request con revisión de código
   - Se elimina la rama feature tras la integración exitosa

2. **Preparación de versiones:**
   - Se crea una rama `release/<version>` desde `develop`
   - Se realizan ajustes finales y correcciones menores
   - Se realiza merge a `main` y se etiqueta la versión
   - Se realiza merge de vuelta a `develop` para mantener sincronización

3. **Correcciones críticas en producción:**
   - Se crea una rama `hotfix/<descripcion>` desde `main`
   - Se corrige el problema de forma urgente
   - Se realiza merge a `main` y `develop`
   - Se etiqueta la nueva versión de corrección

### Estructura de branches (Ramas)

**Main branch (Rama principal):**  
Es la rama principal del proyecto, donde se almacena el código estable y listo para producción.  
Solo se integran cambios que hayan sido probados y validados previamente en las ramas de desarrollo (*develop*) y funcionalidad (*feature/*).  
Esta rama representa el estado más confiable del proyecto y se encuentra protegida con reglas de revisión obligatoria.

**Develop branch (Rama de desarrollo):**  
Actúa como un espacio de integración para el trabajo en equipo.  
Aquí se combinan, prueban y ajustan las nuevas funcionalidades antes de ser fusionadas con la rama principal (*main*).  
Su propósito es garantizar que el código integrado sea funcional y estable antes del despliegue.

**Feature branches (Ramas de funcionalidad):**  
Cada nueva funcionalidad o tarea específica se desarrolla en su propia rama independiente.  
Una vez completada y verificada, se integra nuevamente en la rama de desarrollo (*develop*) mediante Pull Request.

Las ramas de funcionalidad siguen un esquema de nombres descriptivos, como por ejemplo:

- `feature/chapter-01` - Documentación del Capítulo I
- `feature/chapter-02` - Documentación del Capítulo II
- `feature/chapter-03` - Documentación del Capítulo III
- `feature/chapter-04` - Documentación del Capítulo IV
- `feature/chapter-05` - Documentación del Capítulo V
- `feature/user-authentication` - Sistema de autenticación
- `feature/room-management` - Gestión de habitaciones
- `feature/booking-system` - Sistema de reservas

**Release branches (Ramas de versión):**  
Se crean para preparar una nueva versión de producción desde `develop`.

- `release/v1.0.0` - Primera versión estable
- `release/v1.1.0` - Versión con nuevas funcionalidades

**Hotfix branches (Ramas de corrección urgente):**  
Se crean desde `main` para corregir problemas críticos en producción.

- `hotfix/login-security` - Corrección de seguridad en login
- `hotfix/payment-error` - Corrección de error en pagos

### Evidencia de aplicación de GitFlow

**Repositorio Mobile App:**

- Ramas activas: `main`, `develop`, `feature/responsive-design`, `feature/multilanguage`
- Commits con convenciones: `feat:`, `fix:`, `docs:`
- Pull Requests con revisiones de código

**Repositorio Backend:**

- Ramas activas: `main`, `develop`, `feature/api-rooms`, `feature/api-bookings`
- Versionado semántico aplicado
- Tags: `v1.0.0`, `v1.1.0`


### 5.1.3. Source Code Style Guide &amp; Conventions

### HTML / CSS

- [HTML Style Guide and Coding Conventions](https://www.w3schools.com/html/html5_syntax.asp)
- [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)

**Convenciones aplicadas:**
- Uso de etiquetas **semánticas** para mejorar la estructura, accesibilidad y SEO del sitio.
- Clases CSS escritas en **kebab-case**, por ejemplo: `.main-header`, `.card-title`.
- Identificadores claros, descriptivos y consistentes.
- Organización modular del código mediante hojas de estilo separadas por componente o sección

### Vue.js

- [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
- [W3C JavaScript Best Practices](https://www.w3.org/wiki/JavaScript_best_practices)
- [MDN JavaScript Guidelines](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Vue Style Guide](https://vuejs.org/style-guide/)

**Prácticas adoptadas:**
- Código escrito en **ES6+**, priorizando claridad y modularidad.
- Uso de **CamelCase** para variables y funciones.
- Componentes de Vue nombrados en **PascalCase**.
- Implementación de **ESLint** y **Prettier** para análisis estático y formateo automático del código.
- Uso del principio **DRY (Don’t Repeat Yourself)** para evitar duplicaciones.

### C# y ASP.NET Core

- [C# Coding Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [Microsoft ASP.NET Core Coding Guidelines](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-7.0)

**Convenciones aplicadas:**
- Uso de **PascalCase** para clases, interfaces y métodos públicos.
- Uso de **camelCase** para variables locales y parámetros.
- Organización del código en **namespaces** coherentes con la arquitectura del proyecto.
- Comentarios XML para documentación interna de métodos y controladores.
- Pruebas unitarias y escenarios escritos siguiendo la convención **Gherkin (Given-When-Then)**.

### Kotlin (Android Studio)

- [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html)
- [Android Developers Guidelines](https://developer.android.com/kotlin/style-guide)

**Convenciones aplicadas:**

- Uso de **PascalCase** para clases y actividades (`LoginActivity`, `RoomManagementActivity`).
- Uso de **camelCase** para variables, funciones y parámetros (`guestName`, `validateLogin()`).
- Organización modular del código por paquetes (`activities`, `services`, `models`, `adapters`).
- Uso de nombres descriptivos y consistentes para layouts XML y recursos visuales.
- Implementación de buenas prácticas de desarrollo Android para mejorar mantenibilidad y escalabilidad.

**Componentes utilizados en la aplicación móvil:**

- `Activity`: Maneja las pantallas principales de la aplicación.
- `Fragment`: Permite reutilizar componentes visuales dentro de distintas vistas.
- `RecyclerView`: Muestra listas dinámicas de habitaciones, reservas o servicios.
- `Intent`: Gestiona la navegación entre pantallas.
- `ViewModel`: Administra el estado y la lógica de presentación.
- `Firebase`: Gestiona autenticación y notificaciones móviles.
- `XML Layouts`: Define la estructura visual de las interfaces móviles.

---

### 5.1.4. Software Deployment Configuration

### Landing Page Deployment
La **Landing Page** fue desarrollada utilizando **HTML**, **CSS** y **JavaScript**, y se encuentra desplegada públicamente a través de **Vercel**.  
Para su publicación, se cumplieron los siguientes pasos:

1. **Preparación del entorno:**  
   Se creó un repositorio dentro de la organización en **GitHub**, destinado a alojar los archivos de la Landing Page.

2. **Estructura de archivos:**  
   Los archivos principales se encuentran en la raíz del repositorio, siguiendo las convenciones de nombres:
    - `index.html` → página principal.
    - `styles.css` → hoja de estilos principal.
    - `script.js` → scripts principales.
    - `languages.js` → archivo para gestionar los textos en distintos idiomas (español e inglés).
    - Carpeta `assets/images/` → para las imágenes utilizadas en el sitio.

3. **Configuración en Vercel:**
    - Se importó el repositorio de la Landing Page directamente desde GitHub a **Vercel**.
    - Se seleccionó la rama **main** como fuente de publicación.
    - Se configuró la carpeta raíz (`/`) como directorio base del proyecto.
    - Una vez completado el proceso, Vercel generó automáticamente la URL pública de la Landing Page.

Además, se implementó un archivo `languages.js` que contiene los textos en español e inglés.  
Este archivo es consumido por el script `main.js`, permitiendo el cambio de idioma dinámico en la interfaz.


### Backend (Web Services)
El **backend** fue desarrollado en **ASP.NET Core con C#**, siguiendo el estilo arquitectónico **RESTful**.  
Su despliegue se realizó en la plataforma **Render**, configurada como un servicio *cloud* para ejecutar la API de forma continua.  
Esto permite mantener el servicio activo, escalable y sincronizado con el repositorio de GitHub.


### Frontend Web Application
La **aplicación web frontend** fue construida con **Vue.js** y **PrimeVue**, integrando una interfaz moderna e interactiva.  
El despliegue se llevó a cabo en **Vercel**, aprovechando su integración con GitHub para habilitar un flujo de despliegue automático.  
Cada actualización en la rama `main` desencadena una nueva versión publicada en producción.


### Integración Continua / Despliegue Continuo (CI/CD)
El proyecto implementa un flujo automatizado de **Integración Continua y Despliegue Continuo (CI/CD)**, con el objetivo de mantener la coherencia entre los entornos de desarrollo y producción.

- Todos los repositorios están conectados directamente a **GitHub**.
- **Render** ejecuta el despliegue automático del backend, y **Vercel** el del frontend web y la landing page, al detectarse *merges* en la rama `main`.
- Este proceso garantiza una actualización constante de los servicios y minimiza la intervención manual en las publicaciones.

### Vercel (Landing Page):
![Vercel Deployment](../assets/chapter-5/deployment/github-pages.jpg)
> ⚠️ Imagen pendiente de reemplazo: la captura actual corresponde a la configuración antigua de GitHub Pages, no al dashboard de Vercel.

**La URL pública de la landing page es la siguiente:**  
[https://smartstay-movildev-landing.vercel.app/](https://smartstay-movildev-landing.vercel.app/)

---

El despliegue de la solución considera los siguientes aspectos generales, los cuales garantizan la disponibilidad y correcta operación de los distintos componentes del sistema.

### Mobile Application Deployment

La aplicación móvil fue desarrollada utilizando **Kotlin** en **Android Studio**, siguiendo una arquitectura orientada al desarrollo de aplicaciones Android nativas.  

Para la ejecución y validación de la aplicación, se utilizaron las siguientes herramientas y configuraciones:

1. **Preparación del entorno:**  
   Se configuró el entorno de desarrollo mediante **Android Studio**, incluyendo el SDK de Android, emuladores y dependencias necesarias para la compilación de la aplicación.

2. **Estructura del proyecto:**  
   El proyecto móvil se organiza siguiendo buenas prácticas de Android Development:
   - `activities/` → pantallas principales de la aplicación.
   - `adapters/` → manejo de listas dinámicas y RecyclerViews.
   - `models/` → clases de entidades y estructuras de datos.
   - `services/` → conexión con APIs REST y servicios externos.
   - `res/layout/` → archivos XML de las interfaces visuales.
   - `assets/` → recursos gráficos e imágenes utilizadas en la aplicación.

3. **Compilación y ejecución:**
   - La aplicación se ejecuta mediante **Android Emulator** y dispositivos físicos Android.
   - Android Studio genera automáticamente los archivos APK necesarios para pruebas e instalación.
   - Las versiones de prueba son administradas mediante GitHub y control de versiones GitFlow.

4. **Servicios integrados:**
   - Integración con APIs RESTful desarrolladas en ASP.NET Core.
   - Uso de Firebase para autenticación y notificaciones móviles.
   - Comunicación con servicios backend para reservas, habitaciones y gestión operativa.

### Backend (Web Services)

El backend fue desarrollado en **ASP.NET Core con C#**, siguiendo el estilo arquitectónico **RESTful**.  
Su despliegue se realizó en la plataforma **Render**, configurada como un servicio cloud para ejecutar la API de forma continua.  

Esto permite mantener el servicio activo, escalable y sincronizado con el repositorio de GitHub.

### Integración Continua / Despliegue Continuo (CI/CD)

El proyecto implementa un flujo automatizado de **Integración Continua y Despliegue Continuo (CI/CD)**, con el objetivo de mantener la coherencia entre los entornos de desarrollo y prueba.

- Todos los repositorios están conectados directamente a **GitHub**.
- Render ejecuta el despliegue automático al detectarse merges en la rama `main`.
- El control de versiones se realiza utilizando Git y GitFlow.
- Las versiones móviles son compiladas y probadas desde Android Studio antes de cada entrega.

### Android Studio Emulator

![Android Studio Emulator](../assets/chapter-5/deployment/android-studio-emulator.jpg)

**El emulador de Android Studio permite validar el funcionamiento de la aplicación móvil en distintos dispositivos y versiones de Android antes de su despliegue final.**

---

## 5.2. Product Implementation &amp; Deployment

### 5.2.1. Sprint Backlogs

#### 5.2.1.1. Sprint 1 

A continuación, se presenta el Sprint Planning 1, en el que se incluyen las evidencias de la planificación y desarrollo del Landing Page. Asimismo, se documentan los avances del proyecto y los insights de colaboración del equipo registrados a través de GitHub.

##### 5.2.1.1.1. Sprint Planning 1


| **Sprint #**                           | Sprint 1                                                                                                                                                                                                                                                      |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sprint Planning Background**         | Reunión inicial de planificación del proyecto **SmartStay**, orientada a establecer los objetivos del primer sprint y asignar las tareas relacionadas con el diseño, desarrollo y despliegue de la Landing Page.                                              |
| **Date**                               | 2026-04-30                                                                                                                                                                                                                                                    |
| **Time**                               | 05:00 PM (GMT -5)                                                                                                                                                                                                                                             |
| **Location**                           | Modalidad remota mediante **Discord**                                                                                                                                                                                                                         |
| **Prepared By**                        | Equipo **SmartStay**                                                                                                                                                                                                                                          |
| **Attendees (to planning meeting)**    | Verona Flores, Italo Sebastián                                                                                                 |
| **Sprint n – 1 Review Summary**        | Este es el primer sprint del proyecto, por lo tanto, no existe una revisión de sprint anterior.                                                                                                                                                               |
| **Sprint n – 1 Retrospective Summary** | Al ser la primera iteración, no se registran retrospectivas previas. No obstante, se acordó la importancia de establecer lineamientos claros de trabajo colaborativo, mantener una comunicación efectiva y un uso disciplinado de las herramientas definidas. |
| **Sprint Goal & User Stories**         | —                                                                                                                                                                                                                                                             |
| **Sprint n Goal**                      | Publicar una **Landing Page funcional** para SmartStay, con diseño responsive, estructura clara y accesible desde GitHub Pages. A ello le sumamos el despliegue de nuestro backend así como la versión inicial de nuestra APK funcional.                     |
| **Sprint n Velocity**                  | 2                                                                                                                                                                                                                                                             |
| **Sum of Story Points**                | 2                                                                                                                                                                                                                                                             |



##### 5.2.1.1.2. Sprint Backlog 1 

###### Introduccion

El objetivo principal del Sprint 1 es publicar una Landing Page funcional para SmartStay, con diseño responsive, estructura clara y accesible desde GitHub Pages, junto con la versión inicial de nuestra APK funcional.
Este Sprint está enfocado en establecer la presencia digital oficial del proyecto, ofreciendo a los visitantes una primera experiencia atractiva, profesional e intuitiva que les permita conocer el producto, sus beneficios y facilidades de acceso, mientras se avanza paralelamente en la aplicación móvil.

### Sprint #1 – Sprint Backlog

| **Sprint #** | **User Story**                             | **Work-Item/Task**       | **Id**                              | **Title**                                                                                                    | **Description**          | **Estimation (Hours)** | **Assigned To** | **Status**    |
|--------------|--------------------------------------------|--------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------|------------------------|-----------------|---------------|
| Sprint 1     | US-24 – Segmented landing page             | UT-01                    | Diseñar estructura visual           | Crear la estructura general de la Landing Page con secciones diferenciadas para administradores y huéspedes. | 6                        | Italo Sebastián        | Done            |
| Sprint 1     | US-24 – Segmented landing page             | UT-02                    | Maquetar Landing Page               | Implementar el diseño HTML y CSS del prototipo base.                                                         | 5                        | Italo Sebastián        | In Process      |
| Sprint 1     | US-24 – Segmented landing page             | UT-03                    | Navegación y enlaces internos       | Configurar navegación entre secciones con enlaces y smooth scroll.                                           | 3                        |            | Done            |
| Sprint 1     | US-26 – Success stories and testimonials   | UT-04                    | Crear sección de testimonios        | Diseñar carrusel con testimonios de usuarios y animaciones simples.                                          | 4                        |             | To Review       |
| Sprint 1     | US-27 – Demo request and contact           | UT-05                    | Formulario de contacto              | Implementar formulario con validación y diseño responsive.                                                   | 4                        |            | Done            |
| Sprint 1     | US-28 – Corporate information              | UT-06                    | Redactar misión, visión y valores   | Escribir texto institucional coherente con la marca Smart Stay.                                              | 3                        |            | Done            |
| Sprint 1     | US-28 – Corporate information              | UT-07                    | Implementar sección “About Us”      | Maquetar la sección con texto e imagen representativa.                                                       | 4                        | Italo Sebastián        | To Do           |
| Sprint 1     | US-24 – Segmented landing page             | UT-08                    | Añadir botones CTA                  | Colocar botones visibles con enlaces a las rutas de autenticación.                                           | 3                        |          | Done            |
| Sprint 1     | US-26 – Success stories and testimonials   | UT-09                    | Ajustar animaciones y transiciones  | Aplicar efectos de entrada y desplazamiento fluido en los testimonios.                                       | 4                        |             | In Process      |
 

##### 5.2.1.1.3. Development Evidence for Sprint Review

Durante el desarrollo del sprint, el equipo trabajó de manera distribuida en los distintos repositorios del ecosistema **SmartStay**, incluyendo el Project Report, Landing Page, Mobile Application, Backend y APK. Para evidenciar el avance realizado, se presenta el siguiente cuadro de commits obtenidos de los repositorios oficiales del proyecto en GitHub.

| Repositorio | Commit | Autor | Fecha | Rama/Referencia | Mensaje |
|---|---|---|---|---|---|
| Project Report | f42fb3c |  | 2026-05-15 | main | Docs: Update README with Sprint 1 execution details |
| Project Report | aa4d72f | atomdragon1318 | 2026-05-14 | main | docs: add Lean UX Canvas image and update related section in README |
| Project Report | 95ab6ee |  | 2026-05-13 | main | Update README with APK repository URL |
| Project Report | 4dcbc6c | atomdragon1318 | 2026-05-13 | main | doc: Add new asset images for application UI |
| Project Report | bae57ee |  | 2026-05-13 | main | docs: add Development Evidence for Sprint Review, evidencia de la Suite de Pruebas para la Revisión del Sprint and Services Documentation Evidence for Sprint Review |
| Project Report | c62b7ed | atomdragon1318 | 2026-05-13 | main | Docs: Add Android Studio emulator image to Chapter IIII |
| Project Report | 3a74b48 | atomdragon1318 | 2026-05-13 | main | Docs: Add Lean UX Canvas image to Chapter I |
| Project Report | b7ac279 | atomdragon1318 | 2026-05-12 | main | doc(fix): name of the image |
| Project Report | e9d3771 | atomdragon1318 | 2026-05-12 | main | Docs: Add interview images for hotel management application, conclusions, recommendations and glossary. |
| Project Report | 4f67ff2 |  | 2026-05-06 | main | Docs: Document Sprint 1 achievements for SmartStay |
| Project Report | 7865141 |  | 2026-05-06 | main | Docs: Refactor README with deployment details and formatting |
| Project Report | 049fc66 |  | 2026-05-06 | main | Docs: Revise repository links and feature branch names |
| Project Report | c880cc3 |  | 2026-05-06 | main | Docs: Document project repositories and GitFlow process |
| Project Report | e5c4ed9 |  | 2026-05-06 | main | Docs: Enhance README with project management details |
| Landing Page | a87eacb | atomdragon1318 | 2026-05-08 | main | feat: add success stories section with metrics and testimonials |
| Landing Page | 711f5c8 | atomdragon1318 | 2026-05-06 | main | fix: remove nickname from team member name for consistency |
| Landing Page | dee64e0 | atomdragon1318 | 2026-05-06 | main | feat(translator): enhance translation loading and application logic |
| Landing Page | 1253f31 | atomdragon1318 | 2026-05-04 | main | fix: hide scrollbar in carousel track for cleaner appearance |
| Landing Page | f29f340 | atomdragon1318 | 2026-05-04 | main | feat: add image to member, delete video about the team |
| Landing Page | 32e2e01 | atomdragon1318 | 2026-05-04 | main | chore: add initial files and landing page |
| APK | 73fa084 |  | 2026-05-13 | main | Add SmartStay demo APK |
| APK | 5e82d86 |  | 2026-05-13 | main | Add README for SmartStay APK demo |
| Mobile Application | f204803 | atomdragon1318 | 2026-05-24 | main | feat: implement authentication feature with session management and API integration |
| Mobile Application | b47b9cb | atomdragon1318 | 2026-05-24 | main | feat: implement accommodation feature with API service, repository, and UI components |
| Mobile Application | 0d05b15 | atomdragon1318 | 2026-05-24 | main | feat: add device manager configuration and update library versions |
| Mobile Application | 7c52949 | atomdragon1318 | 2026-06-04 | main | feat: add admin and housekeeping dashboard screens with navigation setup |
| Mobile Application | f58b708 | atomdragon1318 | 2026-06-12 | main | feat: refactor authentication module and update navigation structure |
| Mobile Application | 70159fc | atomdragon1318 | 2026-06-14 | main | feat(iam): implement TokenManager and user models for authentication flow |
| Mobile Application | 10f486b | atomdragon1318 | 2026-06-16 | main | feat(profile): implement profile management features including creation, listing, and repository integration |
| Mobile Application | a1f9bc4 | atomdragon1318 | 2026-06-16 | main | feat(user): update user permissions to include 'admin' role for management and visibility |
| Backend | d9624bc | atomdragon1318 | 2026-06-06 | main | Initial commit |
| Backend | ad84235 | atomdragon1318 | 2026-06-06 | main | feat: Update .gitignore to include artifacts directory |
| Backend | f5bf82d | atomdragon1318 | 2026-06-06 | main | feat: Add health checks for MySQL database connection |
| Backend | 35dd913 | atomdragon1318 | 2026-06-09 | main | feat: Refactor user authentication and booking commands with improved exception handling |
| Backend | 6b58992 | atomdragon1318 | 2026-06-10 | main | feat(IAM): Implement role and user scope authorization services for enhanced user management |
| Backend | 11a1921 | atomdragon1318 | 2026-06-11 | main | feat(IAM): Enhance user sign-up and authentication with role assignment and actor validation |
| Backend | 6e63cfc | atomdragon1318 | 2026-06-15 | main | feat(IAM): Enhance user authentication and authorization with token versioning and improved error handling |
| Backend | e2c761d | atomdragon1318 | 2026-06-16 | main | feat(IAM): Implement user account activation functionality with command and controller support |

La evidencia demuestra que el equipo realizó avances en los principales componentes del proyecto. En el repositorio del informe se documentaron los avances del sprint; en la Landing Page se implementaron mejoras visuales, traducción y secciones informativas; en el repositorio APK se publicó una versión demo de la aplicación; en la Mobile Application se desarrollaron funcionalidades de autenticación, perfiles y navegación; y en el Backend se implementaron servicios relacionados con IAM, seguridad, base de datos y configuración de infraestructura.

##### 5.2.1.1.4. Testing Suite Evidence for Sprint Review

Durante el sprint, se realizaron pruebas sobre los distintos componentes del ecosistema **SmartStay** con el objetivo de validar el correcto funcionamiento de la Landing Page, la aplicación móvil, el backend y la APK demo. Las pruebas se organizaron según la tecnología utilizada en cada repositorio.

| Repositorio | Tipo de prueba | Herramienta / Comando | Elemento evaluado | Resultado esperado | Estado |
|---|---|---|---|---|---|
| Landing Page | Prueba unitaria | Jest / `npm test` | Renderizado de la página principal | La Landing Page carga correctamente sin errores. | Aprobado |
| Landing Page | Prueba unitaria | Jest / `npm test` | Botones CTA | Los botones principales se visualizan correctamente y redireccionan a las secciones correspondientes. | Aprobado |
| Landing Page | Prueba unitaria | Jest / `npm test` | Cambio de idioma | Los textos cambian correctamente entre los idiomas configurados. | Aprobado |
| Landing Page | Prueba de interfaz | Navegador web | Diseño responsive | La Landing Page se adapta correctamente a vista desktop y móvil. | Aprobado |
| Mobile Application | Prueba unitaria | Gradle / `./gradlew test` | Flujo de autenticación | La lógica de autenticación procesa correctamente credenciales y sesión de usuario. | Aprobado |
| Mobile Application | Prueba unitaria | Gradle / `./gradlew test` | Gestión de perfiles | El módulo de perfiles permite cargar, crear y visualizar información del usuario. | Aprobado |
| Mobile Application | Prueba de integración | Android Studio Emulator | Navegación de la aplicación | La aplicación permite navegar entre las pantallas principales sin errores críticos. | Aprobado |
| Backend | Prueba unitaria | .NET / `dotnet test` | Servicios IAM | Los servicios de autenticación y autorización responden correctamente. | Aprobado |
| Backend | Prueba de integración | Swagger / API Client | Endpoints del backend | Los endpoints principales retornan respuestas válidas. | Aprobado |
| Backend | Prueba técnica | Health Check | Conexión con base de datos | El backend valida correctamente la conexión con MySQL. | Aprobado |
| APK | Prueba de ejecución | Android Emulator / Dispositivo físico | Instalación de APK | La APK se instala correctamente en el dispositivo de prueba. | Aprobado |
| APK | Prueba funcional | Android Emulator / Dispositivo físico | Inicio de aplicación | La aplicación inicia correctamente desde la APK demo. | Aprobado |


##### 5.2.1.1.5. Execution Evidence for Sprint Review 

Durante el Sprint 1, se logró ejecutar y validar la aplicación móvil en el entorno de desarrollo de Android Studio, utilizando tanto el emulador como dispositivos físicos para asegurar la correcta funcionalidad de las características implementadas. Así mismo, el despliegue del backend y landing page.


![App Execution 1](../assets/chapter-5/sprints/sprint-1/app-execution-01.jpeg)

![App Execution 2](../assets/chapter-5/sprints/sprint-1/app-execution-02.jpg)

![App Execution 3](../assets/chapter-5/sprints/sprint-1/app-execution-03.jpg)


##### 5.2.1.1.6. Services Documentation Evidence for Sprint Review

**Profiles**: Este bounded context maneja la información de los perfiles de los usuarios dentro de la plataforma. Proporciona funcionalidades para crear perfiles, consultar su información y obtener el detalle de un perfil específico. Es esencial para almacenar y gestionar los datos personales asociados a cada usuario del sistema.

![swagerperfiles.png](../assets/chapter-5/api/swagger/swagger-perfiles.png)

**Payments**: Este bounded context administra el procesamiento y la consulta de pagos dentro de la plataforma. Proporciona funcionalidades para registrar nuevos pagos y consultar los pagos asociados a una reserva específica. Es fundamental para garantizar la gestión financiera de las transacciones realizadas por los huéspedes.

![swagerpagos.png](../assets/chapter-5/api/swagger/swagger-pagos.png)

**Authentication**: Este bounded context se encarga de la autenticación y el acceso de los usuarios al sistema. Proporciona funcionalidades para el registro de nuevos usuarios y el inicio de sesión seguro. Es esencial para validar credenciales, controlar el acceso a la plataforma y proteger la información de los distintos actores del sistema.

![swagerautenticacion.png](../assets/chapter-5/api/swagger/swagger-autenticacion.png)

**Users**: Este bounded context maneja la información general de los usuarios registrados en la plataforma. Proporciona funcionalidades para consultar todos los usuarios y obtener la información de un usuario específico por su identificador. Es importante para la administración y supervisión de las cuentas existentes en el sistema.

![swagerusuarios.png](../assets/chapter-5/api/swagger/swagger-usuarios.png)

**Bookings**: Este bounded context gestiona todo el ciclo de vida de las reservas. Proporciona funcionalidades para crear reservas, consultar reservas por identificador, listar todas las reservas, obtener reservas por habitación y ejecutar acciones como confirmar o cancelar una reserva. Es uno de los núcleos funcionales de la plataforma, ya que articula la relación entre huéspedes, habitaciones y disponibilidad.

![swagerbooking.png](../assets/chapter-5/api/swagger/swagger-booking.png)

**Analytics**: Este bounded context administra la generación y consulta de métricas analíticas del sistema. Proporciona funcionalidades para obtener indicadores de desempeño, como métricas mensuales de reservas. Es clave para apoyar la toma de decisiones mediante el análisis del rendimiento operativo de la plataforma.

![swageranaliticas.png](../assets/chapter-5/api/swagger/swagger-analiticas.png)

**AccommodationOptions**: Este bounded context maneja las opciones complementarias relacionadas con los alojamientos. Proporciona funcionalidades para consultar y registrar categorías de hoteles, así como consultar y crear amenidades. Es importante para estructurar la información maestra del sistema y enriquecer la oferta disponible para hoteles y habitaciones.

![swageracopmodation.png](../assets/chapter-5/api/swagger/swagger-acomodation.png)

**Hotels**: Este bounded context administra la información de los hoteles registrados en la plataforma. Proporciona funcionalidades para crear nuevos hoteles, listar todos los hoteles, consultar un hotel por identificador, actualizar su información y eliminarlo. Es esencial para gestionar las propiedades que forman parte del ecosistema SmartStay.

![swagerhoteles.png](../assets/chapter-5/api/swagger/swagger-hoteles.png)

**Rooms**: Este bounded context maneja la información de las habitaciones asociadas a los hoteles. Proporciona funcionalidades para crear habitaciones, listar todas las habitaciones, consultar una habitación por identificador, actualizarlas, eliminarlas y filtrarlas por tipo. Es fundamental para la operación del sistema, ya que conecta directamente la capacidad de alojamiento con las reservas.

![swagercuarto.png](../assets/chapter-5/api/swagger/swagger-cuartos.png)

**RoomTypes**: Este bounded context administra los tipos de habitación disponibles en la plataforma. Proporciona funcionalidades para crear tipos de habitación, listarlos y consultar un tipo específico por identificador. Es importante para clasificar la oferta de habitaciones y mantener consistencia en la estructura del catálogo.

![swagercuartostipos.png](../assets/chapter-5/api/swagger/swagger-cuartostipo.png)

##### 5.2.1.1.7. Software Deployment Evidence for Sprint Review

En este Sprint 1, los miembros del equipo lograron completar las tareas asociadas al desarrollo inicial de la aplicación móvil SmartStay.

El trabajo incluyó la configuración del entorno de desarrollo en Android Studio, la implementación de las primeras interfaces móviles y la integración de componentes principales como la pantalla de inicio de sesión, navegación entre vistas y estructura base de la aplicación.

La aplicación móvil cumple el rol de plataforma principal de interacción para huéspedes y personal operativo, permitiendo centralizar funcionalidades relacionadas con reservas, gestión hotelera y servicios digitales dentro del ecosistema SmartStay.

Una aplicación móvil es fundamental en proyectos modernos orientados a la experiencia del usuario, ya que permite ofrecer accesibilidad, rapidez e interacción en tiempo real desde dispositivos Android. En el caso de SmartStay, la aplicación busca optimizar la experiencia hotelera mediante procesos digitales y una gestión más eficiente de los servicios.


##### 5.2.1.1.8. Team Collaboration Insights during Sprint

Las actividades de desarrollo de este Sprint 1 se realizaron de forma colaborativa, distribuyendo las tareas entre todos los miembros del equipo.
Acciones de colaboración destacadas:

Se utilizó GitHub como plataforma central para la coordinación, control de versiones y seguimiento del proyecto.
Uno de los integrantes configuró el repositorio inicial, creó la estructura de ramas y estableció las normas de trabajo.
Cada miembro del equipo realizó commits claros y documentados con los cambios implementados.
Se trabajó mediante pull requests para integrar las contribuciones al repositorio principal.
Se realizaron revisiones de código en equipo para garantizar la coherencia visual, técnica y funcional de la Landing Page.

Gracias a este flujo de trabajo organizado, el equipo logró avanzar de manera paralela y eficiente, minimizando conflictos en el código y obteniendo un resultado coherente y de calidad.

#### 5.2.1.2. Sprint 2

A continuación, se presenta el Sprint Planning 2, en el que se incluyen las evidencias de planificación y desarrollo de las funcionalidades implementadas durante esta iteración. Asimismo, se documentan los avances del proyecto, las evidencias de pruebas, despliegue y los insights de colaboración del equipo registrados a través de GitHub.

##### 5.2.1.2.1. Sprint Planning 2

| **Sprint #**                        | Sprint 2                                                                                                                                                                                                                                |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sprint Planning Background**      | Reunión de planificación orientada a definir las funcionalidades prioritarias para la segunda iteración del proyecto SmartStay, enfocándose en la implementación de nuevas características de negocio y mejoras en la aplicación móvil. |
| **Date**                            | 15/06/2026                                                                                                                                                                                                                              |
| **Time**                            | 19:00                                                                                                                                                                                                                                   |
| **Location**                        | Modalidad remota mediante Discord                                                                                                                                                                                                       |
| **Prepared By**                     | Equipo SmartStay                                                                                                                                                                                                                        |
| **Attendees (to planning meeting)** | Verona Flores, Ítalo Sebastián                                                                               |
| **Sprint 2 Review Summary**         | Durante el Sprint 1 se logró publicar la Landing Page institucional del proyecto, desplegar la primera versión funcional del backend y validar la ejecución inicial de la aplicación móvil.                                             |
| **Sprint 2 Retrospective Summary**  | Se identificó la necesidad de mejorar la distribución de tareas, aumentar la frecuencia de revisión de código y fortalecer la comunicación para acelerar la integración de funcionalidades.                                             |
| **Sprint Goal & User Stories**      | —                                                                                                                                                                                                                                       |
| **Sprint 2 Goal**                   | Desarrollar una aplicación móvil funcional en Kotlin, incorporando módulos de autenticación y seguridad, gestión de perfiles y usuarios, administración de hoteles y habitaciones, así como procesamiento de pagos.                     |
| **Sprint 2 Velocity**               | 2                                                                                                                                                                                                                                       |
| **Sum of Story Points**             | 2                                                                                                                                                                                                                                       |

---

##### 5.2.1.2.2. Sprint Backlog 2

###### Introducción

El objetivo principal del Sprint 2 es la implementación del núcleo de seguridad, gestión de perfiles, gestión de hoteles y habitaciones en ambos perfiles (Staff y Guest).

Durante esta iteración se desarrollarán funcionalidades relacionadas con IAM (Identity & Access Management), Profiles, Properties Management y Bookings & Payments, accomodations permitiendo incrementar el valor funcional de la aplicación y acercar el producto a una versión más completa y operativa mediante la gestión de sesiones seguras y control de acceso.

### Sprint #2 – Sprint Backlog

| **Sprint #** | **User Story** | **Work-Item/Task** | **Id**                              | **Title**                                                           | **Description**                                                                                                       | **Estimation (Hours)** | **Assigned To**                   | **Status** |
|--------------|----------------|--------------------|-------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------|-----------------------------------|------------|
| Sprint 2     | US-02          | UT-01              | Secure login                        | Implementar AuthInterceptor JWT                                     | Desarrollar el interceptor OkHttp para inyección y revocación dinámica de tokens JWT en cada petición autenticada.    | 6                      | Verona Flores, Ítalo Sebastián    | Done       |
| Sprint 2     | US-02          | UT-02              | Secure login                        | Implementar TokenManager                                            | Crear el gestor de tokens que almacena, recupera y valida el ciclo de vida del JWT en la aplicación móvil.            | 5                      | Verona Flores, Ítalo Sebastián    | Done       |
| Sprint 2     | US-03          | UT-03              | Profile and role management         | Actualizar permisos de usuario con rol admin                        | Extender el modelo de usuario para incluir el rol `admin` con visibilidad y permisos de gestión diferenciados.        | 4                      | Verona Flores, Ítalo Sebastián    | Done       |
| Sprint 2     | US-03          | UT-04              | Profile and role management         | Implementar ProfileDetailScreen y ViewModel                         | Desarrollar la pantalla de detalle de perfil con lógica de carga de datos y manejo de errores desde el ViewModel.     | 5                      | Verona Flores, Ítalo Sebastián    | Done       |
| Sprint 2     | US-03          | UT-05              | Profile and role management         | Implementar CreateProfileScreen y ViewModel                         | Crear la pantalla y ViewModel para el flujo de creación de perfil de usuario con prellenado de email.                 | 5                      | Verona Flores, Ítalo Sebastián    | Done       |
| Sprint 2     | US-03          | UT-06              | Profile and role management         | Integrar Material3 en pantallas de perfil                           | Refactorizar las pantallas de creación y edición de perfil incorporando componentes de Material Design 3.             | 3                      | Verona Flores, Ítalo Sebastián    | Done       |
| Sprint 2     | US-06          | UT-07              | Room and status management          | Implementar listado de habitaciones para guests y hosts             | Desarrollar la pantalla de inventario de habitaciones con vistas diferenciadas según el rol del usuario autenticado.  | 6                      |       | Done       |
| Sprint 2     | US-06          | UT-08              | Room and status management          | Rediseñar tarjetas de hotel para administración                     | Adaptar el componente de hotel cards incorporando controles de gestión RBAC para el perfil administrador.             | 4                      |       | Done       |
| Sprint 2     | US-06          | UT-09              | Room and status management          | Sincronizar modelos de alojamiento con schema del backend           | Refactorizar los modelos de datos de accommodation eliminando pricing a nivel de hotel y alineándolos con la API.     | 4                      |       | Done       |
| Sprint 2     | US-07          | UT-10              | Centralized reservation management  | Implementar pantalla de creación de habitaciones                    | Desarrollar el formulario y lógica de negocio para el registro de nuevas habitaciones con gestión de categorías.      | 5                      |       | Done       |
| Sprint 2     | US-07          | UT-11              | Centralized reservation management  | Agregar campos de dirección, ciudad y país a hoteles                | Incorporar los campos `address`, `city` y `country` en la pantalla HotelListScreen con datos de prueba actualizados.  | 3                      |       | Done       |
| Sprint 2     | US-08          | UT-12              | Automated digital check-in          | Conectar módulo de pagos con alojamientos                           | Integrar el bounded context de Bookings & Payments con el módulo de accommodations para el flujo de reserva completo. | 6                      |  | Done       |
| Sprint 2     | US-08          | UT-13              | Automated digital check-in          | Merge rama accommodations-rebase en feature/payments                | Resolver conflictos de integración entre la rama de alojamientos y el módulo de pagos garantizando consistencia.      | 3                      |  | Done       |
| Sprint 2     | US-05          | UT-14              | Mobile administrative dashboard     | Implementar pantalla de edición de hotel y ViewModel administrativo | Desarrollar la pantalla de edición de propiedades hoteleras con ViewModel para administración de datos del hotel.     | 5                      |       | Done       |
| Sprint 2     | US-05          | UT-15              | Mobile administrative dashboard     | Implementar flujo de registro de propiedades para hosts             | Desarrollar el flujo completo de alta de nuevas propiedades hoteleras accesible desde el perfil host.                 | 6                      |       | Done       |
| Sprint 2     | US-20          | UT-16              | OTA and booking channel integration | Expandir API service e infraestructura de gestión de habitaciones   | Ampliar el servicio de API con nuevos endpoints y repositorios para la administración completa de habitaciones.       | 5                      |       | Done       |
| Sprint 2     | US-10          | UT-17              | Staff task assignment and tracking  | Implementar navegación por tabs y rutas de administración           | Desarrollar la navegación principal basada en tabs e incorporar las nuevas rutas del módulo de administración.        | 4                      |       | Done       |
| Sprint 2     | US-02          | UT-18              | Secure login                        | Agregar booking al dashboard del staff                              | Incorporar el módulo de booking en la vista principal del staff con acceso desde la navegación inferior.              | 4                      |       | Done       |
| Sprint 2     | US-07          | UT-19              | Centralized reservation management  | Corrección de errores en módulo booking                             | Identificar y resolver errores funcionales en el flujo de booking detectados durante pruebas de integración.          | 4                      |                               | Done       |
| Sprint 2     | US-24          | UT-20              | Segmented landing page              | Actualizar logo e identidad visual                                  | Incorporar el logotipo actualizado de SmartStay en la aplicación móvil y ajustar el nombre del proyecto.              | 2                      |                               | Done       |

##### 5.2.1.2.3. Development Evidence for Sprint Review


| Commit    | Autor          | Fecha      | Rama/Referencia      | Mensaje                                                                                                  |
| --------- | -------------- | ---------- |----------------------| -------------------------------------------------------------------------------------------------------- |
| `5a2cfdd` |            | 18/06/2026 | `feature/main`       | cambio de nombre                                                                                         |
| `96771e5` |            | 18/06/2026 | `feature/main`                 | se AGREGO LOGO                                                                                           |
| `225ecb4` |            | 18/06/2026 | `feature/main`                 | se AGREGO LOGO                                                                                           |
| `d908219` |            | 18/06/2026 | `feature/main`                 | fix booking                                                                                              |
| `5b58562` |            | 18/06/2026 | `feature/main`                 | Fix:Errores booking                                                                                      |
| `183b2f2` |  | 17/06/2026 | `feature/main`                 | Se agrego booking                                                                                        |
| `a1f9bc4` | atomdragon1318 | 16/06/2026 | `feature/main`                 | feat(user): update user permissions to include 'admin' role for management and visibility                |
| `9e41bf5` | atomdragon1318 | 16/06/2026 | `feature/main`                 | feat(profile): update ProfileDetailScreen and ViewModel for improved profile loading and error handling  |
| `f8bf74b` | atomdragon1318 | 16/06/2026 | `feature/main`                 | feat(profile): add CreateProfileScreen and ViewModel for profile creation                                |
| `7c71da2` | atomdragon1318 | 16/06/2026 | `feature/main`                 | feat(profile): enhance profile creation and editing screens with email prefill and material3 integration |
| `d758243` | atomdragon1318 | 15/06/2026 | `feature/main`                 | feat(profile): implement profile detail screen and related navigation logic                              |
| `0b0b4e9` |      | 18/06/2026 | `feature/accomodations-rebase` | feat: refactor accommodation options and update navigation                                               |
| `396861d` |      | 18/06/2026 | `feature/accomodations-rebase` | refactor: replace mock data with repository calls in OptionsViewModel                                    |
| `69841b6` |      | 18/06/2026 | `feature/accomodations-rebase` | refactor: handle optional location and description in HotelListScreen                                    |
| `eddbd09` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(accommodation): implement room list inventory for guests and hosts                                  |
| `e0d6b69` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(admin): implement hotel edition screen and administrative viewmodel                                 |
| `f1ff850` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(accommodation): expand API service and implement room management infrastructure                     |
| `311df36` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(nav): implement tab-based main navigation and register new administration routes                    |
| `cdabdca` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(admin): implement room creation and category management                                             |
| `df48baf` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(admin): implement property registration flow for hosts                                              |
| `e3e9a4e` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(accommodation): redesign hotel cards for admin management and update RBAC permissions               |
| `def1952` |      | 20/06/2026 | `feature/accomodations-rebase` | refactor(data): sync accommodation models with backend schema and remove hotel-level pricing             |
| `5449b6b` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(nav): implement tab-based navigation and fix back navigation flow                                   |
| `038bf12` |      | 20/06/2026 | `feature/accomodations-rebase` | feat(accommodation): add address, city, and country fields to hotel mock data in HotelListScreen         |
| `c3a8067` | atomdragon1318 | 14/06/2026 | `feature/chain-admin-dashboard`                | refactor: remove obsolete TODO comment from UserListScreen                                               |
| `70159fc` | atomdragon1318 | 14/06/2026 | `feature/chain-admin-dashboard`                  | feat(iam): implement TokenManager and user models for authentication flow                                |
| `87ed41f` | atomdragon1318 | 14/06/2026 | `feature/chain-admin-dashboard`                  | feat(IAM): update accommodation module with new API service and refactor navigation strings              |
| `354850b` | atomdragon1318 | 14/06/2026 | `feature/chain-admin-dashboard`       | feat: implement AuthInterceptor for JWT token management and update navigation graph                     |
| `2e94c47` |        | 20/06/2026 | `feature/payments`   | feat: connect payments with accommodations                                                               |
| `f241581` |        | 20/06/2026 | `feature/payments`   | Merge remote-tracking branch 'origin/accomodations-rebase' into feature/payments                         |

##### 5.2.1.2.4. Testing Suite Evidence for Sprint Review

###### Evidencia de la Suite de Pruebas para la Revisión del Sprint

Durante este sprint, el equipo realizó actividades de prueba para validar las funcionalidades desarrolladas, asegurando su correcto funcionamiento tanto a nivel de lógica de negocio como de experiencia de usuario.

| Elemento evaluado | Tipo de prueba | Resultado esperado | Estado |
|---|---|---|---|
| [FUNCIONALIDAD] | Prueba unitaria | [RESULTADO] | Aprobado |
| [FUNCIONALIDAD] | Prueba de integración | [RESULTADO] | Aprobado |
| [FUNCIONALIDAD] | Validación de interfaz | [RESULTADO] | Aprobado |
| [FUNCIONALIDAD] | Prueba funcional | [RESULTADO] | Aprobado |

---

##### 5.2.1.2.5. Execution Evidence for Sprint Review

Durante el Sprint 2 se ejecutaron y validaron las funcionalidades desarrolladas dentro de la aplicación móvil SmartStay. Las pruebas se realizaron utilizando Android Studio, dispositivos físicos y servicios desplegados en la nube para verificar la correcta integración entre frontend y backend.

![App Android 1](../assets/chapter-5/implementation/mobile/sprint-2/android-app-01.jpeg)
![App Android 2](../assets/chapter-5/implementation/mobile/sprint-2/android-app-02.jpeg)
![App Android 3](../assets/chapter-5/implementation/mobile/sprint-2/android-app-03.jpeg)
![App Android 4](../assets/chapter-5/implementation/mobile/sprint-2/android-app-04.jpeg)
![App Android 5](../assets/chapter-5/implementation/mobile/sprint-2/android-app-05.jpeg)
![App Android 6](../assets/chapter-5/implementation/mobile/sprint-2/android-app-06.jpeg)
![App Android 7](../assets/chapter-5/implementation/mobile/sprint-2/android-app-07.jpeg)
![App Android 8](../assets/chapter-5/implementation/mobile/sprint-2/android-app-08.jpeg)

---

##### 5.2.1.2.6. Services Documentation Evidence for Sprint Review

Durante este sprint se actualizó el bounded context de IAM/Authentication, incorporando mejoras relacionadas con la autenticación de usuarios y la gestión de roles dentro del sistema. La documentación de los servicios REST fue verificada mediante Swagger/OpenAPI, donde se evidencian los endpoints disponibles para el inicio de sesión y registro de usuarios.

**Authentication**: Este bounded context gestiona la autenticación de usuarios y el control de acceso basado en roles dentro de SmartStay. Sus servicios permiten registrar nuevos usuarios e iniciar sesión en la aplicación, retornando la información necesaria para identificar el rol del usuario y habilitar las funcionalidades correspondientes según sus permisos.


Asimismo, durante el sprint se trabajó con la lógica de roles para diferenciar el acceso de los distintos tipos de usuario del sistema, como Guest, Admin y ChainAdmin, permitiendo controlar qué secciones y acciones están disponibles para cada perfil dentro de la aplicación.

##### 5.2.1.2.7. Software Deployment Evidence for Sprint Review

A continuación, se presentan las evidencias del **despliegue de la Landing Page** de Smart Stay, desarrollada y publicada mediante **Vercel**.

La landing page fue vinculada directamente con el repositorio del proyecto, permitiendo que la publicación se realice a partir de la rama **main**. De este modo, cada cambio validado en el repositorio puede reflejarse en la versión pública del sitio, asegurando consistencia entre el desarrollo y el entorno desplegado.

Gracias a esta configuración, la página quedó disponible públicamente, confirmando el correcto funcionamiento del flujo de despliegue y la integración entre el repositorio y **Vercel**.

**URL de la Landing Page: https://smartstay-movildev-landing.vercel.app/ **

![LANDING.png](../assets/chapter-5/deployment/landing-page-final.png)

Como evidencia complementaria, se presenta una captura de la landing page desplegada y accesible desde su URL pública.

A continuación, se presentan las evidencias del **despliegue del Back End** de Smart Stay, publicado en la plataforma **Render**.

El servicio backend fue enlazado con el repositorio principal del proyecto, permitiendo que la plataforma tome el código de la rama **main** para su despliegue en producción. Gracias a esta configuración, el servicio puede mantenerse actualizado de manera consistente con los cambios validados en el repositorio.

Como evidencia del despliegue, se presenta la **URL pública del servicio** junto con una captura de la documentación **Swagger/OpenAPI** ejecutándose correctamente desde el entorno desplegado. Esto confirma que la API se encuentra activa, accesible y lista para ser consumida por los demás componentes del sistema.

**URL del Back End / Swagger: https://smartstay-movildev-api.onrender.com/scalar/ **

![Evidencia del despliegue en Render](../assets/chapter-5/deployment/render-backend.png)

La evidencia visual demuestra que el backend fue desplegado correctamente y que sus endpoints pueden consultarse desde la interfaz de Swagger.

---

##### 5.2.1.2.8. Team Collaboration Insights during Sprint

Las actividades de desarrollo correspondientes al Sprint 2 fueron ejecutadas de manera colaborativa por todos los integrantes del equipo.

Acciones de colaboración destacadas:

- Se continuó utilizando GitHub como herramienta principal para el control de versiones y seguimiento del avance.
- Se gestionaron ramas específicas para cada funcionalidad desarrollada.
- Se realizaron commits frecuentes y descriptivos para facilitar la trazabilidad de cambios.
- Se utilizaron Pull Requests para la integración controlada de nuevas funcionalidades.
- Se llevaron a cabo revisiones de código entre miembros del equipo.
- Se realizaron reuniones de seguimiento para resolver bloqueos y coordinar avances.

Gracias a estas prácticas, el equipo mantuvo un flujo de trabajo organizado y logró integrar exitosamente las funcionalidades desarrolladas durante el Sprint 2.







#### 5.2.1.3. Sprint 3

A continuación, se presenta el desarrollo del Sprint 3, correspondiente a la iteración final del proyecto SmartStay. A diferencia de los sprints anteriores, esta etapa no se enfocó únicamente en construir módulos aislados, sino en completar, integrar, estabilizar y validar la versión final de la aplicación móvil y los servicios asociados.

Durante este sprint se priorizó el cierre funcional del producto, la corrección de errores críticos, la mejora de experiencia de usuario, la integración completa entre aplicación móvil y backend, la validación de los flujos principales y la preparación de evidencias para la presentación final del proyecto.

---

##### 5.2.1.3.1. Sprint Planning 3

| **Sprint #** | Sprint 3 |
|---|---|
| **Sprint Planning Background** | Reunión de planificación orientada a cerrar el desarrollo funcional de SmartStay, integrar los módulos pendientes y preparar una versión final demostrable para la evaluación del curso. |
| **Date** | 22/06/2026 |
| **Time** | 20:00 |
| **Location** | Modalidad remota mediante Discord |
| **Prepared By** | Equipo SmartStay |
| **Attendees** | Verona Flores, Ítalo Sebastián |
| **Sprint 2 Review Summary** | En el Sprint 2 se lograron implementar funcionalidades base relacionadas con autenticación, perfiles, gestión de hoteles, habitaciones y pagos. Sin embargo, todavía existían flujos incompletos, errores de navegación, validaciones pendientes y falta de integración total entre algunos módulos. |
| **Sprint 2 Retrospective Summary** | El equipo identificó que era necesario mejorar la integración entre frontend y backend, corregir inconsistencias visuales, validar los roles de usuario y completar la documentación de despliegue. También se acordó reforzar las pruebas funcionales antes de la entrega final. |
| **Sprint Goal & User Stories** | US-09, US-11, US-12, US-13, US-14, US-15, US-16, US-17, US-18 y US-19 |
| **Sprint 3 Goal** | Completar la versión final de SmartStay, asegurando que los flujos principales de huésped, staff y administrador funcionen correctamente, con integración backend, validación de datos, mejoras visuales, pruebas funcionales y despliegue documentado. |
| **Sprint 3 Velocity** | 18 work-items completados |
| **Sum of Estimated Hours** | 82 horas |

---

##### 5.2.1.3.2. Sprint Backlog 3

###### Introducción

El Sprint 3 tuvo como objetivo principal completar la versión final funcional de SmartStay. En esta iteración se trabajó sobre funcionalidades diferentes a las abordadas en el Sprint 2, priorizando el cierre del producto, la integración de flujos, la validación de formularios, la experiencia de usuario, la estabilidad de navegación y la preparación de la aplicación para su presentación final.

Las tareas desarrolladas se centraron en completar el flujo del huésped, mejorar el panel del staff, agregar validaciones en formularios críticos, implementar pantallas de resumen, mejorar la gestión de reservas, optimizar la experiencia visual y documentar la ejecución final del sistema.

### Sprint #3 – Sprint Backlog

| **Sprint #** | **User Story** | **Work-Item/Task** | **Id** | **Title** | **Description** | **Estimation (Hours)** | **Assigned To** | **Status** |
|---|---|---|---|---|---|---|---|---|
| Sprint 3 | US-09 | UT-01 | Guest home experience | Implementar pantalla principal del huésped | Desarrollar la pantalla inicial del huésped con resumen de reserva activa, accesos rápidos y estado de habitación. | 5 |  | Done |
| Sprint 3 | US-09 | UT-02 | Guest home experience | Agregar tarjetas de acceso rápido | Incorporar accesos rápidos para reservas, servicios, pagos y perfil dentro del home del huésped. | 4 |  | Done |
| Sprint 3 | US-11 | UT-03 | Booking summary | Crear pantalla de resumen de reserva | Desarrollar una pantalla que muestre datos del hotel, habitación, fechas, costo total y estado de la reserva. | 6 |  | Done |
| Sprint 3 | US-11 | UT-04 | Booking summary | Validar datos antes de confirmar reserva | Implementar validaciones para evitar reservas incompletas, fechas inválidas o habitaciones no disponibles. | 5 |  | Done |
| Sprint 3 | US-12 | UT-05 | Payment confirmation | Implementar pantalla de confirmación de pago | Crear una pantalla final que confirme el pago exitoso y muestre el código de reserva generado. | 5 |  | Done |
| Sprint 3 | US-12 | UT-06 | Payment confirmation | Agregar manejo de error en pagos | Mostrar mensajes de error cuando el pago no pueda procesarse o exista una falla de conexión con el backend. | 4 |  | Done |
| Sprint 3 | US-13 | UT-07 | Staff dashboard | Mejorar panel operativo del staff | Rediseñar el dashboard del staff para visualizar reservas recientes, habitaciones ocupadas y tareas pendientes. | 6 |  | Done |
| Sprint 3 | US-13 | UT-08 | Staff dashboard | Agregar indicadores de estado de habitaciones | Incorporar indicadores visuales para habitaciones disponibles, ocupadas, en limpieza y en mantenimiento. | 5 |  | Done |
| Sprint 3 | US-14 | UT-09 | Room status update | Implementar cambio de estado de habitación | Permitir que el staff actualice el estado de una habitación desde la aplicación móvil. | 6 |  | Done |
| Sprint 3 | US-14 | UT-10 | Room status update | Sincronizar estado de habitación con backend | Conectar la actualización de estado con el servicio backend para mantener información en tiempo real. | 5 |  | Done |
| Sprint 3 | US-15 | UT-11 | Notifications | Crear notificaciones internas de reserva | Implementar alertas visuales dentro de la aplicación cuando se registre una nueva reserva o cambio de estado. | 5 | Verona Flores, Ítalo Sebastián | Done |
| Sprint 3 | US-15 | UT-12 | Notifications | Diseñar componente de notificación reutilizable | Crear un componente visual reutilizable para mensajes de éxito, advertencia y error. | 3 | Verona Flores, Ítalo Sebastián | Done |
| Sprint 3 | US-16 | UT-13 | UI final polish | Unificar estilos visuales finales | Ajustar colores, tipografías, espaciados, botones y tarjetas para mantener coherencia visual en toda la aplicación. | 5 |  | Done |
| Sprint 3 | US-16 | UT-14 | UI final polish | Corregir pantallas con desbordamiento | Solucionar problemas de scroll, tamaños de texto y componentes desalineados en pantallas pequeñas. | 4 |  | Done |
| Sprint 3 | US-17 | UT-15 | Error handling | Implementar mensajes de error globales | Agregar manejo de errores para fallos de conexión, respuestas vacías del backend y datos inválidos. | 5 | Verona Flores, Ítalo Sebastián | Done |
| Sprint 3 | US-18 | UT-16 | Final integration | Integrar flujos Guest, Staff y Admin | Verificar que los flujos principales de cada rol puedan ejecutarse sin interrupciones desde el inicio de sesión. | 6 | Equipo SmartStay | Done |
| Sprint 3 | US-18 | UT-17 | Final integration | Realizar pruebas de regresión | Validar que las funcionalidades desarrolladas en sprints anteriores sigan funcionando luego de la integración final. | 5 | Equipo SmartStay | Done |
| Sprint 3 | US-19 | UT-18 | Final delivery | Preparar evidencias finales de ejecución y despliegue | Organizar capturas, documentación de servicios, URLs de despliegue y evidencias de colaboración para el informe final. | 3 | Equipo SmartStay | Done |

---

##### 5.2.1.3.3. Development Evidence for Sprint Review

Durante el Sprint 3 se registraron commits orientados al cierre final del producto. Estos commits evidencian la implementación de nuevas pantallas, mejoras en los flujos de reserva y pago, actualización del dashboard operativo, corrección de errores, ajustes visuales y validación final de la integración entre módulos.

| Commit | Autor | Fecha | Rama/Referencia | Mensaje |
|---|---|---|---|---|
| `9ac41f2` |  | 22/06/2026 | `feature/guest-home` | feat(guest): implement guest home screen with active booking summary |
| `7bd82e1` |  | 22/06/2026 | `feature/guest-home` | feat(guest): add quick access cards for booking, payments and profile |
| `4e91c8a` |  | 23/06/2026 | `feature/booking-summary` | feat(booking): create booking summary screen |
| `1cf73a5` |  | 23/06/2026 | `feature/booking-summary` | fix(booking): validate dates and room availability before confirmation |
| `6ab39d0` |  | 24/06/2026 | `feature/payment-confirmation` | feat(payment): implement payment confirmation screen |
| `28e74bc` |  | 24/06/2026 | `feature/payment-confirmation` | fix(payment): add error handling for failed transactions |
| `8d12fa9` |  | 24/06/2026 | `feature/staff-dashboard-final` | feat(staff): redesign operational dashboard |
| `31f7dce` |  | 24/06/2026 | `feature/staff-dashboard-final` | feat(staff): add room status indicators |
| `5b87a2d` |  | 25/06/2026 | `feature/room-status-update` | feat(room): implement room status update from staff app |
| `77c0e3f` |  | 25/06/2026 | `feature/room-status-update` | feat(room): sync room status changes with backend service |
| `e48f91b` | atomdragon1318 | 25/06/2026 | `feature/internal-notifications` | feat(notification): add internal booking notification component |
| `3da8c64` | atomdragon1318 | 25/06/2026 | `feature/internal-notifications` | refactor(ui): create reusable feedback message component |
| `0fc19a8` |  | 26/06/2026 | `feature/final-ui-polish` | style(ui): unify colors, typography and card spacing |
| `c94d6e2` |  | 26/06/2026 | `feature/final-ui-polish` | fix(ui): solve scroll and overflow issues in small screens |
| `ae17f4c` | atomdragon1318 | 26/06/2026 | `feature/global-error-handling` | feat(error): implement global error messages for network failures |
| `f7b201d` | EquipoSmartStay | 27/06/2026 | `develop` | merge: integrate guest, staff and admin final flows |
| `b39d8a1` | EquipoSmartStay | 27/06/2026 | `release/sprint-3` | test: run regression testing for final mobile app version |
| `2d6f44e` | EquipoSmartStay | 28/06/2026 | `main` | release: prepare SmartStay final delivery build |

---

##### 5.2.1.3.4. Testing Suite Evidence for Sprint Review

###### Evidencia de la Suite de Pruebas para la Revisión del Sprint

Durante el Sprint 3 se ejecutaron pruebas funcionales, pruebas de integración, pruebas de regresión y validaciones de interfaz. El objetivo fue comprobar que la aplicación final funcione correctamente para los perfiles de huésped, staff y administrador.

| Elemento evaluado | Tipo de prueba | Resultado esperado | Estado |
|---|---|---|---|
| Home del huésped | Prueba funcional | El huésped visualiza su reserva activa, accesos rápidos y datos principales de su estadía. | Aprobado |
| Resumen de reserva | Prueba funcional | La aplicación muestra hotel, habitación, fechas, precio total y estado de reserva antes de confirmar. | Aprobado |
| Validación de reserva | Prueba de integración | El sistema bloquea reservas con fechas inválidas o habitaciones no disponibles. | Aprobado |
| Confirmación de pago | Prueba funcional | Luego de realizar el pago, se muestra una pantalla de confirmación con el código de reserva. | Aprobado |
| Error en pago | Prueba funcional | Si ocurre un error en la transacción, la aplicación muestra un mensaje claro al usuario. | Aprobado |
| Dashboard del staff | Validación de interfaz | El staff visualiza habitaciones, reservas recientes y tareas pendientes de forma ordenada. | Aprobado |
| Cambio de estado de habitación | Prueba de integración | El staff puede actualizar el estado de la habitación y el cambio se sincroniza con el backend. | Aprobado |
| Notificaciones internas | Prueba funcional | La aplicación muestra alertas cuando se registra una reserva o cambia el estado de una habitación. | Aprobado |
| Manejo global de errores | Prueba de regresión | La aplicación muestra mensajes adecuados ante fallos de conexión o respuestas inválidas. | Aprobado |
| Navegación final por roles | Prueba de regresión | Guest, Staff y Admin acceden únicamente a las pantallas correspondientes según su rol. | Aprobado |
| Compatibilidad visual | Validación de interfaz | Las pantallas no presentan desbordamientos ni errores de diseño en dispositivos móviles. | Aprobado |
| Flujo completo de reserva | Prueba end-to-end | El usuario puede buscar habitación, revisar la reserva, pagar y recibir confirmación. | Aprobado |

---

##### 5.2.1.3.5. Execution Evidence for Sprint Review

Durante el Sprint 3 se ejecutó la versión final de la aplicación móvil SmartStay, validando los principales flujos funcionales definidos para la presentación final. Las pruebas fueron realizadas en Android Studio y dispositivos móviles, utilizando servicios backend desplegados para comprobar la integración real del sistema.

Los flujos ejecutados fueron los siguientes:

- Inicio de sesión con usuario registrado.
- Redirección de pantalla según rol del usuario.
- Visualización del home del huésped.
- Consulta de hoteles y habitaciones disponibles.
- Visualización del resumen de reserva.
- Confirmación de reserva.
- Proceso de pago y pantalla de confirmación.
- Visualización del dashboard operativo del staff.
- Actualización del estado de habitaciones.
- Visualización de notificaciones internas.
- Validación de errores de conexión y datos inválidos.
- Navegación final entre módulos principales de la aplicación.

![Sprint 3 App 1](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-1.png)
![Sprint 3 App 2](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-2.png)
![Sprint 3 App 3](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-3.png)
![Sprint 3 App 4](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-4.png)


---

##### 5.2.1.3.6. Services Documentation Evidence for Sprint Review

Durante el Sprint 3 se revisó y actualizó la documentación de los servicios necesarios para la versión final de SmartStay. Esta documentación permitió validar que los endpoints principales se encuentren disponibles y alineados con los flujos implementados en la aplicación móvil.

Los servicios documentados fueron:

- **Authentication Service:** Permite iniciar sesión, validar credenciales y devolver información del usuario autenticado.
- **Users Service:** Gestiona los datos principales de los usuarios y sus roles dentro del sistema.
- **Hotels Service:** Permite consultar, registrar y editar información de propiedades hoteleras.
- **Rooms Service:** Gestiona habitaciones, disponibilidad, categorías y cambios de estado.
- **Bookings Service:** Administra la creación, consulta y confirmación de reservas.
- **Payments Service:** Permite registrar pagos y devolver la confirmación de transacciones.
- **Notifications Service:** Soporta alertas internas relacionadas con reservas y cambios de estado.

La documentación fue revisada mediante Swagger/OpenAPI, verificando que los endpoints respondan correctamente y puedan ser consumidos desde la aplicación móvil.


Además, se verificó que los servicios mantengan una estructura coherente en sus respuestas, utilizando códigos de estado HTTP apropiados y mensajes comprensibles para los casos de éxito y error.

---

##### 5.2.1.3.7. Software Deployment Evidence for Sprint Review

Durante el Sprint 3 se realizó la validación final del despliegue de los componentes principales del proyecto SmartStay.

En primer lugar, se verificó que la Landing Page se encuentre publicada correctamente mediante Vercel. Esta página representa la presencia pública del producto y permite presentar la propuesta de valor de SmartStay a los usuarios interesados.

**URL de la Landing Page:**  
https://smartstay-movildev-landing.vercel.app/


Asimismo, se validó el despliegue del backend en Render, confirmando que los servicios principales se encuentren activos y accesibles desde la documentación Swagger/OpenAPI.

**URL del Back End / Swagger:**  
https://smartstay-movildev-api.onrender.com/scalar/


Finalmente, se generó una versión final de la aplicación móvil en formato APK para su ejecución y validación. Esta versión contiene los módulos integrados y fue utilizada para la demostración final del producto.

**Repositorio del APK:**  
https://github.com/Movil-dev-Aplicaciones-Moviles/APK.git


Con estas evidencias, se confirma que SmartStay cuenta con una landing page pública, servicios backend desplegados y una aplicación móvil lista para ser presentada como producto final del curso.

---

##### 5.2.1.3.8. Team Collaboration Insights during Sprint

Durante el Sprint 3, el equipo SmartStay trabajó de manera coordinada para completar la versión final del producto. La colaboración se centró en integrar funcionalidades, resolver errores, validar flujos completos y preparar las evidencias necesarias para la revisión final.

Acciones de colaboración realizadas:

- Se organizaron reuniones remotas para revisar el avance de las tareas finales.
- Se distribuyeron responsabilidades según el módulo asignado a cada integrante.
- Se utilizaron ramas específicas para funcionalidades nuevas del Sprint 3.
- Se realizaron merges hacia la rama develop para integrar los avances.
- Se creó una rama release/sprint-3 para preparar la versión final.
- Se ejecutaron pruebas de regresión antes del cierre del sprint.
- Se revisaron errores reportados durante la integración final.
- Se corrigieron problemas visuales detectados en dispositivos móviles.
- Se organizaron las evidencias de ejecución, despliegue y documentación.
- Se consolidó la versión final del informe y del producto.

El equipo logró mantener una comunicación constante durante el cierre del proyecto, priorizando las tareas críticas y asegurando que la aplicación pueda ser presentada de forma funcional. La colaboración entre los integrantes permitió completar los flujos principales de SmartStay y preparar una entrega final coherente con los objetivos del curso.

---

##### 5.2.1.3.9. Sprint 3 Final Review Summary

Al finalizar el Sprint 3, el equipo logró completar una versión final funcional de SmartStay. Esta versión integra los principales flujos de uso para huéspedes, staff y administradores, permitiendo demostrar el valor del producto como solución móvil para la gestión hotelera.

Los principales resultados obtenidos fueron:

- Implementación del home principal para el huésped.
- Creación de pantalla de resumen de reserva.
- Validación de fechas y disponibilidad antes de confirmar reservas.
- Implementación de pantalla de confirmación de pago.
- Manejo de errores en pagos y fallos de conexión.
- Mejora del dashboard operativo del staff.
- Implementación de actualización de estado de habitaciones.
- Sincronización de cambios de habitación con backend.
- Incorporación de notificaciones internas.
- Unificación visual de pantallas, botones y tarjetas.
- Corrección de problemas de scroll y diseño responsive.
- Integración final de flujos Guest, Staff y Admin.
- Ejecución de pruebas de regresión.
- Validación de servicios mediante Swagger/OpenAPI.
- Confirmación del despliegue de landing page, backend y APK.

En conclusión, el Sprint 3 permitió cerrar el ciclo de desarrollo de SmartStay con una versión más estable, integrada y lista para su presentación final. Esta iteración representó el paso de una aplicación con módulos funcionales separados hacia un producto completo, validado y alineado con la problemática planteada en el proyecto.

### 5.2.2. Implemented Landing Page Evidence

![Github Pages](../assets/chapter-5/deployment/github-pages.jpg)

**La URL que nos entrega Github Pages para acceder a la landing page es la siguiente:**  
[https://smartstay-movildev-landing.vercel.app/](https://smartstay-movildev-landing.vercel.app/)

landing Page

Esta es la sección inicial, donde está el header.

![Landing1](../assets/chapter-5/implementation/landing-page/landing-page-01.jpeg)

Aquí se puede observar la sección donde se presenta a los productos que ofrecemos.

![Landing2](../assets/chapter-5/implementation/landing-page/landing-page-02.jpeg)

Esta sección describe las soluciones de acorde al tipo de propiedad.
![Landing3](../assets/chapter-5/implementation/landing-page/landing-page-03.jpeg)

Tenemos en esta sección acerca de precios por el servicio.

![Landing4](../assets/chapter-5/implementation/landing-page/landing-page-04.jpeg)

Aquí se puede observar la sección de reseñas.

![Landing5](../assets/chapter-5/implementation/landing-page/landing-page-05.jpeg)

### 5.2.3. Implemented Frontend-Web Application Evidence

Frontend

En esta sección se puede ver las habitaciones disponibles.

![Front1](../assets/chapter-5/implementation/frontend-web/frontend-01.jpeg)


En esta sección se puede ver las habitaciones disponibles desde el punto de vista de un administrador.

![Front2](../assets/chapter-5/implementation/frontend-web/frontend-02.jpeg)

En esta sección se puede ver el panel del administrador.

![Front3](../assets/chapter-5/implementation/frontend-web/frontend-03.jpeg)

En esta sección se puede ver el panel del administrador se puede ver un dashboard con las habitaciones.

![Front4](../assets/chapter-5/implementation/frontend-web/frontend-04.jpeg)

### 5.2.4. Implemented Native-Mobile Application Evidence

Durante el Sprint 2 se ejecutaron y validaron las funcionalidades desarrolladas dentro de la aplicación móvil SmartStay. Las pruebas se realizaron utilizando Android Studio, dispositivos físicos y servicios desplegados en la nube para verificar la correcta integración entre frontend y backend.

![App Android 1](../assets/chapter-5/implementation/mobile/sprint-2/android-app-01.jpeg)
![App Android 2](../assets/chapter-5/implementation/mobile/sprint-2/android-app-02.jpeg)
![App Android 3](../assets/chapter-5/implementation/mobile/sprint-2/android-app-03.jpeg)
![App Android 4](../assets/chapter-5/implementation/mobile/sprint-2/android-app-04.jpeg)
![App Android 5](../assets/chapter-5/implementation/mobile/sprint-2/android-app-05.jpeg)
![App Android 6](../assets/chapter-5/implementation/mobile/sprint-2/android-app-06.jpeg)
![App Android 7](../assets/chapter-5/implementation/mobile/sprint-2/android-app-07.jpeg)
![App Android 8](../assets/chapter-5/implementation/mobile/sprint-2/android-app-08.jpeg)

Durante el Sprint 3 se ejecutó la versión final de la aplicación móvil SmartStay, validando los principales flujos funcionales definidos para la presentación final. Las pruebas fueron realizadas en Android Studio y dispositivos móviles, utilizando servicios backend desplegados para comprobar la integración real del sistema.

Los flujos ejecutados fueron los siguientes:

- Inicio de sesión con usuario registrado.
- Redirección de pantalla según rol del usuario.
- Visualización del home del huésped.
- Consulta de hoteles y habitaciones disponibles.
- Visualización del resumen de reserva.
- Confirmación de reserva.
- Proceso de pago y pantalla de confirmación.
- Visualización del dashboard operativo del staff.
- Actualización del estado de habitaciones.
- Visualización de notificaciones internas.
- Validación de errores de conexión y datos inválidos.
- Navegación final entre módulos principales de la aplicación.

![Sprint 3 App 1](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-1.png)
![Sprint 3 App 2](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-2.png)
![Sprint 3 App 3](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-3.png)
![Sprint 3 App 4](../assets/chapter-5/implementation/mobile/sprint-3/sprint3-app-4.png)

### 5.2.5. Implemented RESTful API and/or Serverless Backend Evidence

Durante este sprint se actualizó el bounded context de IAM/Authentication, incorporando mejoras relacionadas con la autenticación de usuarios y la gestión de roles dentro del sistema. La documentación de los servicios REST fue verificada mediante Swagger/OpenAPI, donde se evidencian los endpoints disponibles para el inicio de sesión y registro de usuarios.

**Authentication**: Este bounded context gestiona la autenticación de usuarios y el control de acceso basado en roles dentro de SmartStay. Sus servicios permiten registrar nuevos usuarios e iniciar sesión en la aplicación, retornando la información necesaria para identificar el rol del usuario y habilitar las funcionalidades correspondientes según sus permisos.


Asimismo, durante el sprint se trabajó con la lógica de roles para diferenciar el acceso de los distintos tipos de usuario del sistema, como Guest, Admin y ChainAdmin, permitiendo controlar qué secciones y acciones están disponibles para cada perfil dentro de la aplicación.

### 5.2.6. RESTful API documentation

**Profiles**: Este bounded context maneja la información de los perfiles de los usuarios dentro de la plataforma. Proporciona funcionalidades para crear perfiles, consultar su información y obtener el detalle de un perfil específico. Es esencial para almacenar y gestionar los datos personales asociados a cada usuario del sistema.

![swagerperfiles.png](../assets/chapter-5/api/swagger/swagger-perfiles.png)

**Payments**: Este bounded context administra el procesamiento y la consulta de pagos dentro de la plataforma. Proporciona funcionalidades para registrar nuevos pagos y consultar los pagos asociados a una reserva específica. Es fundamental para garantizar la gestión financiera de las transacciones realizadas por los huéspedes.

![swagerpagos.png](../assets/chapter-5/api/swagger/swagger-pagos.png)

**Authentication**: Este bounded context se encarga de la autenticación y el acceso de los usuarios al sistema. Proporciona funcionalidades para el registro de nuevos usuarios y el inicio de sesión seguro. Es esencial para validar credenciales, controlar el acceso a la plataforma y proteger la información de los distintos actores del sistema.

![swagerautenticacion.png](../assets/chapter-5/api/swagger/swagger-autenticacion.png)

**Users**: Este bounded context maneja la información general de los usuarios registrados en la plataforma. Proporciona funcionalidades para consultar todos los usuarios y obtener la información de un usuario específico por su identificador. Es importante para la administración y supervisión de las cuentas existentes en el sistema.

![swagerusuarios.png](../assets/chapter-5/api/swagger/swagger-usuarios.png)

**Bookings**: Este bounded context gestiona todo el ciclo de vida de las reservas. Proporciona funcionalidades para crear reservas, consultar reservas por identificador, listar todas las reservas, obtener reservas por habitación y ejecutar acciones como confirmar o cancelar una reserva. Es uno de los núcleos funcionales de la plataforma, ya que articula la relación entre huéspedes, habitaciones y disponibilidad.

![swagerbooking.png](../assets/chapter-5/api/swagger/swagger-booking.png)

**Analytics**: Este bounded context administra la generación y consulta de métricas analíticas del sistema. Proporciona funcionalidades para obtener indicadores de desempeño, como métricas mensuales de reservas. Es clave para apoyar la toma de decisiones mediante el análisis del rendimiento operativo de la plataforma.

![swageranaliticas.png](../assets/chapter-5/api/swagger/swagger-analiticas.png)

**AccommodationOptions**: Este bounded context maneja las opciones complementarias relacionadas con los alojamientos. Proporciona funcionalidades para consultar y registrar categorías de hoteles, así como consultar y crear amenidades. Es importante para estructurar la información maestra del sistema y enriquecer la oferta disponible para hoteles y habitaciones.

![swageracopmodation.png](../assets/chapter-5/api/swagger/swagger-acomodation.png)

**Hotels**: Este bounded context administra la información de los hoteles registrados en la plataforma. Proporciona funcionalidades para crear nuevos hoteles, listar todos los hoteles, consultar un hotel por identificador, actualizar su información y eliminarlo. Es esencial para gestionar las propiedades que forman parte del ecosistema SmartStay.

![swagerhoteles.png](../assets/chapter-5/api/swagger/swagger-hoteles.png)

**Rooms**: Este bounded context maneja la información de las habitaciones asociadas a los hoteles. Proporciona funcionalidades para crear habitaciones, listar todas las habitaciones, consultar una habitación por identificador, actualizarlas, eliminarlas y filtrarlas por tipo. Es fundamental para la operación del sistema, ya que conecta directamente la capacidad de alojamiento con las reservas.

![swagercuarto.png](../assets/chapter-5/api/swagger/swagger-cuartos.png)

**RoomTypes**: Este bounded context administra los tipos de habitación disponibles en la plataforma. Proporciona funcionalidades para crear tipos de habitación, listarlos y consultar un tipo específico por identificador. Es importante para clasificar la oferta de habitaciones y mantener consistencia en la estructura del catálogo.

![swagercuartostipos.png](../assets/chapter-5/api/swagger/swagger-cuartostipo.png)

### 5.2.7. Team Collaboration Insights

**Acciones de colaboración destacadas:**
- Se utilizó **GitHub** como herramienta central de coordinación y control de versiones.
- Uno de los integrantes configuró el repositorio inicial y las ramas de trabajo.
- Cada miembro realizó **commits documentados** con los cambios implementados.
- Se llevaron a cabo **pull requests** para integrar las contribuciones al repositorio principal.
- Se realizaron revisiones de código en equipo para mantener la coherencia visual y funcional de la landing.

Gracias a este flujo de trabajo, el equipo pudo avanzar de forma paralela y ordenada, evitando conflictos en el código y asegurando un resultado consistente.

El equipo logró mantener una comunicación constante durante el cierre del proyecto, priorizando las tareas críticas y asegurando que la aplicación pueda ser presentada de forma funcional. La colaboración entre los integrantes permitió completar los flujos principales de SmartStay y preparar una entrega final coherente con los objetivos del curso.

## 5.3. Video About-the-Product

En el video se mostró una demo funcional de SmartStay, recorriendo sus principales funcionalidades: inicio de sesión, panel de administrador, y gestión de habitaciones y reservas, validando visualmente el cumplimiento de los criterios de aceptación definidos.

Link: https://youtu.be/34tPgoDW-wY
 