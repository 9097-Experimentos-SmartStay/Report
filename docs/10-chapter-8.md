# Capítulo VIII: Experiment-Driven Development

Este capítulo aplica al producto SmartStay el enfoque de desarrollo guiado por experimentos. En lugar de decidir qué construir a partir de opiniones, el equipo formula preguntas sobre sus propias creencias, diseña experimentos acotados que puedan responderlas con datos y usa el pipeline descrito en el Capítulo VII para llevarlos a producción. La lógica del capítulo es: **primero se pregunta, después se diseña, luego se experimenta y al final se aprende**.

En este avance se presentan la planificación (8.1), el diseño (8.2) y las historias de usuario y el backlog To-Be que se derivan del diseño (8.3.1 y 8.3.2). La ejecución de los experimentos, el análisis de sus resultados y el aprendizaje continuo corresponden a las siguientes entregas.

## 8.1. Experiment Planning

### 8.1.1. As-Is Summary

El punto de partida es el estado actual del proyecto, descrito solo con lo que el equipo ha comprobado hasta el 09/11/2026.

**Qué existe.** SmartStay está desplegado en tres productos: una landing page (`https://smartstay-movildev-landing.vercel.app`), una aplicación web para staff y huéspedes (`https://smartstay-movildev-web.vercel.app`) y una API RESTful en Render. La aplicación móvil Flutter consume la misma API. El backend cubre inicio de sesión con doble factor para staff, configuración de hoteles y habitaciones, estados de habitación, reservas, pagos y solicitudes de demostración. El check-in digital quedó fuera del backlog actual, y el control del entorno de la habitación por IoT solo existe como un emulador (`IoTEmulator`) en la API.

**Qué sabemos de los usuarios (Capítulo II).**

| Segmento | Muestra | Hallazgo relevante para los experimentos |
| :--- | :---: | :--- |
| Administradores de hoteles boutique y pequeños | 3 | Hoteles de 12 a 19 habitaciones y equipos de 4 a 6 personas; el 66.7 % usa un sistema propio y el 33.3 % Excel y WhatsApp; el 100 % se muestra motivado a adoptar una herramienta y a pagar una suscripción si el costo se justifica. |
| Huéspedes de hoteles boutique | 4 | Edad promedio de 28 años; el 75 % señala las esperas largas en recepción como principal frustración. |

La muestra es pequeña: sirve para formular preguntas, no para afirmar lo que ocurre en toda la población.

**Qué mediciones técnicas existen hoy (Capítulos VI y VII).**

- Lighthouse del 09/11/2026: la landing page obtiene 81 en rendimiento móvil y 99 en escritorio; el login web, 80 y 98. La accesibilidad del login es 88 y su SEO, 83.
- 265 pruebas automatizadas del backend superadas en la última ejecución de CI sobre `develop`.
- Disponibilidad: 100 de las últimas 100 ejecuciones del scheduler terminaron con éxito.

**Qué no existe.** El equipo no tiene todavía analítica de uso en la landing page ni en la aplicación web, ni líneas base de conversión o de tiempo por tarea, ni entrevistas de validación con el producto desplegado (6.3). Esta carencia es precisamente la que el plan de este capítulo busca cerrar.

### 8.1.2. Raw Material: Assumptions, Knowledge Gaps, Ideas, Claims

El material bruto reúne lo que el equipo cree, ignora, propone o ha escuchado. El criterio es no probar la idea en sí, sino la premisa que la sostiene.

| Id | Tipo | Enunciado | Fuente |
| :-: | :--- | :--- | :--- |
| R-01 | Assumption | Una solicitud de demostración con menos campos obligatorios aumenta la cantidad de administradores que la completan. | El formulario actual de la landing exige ocho campos obligatorios (`firstName`, `lastName`, `hotelName`, `jobTitle`, `email`, `accommodationType`, `roomsRange`, `referralSource`) |
| R-02 | Assumption | Un huésped completa la reserva sin ayuda de recepción si ve claramente las noches y el total antes de confirmar. | Lean UX Assumption 3 (el acceso digital reduce las esperas) y entrevistas a huéspedes |
| R-03 | Assumption | El personal opera más rápido si ve el estado de todas las habitaciones y puede filtrarlas. | Lean UX Assumption 2 e Hypothesis H2 (mejora de 15 % en productividad) |
| R-04 | Assumption | Al huésped le importa más controlar el entorno de la habitación que otras funciones. | Lean UX Assumption 1 e Hypothesis H1 |
| R-05 | Assumption | El check-in digital reduce al menos 40 % el tiempo de check-in. | Lean UX Assumption 3 e Hypothesis H3 |
| R-06 | Claim | «Las esperas en recepción son la principal frustración del huésped.» | El 75 % de los huéspedes entrevistados |
| R-07 | Claim | «Pagaría una suscripción mensual si justifica la mejora operativa.» | El 100 % de los administradores entrevistados |
| R-08 | Idea | Mostrar el formulario de demostración dentro del hero, justo después de elegir el perfil «Administro un hotel». | Equipo, a partir de la landing segmentada (US-24) |
| R-09 | Idea | Añadir filtros por estado y cambio rápido de estado sobre el mapa de habitaciones. | Equipo, a partir del mapa de habitaciones del staff (US-06) |
| R-10 | Idea | Reducir el peso de imágenes y recursos que bloquean el render para bajar el LCP móvil. | Lighthouse del 09/11/2026 |
| R-11 | Knowledge Gap | No sabemos qué porcentaje de los visitantes de la landing page llega a enviar el formulario de demostración. | No hay analítica instalada |
| R-12 | Knowledge Gap | No sabemos cuánto tarda un huésped en completar una reserva ni cuántos la abandonan antes de confirmarla. | No hay analítica instalada |
| R-13 | Knowledge Gap | No sabemos cuánto tarda el staff en ubicar una habitación y cambiar su estado. | Sin mediciones; las entrevistas fueron cualitativas |
| R-14 | Knowledge Gap | No sabemos si un LCP móvil superior a 4 s hace que los visitantes abandonen la landing page. | Lighthouse mide el LCP, pero no el abandono |

Las suposiciones R-04 y R-05 no se pueden probar con el producto actual: el check-in digital está fuera del backlog y el control del entorno solo existe como emulador en la API. Se registran como pendientes para un ciclo posterior y no entran al backlog de preguntas de este avance.

### 8.1.3. Experiment-Ready Questions

Una pregunta lista para experimentar puede basarse en una creencia (*belief-led*) o ser exploratoria cuando todavía no hay creencia previa.

**Preguntas impulsadas por creencias.**

| Id | Pregunta | Creencia que prueba | Tipo |
| :-: | :--- | :--- | :--- |
| Q-01 | ¿Reducir los campos obligatorios del formulario de demostración aumenta la proporción de visitantes que lo envían? | R-01, R-08 | Belief-led |
| Q-02 | ¿Mostrar un resumen con las noches y el total antes de confirmar aumenta la proporción de reservas que el huésped completa? | R-02 | Belief-led |
| Q-03 | ¿Filtrar el mapa de habitaciones por estado y cambiarlo desde el propio mapa reduce el tiempo que tarda el staff en actualizar una habitación? | R-03, R-09 | Belief-led |
| Q-04 | ¿Reducir el LCP móvil de la landing page por debajo de 2.5 s aumenta la proporción de visitantes que navegan más allá del hero? | R-10, R-14 | Belief-led |

**Preguntas exploratorias.**

| Id | Pregunta | Brecha que atiende |
| :-: | :--- | :--- |
| Q-05 | ¿Qué porcentaje de los visitantes de la landing page envía el formulario de demostración hoy? | R-11 |
| Q-06 | ¿En qué paso del flujo de reserva abandonan los huéspedes? | R-12 |
| Q-07 | ¿Cuánto tardan el administrador y el personal de recepción en ubicar una habitación y cambiar su estado con la interfaz actual? | R-13 |

**Las cinco W y una H.** Para descubrir premisas ocultas detrás de Q-01 se aplicó la técnica con la pregunta «¿por qué abandona el formulario de demostración?».

| Pregunta | Resultado |
| :--- | :--- |
| ¿Quién? | Un administrador o gerente de un hotel boutique que llega desde la landing page |
| ¿Qué hace? | Abre el formulario, lo lee y decide si lo completa |
| ¿Dónde? | En la sección `#demo` de la landing page, desde celular o computadora |
| ¿Cuándo? | Después de elegir el perfil «Administro un hotel» y de revisar los beneficios |
| ¿Por qué? | Premisa oculta: el visitante todavía no está seguro de querer una demostración y los ocho campos obligatorios le piden demasiado esfuerzo para una decisión temprana |
| ¿Cómo? | Se mide con la proporción de formularios enviados frente a los formularios vistos |

La técnica generó una pregunta exploratoria adicional, ya incluida como Q-05, porque la premisa oculta no puede evaluarse mientras se ignore la tasa actual de envío.

### 8.1.4. Question Backlog

El Question Backlog ordena las preguntas por el valor de la respuesta, no por el costo de una solución. Cada pregunta lleva su **por qué**, que justifica el esfuerzo del experimento, y cuatro puntajes de 1 a 5:

- **Confianza (C):** cuánto cree el equipo que ya conoce la respuesta. Un valor alto resta prioridad.
- **Riesgo (R):** qué tan grave es equivocarse si la creencia es falsa.
- **Impacto (I):** cuánto cambia el negocio o el producto con la respuesta.
- **Interés (N):** cuánto le importa al equipo conocerla.

**Prioridad = (6 − C) + R + I + N.** En caso de empate prevalece la pregunta con mayor riesgo.

| Orden | Id | Por qué | C | R | I | N | Prioridad |
| :-: | :-: | :--- | :-: | :-: | :-: | :-: | :-: |
| 1 | Q-05 | Sin esta línea base no se puede interpretar ningún experimento sobre la landing page | 1 | 4 | 5 | 4 | 18 |
| 2 | Q-01 | El formulario de demostración es el único canal de captación comercial de la landing page | 3 | 4 | 5 | 5 | 17 |
| 3 | Q-06 | La reserva es la función central del huésped y no sabemos dónde se pierde | 2 | 4 | 5 | 4 | 17 |
| 4 | Q-02 | Un resumen claro es un cambio barato con posible efecto directo en la reserva | 3 | 3 | 5 | 4 | 15 |
| 5 | Q-03 | La productividad del staff es la promesa central frente a los hoteles | 3 | 3 | 4 | 5 | 15 |
| 6 | Q-07 | Sin tiempos actuales no se puede afirmar una mejora | 2 | 3 | 4 | 3 | 14 |
| 7 | Q-04 | El LCP móvil es alto, pero no se sabe si afecta a los visitantes | 3 | 2 | 3 | 4 | 12 |

Los empates en 17 y en 15 no se pudieron resolver por riesgo, porque los pares tienen el mismo riesgo. Q-01 quedó antes que Q-06 por su mayor interés, y Q-02 antes que Q-03 por su menor costo de implementación.

**Backlog amplio y profundo.** El backlog *broad* contiene las siete preguntas, para ver el panorama. El backlog *deep* se limita a las tres preguntas con una variable manipulable y una métrica del dominio ya definida (8.2.2): Q-01, Q-02 y Q-03. Las demás se resuelven con medición, sin cambiar el producto: Q-05, Q-06 y Q-07 son líneas base que se obtienen con el mismo seguimiento que habilita los experimentos, y Q-04 se pospone hasta contar con esa medición.

### 8.1.5. Experiment Cards

Cada tarjeta resume el experimento antes de ejecutarlo. El **frente** contiene la pregunta, el por qué, la hipótesis y el Simplest Useful Thing. El **reverso** contiene las medidas, las condiciones y la escala, que se justifican en 8.2.

#### Experiment Card E-01: Formulario de demostración corto

| **Frente** | |
| :--- | :--- |
| Pregunta | Q-01: ¿reducir los campos obligatorios del formulario de demostración aumenta la proporción de visitantes que lo envían? |
| Por qué | El formulario es el único canal de captación comercial. Ocho campos obligatorios pueden frenar una decisión que todavía es temprana. |
| Hipótesis | Creemos que si el formulario de demostración solo exige nombre, apellido, correo y nombre del hotel, más administradores lo enviarán. Sabremos que es cierto si la tasa de envío del formulario corto llega al 20 % o más. |
| Qué (Simplest Useful Thing) | Una variante del formulario que marca como opcionales `jobTitle`, `accommodationType`, `roomsRange` y `referralSource`, sin cambiar el diseño visual. |

| **Reverso** | |
| :--- | :--- |
| Medidas | M-01 Tasa de envío del formulario de demostración (principal); M-02 tasa de visitantes que llegan a la sección `#demo` (secundaria); M-07 porcentaje de solicitudes con todos los campos completos (de control) |
| Condiciones | Control: formulario actual. Experimental: formulario corto. Asignación aleatoria 50/50 por visitante |
| Escala | 199 visitantes por grupo (398 en total), nivel de significancia 5 %, potencia 80 %, MDE de 10 puntos porcentuales sobre una línea base supuesta de 10 % |

#### Experiment Card E-02: Resumen de reserva antes de confirmar

| **Frente** | |
| :--- | :--- |
| Pregunta | Q-02: ¿mostrar un resumen con las noches y el total antes de confirmar aumenta la proporción de reservas que el huésped completa? |
| Por qué | La reserva es la función central del huésped. Un huésped que duda del total abandona sin pedir ayuda. La política de cancelación ya se muestra en el detalle de la habitación (revisión del 09/11/2026), por lo que el resumen se concentra en las fechas, las noches y el total. |
| Hipótesis | Creemos que si el huésped ve un resumen con las fechas, las noches, el precio por noche y el total antes de confirmar, completará más reservas. Sabremos que es cierto si la tasa de reservas completadas llega al 75 % o más. |
| Qué (Simplest Useful Thing) | Un paso de resumen entre la selección de habitación y el botón de confirmar, con datos que la API ya entrega. |

| **Reverso** | |
| :--- | :--- |
| Medidas | M-03 Tasa de finalización de la reserva (principal); M-04 tiempo hasta completar la reserva (secundaria); M-08 tasa de cancelación de reservas sin pago (de control) |
| Condiciones | Control: flujo actual. Experimental: flujo con paso de resumen. Asignación aleatoria 50/50 por huésped autenticado |
| Escala | 152 huéspedes por grupo (304 en total), nivel de significancia 5 %, potencia 80 %, MDE de 15 puntos porcentuales sobre una línea base supuesta de 60 % |

#### Experiment Card E-03: Filtros y cambio rápido de estado en el mapa de habitaciones

| **Frente** | |
| :--- | :--- |
| Pregunta | Q-03: ¿filtrar el mapa de habitaciones por estado y cambiarlo desde el propio mapa reduce el tiempo que tarda el staff en actualizar una habitación? |
| Por qué | La promesa central frente a los hoteles es la visibilidad en tiempo real y la productividad del personal (Hypothesis H2). |
| Hipótesis | Creemos que si el staff puede filtrar el mapa por estado y cambiarlo desde el propio mapa, actualizará las habitaciones más rápido. Sabremos que es cierto si el tiempo medio para localizar y actualizar una habitación es al menos 15 segundos menor que con el mapa actual. |
| Qué (Simplest Useful Thing) | Un filtro por estado y un menú de cambio de estado sobre cada habitación del mapa existente. |

| **Reverso** | |
| :--- | :--- |
| Medidas | M-05 Tiempo para localizar y actualizar el estado de una habitación (principal); M-06 errores de transición de estado rechazados por el sistema (de control) |
| Condiciones | Control: mapa actual y cambio de estado desde la pantalla de la habitación. Experimental: mapa con filtros y cambio rápido. Diseño cruzado: cada participante usa ambas versiones en orden alterno |
| Escala | 63 tareas por condición, nivel de significancia 5 %, potencia 80 %, MDE de 15 segundos sobre una desviación estándar supuesta de 30 segundos |

---

<div style="page-break-after: always;"></div>

## 8.2. Experiment Design

### 8.2.1. Hypotheses

Cada hipótesis de trabajo (H1) se empareja con su hipótesis nula (H0), que afirma que el cambio no produce diferencia o que cualquier diferencia se debe al azar. Las hipótesis son falsificables, comprobables y especifican su medida. El objetivo es **probarlas**, y no demostrar que son verdaderas.

| Experimento | Hipótesis nula (H0) | Hipótesis de trabajo (H1) |
| :--- | :--- | :--- |
| E-01 | La tasa de envío del formulario corto es igual a la del formulario actual: p<sub>B</sub> = p<sub>A</sub>. | La tasa de envío del formulario corto es mayor que la del formulario actual: p<sub>B</sub> − p<sub>A</sub> ≥ 10 puntos porcentuales. |
| E-02 | La tasa de reservas completadas con el paso de resumen es igual a la del flujo actual: p<sub>B</sub> = p<sub>A</sub>. | La tasa de reservas completadas con el paso de resumen es mayor: p<sub>B</sub> − p<sub>A</sub> ≥ 15 puntos porcentuales. |
| E-03 | El tiempo medio para actualizar una habitación con filtros y cambio rápido es igual al del mapa actual: μ<sub>B</sub> = μ<sub>A</sub>. | El tiempo medio con filtros y cambio rápido es menor: μ<sub>A</sub> − μ<sub>B</sub> ≥ 15 segundos. |

Las pruebas se plantean a dos colas con α = 0.05. Para E-01 y E-02 se usa la comparación de dos proporciones y para E-03, la comparación de medias pareadas.

### 8.2.2. Domain Business Metrics

Todas las Experiment Cards solo pueden citar las métricas de esta sección. Cada una tiene su fórmula, su técnica de recolección y su meta.

| Id | Métrica | Fórmula | Técnica de recolección | Meta |
| :-: | :--- | :--- | :--- | :--- |
| M-01 | Tasa de envío del formulario de demostración | Solicitudes de demostración creadas ÷ visitantes únicos que vieron el formulario | Evento `demo_form_viewed` en la landing page y registros de `POST /api/v1/demo-requests` en el backend | ≥ 20 % |
| M-02 | Alcance de la sección de demostración | Visitantes únicos que llegan a `#demo` ÷ visitantes únicos de la landing page | Eventos `landing_viewed` y `demo_section_reached` | ≥ 40 % |
| M-03 | Tasa de finalización de la reserva | Reservas creadas ÷ flujos de reserva iniciados | Evento `booking_flow_started` y registros de la tabla de reservas | ≥ 75 % |
| M-04 | Tiempo hasta completar la reserva | Mediana de (instante de creación de la reserva − instante de `booking_flow_started`) | Marcas de tiempo de los eventos y de la reserva | ≤ 120 s |
| M-05 | Tiempo para actualizar una habitación | Mediana de (cambio de estado confirmado − inicio de la tarea) | Cronometraje en la sesión de prueba y evento `room_status_changed` | ≤ 15 s |
| M-06 | Transiciones de estado rechazadas | Cambios de estado rechazados ÷ cambios de estado intentados | Respuestas de error de la API al cambiar el estado | ≤ 5 % |
| M-07 | Solicitudes de demostración completas | Solicitudes con los ocho campos informados ÷ solicitudes creadas | Registros de solicitudes de demostración en el backend | Solo seguimiento |
| M-08 | Cancelación de reservas sin pago | Reservas expiradas o canceladas sin pago ÷ reservas creadas | Estados de la reserva en el backend y proceso de expiración de `scheduler.yml` | ≤ 30 % |

Las metas son valores de trabajo que el equipo ajustará cuando se obtengan las líneas base de Q-05, Q-06 y Q-07. No son resultados observados.

### 8.2.3. Measures

Las medidas son la evidencia que responde la pregunta principal y detecta efectos secundarios. Se eligen solo las necesarias, durante el tiempo justo, para reducir costo y riesgo.

| Experimento | Medida principal | Medidas secundarias | Medida de control (*guardrail*) |
| :--- | :--- | :--- | :--- |
| E-01 | M-01 Tasa de envío | M-02 Alcance de la sección de demostración | M-07 Solicitudes completas: se vigila que el formulario corto no entregue solicitudes demasiado pobres para el equipo comercial |
| E-02 | M-03 Tasa de finalización | M-04 Tiempo hasta completar | M-08 Cancelación sin pago: se vigila que el resumen no atraiga reservas que luego no se pagan |
| E-03 | M-05 Tiempo para actualizar | Número de clics por tarea | M-06 Transiciones rechazadas: se vigila que el cambio rápido no provoque errores operativos |

### 8.2.4. Conditions

| Experimento | Condición de control (H0 es cierta) | Condición experimental (evidencia a favor de H1) | Asignación |
| :--- | :--- | :--- | :--- |
| E-01 | Formulario con ocho campos obligatorios | Formulario con cuatro campos obligatorios (nombre, apellido, correo y nombre del hotel) | Aleatoria 50/50 por visitante; el grupo se guarda en el navegador para que el mismo visitante vea siempre la misma versión |
| E-02 | Flujo de reserva actual | Flujo con paso de resumen antes de confirmar | Aleatoria 50/50 por huésped autenticado, a partir del identificador de usuario |
| E-03 | Mapa de habitaciones actual | Mapa con filtros por estado y cambio rápido | Diseño cruzado: cada participante realiza las mismas tareas con las dos versiones, alternando el orden |

**Población.** E-01 se aplica a los visitantes de la landing page que eligen el perfil «Administro un hotel». E-02, a los huéspedes con cuenta que inician una reserva en la aplicación web. E-03, al personal con rol de administrador o recepción, en sesiones de prueba moderadas.

### 8.2.5. Scale Calculations and Decisions

La escala responde a dos preguntas: con qué certeza se quiere decidir y qué tan pequeño es el cambio que vale la pena detectar.

**Parámetros comunes.**

- **Nivel de significancia (α):** 5 %, prueba a dos colas, lo que da z<sub>α/2</sub> = 1.96. Controla el error Tipo I.
- **Potencia estadística (1 − β):** 80 %, lo que da z<sub>β</sub> = 0.84. Controla el error Tipo II. Se eligió el extremo inferior del rango habitual de 80 % a 95 % por el tamaño del tráfico que puede esperar un producto en etapa temprana.
- **Efecto mínimo detectable (MDE):** el cambio mínimo que justificaría el costo de mantener la variante.

**Fórmulas.**

Para comparar dos proporciones con tamaños iguales:

n = [ z<sub>α/2</sub> · √(2 p̄ (1 − p̄)) + z<sub>β</sub> · √(p<sub>1</sub>(1 − p<sub>1</sub>) + p<sub>2</sub>(1 − p<sub>2</sub>)) ]² ÷ (p<sub>2</sub> − p<sub>1</sub>)², con p̄ = (p<sub>1</sub> + p<sub>2</sub>) ÷ 2

Para comparar medias:

n = 2 (z<sub>α/2</sub> + z<sub>β</sub>)² σ² ÷ δ²

**Resultados.**

| Experimento | Línea base supuesta | MDE | Tamaño de muestra por grupo | Total |
| :--- | :--- | :--- | :---: | :---: |
| E-01 | p<sub>1</sub> = 10 % de envío | +10 puntos porcentuales (p<sub>2</sub> = 20 %) | 199 | 398 visitantes |
| E-02 | p<sub>1</sub> = 60 % de finalización | +15 puntos porcentuales (p<sub>2</sub> = 75 %) | 152 | 304 huéspedes |
| E-03 | σ = 30 s de desviación estándar | δ = 15 s | 63 | 126 tareas |

**Sensibilidad.** Si el equipo quisiera detectar un efecto menor, la muestra crece rápidamente, por lo que el MDE es la decisión de escala más costosa:

| Experimento | MDE alternativo | Muestra por grupo con 80 % de potencia | Con 90 % de potencia (MDE original) |
| :--- | :--- | :---: | :---: |
| E-01 | +5 puntos porcentuales | 686 | 266 |
| E-02 | +10 puntos porcentuales | 356 | 203 |
| E-03 | δ = 10 s | 142 | 85 |

**Decisiones de escala.**

1. Las líneas base (10 %, 60 % y σ = 30 s) son **supuestos de partida**, no mediciones. Se reemplazarán por los valores observados en las líneas base de Q-05, Q-06 y Q-07, y se recalculará la muestra antes de iniciar cada experimento.
2. El experimento se ejecuta hasta alcanzar la muestra calculada. No se detiene al ver un resultado favorable en el camino, porque mirar los datos antes de tiempo aumenta el error Tipo I.
3. Si el tráfico de la landing page no alcanza los 398 visitantes en un plazo razonable, el equipo prefiere mantener el MDE de 10 puntos y extender el plazo, y no aceptar un MDE mayor que haría el resultado poco útil.
4. Los datos de E-01 y E-02 provienen de usuarios reales del producto desplegado. Los de E-03 provienen de participantes de los segmentos objetivo en sesiones moderadas, no de integrantes del equipo.

### 8.2.6. Methods Selection

El método es la técnica; la pregunta es el objeto de investigación. El criterio es elegir **la cosa más simple y útil** que alcance la escala y las condiciones necesarias.

| Experimento | Método elegido | Por qué es suficiente | Alternativa descartada |
| :--- | :--- | :--- | :--- |
| E-01 | Prueba A/B en la landing page, con asignación por navegador | Mide el comportamiento real de visitantes y no requiere cuentas | Entrevistas: no entregan una tasa y la muestra es muy pequeña |
| E-02 | Prueba A/B en la aplicación web, con asignación por usuario | El identificador de usuario ya existe y permite una asignación estable | Prueba de usabilidad moderada: cuesta más por participante y no alcanza 304 huéspedes |
| E-03 | Prueba de usabilidad moderada con diseño cruzado | La muestra es pequeña (63 tareas por condición, es decir, unas 10 a 15 personas con varias tareas cada una) y el tiempo por tarea se mide con precisión | A/B en producción: los hoteles son pocos y las tareas, poco frecuentes |

**Reglas éticas y de integridad.**

- **Un solo experimento por persona y por tema.** E-01 (landing), E-02 (reserva del huésped) y E-03 (mapa de habitaciones del staff) actúan sobre pantallas y poblaciones distintas. Un mismo visitante no es expuesto a dos experimentos sobre el mismo tema.
- **No causar daño.** Ninguna variante oculta un precio, una condición o una advertencia. En E-02, la variante agrega información y nunca la quita. En E-03, el cambio rápido no omite las reglas de transición de estado del backend.
- **Datos mínimos.** Solo se registran los eventos necesarios para las métricas de 8.2.2, con un identificador anónimo y sin datos personales en los eventos de la landing page, en línea con la Ley N.º 29733, de Protección de Datos Personales.
- **Transparencia.** La landing page y la aplicación incluirán un aviso de qué se mide y con qué fin en los términos y condiciones.

### 8.2.7. Data Analytics: Goals, KPIs and Metrics Selection

La selección analítica busca economía de rastreo: se mide lo imprescindible para detectar el cambio buscado, y nada más.

| Meta del negocio | KPI | Métrica de 8.2.2 | Experimento | Decisión que habilita |
| :--- | :--- | :--- | :---: | :--- |
| Captar más hoteles interesados | Conversión de visitante a solicitud de demostración | M-01, M-02 | E-01 | Adoptar o descartar el formulario corto |
| Facilitar que el huésped reserve sin ayuda | Reservas completadas por flujo iniciado | M-03, M-04, M-08 | E-02 | Adoptar o descartar el paso de resumen |
| Mejorar la productividad del staff | Tiempo por tarea de gestión de habitaciones | M-05, M-06 | E-03 | Adoptar o descartar los filtros y el cambio rápido |

**Métricas que se decidió no medir.** Páginas vistas totales, tiempo en la página y clics sin relación con las tres decisiones anteriores: son métricas de vanidad que no cambian ninguna decisión del producto.

### 8.2.8. Web and Mobile Tracking Plan

El plan de seguimiento define qué eventos se registran, dónde y con qué propiedades. **Estado:** el backend ya conserva las solicitudes de demostración y las reservas con sus estados; los eventos de cliente aún no están implementados y corresponden a las historias de usuario de 8.3.1.

| Evento | Producto | Se dispara cuando | Propiedades | Métrica | Estado |
| :--- | :--- | :--- | :--- | :-: | :--- |
| `landing_viewed` | Landing page | Se carga la página | `variant`, `profile`, `locale`, `device` | M-02 | Por implementar |
| `demo_section_reached` | Landing page | La sección `#demo` entra en pantalla | `variant`, `profile` | M-02 | Por implementar |
| `demo_form_viewed` | Landing page | El formulario es visible por primera vez | `variant` | M-01 | Por implementar |
| `demo_request_submitted` | Landing page | El backend responde 201 a `POST /api/v1/demo-requests` | `variant`, `fields_completed` | M-01, M-07 | El registro en el backend existe; falta el evento con `variant` |
| `booking_flow_started` | Web y móvil | El huésped abre el detalle de una habitación y pulsa reservar | `variant`, `room_id`, `nights` | M-03, M-04 | Por implementar |
| `booking_summary_viewed` | Web | Se muestra el paso de resumen | `variant`, `total` | M-03 | Por implementar |
| `booking_created` | Web y móvil | La API crea la reserva | `variant`, `booking_id` | M-03, M-04 | La reserva existe en el backend; falta el evento con `variant` |
| `booking_cancelled_unpaid` | Backend | Una reserva expira o se cancela sin pago | `booking_id` | M-08 | Dato existente en el backend |
| `room_status_filter_used` | Web | El staff aplica un filtro de estado | `variant`, `status` | M-05 | Por implementar |
| `room_status_changed` | Web | El backend confirma un cambio de estado | `variant`, `from`, `to`, `duration_ms` | M-05, M-06 | Por implementar |
| `room_status_change_rejected` | Web | El backend rechaza una transición | `from`, `to`, `error_code` | M-06 | Por implementar |

**Principios del plan.**

- **Identificador anónimo.** La landing page usa un identificador aleatorio guardado en el navegador. La aplicación usa el identificador de usuario existente, sin enviarlo a terceros.
- **Una fuente de verdad.** Los eventos que ya existen como datos del backend (reservas, solicitudes de demostración) se leen del backend y no se duplican en el cliente.
- **Variante en todos los eventos.** Toda medida de un experimento incluye `variant` (`A` o `B`), para que el análisis separe los grupos.
- **Retención limitada.** Los eventos se conservan solo durante el experimento y su análisis.

---

<div style="page-break-after: always;"></div>

## 8.3. Experimentation

### 8.3.1. To-Be User Stories

Las historias To-Be se derivan del diseño de 8.2: cada una habilita una variante, un evento del plan de seguimiento o la lectura de resultados. Siguen el formato del Capítulo III y su numeración continúa desde US-60, para no coincidir con las historias existentes (US-01 a US-53).

<table>
  <tr>
    <th>Story ID</th>
    <th>Title</th>
    <th>Description</th>
    <th>Acceptance Criteria</th>
    <th>Related to (Epic ID)</th>
  </tr>

  <tr>
    <td>US-60</td>
    <td>Short demo request form variant</td>
    <td class="user-story-desc"><strong>As an</strong> interested visitor, <strong>I want</strong> to request a demo by filling only my name, email and hotel name <strong>so that</strong> I can start the conversation without a long form.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Required fields</strong><br>
      <strong>Given that</strong> I am assigned to variant B, <strong>when</strong> I open the demo form, <strong>then</strong> only first name, last name, email and hotel name are required and the remaining fields are marked optional.<br>
      <strong>Scenario 2: Successful submission</strong><br>
      <strong>Given that</strong> I filled the required fields, <strong>when</strong> I submit the form, <strong>then</strong> the request is registered with the same validations as variant A and I receive the immediate confirmation.<br>
      <strong>Scenario 3: Same variant for the same visitor</strong><br>
      <strong>Given that</strong> I was assigned to a variant, <strong>when</strong> I return to the landing page from the same browser, <strong>then</strong> I see the same form.
    </td>
    <td>EP-06</td>
  </tr>

  <tr>
    <td>US-61</td>
    <td>Landing page event tracking</td>
    <td class="user-story-desc"><strong>As a</strong> product owner, <strong>I want</strong> the landing page to record anonymous view and form events with their variant <strong>so that</strong> I can calculate the demo conversion.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Events recorded</strong><br>
      <strong>Given that</strong> a visitor loads the page, reaches the demo section and views the form, <strong>when</strong> each of these happens, <strong>then</strong> the events <code>landing_viewed</code>, <code>demo_section_reached</code> and <code>demo_form_viewed</code> are recorded once per visit with the variant.<br>
      <strong>Scenario 2: No personal data</strong><br>
      <strong>Given that</strong> an event is recorded, <strong>when</strong> I inspect its content, <strong>then</strong> it contains an anonymous identifier and no name, email or phone.<br>
      <strong>Scenario 3: Failure does not affect the visitor</strong><br>
      <strong>Given that</strong> the event service is unavailable, <strong>when</strong> the visitor uses the page, <strong>then</strong> the page keeps working and the form can still be submitted.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-62</td>
    <td>Variant assignment service</td>
    <td class="user-story-desc"><strong>As a</strong> product owner, <strong>I want</strong> users to be assigned to a variant randomly and consistently <strong>so that</strong> the groups of each experiment are comparable.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Balanced assignment</strong><br>
      <strong>Given that</strong> an experiment is active, <strong>when</strong> new users arrive, <strong>then</strong> they are assigned to variant A or B with a 50/50 split.<br>
      <strong>Scenario 2: Stable assignment</strong><br>
      <strong>Given that</strong> a user has a variant, <strong>when</strong> the user returns, <strong>then</strong> the same variant is shown.<br>
      <strong>Scenario 3: Experiment switch</strong><br>
      <strong>Given that</strong> an experiment is not active, <strong>when</strong> a user arrives, <strong>then</strong> the control version is shown and no variant is recorded.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-63</td>
    <td>Booking summary before confirmation</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> to see the dates, nights, nightly price and total before I confirm <strong>so that</strong> I book with confidence.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Summary shown</strong><br>
      <strong>Given that</strong> I selected a room and dates and I am in variant B, <strong>when</strong> I continue, <strong>then</strong> I see a summary with the dates, number of nights, price per night and total.<br>
      <strong>Scenario 2: Total matches the booking</strong><br>
      <strong>Given that</strong> I confirm from the summary, <strong>when</strong> the booking is created, <strong>then</strong> the booking total equals the total shown in the summary.<br>
      <strong>Scenario 3: Back without losing data</strong><br>
      <strong>Given that</strong> I am in the summary, <strong>when</strong> I go back to change the dates, <strong>then</strong> my previous selection is kept.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-64</td>
    <td>Booking flow event tracking</td>
    <td class="user-story-desc"><strong>As a</strong> product owner, <strong>I want</strong> to record when a guest starts and completes a booking <strong>so that</strong> I can calculate the completion rate and the time to book.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Start and completion</strong><br>
      <strong>Given that</strong> a guest starts a booking, <strong>when</strong> the booking is created, <strong>then</strong> <code>booking_flow_started</code> and <code>booking_created</code> are recorded with their timestamps and the variant.<br>
      <strong>Scenario 2: Abandonment</strong><br>
      <strong>Given that</strong> a guest starts a booking, <strong>when</strong> the guest leaves without confirming, <strong>then</strong> only <code>booking_flow_started</code> exists for that flow.<br>
      <strong>Scenario 3: Mobile and web</strong><br>
      <strong>Given that</strong> a guest books from the mobile app or from the web, <strong>when</strong> the flow finishes, <strong>then</strong> the same events are recorded with the product that originated them.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-65</td>
    <td>Room status filter and quick change</td>
    <td class="user-story-desc"><strong>As a</strong> hotel staff member, <strong>I want</strong> to filter the room map by status and change a room's status from the map <strong>so that</strong> I update rooms faster.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Filter by status</strong><br>
      <strong>Given that</strong> I am in the room map in variant B, <strong>when</strong> I select a status, <strong>then</strong> only the rooms with that status are shown and the counts per status stay visible.<br>
      <strong>Scenario 2: Quick change</strong><br>
      <strong>Given that</strong> I selected a room, <strong>when</strong> I choose a new status from the room menu, <strong>then</strong> the change is applied with the same transition rules as in the room screen.<br>
      <strong>Scenario 3: Invalid transition</strong><br>
      <strong>Given that</strong> a transition is not allowed, <strong>when</strong> I attempt it from the map, <strong>then</strong> the system rejects it and explains why.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-66</td>
    <td>Room task timing instrumentation</td>
    <td class="user-story-desc"><strong>As a</strong> product owner, <strong>I want</strong> to record the duration and result of room status changes <strong>so that</strong> I can measure the time to update a room.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Duration recorded</strong><br>
      <strong>Given that</strong> a staff member changes a room's status, <strong>when</strong> the backend confirms it, <strong>then</strong> <code>room_status_changed</code> is recorded with the origin and destination status, the duration and the variant.<br>
      <strong>Scenario 2: Rejection recorded</strong><br>
      <strong>Given that</strong> the backend rejects a transition, <strong>when</strong> the response is received, <strong>then</strong> <code>room_status_change_rejected</code> is recorded with the error code.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-67</td>
    <td>Experiment metrics report</td>
    <td class="user-story-desc"><strong>As a</strong> product owner, <strong>I want</strong> a report of each domain metric split by variant <strong>so that</strong> I can analyze the result of an experiment.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Metrics by variant</strong><br>
      <strong>Given that</strong> an experiment has recorded events, <strong>when</strong> I request its report, <strong>then</strong> I get the sample size, the main metric and the guardrail metrics for variant A and variant B.<br>
      <strong>Scenario 2: Sample not reached</strong><br>
      <strong>Given that</strong> the planned sample size was not reached, <strong>when</strong> I request the report, <strong>then</strong> the report states that the result is not conclusive yet.<br>
      <strong>Scenario 3: Authorized access</strong><br>
      <strong>Given that</strong> I am not an administrator, <strong>when</strong> I request the report, <strong>then</strong> access is denied.
    </td>
    <td>EP-04</td>
  </tr>
</table>

### 8.3.2. To-Be Product Backlog

El backlog To-Be ordena las historias de 8.3.1 según su dependencia con los experimentos: primero el seguimiento y la asignación, que habilitan todas las medidas, y después las variantes. Los puntos de historia siguen la escala 1 / 2 / 3 / 5 / 8 del Capítulo III.

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Order</th>
      <th>User Story Id</th>
      <th>Title</th>
      <th>Description</th>
      <th>Experiment</th>
      <th>Story Points (1 / 2 / 3 / 5 / 8)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>US-62</td>
      <td>Variant assignment service</td>
      <td><strong>As a</strong> product owner, <strong>I want</strong> users to be assigned to a variant randomly and consistently <strong>to</strong> compare comparable groups.</td>
      <td>E-01, E-02, E-03</td>
      <td>3</td>
    </tr>
    <tr>
      <td>2</td>
      <td>US-61</td>
      <td>Landing page event tracking</td>
      <td><strong>As a</strong> product owner, <strong>I want</strong> the landing page to record anonymous view and form events <strong>to</strong> calculate the demo conversion.</td>
      <td>E-01</td>
      <td>3</td>
    </tr>
    <tr>
      <td>3</td>
      <td>US-64</td>
      <td>Booking flow event tracking</td>
      <td><strong>As a</strong> product owner, <strong>I want</strong> to record when a guest starts and completes a booking <strong>to</strong> calculate the completion rate.</td>
      <td>E-02</td>
      <td>3</td>
    </tr>
    <tr>
      <td>4</td>
      <td>US-66</td>
      <td>Room task timing instrumentation</td>
      <td><strong>As a</strong> product owner, <strong>I want</strong> to record the duration and result of room status changes <strong>to</strong> measure the time to update a room.</td>
      <td>E-03</td>
      <td>2</td>
    </tr>
    <tr>
      <td>5</td>
      <td>US-60</td>
      <td>Short demo request form variant</td>
      <td><strong>As an</strong> interested visitor, <strong>I want</strong> to request a demo by filling only my name, email and hotel name <strong>to</strong> start the conversation without a long form.</td>
      <td>E-01</td>
      <td>2</td>
    </tr>
    <tr>
      <td>6</td>
      <td>US-63</td>
      <td>Booking summary before confirmation</td>
      <td><strong>As a</strong> guest, <strong>I want</strong> to see the dates, nights, price and total before I confirm <strong>to</strong> book with confidence.</td>
      <td>E-02</td>
      <td>3</td>
    </tr>
    <tr>
      <td>7</td>
      <td>US-65</td>
      <td>Room status filter and quick change</td>
      <td><strong>As a</strong> hotel staff member, <strong>I want</strong> to filter the room map by status and change a room's status from the map <strong>to</strong> update rooms faster.</td>
      <td>E-03</td>
      <td>5</td>
    </tr>
    <tr>
      <td>8</td>
      <td>US-67</td>
      <td>Experiment metrics report</td>
      <td><strong>As a</strong> product owner, <strong>I want</strong> a report of each domain metric split by variant <strong>to</strong> analyze the result of an experiment.</td>
      <td>E-01, E-02, E-03</td>
      <td>5</td>
    </tr>
  </tbody>
</table>

**Total de puntos del backlog To-Be:** 26.

**Criterio de orden.** Las historias 1 a 4 son prerrequisitos de medición: sin asignación de variantes ni eventos, ninguna variante produce evidencia utilizable. Las historias 5 a 7 son las variantes de los tres experimentos, y la historia 8 cierra el ciclo con el análisis.
