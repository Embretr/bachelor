# Requirements Traceability — Ressursplanlegger

> **Owner: Embret** — codebase references and test status per implemented feature.
> Used in §3.6 ¶4 (evaluation framework — coverage check) and §4.6 (DSR Artifacts Mapping).
>
> IDs are aligned with `functional-requirements.md` (FK-01 through FK-42). Every functional requirement has the same ID across both files.
>
> "Tested" here means *verified to function during development* — there is no formal automated test suite. This is acknowledged as L9 in §5.4.

---

## Functional Requirements (FK-01 to FK-42)

### Planning and Assignment

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| FK-01 | Display assignments for selected day in timeline | ✅ | ✅ | `/ressursplanlegger` — Gantt-style timeline with date selector |
| FK-02 | Manual driver/vehicle assignment | ✅ | ✅ | `assignment.assignEmployeeToAssignment` + `assignVehicleToAssignment` tRPC mutations |
| FK-03 | Algorithm-generated optimised plan | ✅ | ✅ | `optimization.runOptimization` — three engines selectable (see FK-22) |
| FK-04 | Coordinator override of algorithm assignment | ✅ | ✅ | Override flow in assignment detail panel; accept/modify/reject |
| FK-05 | Recurring assignments (daily / weekly / biweekly / monthly) | ✅ | ✅ | `Assignment.isRecurring` + `recurringPattern` field |
| FK-06 | Priority levels on assignments | ✅ | ✅ | `Assignment.priority` (low / medium / high) |
| FK-07 | Assignment status workflow | ✅ | ✅ | `Assignment.status` — planned → approved → in progress → completed / cancelled |
| FK-08 | Drag-and-drop reassignment on timeline | ✅ | ✅ | Timeline UI in `/ressursplanlegger` |

### Driver and Vehicle Management

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| FK-09 | Store driver licence classes and competencies | ✅ | ✅ | `Competence` model; `employee.addCompetence` |
| FK-10 | Track certifications with expiry; flag expired | ✅ | ✅ | `Certification` model with `expiresAt`; `employee.addCertification` |
| FK-11 | Show drivers available at a given time | ✅ | ✅ | Employee profile + planning timeline availability view |
| FK-12 | Time-off (vacation, sick leave) with effect on plan | ✅ | ✅ | `employee.addTimeOff`; affects deviation detection |
| FK-13 | Weekly work schedules per driver | ✅ | ✅ | `WorkSchedule` model — day-by-day availability |
| FK-14 | Vehicle profiles (type, capacity, status) | ✅ | ✅ | `Vehicle` model |
| FK-15 | Track vehicle maintenance dates | ✅ | ✅ | Maintenance fields on `Vehicle`; flagged in deviation detection |
| FK-16 | Vehicle status management | ✅ | ✅ | `vehicle.setStatus` — active / maintenance / out_of_service |
| FK-17 | Utilisation metrics for drivers and vehicles | ✅ | ✅ | Computed in dashboard + utilisation charts |
| FK-18 | Trailers and vehicle–trailer associations | ✅ | ✅ | `Trailer` model + association on `Assignment` |

### Optimisation and Algorithm

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| FK-19 | Hard constraints in algorithm | ✅ | ✅ | Competencies, availability, vehicle status, vehicle type, no double-booking — enforced in all three solvers |
| FK-20 | Soft constraints with weighted optimisation | ✅ | ✅ | Workload balance, driver–vehicle preference, priority scheduling, transition minimisation |
| FK-21 | Configurable soft-constraint weights | ✅ | ✅ | Per-company weight configuration UI; flows into solver objective function |
| FK-22 | Multiple optimisation engines selectable at runtime | ✅ | ✅ | `engine` parameter — `"greedy"`, `"ortools"`, `"timefold"` |
| FK-23 | Score and display solution quality | ✅ | ✅ | Hard score + soft score returned with each optimisation run |

### Conflict Detection

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| FK-24 | Auto-detect conflicts after plan generation | ✅ | ✅ | Deviation scanner runs post-optimisation |
| FK-25 | Detect employee overbooking | ✅ | ✅ | Deviation type: `overbooking` |
| FK-26 | Detect overtime violations | ✅ | ✅ | Deviation type: `overtime` |
| FK-27 | Detect missing-competency assignments | ✅ | ✅ | Deviation type: `missing_competency` |
| FK-28 | Detect expired certifications | ✅ | ✅ | Deviation type: `expired_certification` |
| FK-29 | Display deviations inline + dedicated view | ✅ | ✅ | Inline on planning timeline + `/avvik` page |
| FK-30 | Display driving/rest-time status | ⚠️ Partial | ⚠️ Partial | Work-schedule + time-off tracked; no real-time tachograph counter |

### Authentication and Multi-Tenancy

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| FK-31 | Email/password authentication | ✅ | ✅ | Better Auth; session in PostgreSQL |
| FK-32 | Multi-tenant data isolation | ✅ | ✅ | All tRPC procedures scope by `companyId` |
| FK-33 | Token-based user invitation | ✅ | ✅ | `invitation.createInvitation` + `acceptInvitation` |
| FK-34 | User roles within a company (owner / admin / member) | ✅ | ✅ | `Membership.role` enum |

### Dashboard and Overview

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| FK-35 | Dashboard with key operational metrics | ✅ | ✅ | `/dashboard` route |
| FK-36 | All-assignments list view with filtering | ✅ | ✅ | `/oppdrag` route with filter panel |
| FK-37 | Utilisation charts for drivers and vehicles | ✅ | ✅ | Chart components on dashboard |

### Out of Scope (Won't — this version)

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| FK-38 | Driver-facing schedule page | ❌ | N/A | Out of scope (interview-requested, future work §6.3) |
| FK-39 | Billing/invoicing integration | ❌ | N/A | Out of scope (future work §6.3 / adoption barrier §5.2) |
| FK-40 | Push notifications to drivers | ❌ | N/A | Out of scope |
| FK-41 | Admin panel for users/permissions | ❌ | N/A | Out of scope |
| FK-42 | GPS tracking and real-time location | ❌ | N/A | Out of scope |

---

## Non-Functional Requirements

| ID | Requirement (short) | Implemented | Tested | Codebase reference |
|----|---------------------|:-----------:|:------:|---------------------|
| IFK-01 | Plan generation < 3s (greedy, 100 assignments) | ✅ | ✅ | Verified against small benchmark dataset |
| IFK-02 | Plan generation < 60s (OR-Tools, 500 assignments) | ✅ | ⚠️ | Time limit configured; large-dataset benchmark not fully run |
| IFK-08 | Session-based authentication | ✅ | ✅ | Better Auth; session stored in PostgreSQL |
| IFK-09 | Cross-tenant data isolation | ✅ | ✅ | All tRPC procedures enforce `companyId` scope |
| IFK-10 | Input validation (Zod) | ✅ | ✅ | All tRPC inputs validated with Zod schemas |
| IFK-11 | SQL injection prevention (Prisma) | ✅ | ✅ | Prisma parameterised queries throughout |
| IFK-15 | End-to-end type safety | ✅ | ✅ | tRPC + TypeScript; type errors caught at compile time |

---

## Coverage summary

- **Functional requirements (FK-01 to FK-37):** 37 in-scope requirements; 36 fully implemented and verified, 1 partial (FK-30 driving/rest-time status — no real-time tachograph counter).
- **Out-of-scope (FK-38 to FK-42):** 5 explicitly Won't requirements; documented as future work in §6.3.
- **Non-functional requirements (IFK-01 to IFK-15):** 7 documented; 6 fully verified, 1 partial (IFK-02 large-dataset benchmark).

"Tested" reflects developer-verified functioning, not formal automated test coverage. The absence of an automated test suite is named as **L9** in §5.4 (algorithm evaluation against own benchmarks only) and as a non-functional gap noted in §3.7 system validity.