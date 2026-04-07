# Non-Functional Requirements — Ressursplanlegger

> **Owner: Embret** — filled with realistic values based on the system implementation and codebase.

| ID | Category | Requirement | Target |
|----|----------|-------------|--------|
| IFK-01 | Performance | Algorithm response time (greedy solver) | < 3 seconds for up to 100 assignments |
| IFK-02 | Performance | Algorithm response time (OR-Tools CP-SAT) | < 60 seconds for up to 500 assignments (configurable time limit) |
| IFK-03 | Performance | CRUD API response time (assignments, employees, vehicles) | < 1 second per request under normal load |
| IFK-04 | Performance | Initial page load (Next.js, Vercel CDN) | < 3 seconds on a standard broadband connection |
| IFK-05 | Performance | Concurrent users supported | 5–50 coordinators per company without degradation (Vercel serverless auto-scales) |
| IFK-06 | Usability | Time to learn core planning workflow | < 30 minutes for a coordinator familiar with transport planning |
| IFK-07 | Reliability | Service availability | ≥ 99% (Vercel SLA; PostgreSQL cloud provider SLA) |
| IFK-08 | Security | Authentication mechanism | Session-based authentication (Better Auth); sessions stored in PostgreSQL with expiry |
| IFK-09 | Security | Authorisation | All data access scoped to the authenticated user's `companyId`; no cross-tenant data exposure |
| IFK-10 | Security | Input validation | All API inputs validated with Zod schemas before processing |
| IFK-11 | Security | SQL injection prevention | Prisma ORM uses parameterised queries throughout; no raw SQL in application code |
| IFK-12 | Scalability | Maximum employees per company plan | ~150 employees (tested in large benchmark dataset) |
| IFK-13 | Scalability | Maximum assignments per daily plan (greedy) | ~100–200 assignments with sub-3-second response |
| IFK-14 | Scalability | Maximum assignments per daily plan (OR-Tools) | ~500 assignments within 60-second time limit |
| IFK-15 | Maintainability | End-to-end type safety | All API calls type-checked at compile time via tRPC + TypeScript |
| IFK-16 | Portability | Browser support | All modern browsers (Chrome, Firefox, Safari, Edge); no mobile app |
