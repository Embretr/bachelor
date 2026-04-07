# Requirements Traceability — Ressursplanlegger

> **Owner: Embret** — filled based on implemented features visible in the codebase.
> Used in Chapter 4 (Findings) when describing the built system.
> "Tested" here means verified to function during development; no formal test suite exists.

## Functional Requirements

| ID | Requirement (short) | Implemented | Tested | Notes |
|----|---------------------|:-----------:|:------:|-------|
| FK-01 | Display assignments for selected day on planning timeline | ✅ | ✅ | `/ressursplanlegger` — Gantt-style timeline with date selector |
| FK-02 | Manual driver/vehicle assignment | ✅ | ✅ | `assignment.assignEmployeeToAssignment` + `assignVehicleToAssignment` tRPC mutations |
| FK-03 | Algorithm-generated plan (greedy) | ✅ | ✅ | `optimization.runOptimization` with `engine: "greedy"` |
| FK-04 | Algorithm-generated plan (OR-Tools CP-SAT) | ✅ | ✅ | `optimization.runOptimization` with `engine: "ortools"` |
| FK-05 | Algorithm-generated plan (Timefold) | ✅ | ⬜ | `optimization.runOptimization` with `engine: "timefold"` — implemented but not fully benchmarked |
| FK-06 | Override algorithm assignment manually | ✅ | ✅ | Coordinator selects employee/vehicle in assignment detail panel |
| FK-07 | Rest/working-time constraint detection | ✅ | ✅ | Deviation types: `overtime`, `rest_period_violation`, `night_work` |
| FK-08 | Sick-leave registration | ✅ | ✅ | `employee.addTimeOff` mutation; `type: sick_leave` |
| FK-09 | Conflict detection after sick-leave | ✅ | ✅ | Affected assignments gain violation flag; shown in `/avvik` |
| FK-10 | Driver availability view | ✅ | ✅ | Employee profile page shows work schedule, time-off, and certifications |
| FK-11 | Store licence classes / competencies | ✅ | ✅ | `Competence` model; `employee.addCompetence` and `employee.addCertification` |
| FK-12 | Competency matching in algorithm | ✅ | ✅ | HC-01 in all three solvers |
| FK-13 | Vehicle status management | ✅ | ✅ | `vehicle.setStatus` — active / maintenance / out_of_service |
| FK-14 | Vehicle competency requirements | ✅ | ✅ | `VehicleCompetence` M2M; matched in algorithm |
| FK-15 | Conflict/deviation viewer | ✅ | ✅ | `/avvik` — lists all active violations with type, description, and affected assignment |
| FK-16 | Multi-tenant company isolation | ✅ | ✅ | All queries scoped by `companyId` in tRPC context |
| FK-17 | Team (fixed crew) assignment | ✅ | ⬜ | `Team` model + `Assignment.teamId`; UI exists but limited testing |
| FK-18 | Optimisation history and comparison | ✅ | ✅ | `/optimalisering-historikk`; `optimization.compare` |
| FK-19 | Recurring assignments | ✅ | ⬜ | `Assignment.isRecurring` + `recurringPattern`; implemented in schema and CRUD |
| FK-20 | Invitation system | ✅ | ✅ | `invitation.createInvitation` + `acceptInvitation` |

## Non-Functional Requirements

| ID | Requirement (short) | Implemented | Tested | Notes |
|----|---------------------|:-----------:|:------:|-------|
| IFK-01 | Plan generation < 3s (greedy, 100 assignments) | ✅ | ✅ | Verified against small benchmark dataset |
| IFK-02 | Plan generation < 60s (OR-Tools, 500 assignments) | ✅ | ⬜ | Time limit configured; large-dataset benchmark not fully run |
| IFK-08 | Session-based authentication | ✅ | ✅ | Better Auth; session stored in PostgreSQL |
| IFK-09 | Cross-tenant data isolation | ✅ | ✅ | All tRPC procedures enforce `companyId` scope |
| IFK-10 | Input validation (Zod) | ✅ | ✅ | All tRPC inputs validated with Zod schemas |
| IFK-11 | SQL injection prevention (Prisma) | ✅ | ✅ | Prisma parameterised queries throughout |
| IFK-15 | End-to-end type safety | ✅ | ✅ | tRPC + TypeScript; type errors caught at compile time |
