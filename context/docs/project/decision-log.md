# Decision Log — Ressursplanlegger

> Source-of-truth for major decisions referenced in §3.5 (iteration narratives) and §5 (discussion). One entry per decision. Reconstructed retrospectively from project artefacts and recall — exact dates approximate.
>
> Origin labels follow the §12.0.5 origin map: **Admmit-mandate**, **interview-validated**, **designer-technical**, **mixed**.

---

## Methodological decisions

### D1 — Choice of research method: DSR + DSRM

- **Decision:** Design Science Research, applied through Peffers' six-activity DSRM.
- **Alternatives considered:** Case study (interpretivist), purely positivist quantitative evaluation.
- **Reason:** The thesis combines (a) investigating a real-world problem through stakeholder consultation and (b) building a software system to address it. DSR explicitly accounts for artefact creation as a research outcome; case study alone documents context but excludes artefact construction; positivist quantitative evaluation cannot capture how coordinators actually work. The artefact-plus-knowledge contribution is the DSR-canonical structure (Hevner 2004; Peffers 2007).
- **Consequence:** Chapter 3 organises around DSRM activities. Evaluation is framed as validation (Wieringa 2014), not field evaluation — claims about practical impact are predictions grounded in benchmarking and requirements traceability, not observations from production.

---

### D2 — HITL as design principle from project start

- **Decision:** The artefact is positioned at automation level 5–6 (system suggests, human approves). Every algorithm-generated assignment is inspectable, modifiable, acceptable, or rejectable by the coordinator.
- **Alternatives considered:** Full automation with retroactive override only; advisory-only mode with no acceptance-required flow.
- **Reason:** Admmit-mandate from the bachelor task brief. Interviews subsequently validated the necessity through coordinator consensus that automated planning must be correctable, not authoritative. The choice resolves the operator-vs-owner asymmetry (Bainbridge 1983) by retaining operator authority over outcomes.
- **Consequence:** Drives the entire UI architecture (drag-and-drop timeline, accept/modify/reject flow). Drives the deviation taxonomy (system surfaces what to override toward). Drives the user-controlled time/quality tradeoff (operator authority over generation, not just outcomes).

---

### D3 — Multi-tenant architecture

- **Decision:** Every domain entity scoped by `companyId`; tenant isolation enforced at the data layer.
- **Alternatives considered:** Single-tenant deployment per customer; shared tenancy with row-level security in application code only.
- **Reason:** Admmit-mandate — Admmit's customer structure includes multiple transport companies that would each consume the artefact independently. Tenant isolation enforced at the data layer prevents cross-tenant leakage by construction; application-layer isolation alone would risk leakage on every new query path.
- **Consequence:** Every query, mutation, and constraint passes `companyId`. Becomes the architectural foundation for Tilpasningsdyktighet via per-company configurable soft-constraint weights (D9).

---

## Algorithm and solver decisions

### D4 — Greedy heuristic as instant baseline

- **Decision:** Priority-sorted greedy first-fit assignment heuristic implemented as the first solver before the constraint solver.
- **Alternatives considered:** Skip greedy, go directly to CP-SAT; implement only one solver.
- **Reason:** Provides instant feedback in the UI (sub-second on typical sizes). Reference point for measuring richer-solver gains. Establishes the solver-as-pluggable abstraction needed later for the multi-engine registry.
- **Consequence:** The greedy ceiling becomes itself a finding — local optima blocking later assignments motivates D5. Greedy remains the user-facing fast option in the time/quality control (D8).

---

### D5 — CP-SAT as complete solver for medium instances

- **Decision:** Google OR-Tools CP-SAT as the primary constraint-programming engine, with explicit hard + weighted soft constraints + objective function.
- **Alternatives considered:** Integer programming via PuLP/Gurobi; custom constraint propagation; SAT-based solver (Z3).
- **Reason:** Constraint programming fits assignment problems with rich hard/soft interaction. CP-SAT specifically gives near-optimal solutions within a configurable time budget — a critical property for HITL responsiveness. OR-Tools is open-source and has a stable Python API.
- **Consequence:** Models hard constraints (competencies, availability, no double-booking, vehicle type) as feasibility predicates and soft constraints (workload balance, vehicle preference, transitions, priority, employee preferences) as weighted penalties. The time-budget property enables D8.

---

### D6 — Timefold as metaheuristic for large instances

- **Decision:** Timefold metaheuristic engine (tabu search / simulated annealing / late-acceptance hill climbing) added as the third solver for large instances where CP-SAT's time budget binds.
- **Alternatives considered:** Larger CP-SAT time limit; custom local-search implementation; commercial solver (Gurobi).
- **Reason:** CP-SAT's quality degrades when the time limit binds on large instances. Timefold's metaheuristic family scales to large search spaces by accepting non-monotonic moves. Open-source and JVM-based, parallelisable independently of the rest of the stack.
- **Consequence:** Three-engine architecture. Subprocess plumbing complexity becomes the engineering cost. Engine version snapshots required for reproducibility (D7).

---

### D7 — Multi-engine selection and benchmarking framework

- **Decision:** Pluggable solver registry with engine version snapshots; synthetic small/medium/large datasets; comparative benchmarking framework.
- **Alternatives considered:** Single solver; production-data benchmark.
- **Reason:** Operationalises the §12.0.5 "How-not-Of" methodologically independent test — under realistic constraint combinations, *which* solver approach best meets Effektivitet? Synthetic datasets (vs production) because no production data is available; production-pilot is forwarded to §6.3.
- **Consequence:** The multi-engine architecture is itself a research instrument, not just an engineering choice. Effektivitet measurement, not problem validation. Forms the §3.6 evaluation framework backbone.

---

## UI and HITL decisions

### D8 — User-controlled plan-time vs plan-quality tradeoff

- **Decision:** Coordinator-facing toggle between *fast / less accurate* (greedy with short time limit) and *slower / more accurate* (CP-SAT with longer time limit).
- **Alternatives considered:** Internal heuristic that selects engine automatically based on instance size; always-best-effort with no user control.
- **Reason:** Different planning situations have different urgency-quality requirements (sick-leave replanning under pressure vs next-week's planning). Coordinator authority over plan generation is a Tillit/kontroll dimension distinct from plan-content override.
- **Consequence:** Adds a small case of explanation-driven HITL design. The labels themselves became a UX problem — bare time labels are illegible, descriptive labels smuggle in unverifiable quality claims. Final compromise: descriptive labels with a tooltip explaining what the toggle changes.

---

### D9 — Configurable soft-constraint weights (per company)

- **Decision:** Per-company UI for adjusting soft-constraint weights (workload balance, vehicle preference, transitions, priority, employee preferences). Weights flow into the CP-SAT objective function.
- **Alternatives considered:** Single shared weight set across all tenants; per-user weights; hard-constraint configurability.
- **Reason:** Interviews confirmed assignment criteria differ materially across companies. Tilpasningsdyktighet means the same artefact must serve materially different operational rules without code changes. Per-company weights are the minimum viable configurability.
- **Consequence:** Partial Tilpasningsdyktighet realisation. Hard constraints, status workflows, and per-company assignment-rule taxonomies remain hard-coded — acknowledged as L4-adjacent in §5.4 and forwarded to §6.3.

---

## Evaluation and methodology decisions

### D10 — Evaluation framing: validation, not evaluation

- **Decision:** Frame the artefact's testing as validation (Wieringa 2014) — predicting behaviour through synthetic benchmarking and requirements traceability — rather than evaluation in deployed production use.
- **Alternatives considered:** Production pilot; user testing with coordinators using the live system.
- **Reason:** Production pilot not feasible within the bachelor timeframe (no transport company committed to deployment). Validation is the appropriate stance for a not-yet-deployed artefact (Wieringa).
- **Consequence:** Chapter 5 language is calibrated to predicted behaviour, not observed impact ("the validation suggests", "based on the benchmarks, the algorithm is expected to…"). Limitations L5–L9 in §5.4 name the validation/evaluation gap explicitly.

---

## Deviations from plan

### D11 — Sick-leave replanning dropped

- **Decision:** Drop real-time replanning for sick-leave events from scope.
- **Reason:** Time constraints. Implementing replanning correctly requires partial-resolve semantics (what to keep, what to redo, how to bound the disturbance) — non-trivial within the remaining schedule.
- **Consequence:** Forwarded to §6.3 future work. Listed in §5.5 deviations from plan. Sick-leave handling appears in interviews (§4.1) and in the deviation taxonomy (D6) but cannot be replanned in real time within the current artefact.

---

### D12 — User testing with traffic coordinators dropped

- **Decision:** Drop planned user testing of the override flow with three traffic coordinators.
- **Reason:** Time constraints + access constraints (coordinator availability for in-person walkthroughs).
- **Consequence:** Anchors §5.4 L8 (no user testing with coordinators). Listed in §5.5 deviations. Forwarded to §6.3 future work. Override-flow validity is bounded by requirements traceability + designer judgement, not by coordinator-observed use.