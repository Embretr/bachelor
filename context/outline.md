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
- The Norwegian transport sector and the role of the traffic coordinator
- Current practice: manual assignment, tacit knowledge, legacy systems
- Why this is a problem: inefficiency, error risk, key-person dependency
- Why now: availability of optimisation tools, digital transformation in logistics

**1.2 Research Questions** (~0.5 pages)
- State the main research question (verbatim from `context/context.md`)
- List 2–3 sub-questions
- Do not discuss or justify here — that is for Chapter 3

**1.3 Scope and Delimitations** (~0.5 pages)
- What the system does (brief)
- What the thesis covers
- What is explicitly excluded and why

**1.4 Thesis Structure** (~0.5 pages)
- One sentence per chapter describing its contribution
- Must match `context/thesis-spine.md`

---

## Chapter 2 — Theory
**Owner:** Mikael | **Target:** 8–12 pages | **Status:** Not started

**Purpose:** Establish the theoretical foundation underpinning system design and research approach.

### Sections and content

**2.1 Vehicle Routing Problem (VRP)** (~3 pages)
- Definition of VRP and its origin in operations research
- Key VRP variants: CVRP, VRPTW, multi-depot VRP
- How Ressursplanlegger's assignment problem maps to a VRP variant
- Key constraints relevant to transport planning: time windows, capacity, driver availability
- Source needed: Toth & Vigo (2002) or similar foundational VRP text

**2.2 Resource Scheduling and Decision Support** (~3 pages)
- General theory of resource scheduling in operations research
- Human-in-the-loop systems: definition and rationale
- Why full automation is often insufficient in dynamic environments
- Decision support systems vs. fully automated dispatchers
- Source needed: human-in-the-loop automation literature

**2.3 Transport Management Systems (TMS)** (~2 pages)
- What a TMS is and what it typically includes
- Existing systems relevant to the Norwegian context (Timpex, Trimtex, Opptur)
- Gaps in current TMS offerings — bridge to findings in Chapter 4

**2.4 Related Work** (~2 pages)
- Academic work on algorithm-assisted dispatching in transport
- Studies on tacit knowledge in logistics operations
- Position Ressursplanlegger relative to existing solutions

---

## Chapter 3 — Methodology
**Owner:** Mikael | **Target:** 5–8 pages | **Status:** Not started

**Purpose:** Explain how the research was conducted, justify the choices, establish credibility.

### Sections and content

**3.1 Research Design** (~1.5 pages)
- Define Design Science Research (DSR) — one sentence
- Explain why DSR fits a software development + user research project
- Connect DSR to Ressursplanlegger explicitly: the artefact is the platform
- Limitations of DSR for this project
- Source needed: Hevner et al. (2004) or Peffers et al. (2007)

**3.2 Data Collection** (~2 pages)
- Semi-structured interviews: definition and rationale for this approach
- Participant selection: 7 companies, geographic spread, role (traffic coordinator)
- Interview guide: how it was developed, what topics it covered
- Process: how interviews were conducted (phone, recording, consent)
- Transcription: Sonix.ai automated transcription + manual review

**3.3 Data Analysis** (~1 page)
- Thematic analysis: how themes were identified from transcripts
- How findings fed into requirements (fit/gap analysis)
- Limitations: sample size, self-selection bias

**3.4 System Development Process** (~1 page)
- Agile/iterative development approach
- How user research and development were interleaved
- Sprint structure and decision points
- Reference `context/docs/project/sprint-log.md` for detail

**3.5 Validity and Reliability** (~1 page)
- Interview validity: how representative is the sample?
- System validity: how well does the system solve the stated problem?
- Researcher roles and potential bias (Embret: development, Mikael: interviews)

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

**5.5 Limitations of This Study** (~1 page)
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
