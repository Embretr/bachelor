# Scope and Delimitations — Ressursplanlegger

> Claude never writes about out-of-scope items as implemented features.
> Claude never implies out-of-scope items will be built.
> Update this file when scope changes — update thesis-spine.md too.
> Owner: Mikael — confirm with Embret before finalising.

---

## In Scope

### Core Planning Interface
- Viewing all assignments for a selected day or week
- Viewing driver availability and vehicle status in a unified timeline
- Algorithm-generated daily plan displayed to the traffic coordinator
- Manual assignment of a driver and vehicle to an assignment (drag-and-drop or modal)
- Manual override of algorithm-generated assignments
- Approval of the complete daily plan by the traffic coordinator
- Recurring assignments (daily, weekly, biweekly, monthly)
- Priority levels on assignments (low, medium, high)
- Status workflow for assignments (planned → approved → in progress → completed → cancelled)

### Driver and Vehicle Management
- Driver profiles: name, role, department, phone, email, availability, contracted hours
- Driver competencies and certifications with expiry tracking
- Weekly work schedules per driver (day-by-day availability)
- Time-off registration (vacation, sick leave) and its effect on the daily plan
- Vehicle profiles: name, type, capacity, department, status
- Vehicle maintenance tracking (next service date, EU control, crane inspection, lease expiry)
- Vehicle status management (active, maintenance, out of service)
- Trailers and vehicle–trailer associations
- Utilisation metrics for both drivers and vehicles

### Optimisation Algorithm
- Automatic generation of a daily plan from available assignments, drivers, and vehicles
- Three pluggable solver engines: greedy baseline (Python), OR-Tools CP-SAT (Python), Timefold (Java)
- Hard constraints enforced by the algorithm:
  - Employee must possess all required competencies (HC-01)
  - Employee must be available — within schedule, not on time-off, not already assigned (HC-02)
  - Vehicle must be in active status (HC-03)
  - Vehicle type must match assignment requirement (HC-04)
  - No employee double-booking (HC-05)
  - No vehicle double-booking (HC-06)
- Soft constraints with configurable weights:
  - Prefer assigning employee to their designated vehicle (SC-01)
  - Balance workload evenly across employees (SC-02)
  - Minimise transitions between consecutive assignments (SC-03)
  - Schedule high-priority assignments first (SC-04)
  - Respect stated employee preferences (SC-05)
- User-configurable constraint weights — the coordinator decides how much each soft constraint matters
- Solution scoring and quality evaluation
- Benchmarking framework for comparing solver performance

### Conflict Detection
- Automated detection of scheduling violations after plan generation:
  - Incomplete assignments (no employee or vehicle)
  - Employee overbooking (concurrent assignments)
  - Overtime violations
  - Missing competencies
  - Night work conflicts
  - Expired certifications
  - Vehicle maintenance conflicts
  - Rest period violations
  - Unavailable employee assignments
- Deviations displayed inline on the planning timeline and in a dedicated view
- Severity levels (low, medium, high) and status tracking (open, acknowledged, resolved, dismissed)

### Multi-Tenancy and Authentication
- Company-scoped workspaces with data isolation
- Email/password authentication via Better Auth
- Session-based access control
- Token-based company invitation system with roles (owner, admin, member)
- User settings: language, timezone, week start day, notification preferences

### Dashboard and Overview
- Dashboard overview page with key metrics
- Utilisation charts (Recharts)
- All-assignments list view with filtering

---

## Out of Scope

The following are explicitly excluded from the thesis and the system. They may be mentioned as future work in Chapter 6 but must not be described as implemented or planned for delivery.

### Driver-Facing Features
- Driver mobile app or any driver-facing mobile interface
- Real-time driver notifications via push or SMS
- Driver self-service (accepting/declining assignments from the driver's side)

> **Note:** A driver-facing page within the web application is planned but not yet implemented. It is not part of the thesis deliverable. If it is built before submission, update this file.

### External Integrations
- Billing and invoicing systems (identified as important by interviewees, but out of scope)
- Payroll integration
- GPS tracking and real-time location data
- Integration with Timpex, Trimtex, Opptur, or any existing TMS
- External data source integration (e.g., weather, traffic)

### Multi-Tenant Commercial Features
- Multi-company SaaS functionality (subscription management, pricing, onboarding)
- Customer-facing portal or external booking interface
- Role-based access for customers or third parties

### Advanced Planning Features
- Weekly or monthly planning horizon (daily only)
- Automatic sick-leave replanning without coordinator input
- Real-time replanning triggered by live events (e.g., vehicle breakdown mid-route)
- Route optimisation with geographic coordinates and travel time estimation

### Administration
- Admin panel for managing users, roles, and permissions within a company (auth exists, admin UI does not)
- Two-factor authentication (framework exists in Better Auth, not enabled)
- Audit logging of user actions

---

## Boundary Cases

Items that are partially in scope or where the boundary requires clarification.

| Item | Decision | Reason |
|------|----------|--------|
| Driver page (web) | Planned, not in thesis scope | Development started after thesis scope was frozen. If completed before submission, may be mentioned but not evaluated. |
| User admin panel | Auth works, no admin UI | Auth and invitation system are in scope. A dedicated admin panel for user management is not. |
| Recurring assignments | In scope | Implemented — coordinators can create daily, weekly, biweekly, or monthly recurring assignments. |
| Team management | In scope | Fixed and variable teams with employee and vehicle pools are implemented. |
| Multi-engine comparison | In scope | Comparing solver quality and performance across engines is a research contribution. |
| Invoicing | Out of scope | Multiple interviewees flagged this as critical. Acknowledged as a limitation, recommended as future work. |

---

## Confirmed by

- [ ] Embret — technical scope confirmed
- [ ] Mikael — user research scope confirmed
- [ ] Supervisor — [FILL IN NAME] — approved [DATE]
