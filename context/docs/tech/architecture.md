# System Architecture — Ressursplanlegger

> **Owner: Embret** — filled based on actual codebase.
> Used when writing Chapter 4.4 (System Description).

---

## Architectural Style

Ressursplanlegger is a **full-stack monorepo** built on Next.js. There is no separate backend service for standard CRUD operations — the Next.js API routes (via tRPC) serve both as the HTTP server and the business logic layer. The optimisation engines are the only external processes, spawned as subprocesses on demand.

```
┌────────────────────────────────────────────────────────┐
│                    Browser (React 19)                  │
│   Next.js App Router — Client Components + RSC         │
│   TanStack Query ← tRPC client → tRPC HTTP endpoint    │
└──────────────────────┬─────────────────────────────────┘
                       │ HTTPS / tRPC-over-HTTP
┌──────────────────────▼─────────────────────────────────┐
│              Next.js Server (Node.js)                  │
│   tRPC Router — procedures scoped to authenticated     │
│   company context (ctx.session.user → companyId)       │
│   Better Auth — session management                     │
│   Prisma Client → PostgreSQL                           │
└─────────┬──────────────────────┬───────────────────────┘
          │ Prisma / pg           │ subprocess (JSON stdin/stdout)
┌─────────▼──────┐    ┌──────────▼────────────────────────┐
│  PostgreSQL    │    │     Optimisation Engines           │
│  (Docker /     │    │  greedy/solver.py   (Python)       │
│   cloud)       │    │  ortools_engine/solver.py (Python) │
└────────────────┘    │  timefold/solver.jar (Java)        │
                      └────────────────────────────────────┘
```

---

## Layer Breakdown

### Frontend (`src/app/`)

Organised using the Next.js App Router with route groups:

| Route group | Path prefix | Purpose |
|-------------|-------------|---------|
| `(auth)` | `/login`, `/register`, `/accept-invitation` | Unauthenticated pages |
| `(dashboard)` | `/ressursplanlegger`, `/oversikt`, … | Protected planning pages |

Key page routes:
- `/ressursplanlegger` — main planning timeline (Gantt-style)
- `/oversikt` — dashboard overview with utilisation charts
- `/alle-oppdrag` — list view of all assignments
- `/ansatte/[id]` — employee profile and schedule management
- `/kjoretoy/[id]` — vehicle profile and status management
- `/avvik` — deviation/conflict viewer
- `/optimalisering-historikk` — optimisation run history
- `/innstillinger` — user and company settings

State management: TanStack Query (server state); React state (local UI state). No global client store (Redux / Zustand) is used.

### Backend (`src/server/`)

The backend is contained within the Next.js server process. The entry point for the API is a single catch-all route handler at `/api/trpc/[...all]`.

```
src/server/
├── api/
│   ├── root.ts           ← Merges all routers into a single tRPC app router
│   ├── trpc.ts           ← Context builder, middleware, procedure factories
│   └── routers/
│       ├── optimization.ts   ← Runs engines, stores solutions
│       ├── assignment.ts     ← CRUD for assignments; manual assignment
│       ├── employee.ts       ← CRUD for employees, competencies, schedules, time-off
│       ├── vehicle.ts        ← CRUD for vehicles, trailers, competencies
│       ├── deviation.ts      ← Conflict detection and querying
│       ├── company.ts        ← Multi-tenant company management
│       ├── invitation.ts     ← Invite tokens
│       └── settings.ts       ← User preferences
├── db.ts                 ← Prisma client singleton
└── auth.ts               ← Better Auth configuration
```

Every tRPC procedure receives a typed context (`ctx`) that includes the authenticated session and a Prisma client scoped to the user's `companyId`. This enforces multi-tenant data isolation at the procedure level.

### Database (`prisma/`)

PostgreSQL accessed via Prisma ORM. The schema is defined in `prisma/schema.prisma`. Migrations are managed with `prisma migrate`.

Key schema groups:
- **Auth tables:** `User`, `Session`, `Account`, `Verification` (managed by Better Auth)
- **Organisation:** `Company`, `UserSettings`
- **Resources:** `Employee`, `Vehicle`, `Trailer`, `Competence`
- **Planning:** `Assignment`, `Team`, `TimeEntry`
- **Availability:** `WorkSchedule`, `TimeOff`, `Certification`

All resource tables carry a `companyId` foreign key with `onDelete: Cascade` for multi-tenant isolation.

### Optimisation Engines (`engines/`)

```
engines/
├── greedy/
│   └── solver.py             ← Greedy priority-sorted assignment
├── ortools_engine/
│   ├── solver.py             ← Google CP-SAT constraint model
│   └── constraints_loader.py ← JSON-based constraint configuration
└── timefold/
    └── solver.jar            ← Compiled Java Timefold solver
```

The orchestration layer in `src/optimization/client.ts` handles subprocess spawning, JSON I/O, and engine registration. `src/optimization/scorer.ts` evaluates returned solutions.

---

## Data Flow: Optimisation Request

```
1. Coordinator clicks "Generate plan" for a date
2. Frontend sends tRPC mutation: optimization.runOptimization({ date, engine })
3. Server fetches all assignments, employees, vehicles, constraints from PostgreSQL
4. Server serialises the problem as JSON
5. Server spawns the selected engine subprocess and writes JSON to stdin
6. Engine solves, writes JSON solution to stdout
7. Server reads stdout, parses solution
8. Server scores the solution (scorer.ts)
9. Server saves solution to database
10. Server returns solution to frontend via tRPC response
11. Frontend updates the planning timeline via TanStack Query cache invalidation
```

---

## Multi-Tenancy

Data isolation is enforced at two levels:
1. **Database level:** Every entity has a `companyId` FK; queries are always filtered by `companyId`.
2. **Procedure level:** The tRPC context resolves the authenticated user's `companyId` before any procedure runs; procedures cannot query outside their company.

---

## Authentication Flow

1. User visits `/login`
2. Better Auth validates credentials and creates a session record in PostgreSQL
3. A session cookie is set in the browser
4. Every tRPC request carries the session cookie
5. The tRPC context builder (`trpc.ts`) reads the session and resolves `companyId`
6. Protected procedures throw `UNAUTHORIZED` if no valid session exists

---

## Deployment

| Component | Environment | Notes |
|-----------|-------------|-------|
| Next.js app | Vercel | Serverless functions for tRPC routes |
| PostgreSQL | Docker (local dev) / cloud provider (prod) | Started with `start-database.sh` locally |
| Optimisation engines | Co-located with Node.js process | Spawned as subprocesses; must be present on the server |
| Static assets | Vercel CDN | `public/` directory |
