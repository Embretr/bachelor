# Current Practice — How Traffic Coordinators Plan Today

> Source: 7 semi-structured interviews on 4 March 2026. See `context/interviews-summary.md` and `context/intervju/` for raw data.
> Purpose: a concrete, evidence-grounded description of the current resource-planning workflow used by traffic coordinators in Norwegian transport companies — the baseline that Ressursplanlegger is designed to improve on.
> Use for: Ch 1 (motivation), Ch 4.1 (findings on current practice), Ch 4.3 (fit/gap), Ch 5.1 (discussion of the gap closed).

---

## Summary in one paragraph

Across all seven companies interviewed, the daily assignment of drivers and vehicles to jobs is performed manually by a single traffic coordinator. The coordinator works either without a system (pen, phone, memory) or inside an order-management system (Timpex, Trimtex, Opptur, in-house) that stores the orders but does not assign drivers. The coordinator combines the day's order list with a mental model of who is available, who has the right competence, who knows the route, who is close to overtime limits, and which vehicle fits the job, and types the resulting decisions into the system row by row. No system in current use generates a plan automatically; none surface constraint violations before the coordinator commits the assignment.

---

## The workflow, step by step

The pattern below is reconstructed from the interviews and is consistent across all seven companies, with variation in tooling but not in structure.

### 1. Orders arrive
- **Source:** Phone, email, recurring contracts, customer integrations (Harlem Solutions has some customers auto-feeding orders into Opptur), or generated from fixed routes (Norlog Lakselv uses Timpex to auto-generate fixed runs).
- **Volume:** Varies — Norlog Tana ~5 routes/day; Ottem ~45 vehicles across 3 departments; Nordic Crane drivers handle 3–4 jobs each.
- **Planning horizon:** Mostly day-to-day (Bergen Bulk, Norlog Tana). Nordic Crane plans 5 hours to 2 months ahead. Norlog Lakselv mixes fixed routes with day-to-day variable jobs.

### 2. The coordinator builds a mental picture of available resources
This step is entirely cognitive and uses no tooling. The coordinator holds in their head:
- Which drivers are working today (schedule, vacation, sick leave called in this morning).
- Each driver's licences, certifications, and route experience.
- Each driver's accumulated driving and rest hours under the EU/EØS rules.
- Each driver's progress toward weekly and yearly overtime limits.
- Which vehicles are operational, on maintenance, or out of service, and which trailers are coupled where.
- Which customers prefer or refuse specific drivers.

This is the "tacit knowledge" problem: if the coordinator is absent, no one else has the picture.

### 3. Assignments are made one at a time
For each order the coordinator picks a driver and a vehicle by mentally matching the job's requirements against the resource picture. The assignment criteria, ranked by frequency across interviews:
1. Availability and current position
2. Experience, especially on demanding routes
3. Driving and rest time (statutory)
4. Competence and licence (right certificate for the job)
5. Route familiarity (especially in the north)
6. Equipment match (right vehicle for the job)
7. Overtime status (especially against annual limits)

Ottem reports roughly **one minute per assignment**. Across 45 vehicles and three departments this is a substantial daily cognitive load concentrated on a single person.

### 4. Assignments are entered into the system
Once decided, the assignment is typed into whichever system the company uses for orders and invoicing:
- **Timpex** (Norlog Lakselv, Norlog Mo i Rana) — used for orders, invoicing, can auto-generate fixed routes, but the driver-to-job assignment is done manually.
- **Trimtex** (Norlog Tana) — same pattern.
- **Opptur** (Harlem Solutions) — same pattern; some customer orders flow in automatically.
- **In-house order systems** (Ottem, Nordic Crane) — same pattern.
- **No system** (Bergen Bulk Transport) — phone, paper, memory; "the old way".

These systems are containers for assignments, not assignment engines.

### 5. Drivers are notified
- **App with push notifications:** Timpex Confirm at the Norlog companies; the order app at Harlem.
- **Direct phone calls:** Norlog Tana, Bergen Bulk Transport.
- **Communication only on deviations:** Nordic Crane drivers receive their 3–4 jobs and contact the coordinator only if something goes wrong.

### 6. Disruptions are handled by reassignment
The plan is rarely the final plan. The coordinator spends a substantial part of the day reacting:
- **Sick leave** — a driver calls in; the coordinator finds a replacement and reshuffles affected routes. Norlog Tana describes this as "essentially the problem-solving I sit with every single day"; routes that require scanning competence make replacements harder.
- **Cancelled orders** — Ottem reports this happens unpredictably and forces re-planning mid-day.
- **Vehicle breakdown or maintenance overrun** — the affected job needs a different vehicle, which can cascade into other jobs.
- **Late finishes** — push subsequent jobs back or reassign them.

Some companies experience this as routine ("2–3 keystrokes" — Norlog Lakselv; "27 seconds" — Nordic Crane). Others experience it as the dominant daily activity (Norlog Tana, Ottem).

---

## What current systems do not do

This is the gap Ressursplanlegger targets, derived directly from the interviews:

| Capability missing today | Evidence |
|---|---|
| **Automatic driver-to-job assignment** | All seven coordinators assign manually; no system generates a complete plan. |
| **Constraint enforcement before commit** | Coordinators rely on memory for licence, rest-time, overtime, certification expiry; mistakes are caught after the fact, if at all. |
| **Unified capacity overview** | Norlog Mo i Rana operates across three systems (Admin + Timpex + Admit); information is fragmented. |
| **Responsive performance** | Timpex and Trimtex are described as "extremely slow", especially under concurrent use; Norlog Mo i Rana names speed as the single most important thing to improve. |
| **Structured representation of tacit knowledge** | Competence, route familiarity, customer preferences live in the coordinator's head, not in any system. |
| **Decision support for disruption handling** | Sick-leave reshuffling is manual; nothing suggests a feasible replacement that satisfies all constraints. |
| **Time-shifted automatic notification** | Nordic Crane explicitly wants automatic dispatch 18–24 hours before execution; no current system offers this. |

---

## Variation across companies

The structural workflow is the same; the inputs and the felt difficulty differ.

| Company | Distinguishing feature of current practice |
|---|---|
| Bergen Bulk Transport | No system at all; views a TMS as worthwhile only at 15–20+ vehicles. |
| Harlem Solutions | Some customers auto-feed orders, but driver assignment is still manual; argues no two days are alike, so automation is hard to trust. |
| Norlog Lakselv | Fixed routes generated automatically by Timpex; variable jobs assigned manually; integration work with Admin underway. |
| Norlog Mo i Rana | Three systems in parallel; primary pain is speed; goal is to keep everything in a system rather than on yellow notes. |
| Norlog Tana | Small fleet, ~5 routes/day, food/temperature-controlled; scanning competence required on some routes; daily sick-leave reshuffling dominates the workday. |
| Ottem | 45 vehicles, 3 departments; ~1 minute per assignment; orders cancelled unpredictably; wants notification before any auto-assignment commits. |
| Nordic Crane | Crane and transport divisions; transport "much more demanding" because all drivers hold the same certificates so experience is the discriminator; planning horizon spans 5 hours to 2 months. |

---

## Implications for Ressursplanlegger

The current practice analysis defines the design constraints the system inherits:

- **Suggest, do not replace.** The split attitude to automation, combined with the unanimous reliance on coordinator judgement, means the system must propose a plan and let the coordinator override any part of it. This is the "suggest + override" pattern referenced throughout the thesis.
- **Formalise the tacit.** Driver competence, certifications, route familiarity, schedules, and time-off must become structured data so the algorithm can reason about them.
- **Be fast.** The most consistent complaint about incumbent systems is speed. A modern stack and an instant greedy baseline are not optional.
- **Make disruption handling first-class.** Sick leave and cancellation are the daily reality; the system must support quick reassignment, not just initial planning.
- **Surface constraint violations before commit.** Conflict detection (overbooking, overtime, missing competence, expired certifications, rest-period violations) is what turns a list of assignments into a plan the coordinator can trust.
- **Respect the planning horizon.** Some users plan day-to-day; others plan months ahead. The system must accommodate both, including time-shifted notification windows.

These implications are picked up directly in the requirements (`context/docs/requirements/functional-requirements.md`) and in the architectural decisions (`context/docs/tech/architecture.md`, `context/docs/tech/algorithm.md`).
