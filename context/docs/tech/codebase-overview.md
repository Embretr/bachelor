# Codebase Overview — Ressursplanlegger

> Summary of the existing codebase for Claude to understand what has been built.
> Used when writing Chapter 4.4 (System Description) and for code-related tasks.
> Owner: Embret — fill this before Chapter 4 is written.
> Do not paste full source code — paste structure, key files, and what they do.

---

## Repository Structure

Monorepo — frontend, backend, and algorithm engines in one repository.

```
ressursplanlegger-ntnu/
├── src/                        ← All TypeScript source code
│   ├── app/                    ← Next.js App Router pages and layouts
│   │   ├── (auth)/             ← Login, register, accept-invitation
│   │   └── (dashboard)/        ← Protected planning pages
│   │       ├── ressursplanlegger/   ← Main planning timeline
│   │       ├── oversikt/            ← Dashboard overview
│   │       ├── alle-oppdrag/        ← Assignment list view
│   │       ├── ansatte/[id]/        ← Employee profile
│   │       ├── kjoretoy/[id]/       ← Vehicle profile
│   │       ├── avvik/               ← Deviation/conflict viewer
│   │       ├── optimalisering-historikk/  ← Optimisation history
│   │       └── innstillinger/       ← Settings
│   ├── server/                 ← tRPC backend
│   │   ├── api/
│   │   │   ├── root.ts         ← Merges all routers
│   │   │   ├── trpc.ts         ← Context, middleware, procedure builders
│   │   │   └── routers/        ← One file per domain (assignment, employee, vehicle, …)
│   │   ├── db.ts               ← Prisma client singleton
│   │   └── auth.ts             ← Better Auth configuration
│   ├── components/             ← Shared React components (shadcn/ui + custom)
│   ├── optimization/           ← Engine orchestration layer
│   │   ├── client.ts           ← Subprocess spawning, engine registry
│   │   ├── types.ts            ← Problem/solution TypeScript interfaces
│   │   └── scorer.ts           ← Solution scoring
│   └── lib/                    ← Utility functions
├── engines/                    ← Optimisation algorithm engines
│   ├── greedy/
│   │   └── solver.py           ← Python greedy solver
│   ├── ortools_engine/
│   │   ├── solver.py           ← Google OR-Tools CP-SAT solver
│   │   └── constraints_loader.py
│   └── timefold/
│       └── solver.jar          ← Compiled Java Timefold solver
├── prisma/
│   ├── schema.prisma           ← Database schema (source of truth)
│   └── migrations/             ← PostgreSQL migrations
├── benchmarks/                 ← small.json, medium.json, large.json
├── public/                     ← Static assets
├── package.json
├── tsconfig.json
└── start-database.sh           ← Starts PostgreSQL in Docker (local dev)
```

---

## Frontend

**Framework:** Next.js 15 (App Router) with React 19
**Language:** TypeScript
**State management:** TanStack Query for server state; React `useState`/`useReducer` for local UI state. No global client store.
**Styling:** Tailwind CSS v4 + shadcn/ui (Radix UI primitives)

**Key components:**

| Component | What it does |
|-----------|-------------|
| Planning timeline | Gantt-style view of assignments per employee for a selected date; supports drag-and-drop reassignment (`react-dnd`) |
| Assignment card | Coloured block on the timeline; shows customer, project, time, and status; clickable for detail |
| Assignment detail panel | Form for viewing and editing an assignment; includes employee/vehicle dropdowns filtered by competency and availability |
| Utilisation chart | Recharts bar/line chart showing employee and vehicle utilisation percentages |
| Deviation badge | Inline warning on the timeline for constraint violations (overbooking, missing competence, etc.) |
| Employee profile page | Shows employee details, work schedule, time-off, certifications, and assignment history |
| Vehicle profile page | Shows vehicle details, status, upcoming inspections, and trailer attachments |

**Main screens:**
- `/ressursplanlegger` — Planning timeline: Gantt-style view with all employees on the vertical axis and time on the horizontal axis. Unassigned assignments appear in a sidebar. Includes "Generate plan" and "Approve plan" buttons.
- `/oversikt` — Dashboard with utilisation charts and a summary of the day's assignments.
- `/alle-oppdrag` — Table view of all assignments with filtering by date, status, and priority.
- `/ansatte/[id]` — Employee profile: work schedule, time-off registration, certifications, competencies.
- `/kjoretoy/[id]` — Vehicle profile: status management, upcoming service dates, trailer management.
- `/avvik` — Active constraint violations with details (type, affected assignment, suggested resolution).
- `/optimalisering-historikk` — History of past optimisation runs with scores and comparison.
- `/innstillinger` — User preferences (language, timezone) and company settings.

---

## Backend

**Framework:** Next.js API routes (serverless functions) + tRPC
**Structure:** tRPC routers (one per domain) → Prisma client → PostgreSQL
**Authentication:** Better Auth (session cookies; sessions stored in PostgreSQL)

**Key files / modules:**

| File / Module | What it does |
|--------------|-------------|
| `src/server/api/trpc.ts` | Creates the tRPC context (resolves session + companyId), defines middleware and procedure builders |
| `src/server/api/root.ts` | Merges all domain routers into the single app router |
| `src/server/api/routers/optimization.ts` | Fetches problem data, spawns algorithm subprocesses, scores and stores solutions |
| `src/server/api/routers/assignment.ts` | Full CRUD for assignments; manual employee/vehicle assignment |
| `src/server/api/routers/employee.ts` | Employee CRUD; work schedule, time-off, certification management |
| `src/server/api/routers/vehicle.ts` | Vehicle CRUD; status, trailer, competency management |
| `src/server/api/routers/deviation.ts` | Runs conflict detection; returns violation records |
| `src/server/db.ts` | Prisma client singleton (shared across all requests) |
| `src/optimization/client.ts` | Engine registry; spawns Python/Java subprocesses; passes JSON via stdin/stdout |
| `src/optimization/scorer.ts` | Evaluates a solution: hard/soft score, workload balance, priority coverage |

---

## Database

**Type:** PostgreSQL
**Hosting:** Docker container locally (`start-database.sh`); cloud PostgreSQL in production
**ORM / query layer:** Prisma 7 (schema-first; type-safe client generated from `prisma/schema.prisma`)

Key tables:
- `Assignment` — the jobs to be planned
- `Employee` — drivers and other staff
- `Vehicle` — trucks, vans, cranes
- `Competence` — named competencies/licence classes (company-scoped)
- `WorkSchedule` — per-employee, per-weekday working hours
- `TimeOff` — vacation and sick-leave periods
- `Certification` — employee licence/certification records with expiry dates
- `Team` — fixed crew configurations
- `TimeEntry` — actual hours logged against assignments
- `Company` — tenant root; all other entities are FK-linked
- `User`, `Session`, `Account` — Better Auth managed

---

## Algorithm

**Location:** `engines/` directory — separate Python and Java scripts, not part of the Node.js process.
**Language/runtime:** Python 3 (greedy, OR-Tools); Java (Timefold)
**Key dependencies:** `ortools` (Python), `timefold-solver` (Java, packaged as `.jar`)

How it is triggered:
1. Coordinator clicks "Generate plan" for a date and selects an engine
2. Frontend calls `optimization.runOptimization({ date, engine })` via tRPC
3. Server fetches all assignments, employees, vehicles, constraints from PostgreSQL
4. Server serialises the problem as JSON
5. `src/optimization/client.ts` spawns the engine as a subprocess (`python solver.py` or `java -jar solver.jar`)
6. Problem JSON is written to subprocess stdin; solution JSON is read from stdout
7. Solution is scored by `src/optimization/scorer.ts` and returned to the frontend

---

## External Dependencies

| Library / Service | Why it is used |
|-------------------|---------------|
| Google OR-Tools (Python) | CP-SAT constraint solver for near-optimal daily planning |
| Timefold Solver (Java) | Metaheuristic solver for large-scale / multi-day planning |
| Better Auth | Session management and authentication (Prisma adapter) |
| Vercel | Deployment platform for the Next.js app |
| Docker | Local PostgreSQL database container |

---

## What Is Implemented vs. Planned

| Feature | Status |
|---------|--------|
| Planning timeline (Gantt view) | ✅ Implemented |
| Manual assignment (employee + vehicle) | ✅ Implemented |
| Algorithm-generated plan (greedy, OR-Tools, Timefold) | ✅ Implemented |
| Sick-leave registration and affected assignment detection | ✅ Implemented |
| Employee profiles (schedule, time-off, certifications, competencies) | ✅ Implemented |
| Vehicle profiles (status, service dates, trailers, competencies) | ✅ Implemented |
| Conflict/deviation detection (8 violation types) | ✅ Implemented |
| Multi-tenant company isolation | ✅ Implemented |
| Invitation system | ✅ Implemented |
| User settings (language, timezone) | ✅ Implemented |
| Optimisation history and solution comparison | ✅ Implemented |
| Algorithm benchmarking | ✅ Implemented |
| Driver mobile app | ⬜ Out of scope |
| GPS tracking | ⬜ Out of scope |
| Integration with Timpex / Opter | ⬜ Out of scope |
| Billing / invoicing | ⬜ Out of scope |
