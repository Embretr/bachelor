# Optimization Algorithms (`timefold2026solver`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Full MD file read (lines 1–854). All three sections of the documentation page (algorithm overview, architecture, move selection) covered. All areas of interest investigated and either extracted or marked outside scope.
  - **Gaps not investigated:** None — the MD file is the complete source.

## Source metadata
- **BibTeX key:** `timefold2026solver`
- **Reference (APA 7):** Timefold. (2026). *Optimization Algorithms*. https://docs.timefold.ai/timefold-solver/latest/optimization-algorithms/overview (accessed 2026-04-23)
- **Tilgang:** open (public web documentation)
- **Raw source:** `../timefold2026solver.md` (MD fallback — original is a web page)
- **Coverage in raw:** §1 (Basics: search space, optimality, algorithm families, algorithm selection), §2 (Architecture: phases, scope, termination, events, custom phases), §3 (Move and neighbourhood selection). Complete page content.
- **Page number note:** This source is web documentation without printed page numbers. All references use section numbers (§X.Y). No dual page reference applies.

## Sammendrag (2–3 setninger)
Timefold Solver's documentation describes three families of optimization algorithms — Exhaustive Search, Construction Heuristics, and Metaheuristics — and argues that Metaheuristics combined with Construction Heuristics are the recommended choice for real-world planning problems, because exact methods become computationally intractable as problem size grows. The core engineering stance is that finding the optimal solution is usually impossible in practice, so the solver focuses on finding the best solution within the available time budget. For our thesis, this source provides authoritative documentation for what the Timefold engine does, why metaheuristics are appropriate at our scale, and the recommended phase configuration (Construction Heuristic → Local Search).

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.1 ¶4 (NP-hardness, motivation for heuristics) | Covered — §1.1–1.2 directly address intractability and the rationale for heuristics |
| Ch 2.1 ¶5 (Solver comparison: greedy, CP-SAT, Timefold) | Covered — §1.3 algorithm table and §1.4 configuration guidance support the comparison |
| Ch 4.5 ¶2 (Chosen approach and justification for Timefold) | Covered — §1.2, §1.3, §1.4, §2.2, §2.4.4 all support justifying Timefold as the large-instance solver |
| Ch 4.5 ¶5 (Known algorithm limitations) | Partial — §1.2 notes scalability limits and reproducibility issues; no domain-specific limitations |
| Ch 5.2 ¶1 (Algorithm performance under real-world constraints) | Partial — §1.2 addresses scalability and the gap between small-dataset and production-dataset quality |

## Claims this source supports

### Claim: "Planning problems at real-world scale have search spaces so large that exact solution methods are computationally intractable"
- **Suggested for:** Ch 2.1 ¶4 (primary — motivates multi-engine heuristic approach); Ch 4.5 ¶2 (secondary — justifies Timefold selection)
- **Direkte sitat:** "An algorithm that checks every possible solution (even with pruning, such as in Branch And Bound) can easily run for billions of years on a single real-life planning problem." (§1.1)
- **Parafrase:** For planning problems of realistic size, exhaustive search is computationally infeasible; the aim must be to find the best solution within the available time window.
- **Forbehold:** The argument is general to constraint satisfaction and scheduling problems; the source does not quantify "real-world scale" for our specific domain (driver + vehicle assignment).
- **Anvendelse på vårt case:** Ressursplanlegger's decision to use heuristics (greedy, CP-SAT, Timefold) rather than exhaustive search is directly motivated by this claim — with 50+ assignments and 20+ drivers, exact enumeration is infeasible within an operational time budget, and the multi-engine approach is the practical response.

### Claim: "Timefold Solver targets the best solution in available time, not the mathematically optimal solution"
- **Suggested for:** Ch 4.5 ¶2 (primary — justification of approach); Ch 2.1 ¶4 (secondary)
- **Direkte sitat:** "Given these requirements, and despite the promises of some salesmen, it is usually impossible for anyone or anything to find the optimal solution. Therefore, Timefold Solver focuses on finding the best solution in available time." (§1.2)
- **Parafrase:** The solver trades optimality guarantees for practical scalability and reliability — every dataset produces at least a decent result, but not necessarily the global optimum.
- **Forbehold:** This is the vendor's stated positioning, not an independent benchmark. The claim is about design philosophy, not empirically verified performance on our specific problem.
- **Anvendelse på vårt case:** Ressursplanlegger's Timefold engine is configured with a time limit; the plan it returns is the best found within that limit, not a provably optimal assignment. This is appropriate for traffic coordinators who need a plan within minutes, not hours.

### Claim: "Metaheuristics combined with Construction Heuristics are the recommended algorithm family for real-world planning problems"
- **Suggested for:** Ch 2.1 ¶5 (primary — solver comparison); Ch 4.5 ¶2 (secondary)
- **Direkte sitat:** "In practice, Metaheuristics (in combination with Construction Heuristics to initialize) are the recommended choice" (§1.3)
- **Parafrase:** Construction Heuristics provide a fast initial solution (5/5 scalable, ~2/5 optimal); Metaheuristics then improve it (5/5 scalable, 4/5 optimal), outperforming exact methods at scale.
- **Forbehold:** "Recommended" is the vendor's guidance from experience; optimal configuration depends heavily on the specific use case (§1.4).
- **Anvendelse på vårt case:** Ressursplanlegger's Timefold configuration follows this pattern — a construction heuristic initialises the plan and a local search phase (Late Acceptance / Tabu Search) improves it. This is the documented best practice, not an arbitrary choice.

### Claim: "The recommended practical configuration is First Fit Decreasing → Late Acceptance (primary) → Tabu Search (secondary)"
- **Suggested for:** Ch 4.5 ¶2 (primary — describes the solver configuration used)
- **Direkte sitat:** "First Fit Decreasing. Late Acceptance (relatively long time). Tabu Search (relatively short time)." (§1.4)
- **Parafrase:** The vendor recommends starting with First Fit Decreasing (fast, good-enough initial solution) and then improving with Late Acceptance for the bulk of solving time, optionally adding a short Tabu Search phase.
- **Forbehold:** This is a starting configuration; specific parameter values should be tuned with the Benchmarker for production use.
- **Anvendelse på vårt case:** If Ressursplanlegger's Timefold configuration follows this pattern, this citation provides the authoritative source for why that configuration was chosen. If the actual implementation deviates, this claim should be cited only as the "recommended baseline" against which the actual configuration was chosen.

### Claim: "A solver runs phases in sequence — typically Construction Heuristic first, then one or more Local Search (Metaheuristic) phases"
- **Suggested for:** Ch 4.5 ¶2 (describes solver pipeline)
- **Direkte sitat:** "If no phases are configured, Timefold Solver will default to a Construction Heuristic phase followed by a Local Search phase." (§2.2)
- **Parafrase:** The Timefold solver pipeline is sequential: a construction heuristic initialises a solution, and a metaheuristic phase then iteratively improves it.
- **Forbehold:** The phase sequence is fully configurable; the default is documented here, but production configurations often extend or modify it.
- **Anvendelse på vårt case:** Ressursplanlegger's Timefold engine uses this phase structure — the greedy / CP-SAT outputs can act as a warm start before Timefold's local search phase refines the solution further.

### Claim: "Diminished Returns termination is the recommended termination strategy — it is based on the rate of improvement and is largely hardware-independent"
- **Suggested for:** Ch 4.5 ¶2 (implementation detail) — can be cited if Ressursplanlegger uses this termination
- **Direkte sitat:** "For the best experience overall, we recommend using the Diminished Returns termination. It is based on the rate of improvement of the solver, and should therefore be mostly independent of the factors listed above." (§2.4.1)
- **Parafrase:** Unlike time-based or score-based termination, Diminished Returns terminates when the rate of improvement drops below a threshold, making it more portable across hardware configurations.
- **Forbehold:** Only cite if Ressursplanlegger actually uses this termination strategy. If a fixed time limit is used instead, cite the time-spent termination (§2.4.4) instead.
- **Anvendelse på vårt case:** A Diminished Returns termination would allow Ressursplanlegger to terminate as soon as the plan stops improving significantly, rather than always running a fixed time — relevant for coordinator workflows where plan generation time directly affects usability.

### Claim: "Scalability is the primary concern for NP-complete planning problems — quality of results from small datasets does not predict quality on large datasets"
- **Suggested for:** Ch 4.5 ¶5 (known limitations — benchmarking on small datasets)
- **Direkte sitat:** "The quality of a result from a small data set is no indication of the quality of a result from a large data set." (§1.2)
- **Parafrase:** Algorithm performance must be assessed at production scale; results from prototype-sized instances are not valid indicators of production performance.
- **Forbehold:** This is a general engineering principle from the vendor, not an empirical study of our specific problem.
- **Anvendelse på vårt case:** Ressursplanlegger's benchmark results (Ch 4.5 ¶6) should be interpreted in light of this — benchmarks on small test datasets may underestimate or overestimate performance at full fleet scale, which is a limitation of the current validation approach.

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Planning entity | Assignment (oppdrag) | An assignment is the atomic unit that the solver places |
| Planning value | Driver + vehicle combination | Each assignment receives a (driver, vehicle) pair |
| Solution | Plan | The complete daily plan for all assignments |
| Score | Solution score (hard score + soft score) | Same concept, same terminology in our glossary |
| Hard constraint | Hard constraint | Same terminology |
| Soft constraint | Soft constraint | Same terminology |
| Construction Heuristic | Greedy solver (or initial CP-SAT run) | Fast first-pass that initialises a feasible solution |
| Local Search / Metaheuristic | Timefold optimization phase | The improvement phase in Ressursplanlegger |
| Move | Manual override / algorithm reassignment | In Ressursplanlegger a "move" is a reassignment of driver or vehicle |
| Phase | Solver phase | The source's phase architecture maps directly to how Ressursplanlegger chains greedy → Timefold |
| Solver | Timefold engine (within multi-engine optimizer) | One of three solvers in Ressursplanlegger |

### Begrensninger i applikasjon

- **No domain-specific benchmarks:** All performance claims in the source are general (N-queens, generic planning) — no data for driver + vehicle assignment problems at fleet sizes (20–100 drivers).
- **No constraint modelling coverage:** This documentation page covers optimization algorithms only, not how to model hard/soft constraints for driver scheduling. Constraint modelling details are in other Timefold docs or in our own algorithm.md.
- **Vendor documentation:** This source is authoritative for "what Timefold does" but cannot be cited for independent performance claims. It represents design intent, not third-party evaluation.
- **Web documentation (not peer-reviewed):** Suitable for engineering justification and algorithm description, but not for theoretical claims (use pinedo2016scheduling, rossi2006constraint, or glover1986future for theoretical grounding).
- **Version-specific:** Based on urldate 2026-04-23; the "latest" URL means documentation may drift. The specific algorithms (Tabu Search, Late Acceptance, etc.) are stable, but configuration recommendations may change.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Move | "A Move is a change (or set of changes) from a solution A to a solution B." | §3.1 |
| Neighbor (of a solution) | "The new solution is called a neighbor of the original solution, because it can be reached in a single Move." | §3.1 |

## Rammeverk og modeller

### Algorithm Comparison Table (§1.3)

The source presents a rated comparison of all supported algorithm families across five dimensions:

| Algorithm | Scalable? | Optimal? | Easy to use? | Tweakable? | Requires CH? |
|---|---|---|---|---|---|
| Brute Force (ES) | 0/5 | 5/5 | 5/5 | 0/5 | No |
| Branch And Bound (ES) | 0/5 | 5/5 | 4/5 | 2/5 | No |
| First Fit (CH) | 5/5 | 1/5 | 5/5 | 1/5 | No |
| First Fit Decreasing (CH) | 5/5 | 2/5 | 4/5 | 2/5 | No |
| Tabu Search (LS) | 5/5 | 4/5 | 3/5 | 5/5 | Yes |
| Simulated Annealing (LS) | 5/5 | 4/5 | 2/5 | 5/5 | Yes |
| Late Acceptance (LS) | 5/5 | 4/5 | 3/5 | 5/5 | Yes |
| Variable Neighborhood Descent (LS) | 3/5 | 3/5 | 2/5 | 5/5 | Yes |

Note: ES = Exhaustive Search, CH = Construction Heuristic, LS = Local Search (Metaheuristic). Rating scale: 0/5 (worst) to 5/5 (best). Source uses a visual icon format; numeric equivalents reconstructed from table content.

This table is the primary reference when the thesis discusses why Construction Heuristics alone are insufficient for large instances, and why Timefold's Local Search achieves both scalability and near-optimal quality.

### Phase Sequence Architecture (§2.2)

The solver runs phases in sequence. Each phase is an optimization algorithm:

| Phase order | Typical algorithm | Purpose |
|---|---|---|
| Phase 1 | Construction Heuristic (e.g., First Fit Decreasing) | Initialize a feasible (possibly suboptimal) solution |
| Phase 2+ | Local Search (e.g., Late Acceptance, Tabu Search) | Iteratively improve the solution |

Termination can be configured per-phase or at Solver level. The solver terminates after all phases complete or if the Solver-level termination fires first.

## Key arguments / lines of reasoning

### Argument: Exact methods are infeasible for real-world planning problems
- **Premiss 1:** Real planning problems have search spaces on the order of 10^100+ possible solutions.
- **Premiss 2:** Even with pruning (Branch and Bound), checking all possibilities would take billions of years.
- **Premiss 3:** Optimal solutions cannot be found reliably within operational time constraints.
- **Konklusjon:** Metaheuristics that find the best solution in available time are the practical alternative.
- **Sted:** §1.1–1.2
- **Hvilke claims dette støtter:** Ch 2.1 ¶4, Ch 4.5 ¶2

### Argument: Small-dataset quality does not generalise to production scale
- **Premiss 1:** NP-complete problem complexity scales super-polynomially with instance size.
- **Premiss 2:** "The quality of a result from a small data set is no indication of the quality of a result from a large data set."
- **Konklusjon:** Algorithm validation must use production-sized datasets.
- **Sted:** §1.2
- **Hvilke claims dette støtter:** Ch 4.5 ¶5–6, Ch 5.6 ¶2

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| N-queens problem (4, 5, 8, 64 queens) | Exponential growth of search space — 64 queens has >10^115 solutions | §1.1 |
| N-queens change moves | How moves (incremental changes) form the neighbourhood of a solution | §3.1 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 64-queens search space | >10^115 possible solutions | General / illustrative | §1.1 |
| Atoms in known universe (for comparison) | ~10^80 | Reference point for scale | §1.1 |

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Benchmarker | Timefold's tool for comparing algorithm configurations on a specific use case | §1.4, §2.1 |
| Score calculation engine | Component that evaluates solution quality; combined with optimization algorithm | §2 intro |
| Incremental score calculation | Score is updated incrementally (deltas) after each Move, not recalculated from scratch | §2 intro |
| DiminishedReturns termination | Terminates when rate of improvement drops below a threshold; hardware-independent | §2.4.1, §2.4.4 |
| Time gradient | A ratio used by time-based algorithms (e.g., Simulated Annealing) to schedule cooling schedule | §2.4 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "An algorithm that checks every possible solution (even with pruning, such as in Branch And Bound) can easily run for billions of years on a single real-life planning problem." | §1.1 | Ch 2.1 ¶4 — motivating heuristics over exact methods |
| "Therefore, Timefold Solver focuses on finding the best solution in available time." | §1.2 | Ch 4.5 ¶2 — justifying the Timefold engine's design |
| "In practice, Metaheuristics (in combination with Construction Heuristics to initialize) are the recommended choice" | §1.3 | Ch 2.1 ¶5 / Ch 4.5 ¶2 — algorithm family justification |
| "The quality of a result from a small data set is no indication of the quality of a result from a large data set." | §1.2 | Ch 4.5 ¶5–6 / Ch 5.6 ¶2 — benchmarking limitation |
| "Scaling issues cannot be mitigated by hardware purchases later on." | §1.2 | Ch 2.1 ¶4 — algorithm choice over hardware as the key variable |
| "For the best experience overall, we recommend using the Diminished Returns termination." | §2.4.1 | Ch 4.5 ¶2 — if Ressursplanlegger uses this termination |

## Hva kilden IKKE sier

- **Does not compare Timefold vs. CP-SAT (Google OR-Tools):** The algorithm table covers Timefold's own algorithm families only. Claims about how Timefold compares to CP-SAT for our specific problem must come from benchmarking results (Ch 4.5 ¶6), not from this source.
- **Does not provide performance benchmarks for driver/vehicle assignment:** All examples use N-queens. No data for fleet sizes (20–100 drivers, 50–500 assignments).
- **Does not cover constraint modelling (hard/soft constraints):** This page covers optimization algorithms, not how to model planning constraints. For constraint definitions and scoring, see the Timefold constraint documentation or our own algorithm.md.
- **Does not address the human-in-the-loop design pattern:** Nothing about coordinator interaction, trust, or the "suggest + approve" workflow — that is Ch 2.2 territory.
- **Does not make claims about tabu search as a theoretical concept:** For the theoretical grounding of tabu search, cite `\textcite{glover1986future}`. This source documents that Timefold implements tabu search but does not define or analyse it theoretically.
- **MUST CITE marker (Ch 4.5 ¶2) confirmed:** The marker points to `timefold2026solver` for justifying the chosen approach. This source supports that use (§1.2–1.4, §2.2). Fit confirmed.

## Forfatter-perspektiv / metodologi

This source is official vendor documentation authored by the Timefold team. It is authoritative for "what the solver does and how to configure it" but reflects the vendor's perspective and should not be treated as independent evaluation. Use for engineering justification and algorithm description, not for theoretical claims.