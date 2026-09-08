# Capítulo V: Product Implementation

> **Estado:** pendiente de redacción por el equipo (entregable Avance 1 – Semana 4). Estructura 5.1–5.3 según el **alcance del Avance 1** del enunciado (pág. 38-39): la sección 5.2 usa 7 ítems (5.2.1–5.2.7) **sin** "Acuerdo de Servicio – SaaS"; el SaaS se incorpora recién en el Trabajo Parcial con la numeración canónica del TOC del enunciado (5.2.4). Evidencia por producto y por sprint; todos los miembros deben participar en la implementación de cada producto.

## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

**Pendiente:** especificar, por cada producto de software que usarán los miembros, (a) nombre del producto, (b) propósito de uso en el proyecto y (c) ruta de referencia (SaaS) o de descarga (local), cubriendo todos los tipos de actividad: Project Management, Requirements Management, Product UX/UI Design, Software Development, Software Testing, Software Deployment y Software Documentation.

### 5.1.2. Source Code Management

**Pendiente:** repositorio GitHub por producto (Landing Page, Web Services, Frontend Web Applications) con URL; el repo de Web Services incluye el proyecto y sus archivos de pruebas. Implementar **GitFlow** (convenciones para feature/release/hotfix branches), **Semantic Versioning** para releases y **Conventional Commits** para los mensajes.

### 5.1.3. Source Code Style Guide &amp; Conventions

**Pendiente:** convenciones de nomenclatura y estilo para los lenguajes de la solución (HTML, CSS, JavaScript, C# y Gherkin), con nomenclatura en inglés y referencias a guías estándar.

### 5.1.4. Software Deployment Configuration

**Pendiente:** pasos para lograr el despliegue/publicación satisfactorio de cada producto digital (Landing Page, Web Services, Frontend Web Applications) a partir de los repositorios de código fuente.

## 5.2. Product Implementation &amp; Deployment

**Pendiente:** documentar la implementación, pruebas, documentación y despliegue de la Landing Page, Web Services y Frontend Web Applications. Una vez exista el Product Backlog, se incluye una sección interna por cada Sprint (Sprint 1, Sprint 2, …).

> **Acuerdo de Servicio – SaaS (se incorpora en el Trabajo Parcial, numeración canónica 5.2.4):** acuerdo que establece los derechos, obligaciones y restricciones aplicables a los usuarios de la plataforma; debe integrarse públicamente en la sección "Terms and Conditions" del website, cumpliendo con los criterios de claridad, accesibilidad y cumplimiento normativo.

<!-- Evidencia candidata en repo remoto (assets/Chapter-IV/): appAndroid1-8, sprint3-app-1..4, sprint3-development-evidence.png, sprint3-team-collaboration.png, insights.png, render.png, swager*.png (= Swagger); assets/ raíz: trello.jpg, trello2.jpg. -->

### 5.2.1. Sprint Backlogs

**Pendiente:** por sprint, documentar:

- **Sprint Planning n:** cuadro resumen con Sprint Planning Background (Date YYYY-MM-DD, Time, Location, Prepared By, Attendees), Sprint n–1 Review Summary y Retrospective Summary, Sprint Goal (redactado con el template de scrum.org: Outcome / Impact / Customer(s) / Event, + métrica de cumplimiento), Sprint Velocity y Sum of Story Points.
- **Aspect Leaders and Collaborators (LACX):** matriz por sprint (Team Member | GitHub Username | Aspect Name (L/C)) cuya organización L/C se relaciona con la selección de tasks.
- **Sprint Backlog n:** screenshot y URL pública del board, tabla de User Stories con Work-items/Tasks (Id, Title, Description, Estimation en horas, Assigned To) y estados **To-do / In-Process / To-Review / Done**.
- **Development Evidence for Sprint Review:** tabla de commits por repositorio (Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on), con prefijos conventional commit (`feat:`).
- **Testing Suite Evidence for Sprint Review:** unit/integration/acceptance (BDD) ligados a User Stories del sprint, tabla de commits con prefijo `test:`, e ids de commits de testing.
- **Execution Evidence for Sprint Review:** screenshots de vistas principales + enlace a video (Microsoft Stream).
- **Services Documentation Evidence for Sprint Review:** endpoints con OpenAPI, tabla por endpoint con verbo HTTP, sintaxis, parámetros, ejemplo y explicación del response.
- **Software Deployment Evidence for Sprint Review:** capturas y pasos del despliegue del sprint (Landing, Web Apps y Web Services).
- **Team Collaboration Insights during Sprint:** analíticos de colaboración y commits de GitHub con interpretación redactada.

### 5.2.2. Implemented Landing Page Evidence

### 5.2.3. Implemented Frontend-Web Application Evidence

### 5.2.4. Implemented Native-Mobile Application Evidence

### 5.2.5. Implemented RESTful API and/or Serverless Backend Evidence

### 5.2.6. RESTful API documentation

**Pendiente:** documentación de la RESTful API con **OpenAPI Specification vía Swagger** (evidencia desplegada o URL local).

### 5.2.7. Team Collaboration Insights

**Pendiente:** analíticos de colaboración/commits de GitHub por sprint, con interpretación.

## 5.3. Video About-the-Product

**Pendiente:** video promocional según Anexo C del enunciado (nomenclatura `…-about-the-product-sprint-<n>`, `.mp4`, 1 a 3 minutos, orientación promocional, ≥ 1 opinión por segmento objetivo, testimonio de un usuario de las entrevistas de validación). Subir a Microsoft Stream y YouTube; incrustar en la Landing Page. En el informe: screenshot, URL y timing.
