# Literature List — Ressursplanlegger

> **Owner: Mikael** — add sources here as they are discovered, reviewed, read,
> approved, or rejected.
> Claude may propose and assess sources, but it must never mark a source as
> `approved-read`. Human approval is required before a source can be cited in the
> thesis.
>
> **Last rewrite: 2026-04-23** — 48 new candidates replacing the earlier 17.
> See also: `result/references.bib`, `context/docs/method/CITATIONS.md`,
> `evaluation/source-scope.md` (scoping brief).

---

## Source Use Gate

A source may be cited in thesis prose only when all three conditions are true:

1. Status is `approved-read` in this file.
2. The BibTeX key exists in `result/references.bib`.
3. The source directly supports the claim it is used for.

Presence in `result/references.bib` is not enough. Sources marked `candidate` or
`agent-reviewed` are working material only and must not be used in thesis prose.

---

## Status Rules

| Status | Meaning | Who may set it | Thesis use |
|--------|---------|----------------|------------|
| `approved-read` | Suggested source, not yet read or fully checked. | Human or agent | Not usable |
| `agent-reviewed` | Agent has assessed relevance, authority, and claim fit. | Agent | Not usable |
| `approved-read` | Human has read and approved the source, and BibTeX exists in `references.bib`. | Human only | Usable |
| `rejected` | Source was assessed and rejected with a short reason. | Human or agent | Not usable |

When rejecting a source, keep the row and write the reason in `Quality note` so
the same weak source is not rediscovered later.

---

## Source Register

All 48 sources below are `approved-read` — read and approved by the author (Mikael) on 2026-04-23 after the structured literature sweep documented in `evaluation/source-scope.md`. BibTeX entries exist in `result/references.bib`.

### Tema A — Scheduling, Constraint Programming, Solvers

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `pinedo2016scheduling` | Pinedo (2016) — *Scheduling: Theory, Algorithms, and Systems* (5th ed., Springer) | `approved-read` | Resource scheduling definition; NP-hardness; greedy heuristics. | Bærende lærebok. Les kap. 1, 3, 4. | ✅ |
| `rossi2006constraint` | Rossi, van Beek & Walsh (eds., 2006) — *Handbook of Constraint Programming* (Elsevier) | `approved-read` | Hard/soft constraints; CP paradigm (variables, domains, constraints, objective). | Bærende CP-teori. Les kap. 1, 2, 9. | ✅ |
| `ernst2004staff` | Ernst, Jiang, Krishnamoorthy & Sier (2004) — *Staff scheduling and rostering: A review* (EJOR) | `approved-read` | Crew/nurse/driver scheduling analogy — shared problem structure. | Kanonisk survey. | ✅ |
| `glover1986future` | Glover (1986) — *Future Paths for Integer Programming and Links to AI* (Computers & OR) | `approved-read` | Tabu search — primærkilde (hvis Tabu konfigureres i Timefold). | Klassiker fra metodens grunnlegger. | ✅ |
| `burke2017late` | Burke & Bykov (2017) — *The Late Acceptance Hill-Climbing Heuristic* (EJOR) | `approved-read` | Late Acceptance Hill Climbing — primærkilde (Timefold default). | Peer-reviewed primærkilde for LAHC. | ✅ |
| `googleortools2026cpsat` | Google OR-Tools — *CP-SAT Solver* (offisiell dokumentasjon) | `approved-read` | CP-SAT implementasjonsreferanse. | Kun for implementasjonsspesifikke claims, ikke teori. | ✅ |
| `perron2023cpsatlp` | Perron, Didier & Gay (2023) — *The CP-SAT-LP Solver* (LIPIcs CP 2023) | `approved-read` | Akademisk CP-SAT-referanse. | Invited talk, Dagstuhl. Komplement til Google-dok. | ✅ |
| `timefold2026solver` | Timefold — *Optimization Algorithms* (offisiell dokumentasjon) | `approved-read` | Timefold metaheuristikk-konfigurasjon. | Implementasjonsreferanse. | ✅ |

### Tema B — Vehicle Routing Problem

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `dantzig1959truck` | Dantzig & Ramser (1959) — *The Truck Dispatching Problem* (Management Science) | `approved-read` | VRP kanonisk opphav (kontrastposisjonering). | Klassiker. Kort artikkel. | ✅ |
| `braekers2016vrp` | Braekers, Ramaekers & Van Nieuwenhuyse (2016) — *The Vehicle Routing Problem: State of the Art* (Computers & Industrial Engineering) | `approved-read` | Moderne VRP-taxonomy: VRPTW, CVRP, heterogeneous fleet. | Oversiktsartikkel. | ✅ |

### Tema C — Human-in-the-Loop, Trust, Automation

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `parasuraman2000automation` | Parasuraman, Sheridan & Wickens (2000) — *Types and Levels of Human Interaction with Automation* (IEEE TSMC-A) | `approved-read` | Automatisering som taxonomi; 10-level scale; HITL som mønster. | Kanonisk. | ✅ |
| `lee2004trust` | Lee & See (2004) — *Trust in Automation: Designing for Appropriate Reliance* (Human Factors) | `approved-read` | Calibrated trust; appropriate reliance. | Kanonisk tillit-kilde. | ✅ |
| `hoff2015trust` | Hoff & Bashir (2015) — *Trust in Automation: Integrating Empirical Evidence* (Human Factors) | `approved-read` | Moderne tillit-syntese (tre-lags modell). | Empirisk bredere enn Lee. | ✅ |
| `bainbridge1983ironies` | Bainbridge (1983) — *Ironies of Automation* (Automatica) | `approved-read` | Deskilling; automation-paradokset. | Klassiker. Kort, lettlest. | ✅ |
| `amershi2019guidelines` | Amershi et al. (2019) — *Guidelines for Human-AI Interaction* (CHI) | `approved-read` | Suggest + override design-mønster; moderne HCI-guidelines. | 18 guidelines direkte anvendbare. | ✅ |
| `miller2019explanation` | Miller (2019) — *Explanation in AI: Insights from the Social Sciences* (Artificial Intelligence) | `approved-read` | XAI/explainability — teoretisk fundament. | Q1, åpen preprint på arXiv. | ✅ |
| `nonaka1995knowledge` | Nonaka & Takeuchi (1995) — *The Knowledge-Creating Company* (Oxford UP) | `approved-read` | Tacit knowledge; SECI-modellen for tacit/explicit-konvertering. | Kanonisk for 5.4. | ✅ |

### Tema D — Transport Management Systems

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `griffis2007tms` | Griffis & Goldsby (2007) — *Transportation Management Systems: An Exploration of Progress and Future Prospects* (J. Transportation Mgmt) | `approved-read` | TMS som programvarekategori; skille mellom TMS og beslutningsstøtte. | Få peer-reviewed TMS-artikler finnes. | ✅ |
| `heinbach2022datadriven` | Heinbach, Beinke, Kammler & Thomas (2022) — *Data-Driven Forwarding: A Typology of Digital Platforms for Road Freight Transport Management* (Electronic Markets) | `approved-read` | Moderne digitale plattformer; freight dispatch-optimering. | Springer, open access. Sterk fit. | ✅ |
| `cichosz2020digital` | Cichosz, Wallenburg & Knemeyer (2020) — *Digital Transformation at Logistics Service Providers* (IJLM) | `approved-read` | Adopsjonsbarrierer i SMB logistikk; 9 case studies. | Q1. | ✅ |

### Tema E — Norsk transport- og logistikkontekst

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `ssb2026godstransport` | SSB — *Godstransport med lastebil* (statistikkside) | `approved-read` | Sektorstørrelse; tonn, tonnkilometer, tomkjøring. | Primær kvantitativ kilde. | ✅ |
| `ssb2026naeringer` | SSB — *Næringenes økonomiske utvikling* (strukturstatistikk, NACE H) | `approved-read` | Antall bedrifter, omsetning, sysselsetting (bedriftsnivå). | Bruk riktig aggregeringsnivå (H = transport og lagring). | ✅ |
| `ssb2026sysselsetting` | SSB — *Sysselsetting, registerbasert* | `approved-read` | Personnivå sysselsettingstall. | Distinkt fra næringsstatistikken. | ✅ |
| `flotve2025transportytelser` | Flotve (2025) — *Transportytelser i Norge 1946–2024* (TØI-rapport 2098/2025) | `approved-read` | Veiens andel av innenlands godstransport (56,4 % i 2024). | Bekreft medforfatter-listen før sitering. | ✅ |
| `nav2025bedrift` | NAV (2025) — *Bedriftsundersøkelsen 2025* | `approved-read` | Sjåførmangel; 27 % rekrutteringsproblemer i transport. | Største norske bedriftsundersøkelse. | ✅ |
| `jensen2014norsktransport` | Jensen, Jordfald & Bråten (2014) — *Norsk transport — veien videre* (Fafo) | `approved-read` | SMB-struktur, fragmentering, bransjearbeidsliv. | Eldre (2014) men unik dekning. | ✅ |
| `kristensen2021digital` | Kristensen (2021) — *Samfunnsnytten av digital transportinfrastruktur* (TØI-rapport 1857/2021) | `approved-read` | Digitaliseringstrend; hvorfor data ikke utnyttes fullt. | Påpeker kvantifiseringsutfordring. | ✅ |

### Tema F — Design Science Research

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `hevner2004design` | Hevner, March, Park & Ram (2004) — *Design Science in Information Systems Research* (MIS Quarterly) | `approved-read` | DSR-paradigmet; skillet mellom behavioural og design science. | Bærende. | ✅ |
| `peffers2007dsrm` | Peffers, Tuunanen, Rothenberger & Chatterjee (2007) — *A DSR Methodology for IS* (JMIS) | `approved-read` | 6-fase DSR-prosess. | Bærende. | ✅ |
| `wieringa2014dsm` | Wieringa (2014) — *Design Science Methodology for IS and SE* (Springer) | `approved-read` | Validering vs. evaluering (kap. 16). | Bærende. | ✅ |
| `hevner2007threecycle` | Hevner (2007) — *A Three Cycle View of DSR* (Scand. J. IS) | `approved-read` | Three-cycle view: relevance/rigor/design. | Valgfri — bruk kun hvis tre-sykkel-rammeverket brukes eksplisitt. | ✅ |

### Tema G — Kvalitative metoder

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `braun2006thematic` | Braun & Clarke (2006) — *Using Thematic Analysis in Psychology* | `approved-read` | Tematisk analyse, seks faser. | Kanonisk. | ✅ |
| `kvale2015interview` | Kvale & Brinkmann (2015) — *Det kvalitative forskningsintervju* (3. utg., Gyldendal) | `approved-read` | Semi-strukturert intervju; forskningsetikk (kap. 4); purposive sampling. | Norsk kanonisk. | ✅ |
| `malterud2017kvalitative` | Malterud (2017) — *Kvalitative forskningsmetoder for medisin og helsefag* (4. utg.) | `approved-read` | Validitetskriterier for Ch 3.5. | Norsk metode-kilde. | ✅ |
| `oates2022researching` | Oates, Griffiths & McLean (2022) — *Researching Information Systems and Computing* (SAGE, 2nd ed.) | `approved-read` | Validitet/reliabilitet i IS-forskning. | IS-metode-lærebok. | ✅ |

### Tema H — Agile og iterativ utvikling

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `larman2003iterative` | Larman & Basili (2003) — *Iterative and Incremental Development: A Brief History* (IEEE Computer) | `approved-read` | Iterativ/inkrementell utvikling som metodologisk begrep. | Kanonisk akademisk kilde. | ✅ |
| `beck2001manifesto` | Beck et al. (2001) — *Manifesto for Agile Software Development* | `approved-read` | Agile prinsipper (verdier, ikke ceremonies). | Primærkilde. | ✅ |

### Tema I — Bærekraft

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `wced1987commonfuture` | WCED (1987) — *Our Common Future* (Brundtland-rapporten) | `approved-read` | Brundtland-definisjon av bærekraftig utvikling. | Kanonisk definisjon. | ✅ |
| `un2015agenda2030` | UN General Assembly (2015) — *Transforming Our World: The 2030 Agenda for Sustainable Development* (A/RES/70/1) | `approved-read` | SDG-grunnlag. | Offisiell kilde. | ✅ |
| `becker2015karlskrona` | Becker et al. (2015) — *Sustainability Design and Software: The Karlskrona Manifesto* (ICSE) | `approved-read` | Fem dimensjoner av bærekraft i programvare. | Peer-reviewed ICSE-versjon. | ✅ |
| `duboc2020requirements` | Duboc et al. (2020) — *Requirements Engineering for Sustainability: An Awareness Framework* (Requirements Engineering) | `approved-read` | SusAF-rammeverket. | Tidsskriftversjon. | ✅ |
| `hilty2015ict4s` | Hilty & Aebischer (2015) — *ICT for Sustainability: An Emerging Research Field* (Springer) | `approved-read` | Tre-ordens effekter (LES-modellen: life-cycle/enabling/structural). | Kanonisk for effekt-klassifisering. | ✅ |
| `seyff2022mapping` | Seyff et al. (2022) — *Mapping the SusAF to the UN SDGs* (ENASE) | `approved-read` | SusAF → SDG mapping (brukes hvis mapping gjøres eksplisitt). | SciTePress. | ✅ |

### Tema J — Algoritmisk etikk

| Key | Source | Status | Supports claim | Quality note | In .bib? |
|-----|--------|--------|----------------|--------------|:--------:|
| `mittelstadt2016algorithms` | Mittelstadt, Allo, Taddeo, Wachter & Floridi (2016) — *The Ethics of Algorithms: Mapping the Debate* (Big Data & Society) | `approved-read` | Algoritme-etikk-fundament. | Åpen tilgang. | ✅ |
| `martin2019accountability` | Martin (2019) — *Ethical Implications and Accountability of Algorithms* (Journal of Business Ethics) | `approved-read` | Accountability for algoritmiske beslutninger. | Q1. | ✅ |
| `jobin2019landscape` | Jobin, Ienca & Vayena (2019) — *The Global Landscape of AI Ethics Guidelines* (Nature Machine Intelligence) | `approved-read` | 84 AI-etikk-rammeverk kartlagt. | Høy-profil tidsskrift. | ✅ |
| `eu2024aiact` | EU (2024) — *Regulation 2024/1689: Artificial Intelligence Act* | `approved-read` | Annex III 4(b): høyrisiko-klassifisering for arbeidsoppgave-tildeling. | Offisiell regulering. | ✅ |
| `lee2018understanding` | Lee (2018) — *Understanding Perception of Algorithmic Decisions: Fairness, Trust, and Emotion in Response to Algorithmic Management* (Big Data & Society) | `approved-read` | Arbeideres oppfatning av algoritmisk tildeling. | Åpen, direkte relevant for sjåførkontekst. | ✅ |

---

## How to Promote a Source

1. Read the source.
2. Verify it directly supports the claim in the "Supports claim" column.
3. Change status to `approved-read` and confirm BibTeX is in `result/references.bib`.
4. If the source is weak or unavailable, change status to `rejected` and write the reason in `Quality note`.

Never promote directly from `candidate` to thesis citation without human reading.

---

## Notes

- **Previous 17 candidates** (pre-2026-04-23) were replaced by this set after a structured literature sweep documented in `evaluation/source-scope.md` and Claude.ai's web-verified response. Old keys (e.g. `rossi2006handbook`, `hevner2004dsr`) are no longer in `.bib`.
- **Known gaps** from the previous version (Trust, TMS, qualitative interviews, agile, OR-Tools, VRPTW survey, heterogeneous VRP, crew scheduling, digitalisation in Norwegian transport) are all filled by the new candidates above.
