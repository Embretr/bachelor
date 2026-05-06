# Sustainability Design and Software: The Karlskrona Manifesto (`becker2015karlskrona`)

## Status
- [x] Notes generated from raw (Claude, 2026-05-01)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Full paper read (10 PDF pages). All areas of interest investigated. Key manifesto principles, five sustainability dimensions, multi-order effects framework, and ethical framing captured. The paper is short (conference paper), so complete coverage is achievable.
  - **Gaps not investigated:** §III (manifesto genre study) — read and confirmed it contains no content relevant to thesis areas; omitted from extraction.

## Source metadata
- **BibTeX key:** `becker2015karlskrona`
- **Reference (APA 7):** Becker, C., Chitchyan, R., Duboc, L., Easterbrook, S., Penzenstadler, B., Seyff, N., & Venters, C. C. (2015). Sustainability design and software: The Karlskrona manifesto. *Proceedings of the 37th International Conference on Software Engineering (ICSE 2015)*, *2*, 467–476. https://doi.org/10.1109/ICSE.2015.179
- **Tilgang:** IEEE Xplore (NTNU access confirmed — downloaded 2026-05-01 from IEEE Xplore)
- **Raw source:** `../becker2015karlskrona` (PDF without extension; 10 pages)
- **Coverage in raw:** Full paper, pp. 467–476. PDF page 1 = printed page 467 (offset: PDF page + 466 = printed page).

## Sammendrag (2–3 setninger)

The Karlskrona Manifesto is a cross-disciplinary initiative in software engineering that articulates foundational principles for sustainability-aware system design. It defines five sustainability dimensions (environmental, social, economic, technical, individual), a three-order effects framework for analysing software's direct and systemic impacts, and nine normative principles — most notably that sustainability is systemic, multi-dimensional, and precondition-level rather than a competing quality attribute. Its contribution to this thesis is providing the analytical structure and vocabulary for the §5.3 sustainability analysis of Ressursplanlegger.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 5.3 (Sustainability and Ethical Considerations) | **Covered** — five dimensions, multi-order effects, stakeholder responsibility, code-of-ethics critique directly applicable |
| Ch 5.3 ¶1 (SusAF structuring framework) | **Partial** — Karlskrona defines the five dimensions that SusAF operationalises; SusAF itself is Duboc et al. 2020 (duboc2020requirements), not this paper |
| Ch 5.3 ¶4 (SDG framework) | **Outside scope** — SDGs not mentioned; source predates systematic SDG integration in software sustainability literature |
| Ch 2 / other chapters | **Outside scope** — Karlskrona is a software sustainability manifesto; no scheduling theory, HITL, TMS, or DSR content |

## Claims this source supports

### Claim 1: "Sustainability has five dimensions: environmental, social, economic, technical, and individual"
- **Suggested for:** Ch 5.3 ¶1 (structuring framework introduction — provides the five-dimension vocabulary the thesis uses to organise its sustainability analysis)
- **Direkte sitat:** "Following Goodland [34] and Penzenstadler & Femmer [35], we identify five sustainability dimensions: Environmental: concerned with the long term effects of human activities on natural systems. [...] Social: concerned with societal communities (groups of people, organizations) and the factors that erode trust in society. [...] Economic: focused on assets, capital and added value. [...] Technical: refers to longevity of information, systems, and infrastructure and their adequate evolution with changing surrounding conditions. [...] Individual: refers to the well-being of humans as individuals. This includes mental and physical well-being, education, self-respect, skills, mobility, etc." (p. 470 / PDF 4)
- **Parafrase:** The five dimensions provide a disaggregated analytical structure for assessing sustainability effects; they are interdependent but usefully separated for analysis.
- **Forbehold:** These dimensions are presented as a pragmatic analytical tool, explicitly acknowledging ongoing disputes between "weak" and "strong" sustainability views (see §II). The framework is a starting point for analysis, not a settled taxonomy.
- **Anvendelse på vårt case:** Ressursplanlegger's §5.3 sustainability analysis maps across all five dimensions: Environmental (reduced deadhead driving, route density effects), Social (driver workload equity, employment conditions), Economic (overtime cost reduction, company ROI on system), Technical (system longevity, API maintainability), Individual (driver autonomy, coordinator cognitive load).

---

### Claim 2: "Software systems produce three orders of effects that must be distinguished"
- **Suggested for:** Ch 5.3 ¶2 (benefits and harms table — provides the analytical lens for mapping Ressursplanlegger's sustainability effects at different timescales)
- **Direkte sitat:** "First order effects are impacts and opportunities created by the immediate existence of a software system, arising from its design features and flaws. Second order effects are those created by the ongoing use and application of the software, such as how it changes what we do and what we're capable of. Third order effects are the changes that occur through the aggregated behaviours of very large numbers of people using the technology over the medium to long term (e.g., energy demand, mass surveillance, etc). These effects play out across many domains." (p. 470 / PDF 4)
- **Parafrase:** First-order = direct effects of system existence; second-order = effects of ongoing use; third-order = systemic/societal effects at scale.
- **Forbehold:** Third-order effects require aggregated adoption at scale; for a single artefact evaluated in a thesis without production deployment, third-order analysis is speculative and must be framed as such.
- **Anvendelse på vårt case:** First order: Ressursplanlegger reduces coordinator's manual planning burden directly. Second order: coordinator workflow changes when algorithm suggestions become the default starting point — coordinator role shifts from plan-creator to plan-approver. Third order (speculative): if such platforms become widespread in Norwegian transport, driver labor conditions may change as scheduling becomes optimisation-constrained rather than coordinator-discretion-driven — a working-conditions dilemma to flag in §5.3 ¶3.

---

### Claim 3: "System visibility is a necessary precondition and enabler for sustainability design"
- **Suggested for:** Ch 5.3 ¶5 (ethical considerations as substantive design issues — and optionally Ch 5.1.1 ¶1 as supporting the Effektivitet anchor's visibility-as-precondition framing)
- **Direkte sitat:** "System visibility is a necessary precondition and enabler for sustainability design. Strive to make the status of the system and its context visible at different levels of abstraction and perspectives to enable participation and informed responsible choice." (p. 473 / PDF 7)
- **Parafrase:** Sustainability-aware design requires that all stakeholders can see the system's status and act on it; visibility is not optional.
- **Forbehold:** In the Karlskrona context, "system" refers to the socio-technical system at large (including ecological and social contexts), not just the software artefact. For Ressursplanlegger, "system" must be interpreted as the driver/vehicle resource system made visible, not the software itself.
- **Anvendelse på vårt case:** The Karlskrona visibility principle directly aligns with Ressursplanlegger's foundational claim under Effektivitet: making invisible utilisation patterns (overtime, idle time, load imbalance) legible to coordinators and owners is the precondition for sustainable resource planning. This gives the thesis a sustainability-design warrant for prioritising visibility over optimisation in the artefact's design.

---

### Claim 4: "Sustainability is a precondition for system existence, not a quality to be balanced against other attributes"
- **Suggested for:** Ch 5.3 ¶1 (framing sustainability not as an afterthought but as foundational), Ch 5.3 ¶5 (ethical considerations as substantive design issues)
- **Direkte sitat:** "sustainability is not in competition with a specific set of quality attributes against which it has to be balanced - it is a fundamental precondition for the continued existence of the system and influences many of the goals to be considered in systems design." (p. 473 / PDF 7)
- **Parafrase:** Treating sustainability as one of several quality attributes to be traded off is a category error; it is instead a design precondition.
- **Forbehold:** This is a normative principle from the manifesto, not an empirical finding. The thesis uses it as a design stance, not as an established fact.
- **Anvendelse på vårt case:** The claim supports framing §5.3 as an analysis of Ressursplanlegger's sustainability implications treated as design-level concerns — not as a compliance checklist appended after functional design decisions were already made.

---

### Claim 5: "Each stakeholder has a right to know the system's design and status, and to influence the outcome"
- **Suggested for:** Ch 5.3 ¶5 (ethical considerations — operator-vs-owner asymmetry as an ethics question)
- **Direkte sitat:** "There is a narrow conception of the roles of system designers, developers, users, owners, and regulators and their responsibilities [...] sustainability imposes a distinct responsibility on each one of us, and that responsibility comes with a right to know the system design and its status, so that each participant is able to influence the outcome of the technology application in both design and use." (p. 473 / PDF 7)
- **Parafrase:** Stakeholders — including users (coordinators) and owners — have a sustainability-grounded right to inspect and influence the system's design and operation.
- **Forbehold:** The source uses "users" and "owners" generically; the specific operator-vs-owner asymmetry that the thesis identifies (owners and Admmit demand optimisation; coordinators operate the system) is an elaboration beyond what the Karlskrona Manifesto explicitly states.
- **Anvendelse på vårt case:** The stakeholder visibility principle gives a sustainability-design warrant for Ressursplanlegger's Tillit/kontroll design requirement — the coordinator's right to inspect, modify, accept, or reject every algorithm-generated assignment is not only a usability preference but a sustainability-design obligation. The operator-vs-owner asymmetry in §5.3 ¶5 is thus an ethics question about whose sustainability goals the system serves.

---

### Claim 6: "Codes of ethics for software professionals fail to address second- and third-order effects"
- **Suggested for:** Ch 5.3 ¶3 (ethical dilemmas — accountability for algorithm-generated decisions)
- **Direkte sitat:** "it is our responsibility to address the potential harm from the 2nd and 3rd-order effects of the systems we design as part of our design process, even if these are not readily quantifiable." (p. 473 / PDF 7)
- **Parafrase:** Standard professional ethics frameworks are insufficient because they focus only on immediate, quantifiable harm; software designers bear responsibility for systemic and long-term effects.
- **Forbehold:** This is an advocacy claim by the manifesto's authors, not an empirical finding. Its normative force in the thesis is as a design responsibility framing.
- **Anvendelse på vårt case:** Supports §5.3 ¶3's accountability dilemma: when an algorithm-generated assignment goes wrong (wrong driver sent, overtime violation undetected), responsibility falls on the coordinator who accepted the plan — yet the designer bears responsibility for second-order effects of that architecture. The thesis acknowledges this without resolving it empirically.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| software system | Ressursplanlegger | Source uses "software system" generically for any SE artefact |
| system visibility | synlighet av ressursutnyttelse | In Ressursplanlegger: making overtime, idle time, and load imbalance visible to coordinator and owner |
| users | trafikkoordinator | The source conflates users and operators; for us, user = the coordinator who operates the planning surface |
| owners | transportselskapet / Admmit | Source uses "owners" for those who commission software; maps to both company owners and Admmit as platform owner |
| designers / developers | Mikael + Embret (bachelor team) | Explicit in the source's stakeholder model |
| individual dimension | sjåfør / trafikkoordinator | Individual sustainability in our case = driver well-being (workload, autonomy) AND coordinator cognitive load |
| social dimension | sjåfør-rettferdighet, norsk transportsektor | Driver equity and fairness in assignment across a company |
| first/second/third order effects | direkte / bruksbaserte / systemiske effekter | Mapping for §5.3 effects table |
| wicked problem | "dilemma å respondere på" | The source characterises sustainability as a wicked problem, not a solvable one — relevant for §5.3 ¶3 dilemmas framing |

## Forbehold og begrensninger

- **Karlskrona ≠ SusAF:** The outline's `MUST CITE: SusAF / sustainability awareness framework` likely requires *both* this source (foundational dimensions) and Duboc et al. 2020 (`duboc2020requirements`, also in bib) which operationalises SusAF as a RE tool. Becker et al. 2015 defines the five dimensions; Duboc et al. 2020 builds the structured framework tool on top of them. Do NOT cite only becker2015karlskrona when the outline refers to "SusAF" — confirm with duboc2020requirements.
- **SDGs not covered:** The outline's §5.3 ¶4 ("Map effects to the SDG framework") requires a separate SDG source. The Karlskrona Manifesto (2015) predates systematic SDG integration in software sustainability literature and does not reference the SDG framework. Use `\parencite{un2015agenda2030}` — this bib key is already in `result/references.bib`.
- **No empirical data:** The Karlskrona Manifesto is a normative-advocacy document, not an empirical study. It provides design principles and vocabulary, not evidence about what effects software actually has in transport.
- **No transport-sector specificity:** All examples are from generic SE or a suburban car-sharing scenario. Application to Norwegian transport resource planning requires explicit bridging (provided in Application notes).
- **"Sustainability" in the thesis vs. the manifesto:** The thesis's Effektivitet anchor (resource utilisation optimisation) is an economic/technical sustainability concern; the manifesto's primary emphasis is environmental and social sustainability. The overlap is real but partial — avoid citing Karlskrona in support of claims primarily about economic efficiency.
- **Version 0.5:** The manifesto reproduced in the paper is Version 0.5 (January 2015). It is described as a living document. The thesis cites the ICSE 2015 paper, which contains v0.5; later versions exist at sustainabilitydesign.org.
- **Outline MUST CITE marker check:** §5.3 ¶1 says "MUST CITE: SusAF / sustainability awareness framework" — becker2015karlskrona partially satisfies this (foundational dimensions) but does not satisfy the SusAF-specific marker alone.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Sustainability | "the capacity to endure" (adopted from Oxford Dictionary of English) | p. 469 / PDF 3 |
| Environmental sustainability | "concerned with the long term effects of human activities on natural systems" | p. 470 / PDF 4 |
| Social sustainability | "concerned with societal communities (groups of people, organizations) and the factors that erode trust in society" | p. 470 / PDF 4 |
| Economic sustainability | "focused on assets, capital and added value" | p. 470 / PDF 4 |
| Technical sustainability | "refers to longevity of information, systems, and infrastructure and their adequate evolution with changing surrounding conditions" | p. 470 / PDF 4 |
| Individual sustainability | "refers to the well-being of humans as individuals. This includes mental and physical well-being, education, self-respect, skills, mobility, etc." | p. 470 / PDF 4 |

## Rammeverk og modeller

### Five Sustainability Dimensions (p. 470 / PDF 4)

| Dimensjon | Hva det er | Side |
|---|---|---|
| Environmental | Long-term effects on natural systems: ecosystems, raw resources, climate, pollution, waste | p. 470 |
| Social | Societal communities and factors eroding trust: equity, justice, employment, democracy | p. 470 |
| Economic | Assets, capital, added value: wealth creation, profitability, investment | p. 470 |
| Technical | Longevity of systems and infrastructure: maintenance, innovation, obsolescence, data integrity | p. 470 |
| Individual | Well-being of humans: physical/mental health, education, self-respect, mobility | p. 470 |

Note: Dimensions are interdependent — "cumulative effects from the individual dimension will bleed into the social one" (p. 470 / PDF 4).

### Three Orders of Effects Framework (p. 470 / PDF 4)

| Order | Hva det er | Eksempel fra kilden |
|---|---|---|
| First order (direct) | Impacts from the physical existence of the software system | Software's design features and flaws affecting users immediately |
| Second order (indirect) | Effects from ongoing use of the software | Changes in what people do and what they're capable of |
| Third order (systemic) | Effects from aggregated use by large numbers over long term | Energy demand, mass surveillance patterns |

### Karlskrona Manifesto Principles — Nine Core Principles (pp. 472–473 / PDF 7)

| Prinsipp | Formulering (verbatim) |
|---|---|
| Systemic | "Sustainability is systemic. Sustainability is never an isolated property." |
| Multi-dimensional | "Sustainability has multiple dimensions." |
| Trans-disciplinary | "Sustainability transcends multiple disciplines." |
| Independent of system purpose | "Sustainability is a concern independent of the purpose of the system." |
| System and wider contexts | "Sustainability applies to both a system and its wider contexts." |
| System visibility | "System visibility is a necessary precondition and enabler for sustainability design." |
| Multiple levels of action | "Sustainability requires action on multiple levels." |
| Present and future compatible | "It is possible to meet the needs of future generations without sacrificing the prosperity of the current generation." |
| Long-term thinking | "Sustainability requires long-term thinking." |

## Key arguments / lines of reasoning

### Argument: Sustainability as precondition, not quality attribute
- **Premiss(er):** Sustainability is often treated as "one quality among several" to be balanced against performance, cost, etc. But systems that consistently consume more value than they produce cannot be sustained indefinitely.
- **Konklusjon:** "Sustainability is not in competition with a specific set of quality attributes against which it has to be balanced — it is a fundamental precondition for the continued existence of the system."
- **Sted:** (p. 473 / PDF 7)
- **Hvilke claims dette støtter:** Ch 5.3 ¶1, ¶5

### Argument: Software designers bear responsibility for second- and third-order effects
- **Premiss(er):** Standard SE codes of ethics address only immediate harm to individuals and property. But software produces second- and third-order effects that are not readily quantifiable but are nonetheless real.
- **Konklusjon:** "It is our responsibility to address the potential harm from the 2nd and 3rd-order effects of the systems we design as part of our design process, even if these are not readily quantifiable."
- **Sted:** (p. 473 / PDF 7)
- **Hvilke claims dette støtter:** Ch 5.3 ¶3 (accountability dilemma)

### Argument: System visibility enables stakeholder agency
- **Premiss(er):** Each stakeholder — designer, user, owner, regulator — has a distinct sustainability responsibility that requires knowledge of the system's status and structure.
- **Konklusjon:** "Sustainability imposes a distinct responsibility on each one of us, and that responsibility comes with a right to know the system design and its status, so that each participant is able to influence the outcome."
- **Sted:** (p. 473 / PDF 7)
- **Hvilke claims dette støtter:** Ch 5.3 ¶5 (operator-vs-owner asymmetry as ethics question); connects to Tillit/kontroll

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Kodi's car-sharing app (CodeIT) | How sustainability dimensions and multi-order effects apply in practice to transport software — cross-domain proximity to our thesis case | pp. 474–475 / PDF 8–9 |

Note: The car-sharing scenario is the source's primary application example. It involves transportation software, making it a close-domain illustration for the thesis. The example demonstrates how sustainability-is-systemic and multi-order effects apply to a software system that mediates transport decisions — analogous (not identical) to Ressursplanlegger's role in transport resource planning.

## Data og statistikk

Kilden presenterer ingen statistikk. It is a normative-advocacy manifesto paper.

## Forfatter-perspektiv / metodologi

Cross-disciplinary collaborative manifesto, developed through a workshop at RE4SuSy (RE'14, Karlskrona) and refined via synchronous writing sessions over several months. Authors represent software engineering, requirements engineering, human-computer interaction, and sustainability research. The paper explicitly frames itself as advocacy and agenda-setting rather than empirical research. The manifesto is Version 0.5 at time of publication.

## Spot-check verification

1. Quote "First order effects are impacts and opportunities created by the immediate existence of a software system, arising from its design features and flaws. Second order effects are those created by the ongoing use and application of the software, such as how it changes what we do and what we're capable of. Third order effects are the changes that occur through the aggregated behaviours of very large numbers of people using the technology over the medium to long term" (p. 470 / PDF 4) — verified via `pdftotext -f 4 -l 4` — **PASS**

2. Quote "System visibility is a necessary precondition and enabler for sustainability design. Strive to make the status of the system and its context visible at different levels of abstraction and perspectives to enable participation and informed responsible choice." (p. 473 / PDF 7) — verified via `pdftotext -f 7 -l 7` — **PASS**

3. Quote "sustainability is not in competition with a specific set of quality attributes against which it has to be balanced - it is a fundamental precondition for the continued existence of the system and influences many of the goals to be considered in systems design." (p. 473 / PDF 7) — verified via `pdftotext -f 7 -l 7` — **PASS**

**Result:** 3/3 quotes verified, 0 corrections made.