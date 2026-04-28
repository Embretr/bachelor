# Theoretical Framework — Ressursplanlegger

> **Owner: Mikael** — fill in before writing Chapter 2.
> For each theory: what is it, and how does it connect to Ressursplanlegger specifically.
> This file provides the raw material for Chapter 2 (Theory). The thesis text should
> expand on these summaries with proper citations and deeper analysis.

---

## Vehicle Routing Problem (VRP)

**What it is:**
The Vehicle Routing Problem is a combinatorial optimisation problem in operations research. Given a set of customers (each with a demand) and a fleet of vehicles based at one or more depots, the objective is to find a set of routes that serves all customers while minimising total cost — typically distance, time, or number of vehicles used. First formulated by Dantzig and Ramser (1959) as a generalisation of the Travelling Salesman Problem.

**Relevant variants:**
- **VRPTW (VRP with Time Windows)** — each customer must be visited within a defined time window. Most directly relevant to Ressursplanlegger, where assignments have start and end times.
- **CVRP (Capacitated VRP)** — vehicles have a maximum capacity. Relevant when vehicle type and load requirements constrain assignment.
- **Multi-depot VRP** — vehicles are based at multiple depots. Relevant for companies with multiple departments (e.g., Ottem with 3 divisions).
- **Heterogeneous fleet VRP** — vehicles have different capabilities. Maps to the real-world constraint that different vehicle types (truck, van, crane) are suited to different assignments.

**How it connects to Ressursplanlegger:**
The daily planning problem in Ressursplanlegger can be formulated as a variant of the VRP. "Customers" are assignments that need to be served; "vehicles" are the combination of a driver and a physical vehicle; the "cost" is a composite function balancing workload, priority coverage, and constraint satisfaction. However, Ressursplanlegger's problem is not a pure VRP — it focuses on resource assignment (who does what) rather than route sequencing (in which order), since individual assignments have fixed locations and times. The problem is more precisely a resource-constrained scheduling problem with VRP-like constraints.

**Key sources (bibkeys, all `approved-read`):**
- `dantzig1959truck` — Dantzig & Ramser (1959). The Truck Dispatching Problem. *Management Science*, 6(1), 80–91. (Kanonisk opphav.)
- `braekers2016vrp` — Braekers, Ramaekers & Van Nieuwenhuyse (2016). The Vehicle Routing Problem: State of the Art Classification and Review. *Computers & Industrial Engineering*, 99, 300–313. (Moderne taxonomy for VRPTW, CVRP, heterogeneous fleet.)

---

## Resource Scheduling

**What it is:**
Resource scheduling is the problem of assigning a set of limited resources (people, machines, vehicles) to a set of tasks over time, subject to constraints on resource availability, task requirements, and temporal dependencies. It is a fundamental problem in operations research, manufacturing, project management, and logistics. The field encompasses job-shop scheduling, nurse scheduling, crew scheduling, and vehicle/driver assignment — all of which share the structure of matching resources to tasks under constraints.

**How it connects to Ressursplanlegger:**
The core function of Ressursplanlegger is resource scheduling: assigning employees (drivers) and vehicles to assignments (transport jobs) for a given day. The problem involves:
- **Resource constraints:** driver competencies, licence classes, availability, working hours
- **Task requirements:** vehicle type, required competencies, time window, priority
- **Objective:** maximise coverage and balance while respecting all hard constraints
- **Temporal dimension:** assignments have fixed time slots; drivers cannot be double-booked

This is a multi-resource scheduling problem (each assignment requires both an employee and a vehicle), which increases combinatorial complexity compared to single-resource scheduling.

**Key sources:**
- Pinedo, M. L. (2016). *Scheduling: Theory, Algorithms, and Systems* (5th ed.). Springer.
- [FILL IN — crew scheduling / driver scheduling literature]
- [FILL IN — nurse scheduling as analogous domain (relevant for constraint handling)]

---

## Human-in-the-Loop (HITL) Automation

**What it is:**
Human-in-the-loop refers to a system design pattern where an automated process produces a recommendation or plan, but a human reviews, adjusts, and approves the output before it takes effect. The human retains decision authority; the algorithm serves as decision support, not decision maker. HITL systems occupy the middle ground between fully manual processes and full automation.

**Why it matters for Ressursplanlegger:**
Interview findings show a clear consensus: traffic coordinators do not want full automation of the assignment process. Even the most positive respondents (Norlog Lakselv, Mo i Rana, Tana) want the ability to review and correct the algorithm's output. Sceptical respondents (Ottem, Bergen Bulk Transport) explicitly require full manual control as a precondition for adoption. The reasons are rooted in the nature of transport operations:
- **Unpredictability:** Weather, road conditions, last-minute cancellations, and customer preferences create situations the algorithm cannot anticipate.
- **Tacit knowledge:** Coordinators know things that are difficult to formalise — which drivers work well with which customers, which routes are problematic in winter, which drivers prefer certain schedules.
- **Trust:** Coordinators will not adopt a system whose decisions they cannot understand, verify, and override.

**Design implication:**
Ressursplanlegger implements HITL as its core interaction pattern: the algorithm generates a suggested plan, the coordinator reviews it (with conflicts highlighted), makes manual adjustments, and approves the final version. This is the "suggest + override" pattern — the algorithm does the heavy lifting, the human applies judgment.

**Levels of automation (Parasuraman, Sheridan & Wickens, 2000):**
Ressursplanlegger operates at approximately level 5–6 on the 10-level automation scale proposed by Parasuraman, Sheridan and Wickens (which extends and formalises the original Sheridan & Verplank 1978 scale): the system generates a plan and presents it for approval, but the coordinator can modify any part before execution.

**Key sources (bibkeys, all `approved-read`):**
- `parasuraman2000automation` — Parasuraman, Sheridan & Wickens (2000). A Model for Types and Levels of Human Interaction with Automation. *IEEE TSMC-A*, 30(3), 286–297. (Primær HITL-taxonomi.)
- `lee2004trust` — Lee & See (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*, 46(1), 50–80. (Calibrated trust / appropriate reliance.)
- `hoff2015trust` — Hoff & Bashir (2015). Trust in Automation: Integrating Empirical Evidence. *Human Factors*, 57(3), 407–434. (Moderne tillit-syntese.)
- `bainbridge1983ironies` — Bainbridge (1983). Ironies of Automation. *Automatica*, 19(6). (Deskilling / automation-paradoks.)
- `amershi2019guidelines` — Amershi et al. (2019). Guidelines for Human-AI Interaction. *CHI 2019*. (Design-guidelines for suggest+override.)
- `miller2019explanation` — Miller (2019). Explanation in AI. *Artificial Intelligence*, 267. (XAI-fundament.)

---

## Transport Management Systems (TMS)

**What it is:**
A Transport Management System is software used by logistics and transport companies to plan, execute, and monitor the movement of goods. TMS functionality typically includes order management, route planning, carrier management, freight billing, and reporting. In practice, many TMS solutions focus on order/invoice management rather than on the operational planning of who drives what.

**Existing systems in the Norwegian context:**

| System | Used by | Strengths | Key limitations |
|--------|---------|-----------|-----------------|
| Timpex | Norlog Lakselv, Norlog Mo i Rana | Established, handles invoicing, driver notification via Timpex Confirm app | Extremely slow with concurrent users; no optimisation; no capacity overview |
| Trimtex | Norlog Tana | Handles basic order management | Slow; limited features; no planning support |
| Opptur | Harlem Solutions | Order and invoicing | Primarily a billing tool, not a planning tool |
| Custom systems | Ottem, Nordic Crane | Tailored to own operations | No standardisation; difficult to maintain; no optimisation |
| None | Bergen Bulk Transport | — | Fully manual — phone calls, memory, no system at all |

**Gap Ressursplanlegger addresses:**
None of the systems above include optimisation-based plan generation, structured decision support for driver assignment, or automated conflict detection. They are containers for orders and invoices — the actual assignment of drivers to jobs is always a manual, knowledge-dependent process performed by the traffic coordinator. Ressursplanlegger targets precisely this gap: the space between "order exists" and "driver is assigned."

**Key sources:**
- [FILL IN — TMS industry overview or academic review]
- [FILL IN — literature on digitalisation in Norwegian transport/logistics, if available]

---

## Constraint Programming and Optimisation Solvers

**What it is:**
Constraint Programming (CP) is a paradigm for solving combinatorial problems by defining variables, domains, and constraints, then using a solver to find assignments that satisfy all constraints while optimising an objective function. CP-SAT (Constraint Programming with Boolean Satisfiability) combines constraint propagation with SAT-solving techniques, enabling efficient solutions to problems with thousands of variables.

**How it connects to Ressursplanlegger:**
Ressursplanlegger uses three solver approaches that represent different points on the speed–quality tradeoff:

| Solver | Technique | Speed | Quality | Use case |
|--------|-----------|-------|---------|----------|
| Greedy | Priority-sorted first-fit | Instant | No optimality guarantee | Real-time feedback, demos |
| OR-Tools CP-SAT | Constraint programming with SAT | Seconds–minutes | Near-optimal | Standard daily planning |
| Timefold | Metaheuristic (tabu search, simulated annealing) | Minutes–hours | High quality for large instances | Large fleets, multi-day |

This multi-engine approach is itself a design contribution — it allows benchmarking and comparison, and gives the coordinator a choice between speed and solution quality.

**Key sources:**
- Rossi, F., van Beek, P., & Walsh, T. (Eds.). (2006). *Handbook of Constraint Programming*. Elsevier.
- Google OR-Tools documentation: [reference as software, not academic source]
- Timefold Solver documentation: [reference as software]
- [FILL IN — CP-SAT specific papers if needed for depth]

---

## Design Science Research (DSR)

**What it is:**
Design Science Research is a research methodology in information systems that focuses on creating and evaluating artefacts (systems, models, methods) to address practical problems. The research contribution is dual: the artefact itself and the design knowledge generated through building and evaluating it. DSR provides a structured process from problem identification through evaluation and communication.

**How it connects to this thesis:**
Ressursplanlegger is the artefact. The research question asks whether an algorithm-driven platform can support traffic coordinators — answering this requires building the platform (design) and evaluating it against real-world needs (evaluation). DSR provides the methodological framework for treating this build-and-evaluate process as rigorous research.

See `context/docs/method/research-design.md` for the detailed application of DSR phases to this project.

**Key sources:**
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.

---

## Summary: How the Theories Connect

```
Problem domain                    Solution domain
─────────────────                 ─────────────────
VRP / Resource Scheduling    →    Algorithm design (greedy, CP-SAT, Timefold)
Human-in-the-Loop            →    Suggest + override interaction pattern
TMS landscape gaps           →    Ressursplanlegger as a new category of tool
DSR methodology              →    Framework for building and evaluating the artefact
```

The theoretical framework positions Ressursplanlegger at the intersection of operations research (VRP, scheduling), human-computer interaction (HITL automation), and information systems (TMS, DSR). The system is theoretically grounded in optimisation but practically designed around the finding that human judgment remains essential in transport planning.
