# Requirements Engineering for Sustainability: An Awareness Framework for Designing Software Systems for a Better Tomorrow (`duboc2020requirements`)

## Status
- [x] Notes generated from raw (Claude, 2026-05-01)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** All 24 pages read. All areas of interest investigated. Five dimensions, three orders of effects, framework structure, applicability finding, and limitations fully documented. Spot-check passed 5/5.
  - **Gaps not investigated:** None — article is 24 pages and was read in full.

## Source metadata
- **BibTeX key:** `duboc2020requirements`
- **Reference (APA 7):** Duboc, L., Penzenstadler, B., Porras, J., Akinli Kocak, S., Betz, S., Chitchyan, R., Leifler, O., Seyff, N., & Venters, C. C. (2020). Requirements engineering for sustainability: An awareness framework for designing software systems for a better tomorrow. *Requirements Engineering*, *25*(4), 469–492. https://doi.org/10.1007/s00766-020-00336-y
- **Tilgang:** PDF
- **Raw source:** `../duboc2020requirements.pdf`
- **Coverage in raw:** Full article, pp. 469–492. PDF page 1 = printed page 469; offset = PDF page + 468. Dual-reference format used throughout (p. N / PDF p. M).

---

## Sammendrag (2–3 setninger)

Duboc et al. (2020) present the Sustainability Awareness Framework (SusAF), a question-based framework for raising awareness of the potential sustainability effects that software systems could have across five dimensions (social, individual, environmental, economic, technical) and three orders of effects (immediate, enabling, structural). The framework includes structured question sets per dimension, a note-taking form, and the Sustainability Awareness Diagram (SusAD) — an adapted radar chart for visualising chains of effects. An evaluation study with four student groups confirms that SusAF is applicable to systems across different domains and types, including systems not directly aimed at sustainability goals.

---

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 5.3 ¶1 (SusAF framework introduction) | **Covered** — SusAF defined, five dimensions listed, framework components described |
| Ch 5.3 ¶2 (Sustainability effects table per dimension) | **Covered** — topics per dimension (Table 1) and three orders of effects provide the structure |
| Ch 5.3 ¶3 (Key dilemmas: fairness, accountability, privacy, working conditions) | **Partial** — Social and Individual dimension question sets address equity, privacy, agency; framework does not produce conclusions, only raises questions |
| Ch 5.3 ¶4 (SDG framework map) | **Outside scope** — SusAF uses its own five-dimension structure, not SDG mapping; no SDG content in this paper |
| Ch 5.3 ¶5 (Ethical considerations as substantive design issues) | **Covered** — argument that RE professionals bear responsibility for sustainability effects; operator-vs-owner equity question surfaced in Social dimension |
| Ch 5.3 ¶6 (Limitations of sustainability analysis) | **Covered** — paper explicitly states awareness is the scope, not detailed empirical analysis |

---

## Claims this source supports

### Claim 1: SusAF is a structured framework for raising awareness of a software system's potential sustainability effects across five dimensions

- **Suggested for:** Ch 5.3 ¶1 (primary); Ch 5.3 ¶2 (for the effects table structure)
- **Direkte sitat:** "The main goal of the framework is to raise awareness of the sustainability effects that a software system could have in its intended context." (p. 472 / PDF p. 4)
- **Parafrase:** SusAF is not an evaluation or measurement tool but an awareness framework — a first step that helps requirements engineers and stakeholders surface potential effects through structured questions, interviews, and a visualisation diagram.
- **Forbehold:** The paper is explicit that "the detailed analysis of potential effects is currently outside the scope of the framework" (footnote, p. 472 / PDF p. 4). This means §5.3 can legitimately conduct a SusAF-inspired awareness exercise, but cannot claim to have empirically measured or proven sustainability effects.
- **Anvendelse på vårt case:** SusAF strukturerer §5.3 ved å tilby fem dimensjoner som analytisk rammeverk for å identifisere Ressursplanleggers potensielle bærekraftseffekter — systemet er ikke designet for bærekraft, men SusAF er bekreftet egnet for slike systemer (se Claim 5 under).

---

### Claim 2: Five sustainability dimensions — Social, Individual, Environmental, Economic, Technical

- **Suggested for:** Ch 5.3 ¶1 (introduce framework) and ¶2 (effects table structure)
- **Direkte sitat:** "sustainability requires simultaneous consideration of several interrelated dimensions (environmental, economic, individual, social and technical), which we refer to as the **five dimensions of sustainability**" (p. 470 / PDF p. 2)
- **Topics per dimension (Table 1, p. 473 / PDF p. 5):**
  - **Social:** (1) Sense of community; (2) Trust; (3) Inclusiveness and diversity; (4) Equity; (5) Participation and communication
  - **Individual:** (1) Health; (2) Lifelong learning; (3) Privacy; (4) Safety; (5) Agency
  - **Environmental:** (1) Material and resources; (2) Soil, atmospheric and water pollution; (3) Energy; (4) Biodiversity and land use; (5) Logistics and transportation
  - **Economic:** (1) Value; (2) Customer relationship management (CRM); (3) Supply chain; (4) Governance and processes; (5) Innovation and R&D
  - **Technical:** (1) Maintainability; (2) Usability; (3) Extensibility and adaptability; (4) Security; (5) Scalability
- **Forbehold:** The dimension structure was developed by experts in the Karlskrona Alliance on Sustainability Design — their expertise spans sustainability broadly, not any single domain. Some topics (e.g., supply chain, biodiversity) have limited relevance to Ressursplanlegger's case.
- **Anvendelse på vårt case:** Fem dimensjoner gir analysestrukturen for §5.3s effekttabell. Mest relevante for Ressursplanlegger: Social (equity mellom sjåfører via algoritmetildeling; trust mellom koordinator og system), Individual (privacy for ansattdata; agency for sjåfører), Environmental (logistics and transportation — direkte domenerelevans), Economic (value for selskapet; supply chain for planlegging). Technical-dimensjonen overlapper delvis med systemets non-functional requirements (allerede dekket i §4.2).

---

### Claim 3: Three orders of effects — immediate, enabling, structural

- **Suggested for:** Ch 5.3 ¶2 (effects table); Ch 5.3 ¶5 (ethical considerations framing)
- **Direkte sitat:** "From the centre outwards these effects are: (1) immediate, i.e. a direct function of the system or direct effect of its development, (2) enabling, i.e. arising from the use of a system, or (3) structural, i.e. referring to persistent changes that can be observed at the macro-level" (p. 474 / PDF p. 6)
- **Parafrase:** Effects are not only direct (what the system does) but extend over time — enabling effects arise from prolonged use, and structural effects manifest as macro-level societal or economic changes.
- **Forbehold:** Identifying enabling and structural effects requires speculation about long-term use that the thesis cannot empirically verify. §5.3 should present these as potential effects (the awareness purpose of SusAF), not confirmed outcomes.
- **Anvendelse på vårt case:** For Ressursplanlegger: *Immediate* — redusert overtid og lediggang ved algoritmegenererte planer; *Enabling* — koordinatoren endrer planleggingspraksis etter langvarig bruk (avhengighet av algoritmeforslag); *Structural* — normalisering av datamaskinassistert tildelingslogikk i norsk transportsektor kan på sikt forrykke koordinatorrollen og lønnsforhandlingsgrunnlaget for sjåfører.

---

### Claim 4: Software systems exist within and shape wider socio-technical systems

- **Suggested for:** Ch 5.3 ¶5 (ethical considerations as substantive design issues)
- **Direkte sitat:** "software developed today does not exist in isolation but forms part of the wider socio-technical system within which it gets used" (p. 490 / PDF p. 22)
- **Parafrase:** A software system's consequences extend beyond its direct functions — it shapes the socio-technical context it is embedded in, and this must be considered during design and requirements engineering.
- **Forbehold:** The paper argues this broadly for software systems; the specific mechanisms differ case by case. For Ressursplanlegger, the "wider socio-technical system" must be concretely described (Norwegian transport companies, coordinator-driver relationships, labor agreements) to avoid vague hand-waving.
- **Anvendelse på vårt case:** Begrunner §5.3s eksistens som en substantiell seksjonen: Ressursplanlegger er ikke et nøytralt planleggingsverktøy — den former maktforholdet mellom koordinator og sjåfør (hvem som beslutter tildelinger), mellom eier og koordinator (hvem som har innsyn i utnyttelsesdata), og på sikt kanskje normen for hva koordinatorrollen innebærer.

---

### Claim 5: RE professionals bear responsibility for sustainability effects across all dimensions

- **Suggested for:** Ch 5.3 ¶5 (ethical framing); thesis argument for why §5.3 exists
- **Direkte sitat:** "requirements engineers have a degree of responsibility to support the discussion of the potential sustainability effects of the software across all dimensions of sustainability in order to account for potential (un-)desired consequences during the software's life cycle" (p. 470 / PDF p. 2)
- **Parafrase:** Requirements engineering is not value-neutral; designers of software systems are accountable for surfacing and discussing sustainability consequences before and during development.
- **Forbehold:** The source frames this as a professional norm and research programme, not a binding standard. The "responsibility" is normative, not regulatory — appropriate to invoke in academic discussion but not as a compliance claim.
- **Anvendelse på vårt case:** Begrunner at Ressursplanlegger-teamet (som requirements engineers og systemutviklere) har et ansvar for å analysere systemets bærekraftseffekter, noe som er gjort i §5.3. Koblingen til Tillit/kontroll-ankeret er også relevant: hvem er ansvarlig for en algoritme-generert tildeling som viser seg å være urettferdig overfor en sjåfør?

---

### Claim 6: SusAF is applicable to systems not directly focused on sustainability goals

- **Suggested for:** Ch 5.3 ¶1 (justification for applying SusAF to Ressursplanlegger)
- **Direkte sitat:** "The analysis of the SusADs suggests that students successfully managed to apply the framework to systems of different domains and types... We therefore conclude that the evidence **supports RQ1**." (p. 481 / PDF p. 13)
- **Parafrase:** RQ1 in the paper was "Is the framework applicable to systems that are not directly focused on sustainability?" — the study confirms it is. Among systems evaluated: Uber, Netflix, and transportation systems (Electric Scooters, Hyperloop).
- **Forbehold:** The evaluation used students, not industry practitioners. The authors note: "we are hopeful that the framework will serve equally well for professionals" (p. 490 / PDF p. 22) — but this is stated as hope, not confirmed evidence.
- **Anvendelse på vårt case:** Ressursplanlegger er et planleggingsverktøy, ikke et bærekraftsverktøy. Claim 6 gjør det metodologisk legitimt å anvende SusAF som analyseverktøy i §5.3 uten at systemets primærformål er bærekraft.

---

### Claim 7: Social dimension equity question — algorithmic decision systems and differential treatment

- **Suggested for:** Ch 5.3 ¶3 (fairness dilemma)
- **Direkte sitat:** "Can the system make people to be **treated differently** from each other? For example, because the system carries out data analytics or influences human decisions." (Table 2, p. 473 / PDF p. 5 — Social/Equity topic)
- **Parafrase:** SusAF explicitly identifies equity — differential treatment of people by algorithmic/data-analytical systems — as a Social sustainability concern.
- **Forbehold:** This is a question prompt in the framework, not a finding or claim about any specific system. It surfaces the issue for discussion; the thesis must provide the substantive argument.
- **Anvendelse på vårt case:** Direkte relevant for §5.3 ¶3's fairness dilemma: Ressursplanlegger's algorithm generates assignments that may systematically favour or disfavour certain drivers (e.g., based on availability data, overtime status, route familiarity scores). The equity question connects to the Tillit/kontroll anchor — the coordinator's inspect/modify/accept/reject authority is also the mechanism for correcting algorithmic inequity.

---

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| software system | Ressursplanlegger | Direct mapping |
| user | trafikkoordinator (primary); sjåfør (secondary/affected) | The paper's "user" is whoever interacts with the system — for Ressursplanlegger, the coordinator is the user; drivers are affected parties |
| business that owns the system | transportselskap / Admmit | "Business" in SusAF covers both the operator (transportselskap) and the system vendor (Admmit) |
| requirements engineer | Embret og Mikael (designteam) | The paper positions RE professionals as responsible for sustainability discussions |
| socio-technical system | det norske transportsystemet (koordinatorer, sjåfører, selskaper, planleggingspraksis) | SusAF's "wider socio-technical system" maps to the Norwegian transport-sector context |
| immediate effect | direkte virkninger av systemfunksjonen | E.g., reduced overtime in a specific week's schedule |
| enabling effect | muliggjørende virkninger fra langvarig bruk | E.g., coordinator relies on algorithm for routine assignments, freeing cognitive capacity |
| structural effect | strukturelle makronivåvirkninger | E.g., normalisering av algoritmeassistert tildeling i sektoren |
| five dimensions (Social, Individual, Environmental, Economic, Technical) | fem bærekraftsdimensjoner | Used verbatim as analytical categories in §5.3 |
| chain of effects | effektkjede | Sequential causal chain across dimensions/orders |
| SusAD (radar chart) | bærekraftsdiagram | Optional visualisation tool for §5.3 |

---

## Forbehold og begrensninger

- **SusAF is an awareness framework, not an evaluation or measurement framework.** The paper explicitly footnotes: "As an awareness framework, the detailed analysis of potential effects is currently outside the scope of the framework" (p. 472 / PDF p. 4). Any §5.3 sustainability analysis using SusAF is an analytical awareness exercise, not an empirical finding.
- **No SDG mapping.** SusAF uses its own five-dimension structure; the paper does not map to the SDG framework. Outline §5.3 ¶4 requires "Map effects to the SDG framework" — a different source is needed for SDG coverage. SusAF can provide the effects; a separate SDG source maps them.
- **Student-based evaluation only.** The framework was tested with students, not professional RE teams or industry practitioners. Applicability to professional practice is stated as aspirational ("we are hopeful" — p. 490), not demonstrated.
- **Question sets may not fully cover all Ressursplanlegger-specific concerns.** 10% of students in the study felt some questions were not relevant to the system at hand (p. 486 / PDF p. 18). The logistics/transportation topic in the Environmental dimension is the closest match, but it is generic (movement of people or goods, distance), not specific to driver-assignment planning.
- **Technical dimension overlaps with NFRs.** The Technical dimension (Maintainability, Usability, Extensibility, Security, Scalability) largely overlaps with §4.2's non-functional requirements. To avoid duplication, §5.3 should focus on Social, Individual, Environmental, and Economic dimensions when presenting the effects table.
- **MUST CITE marker confirmed:** outline §5.3 ¶1 has `MUST CITE: SusAF / sustainability awareness framework` — this is the source. Confirmed fit.

---

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| sustainability | "the capacity of a socio-technical system to endure" | p. 470 / PDF p. 2 |
| sustainable use | "use S in a way that does not compromise its ability to fulfil F for a period of T" | p. 470 / PDF p. 2 |
| sustainable development | "meets the needs of the present without compromising the ability of future generations to meet their own needs" (Brundtland Commission, cited by authors) | p. 470 / PDF p. 2 |
| immediate effect | "a direct function of the system or direct effect of its development" | p. 474 / PDF p. 6 |
| enabling effect | "arising from the use of a system" | p. 474 / PDF p. 6 |
| structural effect | "referring to persistent changes that can be observed at the macro-level" | p. 474 / PDF p. 6 |

---

## Rammeverk og modeller

### SusAF — Sustainability Awareness Framework (pp. 472–475 / PDF pp. 4–7)

The framework consists of three components:

| Komponent | Hva det er | Side |
|---|---|---|
| Question sets | Five sets of questions (5 topics × 5 questions per dimension) used to guide semi-structured stakeholder interviews or workshops | p. 472–473 / PDF p. 4–5 |
| Instructions and forms | Note-taking form for capturing effects and chains of effects during/after interviews; instructions for drawing the SusAD | p. 474 / PDF p. 6 |
| Sustainability Awareness Diagram (SusAD) | Pentagon radar chart with five sections (one per dimension) and three concentric rings (immediate, enabling, structural effects); visualises chains of effects | p. 474 / PDF p. 6 |

### Five dimensions × five topics matrix (Table 1, p. 473 / PDF p. 5)

| Dimension | Topics (1–5) |
|---|---|
| Social | Sense of community; Trust; Inclusiveness and diversity; Equity; Participation and communication |
| Individual | Health; Lifelong learning; Privacy; Safety; Agency |
| Environmental | Material and resources; Soil, atmospheric and water pollution; Energy; Biodiversity and land use; **Logistics and transportation** |
| Economic | Value; CRM; Supply chain; Governance and processes; Innovation and R&D |
| Technical | Maintainability; Usability; Extensibility and adaptability; Security; Scalability |

**Note:** "Logistics and transportation" as an Environmental topic is directly domain-relevant to Ressursplanlegger.

### Three orders of effects (SusAD structure, p. 474 / PDF p. 6)

| Order | Definition | Example (Airbnb, from paper) |
|---|---|---|
| Immediate | Direct function of system / direct effect of development | "rent rooms" (individual enabling) |
| Enabling | Arising from the use of a system | "greater earnings" (individual enabling) |
| Structural | Persistent changes at macro-level | "gentrification" (social structural) |

---

## Key arguments / lines of reasoning

### Argument: Requirements engineering must become sustainability-aware

- **Premiss 1:** Software systems shape socio-technical systems; their effects extend beyond functional requirements.
- **Premiss 2:** RE professionals have a responsibility to surface and discuss sustainability effects during the software life cycle.
- **Premiss 3:** Current RE methods do not explicitly facilitate sustainability discussions.
- **Konklusjon:** A framework (SusAF) is needed as a practical "first step" to enable RE professionals to raise awareness of sustainability effects — enabling informed design decisions.
- **Sted:** (pp. 469–470 / PDF pp. 1–2)
- **Hvilke claims dette støtter:** Ch 5.3 ¶1, ¶5

### Argument: Systems not aimed at sustainability still have sustainability effects

- **Premiss:** Sustainability effects arise from both intended use and prolonged/widespread use (enabling and structural effects), regardless of design intent.
- **Konklusjon:** SusAF applies to systems across all domains; even non-sustainability-focused systems (Uber, Netflix, Amazon Kindle) have identifiable sustainability effects.
- **Sted:** (p. 481 / PDF p. 13)
- **Hvilke claims dette støtter:** Ch 5.3 ¶1 (justification for applying SusAF to Ressursplanlegger)

---

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Airbnb | How immediate renting → enabling earnings → structural gentrification represents a chain of effects across dimensions (Fig. 1, SusAD) | p. 474–476 / PDF p. 6–8 |
| Amazon Kindle | Students applying SusAF to a non-sustainability system; Fig. 2 shows full SusAD with environmental (CO2), economic (unemployment), individual (privacy) chains | p. 488 / PDF p. 20 |
| E-prescription system | SusAD applied to health-tech; Fig. 3 shows chains across health, privacy, fossil fuel reduction | p. 488 / PDF p. 20 |
| Uber (Transportation IS) | Applied in student study as transportation-domain system; Table 13 classifies as "Arguably related" to sustainability | p. 483 / PDF p. 15 |

---

## Data og statistikk

(Evaluation study data — relevant for establishing framework credibility, not for direct citation in §5.3)

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 27.8% of studied systems were in transportation domain | % of student systems | 2018–2019, two universities | p. 481 / PDF p. 13 |
| 76.9% positive effects in "directly related to sustainability" systems | % of effects | Study | p. 483 / PDF p. 15 |
| 58.7% positive effects even in "unrelated to sustainability" systems | % of effects | Study | p. 483 / PDF p. 15 |
| Framework supported RQ1 (applicability) and RQ2 (insightful discussion) — both "Supported" | O/I/S/SS scale | Spring 2019 cohort | p. 482 / PDF p. 14 |

---

## Forfatter-perspektiv / metodologi

Duboc et al. developed SusAF using Design Science (cited as Hevner et al.) and evaluated it through a quasi-experimental study with four groups of students at two universities (CSULB and LUT) in 2018 and 2019. The paper is both a framework description and an evaluation study; the evaluation is acknowledged as preliminary (student-based, single-context). Authors are associated with the Karlskrona Alliance on Sustainability Design, creating potential biases toward the framework's success (noted in §5.5 threats to validity, p. 480 / PDF p. 12).

---

## Spot-check verification

1. Quote "as the capacity of a socio-technical system to endure" (p. 470 / PDF p. 2) — verified via `pdftotext -f 2 -l 2 duboc2020requirements.pdf - | grep "socio-technical system to endure"` — **PASS**
2. Quote "is to raise awareness of the sustainability effects that a software system could have in its intended context" (p. 472 / PDF p. 4) — verified via `pdftotext -f 4 -l 4 duboc2020requirements.pdf - | grep "raise awareness"` — **PASS**
3. Quote "(Fig. 1) divided into five equal parts, one for each sustainability dimension, and three concentric pentagons" (p. 474 / PDF p. 6) — verified via `pdftotext -f 6 -l 6 duboc2020requirements.pdf - | grep "three concentric"` — **PASS**
4. Quote "meets the needs of the present without compromising the ability of future generations to meet their own needs" (p. 470 / PDF p. 2) — verified via `pdftotext -f 2 -l 2 duboc2020requirements.pdf - | grep "meets the needs"` — **PASS**
5. Quote "does not exist in isolation but forms part of the wider socio-technical system within which it gets used" (p. 490 / PDF p. 22) — verified via `pdftotext -f 22 -l 22 duboc2020requirements.pdf - | grep "does not exist in isolation"` — **PASS**

**Result:** 5/5 quotes verified, 0 corrections made.
m
---

## Koordinasjon med andre kilder

- **§5.3 ¶4 (SDG-mapping):** `duboc2020requirements` dekker IKKE SDG-mapping. For §5.3 ¶4 brukes `un2015agenda2030` (allerede i bib) som SDG-referanse. Writer-agent: siter `\parencite{un2015agenda2030}` for SDG-ramme og `\parencite{duboc2020requirements}` for SusAF-ramme — de er komplementære.
- **§5.3 ¶2 (effekttabell):** Fokuser på Social, Individual, Environmental og Economic dimensjoner. Technical-dimensjonen overlapper med §4.2 NFRs — ikke gjenta der.