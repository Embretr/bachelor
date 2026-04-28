# Sustainability Analysis — Ressursplanlegger

> **Owner: Mikael** — used for the sustainability section in Chapter 5 (Discussion).
> This file distills what the AI agents need to write a good sustainability reflection.
> Source: NTNU guidance on sustainability in bachelor/master theses, SusAF framework,
> UN SDGs, and Karlskrona Manifesto.

---

## What NTNU Requires

The course description requires:

> "I oppgaven skal det reflekteres over oppgavens bærekraftrelevans med utgangspunkt i FNs bærekraftsmål."

Sensors look for **critical reflection** — not just mentioning SDGs, but:
- Discussing how the project affects sustainability **directly and indirectly**
- Discussing **dilemmas** where different concerns must be weighed against each other
- Explaining **why** specific SDGs and dimensions are relevant to this project (not just listing them)
- Integrating sustainability from the start, not as an afterthought

A good sustainability section demonstrates the student's ability to critically reflect on the consequences of their work.

---

## Definition of Sustainability

> "Sustainable development is development that meets the needs of the present without compromising the ability of future generations to meet their own needs."
> — Brundtland, G. H. (1987). *Report of the World Commission on Environment and Development: Our Common Future.*

Sustainability is systemic — it is never an isolated property. It spans multiple dimensions and must be understood across different timescales and orders of effect.

---

## Framework: SusAF (Sustainability Awareness Framework)

NTNU recommends using SusAF to structure the analysis. It has two axes:

### Five Dimensions of Sustainability

Each dimension has specific topics that guide the analysis. Use the topics as prompts when identifying effects.

| Dimension | Topics | Guiding questions for Ressursplanlegger |
|-----------|--------|----------------------------------------|
| **Social** | Community, trust, inclusiveness, equity, participation | Can the system affect how coordinators participate in their work community? Does it change trust dynamics? Does it treat all users equitably? |
| **Individual** | Health, lifelong learning, privacy, safety, agency | Does the system affect coordinator well-being or cognitive load? Does it support or hinder learning? Does it preserve user agency? Does it handle personal data (driver info) responsibly? |
| **Environmental** | Material & resources, waste & pollution, biodiversity, energy, logistics | Does the system affect fuel consumption or vehicle wear? What energy does the platform itself consume? Does optimised logistics reduce environmental impact? |
| **Economic** | Value creation, CRM, supply chain, governance, innovation | Does the system create economic value for transport companies? Does it change the supply chain for transport services? Does it enable innovation in the sector? |
| **Technical** | Maintainability, usability, adaptability, security, scalability | Is the system maintainable long-term? Can it adapt to changing requirements? Is it secure? Can it scale to larger fleets? |

> Source for dimension definitions — Karlskrona Manifesto (Becker et al., 2015):
> - **Individual sustainability:** maintaining human capital (health, education, skills, knowledge, access to services)
> - **Social sustainability:** preserving societal communities in their solidarity and services
> - **Economic sustainability:** maintaining capital and added value
> - **Environmental sustainability:** improving human welfare by protecting natural resources (water, land, air, minerals, ecosystem services)
> - **Technical sustainability:** longevity of information, systems, and infrastructure and their adequate evolution with changing conditions

### Three Levels of Effects

| Level | Definition | Example for Ressursplanlegger |
|-------|-----------|-------------------------------|
| **Immediate** (1st order) | Direct effects from the system's existence and production | Energy used by servers; development resources consumed |
| **Enabling** (2nd order) | Effects from ongoing use of the system | Reduced manual planning time; better working conditions for coordinators |
| **Structural** (3rd order) | Societal changes from wide-scale, long-term use | Shift in transport industry toward data-driven planning; changed role of traffic coordinator |

---

## Relevant SDGs for Ressursplanlegger

Based on analysis of the project's domain and effects:

### Directly Relevant

| SDG | Name | Why relevant |
|:---:|------|-------------|
| **8** | Decent Work and Economic Growth | The system improves working conditions for traffic coordinators by reducing repetitive manual work and cognitive load. It supports economic productivity in the transport sector through more efficient resource utilisation. |
| **9** | Industry, Innovation, and Infrastructure | Ressursplanlegger is an innovation in transport logistics infrastructure — introducing algorithm-assisted planning to a sector that currently relies on manual processes and legacy systems. |
| **12** | Responsible Consumption and Production | More efficient driver/vehicle assignment can reduce empty runs, fuel consumption, and vehicle wear — contributing to more responsible use of transport resources. |

### Indirectly Relevant

| SDG | Name | Why relevant |
|:---:|------|-------------|
| **3** | Good Health and Well-being | Automated conflict detection for overtime and rest-time violations protects driver health and safety. Reduced cognitive load improves coordinator well-being. |
| **11** | Sustainable Cities and Communities | Better transport logistics contributes to sustainable urban infrastructure — fewer unnecessary vehicle movements, reduced emissions in communities. |
| **13** | Climate Action | Optimised routing and reduced empty runs can lower CO2 emissions from transport, though this is an indirect, enabling effect. |

### Not Directly Relevant (but worth acknowledging)

| SDG | Reason for exclusion |
|:---:|---------------------|
| 4 (Quality Education) | The thesis itself contributes to education, but the system does not |
| 5 (Gender Equality) | Not directly addressed by the system |
| 10 (Reduced Inequality) | No direct effect |

---

## SusAF Analysis for Ressursplanlegger

Use this table format in the thesis (Chapter 5, sustainability section):

### Sustainability Effects Table

| ID | Effect | Dimension | Level | Affects | +/- |
|----|--------|-----------|-------|---------|:---:|
| EC-I1 | Reduced time spent on manual assignment planning | Economic | Immediate | EC-E1 | + |
| EC-E1 | Increased operational efficiency and vehicle utilisation | Economic | Enabling | EC-S1 | + |
| EC-S1 | Transport companies can serve more assignments with same fleet size | Economic | Structural | ENV-E1 | + |
| SO-I1 | Reduced cognitive load on traffic coordinators | Social | Immediate | IN-E1 | + |
| SO-E1 | Democratisation of planning knowledge — system captures some tacit knowledge | Social | Enabling | SO-S1 | + |
| SO-S1 | Reduced dependency on individual coordinators — organisational resilience | Social | Structural | — | +/- |
| IN-I1 | Coordinator retains full control via human-in-the-loop design | Individual | Immediate | SO-I1 | + |
| IN-E1 | Improved work satisfaction from reduced repetitive tasks | Individual | Enabling | — | + |
| IN-E2 | Risk of deskilling — coordinators may lose planning expertise over time | Individual | Enabling | SO-S1 | - |
| ENV-E1 | More efficient vehicle assignment reduces fuel consumption and emissions | Environmental | Enabling | ENV-S1 | + |
| ENV-S1 | Wide-scale adoption could measurably reduce transport sector emissions | Environmental | Structural | — | + |
| ENV-I1 | Energy consumption of cloud-hosted SaaS platform | Environmental | Immediate | — | - |
| TE-I1 | Modern tech stack ensures maintainability and adaptability | Technical | Immediate | TE-E1 | + |
| TE-E1 | Multi-engine architecture allows future solver improvements without rewrite | Technical | Enabling | — | + |
| TE-E2 | Dependency on external services (Better Auth, cloud hosting) | Technical | Enabling | — | - |

### Likelihood x Impact Prioritisation

After identifying effects, SusAF recommends classifying them on two axes to determine which to discuss in depth:

| | Low impact | High impact |
|---|---|---|
| **Very likely** | Acknowledge briefly | Discuss in detail |
| **Unlikely** | Omit or footnote | Mention as speculative risk/opportunity |

For the thesis, focus the discussion on the **high-impact, likely effects** (top-right quadrant). Acknowledge low-impact effects briefly. Speculative structural effects (high-impact but uncertain) should be discussed with hedging language.

### SusAD Diagram

The Sustainability Awareness Diagram (SusAD) is a pentagon radar chart with five slices (one per dimension) and three concentric rings (immediate → enabling → structural). Effects are plotted on the diagram to visualise their distribution across dimensions and depth. Consider including a SusAD figure in the thesis — it provides a visual summary of the analysis. Use the pentagon image from the SusAF Taster workbook as a template.

### Key Dilemmas to Discuss

These are the tensions that demonstrate critical thinking:

1. **Efficiency vs. deskilling (IN-E2):** The system makes planning easier, but may cause coordinators to lose the tacit knowledge that currently makes them effective. If the system fails, they may be less able to plan manually than before.

2. **Automation vs. autonomy (IN-I1 vs. SO-S1):** Human-in-the-loop preserves coordinator agency now, but structural effects of wide adoption could gradually shift decision authority to algorithms — even if individual overrides remain available.

3. **Resource efficiency vs. energy consumption (ENV-E1 vs. ENV-I1):** Optimised planning reduces fuel use in transport, but the platform itself consumes energy (servers, computation for solvers). The net environmental effect depends on scale of adoption.

4. **Knowledge capture vs. knowledge loss (SO-E1 vs. IN-E2):** Formalising tacit knowledge in the system preserves it organisationally but may atrophy it individually.

---

## Ethical Perspective (required by grading criterion 2)

The grading rubric (UHR-NRT) explicitly asks whether the work shows an ethical perspective. The sustainability section should address:

1. **Algorithmic fairness:** The algorithm assigns workload to drivers. If soft constraint weights are misconfigured, some drivers could systematically receive less desirable assignments. The coordinator's override capability mitigates this, but the default algorithm output shapes the starting point.

2. **Accountability for errors:** If the algorithm generates a plan with a hidden conflict (e.g., expired certification not flagged), who is responsible — the coordinator who approved it or the system that missed it? The human-in-the-loop design places final responsibility with the coordinator, but the system's conflict detection creates an expectation of completeness.

3. **Privacy and data handling:** The system stores personal data about drivers — availability, competencies, time-off reasons. Multi-tenant architecture with company-scoped isolation protects between companies, but within a company, coordinators see all driver data. This is appropriate for the planning function but must be acknowledged.

4. **Health and working conditions:** The system's conflict detection for overtime and rest-time violations directly supports driver health. However, if optimisation prioritises efficiency (more assignments per driver), it could inadvertently push drivers toward their legal maximums. The configurable constraint weights put this decision in the coordinator's hands.

These points should be woven into the sustainability discussion — not as a separate ethics section, but as part of the SusAF dilemmas.

---

## How to Write the Sustainability Section

### Structure (recommended for Chapter 5.4 or a dedicated section)

1. **Introduction** (2–3 sentences): State that sustainability is assessed using SusAF across five dimensions and three effect levels. Cite the framework.
2. **Analysis table**: Present the effects table above (adapted to final system state).
3. **Discussion of key dilemmas**: Pick 2–3 dilemmas and discuss them critically. This is where sensor looks for depth.
4. **Connection to SDGs**: Map the effects to specific SDGs (use the sub-targets, not just the 17 top-level goals). Explain *why* each SDG is relevant — don't just list them.
5. **Limitations of the analysis**: Acknowledge that effects are projected, not measured. The system has not been deployed at scale, so structural effects are speculative.

### Connecting SusAF to SDGs — the Bryllupskakemodellen (Wedding Cake Model)

The Wedding Cake Model (Stockholm Resilience Centre) shows how the 17 SDGs relate to the three classic sustainability pillars: the biosphere (environmental) forms the foundation, society sits on top, and economy on top of society. This model can be used as a visual bridge between the SusAF dimensions and the SDGs — but for a specific system analysis, the direct mapping from individual effects to specific SDG sub-targets is more precise and useful.

### What to cite

- SusAF framework: Duboc, L., et al. (2020). Do we really know what we are building? Raising awareness of potential sustainability effects of software systems in requirements engineering. *Journal of Systems and Software*, 165, 110570.
- SusAF resources and taster tool: Penzenstadler, B., et al. (2020). SusAF online resources. Available at: https://sustainabilitydesign.org
- Karlskrona Manifesto: Becker, C., et al. (2015). The Karlskrona Manifesto for Sustainability Design. arXiv:1410.6968. [Cite for the five dimensions definition and the three orders of effects]
- SDGs: United Nations General Assembly. (2015). Transforming our world: the 2030 Agenda for Sustainable Development. A/RES/70/1.
- SusAF-SDG mapping: Seyff, N., et al. (2022). Transforming our World through Software: Mapping the Sustainability Awareness Framework to the UN Sustainable Development Goals. In *Proceedings of ENASE 2022*, 417–425.
- Brundtland definition: Brundtland, G. H. (1987). Report of the World Commission on Environment and Development: Our Common Future. United Nations.
- Orders of effects: Betz, S., et al. (2015). [Original source for first/second/third order effects classification — verify exact reference]

> All of these are in `result/references.bib`. Generate source notes via `.claude/agents/source-extractor.md` before citing.

---

## Writing Rules for This Section

- Do NOT just list SDGs — explain the connection to this specific project
- Do NOT only discuss positive effects — the dilemmas are what show critical thinking
- Do NOT claim effects that the system cannot demonstrate (it is not deployed)
- Use hedging language: "could potentially", "may contribute to", "is expected to"
- Keep the section proportional — 1.5–2 pages is appropriate for a bachelor thesis
- Use the SusAF table as a figure with a caption and label
