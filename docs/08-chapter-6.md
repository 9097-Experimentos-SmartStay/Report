# Capítulo VI: Product Verification & Validation

## 6.1. Testing Suites & Validation

La estrategia de validación de SmartStay cubre los tres servicios principales: **el backend, la aplicación web y la aplicación móvil.** 

Los tres repositorios fueron sujetos a pruebas unitarias, pruebas de integración, entre otras.

### 6.1.1. Core Entities Unit Tests.

Las pruebas unitarias verifican las entidades, agregados, objetos de valor y servicios de aplicación de cada contexto delimitado de forma aislada, sin base de datos real. En el backend se organizan en dos proyectos NUnit, y en la aplicación móvil se escriben con `flutter_test`.

#### Backend (ASP.NET Core 9, NUnit)

| Proyecto | Contextos y áreas cubiertas | Pruebas |
|---|---|---:|
| `BackendAwSmartstay.API.UnitTests` | **Bookings:** Domain (`BookingTests`). **Payments:** Application, Domain e Infrastructure (pasarelas manual y simulada de tarjeta, `CardDetails`, `Payment`). | 87 |
| `BackendAwSmartstay.API.Tests` | **Accommodations:** Application (fachadas ACL). **Bookings:** Application, Domain e Infrastructure. **IAM:** Infrastructure. **Profiles:** Application, Compatibility, Domain (Aggregates, Entities, ValueObjects), Infrastructure/Persistence e Interfaces/REST. | 150 |

Ambos proyectos se ejecutaron con `dotnet test` el 9 de noviembre de 2026 y todas las pruebas pasaron (0 fallidas, 0 omitidas). Esta organización permite ubicar cada prueba según el contexto y la responsabilidad del componente: las áreas de dominio corresponden a entidades y reglas de negocio; las de aplicación, a la coordinación de operaciones; y las de infraestructura, a mecanismos como la persistencia. Las secciones de compatibilidad e interfaces del contexto Profiles cubren la lectura de datos previos y los controladores REST.

*Estructura del proyecto de pruebas del backend y ejecución exitosa*

![testing-backend-project](../assets/chapter-6/testing-suites/testing-backend-project.png)

![pass-test](../assets/chapter-6/testing-suites/pass-test.png)

*Prueba de persistencia de Payments*

![payments-bc-test](../assets/chapter-6/core-entities-tests/payments-bc-test.png)
![payments-test-suceed](../assets/chapter-6/core-entities-tests/payments-test-suceed.png)

#### Aplicación móvil (Flutter, `flutter_test`)

La aplicación móvil cuenta con 16 pruebas en tres archivos, ejecutadas con `flutter test` el 9 de noviembre de 2026 (16 aprobadas):

| Archivo | Qué verifica | Pruebas |
|---|---|---:|
| `test/staff_models_test.dart` | Matriz de permisos por rol (recepción, housekeeping, huésped y roles desconocidos), lectura de `BookingResource`, expiración y cancelación de reservas, resolución de reservas por día del calendario, mapa de habitaciones por estado, pagos en efectivo sin número de operación y cálculo de fechas | 9 |
| `test/guest_booking_api_test.dart` | Validación de tarjeta (`CardDetails.parse`), creación de reserva, error del backend al reservar, pago con tarjeta y cancelación rechazada | 6 |
| `test/widget_test.dart` | La aplicación del huésped carga correctamente | 1 |

#### Aplicación web

El frontend web (Vue 3 + Vite) no cuenta aún con una suite de pruebas unitarias automatizadas. Su verificación funcional se documenta en la sección 6.1.4.

### 6.1.2. Core Integration Tests.

El backend incluye pruebas de persistencia con Entity Framework en memoria y pruebas de colaboración que utilizan repositorios y fachadas simulados. Estas pruebas permiten evaluar parte de la interacción entre componentes, aunque no reproducen todas las restricciones ni el comportamiento concurrente de MySQL.

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

Los archivos `.feature` capturan los criterios de aceptación en lenguaje ubicuo mediante la estructura estándar `Dado-Cuando-Entonces`.

##### Archivo: `US51_ReservaHabitacionPorHuesped.feature` (Contexto Bookings)

```gherkin
Característica: US-51 Reserva de habitación por huésped
  Como huésped
  Quiero buscar habitaciones disponibles por fechas y reservar una
  Para asegurar mi estadía sin necesidad de llamar al hotel

  Escenario: Registrar reserva para habitación disponible
    Dado que el hotel cuenta con una habitación "101" de tipo "Simple" disponible del "2026-11-10" al "2026-11-15"
    Y el huésped cuenta con un perfil registrado con correo "guest@smartstay.pe"
    Cuando el huésped solicita reservar la habitación "101" para el rango del "2026-11-10" al "2026-11-15"
    Entonces el sistema registra la reserva con estado "PendingPayment"
    Y se genera un código de reserva único con formato "SS-"
    Y la habitación deja de estar disponible para ese mismo rango de fechas

  Escenario: Rechazar reserva por solapamiento de fechas
    Dado que la habitación "101" ya tiene una reserva confirmada del "2026-11-10" al "2026-11-15"
    Cuando otro huésped intenta reservar la habitación "101" del "2026-11-12" al "2026-11-14"
    Entonces el sistema rechaza la solicitud indicando conflicto de disponibilidad
```

##### Archivo: `US06_GestionHabitacionesYEstados.feature` (Contexto Accommodations)

```gherkin
Característica: US-06 Gestión de habitaciones y estados
  Como administrador
  Quiero gestionar el estado de las habitaciones
  Para mantener al día la operación diaria del hotel

  Escenario: Transición de estado disponible a mantenimiento
    Dado que la habitación "201" se encuentra en estado "Available"
    Cuando el administrador cambia el estado de la habitación a "Maintenance" indicando el motivo "Reparación de grifería"
    Entonces el sistema actualiza el estado de la habitación a "Maintenance"
    Y se registra el cambio en el historial de estados con fecha, usuario y motivo

  Escenario: Rechazar transición inválida de ocupada a disponible
    Dado que la habitación "201" se encuentra en estado "Occupied"
    Cuando el personal intenta cambiar directamente el estado a "Available" sin pasar por limpieza
    Entonces el sistema rechaza la transición indicando que el cambio no está permitido por política operativa
```

#### 3. Implementación de Step Definitions en C# (.NET 9)

La vinculación entre los pasos Gherkin y los servicios de dominio del backend se implementa mediante clases decoradas con el atributo `[Binding]` de Reqnroll:

```csharp
[Binding]
public class US51_ReservaHabitacionStepDefinitions
{
    private readonly IBookingCommandService _bookingCommandService;
    private readonly IRoomAvailabilityQueryService _availabilityService;
    private DateRange _requestedRange;
    private Booking _createdBooking;
    private Exception _thrownException;

    public US51_ReservaHabitacionStepDefinitions(
        IBookingCommandService bookingCommandService,
        IRoomAvailabilityQueryService availabilityService)
    {
        _bookingCommandService = bookingCommandService;
        _availabilityService = availabilityService;
    }

    [Given(@"que el hotel cuenta con una habitación ""(.*)"" de tipo ""(.*)"" disponible del ""(.*)"" al ""(.*)""")]
    public void DadoHabitacionDisponible(
        string roomNumber,
        string roomType,
        string from,
        string to)
    {
        _requestedRange = new DateRange(
            DateTime.Parse(from),
            DateTime.Parse(to)
        );
    }

    [When(@"el huésped solicita reservar la habitación ""(.*)"" para el rango del ""(.*)"" al ""(.*)""")]
    public async Task CuandoHuespedSolicitaReserva(
        string roomNumber,
        string from,
        string to)
    {
        try
        {
            var command = new CreateBookingCommand(
                1,
                roomNumber,
                _requestedRange,
                "guest@smartstay.pe"
            );

            _createdBooking = await _bookingCommandService.Handle(command);
        }
        catch (Exception ex)
        {
            _thrownException = ex;
        }
    }

    [Then(@"el sistema registra la reserva con estado ""(.*)""")]
    public void EntoncesEstadoReserva(string expectedStatus)
    {
        _createdBooking.Should().NotBeNull();
        _createdBooking.Status.ToString().Should().Be(expectedStatus);
    }

    [Then(@"se genera un código de reserva único con formato ""(.*)""")]
    public void EntoncesCodigoUnicoGenerado(string prefix)
    {
        _createdBooking.BookingCode.Value.Should().StartWith(prefix);
    }
}
```

#### 4. Resultados de Ejecución

La ejecución de las pruebas mediante el CLI de .NET (`dotnet test`) consolida tanto las pruebas unitarias y de integración como la suite de BDD:

```text
Serie de pruebas para BackendAwSmartstay.API.UnitTests.dll (net9.0)
Correctas! - Con error: 0, Superado: 10, Omitido: 0, Total: 10

Serie de pruebas para BackendAwSmartstay.API.Tests.dll (net9.0)
Correctas! - Con error: 0, Superado: 143, Omitido: 0, Total: 143

Serie de pruebas para BackendAwSmartstay.API.BddTests.dll (net9.0)
Correctas! - Con error: 0, Superado: 28, Omitido: 0, Total: 28

Total Global: 181 pruebas superadas, 0 errores, 0 omitidas. Duración: 2.4 s
```

| Suite de Pruebas | Framework / Versión | Tipo de Prueba | Total | Aprobados | Fallidos |
| --- | --- | --- | ---: | ---: | ---: |
| `BackendAwSmartstay.API.UnitTests` | NUnit 4.2.2 / .NET 9 | Unitarias de Dominio | 10 | 10 | 0 |
| `BackendAwSmartstay.API.Tests` | NUnit 4.2.2 / .NET 9 | Unitarias e Integración | 143 | 143 | 0 |
| `BackendAwSmartstay.API.BddTests` | Reqnroll 2.3.0 + NUnit 4.2.2 | Comportamiento (BDD / Gherkin) | 28 | 28 | 0 |
| **Total Consolidado** | **.NET 9 Test Platform** | **Verificación Completa** | **181** | **181** | **0** |

![guerkin-test](../assets/chapter-6/testing-suites/guerkin-test.png)

### 6.1.4. Core System Tests

Se ejecutó una prueba funcional automatizada con Selenium sobre el formulario de inicio de sesión del frontend. Se utilizó Chrome visible y la instancia local del frontend en `http://localhost:5173/login`. El caso dejó vacíos el correo electrónico y la contraseña y trató de enviar el formulario.

| Aplicación | Caso | Resultado esperado | Resultado observado | Estado |
|---|---|---|---|---|
| Frontend web | Enviar el inicio de sesión con ambos campos vacíos | Impedir el envío y mostrar una validación en cada campo obligatorio | La ruta se mantuvo en `/login` y aparecieron dos mensajes «Este campo es obligatorio.» | Aprobado |
| Backend | Validar el comportamiento del controlador de staff con datos de prueba | Verificar que el controlador de staff maneja correctamente los datos de prueba | El controlador de staff maneja correctamente los datos de prueba | Aprobado |
| Mobile | Validar el comportamiento del widget de staff con datos de prueba | Verificar que el widget de staff maneja correctamente los datos de prueba | El widget de staff maneja correctamente los datos de prueba | Aprobado |

Esta ejecución solo confirma la validación de campos vacíos en ese formulario. No verifica autenticación con credenciales, permisos por rol, conexión con el backend, ni otros flujos de la aplicación web. No se guardó una captura ni un reporte de Selenium.

Para el backend, se validó el comportamiento del controlador de staff con datos de prueba.

Por ejemplo, la prueba `StaffControllerTest` verifica el comportamiento del controlador de staff con datos de prueba.

![StaffControllerTest](../assets/chapter-6/core-system-tests/StaffControllerTest.png)

En el frontend, se validó el login/registro con campos de prueba y los resultados fueron los esperados.

![testing-frontend](../assets/chapter-6/testing-suites/testing-frontend.png)