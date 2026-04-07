# Optimisation Algorithm — Ressursplanlegger

> **Owner: Embret** — filled based on actual implementation.
> Used when writing Chapter 4.5 (Optimisation Algorithm) and Chapter 5.2 (Algorithm and Human Override).

---

## Overview

The system uses a pluggable multi-engine architecture. Three solvers are available and can be selected at runtime:

| Engine | Technology | Use case |
|--------|-----------|----------|
| Greedy | Python (custom) | Fast baseline; suitable for demos and small instances |
| OR-Tools CP-SAT | Python + Google OR-Tools | Near-optimal; suitable for daily planning (up to ~500 assignments) |
| Timefold | Java (Timefold Solver) | Metaheuristic; suitable for large or multi-day instances |

All three engines are invoked as subprocesses from the Node.js backend. The problem is serialised to JSON and passed via stdin; the solution is read from stdout. This keeps the algorithm code independent of the TypeScript runtime.

---

## Problem Formulation

**Input:** A set of assignments, a set of employees, a set of vehicles, and a set of constraints — all scoped to a planning date.

**Output:** For each assignment, a suggested employee and vehicle (or a violation record if no feasible assignment exists).

### Variables
- `assign[i][j][k]` — Boolean: is assignment `i` assigned to employee `j` with vehicle `k`?

### Hard Constraints (must be satisfied)
| ID | Constraint |
|----|-----------|
| HC-01 | An employee must possess all competencies required by the assignment |
| HC-02 | An employee must be available (within work schedule, not on time-off, not already assigned) |
| HC-03 | A vehicle must be in active status (not under maintenance or out-of-service) |
| HC-04 | The vehicle type must match the assignment's required vehicle type |
| HC-05 | No employee may be double-booked (two concurrent assignments) |
| HC-06 | No vehicle may be double-booked |

### Soft Constraints (penalty-based, weighted)
| ID | Constraint | Weight |
|----|-----------|--------|
| SC-01 | Prefer to assign an employee their designated vehicle | 10 |
| SC-02 | Balance workload evenly across employees | 20 |
| SC-03 | Minimise transitions / travel between consecutive assignments for the same employee | 5 |
| SC-04 | Schedule high-priority assignments before lower-priority ones | 15 |
| SC-05 | Respect stated employee preferences | 10 |

---

## Greedy Solver (`engines/greedy/solver.py`)

**Approach:** Priority-sorted greedy assignment.

```
1. Sort assignments by priority (high → medium → low)
2. For each assignment in sorted order:
   a. Collect employees whose competencies satisfy the assignment's requirements
   b. Filter by availability (work schedule, time-off, not already occupied)
   c. Among remaining candidates, select the employee with the lowest current workload
   d. Assign the first available compatible vehicle of the required type
   e. Mark the employee and vehicle as occupied for the assignment's time slot
3. Return all assignments with their suggested employee/vehicle, plus a list of
   any assignments that could not be scheduled (violations)
```

**Complexity:** O(n × m) where n = number of assignments, m = number of employees.
**Optimality:** None guaranteed — greedy selection may block optimal solutions found later.
**When to use:** Real-time feedback during coordinator session; instant response.

---

## OR-Tools CP-SAT Solver (`engines/ortools_engine/solver.py`)

**Approach:** Constraint Programming — Satisfiability (CP-SAT), a complete solver with an objective.

```
1. Model hard constraints as Boolean clauses (must_satisfy = True)
2. Model soft constraints as terms in a maximisation objective function
3. Run Google CP-SAT solver with a configurable time limit (default: 60 seconds)
4. Extract the best feasible solution found within the time limit
5. Return assignments with employee/vehicle suggestions and a solution score
```

**Formulation:**
- One Boolean variable per (assignment, employee, vehicle) triple
- Exactly-one constraints: each assignment is assigned to at most one (employee, vehicle) pair
- Mutex constraints: each employee and each vehicle appears in at most one assignment per time slot
- Objective: maximise the weighted sum of soft constraint satisfactions

**Solver internals:** Guided local search with symmetry breaking and clause learning (CDCL-style).
**Time limit:** 60 seconds by default; configurable.
**Quality:** Typically near-optimal for instances with up to ~500 assignments and ~100 employees.
**When to use:** Standard daily planning run.

---

## Timefold Solver (`engines/timefold/solver.jar`)

**Approach:** Metaheuristic optimisation (Java, Apache Timefold).

**Techniques used:** Tabu search, simulated annealing, and late-acceptance hill climbing.
**Time limit:** Configurable; can run for hours for very large instances.
**Strengths:** Handles instances with 1000+ assignments or multi-day horizons; supports incremental solving (warm-start from an existing plan).
**Deployment:** Compiled as a `.jar`; spawned as a subprocess by the Node.js backend.
**When to use:** Weekly or multi-day planning; large fleets (>100 vehicles).

---

## Engine Selection and Integration

**Location:** `src/optimization/client.ts`, `src/server/api/routers/optimization.ts`

The coordinator selects an engine via the UI. The backend:
1. Fetches all assignments, employees, vehicles, and constraints for the selected date
2. Serialises the problem as JSON
3. Spawns the selected engine subprocess (`python solver.py` or `java -jar solver.jar`)
4. Passes the JSON problem via stdin
5. Reads the JSON solution from stdout
6. Scores the solution using `src/optimization/scorer.ts`
7. Returns the solution to the frontend for coordinator review

Engine source code snapshots (zip + git hash) are saved for reproducibility.

---

## Scoring (`src/optimization/scorer.ts`)

After a solution is returned, it is evaluated:

```
score = {
  total:        hardScore + softScore,
  hardScore:    0 if all hard constraints satisfied, else negative (count of violations),
  softScore:    weighted sum of satisfied soft constraints,
  breakdown: {
    scheduledPercentage:  (assignments with a suggestion / total) × 100,
    violationPenalty:     sum of hard constraint violation counts,
    workloadBalanceScore: normalised standard deviation of employee workloads,
    priorityScore:        fraction of high-priority assignments successfully scheduled
  }
}
```

A solution with `hardScore < 0` contains infeasible assignments; the coordinator is shown the violations explicitly.

---

## Benchmark Datasets (`benchmarks/`)

Three synthetic datasets for performance testing:

| Dataset | Assignments | Employees | Vehicles |
|---------|------------|-----------|---------|
| small.json | ~20 | ~10 | ~8 |
| medium.json | ~100 | ~40 | ~30 |
| large.json | ~500 | ~150 | ~100 |

Benchmarks record: solve time, number of scheduled assignments, number of violations, and solution score.

---

## Conflict Detection (`src/server/api/routers/deviation.ts`)

After a plan is saved, the system runs automated conflict detection. Detected violation types:

| Code | Description |
|------|-------------|
| `incomplete` | Assignment has no employee or vehicle |
| `overbooking` | Employee assigned to two concurrent assignments |
| `overtime` | Employee's assigned hours exceed working-hours limit |
| `missing_competence` | Employee lacks a required competency |
| `night_work` | Assignment extends into restricted night-work hours |
| `certification_expired` | Employee's required certification has expired |
| `vehicle_maintenance` | Assigned vehicle is under maintenance |
| `rest_period_violation` | Insufficient rest between consecutive assignments |

Violations are surfaced in the Deviations view (`/avvik`) and as inline warnings on the planning timeline.
