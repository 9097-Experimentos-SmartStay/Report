# Capítulo VII: DevOps Practices

## 7.1. Continuous Integration

### 7.1.1. Tools and Practices

El pipeline de integración y despliegue continuo tiene como propósito:

- Automatizar la construcción de las aplicaciones móviles (Android / Flutter) y del backend.
- Ejecutar la suite de pruebas en cada cambio.
- Validar que las métricas de calidad (cobertura, lint, pruebas pasadas) cumplen umbral mínimo antes de integrar.
- Desplegar versiones a entornos de prueba (alpha/beta) para soportar los experimentos del Capítulo VIII.
- Proveer evidencia trazable de cada build asociada a un experimento.

Prácticas habilitantes del enunciado: GIT + GitHub con **GitFlow**, **Conventional Commits** y **Semantic Versioning**.

**Pendiente:** detallar las herramientas concretas de CI seleccionadas por el equipo y su configuración.

### 7.1.2. Build & Test Suite Pipeline Components

> **Pendiente:** insertar diagrama del pipeline (no existe un candidato en el repo de assets; el equipo debe crear `assets/chapter-7/pipeline.png` o equivalente).

Etapas propuestas del pipeline:

| Etapa | Descripción |
| :--- | :--- |
| **1. Checkout / Trigger** | El pipeline se activa por push a ramas configuradas (main, develop, feature/*) o por PR. |
| **2. Build** | Compilación de apps móviles y backend; resolución de dependencias; generación de artefactos. |
| **3. Static Analysis / Lint** | Análisis estático de código, linting, revisión de estilo y reglas de negocio críticas. |
| **4. Unit Tests** | Ejecución de pruebas unitarias (Android: JUnit; Flutter: widget/unit tests; backend .NET: xUnit o equivalente). |
| **5. Integration Tests** | Pruebas de integración con servicios reales o simulados, incluyendo endpoints y lógica de dominio. |
| **6. E2E / UI Tests (si aplica)** | Pruebas de extremo a extremo en emulador/dispositivo real o mediante herramientas automatizadas. |
| **7. Quality Gates** | Evaluación de cobertura, tasa de fallos, y métricas definidas para aprobar o rechazar la integración. |
| **8. Artifact Publish** | Publicación de artefactos (APK/AAB, backend, reports) a un registro o repositorio de builds. *(Corresponde a la entrega continua — 7.2.2.)* |
| **9. Deploy (Alpha/Beta)** | Despliegue a un entorno controlado para ejecución de experimentos con usuarios reales o testers. *(Corresponde a la entrega continua — 7.2.2.)* |

> Nota: la tabla consolidada cubre las etapas de build & test (1–7) y las de publicación/despliegue pre-producción (8–9); al formalizar cada sección del capítulo con evidencia real, las etapas se distribuyen en 7.1.2, 7.2.2 y 7.3.2 según corresponda.

#### Relación con los experimentos

Cada experimento del Capítulo VIII debe poder ejecutarse sobre una build específica y reproducible. El pipeline permite:

- Etiquetar builds asociadas a un experimento (ej: `exp-01-checkin`, `exp-02-operativa`, `exp-03-usabilidad`).
- Capturar las métricas de build y de pruebas automáticas como parte de la evidencia del experimento.
- Garantizar que la versión evaluada con usuarios es la misma que pasó los gates de calidad.

#### Registro de builds y trazabilidad

Se propone mantener un registro mínimo por build (formato propuesto; **los valores del ejemplo son ilustrativos y deben reemplazarse por builds reales**, no constituyen evidencia):

| Campo | Ejemplo |
| :--- | :--- |
| Build ID | `build-20260905-001` |
| Commit SHA | `[sha real del commit]` |
| Rama | `feature/exp-01-checkin` |
| Experimento asociado | `EXP-01-checkin-digital` |
| Estado de tests | *(por completar con resultados reales)* |
| Cobertura | ≥ 80% (umbral de gate) |
| Artefactos | APK debug firmado, logs, reporte de pruebas |

## 7.2. Continuous Delivery

### 7.2.1. Tools and Practices

**Pendiente:** detallar las herramientas y prácticas de entrega continua (publicación de artefactos y despliegue a entornos pre-producción).

### 7.2.2. Stages Deployment Pipeline Components

**Pendiente:** documentar los componentes de despliegue por etapas (staging/alpha/beta) con evidencia. El diseño propuesto corresponde a las etapas 8 y 9 del pipeline consolidado en 7.1.2.

## 7.3. Continuous deployment

### 7.3.1. Tools and Practices

**Pendiente:** herramientas y prácticas de despliegue continuo a producción.

### 7.3.2. Production Deployment Pipeline Components

**Pendiente:** componentes del pipeline de despliegue a producción (Landing Page, Web Apps y Web Services) con evidencia de las configuraciones (cuentas, recursos en cloud, automatización del deployment).

<!-- Evidencia candidata en repo remoto (assets/ raíz y Chapter-IV/): render.png, insights.png, swager*.png, appAndroid*. -->

## 7.4. Continuous Monitoring

### 7.4.1. Tools and Practices

**Pendiente:** herramientas y prácticas de monitoreo continuo del pipeline y del producto desplegado.

### 7.4.2. Monitoring Pipeline Components

Métricas de proceso propuestas para caracterizar cómo se construyó y mantuvo la solución durante el ciclo del proyecto:

| Métrica | Descripción |
| :--- | :--- |
| **Tiempo de ejecución del pipeline** | Tiempo total desde trigger hasta artefacto desplegable. |
| **Tasa de build exitosas** | Porcentaje de builds que pasan los quality gates sin regressions críticas. |
| **Cobertura de pruebas** | Porcentaje de código o de lógica crítica cubierto por pruebas automatizadas. |
| **Tiempo de feedback** | Tiempo que tarda un desarrollador en recibir feedback sobre un cambio (desde commit hasta resultado de pruebas). |
| **Estabilización** | Número de builds o commits necesarios para estabilizar un feature antes de una release experimental. |

Estas métricas son complementarias a las de los experimentos y sirven para evaluar la madurez del proceso de ingeniería que sostiene la experimentación.

### 7.4.3. Alerting Pipeline Components

**Pendiente:** componentes de alerta del monitoreo.

### 7.4.4. Notification Pipeline Components

**Pendiente:** componentes de notificación del monitoreo.
