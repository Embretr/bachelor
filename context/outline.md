# Thesis Outline — Ressursplanlegger

> Claude reads this before writing any chapter.
> Contains section-level outlines with content notes and target lengths.
> Update as structure evolves — but keep thesis-spine.md consistent with changes.

---

## Evidence Marker Taxonomy

All ¶-plans use these markers. The deterministic checker greps for them. Each marker must be on its own indented line under the ¶.

| Marker | Meaning | Used in |
|--------|---------|---------|
| `MUST CITE:` | Academic source from result/references.bib required | Ch 2, 3 |
| `MUST EVIDENCE:` | Empirical/system source from context/ required | Ch 4 |
| `MUST ANCHOR:` | Must explicitly connect to RQ, thesis spine, or earlier chapter | Ch 5 |
| `MUST TRACE:` | Must trace back to a specific section, finding, or limitation | Ch 6 |
| `MUST GROUND:` | Must be grounded in a context source, but detailed evidence comes later | Ch 1 |

---

## Paragraph Intention Tags

Every ¶ in every section plan declares one — and only one — argumentative intention. The tag is the paragraph's reason for existing in this chapter; if the intention cannot be named, the ¶ should not be in the plan. The writer agent reads `INTENT` before deciding the ¶'s opening sentence; the red-thread agent uses it to detect drift.

| Tag | Meaning | When to use |
|-----|---------|-------------|
| `INTENT (DEFINE):` | Introduces a concept, term, or category for the first time | First mention of any technical or theoretical construct |
| `INTENT (ARGUE):` | Advances a claim that requires justification | Any non-trivial assertion the reader could plausibly contest |
| `INTENT (EVIDENCE):` | Supplies empirical, theoretical, or system support for a prior claim | After an `ARGUE` ¶ that needs grounding |
| `INTENT (POSITION):` | Situates the project, system, or argument against an external category | When distinguishing Ressursplanlegger from neighbouring tools/theories |
| `INTENT (DELIMIT):` | Marks what is in or out of scope for the current discussion | When closing a possible reader objection by ruling something out |
| `INTENT (ILLUSTRATE):` | Gives a concrete example that makes an abstract claim graspable | Once per section maximum — not for filler |
| `INTENT (QUALIFY):` | Hedges, scopes, or limits a previous claim | After a strong claim that would otherwise overreach |
| `INTENT (TRANSITION):` | Bridges from this section's argument to the next | Closing ¶ of every section |

**Two governing rules.** (1) Every ¶ plan opens with `INTENT (TAG):` on its own line, before the prose summary. (2) Every section's ¶ tags, read in order, must form a coherent argumentative arc — typically `DEFINE → ARGUE → EVIDENCE → (POSITION/ILLUSTRATE/QUALIFY) → TRANSITION`. If the arc is missing or repeats `DEFINE` three times in a row, the section needs restructuring, not more prose.

---

## Chapter 1 — Introduction
**Owner:** Mikael | **Target:** 3–5 pages | **Status:** Not started

**Purpose:** Orient the reader, establish that manual transport planning is a real problem,
and state what Ressursplanlegger and this thesis contribute.

### Sections and content

**1.1 Background and Motivation** (~1.5 pages)

- ¶1: Open broadly — the transport sector's role in Norway, growing complexity, pressure to digitise. Set the scene for the reader who knows nothing about transport logistics.
- ¶2: Introduce the traffic coordinator role — the person who assigns drivers to jobs every day. Describe the current workflow: manual, phone-based, dependent on one person's memory.
- ¶3: The problem — tacit knowledge not captured, legacy systems (Timpex, Trimtex) that handle invoicing but not planning, no unified view of availability, no conflict detection. Use interview findings as implicit motivation (do not cite interviews yet — that is for Ch 4).
  MUST GROUND: interviews-summary.md Theme 2 (Treghet), Theme 5 (Nøkkelpersonavhengighet)
- ¶4: Consequences — inefficiency, key-person dependency, error risk (overtime violations, double-booking, wrong competencies). These are real costs for companies.
  MUST GROUND: interviews-summary.md Theme 2, Theme 3
- ¶5: Why now — constraint-based optimisation tools (OR-Tools, Timefold) have matured, making algorithm-assisted planning accessible for SMEs. Digital transformation in logistics is accelerating but planning remains a manual gap.
- ¶6: Introduce Ressursplanlegger in one paragraph — a web-based platform that generates optimised daily plans and lets the coordinator review, adjust, and approve. Human-in-the-loop by design.
  MUST GROUND: context/scope.md (in-scope features)

**1.2 Research Questions** (~0.5 pages)

- ¶1: State the main research question verbatim from `context/context.md`.
- ¶2: List the three sub-questions. For each, one sentence explaining what it addresses (problem → solution → evaluation).
- Do NOT discuss or justify — that is for Chapter 3.

**1.3 Scope and Delimitations** (~0.5 pages)

- ¶1: What the system covers — daily planning, driver/vehicle assignment, conflict detection, multi-engine optimisation. Reference `context/scope.md`.
  MUST GROUND: context/scope.md (in-scope features)
- ¶2: What is explicitly excluded — invoicing, driver mobile app, GPS tracking, weekly/monthly planning. State why briefly (time constraints, not part of the research question).
  MUST GROUND: context/scope.md (out-of-scope list)
- ¶3: Division of work — Mikael (user research, requirements, thesis writing), Embret (system development, algorithm implementation). Both contribute to discussion and analysis.

**1.4 Thesis Structure** (~0.5 pages)

- Write as a narrative chain, not a table of contents. Each sentence builds on the previous: problem → theory → method → findings → analysis → conclusion. Must match `context/thesis-spine.md`.
  MUST TRACE: each sentence → context/thesis-spine.md chapter sentence

---

## Chapter 2 — Theory
**Owner:** Mikael | **Target:** 8–9 pages | **Status:** Not started

**Purpose:** Establish the theoretical foundation underpinning system design and research approach.

### Chapter Red Thread

The chapter advances a single claim: the design of Ressursplanlegger and the research that produced it cannot be assessed without four specific bodies of theory, presented in the order they are needed by later chapters.

1. **2.1 Resource Scheduling** frames the *algorithmic problem class* — required so Chapter 4.5 (algorithm) and Chapter 5.2 (algorithm performance) can be read against an established standard rather than as an isolated engineering choice.
2. **2.2 Human-in-the-Loop Automation** frames the *interaction model* — required so the "suggest + override" architecture in Chapter 4.4 and the discussion of automation limits in Chapter 5.2 and 5.4 are grounded, not stylistic.
3. **2.3 Transport Management Systems** frames the *existing tool landscape* — required as the comparative baseline that Chapter 4.3 (fit/gap) and Chapter 5.3 (adoption barriers) extend with empirical detail.
4. **2.4 Design Science Research** frames the *research stance* — required to legitimise a build-and-validate study before Chapter 3 applies its phases.

The progression is problem class → interaction pattern → existing landscape → research stance. Two governing rules apply: no theory is included that is not invoked downstream, and no later claim about the system or the methodology is left ungrounded here. Vehicle routing theory appears once, in 2.1, only to delimit the problem from an adjacent class.

### Sections and content

**2.1 Resource Scheduling** (~2.5 pages)

*Why this section is here:* defines the formal class of problem Ressursplanlegger solves (multi-resource scheduling under hard and soft constraints), justifies the multi-engine algorithm choice in terms of NP-hardness and the speed–quality tradeoff, and delimits the problem from the Vehicle Routing Problem. Without this section, the algorithmic decisions in Chapter 4.5 and the benchmarking in Chapter 5.2 have no theoretical reference point.

- ¶1: INTENT (DEFINE): Define resource scheduling — assigning a set of limited resources (people, vehicles) to tasks over time, subject to constraints on availability, task requirements, and temporal dependencies. Cite `\textcite{pinedo2016scheduling}`. Note analogous domains: nurse scheduling, crew scheduling, driver scheduling — all share the structure of matching resources to tasks under constraints.
  MUST CITE: \textcite{pinedo2016scheduling}
- ¶2: INTENT (POSITION): Multi-resource scheduling — Ressursplanlegger assigns *both* an employee and a vehicle to each assignment. This increases combinatorial complexity compared to single-resource problems. The Ressursplanlegger problem: assignments = tasks with fixed time windows and resource requirements; drivers + vehicles = resources with competency, availability, and capacity constraints; objective = maximise coverage + balance soft constraints.
- ¶3: INTENT (DEFINE): Hard and soft constraints — hard constraints must be satisfied for a plan to be feasible (competencies, availability, no double-booking, vehicle type). Soft constraints define preferences optimised by the algorithm (workload balance, driver preferences, priority). Each soft constraint carries a configurable weight. Cite `\textcite{rossi2006constraint}`. Link to the system's actual constraint model from `context/docs/tech/algorithm.md`.
  MUST CITE: \textcite{rossi2006constraint}; MUST EVIDENCE: context/docs/tech/algorithm.md
- ¶4: INTENT (DELIMIT): NP-hardness and the multi-engine approach — resource scheduling at real fleet sizes is NP-hard; exact methods become infeasible as instance size grows. This motivates heuristics: greedy (instant baseline), CP-SAT (near-optimal within time limit), Timefold (metaheuristic for large instances). The Vehicle Routing Problem (VRP) is an adjacent theoretical area with similar structure — cite `\textcite{braekers2016vrp}` — but Ressursplanlegger's problem diverges from VRP in a key way: assignments have fixed times and locations, so the algorithm decides *who* does what, not *in which order*. Sequencing is not part of the problem.
  MUST CITE: \textcite{pinedo2016scheduling}
- ¶5: INTENT (TRANSITION): Solver comparison — greedy O(n × m), no optimality guarantee; CP-SAT complete solver with configurable time limit, near-optimal for ≤500 assignments; Timefold metaheuristic (tabu search, simulated annealing) for large or multi-day instances. Each occupies a different point on the speed-quality tradeoff. Cite `\textcite{rossi2006constraint}` for constraint programming foundations and `\textcite{glover1986future}` for the tabu-search metaheuristic concept. Close with one bridging sentence: an optimal plan is not the same as an *acceptable* plan in this domain — which motivates the human-in-the-loop framing in Section 2.2.
  MUST CITE: \textcite{rossi2006constraint}, \textcite{glover1986future}

**2.2 Human-in-the-Loop Automation** (~2.5 pages)

*Why this section is here:* establishes that, in this domain, full automation is theoretically the wrong target even when the solver can produce an optimal plan; supplies the trust, control, and automation-level concepts that Chapter 4.4 (system design), Chapter 5.2 (algorithm vs. human override), and Chapter 5.4 (tacit knowledge) rely on. Without this section, "suggest + override" appears as a stylistic preference rather than a theoretically required pattern.

- ¶1: INTENT (DEFINE): Define human-in-the-loop (HITL) automation — a design pattern where an automated process produces a recommendation or plan, but a human reviews, adjusts, and approves before it takes effect. Cite `\textcite{parasuraman2000automation}` and their 10-level automation scale. Position Ressursplanlegger at level 5–6 (system suggests, human approves).
  MUST CITE: \textcite{parasuraman2000automation}
- ¶2: INTENT (ARGUE): Why HITL is necessary in this domain — unpredictability (weather, cancellations, sick leave), tacit knowledge (driver preferences, customer relationships, route knowledge), trust (coordinators won't use a system they can't override). Ground in interview findings implicitly — detailed evidence in Ch 4.
- ¶3: INTENT (POSITION): The "suggest + override" design pattern — algorithm does heavy lifting, coordinator applies judgment. This is Ressursplanlegger's core interaction model.
  MUST EVIDENCE: context/docs/tech/architecture.md
- ¶4: INTENT (EVIDENCE): Trust and adoption — coordinators will not rely on a system whose decisions they cannot understand and override. Cite `\textcite{lee2004trust}`. Connect to adoption barriers (developed in Ch 5.3).
  MUST CITE: \textcite{lee2004trust}
- ¶5: INTENT (TRANSITION): HITL as a design constraint — the system must expose its reasoning (conflict detection, scoring breakdown) so the coordinator can make informed corrections. This shapes the UI as much as the algorithm. Close with one bridging sentence: a theoretically grounded interaction pattern is necessary but not sufficient — the artefact also enters an existing tool landscape, surveyed in Section 2.3.
  MUST EVIDENCE: context/docs/tech/architecture.md

**2.3 Transport Management Systems and the Manual-Planning Persistence** (~2 pages)

*Why this section is here:* names the existing software category Ressursplanlegger enters, shows that not every Norwegian transport company even uses one, and explains *why* coordinators continue to plan manually despite decades of TMS availability — supplying the category-level reference and the explanatory baseline that Chapter 4.3 (fit/gap) and Chapter 5.3 (adoption barriers) extend with empirical detail. Without this section, the fit/gap analysis has no comparator and the manual-work persistence reads as an accident rather than a structural fact.

> **Section red thread.** TMS as a category is defined → its actual penetration in the Norwegian context is shown to be uneven → the persistent manual gap is explained, not merely observed → the reader is handed the comparison frame that Chapter 4.3 will fill in. The section answers one reader question: *if these tools have existed for years, why is the assignment problem still solved with phones, sticky notes, and one person's memory?*

- ¶1: INTENT (DEFINE): Open from the conclusion of `\textcite{griffis2007tms}` — TMS as a category centred on order management, freight billing, and carrier management, *not* on the human assignment of resource to task. State the category boundary first, then the mechanics. Add one sentence on data-driven TMS evolution from `\textcite{heinbach2022datadriven}`. Frame the section so the reader knows it is about *systems and their absence*, not about interview findings — the empirical fit/gap comes in Chapter 4.3.
  MUST CITE: \textcite{griffis2007tms}, \textcite{heinbach2022datadriven}
- ¶2: INTENT (POSITION): The Norwegian TMS picture is uneven. Open with "In Norway, transport SMEs split into three patterns: companies on a commercial TMS (Norlog companies on Timpex; Harlem Solutions on Opptur), companies on bespoke in-house systems (Ottem; Nordic Crane), and companies with no system at all (Bergen Bulk Transport)." Make explicit that not every coordinator has a TMS — the manual problem is not only a *TMS shortfall* problem, it is also a *no-TMS-at-all* problem. Smooth the transition from ¶1 with a single linking clause ("Within that category, the Norwegian market shows...") so the move from theory to local reality is gradual, not abrupt.
  MUST EVIDENCE: interviews-summary.md (system usage per company)
  VERIFY: meeting note "Trimtex finnes ikke" and "two systems, not three" — confirm the actual commercial TMS used at Norlog Tana before the writer agent runs; if Trimtex is a misattribution, drop it and reduce the count to two (Timpex, Opptur).
- ¶3: INTENT (EVIDENCE): Replace the prose "what they do vs. what is missing" with a two-column comparison table: "What commercial TMS provide" (order capture, customer/contract management, invoicing, driver-app dispatch, basic reporting) vs. "What coordinators need but no TMS supplies" (constraint-aware plan generation, capacity overview, conflict detection, formalised tacit knowledge, sick-leave replanning). One sentence after the table defines fit/gap analysis briefly so the reader carries the concept into Chapter 4.3 — "a fit/gap analysis compares system capabilities against documented user needs to expose what an existing tool covers and what it does not." The needs column is labelled as derived from interview themes; full evidence is reserved for Chapter 4.
  MUST EVIDENCE: fitgap-summary.md (capability columns); interviews-summary.md (themes 1, 2, 3, 5)
- ¶4: INTENT (ARGUE): The substantive question — why do Norwegian traffic coordinators still plan manually despite the tools that do exist? Three structural reasons, each grounded: (a) *no commercial TMS does plan generation*; the assignment cognition has nowhere to go even when the surrounding system is modern; (b) *ease-of-use and trust barriers* — interviewees describe Timpex/Trimtex as extremely slow and unintuitive, which raises the cost of any new tool; (c) *job-protection concerns* — coordinators do not want to automate themselves out of work, and sceptical respondents (Ottem, Bergen Bulk Transport) condition adoption on retaining manual control. Add the historical anchor: Norway was an early adopter in adjacent transport-tech domains (e.g., maritime ship-control software) — so the persistence of manual planning is not a story about technological backwardness, it is about the *absence of a planning-specific tool category*. Frame it explicitly: coordinators plan manually not because they want to, but because no tool gives them an alternative that fits the work.
  MUST CITE: \textcite{griffis2007tms}, \textcite{lee2004trust}
  MUST EVIDENCE: interviews-summary.md (themes 2, 4, 6); fitgap-summary.md
  VERIFY: meeting note "Norge var en av de første med ship control software" — confirm a citeable source before keeping the historical claim; if no source exists, drop the maritime anchor and rest the argument on (a)–(c) alone.
- ¶5: INTENT (ILLUSTRATE): One short analogy to make the structural absence concrete — the meeting note pointed to wine and South America. Develop in two sentences: a global product category (mass-market wine; mass-market TMS) can dominate worldwide while leaving a local production pattern (terroir-driven Chilean/Argentinian wine; small-fleet Norwegian transport SMEs with mixed competence and short planning horizons) underserved, because the global category is not built for the local pattern. Apply: Norwegian transport planning is in this position — the global TMS category exists, but a planning-specific tool for the coordinator role does not. Use the analogy once and move on.
  VERIFY: meeting note "wine and South America" — confirm with Mikael which specific case he had in mind so the analogy is precise rather than decorative; if it does not survive verification, replace with a domain example (e.g., nurse rostering tools fitting hospitals but not home-care agencies).
- ¶6: INTENT (TRANSITION): The planning gap — none of the existing systems, and none of the structural reasons that perpetuate manual work, address the space between "an assignment exists in the database" and "a driver is assigned to it." That space is where Ressursplanlegger fits. Close with the bridging sentence: building a tool to occupy this gap, and treating that build as research, requires a methodological frame — Design Science Research, introduced as theory in Section 2.4 and applied in Chapter 3.
  MUST EVIDENCE: fitgap-summary.md (gap items)

**2.4 Design Science Research** (~1.5 pages)

*Why this section is here:* legitimises a build-and-validate study as research, distinguishes validation from evaluation, and supplies the framework that Chapter 3.1 applies and Chapter 3.5 invokes in the validity discussion. Without this section, the thesis would have no answer to the question "why is building a system research?" — and the validation choices in Chapter 3.5 would lack a recognised standard.

- ¶1: INTENT (DEFINE): Define DSR — creating and evaluating artefacts to address practical problems. Cite `\textcite{hevner2004design}` and `\textcite{peffers2007dsrm}`.
  MUST CITE: \textcite{hevner2004design}, \textcite{peffers2007dsrm}
- ¶2: INTENT (ARGUE): Why DSR fits this project — the contribution is both the artefact (Ressursplanlegger) and the knowledge gained through building and validating it. DSR structures the process from problem identification through evaluation.
- ¶3: INTENT (DELIMIT): Validation vs evaluation — cite `\textcite{wieringa2014dsm}`. Explain that this thesis validates (predicts behaviour through benchmarking and requirements traceability) rather than evaluates (deploys in production). Bridge to Chapter 3 where the specific DSR application is detailed.
  MUST CITE: \textcite{wieringa2014dsm}
- ¶4: INTENT (TRANSITION): Bridge to methodology — make explicit that this section explains DSR as theory, while Chapter 3 applies the DSR phases to this specific project. This avoids repeating methodology content in the theory chapter.

> **Note:** Section 2.4 was previously "Related Work." Moved DSR here because sensor criterion NRT3 (Theoretical Insight) explicitly covers "knowledge of relevant methods." Related work on algorithm-assisted dispatching is now woven into 2.1 and 2.2 rather than a separate section — avoiding a thin, disconnected related-work section.

---

## Chapter 3 — Methodology
**Owner:** Mikael | **Target:** 5–8 pages | **Status:** Not started

**Purpose:** Explain how the research was conducted, justify the choices, establish credibility.

### Sections and content

**3.1 Research Design** (~1.5 pages)

- ¶1: State the methodology — Design Science Research (DSR). Cite Peffers (2007) for six-phase model and Hevner (2004) for the framework. One-sentence definition.
  MUST CITE: \textcite{peffers2007dsrm}, \textcite{hevner2004design}
- ¶2: Why DSR fits — combines building a software artefact with investigating a real problem. Contrast briefly with pure case study (no artefact) and pure development (no research).
- ¶3: DSR phases applied — table mapping Peffers' six phases to what was done in this project. Reference `context/docs/method/research-design.md`.
- ¶4: Validation vs evaluation — cite Wieringa (2014). This thesis validates (benchmarking, requirements traceability) rather than evaluates (production deployment). Acknowledge as limitation.
  MUST CITE: \textcite{wieringa2014dsm}

**3.2 Data Collection** (~2 pages)

- ¶1: Semi-structured interviews — define and justify. Allows structured comparison while preserving space for unexpected findings. Cite Oates (2022) or Braun & Clarke (2006).
  MUST CITE: \textcite{kvale2015interview}, \textcite{oates2022researching}
- ¶2: Participant selection — 7 coordinators/managers, varying company size (8–45 vehicles), varying system maturity (no system → Timpex → custom), geographic spread across Norway. Purposive sampling.
- ¶3: Interview guide — five themes: current tools/workflow, assignment criteria, sick-leave handling, automation attitudes, adoption criteria. Open questions. Guide included as appendix.
- ¶4: Process — phone interviews, 4 March 2026, recorded with consent. Duration [FILL IN]. All in Norwegian.
- ¶5: Transcription — Sonix.ai automated + manual correction. Full transcripts in `context/intervju/`.
- ¶6: Research ethics — describe informed consent, anonymisation/company naming decisions, data storage, and Sikt/NSD status. Do not invent approval status; use exactly what is documented in `context/docs/method/research-design.md`.
  MUST EVIDENCE: context/docs/method/research-design.md (Research ethics section)

**3.3 Data Analysis** (~1 page)

- ¶1: Thematic analysis following Braun and Clarke (2006) — familiarisation, coding, theme generation, review, definition.
  MUST CITE: \textcite{braun2006thematic}
- ¶2: From themes to requirements — pain points translated into functional requirements (MoSCoW). Fit/gap analysis compared needs against existing systems.
- ¶3: Limitations — 7 interviews: rich but not generalisable. Self-selection bias. Single-day collection, no longitudinal perspective.

**3.4 System Development Process** (~1 page)

- ¶1: Agile, iterative sprints. Embret as developer, Mikael providing requirements. Not formal Scrum.
  MUST CITE: \textcite{larman2003iterative}
- ¶2: Interleaving — user research fed directly into development priorities. Requirements refined as system took shape. Consistent with DSR's iterative design cycle.
- ¶3: Tech decisions — brief reference to stack (Next.js, Prisma, PostgreSQL, Python/Java solvers). Multi-engine approach chosen for benchmarking. Detail in Ch 4.4.
- ¶4: Timeline — reference sprint-log if filled, otherwise describe general progression (problem investigation → interviews → requirements → prototype → algorithm → refinement).

**3.5 Validity and Reliability** (~1 page)

- ¶1: Malterud's four criteria — systematic critical reflection, relevance, validity, reflexivity. Cite Malterud (2003).
  MUST CITE: \textcite{malterud2017kvalitative}
- ¶2: Interview validity — purposive sample, 7 companies, consistent findings across interviews (triangulation). Not generalisable to entire sector.
- ¶3: System validity — requirements traceability (features match needs?) + algorithm benchmarking (feasible quality plans?). Not production-evaluated — validation per Wieringa.
- ¶4: Researcher bias — dev team = research team. Risk of confirmation bias. Mitigated by structured requirements, interview-grounded analysis, transparent limitations.

---

## Chapter 4 — Findings
**Owner:** Both | **Target:** 10–15 pages | **Status:** Not started

**Purpose:** Present what was found and what was built — without interpretation.

> **Rule:** Present findings and system artefacts only. Do not interpret implications; interpretation belongs in Chapter 5.

### Sections and content

**4.1 Interview Findings** (~4 pages) — *Mikael*

- ¶1: Current planning processes — all manual, varying scale and complexity.
  MUST EVIDENCE: interviews-summary.md Theme 1 (Manuell planlegging)
- ¶2: Pain points — system slowness, tacit knowledge not captured, no capacity overview.
  MUST EVIDENCE: interviews-summary.md Theme 2 (Treghet); Theme 5 (Nøkkelpersonavhengighet)
- ¶3: Sick-leave handling — varies from trivial to daily burden.
  MUST EVIDENCE: interviews-summary.md Theme 3 (Sykefravær)
- ¶4: Attitudes toward automation — split between sceptical and positive.
  MUST EVIDENCE: interviews-summary.md Theme 4 (Holdninger til automatisering)
- ¶5: Assignment criteria — ranked list from interviews.
  MUST EVIDENCE: interviews-summary.md (assignment criteria ranking)

**4.2 Requirements** (~2 pages) — *Mikael*

- ¶1: Functional requirements derived from interviews (MoSCoW table).
  MUST EVIDENCE: context/docs/requirements/functional-requirements.md
- ¶2: Non-functional requirements.
  MUST EVIDENCE: context/docs/requirements/non-functional-requirements.md

**4.3 Fit/Gap Analysis** (~1.5 pages) — *Mikael*

- ¶1: What existing systems provide vs. what coordinators need.
  MUST EVIDENCE: fitgap-summary.md (fit items)
- ¶2: Fit table and gap table.
  MUST EVIDENCE: fitgap-summary.md (gap items, e.g., G-14)

**4.4 System Description** (~3 pages) — *Embret*

- ¶1: Architecture overview.
  MUST EVIDENCE: context/docs/tech/architecture.md
- ¶2: Key features — plan view, manual override, driver/vehicle management.
  MUST EVIDENCE: context/docs/tech/architecture.md; context/scope.md (in-scope features)
- ¶3: UI flow — what the coordinator sees and can do.
  MUST EVIDENCE: context/docs/user-research/ui-flow.md (if available)
- ¶4: Technology stack with brief justification.
  MUST EVIDENCE: context/docs/tech/tech-stack.md

**4.5 Optimisation Algorithm** (~3.5 pages) — *Embret*

- ¶1: Problem formulation.
  MUST EVIDENCE: context/docs/tech/algorithm.md (problem definition)
- ¶2: Chosen approach and justification.
  MUST EVIDENCE: context/docs/tech/algorithm.md; MUST CITE: \textcite{googleortools2026cpsat}, \textcite{perron2023cpsatlp}, \textcite{timefold2026solver}
- ¶3: Constraints modelled (hard and soft).
  MUST EVIDENCE: context/docs/tech/algorithm.md (constraint list)
- ¶4: Objective function.
  MUST EVIDENCE: context/docs/tech/algorithm.md
- ¶5: Known limitations.
  MUST EVIDENCE: context/docs/tech/algorithm.md (limitations section)
- ¶6: Solver benchmarking results — present dataset sizes, runtime, scheduled percentage, violation counts, and score comparison for greedy, OR-Tools, and Timefold where available. Clearly state if any solver was implemented but not fully benchmarked.
  MUST EVIDENCE: context/docs/tech/benchmark-results.md

---

## Chapter 5 — Discussion
**Owner:** Mikael | **Target:** 6–10 pages | **Status:** Not started

**Purpose:** Interpret findings in light of theory and research questions.

### Sections and content

**5.1 Does Ressursplanlegger Address the Identified Pain Points?** (~2 pages)

- ¶0: State the main research question. Frame the discussion as developing an answer through the following sections.
  MUST ANCHOR: context/context.md (RQ verbatim); thesis-spine.md (Ch 5 sentence)
- ¶1: Map interview findings (Ch 4.1) to implemented features (Ch 4.4).
  MUST ANCHOR: Ch 4.1 interview findings → Ch 4.4 system features
- ¶2: What is solved, what is partially solved, what remains unaddressed.
  MUST ANCHOR: Ch 4.3 fitgap (fit vs gap items)
- ¶3: Connect to theory — does the system match scheduling and HITL literature?
  MUST ANCHOR: Ch 2.1 scheduling theory; Ch 2.2 HITL theory

**5.2 Algorithm Performance and the Human-in-the-Loop** (~2 pages)

- ¶1: How well does the algorithm handle real-world constraints?
  MUST ANCHOR: Ch 4.5 algorithm (constraints + limitations + benchmarking results)
- ¶2: Where does human override remain necessary?
  MUST ANCHOR: Ch 4.4 system (manual override); Ch 4.1 interviews (tacit knowledge)
- ¶3: Connect to HITL theory from Ch 2.2.
  MUST ANCHOR: Ch 2.2 HITL theory (Parasuraman); Ch 4.4 system design
- ¶4: Is "suggest + override" the right design pattern?
  MUST ANCHOR: Ch 2.2 DSS vs automation; Ch 4.1 attitudes toward automation

**5.3 Adoption Barriers** (~2 pages)

- ¶1: Cost vs. benefit threshold.
  MUST ANCHOR: Ch 4.1 interviews (Bergen Bulk Transport, Nordic Crane)
- ¶2: Usability and trust in algorithm output.
  MUST ANCHOR: Ch 4.1 interviews (Ottem scepticism); Ch 2.2 trust in automation
- ¶3: Integration with billing systems — missing link.
  MUST ANCHOR: Ch 4.3 fitgap (billing gap); Ch 4.1 interviews
- ¶4: What would it take to deploy in production?
  MUST ANCHOR: Ch 4.4 system limitations; Ch 4.5 algorithm limitations

**5.4 Tacit Knowledge as a Design Challenge** (~1.5 pages)

- ¶1: How Ressursplanlegger formalises coordinator knowledge.
  MUST ANCHOR: Ch 4.4 system (driver profiles, competence); Ch 4.1 interviews (tacit knowledge)
- ¶2: What cannot be automated and why.
  MUST ANCHOR: Ch 4.1 interviews (assignment criteria); Ch 2.2 HITL limits
- ¶3: Implications for future system design.
  MUST ANCHOR: Ch 2.2 theory; Ch 4.5 algorithm limitations

**5.5 Sustainability and Ethical Considerations** (~1.5–2 pages)

- ¶1: Introduce SusAF framework.
  MUST CITE: \textcite{duboc2020requirements}
  MUST EVIDENCE: context/docs/method/sustainability-analysis.md
- ¶2: Present sustainability effects table.
  MUST EVIDENCE: context/docs/method/sustainability-analysis.md
- ¶3: Discuss key dilemmas.
  MUST ANCHOR: Ch 4.4 system features; Ch 2.2 automation vs. autonomy
- ¶4: Map effects to SDGs.
  MUST CITE: \textcite{un2015agenda2030}
- ¶5: Ethical considerations — discuss algorithmic fairness, accountability for errors, privacy/data handling, and health/working-condition effects as part of the sustainability analysis.
  MUST EVIDENCE: context/docs/method/sustainability-analysis.md (Ethical Perspective)
- ¶6: Limitations of sustainability analysis.
  MUST ANCHOR: Ch 5.6 limitations

**5.6 Limitations of This Study** (~1 page)

- ¶1: Small interview sample (7 companies).
  MUST ANCHOR: Ch 3.2 data collection; Ch 3.5 validity
- ¶2: System not deployed in production — no real-world performance data.
  MUST ANCHOR: Ch 3.4 development process; Ch 4.5 algorithm (no production data)
- ¶3: Development team = researchers (potential confirmation bias).
  MUST ANCHOR: Ch 3.5 validity (researcher roles)
- ¶4: User testing status — if `context/docs/user-research/user-tests.md` is still empty or template-only, state explicitly that no formal user testing was conducted and explain how this limits claims about usability, trust, and adoption.
  MUST ANCHOR: context/docs/user-research/user-tests.md if filled; otherwise explicit absence as limitation

---

## Chapter 6 — Conclusion
**Owner:** Both | **Target:** 2–4 pages | **Status:** Not started

**Purpose:** Summarise, answer research questions, suggest future work.

### Sections and content

**6.1 Summary** (~0.5 pages)

- ¶1: Summarise the problem and motivation from Chapter 1 in 2–3 sentences.
  MUST TRACE: Chapter 1 thesis-spine.md sentence
- ¶2: Summarise the theoretical foundation from Chapter 2 and the methodological approach from Chapter 3.
  MUST TRACE: Chapter 2 and Chapter 3 thesis-spine.md sentences
- ¶3: Summarise the findings, artefact, and discussion from Chapters 4 and 5, ending with the thesis's central qualification: the system supports but does not replace coordinator judgement.
  MUST TRACE: Chapter 4 and Chapter 5 thesis-spine.md sentences

**6.2 Answers to Research Questions** (~1 page)

- ¶1: Restate the main research question verbatim and answer it directly with a qualified statement grounded in the findings and discussion.
  MUST TRACE: main RQ → Ch 4 findings → Ch 5 discussion
- ¶2: Answer SQ1 explicitly: current practices, pain points, and needs of traffic coordinators.
  MUST TRACE: SQ1 → Ch 4.1 findings → Ch 5.1 discussion
- ¶3: Answer SQ2 explicitly: how an algorithm-assisted planning system should balance optimisation with coordinator control.
  MUST TRACE: SQ2 → relevant Ch 4 findings → relevant Ch 5 discussion
- ¶4: Answer SQ3 explicitly: the extent to which Ressursplanlegger addresses the identified needs and what its limitations are.
  MUST TRACE: SQ3 → relevant Ch 4 findings → relevant Ch 5 discussion
- ¶5: State the contribution of the thesis: the artefact, the requirements/finding synthesis, and the validation-based knowledge about algorithm-assisted planning in this domain.
  MUST TRACE: Ch 3 methodology → Ch 4 findings → Ch 5 discussion

**6.3 Future Work** (~1 page)

- ¶1: Driver mobile app for push notifications.
  MUST TRACE: Ch 4.1 interviews (feature requests); Ch 5.3 adoption barriers
- ¶2: Billing/invoicing integration.
  MUST TRACE: Ch 4.3 fitgap (billing gap); Ch 5.3 adoption barriers
- ¶3: Production pilot with a real transport company.
  MUST TRACE: Ch 5.6 limitations (no production data)
- ¶4: Real-time replanning for sick-leave events.
  MUST TRACE: Ch 4.1 interviews (sick-leave handling); Ch 4.5 algorithm limitations
- ¶5: Algorithm improvements with larger datasets.
  MUST TRACE: Ch 4.5 algorithm (known limitations); Ch 5.2 algorithm performance
- ¶6: Close with one domain-level claim about algorithm-assisted planning in transport: it is most valuable when it turns tacit knowledge into structured decision support while preserving human responsibility.
  MUST TRACE: thesis-spine.md Chapter 6 sentence
