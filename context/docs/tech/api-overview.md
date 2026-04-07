# API Overview — Ressursplanlegger

> **Owner: Embret** — filled based on actual tRPC router implementation.
> Note: The API is tRPC (not REST). All calls go through a single HTTP endpoint.

---

## Transport Layer

**Protocol:** tRPC over HTTP
**Base endpoint:** `/api/trpc/[procedureName]`
**Dev base URL:** `http://localhost:3000`
**Authentication:** Session cookie (Better Auth). The session is read server-side in the tRPC context; no Bearer token is passed manually.

> tRPC procedures are type-safe RPC calls, not REST endpoints. They are called from the frontend via the tRPC client using `api.routerName.procedureName.useQuery()` / `.useMutation()`. The wire format is JSON over HTTP POST (mutations) or HTTP GET (queries).

---

## Procedures by Router

### assignment router

| Procedure | Type | Description |
|-----------|------|-------------|
| `assignment.getAll` | Query | All assignments for the authenticated company (optional filters: date range, status) |
| `assignment.getById` | Query | Single assignment with employee, vehicle, competence details |
| `assignment.create` | Mutation | Create a new assignment |
| `assignment.update` | Mutation | Update assignment fields |
| `assignment.delete` | Mutation | Delete an assignment |
| `assignment.assignEmployeeToAssignment` | Mutation | Manually assign an employee to an assignment |
| `assignment.assignVehicleToAssignment` | Mutation | Manually assign a vehicle to an assignment |
| `assignment.getConflicts` | Query | Deviations/violations for a specific assignment |

**Key input shapes:**
- `getAll`: `{ startDate?, endDate?, status? }`
- `create`: `{ customer, project, startDate, endDate, startTime?, endTime?, priority, requiredVehicleType?, companyId }`
- `assignEmployeeToAssignment`: `{ assignmentId, employeeId }`

---

### employee router

| Procedure | Type | Description |
|-----------|------|-------------|
| `employee.getAll` | Query | All employees with competencies, work schedules, time-off |
| `employee.getById` | Query | Single employee detail |
| `employee.create` | Mutation | Add an employee |
| `employee.update` | Mutation | Update employee fields |
| `employee.addCompetence` | Mutation | Assign a competency to an employee |
| `employee.addCertification` | Mutation | Add a licence/certification with expiry date |
| `employee.addWorkSchedule` | Mutation | Define working hours for a weekday |
| `employee.addTimeOff` | Mutation | Register vacation or sick leave |

---

### vehicle router

| Procedure | Type | Description |
|-----------|------|-------------|
| `vehicle.getAll` | Query | All vehicles with competencies and status |
| `vehicle.getById` | Query | Single vehicle detail |
| `vehicle.create` | Mutation | Add a vehicle |
| `vehicle.update` | Mutation | Update vehicle fields |
| `vehicle.setStatus` | Mutation | Change status: active / maintenance / out_of_service |
| `vehicle.addCompetence` | Mutation | Mark that a vehicle requires a competency |
| `vehicle.addTrailer` | Mutation | Attach a trailer to a vehicle |

---

### optimization router

| Procedure | Type | Description |
|-----------|------|-------------|
| `optimization.runOptimization` | Mutation | Run a solver (greedy / ortools / timefold) for a given date |
| `optimization.getSolution` | Query | Fetch a saved optimisation solution |
| `optimization.compare` | Mutation | Compare two optimisation solutions |
| `optimization.benchmark` | Mutation | Run benchmark datasets against all engines |

**Key input:**
- `runOptimization`: `{ date: string, engine: "greedy" | "ortools" | "timefold" }`

**Key output:**
- `runOptimization`: `{ solution: Assignment[], score: { total, hardScore, softScore, breakdown } }`

---

### deviation router

| Procedure | Type | Description |
|-----------|------|-------------|
| `deviation.getConflicts` | Query | All active constraint violations for the company |
| `deviation.detectConflicts` | Query | Re-run conflict detection and return violations |

**Violation types returned:** `incomplete`, `overbooking`, `overtime`, `missing_competence`, `night_work`, `certification_expired`, `vehicle_maintenance`, `rest_period_violation`

---

### company router

| Procedure | Type | Description |
|-----------|------|-------------|
| `company.getCompany` | Query | Current user's company details |
| `company.create` | Mutation | Create a new company |
| `company.update` | Mutation | Update company settings |
| `company.addMember` | Mutation | Add a user to the company |

---

### settings router

| Procedure | Type | Description |
|-----------|------|-------------|
| `settings.getSettings` | Query | Current user preferences (language, timezone, notifications) |
| `settings.updateSettings` | Mutation | Update user preferences |

---

### invitation router

| Procedure | Type | Description |
|-----------|------|-------------|
| `invitation.createInvitation` | Mutation | Generate an invitation token |
| `invitation.acceptInvitation` | Mutation | Accept an invitation and join a company |

---

## Authentication Endpoints

Managed by Better Auth at `/api/auth/[...all]` (not tRPC):
- `POST /api/auth/sign-in` — login
- `POST /api/auth/sign-up` — registration
- `POST /api/auth/sign-out` — logout
- `GET /api/auth/session` — current session

---

## Error Format

tRPC errors use the TRPCError structure:
```json
{
  "error": {
    "message": "string",
    "code": "UNAUTHORIZED | NOT_FOUND | BAD_REQUEST | INTERNAL_SERVER_ERROR",
    "data": { "httpStatus": 401 }
  }
}
```
