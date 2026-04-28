# Benchmark Results - Ressursplanlegger

> Owner: Embret. Fill this before writing Chapter 4.5 or Chapter 5.2.
> This file is the evidence source for solver runtime, solution quality, dataset sizes,
> and benchmark limitations. Do not infer numbers in the thesis unless they appear here.

---

## Benchmark Status

| Item | Status | Notes |
|------|:------:|-------|
| Benchmark datasets defined | [FILL IN] | e.g. small, medium, large synthetic datasets |
| Greedy solver benchmarked | [FILL IN] | Runtime, scheduled percentage, violations, score |
| OR-Tools solver benchmarked | [FILL IN] | Runtime, scheduled percentage, violations, score |
| Timefold solver benchmarked | [FILL IN] | Runtime, scheduled percentage, violations, score |
| Benchmark environment documented | [FILL IN] | Machine/runtime versions and relevant limits |
| Limitations documented | [FILL IN] | Synthetic data, no production deployment, incomplete solver coverage |

---

## Benchmark Environment

**Date run:** [FILL IN]

**Machine / environment:** [FILL IN]

**Relevant runtime versions:** [FILL IN]

**Solver configuration:**
- Greedy: [FILL IN]
- OR-Tools CP-SAT: [FILL IN]
- Timefold: [FILL IN]

---

## Dataset Summary

| Dataset | Assignments | Employees | Vehicles | Scenario purpose |
|---------|------------:|----------:|---------:|------------------|
| small | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| medium | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| large | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## Results

| Dataset | Solver | Runtime | Scheduled assignments | Hard violations | Soft score | Notes |
|---------|--------|--------:|----------------------:|----------------:|-----------:|-------|
| small | greedy | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| small | ortools | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| small | timefold | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| medium | greedy | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| medium | ortools | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| medium | timefold | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| large | greedy | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| large | ortools | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| large | timefold | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

---

## Interpretation Boundaries

- Benchmark results are validation evidence, not production evaluation.
- Synthetic datasets may not represent all operational edge cases from real transport companies.
- If a solver was implemented but not fully benchmarked, the thesis must state this explicitly.
- Claims about adoption, real-world impact, or operational savings must not be made from these numbers alone.
