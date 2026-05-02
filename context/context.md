# Master Context — Ressursplanlegger

> **This is the most important single document in the repository.**
> Both authors and Claude read it at the start of every session.
> Keep it accurate and up to date — if something changes, update this file first.

---

## Identification

| Field | Value |
|---|---|
| **Title** | Ressursplanlegger |
| **Subtitle** | Algorithm-Assisted Resource Planning for Transport Companies |
| **Institution** | NTNU Gløshaugen — Department of Computer Science (IDI) |
| **Program** | Data Engineering (Dataingeniør) |
| **Author 1** | Embret Olav Rasmussen Roås — primary responsibility: system development |
| **Author 2** | Mikael Stray — primary responsibility: user research |
| **Supervisor** | Ali Alsam |
| **Submission deadline** | 20 May 2026, 14:00 |
| **Language** | English |
| **Citation style** | APA 7 |

---

## What is Ressursplanlegger?

Ressursplanlegger is a web-based resource planning platform developed for traffic coordinators in Norwegian transport companies. It automatically generates optimised daily plans that assign drivers and vehicles to assignments, which the coordinator can review, manually adjust, and approve.

---

## The Problem

Norwegian transport companies operate without systematic visibility into resource utilization. Overtime is handled reactively, idle time between assignments is invisible, and load balancing across drivers depends on traffic coordinators' memory and intuition rather than any structured overview.

Demand for algorithm-assisted planning thus comes primarily from owners and the business side, not from the coordinators who must operate any such system. This stakeholder asymmetry mirrors Bainbridge's (1983) *ironies of automation*: those whose work depends on a system are rarely the ones who articulate the need for its automation. The same configuration appears across the seven Norwegian transport companies interviewed for this thesis.

Tacit knowledge dependency and slow legacy software are downstream consequences of the visibility gap, not its origin. Traffic coordinators rely on information held in their heads — who has the right licence, who is experienced on which routes, who is approaching overtime limits, which vehicle fits the job — because no system surfaces this information in a structured, comparable form. The two commercial TMS named in the interview pool, Timpex and Opter, handle order management and invoicing but offer no planning or decision support; neither generates assignment plans automatically. Timpex is described by users as extremely slow under concurrent use. Other interviewed companies use internal or custom tools.

This creates several downstream problems:

- **Inefficiency:** Every assignment is a manual decision repeated dozens of times per day.
- **Key-person dependency:** If the coordinator is absent, their knowledge is lost — no one else can plan effectively.
- **No capacity overview:** There is no unified view of driver availability, vehicle status, and assignment load.
- **Error risk:** Manual processes increase the chance of double-booking, overtime violations, and missed competency requirements.

Ressursplanlegger addresses these problems by making resource utilization visible to both coordinator and owner, formalising coordinator knowledge as structured data (competencies, certifications, schedules), and using constraint-aware algorithms to generate assignment plans that the coordinator can inspect, modify, accept, or reject.

---

## Research Question

> How can an algorithm-assisted resource planning platform improve resource utilization in Norwegian transport companies (reducing overtime, idle time between assignments, and uneven driver load) while remaining accountable to the traffic coordinator who operates it?

Sub-questions (each designed to be quotable verbatim as a single-line block quote in Chapter 6, answerable in one paragraph traceable to a specific Discussion anchor sub-section, and bounded by named limitations from §5.4):

1. **SQ1** — *How is resource-utilization visibility distributed across operator and owner stakeholders in current Norwegian transport-company planning practice?*
2. **SQ2** — *How can an algorithm-assisted planning system be designed so that automated optimisation improves resource utilization while remaining operable and overridable by the traffic coordinator?*
3. **SQ3** — *To what extent and under what limitations does Ressursplanlegger demonstrate measurable improvement in resource utilization?*

The thesis argument turns on three locked **anchor concepts** — **Effektivitet**, **Tillit/kontroll**, **Tilpasningsdyktighet** — defined in `context/thesis-spine.md` and `context/glossary.md`. Anchor names are Norwegian compound terms used as proper nouns in English prose; never translated, never split. The theoretical anchor for the human-in-the-loop stance is Bainbridge (1983), *Ironies of Automation*: demand for automation is articulated by owners, not by the operators who must run the system.

---

## Target Users

The thesis distinguishes between *primary operator* (the user who must run the system to do their job) and *primary demand-side stakeholder* (the party that articulates the need for the system in the first place). This distinction structures both the design — the operator must retain authority — and the discussion's framing of stakeholder asymmetry.

| Role | Stakeholder position | Description | System access |
|---|---|---|---|
| **Traffic coordinator (trafikkleder)** | **Primary operator** | Primary daily user. Plans daily assignments, handles sick-leave replacements, manages driver/vehicle allocation. Uses the system multiple times per day. Must retain authority over individual assignment decisions (Tillit/kontroll). | Full access to planning interface, algorithm, manual override |
| **Transport manager / company owner** | **Primary demand-side stakeholder** | Articulates the resource-utilization optimization need. Reviews utilisation statistics, approves plans, monitors deviations. Uses the system weekly or at key decision points. | Dashboard, reports, oversight views |
| **Admin** | Operational support | Manages company settings, users, and invitations. | Settings, user management (admin panel not yet built) |
| **Driver (sjåfør)** | Subject of plan | Receives assignments. Planned to have a dedicated page showing their schedule and assigned tasks. | Own page — planned, not yet implemented |
| **Admmit AS** | **Stakeholder firm (the firm this thesis is written for)** | Articulates the original Human-in-the-Loop mandate and the multi-tenant architecture requirement. Customer firms participating in interviews are Admmit's customers; contact was initiated by the team on its own initiative. | Not a system user; product owner |

Anyone with responsibility for assignments, drivers, or the allocation process should have access to the system. Drivers will have a separate, read-only view of their own schedule.

---

## Technology Stack

Verified against the actual codebase at the Ressursplanlegger repository.

| Layer | Technology | Version |
|---|---|---|
| Frontend framework | Next.js (App Router) + React | 15 / React 19 |
| Language | TypeScript | 5.8 |
| UI components | shadcn/ui + Radix UI | — |
| Styling | Tailwind CSS | v4 |
| API layer | tRPC | 11 |
| Server state | TanStack Query (React Query) | v5 |
| Authentication | Better Auth | 1.3 |
| Database | PostgreSQL | — |
| ORM | Prisma | 7 |
| Algorithm — greedy baseline | Python (custom, no dependencies) | 3.x |
| Algorithm — constraint solver | Google OR-Tools CP-SAT (Python) | latest |
| Algorithm — advanced solver | Timefold Solver (Java) | 1.31.0 |
| Drag & drop | react-dnd | — |
| Charts | Recharts | — |
| Validation | Zod | — |
| Package manager | pnpm | 10.14 |
| Hosting | Railway (app + database) | — |

---

## Architecture Overview

Ressursplanlegger is a **full-stack monorepo** built on Next.js. There is no separate backend service for standard operations — the Next.js API routes (via tRPC) serve as both the HTTP server and business logic layer.

```
┌────────────────────────────────────────────────────────┐
│                    Browser (React 19)                   │
│   Next.js App Router — Client Components + RSC          │
│   TanStack Query ← tRPC client → tRPC HTTP endpoint    │
└──────────────────────┬─────────────────────────────────┘
                       │ HTTPS / tRPC-over-HTTP
┌──────────────────────▼─────────────────────────────────┐
│              Next.js Server (Node.js)                   │
│   tRPC Router — procedures scoped to authenticated      │
│   company context (ctx.session.user → companyId)        │
│   Better Auth — session management                      │
│   Prisma Client → PostgreSQL                            │
└─────────┬──────────────────────┬───────────────────────┘
          │ Prisma / pg           │ subprocess (JSON stdin/stdout)
┌─────────▼──────┐    ┌──────────▼────────────────────────┐
│  PostgreSQL    │    │     Optimisation Engines            │
│  (Railway)     │    │  greedy/solver.py   (Python)        │
│                │    │  ortools_engine/solver.py (Python)  │
│                │    │  timefold/solver.jar (Java)         │
└────────────────┘    └────────────────────────────────────┘
```

**Key architectural decisions:**

- **Type safety end-to-end:** TypeScript on both client and server, tRPC eliminates manual type synchronisation, Prisma generates typed database queries.
- **Engines as subprocesses:** Optimisation algorithms run as separate processes invoked by the Node.js server. The problem is serialised to JSON, passed via stdin, and the solution is read from stdout. This keeps algorithm code independent of the TypeScript runtime and allows solvers written in Python and Java.
- **Multi-tenancy:** Every entity carries a `companyId` foreign key. All tRPC procedures resolve the authenticated user's company before querying. Data isolation is enforced at both the procedure level and the database level.
- **Pluggable solver architecture:** A registry-based engine system allows selecting between solvers at runtime. The greedy solver provides instant feedback; OR-Tools provides near-optimal solutions; Timefold handles large-scale instances.

---

## What Makes Ressursplanlegger Unique

Compared to existing systems used by the interviewed companies (Timpex, Opter, internal/custom tools, manual processes):

| Capability | Existing systems | Ressursplanlegger |
|---|---|---|
| **Assignment optimisation** | None — all manual | Automatic plan generation via constraint-aware algorithms |
| **Constraint handling** | Coordinator remembers constraints | Hard constraints (licence, availability, vehicle type) enforced by algorithm; soft constraints (workload balance, preferences) weighted and optimised |
| **Constraint configurability** | N/A | User can adjust the weight of each soft constraint to control what the algorithm prioritises |
| **Capacity overview** | Fragmented or non-existent | Unified timeline showing all assignments, drivers, and vehicles with utilisation metrics |
| **Decision support** | None | Algorithm suggests a complete plan; coordinator reviews and corrects — "suggest + override" pattern |
| **Speed** | Timpex described as "extremely slow" | Modern web stack, responsive UI, instant greedy solver for real-time feedback |
| **Tacit knowledge** | Lives in the coordinator's head | Formalised as structured data: competencies, certifications, experience, schedules |
| **Conflict detection** | Manual checking | Automated detection of double-booking, overtime, missing competence, expired certifications, rest period violations |

The core differentiator is that Ressursplanlegger is the first system in this context that **automatically generates a plan** rather than simply being a container for manually entered assignments. The coordinator remains in control — the algorithm proposes, the human decides.

---

## Project Status

### Built and functional

- **Authentication:** Email/password login and registration via Better Auth. Session-based with cookies. Company invitation system with token-based access.
- **Employee management:** Full CRUD. Competencies, certifications with expiry tracking, weekly work schedules, time-off (vacation, sick leave). Utilisation metrics.
- **Vehicle management:** Full CRUD. Vehicle types, capacity, maintenance dates, EU control dates, trailers. Status tracking (active, maintenance, out of service).
- **Assignment management:** Full CRUD. Recurring assignments (daily/weekly/biweekly/monthly). Priority levels. Status workflow (planned → approved → in progress → completed). Drag-and-drop on timeline.
- **Planning timeline:** Gantt-style calendar view. Resource utilisation indicators. Vertical stacking of overlapping assignments.
- **Optimisation engines:** All three solvers implemented and operational:
  - Greedy (Python) — instant baseline
  - OR-Tools CP-SAT (Python) — near-optimal, configurable time limit
  - Timefold (Java) — metaheuristic for large instances
- **Solution scoring:** Automated evaluation of solutions (hard score, soft score, breakdown by criterion).
- **Conflict detection:** Automated identification of scheduling violations — overbooking, overtime, missing competencies, night work, expired certifications, rest period violations, vehicle maintenance conflicts.
- **Multi-tenant workspaces:** Company-scoped data isolation. Role-based invitations (owner, admin, member).
- **User settings:** Language, timezone, week start day, notification preferences.
- **Dashboard:** Overview page with key metrics and utilisation charts.
- **Benchmarking:** Synthetic datasets and benchmarking framework for comparing solver performance.

### Not yet built

- **Driver-facing page:** Planned — drivers will have a dedicated view of their own schedule and assigned tasks. Not yet implemented.
- **User/admin management panel:** Authentication works, but there is no admin UI for managing users, roles, or permissions within a company.
- **Billing/invoicing integration:** Out of scope for the thesis, but identified as critical for adoption by multiple interviewees.
- **Two-factor authentication:** Framework exists in Better Auth, not yet enabled.

---

## User Research Summary

Seven semi-structured interviews were conducted on 4 March 2026 with traffic coordinators and transport managers across Norwegian companies:

| # | Company | Current system | Scale |
|---|---|---|---|
| 1 | Bergen Bulk Transport | None (manual) | 8–20 drivers |
| 2 | Harlem Solutions | Opter | Unknown |
| 3 | Norlog Lakselv | Timpex | Medium |
| 4 | Norlog Mo i Rana | Timpex + Admin | Medium |
| 5 | Norlog Tana | Timpex | Small (far north) |
| 6 | Ottem | Own system | ~45 vehicles, 3 departments |
| 7 | Nordic Crane (Svein) | Own system | Crane + transport |

**Key findings:**

1. **All assign jobs manually** — no system provides automatic assignment.
2. **Legacy systems are extremely slow** — Timpex under concurrent use; Opter and internal/custom tools report similar friction.
3. **Critical knowledge is tacit** — licences, experience, route familiarity, overtime status.
4. **Attitude to automation is split** — consensus: the system should suggest a plan the coordinator can correct, not replace the coordinator.
5. **Adoption depends on** speed, cost/benefit ratio, usability, and trust in the algorithm's output.
6. **Assignment criteria** (ranked by frequency): availability/position, experience, driving/rest time, competence/licence, route familiarity, equipment match, overtime status.

Full findings: `context/interviews-summary.md`

---

## Scope — Short Version

See `context/scope.md` for the full list.

**In scope:** Planning interface, algorithm-generated plan, manual override, driver/vehicle profiles, competency tracking, sick-leave handling, conflict detection, multi-tenant company workspaces.

**Out of scope:** Driver mobile app, GPS tracking, billing/invoicing, multi-company SaaS, payroll integration, customer portal.

---

## Key Application Routes

| Route | Purpose |
|---|---|
| `/login`, `/register` | Authentication |
| `/accept-invitation/[token]` | Join a company via invitation |
| `/ressursplanlegger` | Main planning timeline (Gantt-style) |
| `/oversikt` | Dashboard with utilisation metrics |
| `/alle-oppdrag` | List view of all assignments |
| `/ansatte`, `/ansatte/[id]` | Employee management and profiles |
| `/kjoretoy`, `/kjoretoy/[id]` | Vehicle management and profiles |
| `/avvik` | Deviation/conflict viewer |
| `/innstillinger` | User and company settings |
| `/invite` | Invite users to company |

---

## What Claude Must NOT Do

- Invent references or citations — only use sources from `result/references.bib`
- Claim the system has features not listed in `context/scope.md` or the project status above
- Rephrase or alter the research question — use it verbatim from this file
- Use "we believe" or "we think" — use impersonal academic constructions
- Assume something has been tested unless it appears in `context/docs/requirements/requirements-traceability.md`
- Write content for the other author's chapter without being explicitly asked
- Refer to the system as "Cephalo" — the system is called Ressursplanlegger
