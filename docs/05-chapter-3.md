# Capítulo III: Requirements Specification

## 3.1. To-Be Scenario Mapping

Segmento 1: Staff Operativo de Hoteles

<div align="center">
<img src="../assets/chapter-3/scenario-mapping/to-be-staff.png" alt="To-be segmento 1" style="max-width: 90%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
</div>

Segmento 2: Huéspedes de Hoteles Boutique

<div align="center">
<img src="../assets/chapter-3/scenario-mapping/to-be-guest.png" alt="To-be segmento 2" style="max-width: 90%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
</div>

## 3.2. User Stories

<table>
  <tr>
    <th>Epic / Story ID</th>
    <th>Title</th>
    <th>Description</th>
    <th>Acceptance Criteria</th>
    <th>Related to (Epic ID)</th>
  </tr>

  <!-- EPICS -->
  <tr class="epic-row">
    <td><strong>EP-01</strong></td>
    <td><strong>Authentication and User Management</strong></td>
    <td>Epic that groups functionalities for registration, login, profile management, and role-based access control for all user types (administrators, staff, and guests).</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr class="epic-row">
    <td><strong>EP-02</strong></td>
    <td><strong>Central Hotel Management</strong></td>
    <td>Epic that includes reservation management, room management, digital check-in/check-out, daily operations, and internal service coordination.</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr class="epic-row">
    <td><strong>EP-03</strong></td>
    <td><strong>Digital Guest Experience</strong></td>
    <td>Epic focused on the guest experience: IoT environmental control, personalized services, digital communication, and post-stay evaluation.</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr class="epic-row">
    <td><strong>EP-04</strong></td>
    <td><strong>Analytics and Reporting</strong></td>
    <td>Epic that covers management dashboards, occupancy reports, operational KPIs, satisfaction analysis, and financial metrics.</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr class="epic-row">
    <td><strong>EP-05</strong></td>
    <td><strong>Integrations and External Channels</strong></td>
    <td>Epic for connections with OTAs, WhatsApp, payment systems, digital reputation platforms, and third-party webhooks.</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr class="epic-row">
    <td><strong>EP-06</strong></td>
    <td><strong>Landing Page and Digital Marketing</strong></td>
    <td>Epic for the informational website with segmented content, success stories, simulators, and business contact channels.</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr class="epic-row">
    <td><strong>EP-07</strong></td>
    <td><strong>RESTful API and Technical Services</strong></td>
    <td>Epic that includes endpoints, API authentication, technical documentation, monitoring, and integration with external systems.</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr class="epic-row">
    <td><strong>EP-08</strong></td>
    <td><strong>Notifications and Communication</strong></td>
    <td>Epic for the push notification system, email, SMS, automated alerts, and communication between staff and guests.</td>
    <td></td>
    <td>-</td>
  </tr>

  <!-- USER STORIES -->
  <tr>
    <td>US-01</td>
    <td>User registration with validation</td>
    <td class="user-story-desc"><strong>As a</strong> new user, <strong>I want</strong> to register in Smart Stay by validating my email from the mobile application <strong>so that</strong> I can access features according to my role.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Successful registration</strong><br>
      <strong>Given that</strong> I am a new user with valid data, <strong>when</strong> I complete the registration form from the app, <strong>then</strong> my account is successfully created and I receive a confirmation email.<br>
      <strong>Scenario 2: Email already registered</strong><br>
      <strong>Given that</strong> I try to register with an existing email, <strong>when</strong> I submit the form, <strong>then</strong> the system displays the message “Email already registered” and suggests recovering my password.<br>
      <strong>Scenario 3: Incomplete data</strong><br>
      <strong>Given that</strong> I leave required fields empty, <strong>when</strong> I try to continue, <strong>then</strong> the application highlights the missing fields and does not allow me to complete the registration.<br>
      <strong>Scenario 4: Email format validation</strong><br>
      <strong>Given that</strong> I enter an email with an invalid format, <strong>when</strong> I submit the form, <strong>then</strong> the app displays a format error.
    </td>
    <td>EP-01</td>
  </tr>

  <tr>
    <td>US-02</td>
    <td>Secure login</td>
    <td class="user-story-desc"><strong>As a</strong> registered user, <strong>I want</strong> to log in securely from the mobile application <strong>so that</strong> I can access my personalized dashboard according to my role.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Successful login</strong><br>
      <strong>Given that</strong> I have valid credentials, <strong>when</strong> I log in from the app, <strong>then</strong> I access the corresponding dashboard according to my role.<br>
      <strong>Scenario 2: Incorrect credentials</strong><br>
      <strong>Given that</strong> I enter incorrect data, <strong>when</strong> I try to access, <strong>then</strong> I receive an error message without revealing whether the email or password was incorrect.<br>
      <strong>Scenario 3: Account locked</strong><br>
      <strong>Given that</strong> I fail to log in 5 consecutive times, <strong>when</strong> I try again, <strong>then</strong> the account is temporarily locked and I receive a notification.<br>
      <strong>Scenario 4: Persistent session</strong><br>
      <strong>Given that</strong> I activate the “remember me” option, <strong>when</strong> I close and reopen the application, <strong>then</strong> I remain logged in until I log out manually.
    </td>
    <td>EP-01</td>
  </tr>

  <tr>
    <td>US-03</td>
    <td>Profile and role management</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to manage users and assign roles and permissions from the mobile application <strong>so that</strong> I can control access to the system’s different functionalities.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Create staff user</strong><br>
      <strong>Given that</strong> I am an administrator, <strong>when</strong> I create a user from the mobile app, <strong>then</strong> I can assign specific permissions such as housekeeping, reception, or maintenance.<br>
      <strong>Scenario 2: Modify permissions</strong><br>
      <strong>Given that</strong> there is a registered user, <strong>when</strong> I update their permissions from my mobile device, <strong>then</strong> their access rights are modified immediately.<br>
      <strong>Scenario 3: Deactivate user</strong><br>
      <strong>Given that</strong> I need to deactivate a user, <strong>when</strong> I perform the action from the app, <strong>then</strong> the user loses access but their history is preserved.<br>
      <strong>Scenario 4: Access audit</strong><br>
      <strong>Given that</strong> I want to review activity, <strong>when</strong> I access the history from the app, <strong>then</strong> I can view the date, time, user, and action performed.
    </td>
    <td>EP-01</td>
  </tr>

  <tr>
    <td>US-04</td>
    <td>Password recovery</td>
    <td class="user-story-desc"><strong>As a</strong> user, <strong>I want</strong> to recover my password from the mobile application through my email <strong>so that</strong> I can regain access to my account.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Valid request</strong><br>
      <strong>Given that</strong> I request password recovery with a registered email, <strong>when</strong> I send the request, <strong>then</strong> I receive a reset link by email.<br>
      <strong>Scenario 2: Unregistered email</strong><br>
      <strong>Given that</strong> I request recovery with an unregistered email, <strong>when</strong> I send the request, <strong>then</strong> I receive a generic message without revealing whether the email exists or not.<br>
      <strong>Scenario 3: Expired link</strong><br>
      <strong>Given that</strong> the recovery link is older than 30 minutes, <strong>when</strong> I try to use it, <strong>then</strong> the system indicates that it has expired and I must request a new one.<br>
      <strong>Scenario 4: Successful change</strong><br>
      <strong>Given that</strong> I have a valid link, <strong>when</strong> I set a new password, <strong>then</strong> it is successfully updated and I receive confirmation.
    </td>
    <td>EP-01</td>
  </tr>

  <tr>
    <td>US-05</td>
    <td>Mobile administrative dashboard</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to access a centralized dashboard from my smartphone <strong>so that</strong> I can view key hotel information and make quick decisions.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Overview</strong><br>
      <strong>Given that</strong> I access the dashboard from the mobile app, <strong>when</strong> the main screen loads, <strong>then</strong> I see current occupancy, today’s check-ins/check-outs, pending tasks, and important alerts.<br>
      <strong>Scenario 2: Date filters</strong><br>
      <strong>Given that</strong> I want to review a specific period, <strong>when</strong> I select a date range from the app, <strong>then</strong> the indicators are updated correctly.<br>
      <strong>Scenario 3: Quick access</strong><br>
      <strong>Given that</strong> I am on the mobile dashboard, <strong>when</strong> I tap a metric, <strong>then</strong> I am redirected to the corresponding detailed section.<br>
      <strong>Scenario 4: Real-time updates</strong><br>
      <strong>Given that</strong> operational changes occur, <strong>when</strong> they are recorded, <strong>then</strong> the mobile dashboard updates without needing a manual refresh.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-06</td>
    <td>Room and status management</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to manage room statuses from the mobile application <strong>so that</strong> I can optimize the hotel’s daily operations in real time.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Change room status</strong><br>
      <strong>Given that</strong> I select a room from the app, <strong>when</strong> I change its status to available, occupied, cleaning, or maintenance, <strong>then</strong> the system updates it immediately and notifies the corresponding staff.<br>
      <strong>Scenario 2: Mobile room map view</strong><br>
      <strong>Given that</strong> I access the room map from my phone, <strong>when</strong> the view loads, <strong>then</strong> I can see all statuses with color codes and make quick changes.<br>
      <strong>Scenario 3: Change history</strong><br>
      <strong>Given that</strong> I need to review modifications, <strong>when</strong> I check the history from the app, <strong>then</strong> I see the date, time, and user responsible for each change.<br>
      <strong>Scenario 4: Automatic alerts</strong><br>
      <strong>Given that</strong> a room remains in maintenance for more than 24 hours, <strong>when</strong> that time is reached, <strong>then</strong> I receive an automatic alert on my mobile device.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-07</td>
    <td>Centralized reservation management</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to manage all reservations from the mobile application <strong>so that</strong> I can avoid overbooking and optimize hotel occupancy.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Mobile calendar view</strong><br>
      <strong>Given that</strong> I enter the reservations section from the app, <strong>when</strong> I select the calendar view, <strong>then</strong> I can see all reservations organized by date with key information.<br>
      <strong>Scenario 2: Create manual reservation</strong><br>
      <strong>Given that</strong> I receive a reservation by phone, <strong>when</strong> I enter it from the mobile app, <strong>then</strong> the system validates availability and confirms it.<br>
      <strong>Scenario 3: Modify existing reservation</strong><br>
      <strong>Given that</strong> I need to edit a reservation, <strong>when</strong> I make changes from my phone, <strong>then</strong> the system validates availability and notifies the guest.<br>
      <strong>Scenario 4: Cancellation with policies</strong><br>
      <strong>Given that</strong> a reservation is canceled, <strong>when</strong> I process the cancellation from the app, <strong>then</strong> the corresponding policies are applied and the room is released.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-08</td>
    <td>Automated digital check-in</td>
    <td class="user-story-desc"><strong>As an</strong> administrator and guest, <strong>I want</strong> check-in to be completed digitally from the mobile application in less than 3 minutes <strong>so that</strong> the arrival experience is improved.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Successful guest check-in</strong><br>
      <strong>Given that</strong> the guest starts check-in from the app, <strong>when</strong> they complete their data and confirm, <strong>then</strong> they receive digital access to their room and the corresponding code.<br>
      <strong>Scenario 2: Document validation</strong><br>
      <strong>Given that</strong> the guest uploads their documents from their phone, <strong>when</strong> the system processes them, <strong>then</strong> it automatically validates them and approves the check-in.<br>
      <strong>Scenario 3: Assisted check-in</strong><br>
      <strong>Given that</strong> the guest has difficulties, <strong>when</strong> they request help from the application, <strong>then</strong> staff receive a notification to assist them.<br>
      <strong>Scenario 4: Automatic notification</strong><br>
      <strong>Given that</strong> check-in is completed, <strong>when</strong> it is confirmed, <strong>then</strong> housekeeping receives the notification and the administrator sees the updated status.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-09</td>
    <td>Digital check-out and billing</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> to check out from the mobile application and automatically receive my invoice <strong>so that</strong> I can speed up my departure.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Successful check-out</strong><br>
      <strong>Given that</strong> I start check-out from the app, <strong>when</strong> I confirm my departure and review the charges, <strong>then</strong> the room is released and I receive the invoice by email.<br>
      <strong>Scenario 2: Additional charges</strong><br>
      <strong>Given that</strong> I have pending consumption charges, <strong>when</strong> I complete check-out, <strong>then</strong> I see the charge details and can approve the payment.<br>
      <strong>Scenario 3: Late check-out</strong><br>
      <strong>Given that</strong> I leave after the established time, <strong>when</strong> I process check-out, <strong>then</strong> the corresponding charge is applied and I am notified.<br>
      <strong>Scenario 4: Notification to housekeeping</strong><br>
      <strong>Given that</strong> I complete check-out, <strong>when</strong> it is confirmed, <strong>then</strong> housekeeping automatically receives the task to prepare the room.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-10</td>
    <td>Staff task assignment and tracking</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to assign tasks and monitor their progress from the mobile application <strong>so that</strong> I can improve operational coordination.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Assign housekeeping task</strong><br>
      <strong>Given that</strong> a room needs cleaning, <strong>when</strong> I assign the task from the app, <strong>then</strong> staff receive a notification with details and priority.<br>
      <strong>Scenario 2: Update progress</strong><br>
      <strong>Given that</strong> staff start a task, <strong>when</strong> they mark it as “in progress” from their mobile device, <strong>then</strong> I can see the update in real time.<br>
      <strong>Scenario 3: Complete task</strong><br>
      <strong>Given that</strong> a task has been finished, <strong>when</strong> the worker marks it as completed in the app, <strong>then</strong> I receive a notification to validate the work.<br>
      <strong>Scenario 4: Overdue tasks</strong><br>
      <strong>Given that</strong> a task is not completed on time, <strong>when</strong> the deadline passes, <strong>then</strong> the app generates an automatic alert.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-11</td>
    <td>IoT environmental control from the mobile app</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> to control temperature, lighting, and other room environment aspects from my smartphone <strong>so that</strong> I can personalize my room experience.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Temperature adjustment</strong><br>
      <strong>Given that</strong> I am in my room, <strong>when</strong> I change the temperature from the app, <strong>then</strong> the IoT system adjusts the climate in less than 30 seconds.<br>
      <strong>Scenario 2: Lighting control</strong><br>
      <strong>Given that</strong> I want to modify the lights, <strong>when</strong> I use the app controls, <strong>then</strong> I can change brightness, color, and turn specific lights on or off.<br>
      <strong>Scenario 3: Blind settings</strong><br>
      <strong>Given that</strong> I want to control natural light entry, <strong>when</strong> I adjust the blinds from the application, <strong>then</strong> they open or close according to the selected percentage.<br>
      <strong>Scenario 4: Personalized settings</strong><br>
      <strong>Given that</strong> I want quick adjustments, <strong>when</strong> I save a setting such as “rest” or “work,” <strong>then</strong> I can activate multiple preferences with a single tap.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-12</td>
    <td>Service requests from the app</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> to request room service, additional cleaning, and other services from the mobile application <strong>so that</strong> I can access them conveniently and quickly.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Request room service</strong><br>
      <strong>Given that</strong> I want to order food, <strong>when</strong> I access the menu from the app, <strong>then</strong> I can select products, customize them, and confirm the order with an estimated time.<br>
      <strong>Scenario 2: Request additional cleaning</strong><br>
      <strong>Given that</strong> I need extra cleaning, <strong>when</strong> I make the request from the app, <strong>then</strong> I can choose the preferred time and staff receive the request immediately.<br>
      <strong>Scenario 3: Track request</strong><br>
      <strong>Given that</strong> I already placed an order, <strong>when</strong> I check its status in the app, <strong>then</strong> I see the progress in real time.<br>
      <strong>Scenario 4: Special services</strong><br>
      <strong>Given that</strong> I need services such as transportation, tours, or reservations, <strong>when</strong> I request them from the app, <strong>then</strong> staff receive a notification to coordinate the service.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-13</td>
    <td>Digital communication between guest and staff</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> to communicate digitally with hotel staff from the mobile application <strong>so that</strong> I can resolve questions and requests quickly.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Real-time chat</strong><br>
      <strong>Given that</strong> I have a question, <strong>when</strong> I start a chat from the app, <strong>then</strong> I connect with available staff and receive a response in less than 5 minutes.<br>
      <strong>Scenario 2: Specific requests</strong><br>
      <strong>Given that</strong> I need something specific, <strong>when</strong> I send a detailed message, <strong>then</strong> the corresponding department receives the request.<br>
      <strong>Scenario 3: Conversation history</strong><br>
      <strong>Given that</strong> I had several interactions, <strong>when</strong> I enter the history from the app, <strong>then</strong> I can review all conversations from my stay.<br>
      <strong>Scenario 4: Automatic escalation</strong><br>
      <strong>Given that</strong> my request is not resolved within the expected time, <strong>when</strong> that limit is exceeded, <strong>then</strong> the system automatically escalates it to a supervisor.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-14</td>
    <td>Experience personalization based on preferences</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> the system to learn my preferences <strong>so that</strong> it can offer me personalized experiences and services from the mobile application.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Initial preference setup</strong><br>
      <strong>Given that</strong> it is my first stay, <strong>when</strong> I complete my preference profile in the app, <strong>then</strong> the system configures the room according to my preferences before my arrival.<br>
      <strong>Scenario 2: Automatic learning</strong><br>
      <strong>Given that</strong> I have already used the system several times, <strong>when</strong> I return, <strong>then</strong> the application suggests settings and services based on my history.<br>
      <strong>Scenario 3: Personalized recommendations</strong><br>
      <strong>Given that</strong> there is a profile with my preferences, <strong>when</strong> I am at the hotel, <strong>then</strong> I receive recommendations for restaurants, activities, and services aligned with my interests.<br>
      <strong>Scenario 4: Exclusive offers</strong><br>
      <strong>Given that</strong> I am a recurring guest, <strong>when</strong> I enter the app, <strong>then</strong> I see personalized offers and upgrades based on my history.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-15</td>
    <td>Post-stay evaluation and feedback</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> to evaluate my experience from the mobile application after my stay <strong>so that</strong> I can help the hotel improve its services.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic evaluation</strong><br>
      <strong>Given that</strong> I completed my check-out, <strong>when</strong> 2 hours pass, <strong>then</strong> I receive an automatic invitation to evaluate my experience through a simple form.<br>
      <strong>Scenario 2: Detailed feedback</strong><br>
      <strong>Given that</strong> I want to provide more complete feedback, <strong>when</strong> I access the extended form, <strong>then</strong> I can rate specific aspects and leave comments.<br>
      <strong>Scenario 3: Negative feedback follow-up</strong><br>
      <strong>Given that</strong> I leave a low rating, <strong>when</strong> I submit the evaluation, <strong>then</strong> the hotel receives an immediate alert to take action.<br>
      <strong>Scenario 4: Feedback incentives</strong><br>
      <strong>Given that</strong> I complete the evaluation, <strong>when</strong> I submit it, <strong>then</strong> I receive a benefit for my next stay.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-16</td>
    <td>Analytics dashboard and operational KPIs</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to view key metrics and KPIs from the mobile application <strong>so that</strong> I can make informed decisions about hotel operations.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Real-time metrics</strong><br>
      <strong>Given that</strong> I enter the analytics dashboard from the app, <strong>when</strong> the view loads, <strong>then</strong> I see current occupancy, daily revenue, completed tasks, and average satisfaction.<br>
      <strong>Scenario 2: Historical comparisons</strong><br>
      <strong>Given that</strong> I want to analyze trends, <strong>when</strong> I select comparison periods from my phone, <strong>then</strong> I see comparative charts of occupancy, revenue, and operations.<br>
      <strong>Scenario 3: Metric drill-down</strong><br>
      <strong>Given that</strong> I identify an important metric, <strong>when</strong> I select it from the app, <strong>then</strong> I access its details with filters by date, room, or service.<br>
      <strong>Scenario 4: Smart alerts</strong><br>
      <strong>Given that</strong> the system detects negative trends, <strong>when</strong> they occur, <strong>then</strong> I receive automatic alerts with action suggestions.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-17</td>
    <td>Financial and occupancy reports</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to generate and consult financial and occupancy reports from the mobile application <strong>so that</strong> I can support management analysis and decision-making.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic daily report</strong><br>
      <strong>Given that</strong> the operational day ends, <strong>when</strong> midnight arrives, <strong>then</strong> the app displays the daily report with revenue, occupancy, and incidents.<br>
      <strong>Scenario 2: Custom report</strong><br>
      <strong>Given that</strong> I need a specific analysis, <strong>when</strong> I configure dates, metrics, and filters from the app, <strong>then</strong> I generate a custom report in PDF or Excel.<br>
      <strong>Scenario 3: Forecasts</strong><br>
      <strong>Given that</strong> historical data exists, <strong>when</strong> I enter the forecasting section from the app, <strong>then</strong> I see estimated occupancy and revenue.<br>
      <strong>Scenario 4: Benchmarking</strong><br>
      <strong>Given that</strong> I have market data, <strong>when</strong> I generate a comparative report, <strong>then</strong> I see the hotel’s performance against local competitors.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-18</td>
    <td>Guest satisfaction analysis</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to analyze guest satisfaction from the mobile application <strong>so that</strong> I can identify service improvement opportunities.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Satisfaction dashboard</strong><br>
      <strong>Given that</strong> I enter the satisfaction section in the app, <strong>when</strong> the dashboard loads, <strong>then</strong> I see average NPS, rating distribution, and recent comments.<br>
      <strong>Scenario 2: Analysis by category</strong><br>
      <strong>Given that</strong> I want to understand specific issues, <strong>when</strong> I filter by cleanliness, service, or comfort, <strong>then</strong> I see detailed ratings by area.<br>
      <strong>Scenario 3: Time trends</strong><br>
      <strong>Given that</strong> I want to observe evolution, <strong>when</strong> I select a time-based view from the app, <strong>then</strong> I visualize changes in satisfaction over time.<br>
      <strong>Scenario 4: Corrective actions</strong><br>
      <strong>Given that</strong> I identify a recurring problem, <strong>when</strong> I mark it from the app, <strong>then</strong> an automatic task is created for the responsible department.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-19</td>
    <td>IoT energy consumption monitoring</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to monitor energy consumption from the mobile application <strong>so that</strong> I can optimize operating costs and improve hotel efficiency.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Real-time consumption dashboard</strong><br>
      <strong>Given that</strong> I access the monitoring from the app, <strong>when</strong> the view loads, <strong>then</strong> I observe current consumption by room, common area, and main equipment.<br>
      <strong>Scenario 2: Alerts for excessive consumption</strong><br>
      <strong>Given that</strong> a room exceeds normal consumption, <strong>when</strong> the threshold is surpassed, <strong>then</strong> I receive an immediate alert on my phone.<br>
      <strong>Scenario 3: Automatic optimization</strong><br>
      <strong>Given that</strong> a room is unoccupied, <strong>when</strong> 30 minutes pass without activity, <strong>then</strong> the system automatically adjusts lights and temperature to energy-saving mode.<br>
      <strong>Scenario 4: Savings report</strong><br>
      <strong>Given that</strong> optimizations were implemented, <strong>when</strong> I generate the monthly report from the app, <strong>then</strong> I see a comparison of consumption and achieved savings.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-20</td>
    <td>Integration with OTAs and booking channels</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to integrate the hotel inventory with Booking.com, Expedia, and other OTAs <strong>so that</strong> I can maximize occupancy and avoid overbooking, while supervising everything from a mobile interface.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic availability synchronization</strong><br>
      <strong>Given that</strong> I change availability in Smart Stay, <strong>when</strong> it is updated, <strong>then</strong> all connected channels are synchronized in less than 5 minutes.<br>
      <strong>Scenario 2: Automatic reservation import</strong><br>
      <strong>Given that</strong> I receive a reservation from an OTA, <strong>when</strong> it is confirmed, <strong>then</strong> it is automatically imported into Smart Stay with all guest information.<br>
      <strong>Scenario 3: Centralized rate management</strong><br>
      <strong>Given that</strong> I want to change prices, <strong>when</strong> I update them in Smart Stay, <strong>then</strong> they are automatically propagated to all configured channels.<br>
      <strong>Scenario 4: Conflict resolution</strong><br>
      <strong>Given that</strong> there is a discrepancy between channels, <strong>when</strong> the system detects it, <strong>then</strong> it immediately notifies me and suggests corrective actions.
    </td>
    <td>EP-05</td>
  </tr>

  <tr>
    <td>US-21</td>
    <td>WhatsApp Business integration</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to use WhatsApp Business integrated with the application <strong>so that</strong> I can communicate directly with guests and manage inquiries before and after their stay.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic welcome messages</strong><br>
      <strong>Given that</strong> a guest confirms their reservation, <strong>when</strong> it is recorded, <strong>then</strong> they receive an automatic WhatsApp message with arrival and contact information.<br>
      <strong>Scenario 2: Pre-arrival inquiries</strong><br>
      <strong>Given that</strong> a guest sends an inquiry through WhatsApp, <strong>when</strong> the message arrives, <strong>then</strong> staff receive a notification in Smart Stay and can respond from the platform.<br>
      <strong>Scenario 3: Service confirmation</strong><br>
      <strong>Given that</strong> the guest requests a service via WhatsApp, <strong>when</strong> it is processed, <strong>then</strong> they receive an automatic confirmation with details and estimated time.<br>
      <strong>Scenario 4: Post-stay follow-up</strong><br>
      <strong>Given that</strong> the guest has already checked out, <strong>when</strong> 1 day passes, <strong>then</strong> they receive a thank-you message and an invitation to evaluate their experience.
    </td>
    <td>EP-05</td>
  </tr>

  <tr>
    <td>US-22</td>
    <td>Digital reputation management</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to manage reviews and digital reputation from the mobile application <strong>so that</strong> I can respond quickly and maintain a good hotel image.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Review consolidation</strong><br>
      <strong>Given that</strong> I enter the reputation section from the app, <strong>when</strong> it loads, <strong>then</strong> I see reviews from Google, TripAdvisor, and OTAs in one place.<br>
      <strong>Scenario 2: Centralized response</strong><br>
      <strong>Given that</strong> I want to reply to a review, <strong>when</strong> I write the response from the app, <strong>then</strong> it is published on the corresponding platform.<br>
      <strong>Scenario 3: Alerts for negative reviews</strong><br>
      <strong>Given that</strong> a review of 3 stars or less is published, <strong>when</strong> the system detects it, <strong>then</strong> I receive an immediate notification.<br>
      <strong>Scenario 4: Sentiment analysis</strong><br>
      <strong>Given that</strong> several reviews are registered, <strong>when</strong> I access the analysis from the app, <strong>then</strong> I can visualize trends, frequent words, and areas for improvement.
    </td>
    <td>EP-05</td>
  </tr>

  <tr>
    <td>US-23</td>
    <td>Digital payment processing</td>
    <td class="user-story-desc"><strong>As an</strong> administrator and guest, <strong>I want</strong> to process digital payments securely from the mobile application using different payment methods <strong>so that</strong> transactions are easier.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Card payment during check-in</strong><br>
      <strong>Given that</strong> the guest performs digital check-in, <strong>when</strong> they enter their card information, <strong>then</strong> a secure pre-authorization is processed and the check-in is confirmed.<br>
      <strong>Scenario 2: Payment for additional services</strong><br>
      <strong>Given that</strong> the guest requests a service, <strong>when</strong> they confirm the order, <strong>then</strong> they can pay immediately from the app using a saved method.<br>
      <strong>Scenario 3: Automatic charge at check-out</strong><br>
      <strong>Given that</strong> the guest performs check-out, <strong>when</strong> they confirm the final charges, <strong>then</strong> the payment is processed and they receive their digital invoice.<br>
      <strong>Scenario 4: Failed payment handling</strong><br>
      <strong>Given that</strong> a payment fails, <strong>when</strong> the error occurs, <strong>then</strong> the guest receives an immediate notification with payment alternatives.
    </td>
    <td>EP-05</td>
  </tr>

  <tr>
    <td>US-24</td>
    <td>Segmented landing page</td>
    <td class="user-story-desc"><strong>As a</strong> visitor, <strong>I want</strong> to access a landing page segmented according to my profile from my mobile device <strong>so that</strong> I can quickly understand Smart Stay’s value.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Information for administrators</strong><br>
      <strong>Given that</strong> I am a hotel administrator, <strong>when</strong> I enter from my smartphone, <strong>then</strong> I see operational benefits, ROI, success stories, and access to a demo.<br>
      <strong>Scenario 2: Information for guests</strong><br>
      <strong>Given that</strong> I am a traveler, <strong>when</strong> I browse from my phone, <strong>then</strong> I see benefits related to comfort, experience, and technology.<br>
      <strong>Scenario 3: Intuitive mobile navigation</strong><br>
      <strong>Given that</strong> I access the landing page, <strong>when</strong> it loads on my phone, <strong>then</strong> I identify my profile and reach relevant information in less than 3 clicks.<br>
      <strong>Scenario 4: Clear calls to action</strong><br>
      <strong>Given that</strong> I am interested in continuing, <strong>when</strong> I review the page from mobile, <strong>then</strong> I find clear buttons to request a demo, contact sales, or download the app.
    </td>
    <td>EP-06</td>
  </tr>

  <tr>
    <td>US-25</td>
    <td>ROI simulator for hotels</td>
    <td class="user-story-desc"><strong>As an</strong> interested hotel administrator, <strong>I want</strong> to use an ROI simulator from my mobile device <strong>so that</strong> I can estimate the return on investment I would obtain with Smart Stay.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Basic ROI calculation</strong><br>
      <strong>Given that</strong> I enter basic data such as number of rooms and average occupancy, <strong>when</strong> I run the simulation from my phone, <strong>then</strong> I obtain estimated annual savings and payback time.<br>
      <strong>Scenario 2: Customization by hotel type</strong><br>
      <strong>Given that</strong> I select the hotel type, <strong>when</strong> I use the mobile simulator, <strong>then</strong> the calculations are adjusted to my segment.<br>
      <strong>Scenario 3: Comparison with current situation</strong><br>
      <strong>Given that</strong> I enter current operating costs, <strong>when</strong> I generate the result, <strong>then</strong> I see a clear comparison between current and projected operation.<br>
      <strong>Scenario 4: Export results</strong><br>
      <strong>Given that</strong> I finish the simulation, <strong>when</strong> I want to save the results, <strong>then</strong> I can export them as a PDF from the mobile device.
    </td>
    <td>EP-06</td>
  </tr>

  <tr>
    <td>US-26</td>
    <td>Success stories and testimonials</td>
    <td class="user-story-desc"><strong>As an</strong> interested visitor, <strong>I want</strong> to see success stories and testimonials from the mobile application or mobile site <strong>so that</strong> I can validate the effectiveness of the solution.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Video testimonials</strong><br>
      <strong>Given that</strong> I access the section from my phone, <strong>when</strong> I browse it, <strong>then</strong> I can watch videos of real administrators sharing their experience.<br>
      <strong>Scenario 2: Improvement metrics</strong><br>
      <strong>Given that</strong> I review a success story, <strong>when</strong> I open its details, <strong>then</strong> I see concrete data on cost reduction, satisfaction improvement, and time savings.<br>
      <strong>Scenario 3: Filter by hotel type</strong><br>
      <strong>Given that</strong> I want references similar to my business, <strong>when</strong> I filter the cases from mobile, <strong>then</strong> I see the most relevant ones for my profile.<br>
      <strong>Scenario 4: Request more information</strong><br>
      <strong>Given that</strong> I am interested in a specific case, <strong>when</strong> I press the contact option, <strong>then</strong> I can request additional information directly from my phone.
    </td>
    <td>EP-06</td>
  </tr>

  <tr>
    <td>US-27</td>
    <td>Demo request and commercial contact</td>
    <td class="user-story-desc"><strong>As an</strong> interested visitor, <strong>I want</strong> to request a demo and contact the sales team from my mobile device in a simple and fast way <strong>so that</strong> I can explore Smart Stay.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Demo form</strong><br>
      <strong>Given that</strong> I want to see a demonstration, <strong>when</strong> I complete the form from mobile, <strong>then</strong> I receive immediate confirmation.<br>
      <strong>Scenario 2: Automatic scheduling</strong><br>
      <strong>Given that</strong> I submit the request, <strong>when</strong> the registration is completed, <strong>then</strong> I can schedule an appointment in the available calendar.<br>
      <strong>Scenario 3: Accessible contact information</strong><br>
      <strong>Given that</strong> I prefer direct contact, <strong>when</strong> I review the commercial section from mobile, <strong>then</strong> I find the team’s phone number, email, and WhatsApp.<br>
      <strong>Scenario 4: Automatic follow-up</strong><br>
      <strong>Given that</strong> I requested information, <strong>when</strong> some time passes without a response, <strong>then</strong> I receive a reminder or automatic follow-up.
    </td>
    <td>EP-06</td>
  </tr>

  <tr>
    <td>US-28</td>
    <td>Corporate information and values</td>
    <td class="user-story-desc"><strong>As a</strong> visitor, <strong>I want</strong> to know Smart Stay’s mission, vision, and values from a mobile interface <strong>so that</strong> I can understand the company’s philosophy.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Complete “About Us” section</strong><br>
      <strong>Given that</strong> I am looking for institutional information, <strong>when</strong> I enter the section from my smartphone, <strong>then</strong> I find the company’s mission, vision, values, and history.<br>
      <strong>Scenario 2: Team and leadership</strong><br>
      <strong>Given that</strong> I want to know the team, <strong>when</strong> I browse the app or mobile site, <strong>then</strong> I see information about founders and key leaders.<br>
      <strong>Scenario 3: Commitment to sustainability</strong><br>
      <strong>Given that</strong> environmental impact matters to me, <strong>when</strong> I review the information, <strong>then</strong> I find the company’s commitment to sustainability and energy efficiency.<br>
      <strong>Scenario 4: Certifications and recognitions</strong><br>
      <strong>Given that</strong> I want to validate the company’s quality, <strong>when</strong> I review its credentials, <strong>then</strong> I find certifications and recognitions visible from mobile.
    </td>
    <td>EP-06</td>
  </tr>

  <tr>
    <td>US-29</td>
    <td>RESTful API for room management</td>
    <td class="user-story-desc"><strong>As a</strong> developer, <strong>I want</strong> to access RESTful endpoints related to rooms from a mobile or development environment <strong>so that</strong> I can integrate Smart Stay with other systems.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Retrieve available rooms</strong><br>
      <strong>Given that</strong> I make a GET request to the corresponding endpoint, <strong>when</strong> the system processes it, <strong>then</strong> I receive a list of rooms with availability and prices.<br>
      <strong>Scenario 2: Update room status</strong><br>
      <strong>Given that</strong> I make a PUT request with a new status, <strong>when</strong> the system processes it, <strong>then</strong> the room is updated correctly.<br>
      <strong>Scenario 3: Create new reservation</strong><br>
      <strong>Given that</strong> I make a POST request with valid data, <strong>when</strong> the system processes it, <strong>then</strong> the reservation is created and a unique identifier is returned.<br>
      <strong>Scenario 4: Error handling</strong><br>
      <strong>Given that</strong> I send invalid data, <strong>when</strong> the system processes it, <strong>then</strong> I receive a clear and descriptive error.
    </td>
    <td>EP-07</td>
  </tr>

  <tr>
    <td>US-30</td>
    <td>API for IoT device control</td>
    <td class="user-story-desc"><strong>As a</strong> developer, <strong>I want</strong> to use endpoints from mobile applications or external systems <strong>so that</strong> I can control room IoT devices.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Check current device status</strong><br>
      <strong>Given that</strong> I make a request to the corresponding endpoint, <strong>when</strong> it is processed, <strong>then</strong> I obtain the current status of temperature, lights, and blinds.<br>
      <strong>Scenario 2: Control temperature</strong><br>
      <strong>Given that</strong> I send a desired temperature, <strong>when</strong> the request is valid, <strong>then</strong> the system adjusts the room climate.<br>
      <strong>Scenario 3: Control lighting</strong><br>
      <strong>Given that</strong> I send a lighting configuration, <strong>when</strong> the system processes it, <strong>then</strong> the devices are updated according to the submitted parameters.<br>
      <strong>Scenario 4: Check change history</strong><br>
      <strong>Given that</strong> I request the device logs, <strong>when</strong> the query is processed, <strong>then</strong> I receive the history of changes made.
    </td>
    <td>EP-07</td>
  </tr>

  <tr>
    <td>US-31</td>
    <td>API authentication and authorization</td>
    <td class="user-story-desc"><strong>As a</strong> developer, <strong>I want</strong> a secure authentication and authorization system <strong>so that</strong> I can access Smart Stay services from mobile applications or external integrations.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Obtain access token</strong><br>
      <strong>Given that</strong> I send valid credentials, <strong>when</strong> I request authentication, <strong>then</strong> I receive a token with an expiration time.<br>
      <strong>Scenario 2: Access with valid token</strong><br>
      <strong>Given that</strong> I include a valid token in the request, <strong>when</strong> I access a protected endpoint, <strong>then</strong> I receive a successful response.<br>
      <strong>Scenario 3: Expired token</strong><br>
      <strong>Given that</strong> the token has already expired, <strong>when</strong> I make a request, <strong>then</strong> I receive a 401 error with a clear message.<br>
      <strong>Scenario 4: Different access levels</strong><br>
      <strong>Given that</strong> I have limited permissions, <strong>when</strong> I attempt an unauthorized action, <strong>then</strong> I receive a 403 error.
    </td>
    <td>EP-07</td>
  </tr>

  <tr>
    <td>US-32</td>
    <td>Interactive API documentation</td>
    <td class="user-story-desc"><strong>As a</strong> developer, <strong>I want</strong> to access interactive documentation accessible from mobile or desktop devices <strong>so that</strong> I can easily integrate with Smart Stay.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Explore available endpoints</strong><br>
      <strong>Given that</strong> I enter the documentation, <strong>when</strong> I browse it, <strong>then</strong> I see endpoints organized by category.<br>
      <strong>Scenario 2: Test endpoints live</strong><br>
      <strong>Given that</strong> I use the test option, <strong>when</strong> I send a request, <strong>then</strong> I can see the response directly.<br>
      <strong>Scenario 3: Code examples</strong><br>
      <strong>Given that</strong> I review an endpoint, <strong>when</strong> I access its details, <strong>then</strong> I find examples in several languages.<br>
      <strong>Scenario 4: Data schemas</strong><br>
      <strong>Given that</strong> I need to understand the structure, <strong>when</strong> I review the documentation, <strong>then</strong> I see complete request and response schemas.
    </td>
    <td>EP-07</td>
  </tr>

  <tr>
    <td>US-33</td>
    <td>Webhooks for real-time events</td>
    <td class="user-story-desc"><strong>As a</strong> developer, <strong>I want</strong> to configure webhooks <strong>so that</strong> I can receive automatic notifications of important events and synchronize mobile applications or external systems.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Configure webhook</strong><br>
      <strong>Given that</strong> I register a URL and associated events, <strong>when</strong> I save the configuration, <strong>then</strong> the system sends notifications to that endpoint.<br>
      <strong>Scenario 2: Notification for new reservation</strong><br>
      <strong>Given that</strong> there is a webhook for reservations, <strong>when</strong> a new one is created, <strong>then</strong> the system automatically sends the information to the registered endpoint.<br>
      <strong>Scenario 3: Automatic retries</strong><br>
      <strong>Given that</strong> the endpoint does not respond, <strong>when</strong> delivery fails, <strong>then</strong> the system automatically retries several times.<br>
      <strong>Scenario 4: Security verification</strong><br>
      <strong>Given that</strong> I receive the webhook, <strong>when</strong> I verify the signature, <strong>then</strong> I can confirm that the event truly comes from Smart Stay.
    </td>
    <td>EP-07</td>
  </tr>

  <tr>
    <td>US-34</td>
    <td>Mobile push notification system</td>
    <td class="user-story-desc"><strong>As a</strong> guest, <strong>I want</strong> to receive push notifications on my smartphone about reservations, requests, and service statuses <strong>so that</strong> I can stay informed in real time.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Reservation confirmation</strong><br>
      <strong>Given that</strong> I make a reservation, <strong>when</strong> it is confirmed, <strong>then</strong> I receive an immediate push notification with details and next steps.<br>
      <strong>Scenario 2: Check-in reminder</strong><br>
      <strong>Given that</strong> my arrival is in 24 hours, <strong>when</strong> that moment arrives, <strong>then</strong> I receive a notification with a direct link to start digital check-in.<br>
      <strong>Scenario 3: Service updates</strong><br>
      <strong>Given that</strong> I requested room service, <strong>when</strong> its status changes, <strong>then</strong> I receive a notification with the updated progress.<br>
      <strong>Scenario 4: Preference settings</strong><br>
      <strong>Given that</strong> I want to control my notifications, <strong>when</strong> I access the settings, <strong>then</strong> I can choose which types of alerts to receive and at what times.
    </td>
    <td>EP-08</td>
  </tr>

  <tr>
    <td>US-35</td>
    <td>Automatic notifications for staff</td>
    <td class="user-story-desc"><strong>As a</strong> hotel staff member, <strong>I want</strong> to receive automatic notifications on my mobile device about assigned tasks and important operational changes <strong>so that</strong> I can respond quickly.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: New assigned task</strong><br>
      <strong>Given that</strong> the administrator assigns me a task, <strong>when</strong> it is created, <strong>then</strong> I receive an immediate notification with details, priority, and deadline.<br>
      <strong>Scenario 2: Priority change</strong><br>
      <strong>Given that</strong> a task becomes high priority, <strong>when</strong> it is updated, <strong>then</strong> I receive a special notification that requires read confirmation.<br>
      <strong>Scenario 3: Deadline reminders</strong><br>
      <strong>Given that</strong> I have a pending task, <strong>when</strong> the deadline approaches, <strong>then</strong> I receive a reminder 2 hours before.<br>
      <strong>Scenario 4: Operational emergencies</strong><br>
      <strong>Given that</strong> an emergency occurs, <strong>when</strong> it is reported, <strong>then</strong> the corresponding staff receive an immediate alert.
    </td>
    <td>EP-08</td>
  </tr>

  <tr>
    <td>US-36</td>
    <td>Automated and personalized emails</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to send automated and personalized emails to guests at different stages of their experience <strong>so that</strong> I can improve communication and loyalty.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Pre-arrival welcome email</strong><br>
      <strong>Given that</strong> a guest confirms their reservation, <strong>when</strong> 24 hours pass, <strong>then</strong> they receive an email with hotel information, available services, and an arrival guide.<br>
      <strong>Scenario 2: Email during the stay</strong><br>
      <strong>Given that</strong> the guest has stayed 2 or more days at the hotel, <strong>when</strong> the second day arrives, <strong>then</strong> they receive an email with local recommendations and special services.<br>
      <strong>Scenario 3: Post-stay and loyalty email</strong><br>
      <strong>Given that</strong> the guest has already checked out, <strong>when</strong> one week passes, <strong>then</strong> they receive a thank-you email with a special offer for their next visit.<br>
      <strong>Scenario 4: Segmented campaigns</strong><br>
      <strong>Given that</strong> I want to run a specific campaign, <strong>when</strong> I select criteria such as VIP guests or season, <strong>then</strong> I can send personalized emails to that segment.
    </td>
    <td>EP-08</td>
  </tr>

  <tr>
    <td>US-37</td>
    <td>Smart alerts and escalation</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to receive smart alerts about operational problems and have them automatically escalated if they are not handled on time <strong>so that</strong> I can ensure a timely response.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Alert for low satisfaction</strong><br>
      <strong>Given that</strong> a guest rates 2 stars or less, <strong>when</strong> they submit the evaluation, <strong>then</strong> I receive an immediate alert to take action.<br>
      <strong>Scenario 2: Critical technical problem</strong><br>
      <strong>Given that</strong> an IoT device stops responding for more than 10 minutes, <strong>when</strong> the system detects it, <strong>then</strong> I receive an alert with information about the problem and the affected room.<br>
      <strong>Scenario 3: Automatic escalation</strong><br>
      <strong>Given that</strong> an alert is not handled within the defined time, <strong>when</strong> that limit is exceeded, <strong>then</strong> it is automatically escalated to the supervisor or manager.<br>
      <strong>Scenario 4: Revenue and occupancy alerts</strong><br>
      <strong>Given that</strong> occupancy is below expectations, <strong>when</strong> the system detects that trend, <strong>then</strong> I receive an alert with adjustment suggestions.
    </td>
    <td>EP-08</td>
  </tr>

  <tr>
    <td>US-38</td>
    <td>Unified communication dashboard</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to have a centralized communication dashboard accessible from the mobile application <strong>so that</strong> I can manage all guest interactions from one place.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Unified conversation view</strong><br>
      <strong>Given that</strong> I enter the communication dashboard, <strong>when</strong> it loads, <strong>then</strong> I see all active conversations from different channels in a single interface.<br>
      <strong>Scenario 2: Respond from the central dashboard</strong><br>
      <strong>Given that</strong> a guest sends a message via WhatsApp, <strong>when</strong> I respond from the dashboard, <strong>then</strong> the response is automatically sent through the original channel.<br>
      <strong>Scenario 3: Unified guest history</strong><br>
      <strong>Given that</strong> I select a guest, <strong>when</strong> I open their communication profile, <strong>then</strong> I see the complete interaction history regardless of the channel.<br>
      <strong>Scenario 4: Conversation assignment</strong><br>
      <strong>Given that</strong> a complex inquiry arrives, <strong>when</strong> I decide to forward it, <strong>then</strong> I can assign it to specialized staff who receive the corresponding notification.
    </td>
    <td>EP-08</td>
  </tr>

  <tr>
    <td>US-39</td>
    <td>Native mobile application for staff</td>
    <td class="user-story-desc"><strong>As a</strong> hotel staff member, <strong>I want</strong> a native mobile application <strong>so that</strong> I can manage my tasks and communications while moving around the hotel.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Mobile task list</strong><br>
      <strong>Given that</strong> I open the staff application, <strong>when</strong> it loads, <strong>then</strong> I see my pending tasks organized by priority.<br>
      <strong>Scenario 2: Status update</strong><br>
      <strong>Given that</strong> I finish a task, <strong>when</strong> I mark it as completed from the app, <strong>then</strong> the change is synchronized immediately with the central system.<br>
      <strong>Scenario 3: Communication with administration</strong><br>
      <strong>Given that</strong> I have a question or problem, <strong>when</strong> I use the application chat, <strong>then</strong> I can communicate with administration in real time.<br>
      <strong>Scenario 4: Incident reporting</strong><br>
      <strong>Given that</strong> I find a problem, <strong>when</strong> I report it from the app with a photo and location, <strong>then</strong> an incident ticket is automatically created.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-40</td>
    <td>Data backup and recovery</td>
    <td class="user-story-desc"><strong>As a</strong> technical administrator, <strong>I want</strong> the system to allow monitoring of backups and recovery from a mobile interface <strong>so that</strong> I can guarantee operational continuity.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic daily backup</strong><br>
      <strong>Given that</strong> the operational day ends, <strong>when</strong> midnight arrives, <strong>then</strong> the system creates an automatic backup copy.<br>
      <strong>Scenario 2: Integrity verification</strong><br>
      <strong>Given that</strong> a backup is generated, <strong>when</strong> the process finishes, <strong>then</strong> the system validates the integrity of the information.<br>
      <strong>Scenario 3: Recovery in case of failure</strong><br>
      <strong>Given that</strong> a critical failure occurs, <strong>when</strong> I start the recovery process, <strong>then</strong> the system restores operation with the most recent backup.<br>
      <strong>Scenario 4: Error notification</strong><br>
      <strong>Given that</strong> the backup process fails, <strong>when</strong> the system detects the problem, <strong>then</strong> administrators receive an alert in the mobile app.
    </td>
    <td>EP-07</td>
  </tr>

  <tr>
    <td>US-41</td>
    <td>System monitoring and logs</td>
    <td class="user-story-desc"><strong>As a</strong> technical administrator, <strong>I want</strong> to monitor system performance and review logs from a mobile application <strong>so that</strong> I can detect and solve problems quickly.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Performance dashboard</strong><br>
      <strong>Given that</strong> I access the monitoring section from the app, <strong>when</strong> it loads, <strong>then</strong> I see metrics such as response time, CPU usage, memory usage, and errors.<br>
      <strong>Scenario 2: Performance alerts</strong><br>
      <strong>Given that</strong> response time exceeds the defined limit, <strong>when</strong> the system detects it, <strong>then</strong> I receive an automatic alert.<br>
      <strong>Scenario 3: Centralized logs</strong><br>
      <strong>Given that</strong> I need to investigate a problem, <strong>when</strong> I enter the log history from mobile, <strong>then</strong> I can filter by date, user, action, or error level.<br>
      <strong>Scenario 4: Trend analysis</strong><br>
      <strong>Given that</strong> I want to optimize performance, <strong>when</strong> I review historical metrics, <strong>then</strong> I can identify patterns and bottlenecks.
    </td>
    <td>EP-07</td>
  </tr>

  <tr>
    <td>US-42</td>
    <td>Multi-hotel configuration for chains</td>
    <td class="user-story-desc"><strong>As a</strong> hotel chain administrator, <strong>I want</strong> to manage multiple properties from a mobile application <strong>so that</strong> I can centralize operations with independent configurations.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Consolidated chain view</strong><br>
      <strong>Given that</strong> I manage several hotels, <strong>when</strong> I access the master dashboard from the app, <strong>then</strong> I see consolidated KPIs with details by property.<br>
      <strong>Scenario 2: Per-hotel configuration</strong><br>
      <strong>Given that</strong> each hotel has different needs, <strong>when</strong> I configure one from the app, <strong>then</strong> I can customize services, pricing, and operations without affecting the others.<br>
      <strong>Scenario 3: Shared staff</strong><br>
      <strong>Given that</strong> there are employees who work in several hotels, <strong>when</strong> I assign them from the app, <strong>then</strong> they can access only the authorized properties.<br>
      <strong>Scenario 4: Consolidated reports</strong><br>
      <strong>Given that</strong> I need a global analysis, <strong>when</strong> I generate reports from mobile, <strong>then</strong> I obtain individual metrics and comparisons between hotels.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-43</td>
    <td>Integration with existing PMS systems</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to integrate Smart Stay with my current PMS <strong>so that</strong> I can migrate progressively without interrupting operations, while being able to supervise this integration from the mobile app.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Bidirectional synchronization</strong><br>
      <strong>Given that</strong> I have an existing PMS, <strong>when</strong> I configure the integration, <strong>then</strong> reservations are synchronized automatically in both directions.<br>
      <strong>Scenario 2: Gradual migration of functionalities</strong><br>
      <strong>Given that</strong> I want to adopt Smart Stay progressively, <strong>when</strong> I activate specific modules, <strong>then</strong> they can coexist with my current PMS.<br>
      <strong>Scenario 3: Consistency validation</strong><br>
      <strong>Given that</strong> there is data in both systems, <strong>when</strong> it is synchronized, <strong>then</strong> I receive alerts if discrepancies are detected.<br>
      <strong>Scenario 4: Access to the previous system</strong><br>
      <strong>Given that</strong> I am in transition, <strong>when</strong> I complete the migration, <strong>then</strong> I keep read-only access to the previous PMS for a defined period of time.
    </td>
    <td>EP-05</td>
  </tr>

  <tr>
    <td>US-44</td>
    <td>Brand customization per hotel</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to customize the application interface and communications with my hotel’s brand <strong>so that</strong> I can maintain visual and identity consistency.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Customization of colors and logo</strong><br>
      <strong>Given that</strong> I want to adapt the appearance, <strong>when</strong> I upload my logo and define colors, <strong>then</strong> the entire web and mobile interface is updated with my hotel’s visual identity.<br>
      <strong>Scenario 2: Branded personalized emails</strong><br>
      <strong>Given that</strong> automatic communications are sent, <strong>when</strong> they reach the guest, <strong>then</strong> they include the hotel’s logo, colors, and personalized message.<br>
      <strong>Scenario 3: Customized landing page</strong><br>
      <strong>Given that</strong> guests access digital services, <strong>when</strong> they enter, <strong>then</strong> they see an interface completely aligned with the hotel brand.<br>
      <strong>Scenario 4: Message configuration</strong><br>
      <strong>Given that</strong> I want to adapt communication, <strong>when</strong> I configure templates, <strong>then</strong> I can adjust the tone and content of automatic messages.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-45</td>
    <td>Integrated loyalty program</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to manage a loyalty program for recurring guests from the application and system <strong>so that</strong> I can offer automatic benefits and increase retention.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic point accumulation</strong><br>
      <strong>Given that</strong> the guest completes a stay, <strong>when</strong> they check out, <strong>then</strong> they automatically accumulate points according to their total spending and duration.<br>
      <strong>Scenario 2: Tier-based benefits</strong><br>
      <strong>Given that</strong> the guest reaches a VIP level, <strong>when</strong> they make a new reservation, <strong>then</strong> they receive automatic benefits such as an upgrade, late check-out, or amenities.<br>
      <strong>Scenario 3: Personalized offers</strong><br>
      <strong>Given that</strong> guest history exists, <strong>when</strong> a likely travel date approaches, <strong>then</strong> they receive special offers based on their preferences.<br>
      <strong>Scenario 4: Benefit redemption</strong><br>
      <strong>Given that</strong> the guest has enough points, <strong>when</strong> they want to use them from the app, <strong>then</strong> they can redeem them for services, upgrades, or free nights.
    </td>
    <td>EP-03</td>
  </tr>

  <tr>
    <td>US-46</td>
    <td>Event and conference management</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to manage events and conferences from the mobile application <strong>so that</strong> I can offer specific functionalities for groups and organizers.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Create group event</strong><br>
      <strong>Given that</strong> I receive an event request, <strong>when</strong> I register it from the app, <strong>then</strong> I can define special rates, block rooms, and assign services.<br>
      <strong>Scenario 2: Mass check-in</strong><br>
      <strong>Given that</strong> event participants arrive, <strong>when</strong> they start check-in from the app, <strong>then</strong> they can use a special code to speed up the process.<br>
      <strong>Scenario 3: Group communication</strong><br>
      <strong>Given that</strong> there is an active event, <strong>when</strong> I need to send information, <strong>then</strong> I can send mass messages only to its participants.<br>
      <strong>Scenario 4: Consolidated billing</strong><br>
      <strong>Given that</strong> the event ends, <strong>when</strong> I generate the billing from the app, <strong>then</strong> I can issue a master invoice or individual invoices according to the configuration.
    </td>
    <td>EP-02</td>
  </tr>

  <tr>
    <td>US-47</td>
    <td>Predictive IoT maintenance</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to receive predictive maintenance alerts and recommendations in the mobile application <strong>so that</strong> I can reduce failures and downtime.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Continuous monitoring</strong><br>
      <strong>Given that</strong> IoT devices are installed, <strong>when</strong> they are operating, <strong>then</strong> the system continuously monitors their performance, consumption, and usage.<br>
      <strong>Scenario 2: Predictive alerts</strong><br>
      <strong>Given that</strong> a piece of equipment shows signs of wear, <strong>when</strong> the system detects an anomaly, <strong>then</strong> I receive an alert with a preventive recommendation.<br>
      <strong>Scenario 3: Automatic scheduling</strong><br>
      <strong>Given that</strong> maintenance is required, <strong>when</strong> I accept the recommendation from the app, <strong>then</strong> the intervention is automatically scheduled.<br>
      <strong>Scenario 4: Performance history</strong><br>
      <strong>Given that</strong> I want to review equipment behavior, <strong>when</strong> I check the section from mobile, <strong>then</strong> I see the complete history and maintenance performed.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-48</td>
    <td>Competitor analysis and dynamic pricing</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to analyze competitor prices and adjust rates from the mobile application <strong>so that</strong> I can optimize revenue and occupancy.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Competitor price monitoring</strong><br>
      <strong>Given that</strong> I configure competitor hotels, <strong>when</strong> the system analyzes their prices, <strong>then</strong> I see daily comparisons from the app.<br>
      <strong>Scenario 2: Price suggestions</strong><br>
      <strong>Given that</strong> market conditions change, <strong>when</strong> the system detects variations, <strong>then</strong> I receive rate adjustment recommendations.<br>
      <strong>Scenario 3: Automatic rate adjustment</strong><br>
      <strong>Given that</strong> I activate dynamic pricing, <strong>when</strong> certain conditions are met, <strong>then</strong> the system updates rates within the allowed ranges.<br>
      <strong>Scenario 4: Elasticity analysis</strong><br>
      <strong>Given that</strong> price changes are recorded, <strong>when</strong> I generate the analysis from the app, <strong>then</strong> I see the impact on occupancy and revenue.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-49</td>
    <td>Regulatory compliance and automated auditing</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to consult compliance and audit reports from the mobile application <strong>so that</strong> I can facilitate regulatory reviews and ensure traceability.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic regulatory reports</strong><br>
      <strong>Given that</strong> legal obligations exist, <strong>when</strong> the corresponding period ends, <strong>then</strong> the system automatically generates the required reports.<br>
      <strong>Scenario 2: Full traceability</strong><br>
      <strong>Given that</strong> I need an audit, <strong>when</strong> I export information from the app, <strong>then</strong> I obtain the transaction and change history with timestamps.<br>
      <strong>Scenario 3: Tax validation</strong><br>
      <strong>Given that</strong> payments are recorded, <strong>when</strong> they are processed, <strong>then</strong> the system validates that they comply with tax requirements.<br>
      <strong>Scenario 4: Organized digital archive</strong><br>
      <strong>Given that</strong> I must review documents for an audit, <strong>when</strong> I access them from the app, <strong>then</strong> I find files organized by period, type, and guest.
    </td>
    <td>EP-04</td>
  </tr>

  <tr>
    <td>US-50</td>
    <td>Integration with security systems</td>
    <td class="user-story-desc"><strong>As an</strong> administrator, <strong>I want</strong> to integrate Smart Stay with the hotel’s security systems <strong>so that</strong> I can automate access management and improve operational control.</td>
    <td class="acceptance-criteria">
      <strong>Scenario 1: Automatic generation of access code</strong><br>
      <strong>Given that</strong> the guest completes digital check-in, <strong>when</strong> it is confirmed, <strong>then</strong> the system automatically generates a unique code for their room with a defined validity period.<br>
      <strong>Scenario 2: Automatic revocation after check-out</strong><br>
      <strong>Given that</strong> the guest completes check-out, <strong>when</strong> departure is confirmed, <strong>then</strong> all their access codes are automatically revoked.<br>
      <strong>Scenario 3: Temporary access for staff</strong><br>
      <strong>Given that</strong> a staff member needs to enter a room for cleaning or maintenance, <strong>when</strong> the task is assigned, <strong>then</strong> they receive a temporary code valid only during their shift.<br>
      <strong>Scenario 4: Access logs and alerts</strong><br>
      <strong>Given that</strong> any access code is used, <strong>when</strong> entry occurs, <strong>then</strong> it is recorded in a central log and alerts are generated for after-hours access.
    </td>
    <td>EP-05</td>
  </tr>
</table>


## 3.3. Product Backlog

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Order</th>
      <th>User Story Id</th>
      <th>Title</th>
      <th>Description</th>
      <th>Story Points (1 / 2 / 3 / 5 / 8)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>US-24</td>
      <td>Segmented landing page</td>
      <td><strong>As</strong> a visitor, <strong>I want</strong> to find specific information according to my profile (hotel administrator or guest) <strong>to</strong> understand Smart Stay's value.</td>
      <td>5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>US-27</td>
      <td>Demo request and commercial contact</td>
      <td><strong>As</strong> an interested visitor, <strong>I want</strong> to request a demonstration and contact the sales team easily and quickly <strong>to</strong> explore Smart Stay solutions.</td>
      <td>3</td>
    </tr>
    <tr>
      <td>4</td>
      <td>US-26</td>
      <td>Success stories and testimonials</td>
      <td><strong>As</strong> an interested visitor, <strong>I want</strong> to see real success stories from hotels using Smart Stay <strong>to</strong> validate solution effectiveness.</td>
      <td>5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>US-28</td>
      <td>Corporate information and values</td>
      <td><strong>As</strong> a visitor, <strong>I want</strong> to know Smart Stay's mission, vision and values <strong>to</strong> understand the company's philosophy.</td>
      <td>2</td>
    </tr>
    <tr>
      <td>12</td>
      <td>US-01</td>
      <td>User registration with validation</td>
      <td><strong>As</strong> a new user, <strong>I want</strong> to register in Smart Stay by validating my email <strong>to</strong> access functionalities according to my role.</td>
      <td>3</td>
    </tr>
    <tr>
      <td>13</td>
      <td>US-02</td>
      <td>Secure login</td>
      <td><strong>As</strong> a registered user, <strong>I want</strong> to login securely <strong>to</strong> access my personalized dashboard according to my role.</td>
      <td>3</td>
    </tr>
    <tr>
      <td>29</td>
      <td>US-29</td>
      <td>RESTful API for room management</td>
      <td><strong>As</strong> a developer, <strong>I want</strong> to access RESTful endpoints <strong>to</strong> integrate Smart Stay with external hotel management systems.</td>
      <td>8</td>
    </tr>
    <tr>
      <td>30</td>
      <td>US-30</td>
      <td>API for IoT device control</td>
      <td><strong>As</strong> a developer, <strong>I want</strong> endpoints to control room IoT devices <strong>to</strong> enable integration with external applications.</td>
      <td>8</td>
    </tr>
    <tr>
      <td>31</td>
      <td>US-31</td>
      <td>API authentication and authorization</td>
      <td><strong>As</strong> a developer, <strong>I want</strong> a secure authentication system <strong>to</strong> access Smart Stay API endpoints safely.</td>
      <td>5</td>
    </tr>
    <tr>
      <td>32</td>
      <td>US-32</td>
      <td>Interactive API documentation</td>
      <td><strong>As</strong> a developer, <strong>I want</strong> to access complete and interactive documentation <strong>to</strong> easily integrate with Smart Stay API.</td>
      <td>3</td>
    </tr>
    <tr>
      <td>34</td>
      <td>US-03</td>
      <td>Profile and role management</td>
      <td><strong>As</strong> an administrator, <strong>I want</strong> to manage users, assign roles and permissions <strong>to</strong> control access to different functionalities.</td>
      <td>5</td>
    </tr>
    <tr>
      <td>35</td>
      <td>US-04</td>
      <td>Password recovery</td>
      <td><strong>As</strong> a user, <strong>I want</strong> to recover my password via email <strong>to</strong> regain access to my account.</td>
      <td>2</td>
    </tr>
    <tr>
  </tbody>
</table>

## 3.4. Impact Mapping

#### Impact Mapping Segmento 1: Hotel Administrador

![impactmaphotel.png](../assets/chapter-3/impact-mapping/impact-map-hotel.png)

#### Impact Mapping Segmento 2: Traveler

![impactmaptraveler.png](../assets/chapter-3/impact-mapping/impact-map-traveler.png)

### Mapa de impacto integrado

<div align="center">
<img src="../assets/chapter-3/impact-mapping/impact-mapping-overview.png" alt="impact mapping" style="max-width: 90%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
</div>
