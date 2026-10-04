# Capítulo VI: Product Verification & Validation

## 6.1. Testing Suites & Validation

El backend de SmartStay cuenta con el proyecto `BackendAwSmartstay.API.Tests`, que organiza las pruebas en los módulos Accommodations, Bookings y Profiles. Su estructura separa las áreas de aplicación, dominio e infraestructura, y contempla pruebas de compatibilidad e interfaces en el módulo de perfiles.

| Módulo | Áreas presentes en el proyecto de pruebas |
|---|---|
| Accommodations | Application, con una sección ACL. |
| Bookings | Application, Domain e Infrastructure. |
| Profiles | Application, Compatibility, Domain, Infrastructure e Interfaces. |

Esta organización permite ubicar las pruebas según el módulo y la responsabilidad del componente evaluado. Las áreas de dominio corresponden a las entidades y reglas de negocio; las de aplicación, a la coordinación de operaciones; y las de infraestructura, a mecanismos como la persistencia. Las secciones de compatibilidad, interfaces y ACL permiten organizar verificaciones relacionadas con la interacción entre componentes.

![testing-backend-project](../assets/chapter-6/testing-suites/testing-backend-project.png)

### Validación funcional del inicio de sesión del frontend

Se ejecutó una prueba funcional automatizada con Selenium sobre el formulario de inicio de sesión de SmartStay. La ejecución se realizó en Chrome, en modo visible, utilizando el frontend local en `http://localhost:5173/login`.

La prueba consistió en dejar vacíos el correo electrónico y la contraseña e intentar enviar el formulario. Se verificó que ambos campos permanecieran vacíos, que la aplicación conservara la ruta de inicio de sesión y que mostrara una validación comprensible.

| Caso evaluado | Resultado esperado | Resultado observado | Estado |
|---|---|---|---|
| Enviar el formulario de inicio de sesión con correo y contraseña vacíos. | Impedir continuar y mostrar una validación para ambos campos obligatorios. | La aplicación permaneció en `/login` y mostró «Este campo es obligatorio.» debajo del correo y de la contraseña. | Aprobado |

El resultado confirma la validación de campos obligatorios en este escenario. No se utilizaron credenciales ni se crearon cuentas, reservas o pagos.

El alcance de esta prueba se limita al envío del formulario vacío. No verifica la autenticación con credenciales, la autorización por roles ni los demás flujos del frontend.

![testing-frontend](../assets/chapter-6/testing-suites/testing-frontend.png)

### 6.1.1. Core Entities Unit Tests.

### 6.1.2. Core Integration Tests.

### 6.1.3. Core Behavior-Driven Development

### 6.1.4. Core System Tests
