# API Overview — Cephalo

> **Owner: Embret** — fill in all endpoints.

---

## Base URL
`[FILL IN — e.g. http://localhost:3000/api or https://api.cephalo.no/v1]`

## Authentication
`[FILL IN — e.g. JWT Bearer token in Authorization header]`

---

## Endpoints

### Assignments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/assignments` | Get all assignments for a date range |
| POST | `/assignments` | Create a new assignment |
| PATCH | `/assignments/:id` | Update an assignment |
| POST | `/assignments/:id/assign` | Manually assign driver + vehicle |

#### GET /assignments
**Query params:** `date`, `status`
**Response:** `[{ id, title, from, to, scheduledStart, scheduledEnd, status, driverId, vehicleId }]`

### Plan / Optimisation

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/plan/generate` | Run optimisation algorithm |
| GET | `/plan/:date` | Get current plan for a date |
| POST | `/plan/:date/approve` | Approve the generated plan |

#### POST /plan/generate
**Body:** `{ date, departmentId }`
**Response:** `{ plan: [...assignments with suggested driver/vehicle] }`

### Drivers

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/drivers` | List all drivers |
| GET | `/drivers/:id` | Get driver with competences and availability |
| [FILL IN] | | |

### Vehicles

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/vehicles` | List all vehicles |
| [FILL IN] | | |

---

## Error Format
```json
{
  "error": "string",
  "code": "ERROR_CODE",
  "details": {}
}
```
