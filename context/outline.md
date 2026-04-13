# Thesis Outline — Ressursplanlegger

> Claude reads this before writing any chapter.
> Contains section-level outlines with content notes and target lengths.
> Update as structure evolves — but keep thesis-spine.md consistent with changes.

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
- ¶4: Consequences — inefficiency, key-person dependency, error risk (overtime violations, double-booking, wrong competencies). These are real costs for companies.
- ¶5: Why now — constraint-based optimisation tools (OR-Tools, Timefold) have matured, making algorithm-assisted planning accessible for SMEs. Digital transformation in logistics is accelerating but planning remains a manual gap.
- ¶6: Introduce Ressursplanlegger in one paragraph — a web-based platform that generates optimised daily plans and lets the coordinator review, adjust, and approve. Human-in-the-loop by design.

**1.2 Research Questions** (~0.5 pages)

- ¶1: State the main research question verbatim from `context/context.md`.
- ¶2: List the three sub-questions. For each, one sentence explaining what it addresses (problem → solution → evaluation).
- Do NOT discuss or justify — that is for Chapter 3.

**1.3 Scope and Delimitations** (~0.5 pages)

- ¶1: What the system covers — daily planning, driver/vehicle assignment, conflict detection, multi-engine optimisation. Reference `context/scope.md`.
- ¶2: What is explicitly excluded — invoicing, driver mobile app, GPS tracking, weekly/monthly planning. State why briefly (time constraints, not part of the research question).
- ¶3: Division of work — Mikael (user research, requirements, thesis writing), Embret (system development, algorithm implementation). Both contribute to discussion and analysis.

**1.4 Thesis Structure** (~0.5 pages)

- One paragraph: "This thesis is structured as follows." Then one sentence per chapter describing its contribution. Must match `context/thesis-spine.md` exactly.

---

## Chapter 2 — Theory
**Owner:** Mikael | **Target:** 8–12 pages | **Status:** Not started

**Purpose:** Establish the theoretical foundation underpinning system design and research approach.

### Sections and content

**2.1 Vehicle Routing Problem (VRP)** (~3 pages)

- ¶1: Define the VRP — combinatorial optimisation problem, set of customers to serve, fleet of vehicles, minimise cost. Origin: Dantzig & Ramser (1959). Cite `\textcite{dantzig1959truck}`.
- ¶2: VRP variants relevant to this project — CVRP (capacity), VRPTW (time windows), heterogeneous fleet (different vehicle types), multi-depot (multiple departments). Cite `\textcite{toth2014vrp}`.
- ¶3: How Ressursplanlegger's problem maps to VRP — assignments = customers, driver+vehicle = vehicles, objective = coverage + balance. But note the distinction: Ressursplanlegger focuses on *assignment* (who does what) rather than *routing* (in which order). The problem is more precisely a resource-constrained scheduling problem with VRP-like constraints.
- ¶4: NP-hardness and practical implications — exact solutions infeasible for real fleet sizes, heuristics and metaheuristics needed. This motivates the multi-engine approach (greedy, CP-SAT, Timefold).
- ¶5: Constraint types — hard constraints (must satisfy: competencies, availability, no double-booking) vs. soft constraints (optimise: workload balance, preferences). Link to the system's actual constraint model from `context/docs/tech/algorithm.md`.

**2.2 Resource Scheduling and Human-in-the-Loop** (~3 pages)

- ¶1: Define resource scheduling broadly — assigning limited resources to tasks over time, subject to constraints. Cite `\textcite{pinedo2016scheduling}`. Mention analogous domains: nurse scheduling, crew scheduling.
- ¶2: Multi-resource scheduling — Ressursplanlegger assigns *both* an employee and a vehicle to each assignment. This increases combinatorial complexity compared to single-resource problems.
- ¶3: Human-in-the-loop (HITL) automation — define the concept. Cite `\textcite{parasuraman2000automation}` and their 10-level automation scale. Position Ressursplanlegger at level 5–6 (system suggests, human approves).
- ¶4: Why HITL is necessary in this domain — unpredictability (weather, cancellations, sick leave), tacit knowledge (driver preferences, customer relationships, route knowledge), trust (coordinators won't use a system they can't override). Ground in interview findings implicitly — detailed evidence in Ch 4.
- ¶5: The "suggest + override" design pattern — algorithm does heavy lifting, coordinator applies judgment. This is Ressursplanlegger's core interaction model.

**2.3 Transport Management Systems (TMS)** (~2 pages)

- ¶1: Define TMS as a software category — order management, route planning, carrier management, freight billing. Cite industry source if available (check literature-list).
- ¶2: TMS landscape in Norway — Timpex, Trimtex, Opptur. Describe what they do well (invoicing, order tracking) and what they lack (planning, optimisation). Keep factual — detailed gap analysis is in Ch 4.3.
- ¶3: The planning gap — none of the existing systems address the space between "order exists" and "driver is assigned." This is where Ressursplanlegger fits. Bridge sentence to Chapter 4.

**2.4 Design Science Research** (~1.5 pages)

- ¶1: Define DSR — creating and evaluating artefacts to address practical problems. Cite `\textcite{hevner2004dsr}` and `\textcite{peffers2007dsr}`.
- ¶2: Why DSR fits this project — the contribution is both the artefact (Ressursplanlegger) and the knowledge gained through building and validating it. DSR structures the process from problem identification through evaluation.
- ¶3: Validation vs evaluation — cite `\textcite{wieringa2014dsr}`. Explain that this thesis validates (predicts behaviour through benchmarking and requirements traceability) rather than evaluates (deploys in production). Bridge to Chapter 3 where the specific DSR application is detailed.

> **Note:** Section 2.4 was previously "Related Work." Moved DSR here because sensor criterion NRT3 (Theoretical Insight) explicitly covers "knowledge of relevant methods." Related work on algorithm-assisted dispatching is now woven into 2.1 and 2.2 rather than a separate section — avoiding a thin, disconnected related-work section.

---

## Chapter 3 — Methodology
**Owner:** Mikael | **Target:** 5–8 pages | **Status:** Not started

**Purpose:** Explain how the research was conducted, justify the choices, establish credibility.

### Sections and content

**3.1 Research Design** (~1.5 pages)

- ¶1: State the methodology — Design Science Research (DSR). Cite Peffers (2007) for six-phase model and Hevner (2004) for the framework. One-sentence definition.
- ¶2: Why DSR fits — combines building a software artefact with investigating a real problem. Contrast briefly with pure case study (no artefact) and pure development (no research).
- ¶3: DSR phases applied — table mapping Peffers' six phases to what was done in this project. Reference `context/docs/method/research-design.md`.
- ¶4: Validation vs evaluation — cite Wieringa (2014). This thesis validates (benchmarking, requirements traceability) rather than evaluates (production deployment). Acknowledge as limitation.

**3.2 Data Collection** (~2 pages)

- ¶1: Semi-structured interviews — define and justify. Allows structured comparison while preserving space for unexpected findings. Cite Oates (2022) or Braun & Clarke (2006).
- ¶2: Participant selection — 7 coordinators/managers, varying company size (8–45 vehicles), varying system maturity (no system → Timpex → custom), geographic spread across Norway. Purposive sampling.
- ¶3: Interview guide — five themes: current tools/workflow, assignment criteria, sick-leave handling, automation attitudes, adoption criteria. Open questions. Guide included as appendix.
- ¶4: Process — phone interviews, 4 March 2026, recorded with consent. Duration [FILL IN]. All in Norwegian.
- ¶5: Transcription — Sonix.ai automated + manual correction. Full transcripts in `context/intervju/`.

**3.3 Data Analysis** (~1 page)

- ¶1: Thematic analysis following Braun & Clarke (2006) — familiarisation, coding, theme generation, review, definition.
- ¶2: From themes to requirements — pain points translated into functional requirements (MoSCoW). Fit/gap analysis compared needs against existing systems.
- ¶3: Limitations — 7 interviews: rich but not generalisable. Self-selection bias. Single-day collection, no longitudinal perspective.

**3.4 System Development Process** (~1 page)

- ¶1: Agile, iterative sprints. Embret as developer, Mikael providing requirements. Not formal Scrum.
- ¶2: Interleaving — user research fed directly into development priorities. Requirements refined as system took shape. Consistent with DSR's iterative design cycle.
- ¶3: Tech decisions — brief reference to stack (Next.js, Prisma, PostgreSQL, Python/Java solvers). Multi-engine approach chosen for benchmarking. Detail in Ch 4.4.
- ¶4: Timeline — reference sprint-log if filled, otherwise describe general progression (problem investigation → interviews → requirements → prototype → algorithm → refinement).

**3.5 Validity and Reliability** (~1 page)

- ¶1: Malterud's four criteria — systematic critical reflection, relevance, validity, reflexivity. Cite Malterud (2003).
- ¶2: Interview validity — purposive sample, 7 companies, consistent findings across interviews (triangulation). Not generalisable to entire sector.
- ¶3: System validity — requirements traceability (features match needs?) + algorithm benchmarking (feasible quality plans?). Not production-evaluated — validation per Wieringa.
- ¶4: Researcher bias — dev team = research team. Risk of confirmation bias. Mitigated by structured requirements, interview-grounded analysis, transparent limitations.

---

## Chapter 4 — Findings
**Owner:** Both | **Target:** 10–15 pages | **Status:** Not started

**Purpose:** Present what was found and what was built — without interpretation.

### Sections and content

**4.1 Interview Findings** (~4 pages) — *Mikael*
- Current planning processes (all manual, varying scale and complexity)
- Pain points: system slowness, tacit knowledge not captured, no capacity overview
- Sick-leave handling: varies from trivial to daily burden
- Attitudes toward automation: split between sceptical and positive
- Assignment criteria: ranked list from `context/interviews-summary.md`
- Source: `context/interviews-summary.md`

**4.2 Requirements** (~2 pages) — *Mikael*
- Functional requirements derived from interviews (MoSCoW table)
- Non-functional requirements
- Source: `context/docs/requirements/functional-requirements.md` + `context/docs/requirements/non-functional-requirements.md`

**4.3 Fit/Gap Analysis** (~1.5 pages) — *Mikael*
- What existing systems provide vs. what coordinators need
- Fit table and gap table
- Source: `context/fitgap-summary.md`

**4.4 System Description** (~3 pages) — *Embret*
- Architecture overview (reference `context/docs/tech/architecture.md`)
- Key features: plan view, manual override, driver/vehicle management
- UI flow: what the coordinator sees and can do
- Technology stack with brief justification

**4.5 Optimisation Algorithm** (~3 pages) — *Embret*
- Problem formulation
- Chosen approach and justification
- Constraints modelled (hard and soft)
- Objective function
- Known limitations
- Source: `context/docs/tech/algorithm.md`

---

## Chapter 5 — Discussion
**Owner:** Mikael | **Target:** 6–10 pages | **Status:** Not started

**Purpose:** Interpret findings in light of theory and research questions.

### Sections and content

**5.1 Does Ressursplanlegger Address the Identified Pain Points?** (~2 pages)
- Map interview findings (Chapter 4.1) to implemented features (Chapter 4.4)
- What is solved, what is partially solved, what remains unaddressed
- Connect to theory: does the system match what the VRP/scheduling literature suggests?

**5.2 Algorithm Performance and the Human-in-the-Loop** (~2 pages)
- How well does the algorithm handle real-world constraints?
- Where does human override remain necessary?
- Connect to human-in-the-loop theory from Chapter 2.2
- Is "suggest + override" the right design pattern for this domain?

**5.3 Adoption Barriers** (~2 pages)
- Cost vs. benefit threshold (raised by Bergen Bulk Transport, Nordic Crane)
- Usability and trust in algorithm output (Ottem's scepticism)
- Integration with billing systems — missing link
- What would it take to deploy this in production?

**5.4 Tacit Knowledge as a Design Challenge** (~1.5 pages)
- How Ressursplanlegger attempts to formalise coordinator knowledge (licence, competence, experience)
- What cannot be automated and why
- Implications for future system design

**5.5 Sustainability** (~1.5–2 pages)
- Introduce SusAF framework (five dimensions, three effect levels) — cite Duboc et al. (2020)
- Present sustainability effects table (see `context/docs/method/sustainability-analysis.md`)
- Discuss 2–3 key dilemmas: efficiency vs. deskilling, automation vs. autonomy, resource savings vs. energy consumption
- Map effects to relevant SDGs (8, 9, 12 primarily; 3, 11, 13 secondarily) — use sub-targets, not just top-level goals
- Acknowledge limitations: effects are projected, not measured; no production deployment

**5.6 Limitations of This Study** (~1 page)
- Small interview sample (7 companies)
- System not deployed in production — no real-world performance data
- Development team = researchers (potential confirmation bias)

---

## Chapter 6 — Conclusion
**Owner:** Both | **Target:** 2–4 pages | **Status:** Not started

**Purpose:** Summarise, answer research questions, suggest future work.

### Sections and content

**6.1 Summary** (~0.5 pages)
- One paragraph per chapter — what each contributed

**6.2 Answers to Research Questions** (~1 page)
- Address the main research question directly
- Address each sub-question explicitly

**6.3 Future Work** (~1 page)
- Driver mobile app for push notifications
- Billing/invoicing integration
- Production pilot with a real transport company
- Real-time replanning for sick-leave events
- Algorithm improvements with larger datasets
