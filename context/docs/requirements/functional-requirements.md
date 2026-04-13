# Functional Requirements — Ressursplanlegger

> **Owner: Mikael** — derived from interviews-summary.md, verified against implemented features.
> MoSCoW: Must / Should / Could / Won't
> Source indicates which interview(s) or stakeholder prompted the requirement.
> Implementation status reflects the actual codebase — see requirements-traceability.md for test status.

---

## Planning and Assignment

| ID | Requirement | Priority | Source | Implemented |
|----|-------------|:--------:|--------|:-----------:|
| FK-01 | The system shall display all assignments for a selected day in a timeline view | Must | All interviews | Yes |
| FK-02 | The coordinator shall be able to manually assign a driver and vehicle to an assignment | Must | All interviews | Yes |
| FK-03 | The system shall generate an optimised daily plan via a scheduling algorithm | Must | Ressursplanlegger team | Yes |
| FK-04 | The coordinator shall be able to override any algorithm-generated assignment | Must | Ottem, Nordic Crane | Yes |
| FK-05 | The system shall support recurring assignments (daily, weekly, biweekly, monthly) | Should | Norlog Lakselv, Norlog Mo i Rana | Yes |
| FK-06 | The coordinator shall be able to set priority levels on assignments (low, medium, high) | Should | Ressursplanlegger team | Yes |
| FK-07 | The system shall track assignment status through a workflow (planned → approved → in progress → completed → cancelled) | Must | All interviews | Yes |
| FK-08 | The coordinator shall be able to drag and drop assignments on the timeline to reassign them | Could | Ressursplanlegger team | Yes |

## Driver and Vehicle Management

| ID | Requirement | Priority | Source | Implemented |
|----|-------------|:--------:|--------|:-----------:|
| FK-09 | The system shall store driver licence classes and competencies | Must | Norlog Lakselv, Nordic Crane | Yes |
| FK-10 | The system shall track certifications with expiry dates and flag expired ones | Should | Nordic Crane | Yes |
| FK-11 | The system shall show which drivers are available at a given time | Should | All interviews | Yes |
| FK-12 | The system shall allow registration of time-off (vacation, sick leave) with effect on the daily plan | Must | Norlog Tana, Ottem | Yes |
| FK-13 | The system shall maintain weekly work schedules per driver (day-by-day availability) | Should | Norlog Lakselv, Norlog Mo i Rana | Yes |
| FK-14 | The system shall store vehicle profiles with type, capacity, and status | Must | All interviews | Yes |
| FK-15 | The system shall track vehicle maintenance dates (next service, EU control, crane inspection) | Should | Nordic Crane, Ottem | Yes |
| FK-16 | The system shall support vehicle status management (active, maintenance, out of service) | Should | Ottem | Yes |
| FK-17 | The system shall calculate and display utilisation metrics for drivers and vehicles | Could | Ressursplanlegger team | Yes |
| FK-18 | The system shall support trailers and vehicle–trailer associations | Could | Nordic Crane | Yes |

## Optimisation and Algorithm

| ID | Requirement | Priority | Source | Implemented |
|----|-------------|:--------:|--------|:-----------:|
| FK-19 | The algorithm shall enforce hard constraints: required competencies, driver availability, vehicle status, vehicle type match, no double-booking | Must | All interviews | Yes |
| FK-20 | The algorithm shall optimise soft constraints: workload balance, driver–vehicle preference, priority scheduling, transition minimisation | Should | Ressursplanlegger team | Yes |
| FK-21 | The coordinator shall be able to configure the weight of each soft constraint | Should | All interviews (consensus: user control) | Yes |
| FK-22 | The system shall support multiple optimisation engines selectable at runtime | Could | Ressursplanlegger team | Yes |
| FK-23 | The system shall score and display the quality of a generated solution | Should | Ressursplanlegger team | Yes |

## Conflict Detection

| ID | Requirement | Priority | Source | Implemented |
|----|-------------|:--------:|--------|:-----------:|
| FK-24 | The system shall automatically detect scheduling conflicts after plan generation | Must | All interviews | Yes |
| FK-25 | The system shall detect employee overbooking (concurrent assignments) | Must | Norlog Mo i Rana, Ottem | Yes |
| FK-26 | The system shall detect overtime violations | Should | Nordic Crane | Yes |
| FK-27 | The system shall detect missing competency assignments | Must | Norlog Lakselv, Nordic Crane | Yes |
| FK-28 | The system shall detect expired certifications | Should | Nordic Crane | Yes |
| FK-29 | The system shall display deviations inline on the planning timeline and in a dedicated view | Should | Ressursplanlegger team | Yes |
| FK-30 | The system shall display driving/rest-time status for drivers | Should | Nordic Crane | Partial |

## Authentication and Multi-Tenancy

| ID | Requirement | Priority | Source | Implemented |
|----|-------------|:--------:|--------|:-----------:|
| FK-31 | The system shall support email/password authentication | Must | Ressursplanlegger team | Yes |
| FK-32 | The system shall isolate data per company (multi-tenant) | Must | Ressursplanlegger team | Yes |
| FK-33 | The system shall support inviting new users to a company via a token-based link | Should | Ressursplanlegger team | Yes |
| FK-34 | The system shall support user roles within a company (owner, admin, member) | Should | Ottem (multiple departments) | Yes |

## Dashboard and Overview

| ID | Requirement | Priority | Source | Implemented |
|----|-------------|:--------:|--------|:-----------:|
| FK-35 | The system shall provide a dashboard overview with key operational metrics | Should | Ressursplanlegger team | Yes |
| FK-36 | The system shall provide an all-assignments list view with filtering | Should | Ressursplanlegger team | Yes |
| FK-37 | The system shall display utilisation charts for drivers and vehicles | Could | Ressursplanlegger team | Yes |

## Not Implemented (Won't — out of scope)

| ID | Requirement | Priority | Source | Implemented |
|----|-------------|:--------:|--------|:-----------:|
| FK-38 | The system shall provide a driver-facing page showing the driver's own schedule | Won't (this version) | All interviews | No |
| FK-39 | The system shall integrate with billing/invoicing systems | Won't | Norlog Lakselv, Norlog Mo i Rana, Harlem Solutions | No |
| FK-40 | The system shall send push notifications to drivers when assignments change | Won't | Norlog Tana, Nordic Crane | No |
| FK-41 | The system shall provide an admin panel for managing users and permissions | Won't (this version) | Ressursplanlegger team | No |
| FK-42 | The system shall provide GPS tracking and real-time location data | Won't | Bergen Bulk Transport | No |

---

## Notes

- Requirements FK-38 through FK-42 are documented as "Won't" for this version. They are acknowledged as relevant based on interview findings and should be mentioned as future work in Chapter 6.
- FK-30 (driving/rest-time status) is marked as partial — the system tracks work schedules and time-off but does not have a real-time driving-hours counter based on tachograph data.
- All "Implemented: Yes" entries have been verified against the actual codebase. Test status is tracked separately in `requirements-traceability.md`.