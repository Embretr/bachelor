# Handbook of Constraint Programming (`rossi2006constraint`)

## Status
- [x] Notes generated from raw on 2026-04-28
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT (for the chapters used)
  - **Reasoning:** The PDF is a curated 144-page excerpt containing four chapters of the handbook. Three are used in this extraction: Ch 5 (Local Search Methods, pp. 135–167 — partial), Ch 8 (The Complexity of Constraint Languages, pp. 245–278), and Ch 22 (Constraint-Based Scheduling and Planning, pp. 761–800 — complete). The fourth, Ch 23 (Vehicle Routing), is in the PDF but is **not used** in this extraction — by user decision the thesis does not engage with VRP framing. All claims the writer needs for Ch 2.1 ¶3 (constraint-programming framing of hard/soft constraints), ¶4 (NP-hardness), and ¶5 (heuristic search and the speed–quality tradeoff) are captured below from Ch 5, 8 and 22, with verbatim quotes and dual page references. Ch 9 "Soft Constraints" (the handbook's canonical chapter for soft-constraint formalisms) is NOT in the excerpt and will not be added; the hard/soft cite is therefore anchored in Ch 22.1.5's scheduling vocabulary (deadline vs. due date + weighted objective). See "Hva kilden IKKE sier" for the resulting citation-strategy implications.
  - **Gaps not investigated:** Ch 5 in the book continues to p. 244, but the PDF cuts at p. 167 (after the SLS introduction and tabu-search material). The remaining 77 pages of Ch 5 are not in the file. Ch 9 "Soft Constraints" is intentionally not included. Ch 23 is in the file but skipped on scope grounds (no VRP framing). The other 24 chapters of the handbook (Ch 1–4, 6–7, 10–21, 24–28) are not in the PDF and therefore not investigated.

## Source metadata
- **BibTeX key:** `rossi2006constraint`
- **Reference (APA 7):** Rossi, F., van Beek, P., & Walsh, T. (Eds.). (2006). *Handbook of constraint programming* (Foundations of Artificial Intelligence, Vol. 2). Elsevier.
- **Tilgang:** PDF (curated excerpt, 4 chapters; only 3 chapters used)
- **Raw source:** `../rossi2006constraint.pdf` (144 PDF pages, ~155 printed pages across the four chapters)
- **Coverage in raw:** Ch 5 §5.1 + early SLS material (printed 135–167, PDF 1–33); Ch 8 (printed 245–278, PDF 34–67); Ch 22 complete (printed 761–800, PDF 68–109); Ch 23 complete (printed 801–836, PDF 109–144) — *present in PDF but not used*.
- **Page-mapping note:** Printed page = PDF page + 134 for Ch 5; printed page = PDF page + 211 for Ch 8; printed page = PDF page + 691 for Ch 22. Verified by spot check (PDF p. 76 = printed p. 767; PDF p. 105 = printed p. 796).

## Sammendrag (2–3 setninger)
The *Handbook of Constraint Programming* is the canonical research reference work for constraint programming (CP); the chapters used here cover stochastic local search (Hoos & Tsang, Ch 5), the complexity-theoretic foundations of CSP (Cohen & Jeavons, Ch 8) and constraint-based scheduling and planning (Baptiste, Laborie, Le Pape & Nuijten, Ch 22). Its contribution to this thesis is fourfold: (i) the formal CSP definition that grounds Ressursplanlegger's constraint model, (ii) the foundational result that the general CSP is NP-hard, justifying heuristic rather than exact methods at fleet scale, (iii) the constraint-based scheduling framing that distinguishes mandatory deadlines from preference-based due dates and weights individual activities in the objective, and (iv) the documented strengths of mixing CP with local search and metaheuristics — which directly supports Ressursplanlegger's multi-engine architecture (greedy + CP-SAT + Timefold).

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.1 ¶1 (resource scheduling definition) | partial — Ch 22.1 gives the activity/resource/temporal-constraint formulation but pinedo2016scheduling is the more direct source for the headline definition |
| Ch 2.1 ¶2 (multi-resource scheduling) | covered — Ch 22.1.2 distinguishes unary, cumulative and state resources |
| Ch 2.1 ¶3 (hard and soft constraints) | partial — Ch 22.1.5 distinguishes mandatory deadlines from preference-based due dates and presents weighted objective functions; the explicit "soft constraint" formalism is in Ch 9 of the handbook (NOT in this PDF excerpt; not added by scope decision) |
| Ch 2.1 ¶4 (NP-hardness, multi-engine motivation) | covered — Ch 8 proves the general CSP is NP-hard; Ch 22.5 motivates heuristic search on complexity grounds |
| Ch 2.1 ¶5 (solver comparison, CP foundations) | covered — Ch 5 and Ch 22.5.1 frame local search and metaheuristics (tabu, simulated annealing) for CSPs; Ch 22.6 articulates the hybrid CP+LS+MIP design pattern |
| Ch 4.5 ¶3 (hard/soft constraints in algorithm) | partial — same caveat as Ch 2.1 ¶3 |
| Ch 4.5 ¶4 (greedy + CP-SAT + Timefold rationale) | covered — Ch 22.5.1 explicitly recommends mixing constraint-based tree search with local search for industrial scheduling; Ch 22.6 lists hybrid CP+LS+LNS+MIP as a proven strength |

## Claims this source supports

### Claim: "The general constraint satisfaction problem is NP-hard"
- **Suggested for:** Ch 2.1 ¶4 (NP-hardness justifies heuristics over exact methods)
- **Direkte sitat:**
  > "It has been shown that the class of all constraint satisfaction problem instances is NP-hard [72], so it is unlikely that efﬁcient general-purpose algorithms exist for solving all forms of constraint problem. However, in many practical applications the instances that arise have special forms that enable them to be solved more efﬁciently." (p. 245 / PDF 34)
- **Parafrase:** Cohen & Jeavons open Ch 8 with the foundational NP-hardness result for the CSP class. Practical instances may admit faster solutions when constraint structure is restricted (the rest of Ch 8 develops which restrictions yield polynomial-time tractability), but the general problem remains intractable.
- **Forbehold:** The cite is to "[72]" inside the chapter — Cohen & Jeavons report rather than re-prove the result. They focus on tractable *constraint languages* (Schaefer's dichotomy on Boolean domains; the algebraic theory of polymorphisms on finite domains) — none of which directly characterise our multi-resource assignment problem. The handbook covers tractability dichotomies but does not say multi-resource driver/vehicle assignment is or isn't tractable.
- **Anvendelse på vårt case:** Ressursplanlegger's planning problem encodes hard constraints (licence class, working hours, no double-booking, vehicle-type compatibility) and a weighted soft-constraint objective; this places it inside the general CSP class, so the NP-hardness result applies and rules out exact polynomial-time solution as fleet size grows. This is the formal reason the architecture commits to a greedy baseline plus near-optimal solvers (CP-SAT) and metaheuristics (Timefold) instead of a single exact engine.

### Claim: "Mandatory deadlines and preference-based due dates are modelled differently — deadlines as hard, due dates as preferences inside a weighted objective"
- **Suggested for:** Ch 2.1 ¶3 (hard vs. soft constraints, weighted objective); Ch 4.5 ¶3 / ¶4 (algorithm constraint model)
- **Direkte sitat:**
  > "Many of the classical scheduling criteria take into account a due date δi that one would like to meet for each activity. In contrast to a deadline di which is mandatory, a due date δi can be seen as a preference. In the following, Ci denotes the completion time of activity Ai. Lateness Li of Ai is deﬁned as the difference between the completion time and the due date of Ai […]. The tardiness Ti of Ai is deﬁned as max(0, Li), while earliness of Ai is deﬁned as max(0, −Li). The notation Ui is used to denote a unit penalty per late job, i.e., Ui equals 0 when Ci ≤ δi and equals 1 otherwise." (p. 770 / PDF 79)

  > "The commonly studied criteria F are either formulated as a sum or as a maximum. A weight per activity wi may be used to give more importance to some activities. We mention the following well-known optimization criteria: • Makespan: F = Cmax = max Ci • Total weighted ﬂow (or completion) time: F = Σ wi Ci • Maximum tardiness: F = Tmax = max Ti • Total weighted tardiness: F = Σ wi Ti • Total weighted number of late jobs: F = Σ wi Ui." (p. 770–771 / PDF 79–80)
- **Parafrase:** Baptiste, Laborie, Le Pape & Nuijten formalise the distinction between a *deadline* (a mandatory, hard temporal bound — must be satisfied for the schedule to be feasible) and a *due date* (a preferred completion time whose violation is penalised through tardiness, late-jobs counts or related criteria). They model preferences via a weighted objective function: each activity carries a weight w_i that scales its contribution to the optimisation criterion, so that more important activities get more attention from the optimiser.
- **Forbehold:** The handbook's most direct treatment of "soft constraints" as a distinct formal apparatus is Ch 9 (Bistarelli, Gadducci), which is **not in this PDF excerpt**. Ch 22.1.5 instead reaches the same modelling outcome through the standard scheduling vocabulary of *mandatory deadlines / preference-based due dates / weighted objective criteria*. The writer should describe the source's framing in scheduling terms (deadline vs. due date, weighted criteria) rather than implying that Rossi et al. provide a generic soft-constraint formalism.
- **Anvendelse på vårt case:** Ressursplanlegger's hard constraints (licence class, vehicle-type fit, working-hour limits, no double-booking, registered absences) are deadlines / feasibility bounds in the Baptiste et al. sense. Soft constraints (workload balance across drivers, driver preferences, customer–driver continuity, assignment-priority weight) correspond to the weighted-objective form: each is a coefficient on a tardiness-style penalty that the optimiser sums over activities to produce the soft score. Coordinator-configurable weights are the direct analogue of the per-activity w_i in the handbook.

### Claim: "Constraint propagation alone cannot remove all impossible values; heuristic search is required at scale"
- **Suggested for:** Ch 2.1 ¶4 (multi-engine rationale); Ch 2.1 ¶5 (CP foundations for solvers)
- **Direkte sitat:**
  > "Since for complexity reasons constraint propagation cannot remove all impossible values from the domains of variables, heuristic search is required to generate a solution to the problem instance under consideration." (p. 789 / PDF 98)

  > "Even when search can be simpliﬁed by looking for good sequences and using dominance properties, search spaces for planning or scheduling problems tend to be very large. In practice, it is often impossible to explore a search space completely and guarantee the delivery of an optimal solution. For an industrial planning or scheduling application it however generally sufﬁces to provide 'good' solutions within reasonable time. It is for such applications more important to be robust with respect to variations in the problem instances like variations in problem size, variations in numerical characteristics, and addition of side constraints. This is often achieved by mixing constraint-based tree search with Local Search (LS) or by actually implementing LS with constraints." (p. 792 / PDF 101)
- **Parafrase:** Baptiste et al. justify heuristic and hybrid search on a complexity argument: at industrial sizes, propagation prunes some but not enough of the search space; complete search is infeasible; therefore the practical goal is "good" solutions within a time budget, with robustness to instance variation as the priority. They explicitly recommend mixing constraint-based tree search with local search.
- **Forbehold:** "Heuristic search" in this passage means CP tree search guided by problem-specific heuristics — not unstructured greedy assignment. The argument applies cleanly to CP-SAT (constraint propagation + tree search) and to Timefold (local-search metaheuristic over a constraint-based model); it applies *by extension* to a true greedy first-feasible engine. The writer should not paraphrase as if the handbook endorses pure greedy methods.
- **Anvendelse på vårt case:** Ressursplanlegger's three engines occupy different points on this complexity-driven tradeoff: greedy gives an instant feasible plan when the coordinator needs an immediate baseline; CP-SAT applies propagation plus search to find a near-optimal plan within a configurable time limit (typically ≤500 assignments); Timefold provides a local-search metaheuristic that scales to multi-day or multi-fleet instances. The "robustness to side constraints" criterion that Baptiste et al. name is the same property that lets us add company-specific soft constraints (e.g., customer–driver continuity) without re-architecting the solver.

### Claim: "Stochastic local search and metaheuristics (tabu search, simulated annealing) are an established CP solving paradigm"
- **Suggested for:** Ch 2.1 ¶5 (Timefold/metaheuristic legitimacy as CP technique); Ch 2.1 ¶4 (multi-engine repertoire)
- **Direkte sitat:**
  > "Most local search methods use randomisation to ensure that the search process does not stagnate with unsatisfactory candidate solutions and are therefore referred to as stochastic local search (SLS) methods. Prominent examples of SLS methods are randomised iterative improvement (also known as stochastic hill-climbing), evolutionary algorithms, simulated annealing, tabu search, dynamic local search and, more recently, ant colony optimisation. These classes of local search algorithms are also widely known as metaheuristics." (p. 135 / PDF 1)

  > "Local search is one of the fundamental paradigms for solving computationally hard combinatorial problems, including the constraint satisfaction problem (CSP). It provides the basis for some of the most successful and versatile methods for solving the large and difﬁcult problem instances encountered in many real-life applications. Despite impressive advances in systematic, complete search algorithms, local search methods in many cases represent the only feasible way for solving these large and complex instances." (p. 135 / PDF 1)

  > "The key idea behind Tabu Search (TS) is to use memory to prevent the search process from stagnating in local minima or, more generally, attractive non-solution areas of the given search space." (p. 145 / PDF 11, approximate — see Forbehold)
- **Parafrase:** Hoos & Tsang frame stochastic local search (SLS) — including tabu search, simulated annealing and related metaheuristics — as the established paradigm for solving large-instance CSP problems where complete search is infeasible. Tabu search uses a memory of recent moves to avoid stagnation; simulated annealing uses temperature-controlled randomised acceptance. Both are widely deployed, well-studied techniques.
- **Forbehold:** The OCR quality on Ch 5 pp. 137–145 is poor (e.g., "9" appears for "g", "II" for "I", apostrophes garbled to "'") — the verbatim quotes from the introduction (p. 135) are clean, but quotes from later in Ch 5 should be spot-checked against the PDF before being inserted in the thesis.
- **Anvendelse på vårt case:** Timefold's tabu-search and simulated-annealing components are directly the SLS metaheuristics Hoos & Tsang describe as state-of-the-art for large CSP instances. Citing this chapter establishes that Timefold's design choice is mainstream constraint-programming practice rather than an ad-hoc engineering decision, and supports the multi-engine architecture's positioning of Timefold for instances that exceed CP-SAT's practical reach.

### Claim: "CP for scheduling derives strength from combining OR algorithms with the AI/CP modelling paradigm"
- **Suggested for:** Ch 2.1 ¶5 (CP foundations) — supplementary; Ch 4.5 ¶2 (justification for CP-SAT choice)
- **Direkte sitat:**
  > "Constraint-Based Scheduling has over the years grown into one of the most successful application areas of CP. One of the key factors of this success lies in the fact that a combination was found of the best of two ﬁelds of research that pay attention to scheduling, namely Operations Research (OR) and Artiﬁcial Intelligence (AI)." (p. 762 / PDF 71)

  > "[T]wo strengths emerge: i) natural and ﬂexible modeling of scheduling problems as Constraint Satisfaction Problems (CSPs) and ii) powerful propagation of temporal and resource constraints." (p. 762 / PDF 71)

  > "Two other strengths identiﬁed in this chapter are i) a natural ﬁt of expressing scheduling speciﬁc heuristics using CP tree search, and ii) a proven good potential of combining the CP approach with solution techniques as Local Search, Large Neighborhood Search, and Mixed Integer Programming." (p. 795 / PDF 104)
- **Parafrase:** Baptiste et al. argue that constraint-based scheduling succeeds because it integrates efficient OR-style propagation algorithms inside the flexible AI/CP modelling paradigm. Four named strengths: flexible CSP modelling, powerful propagation, scheduling-specific tree-search heuristics, and a track record of hybridisation with local search, large neighbourhood search, and mixed-integer programming.
- **Forbehold:** This is a survey-style framing, not a single proof. It is appropriate for high-level positioning sentences ("CP-SAT belongs to a tradition of...") rather than narrow technical claims.
- **Anvendelse på vårt case:** The CP-SAT engine in Ressursplanlegger is exactly the OR/AI hybrid Baptiste et al. describe — Google OR-Tools' CP-SAT inherits both the efficient SAT/MIP-style propagation and the CP modelling vocabulary. The multi-engine setup (greedy + CP-SAT + Timefold) instantiates the "combining CP with LS / LNS / MIP" pattern the chapter identifies as a proven strength.

### Claim: "Real-world scheduling problems carry side constraints that simple Advanced Planning and Scheduling systems oversimplify, leading to impractical plans"
- **Suggested for:** Ch 5.1 / 5.4 (discussion of why legacy TMS systems leave the planning gap open); Ch 2.1 ¶3 (motivates configurable soft-constraint weights)
- **Direkte sitat:**
  > "[I]t's especially on the side constraints that APS's [Advanced Planning and Scheduling systems] tend to be weak, thus leading to the system solving an oversimpliﬁed problem resulting in producing impractical solutions for the original problem. It is here that we believe Constraint-Based Planning and Scheduling have a great, largely unused, potential." (p. 794–795 / PDF 103–104)

  > "[A]nother strength was identiﬁed namely the capacity to in a natural and ﬂexible way model the scheduling or planning problem at hand in the required real-life detail. We want to stress that this capacity is becoming more and more important. Indeed through the widespread adoption of ERP (Enterprise Resource Planning) systems, more and more companies have access to the data that allows them to capture the reality in the detail they need." (p. 794 / PDF 103)
- **Parafrase:** Baptiste et al. argue that the limitation of existing Advanced Planning and Scheduling (APS) systems is not raw solving power but the inability to represent company-specific side constraints. The result is that APS systems solve a simplified problem and produce plans that don't match operational reality. Constraint-based scheduling, by contrast, lets each company's constraints be modelled directly and has unused potential precisely on this dimension.
- **Forbehold:** The handbook is not transport-specific — "APS" here is the manufacturing-software category, not Norwegian TMS systems like Timpex/Opter. The argument about flexibility-vs-oversimplification transfers, but the writer must not over-claim that Baptiste et al. directly characterise Norwegian TMS shortcomings; that anchoring belongs to the interview findings.
- **Anvendelse på vårt case:** This passage supports Ch 5.1/5.4's argument that Ressursplanlegger's competitive position vs. Timpex/Opter lies precisely in handling planning with company-specific constraints — the same class of "side constraints" Baptiste et al. flag as the weakness of APS systems. It also supports Ch 2.1 ¶3's framing that configurable soft-constraint weights are a feature, not an engineering convenience.

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| activity (Ai) | oppdrag (assignment) | Source uses indexed activity over time; we use oppdrag with start/end and resource requirement. |
| resource (Rj) | sjåfør + kjøretøy (driver + vehicle) | Source defines resources with capacity, calendars, breakability; ours are unary (binary capacity 1) plus competence/licence attributes. |
| processing time (proc(Ai)) | oppdragsvarighet | Direct equivalent. |
| start(Ai), end(Ai) | starttidspunkt, sluttidspunkt for oppdrag | Direct equivalent. |
| release date (ri) and deadline (di) | tidligste mulige starttid og senest tillatte sluttid | Source uses [ri, di] as the activity's hard time window — our hard time window is identical. |
| due date (δi) | preferert sluttid / kundens ønske | The source's "preference" — in our model expressed as a soft constraint with configurable weight rather than via tardiness exactly. |
| weight per activity (wi) | oppdragsprioritet (configurable) | Direct equivalent — controls how much an activity contributes to the soft objective. |
| feasibility / feasible solution | gyldig plan (alle harde constraints overholdt) | Direct equivalent. |
| optimisation criterion (F) | soft score / objektivfunksjon | Source's F = Σ wi · Ti, F = Σ wi · Ui etc. correspond directly to our weighted soft-score components. |
| side constraint | bedriftsspesifikk myk constraint (configurable) | Source's term for the company-specific add-ons that turn the textbook problem into an industrial one. |
| tabu search | Timefold tabu-komponent | Same algorithm class. |
| simulated annealing | Timefold simulated-annealing-komponent | Same algorithm class. |
| metaheuristic / SLS | Timefold-engine | Source umbrella term for tabu/SA/genetic/etc. |
| constraint propagation | CP-SAT propagation | Same mechanism. |
| (constraint-based) tree search | CP-SAT search | Same mechanism. |
| job shop scheduling problem (JSP) | Vårt problem (analog, ikke identisk) | Multi-resource scheduling with fixed activity locations; the closest established academic analogue for Ressursplanlegger's structure. |

### Begrensninger i applikasjon

- **Domain mismatch — no transport coordinator anywhere in the source.** Ch 22 covers manufacturing and project scheduling. The human role (planner, dispatcher, *trafikkoordinator*) is essentially absent. The handbook describes the algorithmic component, not the workflow that uses it. For Ch 2.2 (HITL) and Ch 5.2 the source is therefore not applicable — citations there must come from parasuraman2000automation, lee2004trust, etc.
- **Soft-constraint formalism is in Ch 9, not in this PDF excerpt.** The handbook's canonical chapter on soft constraints (semiring-based, weighted, fuzzy) is Bistarelli et al., Ch 9 — not included by scope decision. The hard/soft framing in our outline is cited from this PDF via Ch 22.1.5 (deadline vs. due date, weighted objective), and the writer should *not* claim that Rossi et al. develop a general soft-constraint formalism on the basis of the current excerpt.
- **Vocabulary translation overhead.** The source talks about "machines", "operators", "jobs", "activities" in a manufacturing/project context. Each citation must translate into our driver+vehicle assignment vocabulary in the writing — see the application notes per claim above.
- **Ch 5 OCR quality is uneven.** Pages 137–150 of the PDF have OCR artefacts (`g(s)` rendered as `9(s)`, apostrophes garbled). Verbatim quotes from this region must be checked in the PDF before being inserted into the thesis. The Ch 5 introduction (p. 135) and Ch 22 throughout are clean.
- **Scale assumption.** The handbook's complexity arguments assume "industrial-scale" instances of hundreds-to-thousands of activities. Our smallest interview companies operate at 8–15 vehicles per day; for those, the practical motivation for heuristics is not raw NP-hardness but solver-runtime predictability and side-constraint flexibility. The writer should pair the NP-hardness claim with the runtime/robustness argument from Baptiste et al. p. 792 rather than relying on asymptotic complexity alone.
- **No claims about Norwegian transport sector.** The source contains zero data about Norwegian transport, SMEs, legacy TMS systems, or the specific constraints (kjøre-/hviletid, ADR, tariffavtale) that shape the Ressursplanlegger problem. All such anchoring must come from the interviews and the technical-architecture documentation.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Constraint Satisfaction Problem (CSP) instance | "A CSP instance is a triple P = (V, D, C), where V = {x1, ... , xn} is a finite set of n variables, D is a function that maps each variable xi to the set Di of possible values it can take (Di is called the domain of xi), and C = {C1, ... , Cm} is a finite set of constraints." (Definition 5.1, paraphrased through OCR; see Cohen & Jeavons Definition 8.2 for the canonical form) | 137 / PDF 3 |
| CSP (canonical, Cohen & Jeavons) | "For any set D and any constraint language Γ over D, the constraint satisfaction problem CSP(Γ) is the combinatorial decision problem with Instance: A triple ⟨V, D, C⟩ […] Question: Does there exist a solution, that is, a function ϕ, from V to D, such that, for each constraint ⟨s, R⟩ ∈ C, with s = ⟨v1, …, vn⟩, the tuple ⟨ϕ(v1), …, ϕ(vn)⟩ belongs to the relation R?" (Definition 8.2) | 247 / PDF 36 |
| Tractable constraint language | "A constraint language, Γ, is said to be tractable if CSP(Γ′) can be solved in polynomial time, for each finite subset Γ′ ⊆ Γ." (Definition 8.3) | 247 / PDF 36 |
| NP-complete constraint language | "A constraint language, Γ, is said to be NP-complete if CSP(Γ′) is NP-complete, for some finite subset Γ′ ⊆ Γ." (Definition 8.3) | 247 / PDF 36 |
| Stochastic local search (SLS) algorithm | "Most local search methods use randomisation to ensure that the search process does not stagnate with unsatisfactory candidate solutions and are therefore referred to as stochastic local search (SLS) methods." | 135 / PDF 1 |
| Metaheuristic | "These classes of local search algorithms [SLS — randomised iterative improvement, evolutionary algorithms, simulated annealing, tabu search, dynamic local search, ant colony optimisation] are also widely known as metaheuristics." | 135 / PDF 1 |
| Deadline vs. due date | "A due date δi … can be seen as a preference. … In contrast to a deadline di which is mandatory, a due date δi can be seen as a preference." | 770 / PDF 79 |

## Rammeverk og modeller

### Common scheduling optimisation criteria (Baptiste et al., §22.1.5, p. 770–771 / PDF 79–80)

| Criterion | Form | Verbal description | Side |
|---|---|---|---|
| Makespan | F = Cmax = max Ci | End time of the schedule (last activity to finish). | 770 / PDF 79 |
| Total weighted flow time | F = Σ wi · Ci | Sum of weighted completion times. | 771 / PDF 80 |
| Maximum tardiness | F = Tmax = max Ti | Worst-case lateness across activities. | 771 / PDF 80 |
| Total weighted tardiness | F = Σ wi · Ti | Sum of per-activity weighted tardiness. | 771 / PDF 80 |
| Total weighted number of late jobs | F = Σ wi · Ui | Sum of per-activity weighted late-job indicators (Ui = 0 if on time, 1 if late). | 771 / PDF 80 |

These criteria are the textbook templates the writer can refer to when describing Ressursplanlegger's soft-score components. Our soft objective is a weighted sum, putting it in the *Σ wi · …* family.

### Resource-type taxonomy (Baptiste et al., §22.1.2, p. ~764–767 / PDF ~73–76)

| Resource type | Definition | Maps to | Side |
|---|---|---|---|
| Unary (disjunctive) | Resource of capacity 1 — at most one activity at a time. | Sjåfør og kjøretøy i Ressursplanlegger | 764 / PDF 73 |
| Cumulative | Resource with capacity > 1 — multiple activities may overlap up to capacity. | Ikke aktuelt (fast capacity 1 per ressurs) | 764 / PDF 73 |
| State resource | Infinite-capacity resource whose state varies over time; activities require specific states. | Ikke direkte aktuelt | 769 / PDF 78 |
| Reservoir | Multi-capacity resource that can be consumed and/or produced. | Ikke aktuelt | 769 / PDF 78 |

For Ressursplanlegger both drivers and vehicles are unary (disjunctive) resources — the multi-resource character is in the cardinality of the resource set per assignment, not in resource capacity per se.

### Hybrid CP solution architectures (Baptiste et al., §22.5–22.6)

The handbook lists the following proven hybrid patterns for industrial CP scheduling:

| Hybrid | Description | Site i kilden |
|---|---|---|
| CP + Local Search | Constraint-based tree search alternated with LS over move neighbourhoods (e.g., shuffle moves, large-neighbourhood search). | p. 791–793 / PDF 100–102 |
| CP + Mixed-Integer Programming | Constraint propagation as preprocessor / sub-problem solver for a MIP-driven master problem (or vice versa). | p. 793–794 / PDF 102–103 |
| CP + Limited Discrepancy Search | Tree search restricted to paths that diverge limitedly from a heuristic baseline. | p. 792 / PDF 101 |

Ressursplanlegger's three-engine pattern (greedy → CP-SAT → Timefold) is a coarser variant of the same idea — different engines for different scale/quality regimes — though the *internal* architecture of each engine (especially CP-SAT) is the OR/CP hybrid the handbook describes.

## Key arguments / lines of reasoning

### Argument: NP-hardness motivates heuristics, not exact methods, at industrial scale
- **Premiss 1:** The general CSP class is NP-hard (Ch 8, p. 245).
- **Premiss 2:** Constraint propagation prunes some but not enough of the search space at industrial sizes (Ch 22, p. 789).
- **Premiss 3:** Industrial users typically need "good" solutions in bounded time, and *robustness to instance variation* (size, side constraints) — not asymptotic optimality (Ch 22, p. 792).
- **Konklusjon:** The recommended industrial approach is to mix constraint-based tree search with local search and/or MIP — not to commit to a single exact engine.
- **Sted:** p. 245 / PDF 34, p. 789–795 / PDF 98–104.
- **Hvilke claims dette støtter:** Ch 2.1 ¶4 (NP-hardness justifies multi-engine), ¶5 (CP-foundations for solver-comparison narrative), Ch 4.5 ¶2 (multi-engine choice).

### Argument: CP's flexibility, not its exactness, is its main industrial value
- **Premiss 1:** Real-world planning problems carry an enormous variety of company-specific side constraints (Ch 22 conclusion p. 794–795).
- **Premiss 2:** Existing APS systems oversimplify because their core models cannot accommodate side constraints (Ch 22 conclusion p. 794–795).
- **Premiss 3:** CP's modelling vocabulary lets new constraints be added without re-designing the solver (Ch 22.6 conclusion).
- **Konklusjon:** The CP value proposition for industrial scheduling is flexibility-in-modelling combined with propagation-driven solving, not solely raw optimality.
- **Sted:** p. 794–795 / PDF 103–104.
- **Hvilke claims dette støtter:** Ch 2.1 ¶3 (motivates configurable soft-constraint weights), Ch 5.1 / 5.4 (interpretation: why Timpex/Opter leave the planning gap open).

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Job Shop Scheduling Problem with hybrid CP+LS (Caseau & Laburthe) | "Repair" + "shuffle" moves combined with constraint-based search produce excellent makespan results vs. pure exact methods. | 791 / PDF 100 |
| Preemptive JSP with edge-finding + Jackson derivation + limited discrepancy search (Le Pape & Baptiste) | Stacking constraint propagation, a local-optimisation operator, and a tree-search variant cuts the average deviation to optimal from 13.72% to 0.23% in 10 minutes CPU. | 792 / PDF 101 |
| Industrial scheduling with subcontracting / unperformed activities | How "left unperformed against a cost" is a standard industrial relaxation modelled as cost in the objective rather than infeasibility — same pattern as Ressursplanlegger's "Skipped at cost" policy. | 769 / PDF 78 |

## Data og statistikk

Few raw statistics — the chapters used here are theoretical / methodological. The closest figures:

| Tall | Enhet | År/scope | Side |
|---|---|---|---|
| 13.72% → 0.23% | Average deviation to optimal — pure depth-first search → full CP+LS hybrid | Le Pape & Baptiste, 10 min CPU, 10 instances × 100 activities | 792 / PDF 101 |

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Schaefer's Dichotomy Theorem | Every Boolean constraint language is either tractable or NP-complete — the foundational tractability result that anchors Ch 8. | 248 / PDF 37 |
| Algebraic theory of polymorphisms | The mathematical apparatus that classifies tractable constraint languages over finite domains. | §8.3, p. 251+ / PDF 40+ |
| Edge-finding | A specific propagation algorithm used in Constraint-Based Scheduling for unary/cumulative resources. | 783 / PDF 92 |
| Limited Discrepancy Search (LDS) | A tree-search alternative that bounds how often the search may diverge from heuristic recommendations — useful when the heuristic is good but imperfect. | 792 / PDF 101 |
| Large Neighbourhood Search (LNS) | A class of metaheuristics that destroy and re-build large parts of a solution; one of the four hybrid combinations Ch 22.6 names as a strength of CP-based scheduling. | 795 / PDF 104 |
| Optional / unperformed activities | Activities the planner can choose not to schedule, against a cost — modelling trick for Ressursplanlegger-style "skip at cost" policies. | 768–769 / PDF 77–78 |
| Side constraint | The OR/CP term for company-specific constraints layered on top of the textbook problem; central to Ch 22.6's argument that APS systems oversimplify. | 794–795 / PDF 103–104 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "It is for such applications more important to be robust with respect to variations in the problem instances like variations in problem size, variations in numerical characteristics, and addition of side constraints. This is often achieved by mixing constraint-based tree search with Local Search (LS) or by actually implementing LS with constraints." | 792 / PDF 101 | Ch 2.1 ¶5 — multi-engine and robustness justification |
| "It's especially on the side constraints that APS's tend to be weak, thus leading to the system solving an oversimpliﬁed problem resulting in producing impractical solutions for the original problem." | 794–795 / PDF 103–104 | Ch 5.1 / 5.4 — why legacy TMS systems leave the planning gap open |

## Hva kilden IKKE sier

- **Ch 9 "Soft Constraints" (Bistarelli, Gadducci) is NOT in the PDF excerpt and will not be added.** The semiring-based soft-constraint formalism (cSPs, weighted CSPs, fuzzy CSPs) — the canonical reference for "soft constraints" as a distinct mathematical object — therefore cannot be cited from this PDF. The hard/soft framing for Ch 2.1 ¶3 is anchored instead in Ch 22.1.5's deadline/due-date/weighted-criteria vocabulary.
- **Outline marker `MUST CITE: \textcite{rossi2006constraint}` for Ch 2.1 ¶3 must be scoped to the Ch 22 framing.** The PDF supports the cite via Ch 22's deadline/due-date and weighted-objective material — narrower than a generic soft-constraint formalism. The writer must phrase the cite in scheduling vocabulary, not in soft-CSP vocabulary.
- **Outline marker `MUST CITE: \textcite{rossi2006constraint}` for Ch 2.1 ¶5 (constraint programming foundations) is fully supported.** Ch 22.5/22.6 and Ch 5 are the right anchors.
- **Ch 23 (Vehicle Routing) is in the PDF but is not used.** By scope decision, the thesis does not engage with VRP framing. Ch 23 contains substantial material on real-world side constraints and CP for routing that overlaps thematically with Ch 22.6, but the Ch 22.6 passages alone are sufficient for the side-constraint / APS-oversimplification argument the writer needs.
- **The handbook does NOT directly address driver+vehicle assignment, traffic coordinators, or Norwegian transport companies.** Every quotation has to be applied across a domain gap (machine scheduling → driver-vehicle dispatching). The application notes in each claim above provide that bridge.
- **The handbook does NOT provide arguments about human-in-the-loop, trust, automation levels, or coordinator workflow.** Ch 2.2 cannot be supported from this source.
- **The handbook does NOT compare Google OR-Tools' CP-SAT specifically against Timefold or any modern solver by name.** Both engines post-date the 2006 publication. Citation must be limited to the *paradigms* (constraint propagation + tree search; SLS metaheuristics) — not to the specific solver implementations.
- **The handbook does NOT provide statistics on Norwegian transport, SMEs, or TMS market structure.** All such anchoring must come from interviews, fitgap-summary, and Norwegian industry sources.
- **The handbook's Ch 5 in this PDF stops at p. 167** — the major SLS algorithmic comparisons, the SLS-method taxonomy, and the empirical performance results the chapter is best-known for run pp. 168–244 and are NOT in the file. The Ch 5 quotes used above are confined to the introduction (p. 135) and tabu-search definitions (p. ~145), where the OCR is acceptable.

## Forfatter-perspektiv / metodologi

The handbook is a 2006 edited research-reference work in Elsevier's *Foundations of Artificial Intelligence* series. Its chapters survey the state of the art rather than report new empirical work; the relevant chapters used here are written by senior CP researchers (Hoos, Tsang, Cohen, Jeavons, Baptiste, Laborie, Le Pape, Nuijten) and are explicitly methodological/theoretical. Cite these chapters for foundational definitions, paradigm descriptions, and design-rationale arguments — not for empirical claims about specific contemporary systems or industries.
