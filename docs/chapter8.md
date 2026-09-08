# Capítulo VIII: Experiment-Driven Development

Este capítulo presenta el **diseño experimental** que sustenta la evaluación del producto SmartStay, en línea con la metodología de Experiment-Driven Development del curso. Se describen los experimentos planeados para validar las hipótesis identificadas en el Capítulo I, con su respectivo contexto, participantes, variables, métricas, instrumentos de recolección y análisis esperado.

La estructura se organiza en **tres experimentos principales**, cada uno documentado mediante *Experiment Cards*, *Gherkin scenarios* y una matriz de métricas asociada:

- **EXP-01 — Check-in digital** → valida la hipótesis **H3** del Capítulo I (reducción ≥ 40% del tiempo de check-in).
- **EXP-02 — Productividad del staff** → valida la hipótesis **H2** del Capítulo I (mejora ≥ 15% de la productividad).
- **EXP-03 — Usabilidad de la app del huésped** → hipótesis de usabilidad (SUS ≥ 68, completitud ≥ 90%), transversal y complementaria a la validación de H1 (satisfacción del huésped).

---

## Experimento 1 — Validación de la Experiencia de Check-in Digital

### Contexto y motivación

Una de las principales promesas de SmartStay es el **check-in digital**: el huésped puede ocupar su habitación sin pasar por recepción, usando la aplicación móvil y el mecanismo de acceso digital (autenticación + control de apertura de puerta).

La hipótesis de negocio asociada es (H3 del Capítulo I):

> **H3.** Si ofrecemos check-in digital y control de acceso mediante app, entonces el tiempo promedio de check-in se reduce al menos un 40% respecto al flujo tradicional en recepción.

Este experimento busca **validar o refutar H3** con datos reales o simulados, según la disponibilidad de hoteles piloto.

### Experiment Card

| Campo | Descripción |
| :--- | :--- |
| **Experiment ID** | EXP-01-checkin-digital |
| **Título** | Validación del tiempo de check-in con flujo digital vs. recepción tradicional |
| **Pregunta de investigación** | ¿En qué medida el check-in digital reduce el tiempo total de ingreso/registro del huésped? |
| **Por qué (why)** | El tiempo de espera en recepción es un factor documentado de frustración del huésped; reducirlo impacta satisfacción y operación. |
| **Qué (what)** | Comparación del tiempo total desde la llegada hasta que la habitación está lista para uso, entre el flujo físico (recepción → llave física) y el flujo digital (app → autenticación → apertura). |
| **Hipótesis (H3)** | El tiempo total con flujo digital será al menos 40% menor que con flujo tradicional en recepción. |
| **Tipo de experimento** | Cuasiexperimental con grupos comparables (o simulación controlada si no hay hotel piloto). |
| **Variable independiente** | Tipo de flujo: tradicional vs. digital. |
| **Variable dependiente** | Tiempo total de check-in (segundos), medida cronometrada. |
| **Variables de control** | Horario de llegada, tipo de huésped (nuevo vs. recurrente), número de huéspedes, estado del hotel (ocupación). |
| **Participantes objetivo** | Huéspedes que llegan a un hotel piloto implementando SmartStay (o simulación con usuarios reales en entorno controlado). |
| **Métrica principal** | Tiempo total de check-in (mean, median, p95). |
| **Métricas secundarias** | Satisfacción percibida (Likert 1–5), tasa de completitud sin intervención de staff, número de errores/rollback. |
| **Criterio de éxito** | Reducción ≥ 40% del tiempo total con significancia estadística (p < 0.05) y satisfacción ≥ 4/5. |
| **Riesgos / limitaciones** | Ausencia de hotel piloto, sesgo de selección, condiciones operativas no representativas. |

### Escenarios Gherkin

```gherkin
Feature: Check-in Digital con Control de Acceso

  Scenario: Huésped nuevo completa check-in digital sin intervención de recepción
    Given que el huésped tiene una reserva confirmada en el sistema SmartStay
    And el hotel está operativo y la habitación está lista
    When el huésped inicia sesión en la aplicación móvil
    And selecciona "Check-in Digital" para su reserva
    And autentica su identidad mediante los canales configurados
    Then el sistema valida la reserva y confirma la disponibilidad de la habitación
    And emite un token de acceso digital para la puerta de la habitación
    And el huésped puede abrir la puerta desde la aplicación
    And el check-in se registra automáticamente en el sistema con marca de tiempo
```

```gherkin
  Scenario: Fallback cuando el acceso digital falla
    Given que el huésped tiene una reserva confirmada
    And el mecanismo de apertura digital reporta falla de comunicación
    When el huésped intenta abrir la puerta desde la app
    And el intento falla por timeout de IoT Gateway
    Then el sistema notifica al huésped sobre el fallo
    And ofrece la opción de contactar a recepción o usar llave física de respaldo
    And registra el incidente para análisis posterior del experimento
```

### Diseño de la recolección de datos

| Aspecto | Detalle |
| :--- | :--- |
| **Instrumento** | Registro automático de timestamps en backend (eventos: checkin_iniciado, habitacion_lista, apertura_exitosa) + encuesta post-check-in (NPS / Likert). |
| **Muestreo** | Todos los check-ins del periodo experimental que cumplan criterios de inclusión (reserva confirmada, habitación lista). |
| **Frecuencia** | Por evento, continuo durante la ventana del experimento. |
| **Análisis** | Estadística descriptiva, prueba t de Student o Mann-Whitney U según distribución, intervalo de confianza del 95% para la diferencia de medias. |

### Plan de análisis

- Calcular tiempo total = `t_apertura - t_llego` para cada caso.
- Comparar distribución entre grupo tradicional y grupo digital.
- Evaluar satisfacción como variable complementaria.
- Documentar los casos anómalos y respaldarlos en el reporte final con carpetas de evidencia.

---

## Experimento 2 — Productividad del Personal Operativo con Información en Tiempo Real

### Contexto y motivación

El **staff operativo** (housekeeping, mantenimiento, recepción) trabaja con información fragmentada en muchos hoteles pequeños: ¿qué habitaciones están ocupadas, en limpieza, listas o en mantenimiento? Esta situación genera movimiento innecesario, retrasos y duplicidad de tareas.

La hipótesis asociada es (H2 del Capítulo I):

> **H2.** Si el personal operativo usa una aplicación móvil con visibilidad en tiempo real de las habitaciones, entonces la productividad en la asignación y ejecución de tareas mejora al menos un 15%.

### Experiment Card

| Campo | Descripción |
| :--- | :--- |
| **Experiment ID** | EXP-02-operativa-en-tiempo-real |
| **Título** | Validación de la productividad del staff con dashboard móvil en tiempo real |
| **Pregunta de investigación** | ¿Cuánto mejora la productividad operativa cuando el staff cuenta con información en tiempo real en su dispositivo móvil? |
| **Por qué (why)** | La falta de visibilidad en tiempo real genera asignación ineficiente de tareas, retrasos en check-out y habitaciones que quedan "ocupadas" más tiempo del necesario. |
| **Qué (what)** | Comparación del tiempo de ciclo de tareas de housekeeping y recepción con y sin la app de visibilidad en tiempo real. |
| **Hipótesis (H2)** | La productividad mejora ≥ 15% con la app de visibilidad en tiempo real. |
| **Tipo de experimento** | Comparación antes/después (pre/post) en misma operación, o grupos paralelos si hay más de un hotel. |
| **Variable independiente** | Disponibilidad de la app SmartStay para staff (con visibilidad VS sin ella / sistema anterior). |
| **Variable dependiente** | Productividad operativa medida como tareas completadas por unidad de tiempo, tiempo promedio por tarea, y tasa de retrabajo. |
| **Variables de control** | Tamaño del hotel, número de personal, régimen de ocupación, definición de tareas, entrenamiento previo. |
| **Participantes objetivo** | Personal de housekeeping, mantenimiento y recepción de hotel piloto. |
| **Métrica principal** | Tareas completadas por hora (o por turno) — baseline vs. experimental. |
| **Métricas secundarias** | Tiempo promedio por tarea (limpieza, asignación, check-out), tasa de tareas reabiertas, percepción de utilidad (encuesta interna). |
| **Criterio de éxito** | Mejora ≥ 15% en la métrica principal con significancia estadística y percepción interna ≥ 4/5. |
| **Riesgos / limitaciones** | Curva de aprendizaje del personal, resistencia al cambio, efecto Hawthorne. |

### Escenarios Gherkin

```gherkin
Feature: Visibilidad Operativa del Staff

  Scenario: Housekeeping recibe tarea asignada desde la app
    Given que el sistema marca una habitación como "check-out completado"
    And la habitación requiere limpieza antes del próximo check-in
    When el jefe de housekeeping ve el panel de tareas pendientes
    Then el sistema le asigna la habitación al personal disponible
    And el asignado recibe notificación push con detalles de la habitación
    And el asignado acepta la tarea en la app
    And la habitación pasa a estado "en limpieza" en el panel de todos
```

```gherkin
  Scenario: Recepción consulta estado en tiempo real para resolver consulta de huésped
    Given que un huésped pregunta en recepción por el estado de su solicitud de room service
    When el recepcionista consulta el estado en la app SmartStay
    Then el sistema muestra el estado actual y el tiempo estimado
    And el recepcionista puede comunicar información precisa al huésped
    And el registro de la consulta queda para métricas de servicio
```

### Diseño de la recolección de datos

| Aspecto | Detalle |
| :--- | :--- |
| **Instrumento** | Registros del sistema (eventos de tarea: asignada, aceptada, iniciada, completada), cronómetro de ciclo por tarea, encuesta de percepción al personal. |
| **Muestreo** | Turnos completos durante el periodo experimental. |
| **Frecuencia** | Por tarea, continuo. |
| **Análisis** | Comparación antes/después con prueba para medias pareadas o equivalente; análisis de variabilidad y calidad (tasa de retrabajo). |

### Plan de análisis

- Definir claramente el **baseline** (sistema actual o medición previa).
- Calcular métrica principal por turno y por tipo de tarea.
- Considerar el efecto de aprendizaje incluyendo una fase de aclimatación antes de medir.
- Reportar según rúbrica del curso: hipótesis, resultados, conclusión, limitaciones.

---

## Experimento 3 — Evaluación de Usabilidad y Experiencia de Usuario (UX) de la App del Huésped

### Contexto y motivación

Independientemente de la funcionalidad, la **calidad de la experiencia de usuario** determina la adopción real del producto. El Experimento 3 se enfoca en validar que la aplicación móvil del huésped cumple con estándares de usabilidad y que los usuarios pueden completar sus tareas críticas sin fricción significativa. Su hipótesis es transversal a los experimentos EXP-01 y EXP-02 (una app usable es prerequisito para medir sus métricas sin contaminación por errores de interacción) y complementa la validación de la hipótesis H1 del Capítulo I (satisfacción del huésped).

### Experiment Card

| Campo | Descripción |
| :--- | :--- |
| **Experiment ID** | EXP-03-usabilidad-app-huesped |
| **Título** | Evaluación de usabilidad y experiencia de usuario de la app móvil del huésped |
| **Pregunta de investigación** | ¿La aplicación móvil del huésped permite completar las tareas críticas (check-in, control de habitación, solicitud de servicios) con una experiencia usable y satisfactoria? |
| **Por qué (why)** | Una funcionalidad potente pero confusa no se adopta; la usabilidad es un factor determinante de valor percibido. |
| **Qué (what)** | Evaluación heurística + pruebas de usabilidad con usuarios reales o representativos, midiendo completitud, tiempo, errores y satisfacción. |
| **Hipótesis (EXP-03)** | Los usuarios pueden completar las tareas críticas con ≤ 1 error importante y una puntuación SUS ≥ 68. |
| **Tipo de experimento** | Evaluación de usabilidad con tareas definidas, con pruebas de usabilidad moderadas o no moderadas según recursos. |
| **Variable independiente** | Versión de la app evaluada (y task flow específico). |
| **Variable dependiente** | Completitud de tareas, tiempo por tarea, número de errores, puntuación SUS (System Usability Scale). |
| **Variables de control** | Perfil del usuario (familiaridad con apps de viaje/hotel), dispositivo, condiciones del entorno. |
| **Participantes objetivo** | Huéspedes potenciales o reales, representativos del segmento objetivo. |
| **Métrica principal** | Puntuación SUS global y tasa de completitud de tareas críticas. |
| **Métricas secundarias** | Tiempo por tarea, errores críticos, comentarios cualitativos, NPS percibido. |
| **Criterio de éxito** | SUS ≥ 68 (umbral aceptable) y completitud ≥ 90% en tareas críticas con ≤ 1 error crítico por sesión. |
| **Riesgos / limitaciones** | Sesgo de voluntarios, pequeña muestra, ambiente no representativo. |

### Escenarios Gherkin

```gherkin
Feature: Tareas Críticas del Huésped

  Scenario: El huésped controla la iluminación y temperatura de su habitación
    Given que el huésped ya realizó check-in y está dentro de la habitación
    And el sistema IoT Gateway está conectado y operativo
    When el huésped abre la sección de "Control de Habitación" en la app
    Then puede ver el estado actual de iluminación y temperatura
    And puede ajustar la temperatura a un valor deseado
    And puede encender/apagar luces individualmente o por grupos
    And los cambios se reflejan físicamente en la habitación
```

```gherkin
  Scenario: El huésped solicita room service y recibe seguimiento
    Given que el huésped está en la app y tiene una reserva activa
    When selecciona "Solicitar Servicio" y elige tipo de servicio
    And confirma los detalles y el horario
    Then el sistema registra la solicitud y la asigna al canal correspondiente
    And el huésped puede ver el estado de la solicitud en tiempo real
    And recibe notificación cuando el servicio se completa
```

### Diseño de la recolección de datos

| Aspecto | Detalle |
| :--- | :--- |
| **Instrumento** | Rúbrica de tareas (completada / no completada / con ayuda), cronómetro, registro de errores, cuestionario SUS, notas del moderador. |
| **Muestreo** | Sesiones individuales o grupales pequeñas, según recursos del equipo. |
| **Frecuencia** | Una sesión por participante, con entre 3 y 5 tareas críticas por sesión. |
| **Análisis** | Estadística descriptiva de completitud y tiempo; distribución de puntuaciones SUS; análisis cualitativo de patrones de error. |

### Plan de análisis

- Calcular el SUS por participante y el promedio global.
- Reportar por tarea: % completada sin ayuda, % con ayuda, % no completada.
- Identificar patrones de error recurrentes y proponer mejoras priorizadas.
- Relacionar los hallazgos con las hipótesis de Lean UX del Capítulo I.

---

## Matriz de métricas global de los experimentos

La siguiente tabla resume las métricas clave de los tres experimentos (sustenta la sección 8.2.2 Domain Business Metrics del enunciado; al formalizar, cada métrica debe definirse con fórmula de cálculo, técnica de recolección y meta deseada).

| Experimento | Hipótesis | Métrica principal | Métrica secundaria | Criterio de éxito |
| :--- | :--- | :--- | :--- | :--- |
| EXP-01 — Check-in digital | H3: reducción ≥ 40% del tiempo | Tiempo total de check-in (mean, median, p95) | Satisfacción (Likert), tasa de completitud sin staff, errores | ≥ 40% reducción + satisfacción ≥ 4/5 + significancia estadística |
| EXP-02 — Operativa en tiempo real | H2: productividad ≥ 15% | Tareas completadas por unidad de tiempo | Tiempo por tarea, tasa de retrabajo, percepción interna | ≥ 15% mejora + significancia estadística + percepción ≥ 4/5 |
| EXP-03 — Usabilidad app | Hipótesis de usabilidad (SUS ≥ 68, ≤ 1 error crítico) | Puntuación SUS, tasa de completitud | Tiempo por tarea, errores críticos, comentarios cualitativos | SUS ≥ 68, completitud ≥ 90%, ≤ 1 error crítico por sesión |

---

## Consideraciones éticas y logísticas

**Insumo para la Matriz de Evaluación Ética y de Impacto** que el enunciado exige en la fase de experimentación (Anexo F: dimensiones de salud pública y seguridad, inclusión y accesibilidad, impacto social/cultural, económico, ambiental antrópico, enfoque global, y revelación de peligros y responsabilidad).

- **Consentimiento informado:** todos los participantes (huéspedes y personal) deben consentir la recolección de datos y ser informados sobre el propósito del experimento.
- **Privacidad:** los datos operativos y de uso no deben exponer información personal identificable sin consentimiento explícito.
- **Seguridad:** los experimentos que involucren acceso a habitaciones deben garantizar que los mecanismos de respaldo (llave física, recepción) funcionen en todo momento.
- **Viabilidad:** ante la ausencia de hotel piloto, los experimentos pueden ejecutarse como simulaciones controladas o pruebas con usuarios representativos, documentando la limitación en el reporte final.

---

<div style="page-break-after: always;"></div>
