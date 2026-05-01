% sprint-log.md — Ressursplanlegger

# Sprint Log — Ressursplanlegger

> Source-of-truth for §3.5 (Iterative Development Process). Eight named iterations told as a connected narrative. Boundaries are reconstructed retrospectively from the codebase, GitHub Issues, and decision recall — precise dates and ordering are approximate.
>
> Origin labels follow the §12.0.5 origin map: **Admmit-mandate** (specified by Admmit at project start), **interview-validated** (surfaced or confirmed in stakeholder consultations), **designer-technical** (team's own technical exploration), **mixed** (combination).

---

## Project structure

- **Team:** Mikael (user research, requirements, thesis writing) + Embret (system development, algorithm implementation).
- **Tooling:** GitHub for version control and issue tracking. No separate project management tool.
- **Cadence:** Informal sprints. Iteration boundaries are conceptual rather than calendrical — each iteration ends when its substrate stabilises enough to motivate the next.
- **Stakeholders:** Admmit (oppdragsgiver) for mandate clarification + final demo. NTNU supervisor for academic guidance. Seven traffic coordinators consulted in brief phone interviews (~15 minutes each) on a single day.

---

## Iteration 1 — Schema and Timeline Scaffolding

- **Origin:** Admmit-mandate (multi-tenant architecture) + designer-technical (data model + read-only timeline UI).
- **Tried:** Core entity model — employees, vehicles, assignments, certifications, work schedules, time-off. Multi-tenant data isolation enforced at the data layer (every query scoped by `companyId`). Read-only Gantt-style timeline UI rendering existing assignments without optimisation.
- **Why:** Later solver iterations need a structured substrate. Multi-tenancy must be enforced at the data layer per Admmit's customer structure — bolting it on later would risk cross-tenant leakage.
- **What happened:** Substrate adequate for the simplest assignment heuristic but required revision when constraint-solver formalisation surfaced gaps in the data model — explicit time-off windows, certificate-expiry as queryable date, and per-day work-schedule entries became needed only after ¶2.
- **Learned:** Schema-first discipline reduces rework but cannot fully anticipate solver requirements. The substrate is itself an iteration, not a one-shot setup.
- **Next:** With substrate stable, attempt the simplest possible assignment heuristic.

---

## Iteration 2 — Single-engine Baseline (greedy)

- **Origin:** Designer-technical exploration.
- **Tried:** Priority-sorted greedy first-fit assignment heuristic. Sort assignments by priority, walk through them, assign the first feasible driver/vehicle combination found.
- **Why:** Instant baseline producing a feasible plan. Reference point for richer solvers and instant UI feedback for the coordinator while drag-and-drop happens.
- **What happened:** Works on small instances (<30 assignments). On larger instances, priority-sorted greedy commits early to locally optimal but globally suboptimal choices, blocking later high-priority assignments and producing avoidable idle time and overtime.
- **Learned:** The greedy ceiling is structural, not a tuning issue. Cannot break out of it by reordering the priority comparator — needs constraint propagation and a global view.
- **Next:** Introduce a complete solver.

---

## Iteration 3 — Constraint Generalisation (CP-SAT)

- **Origin:** Designer-technical exploration.
- **Tried:** Google OR-Tools CP-SAT solver with explicit hard constraints (competencies, availability, no double-booking, vehicle type) + weighted soft constraints (workload balance, vehicle preference, transitions, priority, employee preferences) + objective function maximising scheduled assignments minus weighted soft-constraint violations.
- **Why:** Constraint programming is a known fit for assignment problems with complex interaction between hard and soft constraints. CP-SAT specifically gives near-optimal solutions within a configurable time budget.
- **What happened:** Near-optimal solutions on small to medium instances within a 30–60 second time limit. Quality degrades on larger instances when the time limit binds — solver returns the best feasible solution found rather than the optimum. Modelling complexity higher than the heuristic — required several iterations to get hard-vs-soft mapping correct.
- **Learned:** CP-SAT covers the medium-instance gap but introduces a scaling boundary that motivates a third engine for large instances.
- **Next:** A third engine for large instances + a way to compare the three.

---

## Iteration 4 — Multi-engine Selection and Benchmarking

- **Origin:** Designer-technical exploration. Operationalises the §12.0.5 "How-not-Of" methodologically independent test.
- **Tried:** Pluggable solver registry with three engines: greedy heuristic (instant baseline), OR-Tools CP-SAT (complete-with-time-budget), Timefold metaheuristic (large-instance scaling via tabu / simulated annealing / late-acceptance hill climbing). Benchmarking framework with synthetic small / medium / large datasets. Engine version snapshots for reproducibility.
- **Why:** Under realistic constraint combinations, *which solver approach best meets Effektivitet?* — a how-question independent of whether the visibility gap is real (interviews surface this) or whether HITL is necessary (Admmit mandate).
- **What happened:** Subprocess plumbing complex — Timefold runs as a separate JVM process; CP-SAT inside Python; greedy in TypeScript. Reproducibility issues required adding engine-version snapshots after early benchmark results were inconsistent across runs.
- **Learned:** The multi-engine architecture is a comparative test of *how*, not *whether*. Effektivitet measurement, not problem validation. This framing returns in §3.6, §4.5, and §5.1.1.
- **Next:** With computation infrastructure stable, build the human-in-the-loop surface.

---

## Iteration 5 — HITL Surface (drag-and-drop timeline + override flow)

- **Origin:** Mixed — Admmit-mandate (HITL principle from project start) + interview-validated (drag-drop UI specifically validated by interview-derived consensus that the system should suggest a plan the coordinator can correct, not replace the coordinator).
- **Tried:** Gantt-style drag-and-drop assignment UI. Explicit accept / modify / reject on every algorithm-generated suggestion. Thin post-hoc constraint check (basic feasibility only — over-booking, missing competence).
- **Why:** HITL was Admmit's requirement from project start. Interviews validated the necessity through a consensus that automated planning must be correctable, not authoritative.
- **What happened:** Drag-and-drop functional. State-consistency between optimistic UI updates and server mutations produced occasional stale conflict displays — the timeline showed a violation that had already been resolved server-side. Required adding a refresh hook on assignment updates.
- **Learned:** HITL surface needs richer real-time feedback than a thin post-hoc check. Coordinator authority is meaningful only when the system surfaces what to act on.
- **Next:** Expand the post-hoc check into a full deviation taxonomy.

---

## Iteration 6 — Real-time Deviation Detection

- **Origin:** Designer / domain knowledge — extensions of pain points around tacit knowledge but specific deviation categories were not asked about in interviews (per §12.0.5 origin map).
- **Tried:** Post-generation conflict scanner across multiple deviation categories — overbooking, overtime violations, missing competencies, expired certifications, rest-period violations, vehicle maintenance conflicts, night-work conflicts, unavailable-employee assignments. Severity levels and a status workflow (open / acknowledged / resolved). Inline display on the planning timeline plus a dedicated deviations view.
- **Why:** A meaningful HITL surface requires the system to surface *what* the coordinator should override toward — not an empty timeline they edit blindly.
- **What happened:** False positives where edge-case interactions between work-schedule and time-off produce noisy alerts (week boundaries, mid-shift absences). Rest-period violations inherently noisy due to multiple regulatory definitions (48h average vs 60h max vs 13h daily).
- **Learned:** Deviation detection materialises tacit knowledge as structured conflict data. Tuning thresholds is itself a coordination problem the system cannot fully resolve — the coordinator decides when a flagged deviation is real.
- **Next:** With the planning surface and deviation feedback complete, expose the user-facing planning-time control.

---

## Iteration 7 — User-controlled Plan-time vs Plan-quality Tradeoff

- **Origin:** Designer / Tillit/kontroll refinement — gives the coordinator agency over the planning *process*, not just over plan outcomes.
- **Tried:** User-facing solver-time-budget control — coordinator selects either *fast / less accurate* (heuristic with short time limit) or *slower / more accurate* (CP-SAT with longer time limit). The time-quality tradeoff is exposed as a deliberate choice rather than an internal default.
- **Why:** Different planning situations have different urgency-quality requirements (a sick-leave replanning under time pressure differs from next-week's planning). Coordinator authority over plan generation is a Tillit/kontroll dimension distinct from plan-content override.
- **What happened:** The choice surface itself raised the question of *what the user is choosing between*. Bare time labels are not legible; descriptive labels ("fast suggestion" vs "best-effort plan") are clearer but smuggle in claims about quality the system cannot verify per-instance.
- **Learned:** Exposing a tradeoff requires explanation as interface (Miller framing). The time control is itself a small case of explanation-driven HITL design.
- **Next:** Bridge into per-company configurability of *planning rules* (the soft-constraint weight space).

---

## Iteration 8 — Configurable Soft-constraint Weights

- **Origin:** Designer / architectural — operationalises the Tilpasningsdyktighet anchor that the project committed to from project start (Admmit-mandated multi-tenant architecture). Specific weight set chosen by designers, not interview-validated as the right set.
- **Tried:** Per-company weight configuration UI for soft constraints — workload balance, vehicle preference, transitions between consecutive assignments, priority, employee preferences. Weights flow into the solver objective function.
- **Why:** Interviews confirmed assignment criteria differ materially across companies. Tilpasningsdyktighet means the same artefact must serve materially different operational rules without code changes.
- **What happened:** Hard to validate that user-chosen weight combinations don't produce degenerate solutions (e.g., weights summing to zero, or one weight dominating to the exclusion of others). UX challenge of explaining what each weight means to a coordinator without optimization vocabulary.
- **Learned:** Configurability for soft weights is a partial Tilpasningsdyktighet realisation. Broader configurability — hard constraints, status workflow definitions, per-company assignment-rule taxonomies — is acknowledged as L4-adjacent and remains future work (cross-references §6.3 + §5.4 L4).
- **Next:** With eight iterations of artefact in place, the methodological question is *how* to test whether it meets the locked anchors — bridges into §3.6.

---

## Cross-iteration summary

| Iteration | Anchor preloaded | Origin | Key learning |
|---|---|---|---|
| 1 — Schema | — | Admmit + designer | Substrate is itself an iteration |
| 2 — Greedy | Effektivitet (negative result) | Designer | Greedy ceiling is structural |
| 3 — CP-SAT | Effektivitet | Designer | Time budget binds on large instances |
| 4 — Multi-engine | Effektivitet (How-not-Of) | Designer | Comparative test of *how*, not *whether* |
| 5 — HITL surface | Tillit/kontroll | Admmit + interview | HITL needs richer feedback than thin post-hoc check |
| 6 — Deviation taxonomy | Tillit/kontroll | Designer / domain | Tuning thresholds is itself a coordination problem |
| 7 — Time/quality control | Tillit/kontroll | Designer | Tradeoff exposure requires explanation |
| 8 — Configurable weights | Tilpasningsdyktighet | Designer / architectural | Soft-weight config is partial; hard-constraint config is L4 |

---

## What was not done (forwarded to §5.5 Deviations / §6.3 Future Work)

- **Real-time replanning for sick-leave events** — planned but dropped due to time. Forwarded to §6.3 (future work) and §5.5 (deviation from plan).
- **User testing with traffic coordinators** — planned (3 coordinators were considered for testing the override flow) but dropped due to time. Forwarded to §5.4 L8 (no user testing) and §5.5.