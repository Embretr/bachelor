# Scope and Delimitations — Ressursplanlegger

> Claude never writes about out-of-scope items as implemented features.
> Claude never implies out-of-scope items will be built.
> Update this file when scope changes — update thesis-spine.md too.
> Owner: Mikael — confirm with Embret before finalising.

---

## In Scope

### Core Planning Interface
- Viewing all assignments for a selected day or week
- Viewing driver availability and vehicle status
- Algorithm-generated daily plan displayed to the traffic coordinator
- Manual assignment of a driver and vehicle to an assignment
- Manual override of algorithm-generated assignments
- Approval of the complete daily plan by the traffic coordinator

### Driver and Vehicle Management
- Driver profiles: name, licence class, competence, availability status
- Vehicle profiles: type, registration, current status
- Sick-leave registration and its effect on the daily plan

### Optimisation Algorithm
- Automatic generation of a daily plan from available assignments, drivers, and vehicles
- Modelling of hard constraints: driving/rest time, licence class, vehicle type requirements
- [FILL IN: soft constraints modelled]
- [FILL IN: objective function — what is maximised]

---

## Out of Scope

The following are explicitly excluded. They may be mentioned as future work but must not be described as implemented.

### Driver-Facing Features
- Driver mobile app or any driver-facing interface
- Real-time driver notifications via push or SMS
- Driver self-service (accepting/declining assignments)

### External Integrations
- Billing and invoicing systems
- Payroll integration
- GPS tracking and real-time location data
- Integration with Timpex, Trimtex, or any existing TMS

### Multi-Tenant / Commercial
- Multi-company SaaS functionality
- Role-based access for customers or third parties
- Subscription management or pricing

### Advanced Planning Features
- Weekly or monthly planning horizon (daily only unless confirmed otherwise)
- Automatic sick-leave replanning without coordinator input
- Customer portal or external booking interface

---

## Boundary Cases

> Document decisions about items that are partially in scope.

| Item | Decision | Reason |
|------|----------|--------|
| [FILL IN] | | |

---

## Confirmed by

- [ ] Embret — technical scope confirmed
- [ ] Mikael — user research scope confirmed
- [ ] Supervisor — [FILL IN NAME] — approved [DATE]
