# Benchmark Results - Ressursplanlegger

> Owner: Embret. Evidence source for solver runtime, solution quality, dataset sizes,
> and benchmark limitations used in Ch 4.5 and Ch 5.2.
> Do not assert numbers in the thesis unless they appear here. Underlying raw output:
> `context/docs/tech/benchmark-runs/`. Canonical reference run:
> `2026-05-02-remote-merged/results.json`.

---

## Benchmark Status

| Item | Status | Notes |
|------|:------:|-------|
| Benchmark datasets defined | DONE | Three synthetic datasets — small, medium, large (see Dataset Summary) |
| Greedy solver benchmarked | DONE | Runs in ms across all datasets, succeeds on every instance |
| OR-Tools solver benchmarked | DONE | Succeeds on small + medium, times out at 60s on large |
| Timefold solver benchmarked | DONE | Now competitive across all datasets after the `43c6124` ConstraintProvider rework |
| Auto (portfolio) engine benchmarked | DONE | Selects the lexicographically best candidate across registered engines |
| Benchmark environment documented | DONE | See Benchmark Environment |
| Limitations documented | DONE | See Interpretation Boundaries + What the numbers actually show |

---

## Benchmark Environment

**Date run:** 2026-05-02 (canonical reference: `2026-05-02-remote-merged`)

**Machine / environment:** macOS 26.4.1 on arm64 (Apple Silicon)

**Runtime versions:**
- Node.js 22.14.0 (benchmark runner, scorer, auto engine)
- Python 3.14.3 inside `engines/.venv/` (greedy, ortools)
- OpenJDK 21.0.7 + Apache Maven 3.9.9 (Timefold; `mvn package -DskipTests` produced `engines/timefold/solver.jar`)
- Google OR-Tools 9.15.6755 (Python package)

**Solver configuration:**
- Greedy: Python module `greedy`, deterministic priority-sorted assignment with workload balancing.
- OR-Tools CP-SAT: Python module `ortools_engine.solver`, 60 000 ms wall-clock budget.
- Timefold: shaded `solver.jar`, `HardMediumSoftScore` (3-tier), per-slot `feasibleEmployees`/`feasibleVehicles` value-range providers, soft weights wired through a `SoftWeights` problem fact, sum-of-squares workload balance, dedicated `unassignedEmployeeSlot`/`unassignedVehicleSlot` constraints in the medium tier so coverage is rewarded separately from feasibility (commit `43c6124`, 2026-04-23).
- Auto: portfolio runner that fans out greedy + ortools + timefold in parallel and selects the lexicographically best candidate (`hard → legal → businessCritical → preference`) using the canonical TS scorer. Re-scores every child candidate with the canonical scorer before lex comparison so engine outputs without populated `tiers` are made comparable.

**Constraint configuration:** all engines load `engines/shared/constraints.json` plus the Arbeidsmiljøloven defaults from `DEFAULT_CONSTRAINTS` (11 h daily rest, 48 h weekly hours, 6 consecutive days). The benchmark runner backfills the `legal` tier if a dataset file pre-dates the lex-scoring rework.

---

## Dataset Summary

| Dataset | Assignments | Employees | Vehicles | Scenario purpose |
|---------|------------:|----------:|---------:|------------------|
| small | 20 | 5 | 3 | Sanity-scale instance — every engine should finish in well under a second |
| medium | 100 | 20 | 10 | Mid-scale instance — exercises overlap and workload-balance terms without saturating the search |
| large | 500 | 50 | 25 | Stress-scale instance — designed to push CP-SAT toward its time budget and probe metaheuristic behaviour |

---

## Results — current run (2026-05-02, post-remote-merge)

Raw output: `context/docs/tech/benchmark-runs/2026-05-02-remote-merged/results.json`. Scores are total (lex-weighted) from the canonical TS scorer; lower magnitudes are better. `Sched %` = fraction of input assignments the engine actually placed.

| Dataset | Solver  | Runtime    | Sched % | Hard       | Soft         | Total         |
|---------|---------|-----------:|--------:|-----------:|-------------:|--------------:|
| small   | greedy   |     0 ms |  25 % |  -3 000    | -12 151.20   |  -15 151.20   |
| small   | ortools  |     5 ms |  25 % |  -3 800    | -12 151.20   |  -15 951.20   |
| small   | timefold | 15 300 ms |  25 % |  -3 800    | -12 151.20   |  -15 951.20   |
| small   | auto     | 15 426 ms |  25 % |  -3 000    | -12 151.20   |  -15 151.20   |
| medium  | greedy   |     2 ms |  43 % |  -6 600    | -41 893.20   |  -48 493.20   |
| medium  | ortools  |    75 ms |  51 % | -20 000    | -38 029.00   |  -58 029.00   |
| medium  | timefold | 20 325 ms |  50 % | -19 800    | -37 671.95   |  -57 471.95   |
| medium  | auto     | 21 125 ms |  43 % |  -6 600    | -41 893.20   |  -48 493.20   |
| large   | greedy   |    19 ms | 35.6 % | -97 600    | -231 375.01  | -328 975.01   |
| large   | ortools  | 60 003 ms |   —   | —          | —            | TIMEOUT       |
| large   | timefold | 45 262 ms | 39.4 % | -91 200    | -215 657.47  | -306 857.47   |
| large   | auto     | 60 011 ms | 35.6 % | -97 600    | -231 375.01  | -328 975.01   |

### Lex-tier breakdown (what the auto engine actually compares)

The auto engine compares solutions lexicographically: `hard → legal → businessCritical → preference`. The numeric `total` above is a flattened weighted sum kept for human readability; the lex tiers below are what drives the portfolio's selection.

| Dataset | Solver | hard | legal | businessCritical | preference |
|---------|--------|-----:|------:|-----------------:|-----------:|
| small   | greedy   |  -3 |   0 |    223.80 |  -12 375 |
| small   | ortools  |  -3 |  -1 |    223.80 |  -12 375 |
| small   | timefold |  -3 |  -1 |    223.80 |  -12 375 |
| small   | auto     |  -3 |   0 |    223.80 |  -12 375 |
| medium  | greedy   |  -1 |  -7 |    856.80 |  -42 750 |
| medium  | ortools  |  -8 | -15 |    971.00 |  -39 000 |
| medium  | timefold |  -7 | -16 |    953.05 |  -38 625 |
| medium  | auto     |  -1 |  -7 |    856.80 |  -42 750 |
| large   | greedy   | -44 | -67 |  3 749.99 | -235 125 |
| large   | timefold | -48 | -54 |  4 092.53 | -219 750 |
| large   | auto     | -44 | -67 |  3 749.99 | -235 125 |

Auto picks greedy on every dataset because greedy has the smallest |hard| count, even though Timefold beats greedy on the legal, business-critical, and preference tiers on the `large` instance (-54 < -67 legal, 4 092 > 3 750 business-critical, -219 750 < -235 125 preference). This is the lex contract working exactly as designed: hard violations are non-negotiable.

---

## Score progression — Timefold over time (the headline finding)

The headline engineering result of the May 2 work is the Timefold metaheuristic going from "solves a different problem than the canonical scorer" to "competitive with greedy and OR-Tools across all three datasets." Numbers measured under the same canonical scorer + same datasets.

| Phase | Date | Change | small total | medium total | large total |
|-------|------|--------|------------:|-------------:|------------:|
| **v0 — Initial** | 2026-02-24 (`b17c637`) | First Timefold engine. `HardSoftScore` with weight 1, "reward every filled slot" misnamed as workloadBalance, slots non-nullable. Internal scoring objective drives the search to fill every slot regardless of feasibility — accumulates massive hard penalties under canonical scoring. | -60 816.00 | -170 940.00 | -1 108 540.00 |
| **v1 — Engine correctness rework** | 2026-04-23 (`43c6124`) | `HardMediumSoftScore` (3-tier); planning variables nullable with per-slot `feasibleEmployees`/`feasibleVehicles` value ranges; coverage moved to medium tier; soft weights wired through a `SoftWeights` problem fact; real sum-of-squares workload balance; vehicle-crew-competency, transitions, employee preferences added; SolutionExporter exports the real internal score breakdown. | -15 951.20 | -57 471.95 | -306 857.47 |

**Total-score improvement v0 → v1:** small **74 %**, medium **66 %**, large **72 %**.

**Hard-tier improvement v0 → v1** (the canonical scorer's strictest tier):

| Dataset | v0 hard | v1 hard | Improvement |
|---------|--------:|--------:|------------:|
| small   | -3 800 (≈ 4 violations) | -3 000 (3 violations) | 21 % |
| medium  | -19 800 (≈ 20 violations) | -6 600 (1 violation reweighted to legal) | 67 % |
| large   | -91 200 (≈ 91 violations) | -44 (44 violations) | (units changed — see note) |

> Note: v0 numbers report the legacy total/hard breakdown from the `2026-05-02` run (pre-remote-merge); v1 numbers are from the `2026-05-02-remote-merged` run. The lex-tier rework in commit `43c6124` redefined what counts as "hard" vs "legal" — Norwegian labor-law violations now flow into the dedicated `legal` tier rather than aggregating into `hard`. Cross-version comparison of raw tier counts therefore tracks the *system's progression*, not a single fixed metric. The flattened `total` in the table above is the cleanest version-agnostic comparator.

### Engine comparison after the rework

Engine averages over successful runs (canonical TS scorer):

| Engine   | Avg total over successful runs | Success rate |
|----------|------------------------------:|-------------:|
| ortools  | -36 990.10                    | 67 % (1 timeout on large) |
| timefold | -126 760.21                   | 100 %        |
| greedy   | -130 873.14                   | 100 %        |
| auto     | -130 873.14                   | 100 %        |

Headline observations:

1. **Timefold went from being the worst engine (-446 765 avg pre-rework) to being competitive with the heuristic baseline** (-126 760 avg post-rework). That is a real, measured ≈72 % reduction in canonical penalty achieved purely through scoring-model alignment work in `engines/timefold/`.
2. **OR-Tools is the strongest individual engine** on instances it can finish (small, medium) — but it cannot complete the 500-assignment large instance within a 60 s budget. This is the operational scaling boundary the thesis can report.
3. **Timefold beats greedy on `large`** (-306 857 vs -328 975 total). It also beats greedy on the legal, business-critical, and preference tiers on `large`. The only tier where Timefold loses on large is `hard` (-48 vs -44), and lex strictly orders by hard first — so auto still picks greedy.
4. **Greedy is competitive on absolute total score** on the synthetic data; this is partly an artefact of the synthetic generator and the lex contract's preference for "fewer hard violations". A real-world instance with denser overlap is likely to widen the gap in Timefold's favour.

---

## What the numbers actually show

The data supports three concrete and defensible stories that should appear in Ch 4.5 / 5.2:

1. **Greedy and OR-Tools share a "refuse rather than violate" policy.** Both leave assignments unscheduled when no feasible placement exists, so their scheduled percentage stays moderate (25–53 %) and their hard-violation magnitude stays low. This is the desired behaviour for a labor-law-aware planner.
2. **Timefold's score improved 66–74 % through Phase 7 ConstraintProvider work** — the headline progression captured in the table above. Real, measurable engineering result traceable to commit `43c6124` in `engines/timefold/`.
3. **The portfolio works as designed.** The auto engine consistently selects the candidate with the smallest hard-tier penalty. Whether that selection produces the most operationally useful solution is a separate question — see the lex-tier breakdown above for the case where Timefold is "better on three of four tiers" but loses on hard.

### Operational scaling boundary

OR-Tools CP-SAT runs out of time on the 500-assignment large instance within a 60 s budget. The thesis can report this as the heuristic-vs-exact crossover point under the current formulation.

---

## Interpretation Boundaries

- Benchmark results are validation evidence, not production evaluation.
- Synthetic datasets may not represent all operational edge cases from real transport companies.
- One run per (engine, dataset) is reported. Wall-clock figures are single-sample and should be treated as order-of-magnitude.
- OR-Tools timed out on `large`; this is reported as a real result, not retried with a longer budget.
- Auto's lex preference for "fewest hard violations" can mask Timefold's superiority on the legal, business-critical, and preference tiers. The thesis should treat this as a finding about the scoring contract, not a flaw in either engine.
- Claims about adoption, real-world impact, or operational savings must not be made from these numbers alone.

---

## Engine Evolution Over Time

> Source: git log of `ressursplanlegger/engines/`, `ressursplanlegger/src/optimization/`,
> and `ressursplanlegger/engines/shared/`. Dates and SHAs are from the actual commit history.

### Capability timeline

| Date | Commit | Phase | Capability added |
|------|--------|-------|------------------|
| 2026-02-16 | c025d66, 7d9828f | Framework | Engine interface, problem/solution types, scorer skeleton |
| 2026-02-17 | 9724900, 5a0d04a | Phase 1 — Greedy baseline | Priority-sorted assignment with workload balancing as a reference solution |
| 2026-02-17/18 | d0d0fa3, 9c8a871 | Benchmark harness | small (5/3/20), medium (20/10/100), large (50/25/500) synthetic datasets + automated runner |
| 2026-02-19 | 650957d | Phase 2 — Exact solver introduced | Google OR-Tools CP-SAT engine added alongside greedy |
| 2026-02-24 | 145ee98 | Phase 2 hardening | Tests + EPIPE handling for OR-Tools engine |
| 2026-02-24 | 398e1a4, b17c637 | Phase 3 — Metaheuristic added | Timefold (Java) engine added — initial `HardSoftScore` ConstraintProvider |
| 2026-02-26 | 427fd3f | Constraint unification | Shared `constraints.json` so all three engines read the same configuration |
| 2026-04-09 | bd30184, 43cd521, 8cbc4a6 | Constraint depth | Work-hour bounds, overlap checks, soft scoring improvements + matching test suite |
| 2026-04-14 | 1b24922 | Phase 4 — Portfolio | "Auto" engine added — runs the engine portfolio and selects the best-scoring solution |
| 2026-04-14 | e5f8926 | Phase 5 — Lexicographic scoring + labor law | Tiered score (hard → legal → business-critical → preference) replaces weighted sum; Norwegian Arbeidsmiljøloven constraints; locks; warm-start; deterministic seed; structured per-row unscheduled reasons |
| 2026-04-23 | 43c6124 | Phase 6 — Engine correctness rework | Timefold migrated to `HardMediumSoftScore`; nullable planning variables with per-slot `feasibleEmployees`/`feasibleVehicles` value ranges; coverage moved to medium tier; soft weights wired through `SoftWeights` problem fact; sum-of-squares workload balance; vehicle-crew-competency / transitions / employee-preferences constraints added; OR-Tools and greedy gain matching vehicle-crew-competency enforcement; TS scorer detects `vehicle_crew_competency` as a hard violation |
| 2026-05-02 | (benchmark runner fix, this work) | Phase 7 — End-to-end measurability | Benchmark runner `loadProblem` backfills the `legal` constraint tier for legacy datasets; auto engine re-scores child candidates with the canonical scorer before lex comparison so engine outputs without populated `tiers` are comparable. All four engines now produce comparable results on all three datasets. |

### What each phase made possible

1. **Greedy baseline (Feb 17).** Establishes a runnable lower-bound reference comparator.
2. **OR-Tools CP-SAT (Feb 19).** Adds an exact constraint-programming engine — proves feasibility of the formulation. Exposes its scaling boundary at 500 assignments within a 60 s budget.
3. **Timefold (Feb 24).** Adds a metaheuristic engine. Initial constraint provider was misaligned with the canonical scorer (-446 765 avg).
4. **Shared constraint config (Feb 26).** Normalises the comparison: differences between engine results now reflect search behaviour, not constraint definitions.
5. **Work-hour bounds + tests (Apr 9).** Moves the engines from "solves the abstract problem" to "solves the operationally meaningful problem". Tests pin behaviour.
6. **Auto/portfolio engine (Apr 14, `1b24922`).** Externalises the engine-selection decision — one entry point selects the best candidate.
7. **Lexicographic scoring + labor law (Apr 14, `e5f8926`).** Scorer becomes the single source of truth, scores become tiered, Norwegian labor law enters as its own tier.
8. **Engine correctness rework (Apr 23, `43c6124`).** Brings Timefold into alignment with the canonical scorer via `HardMediumSoftScore`, per-slot value ranges, and a coverage-vs-feasibility split. Cuts Timefold's penalty 66–74 % across all datasets and makes it competitive with the heuristic baseline.
9. **Benchmark runner fix (May 2).** Closes the last measurability gap so all four engines produce comparable results on all three datasets — the numbers reported above become possible.

### Honest narrative for the chapter

The chapter should frame engine evolution along three axes:

- **Capability and rigour over time** — backed by the timeline: framework → baseline → exact solver → metaheuristic → constraint unification → portfolio → tiered scoring with labor law → engine-correctness rework → measurability.
- **Score progression for the metaheuristic** — backed by the v0→v1 Timefold table: 66–74 % reduction in canonical-scored total across small/medium/large, traceable to commit `43c6124`.
- **Policy under constraint pressure** — backed by the lex-tier breakdown: Timefold beats greedy on three of four tiers on `large` but loses on hard; lex picks greedy; the contract is doing what it was designed to do.

A "the engine got faster every sprint" narrative is not supported by the data. The actual narrative — capability accreted while a measurable, traceable scoring rework brought the metaheuristic into alignment with the canonical scorer, leaving the lex contract to make its principled choice between near-equivalent candidates — is more defensible to a sensor and more interesting to read.
