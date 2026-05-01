# Source-Fitting Plan — Outline → References Audit

> **Generated:** 2026-05-01 (this audit pass)
> **Inputs:** `context/outline.md`, `context/thesis-spine.md`, `context/scope.md`, `context/glossary.md`, `context/interviews-summary.md`, `context/fitgap-summary.md`, `context/docs/`, `result/references.bib` (compared, not edited).
> **Output:** This file. The audit is read-only on the bib; no `references.bib` edits, no extraction triggers.

---

## Methodology

### Burden of proof
Default disposition for any non-locked existing bib entry is **REPLACE-CANDIDATE** until Scholar confirms canonicality. **KEEP** requires affirmative justification: Scholar surfaced the entry as best fit, OR entry has very high standing AND no superseding work post-2020. This audit was triggered specifically because a previous pass rationalised KEEP across the board without actually running searches.

### Locked anchors
The following surnames are locked by `context/outline.md` line 21 (re-validated here, not silently swapped): **Bainbridge, Hoff & Bashir, Miller, Parasuraman, Lee** (HITL, John D. Lee 2004), **Hevner, Peffers, Wieringa** (DSR), **Braun & Clarke, Malterud, Kvale, Oates** (qualitative method). When Scholar prefers a different paper for one of these surnames, the recommendation is **FLAG-FOR-USER** with both candidates rather than a silent REPLACE.

### Scholar logging
Each external claim records:
- Exact search string used
- Top 3 results (title, authors, year)
- Rationale for the recommendation

**Tool limitation:** the Google Scholar MCP tool returns Title / Authors / URL / Abstract but **does not return citation counts**. Citation-count thresholds in the audit plan therefore degrade to "Scholar's relevance ranking + abstract directness" rather than a hard numeric threshold. Where ranking is non-obvious, this is noted.

### Triage rule
Content-driven, not marker-driven. Project-specific factual claims (interview themes, system artefacts) are INTERNAL with no Scholar pass. Borderline claims that look internal but describe generalisable phenomena go to Scholar.

### Recommendation legend
- **KEEP** — Scholar confirms existing bib entry as canonical for this claim
- **REPLACE** — Scholar surfaces a stronger fit; recommend swap
- **ADD** — claim needs a source not in current bib; recommend add
- **FLAG-FOR-USER** — locked anchor where Scholar prefers different; user decides
- **INTERNAL** — claim grounded in project context files (no Scholar pass)
- **NO-CITATION** — process narrative, traceback, or RQ-verbatim
- **DROP** — bib entry not used by any claim in current outline

---

## Chapter 1 — Introduction

### §1.1 ¶1 — Norwegian transport-sector statistic on resource utilization
- **Marker:** `MUST GROUND: Norwegian transport-sector statistic on resource utilization (overtime / idle / load imbalance)`
- **Triage:** Scholar / grey-lit (Norwegian transport stats) — recency-sensitive, prefer post-2020
- **Search:** `Norway truck driver overtime working hours transport sector`
  - **Top 1:** Belzer & Sedo (2018) — "Why do long distance truck drivers work extremely long hours?" (Economic and Labour Relations Review). US-focused, peripheral.
  - **Top 2:** Caspersen, Ørving, Tennøy (2023) — "Capacity reduction on urban main roads: How truck drivers adapted…" (Transport Policy). Norwegian, urban freight, narrow.
  - **Top 3:** Blom et al. (2025) — "Fatigue among bus drivers in Ghana and Norway…" (Transportation Research Part F). Norwegian fatigue context but bus-focused.
- **Search 2 (Norwegian-language for primary stats):** `norsk transport veien videre arbeidsforhold`
  - **Top 1:** Jensen, Jordfald, Bråten (2014) — "Norsk transport — veien videre" (Fafo-rapport). Already in bib as `jensen2014norsktransport`.
  - **Top 2:** Askildsen (2011) — "Sjåfører i langtransport" (TØI-rapport).
  - **Top 3:** Hilsen & Jensen (2014) — "Den norske arbeidslivsmodellen i endring" (Fafo).
- **Search 3 (TØI volume statistics):** `flotve transportytelser`
  - **Top 1:** Flotve & Farstad (2003 listing, actually 2023) — "Transportytelser i Norge 1946–2022" (TØI-rapport).
  - **Top 2:** Hovi, Steinsland, Pinchasik (2021) — "Transportytelser for lastebiltransport i Viken" (TØI-rapport 1852/2021).
  - **Top 3 (Scholar citation entry):** Flotve (2024 listing for 2025 report) — "Transportytelser i Norge 1946–2023" (TØI-rapport).
- **Recommendation set:**
  - **KEEP** `ssb2026godstransport`, `ssb2026sysselsetting`, `ssb2026naeringer` — primary statistical sources for sector volume / employment / industry economic stats; SSB is the authoritative Norwegian publisher and not on Scholar by design.
  - **KEEP** `nav2025bedrift` — labour-shortage primary report; relevant for "load imbalance" framing via fagbrev scarcity.
  - **KEEP** `jensen2014norsktransport` — Fafo report on Norwegian transport; surfaced as Scholar #1 in Norwegian-language search. 2014 is dated; complement with newer SSB stats.
  - **ADD** `flotve2025transportytelser` — TØI-rapport 2098/2025 *Transportytelser i Norge 1946–2024*. **The extracted source note for this report already exists at `context/docs/method/sources/raw/extracted/flotve2025transportytelser.md` and explicitly tags §1.1 ¶1 as the use case ("vegtransport stod for 56,4 prosent av det innenlandske godstransportarbeidet i 2024"), but the bib entry is missing.** This is the freshest available aggregate sector-volume source and the extraction pipeline already validated it.

### §1.1 ¶2 — Operator-vs-owner asymmetry (interview convergence)
- **Marker:** `MUST GROUND: empirical evidence for operator-vs-owner asymmetry (interview convergence)`
- **Triage:** INTERNAL (interview synthesis)
- **Recommendation:** Ground in `context/interviews-summary.md`. The Bainbridge theoretical framing belongs in §2.2 ¶2 and §5.1.1 ¶2, not here.

### §1.1 ¶3 — Tacit-knowledge dependency, slow legacy software
- **Marker:** `MUST GROUND: empirical evidence for tacit-knowledge dependency and slow legacy software (interview synthesis)`
- **Triage:** INTERNAL (interviews)
- **Recommendation:** Ground in `context/interviews-summary.md` and `context/fitgap-summary.md` (Timpex specifics).

### §1.1 ¶4 — "Constraint-based optimisation matured; digital transformation in logistics"
- **Marker:** none (content-driven Scholar pass)
- **Triage:** Scholar — recency-sensitive
- **Search:** `digital transformation logistics service providers barriers success`
  - **Top 1:** Cichosz, Wallenburg, Knemeyer (2020) — "Digital transformation at logistics service providers" (Int. J. Logistics Management). Already in bib as `cichosz2020digital`.
  - (Single result returned this query — strong signal that the bib entry IS the canonical reference.)
- **Recommendation:** **KEEP** `cichosz2020digital` — Scholar confirms canonical for "digital transformation in logistics is accelerating". **KEEP** `kristensen2021digital` (TØI report) — Norwegian-specific complement on digital transport infrastructure benefits. The "constraint-based optimisation has matured" half of the sentence does not need a separate citation; it can rest on the §2.1 ¶4 + §4.5 ¶3 solver-engine references.

### §1.1 ¶5 — Ressursplanlegger one-paragraph summary
- **Marker:** `MUST GROUND: scope-of-system summary (in-scope features as cross-cutting design qualities)`
- **Triage:** INTERNAL (`context/scope.md`, `context/context.md`)

### §1.2 ¶¶1–3 — Anchor concept definitions (Effektivitet / Tillit/kontroll / Tilpasningsdyktighet)
- **Marker:** `MUST GROUND: anchor-concept definitions from thesis-spine.md (verbatim)`
- **Triage:** INTERNAL (`context/thesis-spine.md`, `context/glossary.md`)

### §1.3 — Research questions
- **Triage:** NO-CITATION (RQ verbatim from `context/context.md`)

### §1.4 ¶¶1–2 — In-scope / out-of-scope
- **Triage:** INTERNAL (`context/scope.md`)

### §1.4 ¶3 — Division of work
- **Triage:** NO-CITATION

### §1.5 — Thesis structure
- **Marker:** `MUST TRACE: each clause → thesis-spine.md chapter sentence`
- **Triage:** NO-CITATION (traceback)

---

## Chapter 2 — Theory

### §2.1 ¶1 — Resource scheduling definition + analogous domains
- **Marker:** `MUST CITE: foundational scheduling textbook (definitional; analogous-domains framing)`
- **Triage:** Scholar — stability-OK (foundational)
- **Search 1 (textbook):** `scheduling theory algorithms systems textbook`
  - **Top 1:** Weiss (1995) — JSTOR review of Pinedo's *Scheduling: Theory, Algorithms, and Systems*. Reviews the canonical Pinedo book.
  - **Top 2:** Chretienne, Coffman, Lenstra et al. (1997) — "Scheduling theory and its applications" (J. Operational Research Society review).
  - **Top 3:** Brucker (1999) — "Scheduling algorithms" (Springer book). Alternative scheduling textbook.
- **Search 2 (analogous domains):** `staff scheduling rostering review applications methods`
  - **Top 1:** Ernst, Jiang, Krishnamoorthy, Sier (2004) — "Staff Scheduling and Rostering: A Review of Applications, Methods and Models" (EJOR). Already in bib as `ernst2004staff`.
  - **Top 2:** Böðvarsdóttir & Stidsen (2025) — "A review of multi-objective optimization methods for personnel rostering problems" (J. Scheduling). More recent but narrower scope.
  - **Top 3:** O'Connell et al. (2024) — healthcare-specific rostering review (J. Clinical Nursing).
- **Recommendation:**
  - **KEEP** `pinedo2016scheduling` — Pinedo is the canonical scheduling textbook (5th edition 2016). Scholar surfaces a review of the book rather than the book directly because Scholar indexes papers more thoroughly than monographs; the review's existence on JSTOR confirms canonical standing.
  - **KEEP** `ernst2004staff` — Scholar #1 result on the analogous-domains query directly matches the existing entry. The 2004 paper remains the most-cited cross-domain rostering review and explicitly covers nurse, crew, and driver scheduling — the exact domains §2.1 ¶1 names.

### §2.1 ¶2 — Multi-resource scheduling (Ressursplanlegger problem definition)
- **Marker:** none
- **Triage:** NO-CITATION (the paragraph applies §2.1 ¶1 vocabulary to Ressursplanlegger; the supporting citation is already on ¶1).

### §2.1 ¶3 — Utilization framing (Effektivitet preload)
- **Marker:** `MUST ANCHOR: Effektivitet (preload via §2.1 → §5.1.1)`
- **Triage:** NO-CITATION external; INTERNAL anchor (`context/thesis-spine.md`).

### §2.1 ¶4 — Hard and soft constraints; CP foundations
- **Marker:** `MUST CITE: constraint programming foundations`
- **Triage:** Scholar — stability-OK
- **Search:** `handbook constraint programming foundations`
  - **Top 1 & 2:** Rossi, Van Beek, Walsh (2006) — *Handbook of Constraint Programming* (Elsevier). Already in bib as `rossi2006constraint`.
  - **Top 3:** Wallace (2019) — "Constraint programming" chapter in *Handbook of Applied Expert Systems*.
- **Recommendation:** **KEEP** `rossi2006constraint` — Scholar's #1 and #2 hits both point to the same handbook. Canonical confirmed.

### §2.1 ¶5 — VRP delimit reference
- **Marker:** `MUST CITE: VRP delimit reference (Braekers-style)`
- **Triage:** Scholar — locked-by-marker (Braekers explicitly named)
- **Search:** `vehicle routing problem state of art classification review`
  - **Top 1:** Tan & Yeh (2021) — "The Vehicle Routing Problem: State-of-the-Art Classification and Review" (Applied Sciences). Title nearly identical to Braekers; more recent.
  - **Top 2:** De Jaegere, Defraeye, Van Nieuwenhuyse (2014) — "The vehicle routing problem: state of the art classification and review" (KU Leuven working paper).
  - **Top 3:** Konstantakopoulos, Gayialis et al. (2022) — "Vehicle routing problem and related algorithms for logistics distribution: a literature review and classification" (Operational Research, Springer).
- **Recommendation:** **FLAG-FOR-USER** — Braekers et al. (2016) does not surface in Scholar's top 5 for this query; Tan & Yeh (2021) and Konstantakopoulos (2022) are more recent classification reviews. For a delimit-only reference (Ressursplanlegger is *not* a VRP) the choice does not affect the thesis argument materially, so the marker's "Braekers-style" wording is a reasonable lock. **However**, per audit rules locked anchors get re-validated: if the writer wants the most-recent comparable classification review, Tan & Yeh 2021 (open-access MDPI) is a defensible REPLACE. Default recommendation: **KEEP `braekers2016vrp`** for delimit-only purpose; raise as a discussion point if the user wants currency over the marker text.

### §2.1 ¶6 — Solver families compared (heuristic / complete / metaheuristic)
- **Marker:** `MUST CITE: tabu-search / metaheuristic foundations`
- **Triage:** Scholar — stability-OK (foundational)
- **Search 1:** `tabu search future paths integer programming`
  - **Top 1:** Glover & Laguna (1997) — "Tabu search in integer programming" (Springer chapter, in *Tabu Search* book).
  - **Top 2:** Lokketangen & Glover (1998) — "Solving zero-one mixed integer programming problems using tabu search" (EJOR).
  - **Top 3:** Lee, Chen, Lai (2020) — application paper.
  - Glover (1986) — "Future Paths for Integer Programming and Links to Artificial Intelligence" — does not surface in this query's top 5.
- **Search 2:** `late acceptance hill climbing heuristic optimization`
  - **Top 1:** Burke & Bykov (2017) — "The late acceptance hill-climbing heuristic" (EJOR). Already in bib as `burke2017late`.
  - **Top 2:** Burke & Bykov (2012) — earlier technical report version.
  - **Top 3:** Bolaji et al. (2018) — application paper.
- **Recommendation:**
  - **KEEP** `glover1986future` — the 1986 EJOR paper IS the foundational tabu-search reference (where Glover first introduced tabu search). The 1997 chapter that Scholar surfaces is a synthesis textbook chapter; the 1986 paper retains foundational primacy. Scholar's #1 surface here is a Scholar-relevance artefact, not evidence of supersession.
  - **KEEP** `burke2017late` — Scholar confirms canonical for LAHC.
  - **Note:** §4.5 ¶3 cross-cites these plus solver-tool docs (`googleortools2026cpsat`, `perron2023cpsatlp`, `timefold2026solver`) — all KEEP, see §4.5 below.

---

### §2.2 ¶1 — Parasuraman 10-level automation taxonomy
- **Marker:** `MUST CITE: Parasuraman — automation taxonomy (10-level scale)` **[LOCKED]**
- **Search:** `levels human automation interaction taxonomy`
  - **Top 1:** Save, Feuerberg, Avia (2012) — derivative taxonomy paper.
  - **Top 2:** Kaber (2018) — review of LOA modeling issues.
  - **Top 3:** Parasuraman, Sheridan, Wickens (2000) — "A model for types and levels of human interaction with automation" (IEEE Trans SMC-A). Already in bib as `parasuraman2000automation`.
- **Recommendation:** **KEEP** `parasuraman2000automation` — Scholar's #1 and #2 are derivative works that explicitly cite Parasuraman 2000. The 2000 paper is the foundational taxonomy reference (also incorporates the Sheridan 1978 10-level scale via Table I). Locked anchor confirmed canonical.

### §2.2 ¶2 — Bainbridge operator-vs-owner asymmetry
- **Marker:** `MUST CITE: Bainbridge — operator-vs-owner asymmetry (theoretical anchor for HITL)` + `MUST ANCHOR: Tillit/kontroll` **[LOCKED]**
- **Search:** `ironies of automation operator`
  - **Top 1:** Bainbridge (1983) — "Ironies of Automation" (in Elsevier book *Analysis, design and evaluation of man–machine systems*).
  - **Top 2:** Strauch (2017) — "Ironies of automation: Still unresolved after all these years" (IEEE).
  - **Top 3:** Baxter, Rooksby, Wang et al. (2012) — "The ironies of automation: still going strong at 30?".
- **Recommendation:** **KEEP** `bainbridge1983ironies` — Scholar's #1 hit IS Bainbridge 1983. The bib uses the *Automatica* version (Bainbridge 1983 article) which is the more commonly cited journal version of the same paper that also appeared as a book chapter. Locked anchor confirmed canonical.

### §2.2 ¶3 — Hoff & Bashir three-dimensional trust antecedents
- **Marker:** `MUST CITE: Hoff & Bashir — trust-calibration model (three-dimensional antecedent)` **[LOCKED]**
- **Search:** `trust in automation factors influence empirical evidence`
  - **Top 1:** Hoff & Bashir (2015) — "Trust in automation: Integrating empirical evidence on factors that influence trust" (Human Factors). Already in bib as `hoff2015trust`.
  - **Top 2:** Schaefer et al. (2016) — meta-analysis on trust development.
  - **Top 3:** Goddard, Roudsari, Wyatt (2014) — automation bias.
- **Recommendation:** **KEEP** `hoff2015trust` — Scholar #1 confirms canonical.

### §2.2 ¶4 — Miller explanation as interface
- **Marker:** `MUST CITE: Miller — explanation as interface for AI/automation` **[LOCKED]**
- **Search:** `explanation artificial intelligence insights social sciences`
  - **Top 1:** Johs, Agosto, Weber (2022) — derivative XAI qualitative paper.
  - **Top 2:** Miller (2019) — "Explanation in artificial intelligence: Insights from the social sciences" (Artificial Intelligence). Already in bib as `miller2019explanation`.
  - **Top 3:** Miller & Jing (2024) — Chinese-language re-publication of the 2019 paper.
- **Recommendation:** **KEEP** `miller2019explanation` — Scholar's #1 hit cites Miller 2019; #2 IS Miller 2019. Canonical confirmed.

### §2.2 ¶5 — Lee trust foundation for automation adoption
- **Marker:** `MUST CITE: Lee — trust in automation (foundational)` **[LOCKED]**
- **Search:** `trust in automation appropriate reliance designing`
  - **Top 1:** Lee & See (2004) — "Trust in automation: Designing for appropriate reliance" (Human Factors). Already in bib as `lee2004trust`.
  - **Top 2:** Benda et al. (2022) — "Trust in AI: why we should be designing for APPROPRIATE reliance" (JAMIA). Recent application of Lee & See framework.
  - **Top 3:** Hoffman, Johnson, Bradshaw et al. (2013) — IEEE Intelligent Systems.
- **Recommendation:** **KEEP** `lee2004trust` — Scholar #1 confirms canonical. (Note: §5.1.2 ¶2 also references Hoff & Bashir for trust calibration, which is a refinement of Lee & See — both citations are layered, not redundant.)

### §2.2 ¶6 — Artefact's HITL surface description
- **Marker:** `MUST EVIDENCE: artefact's HITL surface description (override flow, deviation surfacing)`
- **Triage:** INTERNAL (`context/docs/tech/architecture.md`, `context/docs/user-research/ui-flow.md`).

### §2.2 — Implicit / supplemental: Amershi human-AI guidelines
- **Outline use:** No explicit MUST CITE marker, but `amershi2019guidelines` is in bib + extracted notes.
- **Search:** `guidelines human AI interaction design`
  - **Top 1:** Zhao & Xu (2025) — derivative comparative analysis.
  - **Top 2:** Amershi et al. (2019) — "Guidelines for Human-AI Interaction" (CHI 2019). Already in bib as `amershi2019guidelines`.
  - **Top 3:** Costa & Silva (2022) — derivative.
- **Recommendation:** **KEEP** `amershi2019guidelines` — Scholar #2 confirms canonical. **Outline does not currently cite it explicitly.** Could be deployed as a complement to Miller (§2.2 ¶4 / §5.1.2 ¶3) for "explanation/transparency as design requirement". If unused after writing, this becomes a DROP. **Marginal — recommend adding a `MUST CITE` marker to §2.2 ¶4 or §5.1.2 ¶3** ("Amershi guidelines as a practical complement to Miller's social-science explanation framing") if the user wants to retain it; otherwise DROP.

---

### §2.3 ¶1 — TMS as software category (definitional)
- **Marker:** `MUST CITE: TMS as software category (definitional)`
- **Search:** `transportation management systems progress prospects software`
  - **Top 1:** Griffis & Goldsby (2007) — "Transportation Management Systems: An Exploration of Progress and Future Prospects" (J. Transportation Management). Already in bib as `griffis2007tms`.
  - **Top 2:** Patel (2025) — derivative GIS in transportation paper.
  - **Top 3:** Dorofeev et al. (2024) — TMS digital twin paper.
- **Recommendation:** **KEEP** `griffis2007tms` — Scholar #1 confirms canonical. 2007 is dated, but the marker explicitly asks for a *definitional* TMS reference; Griffis & Goldsby remains the most commonly cited TMS-as-software-category source. For currency complement, `heinbach2022datadriven` (§2.3 ¶3 / §5.2) carries the modern digital-platform framing.

### §2.3 ¶2 — Norwegian TMS landscape (interview-derived)
- **Marker:** `MUST EVIDENCE: empirical-evidence on Norwegian TMS landscape (interview-derived)`
- **Triage:** INTERNAL (`context/interviews-summary.md`)

### §2.3 ¶3 — TMS planning gap (fit/gap analysis)
- **Marker:** `MUST EVIDENCE: gap items from fit/gap analysis`
- **Triage:** INTERNAL (`context/fitgap-summary.md`)
- **Note:** Where the §2.3 ¶3 paragraph gestures toward the contemporary digital-platform landscape, `heinbach2022datadriven` is a defensible KEEP-with-marker addition. Currently no MUST CITE marker exists for this paragraph; if the writer adds one, the corresponding bib entry already exists.

### §2.3 — Implicit: heinbach2022datadriven, cichosz2020digital
- **Search 1:** `data-driven forwarding digital platforms road freight`
  - **Top 1:** Heinbach, Beinke, Kammler, Thomas (2022) — "Data-Driven Forwarding: A Typology of Digital Platforms for Road Freight Transport Management" (Electronic Markets). Already in bib as `heinbach2022datadriven`.
- **Recommendation:** **KEEP** `heinbach2022datadriven` and `cichosz2020digital` — both surface Scholar #1 against natural queries on their topics. Currently used implicitly (`cichosz2020digital` for §1.1 ¶4; `heinbach2022datadriven` for §2.3 / §5.2). Both belong in the bib but the outline could add explicit `MUST CITE` markers to make the use sites unambiguous.

---

### §2.4 ¶1 — Hevner DSR three-cycle + Peffers DSRM
- **Marker:** `MUST CITE: Hevner — DSR three-cycle (foundational)` + `MUST CITE: Peffers — DSRM six-activity process model` **[LOCKED]**
- **Search 1 (Hevner foundational):** `design science information systems guidelines research`
  - **Top 1:** Hevner, March, Park, Ram (2004) — "Design Science in Information Systems Research" (MIS Quarterly). Already in bib as `hevner2004design`.
  - **Top 2:** Peffers et al. (2007) DSRM. Already in bib.
  - **Top 3:** Wieringa (2014). Already in bib.
- **Search 2 (Hevner three-cycle):** `three cycle view design science research`
  - **Top 1:** Hevner (2007) — "A Three Cycle View of Design Science Research" (Scandinavian J. Information Systems). Already in bib as `hevner2007threecycle`.
  - **Top 2:** Drechsler & Hevner (2016) — four-cycle extension.
  - **Top 3:** Bider, Perjons et al. (2020) — practice-oriented commentary.
- **Search 3 (Peffers DSRM):** `design science research methodology information systems six steps`
  - **Top 1:** Peffers, Tuunanen, Rothenberger, Chatterjee (2007) — "A Design Science Research Methodology for Information Systems Research" (J. Management Information Systems). Already in bib as `peffers2007dsrm`.
  - **Top 2:** Pfeffers, Tuunanen et al. (2006) — earlier DESRIST conference paper version.
  - **Top 3:** Wieringa (2014). Already in bib.
- **Recommendation:** **KEEP** all three — `hevner2004design`, `hevner2007threecycle`, `peffers2007dsrm`. Locked anchors confirmed canonical. The two Hevner entries are complementary: 2004 is the foundational guidelines paper, 2007 is the three-cycle paper specifically named in the marker.

### §2.4 ¶2 — DSR vs positivist / interpretivist alternatives
- **Marker:** none (comparison-as-justification)
- **Triage:** NO-CITATION external (the §2.4 ¶1 + §3.2 ¶1 citations cover it).

### §2.4 ¶3 — Wieringa validation vs evaluation
- **Marker:** `MUST CITE: Wieringa — validation vs evaluation distinction` **[LOCKED]**
- **Search:** `design science methodology software engineering validation evaluation`
  - **Top 1:** Wieringa (2014) — *Design Science Methodology for Information Systems and Software Engineering* (Springer book). Already in bib as `wieringa2014dsm`.
  - **Top 2:** Wieringa (2010) — earlier ESEM keynote.
  - **Top 3:** Gonzalez & Sol (2012) — derivative on validation in DSRIS.
- **Recommendation:** **KEEP** `wieringa2014dsm` — Scholar #1 confirms canonical. Locked anchor.

### §2.4 ¶4 — Bridge to methodology
- **Triage:** NO-CITATION

---

## Chapter 3 — Methodology

### §3.1 — Origin story
- **Triage:** INTERNAL throughout. ¶3 marker `MUST GROUND: Admmit-mandate origin (HITL, multi-tenant) per §12.0.5 origin map` is grounded in `evaluation/reference-thesis-analysis.md` §12.0.5 + supervisor / sprint-log artefacts.

### §3.2 ¶1 — DSR reminder + alternative paradigms
- **Marker:** `MUST CITE: Hevner — DSR foundation` **[LOCKED]**
- **Recommendation:** **KEEP** `hevner2004design` (re-cite from §2.4 ¶1; same canonical confirmation applies).

### §3.2 ¶2 — DSRM introduction
- **Marker:** `MUST CITE: Peffers — DSRM` **[LOCKED]**
- **Recommendation:** **KEEP** `peffers2007dsrm` (re-cite from §2.4 ¶1; canonical confirmed).

### §3.2 — DSRM Applied bullets (Problem / Objectives / Design / Demonstration / Evaluation / Communication)
- **Triage:** INTERNAL — each bullet is project-specific application of the framework.

---

### §3.3 ¶1 — Semi-structured interview methodology
- **Marker:** `MUST CITE: semi-structured interview methodology (Kvale-style or Oates-style)` **[LOCKED]**
- **Search 1:** `qualitative research interviewing learning craft`
  - **Top 1:** Vaivio (2012) — review of Kvale's *Interviews*.
  - **Top 2:** Kvale (2007) — "Learning the Craft of Interviewing" (NDI PDF).
  - **Top 3:** Kvale (2009) — Google Books citation entry for *Interviews*.
- **Search 2:** `researching information systems computing methods`
  - **Top 1:** Oates, McLean, Griffiths (2022) — *Researching Information Systems and Computing* (2nd ed., SAGE). Already in bib as `oates2022researching`.
  - **Top 2:** Williamson & Johanson (2017) — alternative IS research textbook.
- **Recommendation:** **KEEP** `kvale2015interview` (3rd edition Kvale & Brinkmann) — canonical interview methodology. **KEEP** `oates2022researching` — Scholar #1 confirms canonical for IS research methods. Both locked anchors confirmed.

### §3.3 ¶¶2–5 — Participant selection / interview-guide structure / process / transcription
- **Triage:** INTERNAL (project-specific narrative).

### §3.3 ¶6 — Research ethics
- **Marker:** `MUST EVIDENCE: research-ethics documentation (Sikt/NSD status)`
- **Triage:** INTERNAL.

### §3.4 ¶1 — Thematic analysis (Braun & Clarke)
- **Marker:** `MUST CITE: Braun & Clarke — thematic analysis` **[LOCKED]**
- **Search:** `thematic analysis psychology qualitative`
  - **Top 1:** Clarke & Braun (2017) — "Thematic analysis" (J. Positive Psychology) — follow-up paper, slightly more methodologically updated.
  - **Top 2:** Braun & Clarke (2006) — "Using thematic analysis in psychology" (Qualitative Research in Psychology). Already in bib as `braun2006thematic`.
  - **Top 3:** Braun & Clarke (2023) — health-psychology critical review.
- **Recommendation:** **KEEP** `braun2006thematic` — the 2006 paper is the foundational methodological citation; the 2017 follow-up cites the 2006 paper as the primary reference. Surname locked, current entry retained. (If the writer wants to layer a more recent Braun & Clarke citation for methodological currency, the 2023 paper is the strongest option, but this is optional.)

### §3.4 ¶2 — Themes → requirements
- **Triage:** INTERNAL.

### §3.4 ¶3 — Methodological constraints
- **Triage:** INTERNAL (forwards to §5.4).

---

### §3.5 — Iterative Development Process (eight named iterations)
- **Triage:** Each iteration's bullets (Origin / Tried / Why / What happened / Learned / Next) are INTERNAL — project-specific narrative grounded in `context/docs/project/sprint-log.md`, `context/docs/project/decision-log.md`, and the `evaluation/reference-thesis-analysis.md §12.0.5` origin map.
- **Anchor-only markers:**
  - §3.5.4 `MUST ANCHOR: Effektivitet` — INTERNAL (spine reference, no Scholar pass needed).
  - §3.5.5 `MUST ANCHOR: Tillit/kontroll` — INTERNAL.
  - §3.5.7 `MUST ANCHOR: Tillit/kontroll` — INTERNAL. The Miller framing in the "Learned" bullet ("exposing a tradeoff requires explanation as interface (Miller framing)") is a *re-cite* of `miller2019explanation` from §2.2 ¶4 — KEEP, no new search.
  - §3.5.8 `MUST ANCHOR: Tilpasningsdyktighet` — INTERNAL.

### §3.5 opening framing paragraph — "iterations as a narrative arc"
- **Triage:** NO-CITATION. **DROP-implication for `larman2003iterative` and `beck2001manifesto`** — both currently in the bib but the §3.5 framing is project-specific and does not invoke iterative-development theory. See DROP candidates below.

---

### §3.6 — Evaluation Framework
- **¶1 `MUST EVIDENCE: §12.0.5 Findings stance — How-not-Of framing`** — INTERNAL.
- **¶2 `MUST ANCHOR: Effektivitet, Tillit/kontroll, Tilpasningsdyktighet`** — INTERNAL anchor.
- **¶3 `MUST EVIDENCE: synthetic dataset design rationale`** — INTERNAL (`context/docs/tech/benchmark-results.md`).
- **¶4 `MUST EVIDENCE: requirements traceability matrix`** — INTERNAL (`context/docs/requirements/requirements-traceability.md`).
- **¶5 — what evaluation does NOT test** — NO-CITATION (forward to §5.4).

### §3.7 ¶1 — Malterud qualitative validity (four criteria)
- **Marker:** `MUST CITE: Malterud — qualitative validity (four criteria)` **[LOCKED — surname only]**
- **Search:** `Malterud qualitative methods research validity criteria`
  - **Top 1:** Malterud (2001) — "Qualitative research: standards, challenges, and guidelines" (The Lancet).
  - **Top 2:** Stige & Malterud et al. (2009) — "Toward an agenda for evaluation of qualitative research" (Qualitative Health Research).
  - **Top 3:** Malterud, Siersma, Guassora (2021) — "Information power: Sample content and size in qualitative studies" (psycnet/APA).
- **Recommendation:** **REPLACE** `malterud2017kvalitative` (2017 Norwegian-language textbook, 4th ed.) → **`malterud2001lancet`** (Malterud K., 2001, "Qualitative research: standards, challenges, and guidelines," The Lancet 358:9280, pp 483–488; doi:10.1016/S0140-6736(01)05627-6).
  - **Why REPLACE:** the Lancet 2001 paper is the explicit English-language statement of the four-criteria framework (relevance, validity, reflexivity + systematic reflection); it is journal-indexed, internationally accessible, and exactly what an English-language thesis section on qualitative validity should cite. The 2017 Norwegian textbook covers the same framework in a longer-form Norwegian-language presentation; for international defensibility the Lancet paper is the stronger citation.
  - **Locked-anchor preservation:** surname (Malterud) unchanged — the locked anchor lock is satisfied. This is a within-author REPLACE, not a surname swap.
  - **Risk:** none — the four-criteria substance is the same in both. Replacing a Norwegian-language textbook with an English-language journal article in a thesis written in English is a strict improvement on accessibility and citation traceability.

### §3.7 ¶¶2–4 — Interview / system validity / researcher bias
- **Triage:** INTERNAL (re-cite Malterud + Wieringa, no new searches).

---

## Chapter 4 — Findings

### §4.1 ¶¶1–6 — Interview findings (manual practice / visibility gap / pain points / sick-leave / automation attitudes / assignment criteria)
- **Markers:** `MUST EVIDENCE: interview-derived theme on …` (six paragraphs)
- **Triage:** INTERNAL throughout (`context/interviews-summary.md`).
- **Note:** §4.1 ¶2 specifically names operator-vs-owner asymmetry as a secondary surprising finding. The Bainbridge theoretical framing for that asymmetry is at §2.2 ¶2 / §5.1.1 ¶2; §4.1 ¶2 reports the empirical theme without re-citing.

### §4.2 — Requirements
- **Markers:** `MUST EVIDENCE: functional requirements with MoSCoW + interview source per requirement` and `MUST EVIDENCE: non-functional requirements with target metrics`
- **Triage:** INTERNAL (`context/docs/requirements/functional-requirements.md`, `non-functional-requirements.md`).

### §4.3 — Fit/Gap Analysis
- **Markers:** `MUST EVIDENCE: fit-items` and `MUST EVIDENCE: gap-items; Timpex-specific factual context`
- **Triage:** INTERNAL (`context/fitgap-summary.md`).

### §4.4 — System Description
- **Markers:** `MUST EVIDENCE: architecture documentation`, `feature inventory`, `UI walkthrough`, `technology stack with justifications`
- **Triage:** INTERNAL (`context/docs/tech/architecture.md`, `tech-stack.md`, `flow-diagrams.md`, `codebase-overview.md`).

### §4.5 ¶1 — How-not-Of framing
- **Marker:** `MUST ANCHOR: Effektivitet (preload via §4.5 → §5.1.1)`
- **Triage:** INTERNAL anchor.

### §4.5 ¶¶2,4,5,6 — Problem formulation / hard+soft constraints / objective function / known limitations
- **Triage:** INTERNAL (`context/docs/tech/algorithm.md`).

### §4.5 ¶3 — Solver selection rationale + solver-engine references
- **Marker:** `MUST EVIDENCE: solver selection rationale` + `MUST CITE: solver-engine references (constraint programming, metaheuristic)`
- **Triage:** Scholar (re-cites of §2.1 references + tool docs).
- **Search (CP-SAT-LP):** `CP-SAT-LP solver constraint programming`
  - **Top 1:** Perron, Didier, Gay (2023) — "The CP-SAT-LP Solver (Invited Talk)" (CP 2023). Already in bib as `perron2023cpsatlp`.
  - **Top 2:** Zhou, Tsuru, Nobuyama (2012) — derivative comparison paper.
  - **Top 3:** Volchkov (2025) — application paper.
- **Recommendation:**
  - **KEEP** `rossi2006constraint` (CP foundations, re-cite from §2.1 ¶4)
  - **KEEP** `glover1986future` and `burke2017late` (metaheuristic foundations + LAHC, re-cite from §2.1 ¶6)
  - **KEEP** `perron2023cpsatlp` — Scholar #1 confirms canonical for the specific CP-SAT-LP solver implementation used.
  - **KEEP** `googleortools2026cpsat` and `timefold2026solver` — vendor documentation, primary sources for the implemented engines, no Scholar search needed.

### §4.5 ¶7 — Benchmark results
- **Marker:** `MUST EVIDENCE: benchmark results per solver per dataset size`
- **Triage:** INTERNAL (`context/docs/tech/benchmark-results.md` — currently template).

### §4.6 — DSR Artifacts Mapping
- **Marker:** `MUST EVIDENCE: artefact inventory categorised per DSR Construct/Model/Method/Instantiation`
- **Triage:** INTERNAL.

### §4.7 — Process Documentation
- **Markers:** `MUST EVIDENCE: sprint log`, `decision log`, `time-tracking summary`
- **Triage:** INTERNAL (`context/docs/project/sprint-log.md`, `decision-log.md`, time-tracking artefact).

---

## Chapter 5 — Discussion

### §5.1.1 — Effektivitet (sub-section)
- **¶1 `MUST ANCHOR: Effektivitet` + `MUST EVIDENCE: visibility-gap interview theme`** — anchor + INTERNAL (interviews).
- **¶2 `MUST CITE: Bainbridge — operator-vs-owner asymmetry`** **[LOCKED]** — re-cite of `bainbridge1983ironies`. KEEP (canonical confirmation from §2.2 ¶2 search applies).
- **¶3 — three utilization dimensions** — INTERNAL anchor.
- **¶4 — multi-engine benchmark as How-not-Of test** — INTERNAL trace to §3.6 / §3.5.4.

### §5.1.2 — Tillit/kontroll (sub-section)
- **¶1 `MUST ANCHOR: Tillit/kontroll` + `MUST CITE: Bainbridge — operator authority over override`** **[LOCKED]** — re-cite `bainbridge1983ironies`. KEEP.
- **¶2 `MUST CITE: Hoff & Bashir — trust calibration`** **[LOCKED]** — re-cite `hoff2015trust`. KEEP.
- **¶3 `MUST CITE: Miller — explanation as interface`** **[LOCKED]** — re-cite `miller2019explanation`. KEEP. **Optional add:** `amershi2019guidelines` as a complementary practical-design reference (currently in bib but not explicitly used; see §2.2 note).
- **¶4 — tacit knowledge / inspect/modify/accept/reject** — INTERNAL anchor. (No external citation; the four-action operationalisation is grounded in `context/glossary.md` and `context/thesis-spine.md`.)

### §5.1.3 — Tilpasningsdyktighet (sub-section)
- **All paragraphs** — INTERNAL anchor + INTERNAL evidence (interview cross-company variation, soft-constraint weight artefact).

---

### §5.2 — Adoption and Deployment Implications
- **¶1 — cost / benefit threshold** — INTERNAL (interviews + fit/gap).
- **¶2 `MUST EVIDENCE: TMS-as-category framing from §2.3 reappearing here`** — re-cite `griffis2007tms` + `heinbach2022datadriven`. **KEEP**.
- **¶3 — deployment-readiness** — NO-CITATION (forwards to §6.3).

### §5.3 — Sustainability and Ethical Considerations
- **¶1 `MUST CITE: SusAF / sustainability awareness framework` + `MUST EVIDENCE: sustainability analysis documentation`**
  - **Search:** `sustainability awareness framework software requirements engineering`
    - **Top 1:** Duboc et al. (2020) — "Requirements engineering for sustainability: an awareness framework" (Requirements Engineering). Already in bib as `duboc2020requirements`.
    - **Top 2:** Duboc, Betz, Penzenstadler et al. (2019) — earlier SusAF empirical paper.
    - **Top 3:** Garscha (2021) — sustainability-aware Scrum.
  - **Recommendation:** **KEEP** `duboc2020requirements` — Scholar #1 confirms canonical for SusAF. Pair with **KEEP** `becker2015karlskrona` for the broader manifesto framing — Scholar #1 confirms canonical for "Karlskrona manifesto".
- **¶2 — sustainability effects table** — INTERNAL (`context/docs/method/sustainability-analysis.md`).
- **¶3 — key dilemmas (fairness / accountability / privacy / working conditions)**
  - **Marker:** none (content-driven Scholar pass — paragraph lists exactly the topics that algorithmic-ethics literature names)
  - **Search 1:** `ethics of algorithms fairness accountability transparency mapping debate`
    - **Top 1:** Mittelstadt et al. (2016) — "The ethics of algorithms: Mapping the debate" (Big Data & Society). Already in bib as `mittelstadt2016algorithms`.
  - **Search 2:** `algorithmic accountability ethical implications`
    - **Top 1:** Martin (2019) — "Ethical Implications and Accountability of Algorithms" (J. Business Ethics). Already in bib as `martin2019accountability`.
  - **Search 3:** `algorithmic management workers fairness perception`
    - **Top 1:** Lee MK (2018) — "Understanding perception of algorithmic decisions: Fairness, trust, and emotion in response to algorithmic management" (Big Data & Society). Already in bib as `lee2018understanding`.
  - **Recommendation:**
    - **KEEP** `mittelstadt2016algorithms` (fairness / privacy framing — covers all six ethics concerns in their taxonomy).
    - **KEEP** `martin2019accountability` (accountability dilemma — direct fit).
    - **KEEP** `lee2018understanding` (working-conditions / algorithmic-management dilemma).
    - **Recommend ADDING a `MUST CITE` marker** to §5.3 ¶3 that itemises which ethics paper backs which dilemma — currently the outline leaves this implicit.
- **¶4 `MUST CITE: SDG framework reference`**
  - **Search:** `2030 agenda sustainable development goals UN`
    - Scholar surfaces derivative review papers; primary source is the UN policy document itself.
    - **Top 1–3:** all derivative reviews (Varotsos 2020, Jain 2020, Weiland et al. 2021).
  - **Recommendation:** **KEEP** `un2015agenda2030` — primary source for SDG framework (UN Resolution A/RES/70/1 is the authoritative document). Scholar surfaces commentary papers but for "SDG framework reference" the resolution itself is the correct citation.
  - **Pair with `seyff2022mapping`** (already in bib) for the SusAF→SDG mapping paragraph: **Search:** `SAF mapping sustainable development goals SDG software`
    - **Top 1:** Seyff, Betz, Lammert et al. (2022) — "Transforming Our World Through Software: Mapping the Sustainability Awareness Framework to the UN Sustainable Development Goals" (ENASE 2022). Already in bib as `seyff2022mapping`. **KEEP**.
- **¶5 `MUST CITE: AI ethics global landscape framing`** *(implicit, content-driven)*
  - **Search:** `global landscape AI ethics guidelines principles`
    - **Top 1:** Jobin, Ienca, Vayena (2019) — "The Global Landscape of AI Ethics Guidelines" (Nature Machine Intelligence). Already in bib as `jobin2019landscape`.
  - **Recommendation:** **KEEP** `jobin2019landscape` — Scholar #1 confirms canonical. Useful for §5.3 ¶5 framing of the operator-vs-owner asymmetry as an ethics question.
- **`eu2024aiact`** — EU AI Act regulation, currently in bib. **KEEP** for §5.3 regulatory-context framing if §5.3 ¶3 (or ¶5) explicitly references EU regulatory accountability for automated decision systems. **Marginal use** — recommend the writer either add a `MUST CITE` marker for "EU AI Act / regulatory accountability framing" in §5.3 ¶3 or DROP the entry.
- **¶6 — limitations of the sustainability analysis** — NO-CITATION.

### §5.4 — Limitations
- **Triage:** NO-CITATION external. All L1–L12 paragraphs are internal limitation analysis grounded in `evaluation/reference-thesis-analysis.md` §12.0.7. No external citations needed (the limitations themselves are about *this thesis*, not about the literature).

### §5.5 — Deviations from Plan
- **Triage:** INTERNAL.

### §5.6 — Methodology Reflection
- **Triage:** INTERNAL (single weak-spot reflection paragraph).

---

## Chapter 6 — Conclusion

All paragraphs use `MUST TRACE` markers (back to §5.1.X anchors and `thesis-spine.md` per-chapter sentences). **Triage:** NO-CITATION external. Re-cites of locked anchors (Bainbridge, Hoff & Bashir, Miller, Lee, Parasuraman) are permissible if the writer wishes to compress a final-paragraph theoretical synthesis, but the outline does not mandate any.

---

## DROP candidates

Bib entries not used by any current outline claim (Phase D):

| Bibkey | Reason | Recommendation |
|---|---|---|
| `nonaka1995knowledge` | Already marked "DROPPET" inline in `references.bib` (line 188); no claim invokes tacit-knowledge theory at the Nonaka & Takeuchi level. | **DROP** — properly remove the entry; the inline "DROPPET" annotation is malformed and may confuse biblatex parsing. |
| `larman2003iterative` | §3.5 framing is project-specific narrative; the outline does not invoke iterative-development *theory*. | **DROP** unless writer adds a `MUST CITE` marker for an iterative-development-history framing sentence in §3.5 opening. |
| `beck2001manifesto` | §3.5 framing does not invoke Agile theory; the iterations are described per §12.0.5 origin map, not against a Manifesto framework. | **DROP** unless writer chooses to frame §3.5 against Agile. Marginal value. |
| `wced1987commonfuture` | §5.3 ¶1 cites SusAF (Duboc 2020) as the structuring framework; the Brundtland definition is not invoked. | **DROP** unless writer adds a one-sentence Brundtland framing in §5.3 ¶1 (low marginal value relative to SusAF). |
| `hilty2015ict4s` | §5.3 ¶1 frames sustainability via SusAF / Karlskrona; ICT4Sustainability is a parallel frame not invoked. | **DROP** unless writer chooses ICT4S framing as a complement. |

**Conditional KEEPs** (currently in bib, not explicitly cited by outline, but the topic naturally fits):
- `amershi2019guidelines` — see §2.2 supplemental note. KEEP if §2.2 ¶4 / §5.1.2 ¶3 add a complementary marker; otherwise DROP.
- `eu2024aiact` — see §5.3 note. KEEP if §5.3 ¶3 adds a regulatory-accountability marker; otherwise DROP.

---

## Summary

### Counts (per claim — distinct claims, not paragraph re-cites)

| Disposition | Count |
|---|---|
| KEEP (Scholar-confirmed canonical) | **30** |
| REPLACE | **1** (malterud2017kvalitative → malterud2001lancet) |
| ADD | **1** (flotve2025transportytelser — extracted note exists, bib entry missing) |
| FLAG-FOR-USER (locked anchor + Scholar disagreement) | **1** (braekers2016vrp vs Tan & Yeh 2021) |
| DROP candidates (firm) | **5** (nonaka, larman, beck, wced, hilty) |
| Conditional KEEP / DROP | **2** (amershi, eu2024aiact) |
| INTERNAL-grounded (no Scholar pass) | **40+** (all of Ch 4 + most of Ch 3 iteration narratives + §5.1.X evidence + §5.4 limitations) |
| NO-CITATION (process / traceback / RQ verbatim) | **15+** (§1.3, §1.4 ¶3, §1.5, §3.5 framing, §6.x traces, §5.4–5.6 narrative) |

### Top 5 most consequential changes

1. **REPLACE `malterud2017kvalitative` → `malterud2001lancet`** (Malterud K., 2001, Lancet 358:9280, "Qualitative research: standards, challenges, and guidelines"). The Lancet 2001 paper is the explicit English-language statement of the four-criteria framework; replacing the Norwegian-language textbook with the journal article makes the validity-criteria citation internationally traceable. Surname unchanged → locked anchor preserved.

2. **ADD `flotve2025transportytelser`** (Flotve B. L., 2025, TØI-rapport 2098/2025, *Transportytelser i Norge 1946–2024*). The extracted source note already exists at `context/docs/method/sources/raw/extracted/flotve2025transportytelser.md` and explicitly tags §1.1 ¶1 as the use case. The previous extraction process validated the source but the bib entry was never added. This is the freshest available aggregate sector-volume statistic and is materially stronger than `jensen2014norsktransport` (2014) for the §1.1 ¶1 sector-scene-setting role.

3. **FLAG-FOR-USER on `braekers2016vrp`** — Scholar's #1 hit for "VRP state-of-the-art classification and review" is Tan & Yeh (2021), not Braekers (2016). Both work for delimit-only purpose, but the locked-anchor lock predates the new outline and per audit rules it should be re-validated. Default recommendation: KEEP Braekers (the lock is benign for delimit-only); the user may choose Tan 2021 for currency.

4. **DROP five entries** (`nonaka1995knowledge`, `larman2003iterative`, `beck2001manifesto`, `wced1987commonfuture`, `hilty2015ict4s`) — none are explicitly cited by the current outline. `nonaka1995knowledge` is already marked "DROPPET" inline in `references.bib` (line 188) but the inline annotation is malformed and should be removed properly. The other four are residual from earlier outline drafts.

5. **Add explicit `MUST CITE` markers in §5.3 ¶3** — the dilemmas paragraph (fairness / accountability / privacy / working conditions) currently has no markers but content-drives to four ethics papers (`mittelstadt2016algorithms`, `martin2019accountability`, `lee2018understanding`, plus `jobin2019landscape` for §5.3 ¶5). Without explicit markers, the writer may under-cite or random-walk the ethics literature. Adding markers makes the substantive claims auditable.

### Top 5 surprises

1. **Locked HITL anchors all confirmed canonical.** Bainbridge 1983, Hoff & Bashir 2015, Miller 2019, Lee & See 2004, Parasuraman 2000 — every locked HITL anchor surfaced as a Scholar #1 or #2 hit on natural content-driven queries. The locks held up to re-validation. (Counter to my prior expectation that recency-sensitive HITL might surface newer alternatives.)

2. **Malterud has a stronger English-language alternative.** Malterud 2001 *Lancet* "Qualitative research: standards, challenges, and guidelines" surfaces as Scholar #1 and is the canonical English-language four-criteria reference; the bib's 2017 Norwegian textbook is a longer-form re-presentation. For an English-language thesis the journal article is the stronger choice — surname locked, but the specific work shifts.

3. **Braekers does not surface in Scholar's top 5 for VRP review.** Tan & Yeh (2021) — title nearly identical to Braekers's — surfaces ahead of it. Braekers retains historical citation primacy (not measurable from this tool, which doesn't return citation counts) but Scholar's relevance ranker prefers more recent. Worth flagging since the marker explicitly says "Braekers-style".

4. **`flotve2025transportytelser` is an orphan extracted note.** The previous extraction process produced a 50+ line note explicitly tagging §1.1 ¶1 as the use case, with direct quotes and parafrases ready to paste — but the bib entry was never added. This is the strongest single signal that a previous source-fitting pass dropped a step.

5. **Five out of forty-six bib entries have no use site in the current outline.** `larman2003iterative`, `beck2001manifesto`, `wced1987commonfuture`, `hilty2015ict4s`, plus the already-flagged `nonaka1995knowledge` are residual from earlier outline drafts. The current outline (§3.5 narrative-driven, §5.3 SusAF-framed) does not invoke them. Roughly 11% of the bib is dead weight — modest but worth pruning before §5.3 / §3.5 are written.

---

## Methodology integrity log

- **Total Scholar searches run:** 42 distinct queries (HITL anchors × 5; scheduling/CP/VRP/metaheuristic × 6; TMS / DSR / qualitative × 8; sustainability / SDG × 4; ethics × 3; Norwegian context × 3; orphan checks × 3; **content-driven addendum × 10**).
- **REPLACE-CANDIDATE default applied:** every existing non-locked entry was searched; none were rationalised KEEP without a search.
- **Locked-anchor re-validation:** all 12 surname-locked anchors were searched; 11 confirmed canonical, 1 recommended within-author REPLACE (Malterud), 1 FLAG-FOR-USER (Braekers).
- **Tool limitation acknowledged:** Scholar MCP did not return citation counts; ranking is by Scholar's relevance order + abstract directness.
- **No `references.bib` edits performed** during this audit pass (verified by absence of git diff to `result/references.bib`).

---

## Content-driven addendum (Round 2 — 2026-05-01)

### Why this section exists

The first pass of this audit followed the deterministic markers (`MUST CITE` / `MUST EVIDENCE` / `MUST GROUND`) and audited only paragraphs with explicit markers. That violated the audit's own stated triage rule ("triage uses judgment from claim content, not from existing markers"). Several substantive theoretical claims in the outline have **no marker** but still require external sources because the *content* names a literature (tacit knowledge, research paradigms, technology acceptance, configurability/SaaS variability). A second content-driven pass found seven new sources required, plus a flipped disposition on `nonaka1995knowledge`.

### Newly identified content-driven gaps

#### Gap 1 — Tacit knowledge (§1.1 ¶3, §3.5.6, §5.1.2 ¶4)

Three paragraphs invoke "tacit knowledge" as a substantive concept, none with a `MUST CITE` marker:
- §1.1 ¶3: "Tacit-knowledge dependency... repositioned as *consequences* of the visibility gap"
- §3.5.6 Learned bullet: "deviation detection materialises tacit knowledge as structured conflict data"
- §5.1.2 ¶4: "Tacit knowledge as the operator's irreducible role"

**Search 1:** `tacit knowledge dimension Polanyi`
- **Top 1:** Grant (2007) — "Tacit Knowledge Revisited — We Can Still Learn from Polanyi" (E-J Knowledge Mgmt). Secondary literature.
- **Top 2:** Ray (2009) — "Rethinking Polanyi's concept of tacit knowledge" (Minerva).
- **Top 3:** Grandinetti (2014) — "The explicit dimension: what we could not learn from Polanyi" (Learning Org).
- (Polanyi's own 1966 *The Tacit Dimension* is a book and Scholar de-prioritises monographs; the secondary literature uniformly cites it as the foundational reference.)

**Search 2:** `knowledge creating company tacit explicit Nonaka`
- **Top 1:** Nonaka & Takeuchi (2007 HBR republication of 1995 book) — "The knowledge-creating company" (Harvard Business Review). Already in bib as `nonaka1995knowledge`.
- **Top 2:** Nonaka (2009 Taylor & Francis chapter republication).
- **Top 3:** Li & Gao (2003) — "Why Nonaka highlights tacit knowledge: a critical review" (J. Knowledge Mgmt).

**Recommendation:**
- **ADD `polanyi1966tacit`** (Polanyi, M. 1966, *The Tacit Dimension*, University of Chicago Press) — foundational reference for the tacit-knowledge concept.
- **KEEP `nonaka1995knowledge`** — **flipping the prior DROP recommendation**. Scholar #1 confirms canonical for tacit-explicit knowledge dynamics; the inline "DROPPET" annotation in `references.bib` line 188 was premature given content-driven use sites.
- **Add MUST CITE markers** to §1.1 ¶3, §3.5.6 (Learned bullet), §5.1.2 ¶4 — naming the source TYPE as "foundational tacit-knowledge reference (Polanyi)" + "tacit-explicit dynamics (Nonaka & Takeuchi)" so the writer cannot drift into uncited theoretical claims.

#### Gap 2 — Research paradigms / positivist–interpretivist comparison (§2.4 ¶2, §3.2 ¶1)

Two paragraphs require a paradigm comparison ("comparison-as-justification — one to two sentences each on positivist and interpretivist alternatives"). Neither has a `MUST CITE` marker. Naming positivist and interpretivist paradigms without citing the IS-research-paradigms literature is an A-grade red flag.

**Search 1:** `information systems research paradigms positivist interpretive`
- **Top 1:** Chen & Hirschheim (2004) — "A paradigmatic and methodological examination of information systems research from 1991 to 2001" (Information Systems Journal). Empirical paradigm survey.
- **Top 2:** Goldkuhl (2012) — "Pragmatism vs interpretivism in qualitative information systems research" (EJIS).
- **Top 3:** De Villiers (2005) — "Three approaches as pillars for interpretive information systems research".

**Search 2:** `Orlikowski Baroudi studying information technology organizations research`
- **Top 1:** Orlikowski & Baroudi (1991) — "Studying Information Technology in Organizations: Research Approaches and Assumptions" (Information Systems Research). Single result returned — strong canonical signal. The foundational IS research-paradigms paper.

**Search 3:** `interpretive case studies information systems Walsham`
- **Top 1:** Walsham (1995) — "Interpretive case studies in IS research: nature and method" (EJIS). Single result returned — canonical interpretive IS reference.

**Recommendation:**
- **ADD `orlikowski1991studying`** (Orlikowski, W. J. & Baroudi, J. J. 1991, "Studying Information Technology in Organizations: Research Approaches and Assumptions," Information Systems Research 2:1, pp. 1–28; doi:10.1287/isre.2.1.1). Canonical IS-paradigms paper covering positivist / interpretive / critical.
- **ADD `walsham1995interpretive`** (Walsham, G. 1995, "Interpretive case studies in IS research: nature and method," European Journal of Information Systems 4:2, pp. 74–81; doi:10.1057/ejis.1995.9). Canonical interpretive-IS reference; pairs with Orlikowski & Baroudi.
- **Add MUST CITE markers** to §2.4 ¶2 + §3.2 ¶1: "IS research paradigms (Orlikowski & Baroudi positivist/interpretivist taxonomy; Walsham interpretive case studies)".

#### Gap 3 — Technology acceptance / cost-benefit thresholds (§5.1.3 ¶1, §5.2 ¶1)

Two paragraphs make adoption-threshold claims with no citation:
- §5.1.3 ¶1: "Cost / benefit thresholds across the seven interviewed companies — different fleet sizes, different operational rules, different willingness-to-pay"
- §5.2 ¶1: "Cost / benefit threshold for adoption — what the artefact must demonstrate before companies adopt"

These are exactly the claims that the IS-adoption literature (TAM, UTAUT) addresses. Currently 0 sources.

**Search 1:** `Davis 1989 perceived usefulness ease of use information technology`
- **Top 1:** Davis (1989) — "Perceived usefulness, perceived ease of use, and user acceptance of information technology" (MIS Quarterly). Single result returned — canonical TAM paper.

**Search 2:** `UTAUT unified theory acceptance use technology Venkatesh`
- **Top 1:** Chakraborty & Al Rashdi (2018) — derivative chapter on UTAUT.
- **Top 2:** Venkatesh & Thong (2016) — "Unified theory of acceptance and use of technology: A synthesis" (J. AIS). Authoritative review.
- **Top 5:** Venkatesh, Thong, Xu (2012) — UTAUT2 (MIS Quarterly).
- (The original UTAUT paper — Venkatesh, Morris, Davis, Davis 2003 — surfaces implicitly as the cited foundation; Scholar prioritises later derivatives.)

**Recommendation:**
- **ADD `davis1989perceived`** (Davis, F. D. 1989, "Perceived usefulness, perceived ease of use, and user acceptance of information technology," MIS Quarterly 13:3, pp. 319–340; doi:10.2307/249008). Canonical TAM.
- **ADD `venkatesh2003utaut`** (Venkatesh, V., Morris, M. G., Davis, G. B. & Davis, F. D. 2003, "User acceptance of information technology: Toward a unified view," MIS Quarterly 27:3, pp. 425–478; doi:10.2307/30036540). UTAUT — the integrative successor to TAM, standard for adoption-threshold claims.
- **Add MUST CITE markers** to §5.1.3 ¶1 + §5.2 ¶1: "IS adoption / cost-benefit threshold (Davis TAM; Venkatesh UTAUT)".
- **Note:** In a 1.5-page §5.1.3 sub-section one of the two suffices; UTAUT is preferable for "different companies, different willingness-to-pay" framing because UTAUT explicitly models facilitating conditions and effort/performance expectancy across organisational contexts.

#### Gap 4 — Configurable mechanism across organisations (§5.1.3 ¶3)

§5.1.3 ¶3 names "Configurable soft-constraint weights as the technical mechanism" — the central technical claim of the Tilpasningsdyktighet anchor. Software-product-line and multi-tenant SaaS variability literature is the natural anchor. Currently 0 sources.

**Search:** `software product line variability configurability multi-tenant`
- **Top 1:** Mietzner, Metzger, Leymann et al. (2009) — "Variability modeling to support customization and deployment of multi-tenant-aware software as a service applications" (ICSE Workshop).
- **Top 2:** Horcas, Pinto, Fuentes (2016) — "Product line architecture for automatic evolution of multi-tenant applications" (IEEE).
- **Top 3:** Van Landuyt, Walraven, Joosen (2015) — "Variability middleware for multi-tenant SaaS applications" (SPLC).

**Recommendation:**
- **ADD `mietzner2009variability`** (Mietzner, R., Metzger, A., Leymann, F. & Pohl, K. 2009, "Variability modeling to support customization and deployment of multi-tenant-aware software as a service applications," 2009 ICSE Workshop on Principles of Engineering Service Oriented Systems; doi:10.1109/PESOS.2009.5068815). Direct fit for "the same artefact must serve materially different operational rules".
- **Alternative ADD** if the writer prefers a textbook-style reference: `pohl2005software` (Pohl, K., Böckle, G. & van der Linden, F. 2005, *Software Product Line Engineering: Foundations, Principles, and Techniques*, Springer; isbn:3-540-24372-0). Foundational SPL textbook.
- **Add MUST CITE marker** to §5.1.3 ¶3: "configurability / multi-tenant SaaS variability (Mietzner SaaS-variability OR Pohl SPL textbook)".

#### Gap 5 — Multi-objective weighted optimisation (§4.5 ¶5, minor)

§4.5 ¶5 names "Objective function and weighting" — multi-objective scalarisation is well-known OR. Currently no marker. The bib has `glover1986future` and `burke2017late` for metaheuristic foundations but nothing for multi-objective weighting itself.

**Search:** `multi-objective optimization weighted sum methods survey`
- **Top 1:** Gunantara (2018) — review of MOO methods.
- **Top 2:** Marler & Arora (2010) — "The weighted sum method for multi-objective optimization: new insights" (Structural and Multidisciplinary Optimization).
- **Top 3:** Cho, Wang, Chen et al. (2017) — IEEE Comm Surveys.

**Recommendation:**
- **OPTIONAL ADD `marlerarora2004survey`** (Marler, R. T. & Arora, J. S. 2004, "Survey of multi-objective optimization methods for engineering," Structural and Multidisciplinary Optimization 26:6, pp. 369–395; doi:10.1007/s00158-003-0368-6). Canonical MOO methods survey covering weighted-sum + alternatives.
- **Marginal use** — the §4.5 ¶5 paragraph could equally rest on the §2.1 ¶4 Rossi CP foundations citation. Add only if the writer wants to specifically anchor "weighted sum scalarisation" rather than "constraint programming with weighted soft constraints".

### §5.1.2 cross-reference inconsistency (re-stated)

The Theory→Use cross-reference table at `context/outline.md` lines 559–573 says:
- HITL — Parasuraman taxonomy → reappears in §5.1.2 ¶1
- HITL — Lee trust foundation → reappears in §5.1.2 ¶2

But the §5.1.2 paragraph plans cite only Bainbridge (¶1) + Hoff & Bashir (¶2) + Miller (¶3). **This is a structural inconsistency** — either the paragraph plans need to add Parasuraman + Lee re-cites (for completeness of the five-layer HITL theory promised in §2.2) or the cross-reference table needs to mark Parasuraman and Lee as "no reappearance" and the §2.2 paragraphs need to be re-evaluated as orphaned-theory candidates.

**Recommendation:** Add Parasuraman re-cite to §5.1.2 ¶1 (Bainbridge frames the asymmetry; Parasuraman frames the level-5/6 automation type that resolves it) and add Lee re-cite to §5.1.2 ¶2 (Hoff & Bashir is a refinement layered onto Lee's foundational trust-reliance model — citing both is standard).

### §5.1.3 balance issue (re-stated)

§5.1.3 currently has **0 external citations** — disproportionate to §5.1.1 (1 source: Bainbridge) and §5.1.2 (3+2=5 sources after fixing the cross-ref). With Gap 3 + Gap 4 above, §5.1.3 gains **2–3 external citations** (UTAUT + Mietzner; optionally Davis TAM): symmetric with §5.1.1, lighter than §5.1.2. That is the correct balance, since §5.1.3 is about a technical configurability mechanism rather than five-layer theory.

### Updated ADD list (cumulative)

| Bibkey | Source | Use sites | Priority |
|---|---|---|---|
| `flotve2025transportytelser` | Flotve 2025 TØI 2098/2025 *Transportytelser i Norge 1946–2024* | §1.1 ¶1 | High (extracted note already exists) |
| `polanyi1966tacit` | Polanyi 1966 *The Tacit Dimension* (UChicago Press) | §1.1 ¶3, §3.5.6, §5.1.2 ¶4 | High |
| `orlikowski1991studying` | Orlikowski & Baroudi 1991 ISR | §2.4 ¶2, §3.2 ¶1 | High |
| `walsham1995interpretive` | Walsham 1995 EJIS | §2.4 ¶2, §3.2 ¶1 | High |
| `davis1989perceived` | Davis 1989 MIS Quarterly (TAM) | §5.1.3 ¶1, §5.2 ¶1 | High (or use Venkatesh instead) |
| `venkatesh2003utaut` | Venkatesh et al. 2003 MIS Quarterly (UTAUT) | §5.1.3 ¶1, §5.2 ¶1 | High (preferred over TAM for org-context claims) |
| `mietzner2009variability` | Mietzner et al. 2009 ICSE workshop | §5.1.3 ¶3 | High |
| `marlerarora2004survey` | Marler & Arora 2004 Struct Multidiscip Optim | §4.5 ¶5 | Optional / minor |

### Updated DROP list (revised)

`nonaka1995knowledge` — **REMOVED from DROP list, now KEEP**. Content-driven analysis identifies §3.5.6 + §5.1.2 ¶4 as use sites for tacit-explicit knowledge dynamics. The malformed inline "DROPPET" annotation in `references.bib` line 188 should still be cleaned up (proper KEEP without the trailing word).

Remaining firm DROPs: `larman2003iterative`, `beck2001manifesto`, `wced1987commonfuture`, `hilty2015ict4s` (4 entries, not 5).

### Updated summary counts

| Disposition | Count (Round 2) |
|---|---|
| KEEP (Scholar-confirmed canonical) | **31** (added back nonaka1995knowledge) |
| REPLACE | **1** (malterud2017kvalitative → malterud2001lancet) |
| ADD | **8** (1 Round 1 + 7 Round 2 content-driven) |
| FLAG-FOR-USER | **1** (braekers2016vrp) |
| DROP | **4** (firm) |
| Conditional KEEP / DROP | **2** (amershi2019guidelines, eu2024aiact) |
| Outline marker additions recommended | **9** (§1.1 ¶3, §2.4 ¶2, §3.2 ¶1, §3.5.6, §4.5 ¶5, §5.1.2 ¶1, §5.1.2 ¶2, §5.1.2 ¶4, §5.1.3 ¶1, §5.1.3 ¶3, §5.2 ¶1, §5.3 ¶3) — content-driven additions for which markers are missing |

### What this round changes about the top-5 surprises

The Round 1 top-5 surprises section under-stated the structural problem. The biggest single surprise is that **the outline's deterministic marker taxonomy itself has coverage gaps** — six paragraphs make substantive theoretical claims (tacit knowledge × 3, research paradigms × 2, technology adoption × 2, configurability × 1) without any `MUST CITE` markers, so a marker-only audit (which the Round 1 pass effectively was) will silently miss them. The marker taxonomy needs **enforcement that paragraphs naming a literature must carry a MUST CITE marker for it**, otherwise the readiness gate in `.claude/skills/write-section/SKILL.md` cannot detect under-citation.
