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

### Sections and content

**2.1 Resource Scheduling** (~2.5 pages)

- ¶1: Define resource scheduling — assigning a set of limited resources (people, vehicles) to tasks over time, subject to constraints on availability, task requirements, and temporal dependencies. Cite `\textcite{pinedo2016scheduling}`. Note analogous domains: nurse scheduling, crew scheduling, driver scheduling — all share the structure of matching resources to tasks under constraints.
  MUST CITE: \textcite{pinedo2016scheduling}
- ¶2: Multi-resource scheduling — Ressursplanlegger assigns *both* an employee and a vehicle to each assignment. This increases combinatorial complexity compared to single-resource problems. The Ressursplanlegger problem: assignments = tasks with fixed time windows and resource requirements; drivers + vehicles = resources with competency, availability, and capacity constraints; objective = maximise coverage + balance soft constraints.
- ¶3: Hard and soft constraints — hard constraints must be satisfied for a plan to be feasible (competencies, availability, no double-booking, vehicle type). Soft constraints define preferences optimised by the algorithm (workload balance, driver preferences, priority). Each soft constraint carries a configurable weight. Cite `\textcite{rossi2006constraint}`. Link to the system's actual constraint model from `context/docs/tech/algorithm.md`.
  MUST CITE: \textcite{rossi2006constraint}; MUST EVIDENCE: context/docs/tech/algorithm.md
- ¶4: NP-hardness and the multi-engine approach — resource scheduling at real fleet sizes is NP-hard; exact methods become infeasible as instance size grows. This motivates heuristics: greedy (instant baseline), CP-SAT (near-optimal within time limit), Timefold (metaheuristic for large instances). The Vehicle Routing Problem (VRP) is an adjacent theoretical area with similar structure — cite `\textcite{dantzig1959truck}` and `\textcite{braekers2016vrp}` — but Ressursplanlegger's problem diverges from VRP in a key way: assignments have fixed times and locations, so the algorithm decides *who* does what, not *in which order*. Sequencing is not part of the problem.
  MUST CITE: \textcite{pinedo2016scheduling}
- ¶5: Solver comparison — greedy O(n × m), no optimality guarantee; CP-SAT complete solver with configurable time limit, near-optimal for ≤500 assignments; Timefold metaheuristic (tabu search, simulated annealing) for large or multi-day instances. Each occupies a different point on the speed-quality tradeoff. Cite `\textcite{rossi2006constraint}` for constraint programming foundations.
  MUST CITE: \textcite{rossi2006constraint}

**2.2 Human-in-the-Loop Automation** (~2.5 pages)

- ¶1: Define human-in-the-loop (HITL) automation — a design pattern where an automated process produces a recommendation or plan, but a human reviews, adjusts, and approves before it takes effect. Cite `\textcite{parasuraman2000automation}` and their 10-level automation scale. Position Ressursplanlegger at level 5–6 (system suggests, human approves).
  MUST CITE: \textcite{parasuraman2000automation}
- ¶2: Why HITL is necessary in this domain — unpredictability (weather, cancellations, sick leave), tacit knowledge (driver preferences, customer relationships, route knowledge), trust (coordinators won't use a system they can't override). Ground in interview findings implicitly — detailed evidence in Ch 4.
- ¶3: The "suggest + override" design pattern — algorithm does heavy lifting, coordinator applies judgment. This is Ressursplanlegger's core interaction model.
  MUST EVIDENCE: context/docs/tech/architecture.md
- ¶4: Trust and adoption — coordinators will not rely on a system whose decisions they cannot understand and override. Cite `\textcite{lee2004trust}`. Connect to adoption barriers (developed in Ch 5.3).
  MUST CITE: \textcite{lee2004trust}
- ¶5: HITL as a design constraint — the system must expose its reasoning (conflict detection, scoring breakdown) so the coordinator can make informed corrections. This shapes the UI as much as the algorithm.
  MUST EVIDENCE: context/docs/tech/architecture.md

**2.3 Transport Management Systems (TMS)** (~1.5 pages)

- ¶1: Define TMS as a software category — order management, route planning, carrier management, freight billing. Cite industry source if available (check literature-list).
  MUST CITE: \textcite{griffis2007tms}, \textcite{heinbach2022datadriven}
- ¶2: TMS landscape in Norway — Timpex, Trimtex, Opptur. Describe what they do well (invoicing, order tracking) and what they lack (planning, optimisation). Keep factual — detailed gap analysis is in Ch 4.3.
  MUST EVIDENCE: interviews-summary.md (system usage per company); fitgap-summary.md
- ¶3: The planning gap — none of the existing systems address the space between "order exists" and "driver is assigned." This is where Ressursplanlegger fits. Bridge sentence to Chapter 4.
  MUST EVIDENCE: fitgap-summary.md (gap items)

**2.4 Design Science Research** (~1.5 pages)

- ¶1: Define DSR — creating and evaluating artefacts to address practical problems. Cite `\textcite{hevner2004design}` and `\textcite{peffers2007dsrm}`.
  MUST CITE: \textcite{hevner2004design}, \textcite{peffers2007dsrm}
- ¶2: Why DSR fits this project — the contribution is both the artefact (Ressursplanlegger) and the knowledge gained through building and validating it. DSR structures the process from problem identification through evaluation.
- ¶3: Validation vs evaluation — cite `\textcite{wieringa2014dsm}`. Explain that this thesis validates (predicts behaviour through benchmarking and requirements traceability) rather than evaluates (deploys in production). Bridge to Chapter 3 where the specific DSR application is detailed.
  MUST CITE: \textcite{wieringa2014dsm}
- ¶4: Bridge to methodology — make explicit that this section explains DSR as theory, while Chapter 3 applies the DSR phases to this specific project. This avoids repeating methodology content in the theory chapter.

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
