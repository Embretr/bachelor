# Scheduling: Theory, Algorithms, and Systems (`pinedo2016scheduling`)

## Status
- [x] Notes generated from raw on 2026-04-28
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [ ] Coverage complete — all CITATIONS.md claims for this source dekket

## Source metadata
- **BibTeX key:** `pinedo2016scheduling`
- **Reference (APA 7):** Pinedo, M. L. (2016). *Scheduling: Theory, algorithms, and systems* (5th ed.). Springer. https://doi.org/10.1007/978-3-319-26580-3
- **Tilgang:** PDF (NTNU Oria / Springer eBook)
- **Raw source:** `raw/pinedo2016scheduling.pdf` (674 PDF pages, ~670 printed pages)
- **Coverage in raw:** Front matter (pp. vii–xx), Ch 1 (pp. 1–10), Ch 2.4 Complexity Hierarchy (pp. 25–32), Ch 14 General Purpose Procedures for Deterministic Scheduling (pp. 376–393), Appendix D Complexity Theory (pp. 585–598), Appendix E Complexity Classification (pp. 599–602), Appendix F–G partial. Index pass on Subject Index (pp. 665–670). ~108 pages read of 674.

## Sammendrag (2–3 setninger)
Pinedo's textbook is the canonical academic reference for *machine* scheduling theory. It defines scheduling as the allocation of resources to tasks over time to optimise one or more objectives, develops the deterministic and stochastic theory through the αβγ classification, and surveys general-purpose solution procedures (dispatching rules, local search metaheuristics, constraint programming). The book's contribution to this thesis is (a) the formal definition of scheduling as resource allocation under constraints, (b) the complexity-theoretic justification for using heuristics rather than exact methods, and (c) the taxonomy of constructive heuristics (dispatching rules) and improvement heuristics (simulated annealing, tabu search) that informs the multi-engine architecture of Ressursplanlegger.

## Claims-mapping (per CITATIONS.md)

> **Note on CITATIONS.md drift.** The ¶-numbers in CITATIONS.md (last updated 2026-04-23) appear to predate the current `outline.md`. In the current outline, 2.1 has only ¶1–¶5; the old ¶3 NP-hardness claim is now in ¶4, and the old ¶7 greedy claim is folded into ¶4. The mapping below uses CITATIONS.md ¶-numbers but flags the drift.

### Claim: "Resource scheduling defined as assigning limited resources to tasks over time under constraints" (Ch 2.1 ¶1)
- **Sted i kilden:** §1.1 The Role of Scheduling, p. 1; also §1.3 Outline of the Book, p. 7
- **Direkte sitat:**
  > "Scheduling is a decision-making process that is used on a regular basis in many manufacturing and services industries. It deals with the allocation of resources to tasks over given time periods and its goal is to optimize one or more objectives." (p. 1)

  > "The resources and tasks in an organization can take many different forms. The resources may be machines in a workshop, runways at an airport, crews at a construction site, processing units in a computing environment, and so on. The tasks may be operations in a production process, take-offs and landings at an airport, stages in a construction project, executions of computer programs, and so on. Each task may have a certain priority level, an earliest possible starting time and a due date." (p. 1)

  > "Given a collection of jobs requiring processing in a certain machine environment, the problem is to sequence these jobs, subject to given constraints, in such a way that one or more performance criteria are optimized." (p. 7)
- **Parafrase:** Pinedo defines scheduling as a decision-making process that allocates resources (machines, crews, processing units, vehicles) to tasks (operations, take-offs, executions, jobs) over time, with the goal of optimising one or more objectives subject to constraints such as priorities, release dates, and due dates.
- **Forbehold:** Pinedo's framing covers manufacturing and services explicitly; transport scheduling is not named but is clearly within scope (he uses runways/airport gates and crew scheduling as illustrative examples). The phrase "subject to constraints" appears most explicitly on p. 7, not in the headline definition on p. 1 — the writer should cite both pages or paraphrase carefully so as not to attribute the constraint clause to a sentence that does not contain it.

### Claim: "NP-hardness of scheduling motivates heuristics" (Ch 2.1 ¶3 — now ¶4 in current `outline.md`)
- **Sted i kilden:** §2.4 Complexity Hierarchy, p. 26; Appendix D.2, p. 588; Appendix D.4 Approximation Algorithms and Schemes, p. 594; §14.2 Composite Dispatching Rules, p. 378
- **Direkte sitat:**
  > "A significant amount of research in deterministic scheduling has been devoted to finding efficient, so-called polynomial time, algorithms for scheduling problems. However, many scheduling problems do not have a polynomial time algorithm; these problems are the so-called NP-hard problems. Verifying that a problem is NP-hard requires a formal mathematical proof (see Appendix D)." (p. 26)

  > "Definition D.2.3 (NP-hardness). A problem P, either a decision problem or an optimization problem, is called NP-hard if the entire class of NP problems polynomially reduces to P." (p. 588)

  > "Many scheduling problems are either NP-hard in the ordinary sense or strongly NP-hard. For these problems it will be clearly very hard to find an optimal solution in a time effective manner. It is of interest to develop for these problems polynomial time algorithms that can deliver, with some form of a guarantee, solutions close to optimal. This need has led to a significant amount of research in an area that is referred to as Approximation Algorithms or as Approximation Schemes." (p. 594)

  > "As stated in Chapter 3, the 1 || Σ w_j T_j problem is strongly NP-hard. As branch-and-bound methods are prohibitively time consuming even for only 30 jobs, it is important to have a heuristic that provides a reasonably good schedule with a reasonable computational effort." (p. 378)
- **Parafrase:** Many scheduling problems lack polynomial-time algorithms and are NP-hard, which makes finding exact optimal solutions intractable as instance size grows. This intractability is the explicit motivation Pinedo gives for the development of approximation algorithms and heuristics — he frames the entire body of work on dispatching rules, local search, and approximation schemes as a response to NP-hardness.
- **Forbehold:** CITATIONS.md tags the source location as "ch. 4," but Pinedo's Ch 4 is "Advanced Single Machine Models (Deterministic)" and does *not* contain general NP-hardness exposition. The actual locations are §2.4 (p. 26), Appendix D (pp. 585–598), and the motivating paragraph in §14.2 (p. 378). CITATIONS.md should be updated. Pinedo speaks in machine-scheduling terms (jobs on machines), so the writer should phrase the claim as "scheduling problems are NP-hard at scale, motivating heuristics" rather than implying Pinedo addresses the multi-resource driver/vehicle problem of Ressursplanlegger directly.

### Claim: "Greedy heuristics for assignment problems" (Ch 2.1 ¶7 — folded into ¶4 in current `outline.md`)
- **Sted i kilden:** §14.1 Dispatching Rules, p. 376; §14.3 Local Search, p. 382 (definitional contrast); §D.1, p. 587
- **Direkte sitat:**
  > "Research in dispatching rules has been active for several decades and many different rules have been studied in the literature. These rules can be classified in various ways. For example, a distinction can be made between *static* and *dynamic* rules. Static rules are not time dependent. They are just a function of the job and/or of the machine data, for instance, WSPT." (p. 376)

  > "A number of these rules yield optimal schedules in some machine environments and are reasonable heuristics in others. All of these rules have variations that can be applied in more complicated settings." (p. 376)

  > "Dispatching rules are useful when one attempts to find a reasonably good schedule with regard to a single objective such as the makespan, the total completion time, or the maximum lateness." (p. 377)

  > "The heuristics described in the first two sections of this chapter [§14.1 dispatching rules and §14.2 composite dispatching rules] are of the constructive type. They start without a schedule and gradually construct a schedule by adding one job at a time." (p. 382)

  > "Some of the easiest scheduling problems can be solved through a simple priority rule, e.g., WSPT, EDD, LPT, and so on." (p. 587)
- **Parafrase:** Pinedo describes a class of *constructive* heuristics — dispatching rules and composite dispatching rules — that build a schedule incrementally by selecting one job at a time according to a priority index. These rules are computationally cheap, often optimal in simple machine environments, and serve as "reasonable heuristics" in more complex environments. They are explicitly contrasted with *improvement-type* heuristics (simulated annealing, tabu search) that start from a complete schedule and iterate.
- **Forbehold:** Pinedo does **not** use the word "greedy" as a primary technical term in this discussion — the canonical term in his text is **dispatching rule** (constructive heuristic). The "greedy" framing in our outline is closer to combinatorial-optimisation parlance. CITATIONS.md tags the source as "ch. 3," but Ch 3 is "Single Machine Models (Deterministic)" and is about exact algorithms, not greedy heuristics. The relevant location is **Ch 14.1–14.2 (pp. 376–382)**. CITATIONS.md should be updated. The writer should either (a) cite Pinedo for "constructive / dispatching-rule heuristics" using his language, or (b) keep the "greedy" framing but cite Pinedo only as a corroborating reference for the general principle, paired with a primary CO source if needed.

### Claim: "Greedy heuristic for initial assignment" (Ch 4.5 ¶4)
- **Sted i kilden:** Same as previous claim — §14.1 Dispatching Rules, p. 376; §14.3 Local Search (constructive vs improvement), p. 382
- **Direkte sitat:** See preceding claim. The most directly applicable line is:
  > "The heuristics described in the first two sections of this chapter are of the constructive type. They start without a schedule and gradually construct a schedule by adding one job at a time." (p. 382)
- **Parafrase:** Constructive heuristics that build a schedule one job at a time are the textbook category in which Ressursplanlegger's "greedy" engine sits. Pinedo's framing supports the engineering rationale of using such a heuristic to provide a fast, feasible initial assignment that an improvement-type metaheuristic (CP-SAT, Timefold) can then refine.
- **Forbehold:** Same as Ch 2.1 ¶7 above — Pinedo's term is *constructive heuristic / dispatching rule*, not "greedy." When citing Pinedo for the Ressursplanlegger greedy engine, the writer should connect the two terms explicitly (e.g., *"a constructive heuristic of the dispatching-rule type \parencite{pinedo2016scheduling}"*) rather than implying that Pinedo writes about a "greedy" engine.

### Claim: "Hard/soft constraint model, weighted-sum scoring" (Ch 4.5 ¶5 → rossi2006constraint, pinedo2016scheduling)
- **Sted i kilden:** Not found.
- **Direkte sitat:** —
- **Parafrase:** —
- **Forbehold:** **Hypothesis NOT confirmed for pinedo2016scheduling.** The hard-constraint / soft-constraint vocabulary is *not* Pinedo's. Pinedo speaks of "feasibility" (a schedule that violates a constraint is infeasible) and "objective function" / "performance criterion" (the quantity to be optimised), but the explicit hard-vs-soft distinction with weighted-sum aggregation is the constraint-programming / CSP framing developed in Rossi, van Beek & Walsh (2006). **Recommend dropping pinedo2016scheduling from this claim** in CITATIONS.md and citing Rossi alone (and the implementation reference in `context/docs/tech/algorithm.md`).

## Additional claims this source supports

### Suggested for: Ch 2.1 ¶4 (NP-hardness motivates the multi-engine approach)
Pinedo's §14.2 (p. 378) explicitly justifies heuristics on the grounds that "branch-and-bound methods are prohibitively time consuming even for only 30 jobs" — a stronger empirical anchor for the multi-engine argument than the abstract NP-hardness statement alone.

### Suggested for: Ch 2.1 ¶5 (Solver comparison — speed-quality tradeoff)
Pinedo's contrast between *constructive* heuristics (dispatching rules — fast, single pass) and *improvement* heuristics (simulated annealing, tabu search — slower, iterative) at p. 382 directly supports our framing of greedy vs. CP-SAT vs. Timefold as occupying different points on the speed–quality tradeoff.

### Suggested for: Ch 2.1 ¶4 or ¶5 (Tabu search and simulated annealing as established metaheuristics)
Pinedo §14.3 (pp. 382–388) gives textbook descriptions of both simulated annealing and tabu search as local-search procedures for scheduling. This means `pinedo2016scheduling` could substitute for `glover1986future` and similar sources if a tertiary/textbook citation is preferred over a primary one. Recommend keeping primary sources for the named metaheuristics but citing Pinedo as the textbook anchor.

### Suggested for: Ch 2.1 ¶4 (CP as one of several solution paradigms)
Pinedo §15.3 and Appendix C cover Constraint Programming explicitly — Pinedo could supplement Rossi as a textbook reference here. Not necessary if Rossi already carries the CP citation.

## Definisjoner gitt av kilden

| Term | Definisjon | Side |
|---|---|---|
| Scheduling | "A decision-making process … It deals with the allocation of resources to tasks over given time periods and its goal is to optimize one or more objectives." | 1 |
| Polynomial time algorithm | "An O(n³) algorithm is usually referred to as a polynomial time algorithm; the number of iterations is polynomial in the size (n) of the problem." | 587 |
| NP-hardness | "A problem P, either a decision problem or an optimization problem, is called NP-hard if the entire class of NP problems polynomially reduces to P." (Def. D.2.3) | 588 |
| NP-hard in the ordinary sense / strongly NP-hard | Problems whose complexity reduces from PARTITION admit pseudo-polynomial algorithms and are *NP-hard in the ordinary sense*; problems whose complexity reduces from SATISFIABILITY, 3-PARTITION, HAMILTONIAN CIRCUIT or CLIQUE are *strongly NP-hard*. | 589, 590 |
| Approximation algorithm (ρ-approximation) | "An algorithm A is called a ρ-approximation algorithm for a problem, if for any instance I of that problem the algorithm A yields a feasible solution with objective value A(I) such that |A(I) − OPT(I)| ≤ ε · OPT(I)." (Def. D.4.1) | 594 |
| Dispatching rule (static vs dynamic) | "Static rules are not time dependent. They are just a function of the job and/or of the machine data, for instance, WSPT. Dynamic rules are time dependent." | 376 |
| Constructive heuristic | "[Dispatching rules and composite dispatching rules] are of the constructive type. They start without a schedule and gradually construct a schedule by adding one job at a time." | 382 |
| Improvement heuristic / local search | "Algorithms of the improvement type … start out with a complete schedule, which may be selected arbitrarily, and then try to obtain a better schedule by manipulating the current schedule." | 382 |
| Tabu-search | A deterministic local-search procedure that maintains a tabu-list of forbidden moves to escape local minima (Algorithm 14.3.3). | 386–387 |
| Simulated annealing | A probabilistic local-search procedure with a cooling schedule β_k that controls the probability of accepting worse solutions (Algorithm 14.3.2). | 384–385 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "Scheduling is a decision-making process … It deals with the allocation of resources to tasks over given time periods and its goal is to optimize one or more objectives." | 1 | Ch 2.1 ¶1 — definition of scheduling |
| "Given a collection of jobs requiring processing in a certain machine environment, the problem is to sequence these jobs, subject to given constraints, in such a way that one or more performance criteria are optimized." | 7 | Ch 2.1 ¶1 — explicit constraint framing |
| "Many scheduling problems do not have a polynomial time algorithm; these problems are the so-called NP-hard problems." | 26 | Ch 2.1 ¶4 — NP-hardness |
| "Many scheduling problems are either NP-hard in the ordinary sense or strongly NP-hard. For these problems it will be clearly very hard to find an optimal solution in a time effective manner." | 594 | Ch 2.1 ¶4 — NP-hardness motivates heuristics |
| "As branch-and-bound methods are prohibitively time consuming even for only 30 jobs, it is important to have a heuristic that provides a reasonably good schedule with a reasonable computational effort." | 378 | Ch 2.1 ¶4 — practical motivation for heuristics |
| "[Dispatching and composite dispatching rules] are of the constructive type. They start without a schedule and gradually construct a schedule by adding one job at a time." | 382 | Ch 2.1 ¶4, Ch 4.5 ¶4 — greedy/constructive heuristic |
| "A number of these [dispatching] rules yield optimal schedules in some machine environments and are reasonable heuristics in others." | 376 | Ch 2.1 ¶4, ¶5 — solver comparison |
| "Some of the easiest scheduling problems can be solved through a simple priority rule, e.g., WSPT, EDD, LPT, and so on." | 587 | Ch 2.1 ¶4 — priority/dispatching rules as polynomial-time exact methods in special cases |
| "Each task may have a certain priority level, an earliest possible starting time and a due date." | 1 | Ch 2.1 ¶2 — task attributes mirroring Ressursplanlegger's assignments |

## Hva kilden IKKE sier

This is the most important section for the writer. Because Pinedo is a *machine* scheduling textbook, several claims in our outline are **outside Pinedo's scope** and must be sourced elsewhere:

- **Personnel / driver / nurse / crew scheduling.** Pinedo deals with jobs on machines. Driver scheduling is a different problem class (no fixed routing through a workcenter; resources have personal preferences and labour-law constraints). Use `ernst2004staff` for the personnel-scheduling positioning.
- **Vehicle routing.** Pinedo does not cover the VRP. Use `braekers2016vrp` only as the brief delimitation reference in 2.1 ¶4 — VRP is not engaged with as a theory in this thesis.
- **Multi-resource scheduling (driver + vehicle simultaneously).** Pinedo's models assign jobs to a single resource (a machine). The Ressursplanlegger problem of assigning *both* a driver and a vehicle to each assignment is not a standard Pinedo model. Cite Pinedo for the foundational definition only; do not claim Pinedo's models cover the Ressursplanlegger problem directly.
- **Hard / soft constraint vocabulary.** Pinedo speaks of *feasibility* (constraint = inviolable) and *objective function* (preferences). The explicit *hard-constraint vs soft-constraint* distinction with weighted-sum aggregation is Constraint Programming / CSP terminology, not Pinedo's. Cite `rossi2006constraint` for that vocabulary.
- **CP-SAT specifically.** Pinedo discusses Constraint Programming (Appendix C, §15.3) but not the modern CP-SAT solver. Cite `googleortools2026cpsat` and `perron2023cpsatlp`.
- **Late acceptance hill climbing.** Pinedo covers simulated annealing, tabu search, genetic algorithms, and ant colony optimisation, but *not* late acceptance hill climbing. Cite `burke2017late` for that.
- **The word "greedy"** as a primary term. Pinedo's term is *dispatching rule* / *constructive heuristic*. The writer should bridge these terms explicitly when citing Pinedo for the greedy engine.

## Forfatter-perspektiv / metodologi
Pinedo (NYU Stern) writes from an Operations Research / Industrial Engineering perspective. The book is a graduate-level reference structured around three pillars: deterministic theory (Part I), stochastic theory (Part II), and practical implementation (Part III, Chs 14–20). It is the standard academic citation for machine-scheduling foundations in OR, but is *machine-centric* — its examples are workshops, semiconductor fabs, paper-bag factories, and airport gate assignment, not transport dispatching. For our purposes, Pinedo provides the rigorous theoretical foundation (definition, complexity theory, heuristic taxonomy) but must be supplemented by domain-specific sources for personnel scheduling and constraint-programming vocabulary.