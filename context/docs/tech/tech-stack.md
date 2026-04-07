# Technology Stack — Ressursplanlegger

> **Owner: Embret** — filled based on actual codebase.
> Used directly in Chapter 4.4 and Chapter 5 (discussion of tech choices).

---

## Stack Overview

| Layer | Technology | Version |
|-------|-----------|---------|
| Frontend framework | Next.js (React) | 15 (App Router) |
| Language | TypeScript | 5.8.2 |
| UI component library | shadcn/ui + Radix UI | — |
| Styling | Tailwind CSS | 4.0.15 |
| API layer | tRPC | 11.0.0 |
| Authentication | Better Auth | 1.3 |
| Database | PostgreSQL | — |
| ORM / Query layer | Prisma | 7.2.0 |
| Algorithm — greedy baseline | Python (custom) | 3.x |
| Algorithm — constraint solver | Google OR-Tools (CP-SAT) | latest |
| Algorithm — advanced solver | Timefold Solver (Java) | — |
| Package manager | pnpm | 10.14.0 |
| Hosting | Vercel (frontend) / Docker (DB) | — |
| CI/CD | GitHub Actions | — |

---

## Decision Log per Technology

### Frontend: Next.js 15 with React 19
**Chosen:** Next.js 15 (App Router) with React 19
**Alternatives considered:** Vue 3, SvelteKit, plain Create React App
**Reason for choice:** Next.js provides server-side rendering, file-based routing, and seamless deployment to Vercel. The App Router model supports server components, which reduces client-side JavaScript. Full-stack TypeScript across the same monorepo removes the need for a separate Express/FastAPI backend for most routes.
**Reason against alternatives:** Vue and Svelte have smaller ecosystems and less integration with the tRPC + Prisma toolchain. Plain CRA lacks SSR and routing conventions.

### API Layer: tRPC
**Chosen:** tRPC 11
**Alternatives considered:** REST (Express/Fastify), GraphQL
**Reason for choice:** tRPC provides end-to-end type safety between the Next.js backend and the React frontend without code generation or schema files. Type errors in API calls are caught at compile time, which reduces runtime bugs in a complex domain model with many nested relationships.
**Reason against alternatives:** REST requires manual type synchronisation between client and server. GraphQL introduces schema overhead and a resolver pattern that adds complexity for a single-team project.

### Database: PostgreSQL
**Chosen:** PostgreSQL
**Alternatives considered:** MySQL, SQLite, MongoDB
**Reason for choice:** PostgreSQL supports advanced indexing, transactions, and relational integrity — all necessary for a planning domain with M2M relationships (assignments ↔ employees ↔ vehicles ↔ competencies). The combination with Prisma gives type-safe queries and migration management.
**Reason against alternatives:** SQLite is not suitable for concurrent writes in a multi-user web application. MongoDB's document model is a poor fit for a highly relational domain.

### ORM: Prisma
**Chosen:** Prisma 7
**Alternatives considered:** Drizzle ORM, TypeORM, raw pg
**Reason for choice:** Prisma generates a type-safe client from the schema, provides a visual browser (Prisma Studio) for debugging, and handles migrations. The schema-first approach is readable and maintainable by both authors.
**Reason against alternatives:** TypeORM uses decorators and reflection, which adds complexity. Drizzle is lower-level and lacks Prisma Studio.

### Algorithm Libraries
**Chosen (multi-engine):** Python greedy solver (custom), Google OR-Tools CP-SAT (Python), Timefold Solver (Java)
**Alternatives considered:** OR-Tools alone, pure JavaScript solver, external optimisation API
**Reason for choice:** A pluggable multi-engine architecture allows comparing solver quality and performance — which is itself a research contribution. The greedy solver provides a fast baseline; OR-Tools provides near-optimal solutions for medium-scale problems; Timefold handles large-scale instances with advanced metaheuristics. All are invoked as subprocesses, keeping the algorithm code independent of the Node.js runtime.
**Reason against alternatives:** A JavaScript solver would be slower and lack mature optimisation libraries. An external API introduces network latency and a dependency on a third-party service.

### Authentication: Better Auth
**Chosen:** Better Auth 1.3
**Alternatives considered:** NextAuth.js, Auth0, custom JWT
**Reason for choice:** Better Auth provides a modern, framework-agnostic session management layer with a Prisma adapter, enabling session and account data to live in the same PostgreSQL database as the application data. It supports OAuth flows if needed later.
**Reason against alternatives:** NextAuth.js requires more configuration for custom Prisma adapters and has historically had breaking changes between major versions. Auth0 introduces a paid external dependency.

---

## Dependencies Worth Mentioning in the Thesis

| Package | Purpose | Why this one |
|---------|---------|--------------|
| `@tanstack/react-query` | Client-side data fetching and cache | Industry standard; integrates directly with tRPC |
| `react-dnd` | Drag-and-drop on the planning timeline | Headless DnD library; works with custom renderers |
| `zod` | Runtime schema validation for API inputs | Composable, TypeScript-native; shared between frontend and backend |
| `recharts` | Utilisation and capacity charts | React-native chart library built on D3 |
| `superjson` | Serialisation of Date/BigInt through tRPC | Required for Prisma Date objects over tRPC |
| `sonner` | Toast notifications for user feedback | Accessible and minimal; works with React 19 |
| `ortools` (Python) | CP-SAT constraint solver | Google-maintained, best-in-class open-source solver |
