# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup

La startup Movildev, con su producto SmartStay, surge con el objetivo de transformar la gestión hotelera mediante el uso de tecnologías digitales e Internet of Things (IoT). Nuestra propuesta integra en una sola solución la administración de huéspedes, control de habitaciones y servicios mediante una arquitectura de microservicios y conectividad constante.

A diferencia de soluciones tradicionales, SmartStay se enfoca en una experiencia móvil robusta, ofreciendo una aplicación nativa en Android (Kotlin) para la gestión operativa del personal y una aplicación multiplataforma en Flutter para el autoservicio y confort del huésped. A través de estas interfaces, el hotel puede optimizar recursos y, al mismo tiempo, ofrecer experiencias personalizadas y automatizadas que elevan el estándar de hospitalidad.

Entre sus principales características destacan:

- **Gestión de Acceso Digital:** Registro automático y control de acceso a habitaciones desde dispositivos móviles.
- **Control de Entorno IoT:** Monitoreo y ajuste de temperatura, iluminación y consumo energético de forma remota.
- **Servicios Personalizados:** Integración de room service y programación de limpieza con notificaciones en tiempo real.
- **Optimización Operativa:** Tableros de estado para identificación inmediata de habitaciones libres o en mantenimiento.

### 1.1.2. Perfiles de integrantes del equipo

<table border>
  <thead>
    <tr>
      <th>Foto</th>
      <th>Nombre completo</th>
      <th>Código</th>
      <th>Carrera</th>
      <th>Habilidades técnicas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" valign="middle">
       <img src="../assets/chapter-1/members/samuel-bonifacio-jaramillo.png" alt="Bonifacio Jaramillo Samuel Jesus" width="300">
      </td>
      <td>Bonifacio Jaramillo Samuel Jesus</td>
      <td>u202317269</td>
      <td>Ingeniería de Software</td>
      <td>Soy Desarrollador full stack orientado a soluciones de IA. Amplia experiencia en pipelines automatizados y experimentos con LLMs. Actualmente desarrollando workflows inteligentes.</td>
    </tr>
    <tr>
      <td></td>
      <td>Ponce Perales, Alberto Alejandro</td>
      <td>u202320684</td>
      <td>Ingeniería de Software</td>
      <td>Estudiante de la carrera de Ingeniería de Software en la UPC. Actualmente cuento con conocimientos en lenguajes de programación como C++ y manejo de Java. Considero que mis mayores virtudes son: la responsabilidad, capacidad de adaptarme, trabajar en equipo y la resiliencia.</td>
    </tr>
    <tr>
      <td></td>
      <td>Verona Flores, Ítalo Sebastián</td>
      <td>u20221e617</td>
      <td>Ingeniería de Software</td>
      <td>[Completar]</td>
    </tr>
    <tr>
      <td align="center" valign="middle">
       <img src="../assets/chapter-1/members/piero-sulca.jpg" alt="Sulca Sanchez Piero Angel" width="300">
      </td>
      <td>Sulca Sanchez, Piero Angel</td>
      <td>u202423711</td>
      <td>Ingeniería de Software</td>
      <td>Curso la carrera de Ingeniería de Software y tengo experiencia en desarrollo web trabajando con equipos pequeños. Me apasiona el Front End, sobre todo cuando hay espacio para el diseño creativo: interfaces 3D, animaciones, productos que se ven y se sienten distintos. En el equipo puedo aportar en levantamiento de requerimientos, diseño de interfaces, desarrollo web con React y TypeScript, diseño de bases de datos. En el equipo aporto organización y colaboración. </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
       <img src="../assets/chapter-1/members/alejandro-galindo.jpg" alt="Galindo Montero Alejandro Manuel" width="300">
      </td>
      <td>Galindo Manuel, Alejandro</td>
      <td>u202321264</td>
      <td>Ingeniería de Software</td>
      <td>Mi nombre es Alejandro Manuel Galindo Montero, tengo 22 años y curso la carrera de Ingeniería de Software. Me considero una persona creativa y responsable, y en mis tiempos libres me gusta aprender cosas nuevas. Cuento con conocimientos en desarrollo web y móvil, además de experiencia en desarrollo full stack con C#, Java, TypeScript y Flutter. En este proyecto apoyaré con todos los conocimientos que he adquirido en los últimos años. </td>
    </tr>
  </tbody>
</table>

---

## 1.2. Solution Profile

### 1.2.1. Antecedentes y problemática

**Who? (¿Quiénes?)** El problema afecta al Staff Operativo (limpieza, administración, mantenimiento y recepción) y a los huéspedes que buscan autonomía. El Staff Operativo depende de procesos manuales que fragmentan la comunicación interna. Los huéspedes, por su parte, enfrentan una experiencia desconectada que limita su control sobre el entorno de la habitación y la interacción con los servicios del hotel.

**What? (¿Qué?)** El problema central es la nula movilidad y falta de integración digital en la gestión hotelera integral. Esto se traduce en una dependencia de terminales fijas, control ineficiente de habitaciones por falta de datos en tiempo real (IoT), y una experiencia del huésped desconectada de los servicios del hotel.

**Where? (¿Dónde?)** Ocurre en hoteles de tamaño mediano a grande, donde la complejidad operativa y el volumen de huéspedes hacen que los procesos manuales sean ineficientes. La falta de movilidad afecta tanto a las áreas de servicio como a las habitaciones, generando cuellos de botella en la gestión diaria.

**When? (¿Cuándo?)** Ocurre de manera continua las 24 horas. La ineficiencia se agudiza en momentos críticos como los procesos de check-in/check-out, horas pico de solicitudes de servicios, y temporadas de alta ocupación donde la respuesta inmediata es vital para la satisfacción.

**Why? (¿Por qué?)** Se debe a la dependencia de sistemas tradicionales (Legacy Systems) que no permiten la interoperabilidad. Existe una carencia de una arquitectura de software moderna que integre servicios RESTful con tecnología IoT, impidiendo el monitoreo de recursos y la personalización del confort del huésped de forma remota y automatizada.

**How? (¿Cómo?)** La falta de una solución móvil integrada genera ineficiencias operativas, pérdida de productividad y una experiencia del huésped fragmentada. El personal del hotel no puede acceder a información en tiempo real ni gestionar las habitaciones de manera eficiente, mientras que los huéspedes no pueden controlar su entorno ni interactuar con los servicios del hotel desde sus dispositivos móviles.

**How Much? (¿Cuánto?)** La ineficiencia genera una pérdida estimada del 15-20% en la productividad operativa y un aumento innecesario en los costos de suministros y energía por falta de monitoreo. Además, la baja calificación en la experiencia de usuario (User Experience) se traduce en una disminución de la lealtad del cliente y una pérdida de competitividad frente a hoteles tecnológicamente avanzados.

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements

**Problem Statement: Optimización de la Gestión Operativa y Experiencia del Huésped**

El equipo de SmartStay identificó que los hoteles boutique y de pequeña escala operan con sistemas fragmentados o manuales, lo que se refleja en:

- Horarios de check-in/check-out rígidos y con colas en recepción.
- Incapacidad de controlar el entorno de la habitación (luz, temperatura, electrodomésticos) desde el celular del huésped.
- Dificultad del personal operativo para obtener visibilidad en tiempo real de habitaciones ocupadas, disponibles y en mantenimiento.
- Falta de integración entre la reserva, la llegada física del huésped y la automatización de la habitación.

Estos factores impactan directamente en la percepción de calidad del hotel, en los tiempos operativos del personal y en el costo operativo por habitación.

---

#### 1.2.2.2. Lean UX Assumptions

El equipo plantea las siguientes suposiciones iniciales para validar con los usuarios reales del sistema:

1. **El huésped prioriza el control del entorno de la habitación** (luz, temperatura, entretenimiento) sobre otras funcionalidades menores.
2. **El personal operativo necesita visibilidad en tiempo real de habitaciones remotas** antes de iniciar tareas de limpieza o mantenimiento.
3. **La identificación y control de acceso digital reduce los tiempos de espera en el check-in** y elimina colas en recepción.
4. **La integración de un módulo IoT simplifica la operación del hotel** sin requerir infraestructura adicional costosa.
5. **Un sistema basado en roles permite aislar la información del huésped del personal** sin comprometer la seguridad ni la experiencia del usuario.

Estas suposiciones serán validadas o refutadas mediante entrevistas, prototipos y experimentos de uso durante el desarrollo del proyecto.

---

#### 1.2.2.3. Lean UX Hypothesis Statements

Para cada suposición planteamos una hipótesis comprobable:

- **H1.** Si ofrecemos control de habitación vía móvil (luz, temperatura, puerta), entonces la satisfacción del huésped aumenta al menos un 20% respecto a hoteles sin esa funcionalidad.
- **H2.** Si el personal operativo usa una aplicación móvil con estado en tiempo real de habitaciones, entonces la productividad en limpieza y asignación de tareas mejora al menos un 15%.
- **H3.** Si implementamos check-in digital y control de acceso (acceso a habitación mediante app), entonces el tiempo promedio de check-in se reduce al menos un 40%.
- **H4.** Si integramos un gateway IoT de bajo costo con la solución SmartStay, entonces el hotel puede ofrecer los beneficios de automatización sin invertir en sistemas POS/PMS tradicionales de adaptación costosa.

---

#### 1.2.2.4. Lean UX Canvas

![Lean UX Canvas](../assets/chapter-1/lean-ux/lean-ux-canvas.png)

---

## 1.3. Segmentos objetivo

SmartStay apunta a dos segmentos principales:

### Segmento 1 — Staff Operativo de Hoteles

- **Quiénes:** Recepcionistas, jefes de housekeeping, personal de mantenimiento, gerentes de operación.
- **Necesidades:** Visibilidad de habitaciones, asignación rápida de tareas, control de accesos, reportes de consumo energético y estado de IoT.
- **Propuesta de valor:** Reducción de tiempos de operación y mejor coordinación del personal.

### Segmento 2 — Huéspedes de Hoteles Boutique

- **Quiénes:** Viajeros nacionales e internacionales que reservan en hoteles boutique y pequeños.
- **Necesidades:** Check-in sin colas, control de su habitación desde el celular, facilidad de comunicación con el hotel, personalización de servicios.
- **Propuesta de valor:** Experiencia moderna, sin fricción, con control total de su estancia.

---

<div style="page-break-after: always;"></div>
