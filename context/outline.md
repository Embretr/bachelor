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
- ¶1: The Norwegian transport sector and the role of the traffic coordinator.
  MUST CITE: context for transport sector scope (if source available in references.bib)
- ¶2: Current practice: manual assignment, tacit knowledge, legacy systems.
  MUST EVIDENCE: interviews-summary.md Theme 1 (Manuell planlegging)
- ¶3: Why this is a problem: inefficiency, error risk, key-person dependency.
  MUST EVIDENCE: interviews-summary.md Theme 2 (Treghet), Theme 5 (Nøkkelpersonavhengighet)
- ¶4: Why now: availability of optimisation tools, digital transformation in logistics.
  MUST CITE: relevant OR/logistics digitisation source from references.bib

**1.2 Research Questions** (~0.5 pages)
- ¶1: State the main research question (verbatim from `context/context.md`).
- ¶2: List 2–3 sub-questions.
- Do not discuss or justify here — that is for Chapter 3

**1.3 Scope and Delimitations** (~0.5 pages)
- ¶1: What the system does (brief).
  MUST EVIDENCE: context/scope.md (in-scope features)
- ¶2: What the thesis covers.
- ¶3: What is explicitly excluded and why.
  MUST EVIDENCE: context/scope.md (out-of-scope list)

**1.4 Thesis Structure** (~0.5 pages)
- ¶1: One sentence per chapter describing its contribution.
  MUST TRACE: each sentence → context/thesis-spine.md chapter sentence

---

## Chapter 2 — Theory
**Owner:** Mikael | **Target:** 8–12 pages | **Status:** Not started

**Purpose:** Establish the theoretical foundation underpinning system design and research approach.

### Sections and content

**2.1 Vehicle Routing Problem (VRP)** (~3 pages)
- ¶1: Define VRP and its origin in operations research.
  MUST CITE: \textcite{dantzig1959truck} (origin), \parencite{toth2014vrp} (comprehensive reference)
- ¶2: Key VRP variants: CVRP, VRPTW, multi-depot VRP.
  MUST CITE: \parencite{toth2014vrp} or equivalent VRP survey
- ¶3: How Ressursplanlegger's assignment problem maps to a VRP variant.
  MUST CITE: VRP formulation source; MUST EVIDENCE: context/docs/tech/algorithm.md
- ¶4: Key constraints relevant to transport planning: time windows, capacity, driver availability.
  MUST CITE: VRP constraint literature

**2.2 Resource Scheduling and Decision Support** (~3 pages)
- ¶1: General theory of resource scheduling in operations research.
  MUST CITE: scheduling/OR foundational source
- ¶2: Human-in-the-loop systems: definition and rationale.
  MUST CITE: \parencite{parasuraman2000model} or equivalent HITL source
- ¶3: Why full automation is often insufficient in dynamic environments.
  MUST CITE: HITL/automation literature
- ¶4: Decision support systems vs. fully automated dispatchers.
  MUST CITE: DSS literature source

**2.3 Transport Management Systems (TMS)** (~2 pages)
- ¶1: What a TMS is and what it typically includes.
  MUST CITE: TMS definition source
- ¶2: Existing systems relevant to the Norwegian context (Timpex, Trimtex, Opptur).
  MUST EVIDENCE: interviews-summary.md (system usage per company); fitgap-summary.md
- ¶3: Gaps in current TMS offerings — bridge to findings in Chapter 4.
  MUST EVIDENCE: fitgap-summary.md (gap items)

**2.4 Related Work** (~2 pages)
- ¶1: Academic work on algorithm-assisted dispatching in transport.
  MUST CITE: dispatching/routing literature
- ¶2: Studies on tacit knowledge in logistics operations.
  MUST CITE: tacit knowledge literature (e.g., Nonaka if in references.bib)
- ¶3: Position Ressursplanlegger relative to existing solutions.
  MUST CITE: related systems/papers; MUST EVIDENCE: fitgap-summary.md

---

## Chapter 3 — Methodology
**Owner:** Mikael | **Target:** 5–8 pages | **Status:** Not started

**Purpose:** Explain how the research was conducted, justify the choices, establish credibility.

### Sections and content

**3.1 Research Design** (~1.5 pages)
- ¶1: Define Design Science Research (DSR).
  MUST CITE: \textcite{peffers2007design} or \textcite{hevner2004design}
- ¶2: Explain why DSR fits a software development + user research project.
  MUST CITE: DSR methodology justification source
- ¶3: Connect DSR to Ressursplanlegger explicitly: the artefact is the platform.
  MUST CITE: DSR artefact definition
- ¶4: Limitations of DSR for this project.
  MUST CITE: DSR limitations literature

**3.2 Data Collection** (~2 pages)
- ¶1: Semi-structured interviews: definition and rationale for this approach.
  MUST CITE: qualitative methods source (e.g., Brinkmann & Kvale)
- ¶2: Participant selection: 7 companies, geographic spread, role (traffic coordinator).
  MUST EVIDENCE: context/context.md (user research summary table)
- ¶3: Interview guide: how it was developed, what topics it covered.
  MUST EVIDENCE: context/docs/method/research-design.md
- ¶4: Process: how interviews were conducted (phone, recording, consent).
  MUST EVIDENCE: context/docs/method/research-design.md
- ¶5: Transcription: Sonix.ai automated transcription + manual review.

**3.3 Data Analysis** (~1 page)
- ¶1: Thematic analysis: how themes were identified from transcripts.
  MUST CITE: thematic analysis methodology source (e.g., Braun & Clarke)
- ¶2: How findings fed into requirements (fit/gap analysis).
  MUST EVIDENCE: context/docs/method/research-design.md
- ¶3: Limitations: sample size, self-selection bias.

**3.4 System Development Process** (~1 page)
- ¶1: Agile/iterative development approach.
  MUST CITE: agile/iterative methodology source
- ¶2: How user research and development were interleaved.
  MUST EVIDENCE: context/docs/project/sprint-log.md
- ¶3: Sprint structure and decision points.
  MUST EVIDENCE: context/docs/project/sprint-log.md

**3.5 Validity and Reliability** (~1 page)
- ¶1: Interview validity: how representative is the sample?
  MUST CITE: qualitative validity criteria (e.g., Malterud or Lincoln & Guba)
- ¶2: System validity: how well does the system solve the stated problem?
- ¶3: Researcher roles and potential bias (Embret: development, Mikael: interviews).

---

## Chapter 4 — Findings
**Owner:** Both | **Target:** 10–15 pages | **Status:** Not started

**Purpose:** Present what was found and what was built — without interpretation.

### Sections and content

**4.1 Interview Findings** (~4 pages) — *Mikael*
- ¶1: Current planning processes (all manual, varying scale and complexity).
  MUST EVIDENCE: interviews-summary.md Theme 1 (Manuell planlegging)
- ¶2: Pain points: system slowness, tacit knowledge not captured, no capacity overview.
  MUST EVIDENCE: interviews-summary.md Theme 2 (Treghet); Theme 5 (Nøkkelpersonavhengighet)
- ¶3: Sick-leave handling: varies from trivial to daily burden.
  MUST EVIDENCE: interviews-summary.md Theme 3 (Sykefravær)
- ¶4: Attitudes toward automation: split between sceptical and positive.
  MUST EVIDENCE: interviews-summary.md Theme 4 (Holdninger til automatisering)
- ¶5: Assignment criteria: ranked list from interviews.
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
- ¶2: Key features: plan view, manual override, driver/vehicle management.
  MUST EVIDENCE: context/docs/tech/architecture.md; context/scope.md (in-scope features)
- ¶3: UI flow: what the coordinator sees and can do.
  MUST EVIDENCE: context/docs/user-research/ui-flow.md (if available)
- ¶4: Technology stack with brief justification.
  MUST EVIDENCE: context/docs/tech/tech-stack.md

**4.5 Optimisation Algorithm** (~3 pages) — *Embret*
- ¶1: Problem formulation.
  MUST EVIDENCE: context/docs/tech/algorithm.md (problem definition)
- ¶2: Chosen approach and justification.
  MUST EVIDENCE: context/docs/tech/algorithm.md; MUST CITE: OR-Tools/solver literature
- ¶3: Constraints modelled (hard and soft).
  MUST EVIDENCE: context/docs/tech/algorithm.md (constraint list)
- ¶4: Objective function.
  MUST EVIDENCE: context/docs/tech/algorithm.md
- ¶5: Known limitations.
  MUST EVIDENCE: context/docs/tech/algorithm.md (limitations section)

---

## Chapter 5 — Discussion
**Owner:** Mikael | **Target:** 6–10 pages | **Status:** Not started

**Purpose:** Interpret findings in light of theory and research questions.

### Sections and content

**5.1 Does Ressursplanlegger Address the Identified Pain Points?** (~2 pages)
- ¶1: Ressursplanlegger fills the planning gap.
  MUST ANCHOR: Ch 4.3 fitgap (core gap); Ch 2.3 TMS landscape
- ¶2: Map interview findings (Chapter 4.1) to implemented features (Chapter 4.4).
  MUST ANCHOR: Ch 4.1 interview findings → Ch 4.4 system features
- ¶3: What is solved, what is partially solved, what remains unaddressed.
  MUST ANCHOR: Ch 4.3 fitgap (fit vs gap items)
- ¶4: Connect to theory: does the system match what the VRP/scheduling literature suggests?
  MUST ANCHOR: Ch 2.1 VRP theory; Ch 2.2 scheduling theory

**5.2 Algorithm Performance and the Human-in-the-Loop** (~2 pages)
- ¶1: How well does the algorithm handle real-world constraints?
  MUST ANCHOR: Ch 4.5 algorithm (constraints + limitations)
- ¶2: Where does human override remain necessary?
  MUST ANCHOR: Ch 4.4 system (manual override feature); Ch 4.1 interviews (tacit knowledge)
- ¶3: Connect to human-in-the-loop theory from Chapter 2.2.
  MUST ANCHOR: Ch 2.2 HITL theory (Parasuraman); Ch 4.4 system design
- ¶4: Is "suggest + override" the right design pattern for this domain?
  MUST ANCHOR: Ch 2.2 DSS vs automation; Ch 4.1 attitudes toward automation

**5.3 Adoption Barriers** (~2 pages)
- ¶1: Cost vs. benefit threshold.
  MUST ANCHOR: Ch 4.1 interviews (Bergen Bulk Transport, Nordic Crane)
- ¶2: Usability and trust in algorithm output.
  MUST ANCHOR: Ch 4.1 interviews (Ottem scepticism); Ch 2.2 trust in automation
- ¶3: Integration with billing systems — missing link.
  MUST ANCHOR: Ch 4.3 fitgap (billing gap); Ch 4.1 interviews
- ¶4: What would it take to deploy this in production?
  MUST ANCHOR: Ch 4.4 system limitations; Ch 4.5 algorithm limitations

**5.4 Tacit Knowledge as a Design Challenge** (~1.5 pages)
- ¶1: How Ressursplanlegger attempts to formalise coordinator knowledge.
  MUST ANCHOR: Ch 4.4 system (driver profiles, competence); Ch 4.1 interviews (tacit knowledge)
- ¶2: What cannot be automated and why.
  MUST ANCHOR: Ch 4.1 interviews (assignment criteria); Ch 2.2 HITL limits
- ¶3: Implications for future system design.
  MUST ANCHOR: Ch 2.2 theory; Ch 4.5 algorithm limitations

**5.5 Limitations of This Study** (~1 page)
- ¶1: Small interview sample (7 companies).
  MUST ANCHOR: Ch 3.2 data collection; Ch 3.5 validity
- ¶2: System not deployed in production — no real-world performance data.
  MUST ANCHOR: Ch 3.4 development process; Ch 4.5 algorithm (no production data)
- ¶3: Development team = researchers (potential confirmation bias).
  MUST ANCHOR: Ch 3.5 validity (researcher roles)

---

## Chapter 6 — Conclusion
**Owner:** Both | **Target:** 2–4 pages | **Status:** Not started

**Purpose:** Summarise, answer research questions, suggest future work.

### Sections and content

**6.1 Summary** (~0.5 pages)
- ¶1: One paragraph per chapter — what each contributed.
  MUST TRACE: each paragraph → corresponding chapter's thesis-spine.md sentence

**6.2 Answers to Research Questions** (~1 page)
- ¶1: Answer the main research question directly.
  MUST TRACE: main RQ → Ch 4 findings → Ch 5 discussion
- ¶2: Answer SQ1.
  MUST TRACE: SQ1 → Ch 4.1 findings → Ch 5.1 discussion
- ¶3: Answer SQ2.
  MUST TRACE: SQ2 → relevant Ch 4 findings → relevant Ch 5 discussion

**6.3 Future Work** (~1 page)
- ¶1: Driver mobile app for push notifications.
  MUST TRACE: Ch 4.1 interviews (feature requests); Ch 5.3 adoption barriers
- ¶2: Billing/invoicing integration.
  MUST TRACE: Ch 4.3 fitgap (billing gap); Ch 5.3 adoption barriers
- ¶3: Production pilot with a real transport company.
  MUST TRACE: Ch 5.5 limitations (no production data)
- ¶4: Real-time replanning for sick-leave events.
  MUST TRACE: Ch 4.1 interviews (sick-leave handling); Ch 4.5 algorithm limitations
- ¶5: Algorithm improvements with larger datasets.
  MUST TRACE: Ch 4.5 algorithm (known limitations); Ch 5.2 algorithm performance
