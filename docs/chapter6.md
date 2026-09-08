# Capítulo VI: Product Verification & Validation

## 6.1. Testing Suites & Validation

Este capítulo documenta la estrategia de pruebas automatizadas que sustenta la validación del producto SmartStay. La estrategia se organiza según los siguientes niveles, cada uno asociado a las secciones del enunciado:

### 6.1.1. Core Entities Unit Tests

Pruebas unitarias sobre las **entidades principales** del dominio: validan cada componente de forma aislada (lógica de dominio, repositorios simulados, validaciones de negocio). Ejemplos en SmartStay: casos de uso de reserva, validación de check-in, cálculo de estados de habitación, reglas de RBAC.

### 6.1.2. Core Integration Tests

Pruebas de integración entre capas y servicios: backend + base de datos, backend + IoT Gateway (simulado), autenticación + tokens; validan la comunicación frontend-backend y la interacción entre servicios/APIs. Ejemplos en SmartStay: flujo de login JWT, creación de reserva, asignación de habitación, endpoint de control de puerta.

### 6.1.3. Core Behavior-Driven Development

Pruebas E2E / de aceptación que validan flujos completos desde la perspectiva del usuario (check-in digital completo, control de habitación, solicitud de servicio, asignación de tarea por staff). El BDD se aplica definiendo el comportamiento esperado con archivos `.feature` en **Gherkin** y steps en lenguaje de programación (Cucumber, SpecFlow o similares), ligados a las User Stories del sprint correspondiente.

**Pendiente:** redactar los escenarios `.feature` y sus steps cuando existan los repositorios y builds de testing.

### 6.1.4. Core System Tests

**Pendiente:** pruebas de sistema de la aplicación completa en entorno **web y móvil**: navegación, interacción con APIs y respuesta del sistema en distintos escenarios.

### Criterios de aceptación por nivel

| Nivel | Criterio |
| :--- | :--- |
| Unit | Cobertura global ≥ umbral definido; pruebas críticas del dominio cubren casos felices y edge cases. |
| Integración | Cada flujo de negocio clave tiene al menos una prueba de integración que valida el contrato y el estado resultante. |
| E2E | Los flujos críticos identificados en el Capítulo VIII (check-in, control de habitación, room service) tienen pruebas automatizadas que validan el path feliz y los fallbacks más comunes. |

### Relación con los experimentos

El testing automatizado sirve dos propósitos en el contexto del curso de Experimentos:

1. **Garantía de calidad de la herramienta experimental:** la app usada en los experimentos es una versión que pasó pruebas automatizadas, reduciendo el riesgo de que los resultados del experimento se vean contaminados por fallas técnicas evitables.
2. **Métrica de proceso:** la tasa de pruebas pasadas, cobertura y tiempo de ejecución del pipeline son métricas de proceso que pueden incluirse en el análisis del experimento si es relevante (ej: estabilidad del build entre sesiones).

## 6.2. Static testing & Verification

### 6.2.1. Static Code Analysis

#### 6.2.1.1. Coding standard & Code conventions

**Pendiente:** verificar el cumplimiento de estándares del lenguaje/framework usados (p. ej. PEP8 para Python, ESLint para JavaScript): código legible, consistente y con buenas prácticas (nombres de variables, indentación, comentarios).

#### 6.2.1.2. Code Quality & Code Security

**Pendiente:** evaluar calidad por complejidad, duplicación y mantenibilidad con métricas/herramientas (p. ej. SonarQube, ESLint o Checkmarx) e identificar vulnerabilidades: inyecciones SQL, Cross-Site Scripting (XSS) y manejo inseguro de datos sensibles.

### 6.2.2. Reviews

**Pendiente:** documentar las revisiones de código/artefactos realizadas por el equipo.

## 6.3. Validation Interviews

**Pendiente:** registrar las entrevistas de validación en las que usuarios de los segmentos objetivo interactúan con la Landing Page y las aplicaciones, aplicando el formato de evaluación heurística del Anexo D del enunciado (usabilidad, arquitectura de información e inclusive design).

<!-- Evidencia candidata en repo remoto (assets/Chapter-IIII/): entrevista-1-admin.png, entrevista-1-cliente.png, entrevista-2-admin.png, android-studio-emulator.jpg; assets/ raíz: appexecution1-3. -->

### 6.3.1. Diseño de Entrevistas

**Pendiente:** por segmento objetivo, elementos a incluir en la sesión (Landing Page + aplicaciones) y los user flows que formarán parte de la validación.

### 6.3.2. Registro de Entrevistas

**Pendiente:** 3 a 5 entrevistas por segmento; por entrevista: nombres, apellidos, edad, distrito, screenshot de un cuadro de video y URL del video en Microsoft Stream con timing (inicio y duración), más resumen descriptivo de las apreciaciones del entrevistado.

### 6.3.3. Evaluaciones según heurísticas

**Pendiente:** evaluación de las sesiones de validación según el formato del Anexo D (UX Heuristics & Principles Evaluation — Usability / Inclusive Design / Information Architecture): escala de severidad 1–4, tabla resumen (Problema, Severidad, Heurística violada) y descripción de problemas con capturas y recomendaciones.

## 6.4. Auditoría de Experiencias de Usuario

**Pendiente:** auditoría UX entre grupos según el enunciado (se realiza en Avance 2).

### 6.4.1. Auditoría realizada

#### 6.4.1.1. Información del grupo auditado

#### 6.4.1.2. Cronograma de auditoría realizada

#### 6.4.1.3. Contenido de auditoría realizada

### 6.4.2. Auditoría recibida

#### 6.4.2.1. Información del grupo auditor

#### 6.4.2.2. Cronograma de auditoría recibida

#### 6.4.2.3. Contenido de auditoría recibida

#### 6.4.2.4. Resumen de modificaciones para subsanar hallazgos
