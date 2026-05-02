# Thesis Outline — Ressursplanlegger

> Claude reads this before writing any chapter.
> Contains section-level outlines with content notes and target lengths.
> Update as structure evolves — but keep thesis-spine.md consistent with changes.

---

## Evidence Marker Taxonomy

All ¶-plans use these markers. The deterministic checker greps for them. Each marker must be on its own indented line under the ¶.

| Marker | Meaning | Used in |
|--------|---------|---------|
| `MUST CITE:` | Academic source TYPE required (foundational textbook, locked theoretical anchor by surname, methodological tradition, etc.). The downstream source-fitting task resolves the type to a specific bib entry plus verified source notes. | Ch 2, 3 |
| `MUST EVIDENCE:` | Empirical / system evidence TYPE required (interview-derived theme, fit/gap item, architecture documentation, benchmark results, etc.). Resolved to specific extracted-content references at write-time. | Ch 4 |
| `MUST ANCHOR:` | Must explicitly connect to the RQ, thesis spine, an earlier chapter section, or a locked anchor concept. For Ch 5 sub-sections the value MUST be one of `Effektivitet`, `Tillit/kontroll`, `Tilpasningsdyktighet` verbatim. Synonyms ("kontroll" alone, "fleksibilitet", "skalerbarhet", "human control", "menneskelig overstyring") fail the readiness gate. | Ch 5 (every sub-section); other chapters where structurally relevant |
| `MUST TRACE:` | Must trace back to a specific section, finding, or limitation. For Ch 6 RQ-answer paragraphs the format is `§5.1.X (<anchor name>)` with the anchor name verbatim. | Ch 6 |
| `MUST GROUND:` | Must be grounded in a context source — TYPE-described — with detailed evidence delivered later. | Ch 1 |

**Source-independence note (locked):** The current state of `result/references.bib`, `context/docs/method/sources/raw/extracted/`, `context/interviews-summary.md` theme labels, and `context/docs/tech/` is draft. This outline is structured around the locked substance (anchors, RQ, SQs, L1–L12, ChatSSB-derived A-grade pattern, five-layer HITL, §12.0.5 origin map). Sources and evidence are fitted to the structure as a downstream task. Locked theoretical authors may be referenced by surname (Bainbridge, Hoff & Bashir, Miller, Parasuraman, Lee, Hevner, Peffers, Wieringa, Orlikowski & Baroudi, Braun & Clarke, Malterud) — surnames are stable even when bib keys change.

---

## Chapter 1 — Introduction
**Owner:** Mikael | **Target:** ~4 pages | **Status:** Not started

**Purpose:** Open the thesis on the resource-utilization visibility gap, name the three anchor concepts, state the research question and sub-questions, delimit the scope, and set the narrative chain.

### Sections and content

**1.1 Background and Motivation** (~1.5 pages)

- ¶1: Open with a concrete Norwegian transport-sector fact about resource utilization (overtime, idle time, load imbalance) AND the seven-interview convergence on the visibility gap. Drop generic preamble — no "transport sector role in Norway, growing complexity"; no "in today's digital world".
  MUST GROUND: Norwegian transport-sector statistic on resource utilization (overtime / idle / load imbalance)
- ¶2: Introduce the traffic coordinator role and the operator-vs-owner stakeholder configuration. Coordinator runs the system day to day; owners and Admmit articulate the demand for algorithm-assisted planning. The configuration mirrors Bainbridge's *ironies of automation*.
  MUST GROUND: empirical evidence for operator-vs-owner asymmetry (interview convergence)
- ¶3: Tacit-knowledge dependency and slow legacy software repositioned as *consequences* of the visibility gap, not its origin. Tacit knowledge is used here as a domain concept (operational knowledge held by the coordinator that is not formally captured in any system) rather than as a theoretically anchored construct — no foundational theory citation is required at this scope. Reference Timpex and Opter as real Norwegian TMS named in the interview pool; describe other interviewed companies as using internal/custom systems. Neither Timpex nor Opter generates assignment plans automatically.
  MUST GROUND: empirical evidence for tacit-knowledge dependency and slow legacy software (interview synthesis)
- ¶4: Why now — constraint-based optimisation tools have matured, making algorithm-assisted planning feasible for SMEs; digital transformation in logistics is accelerating but the resource-utilization planning gap persists.
- ¶5: Introduce Ressursplanlegger in one paragraph — algorithm-assisted, multi-engine solver layer, drag-and-drop HITL timeline. Coordinator can inspect, modify, accept, or reject every algorithm-generated assignment.
  MUST GROUND: scope-of-system summary (in-scope features as cross-cutting design qualities)

**1.2 Anchor Concepts** (~0.5 pages, NEW)

- ¶1 (Effektivitet): three sentences naming the anchor verbatim. Define its three concrete dimensions (overtime, idle time, load balance) and state visibility as the precondition for optimization.
- ¶2 (Tillit/kontroll): three sentences naming the compound term verbatim. State the four operator actions (inspect, modify, accept, reject) and the inseparability of trust and control.
- ¶3 (Tilpasningsdyktighet): three sentences naming the anchor verbatim. State the cross-company adaptability claim and distinguish from skalerbarhet.
- These exact names recur in every later chapter; synonyms drift the spine.
  MUST GROUND: anchor-concept definitions from thesis-spine.md (verbatim)

**1.3 Research Questions** (~0.5 pages)

- ¶1: State the main RQ verbatim. One sentence on what it asks — the linking phrase between resource-utilization improvement and coordinator accountability.
- ¶2: List SQ1, SQ2, SQ3 verbatim. One sentence each on what each addresses, naming the anchor it maps to (SQ1 → Effektivitet, SQ2 → Tillit/kontroll, SQ3 → Tilpasningsdyktighet primary + cross-anchor).
- Do NOT discuss or justify here — that is for Chapter 3.

**1.4 Scope and Delimitations** (~0.5 pages)

- ¶1: In-scope summary. Bridge from §1.2 anchors as cross-cutting design qualities — every in-scope feature must satisfy at least one anchor.
  MUST GROUND: in-scope feature list
- ¶2: Out-of-scope items, each with a one-sentence "out because…" justification — Vehicle Routing Problem (assignment, not sequencing), full automation without HITL (Admmit mandate), cross-border / international transport regulations (Norwegian-only), real-time GPS / dispatch tracking (planning, not execution-monitoring), driver mobile app (web-only).
  MUST GROUND: out-of-scope list with justifications
- ¶3: Division of work — Mikael (user research, requirements, thesis writing), Embret (system development, algorithm implementation). Both contribute to discussion and analysis.

**1.5 Thesis Structure** (~0.5 pages)

- Single narrative-chain paragraph matching `thesis-spine.md` per-chapter sentences. Each clause links to the next by content bridge, not section labels — visibility-gap problem leads to layered theory which guides DSR methodology, surfacing empirical findings and the artefact, interpreted under the three anchors with hierarchical limitations, closing on each sub-question answered with no new material.
  MUST TRACE: each clause → thesis-spine.md chapter sentence

---

## Chapter 2 — Theory
**Owner:** Mikael | **Target:** ~8.5 pages, asymmetric depth | **Status:** Not started (cleared 2026-05-01 per restructure; previous draft archived under `evaluation/review/sections/archive/2026-05-01-ch2-supervisor-snapshot/`)

**Purpose:** Establish the theoretical foundation underpinning system design and research approach, with depth proportional to argumentative load.

### Sections and content

**2.1 Resource Scheduling** (~2 pages)

- ¶1: Define resource scheduling — assigning a set of limited resources (people, vehicles) to tasks over time, subject to constraints. Note analogous domains (nurse scheduling, crew scheduling, driver scheduling) to establish the multi-resource-assignment problem framing. Open with a single-resource example from an adjacent domain to build intuition before introducing multi-resource complexity. Introduce the traffic coordinator early — the human actor whose work the scheduling problem describes.
  MUST CITE: foundational scheduling textbook (definitional; analogous-domains framing)
- ¶2: Multi-resource scheduling — Ressursplanlegger assigns *both* an employee and a vehicle to each assignment. Increases combinatorial complexity compared to single-resource problems. Define the Ressursplanlegger problem in this vocabulary: assignments = tasks with fixed time windows and resource requirements; drivers + vehicles = resources with competency, availability, and capacity constraints; objective = maximise coverage + balance soft constraints.
- ¶3: **Utilization framing** (key add — preloads §5.1.1 Effektivitet vocabulary). Scheduling under the utilization lens — overtime, idle time between assignments, uneven driver load — not just constraint satisfaction. Visibility into current utilization is the precondition for optimization; the system's first contribution is making invisible utilization patterns legible.
  MUST ANCHOR: Effektivitet (preload via §2.1 → §5.1.1)
- ¶4: Hard and soft constraints. Hard constraints must be satisfied for feasibility (competencies, availability, no double-booking, vehicle type). Soft constraints define preferences with configurable weights (workload balance, driver preferences, priority).
  MUST CITE: constraint programming foundations
- ¶5: NP-hardness motivating heuristics. The Vehicle Routing Problem is referenced **only to delimit** — Ressursplanlegger is an assignment problem (who does what), not a sequencing problem. Sequencing is not part of the problem.
  MUST CITE: VRP delimit reference (Braekers-style)
- ¶6: Solver families compared briefly — heuristic / complete / metaheuristic. Each occupies a different point on the speed-quality tradeoff. Detailed solver descriptions in Ch 4.5.
  MUST CITE: tabu-search / metaheuristic foundations

**2.2 Human-in-the-Loop Automation** (~3 pages, the section that grows most)

Five-layer HITL theory: Parasuraman taxonomy + Lee trust foundation + Bainbridge operator-owner asymmetry + Hoff & Bashir trust calibration + Miller explanation. Layered, not replaced.

- ¶1: Define human-in-the-loop. Position Ressursplanlegger at automation level 5–6 on the Parasuraman scale (system suggests, human approves).
  MUST CITE: Parasuraman — automation taxonomy (10-level scale)
- ¶2 (NEW — Bainbridge frame): operator-vs-owner asymmetry; the irony of automation that automation needs are rarely articulated by those who must operate the system. Establishes the framing this thesis empirically extends to Norwegian transport's resource-planning domain.
  MUST CITE: Bainbridge — operator-vs-owner asymmetry (theoretical anchor for HITL)
  MUST ANCHOR: Tillit/kontroll
- ¶3 (NEW — Hoff & Bashir): three-dimensional model of trust antecedents (dispositional, situational, learned). Frames how operator trust forms over use of the artefact and what conditions enable calibrated trust rather than over- or under-reliance.
  MUST CITE: Hoff & Bashir — trust-calibration model (three-dimensional antecedent)
- ¶4 (NEW — Miller): explanation as interface; transparency as a design requirement for automated decision systems. Motivates the artefact's surfacing of algorithm reasoning (deviation alerts, scoring breakdown, time-quality control).
  MUST CITE: Miller — explanation as interface for AI/automation
- ¶5 (Lee — repositioned): trust foundation for automation adoption. Coordinators will not rely on a system whose decisions they cannot understand and override. Connect to adoption barriers developed in Ch 5.
  MUST CITE: Lee — trust in automation (foundational)
- ¶6: HITL as design constraint — the system must expose its reasoning so the coordinator can make informed corrections. Shapes the UI as much as the algorithm.
  MUST EVIDENCE: artefact's HITL surface description (override flow, deviation surfacing)

**2.3 Transport Management Systems (TMS)** (~1 page, **trimmed**)

> **Supervisor calibration 2026-05-02** (full log: `context/docs/project/supervisor-feedback.md`):
> - The TMS definition in ¶1 must be used unchanged in ¶2 and ¶3 — do not let the second paragraph narrow it implicitly. If a narrower sense is needed, flag the shift in-prose and revert.
> - State of the art must be named, not implied: list Timpex, Opter, and at least one international vendor that appears in the literature; describe what each covers.
> - Do not claim that all (or "Norwegian", or generally) transporters operate a TMS. Several interviewed companies do not. Frame TMS coverage as variable.
> - Theory chapter purity: no interview material in §2.3 prose. The Norwegian-TMS landscape claim in ¶2 is theory-of-the-domain (vendors named, what each does), not interview-grounded; reserve interview-validated coverage for Ch 4.
> - Bridge sentences between ¶1→¶2→¶3 are mandatory. The previous draft was flagged for abrupt transitions.
> - The internal term "fit/gap" must not appear unglossed in prose. ¶3 reframes the gap as "what existing systems cover vs. what is missing"; the planning label stays in `fitgap-summary.md` and Ch 4.3 outline only.

- ¶1: Define TMS as software category — order management, route planning, carrier management, freight billing. The TMS scope established here is the operational definition used through the rest of §2.3; later paragraphs do not narrow it without flagging.
  MUST CITE: TMS as software category (definitional)
- ¶2: TMS landscape — name the live state-of-the-art. **Timpex and Opter** are the real Norwegian TMS named by interviewed companies (treated here as public market facts, not interview evidence); neither generates assignment plans automatically. Add at least one international TMS vendor named in the literature to anchor the category beyond Norway. Frame adoption as variable across the sector — not all transport companies operate a TMS. Vendor-specific operational content (slow performance under concurrent use, etc.) is reserved for Ch 4.3.
  MUST CITE: international TMS vendor reference (literature-anchored)
- ¶3: What existing TMS cover vs. what is missing — the planning space between "order exists" and "driver is assigned" is unaddressed by the systems just named. Reframe in plain language ("what exists / what is missing"); do not surface the term "fit/gap" in prose. The structural claim is theoretical here; Ch 4.3 substantiates with the empirical comparison. Bridge sentence to Chapter 4.

**2.4 Design Science Research** (~2 pages, slightly expanded)

> **Supervisor calibration 2026-05-02** (full log: `context/docs/project/supervisor-feedback.md`):
> - Theory chapter purity: no interview material in §2.4 prose.
> - Definitional consistency: DSR is defined once in ¶1; ¶2 and ¶3 do not redefine it.
> - Bridge sentences between paragraphs are mandatory; the previous draft of Ch 2 was flagged for abrupt transitions throughout.
> - Be careful with sweeping claims about IS-research practice; prefer "the literature reports" over universal statements.

- ¶1: Define DSR — creating and evaluating artefacts to address practical problems. Name the three foundational cycles (relevance, design, rigor) and the six DSRM activities.
  MUST CITE: Hevner — DSR three-cycle (foundational)
  MUST CITE: Peffers — DSRM six-activity process model
- ¶2: Why DSR fits this project. **Comparison-as-justification** — one to two sentences each on positivist and interpretivist alternatives and why neither alone fits the artefact-plus-knowledge contribution.
  MUST CITE: IS research paradigms (Orlikowski & Baroudi — positivist/interpretivist taxonomy)
- ¶3: Validation vs evaluation. This thesis validates (predicts behaviour through benchmarking and requirements traceability) rather than evaluates (deploys in production). Acknowledged here, returned to in §3.6 and §5.4 L5.
  MUST CITE: Wieringa — validation vs evaluation distinction
- ¶4: Bridge to methodology — §3.2 will apply DSRM step-by-step to this specific project. Theory and application separated to keep §2.4 portable and §3.2 concrete.

> **Note:** §2.4 was previously "Related Work". Moved DSR here because sensor criterion NRT3 (Theoretical Insight) explicitly covers "knowledge of relevant methods". Algorithm-assisted dispatching and prior work are woven into §2.1 and §2.2 rather than a separate thin related-work section.

---

## Chapter 3 — Methodology
**Owner:** Mikael | **Target:** ~13.5 pages, expanded from prior 5–8p | **Status:** Not started

**Purpose:** Explain how the research was conducted and how the artefact was built, justify the choices, name the iterations honestly, and establish credibility.

Eight sections per the §8.4 reference-thesis pattern: origin story, applied DSRM, data collection, data analysis, named iterative development, evaluation framework, validity and reliability.

### Sections and content

**3.1 Defining the Task** (~1.5 pages, NEW per §8.4 + §12.1)

Origin story — how the project began. Reads as a story, not a specification.

- ¶1: How the project began — Admmit's bachelor task offer to NTNU. The decision to accept the task and build Ressursplanlegger.
- ¶2: Stakeholder access — seven traffic coordinators contacted directly by the team on its own initiative (Admmit did not broker introductions). Phone interviews on a single day.
- ¶3: HITL as Admmit mandate from project start — explicitly stated by Admmit at the outset, validated by interviews but not introduced by them. The multi-tenant architecture follows from Admmit's customer structure, also Admmit-mandated.
  MUST GROUND: Admmit-mandate origin (HITL, multi-tenant) per §12.0.5 origin map
- ¶4: Bridge to method — story-driven framing. Every later design choice is traceable to this origin or to the seven-interview dialogue, with the §12.0.5 origin map distinguishing interview-validated from designer / Admmit-mandated / domain-knowledge-driven decisions.

**3.2 Method Theory — DSR + DSRM Applied** (~2 pages, expanded per §11.5)

- ¶1: Brief DSR reminder + alternative paradigms briefly considered. One to two sentences each on positivist and interpretivist alternatives and why DSR fits the artefact-plus-knowledge structure of this work.
  MUST CITE: Hevner — DSR foundation
  MUST CITE: IS research paradigms (Orlikowski & Baroudi)
- ¶2: Introduce DSRM (Peffers six-step) as the structured framework operationalising DSR for this thesis.
  MUST CITE: Peffers — DSRM
- **DSRM Applied bullets** — each of the six DSRM activities gets one bullet of two to four sentences applied to this specific project (per §11.5, the single most copyable A-grade move):
  - **Problem Identification and Motivation:** the resource-utilization visibility-gap finding from interviews + Admmit's mandate motivated formalising algorithm-assisted planning. The problem is described concretely in §4.1 and discussed in §5.1.1.
  - **Objectives of a Solution:** locked anchor concepts — Effektivitet (overtime / idle time / load balance), Tillit/kontroll (coordinator authority via inspect / modify / accept / reject), Tilpasningsdyktighet (cross-company adaptability via configurable weights and rules).
  - **Design and Development:** algorithm-assisted planning platform with multi-engine solver layer (heuristic / constraint solver / metaheuristic) and drag-and-drop human-in-the-loop timeline. Built across eight named iterations described in §3.5.
  - **Demonstration:** synthetic-dataset multi-engine benchmark (described in §3.6) plus requirements traceability matrix as the coverage check.
  - **Evaluation:** what the artefact tests is *how* solver approaches compare under realistic constraint combinations — a methodologically independent test of how-not-of per §12.0.5. What it does not test (production deployment, real-world utilization gains, user-tested override flow) is forwarded to §5.4 limitations.
  - **Communication:** this thesis itself + recommendations to Admmit on deployment and configurability.

**3.3 Data Collection** (~1.5 pages)

The stakeholder-access narrative now lives in §3.1 (origin story); this section is purely methodological.

- ¶1: Semi-structured interviews — definition and justification grounded in the *form of data needed* (open enough to surface unexpected themes like the visibility gap, structured enough for cross-interview comparison). No required external methodology citation here; the methodological frame is DSRM Problem Identification (Peffers, cited in §3.2), not standalone qualitative interview craft. The thematic analysis citation (§3.4 Braun & Clarke) covers what was actually done with the data.
- ¶2: Participant selection — purposive sampling rationale. Seven coordinators / managers across companies of varying size and system maturity, geographic spread.
- ¶3: Interview guide structure — five themes (current tools / workflow, assignment criteria, sick-leave handling, automation attitudes, adoption criteria). Open questions. Guide included as appendix.
- ¶4: Process — phone interviews on a single day, recorded with consent. Conducted in Norwegian. Duration recorded in interview metadata.
- ¶5: Transcription approach — automated transcription with manual correction.
- ¶6: Research ethics — informed consent, anonymisation / company-naming decisions, data storage, Sikt / NSD status. State exactly what is documented; do not invent approval status.
  MUST EVIDENCE: research-ethics documentation (Sikt/NSD status)

**3.4 Data Analysis** (~1 page)

- ¶1: Thematic analysis — familiarisation, coding, theme generation, review, definition.
  MUST CITE: Braun & Clarke — thematic analysis
- ¶2: From themes to requirements — pain points translated into functional requirements via MoSCoW. Fit/gap analysis compared needs against existing systems.
- ¶3: Methodological constraints — rich but not generalisable; self-selection bias; single-day collection. Limitations of the analysis are catalogued in §5.4 (do not duplicate here).

**3.5 Iterative Development Process** (~5 pages, NEW/expanded per §8.4 Move 3)

Eight named iterations told as a connected narrative (tried → why → what happened → learned → next). Each iteration carries an inline origin label per §12.0.5 honesty rule.

Opening framing paragraph (~0.4 pages):
- Introduces the eight iterations as a narrative arc from substrate (§3.5.1) through algorithm depth (§3.5.2–§3.5.4) to operator surface (§3.5.5–§3.5.7) and per-company configurability (§3.5.8). Explains the tried / why / what-happened / learned / next pattern. Includes one sentence noting that iteration boundaries are reconstructed retrospectively from project artefacts and decision points; precise dates and ordering are approximate.
- Bridges to §3.6 — the iterations describe how the artefact was built; §3.6 describes how the artefact is tested.

Each iteration is a numbered sub-subsection (§3.5.1 through §3.5.8) of approximately 0.55 pages, structured as a six-bullet list with the **Origin** bullet first.

---

**3.5.1 Schema and Timeline Scaffolding**

- **Origin:** Admmit mandate (multi-tenant architecture) + designer-technical exploration (data model + read-only timeline UI)
- **Tried:** core entity model for employees, vehicles, assignments, certifications, work schedules, and time-off; multi-tenant data isolation enforced at the data layer; read-only Gantt-style timeline UI
- **Why:** later solver iterations need a structured substrate; the multi-tenant boundary must be enforced at the data layer per Admmit's customer structure
- **What happened:** substrate adequate for the simplest assignment heuristic but required revision when constraint-solver formalisation surfaced gaps in the data model (explicit time-off windows, certificate-expiry as queryable date)
- **Learned:** schema-first discipline reduces rework but cannot fully anticipate solver requirements; the substrate is itself an iteration, not a one-shot setup
- **Next:** with substrate stable, attempt the simplest possible assignment heuristic

**3.5.2 Single-engine Baseline (greedy)**

- **Origin:** designer-technical exploration
- **Tried:** priority-sorted greedy first-fit assignment heuristic
- **Why:** instant baseline producing a feasible plan; reference point for richer solvers; instant UI feedback for the coordinator
- **What happened:** works on small instances; on larger instances priority-sorted greedy commits early to locally optimal but globally suboptimal choices, blocking later assignments and producing avoidable idle time and overtime
- **Learned:** the greedy ceiling is structural, not a tuning issue — needs constraint propagation and a global view to break out
- **Next:** introduce a complete solver

**3.5.3 Constraint Generalisation (CP-SAT)**

- **Origin:** designer-technical exploration
- **Tried:** constraint-programming solver with explicit hard + weighted soft constraints + objective function
- **Why:** constraint programming is a known fit for assignment problems with complex interaction between hard and soft constraints
- **What happened:** near-optimal solutions on small to medium instances within a configurable time limit; quality degrades on larger instances when the time limit binds; modelling complexity higher than the heuristic
- **Learned:** CP-SAT covers the medium-instance gap but introduces a scaling boundary that motivates a third engine
- **Next:** a third engine for large instances + a way to compare the three

**3.5.4 Multi-engine Selection and Benchmarking**

- **Origin:** designer-technical exploration — operationalises the §12.0.5 "How-not-Of" methodologically independent test
- **Tried:** pluggable solver registry with three engines (heuristic, complete, metaheuristic); benchmarking framework with synthetic small / medium / large datasets; engine version snapshots for reproducibility
- **Why:** under realistic constraint combinations, which solver approach best meets Effektivitet? — a how-question independent of whether the visibility gap is real (interviews surface this) or whether HITL is necessary (Admmit mandate)
- **What happened:** subprocess plumbing complex; reproducibility issues required adding engine-version snapshots after early benchmark results were inconsistent
- **Learned:** the multi-engine architecture is a comparative test of *how*, not *whether* — Effektivitet measurement, not problem validation. This framing returns in §3.6, §4.5, and §5.1.1.
  MUST ANCHOR: Effektivitet
- **Next:** with computation infrastructure stable, build the human-in-the-loop surface

**3.5.5 HITL Surface (drag-and-drop timeline + override flow)**

- **Origin:** Admmit mandate (HITL principle from project start) + interview-driven (drag-drop UI specifically validated by interview-derived consensus on coordinator-led correction) — mixed
- **Tried:** Gantt-style drag-and-drop assignment UI; explicit accept / modify / reject on every algorithm-generated suggestion; thin post-hoc constraint check (basic feasibility only)
- **Why:** HITL was Admmit's requirement from project start; interviews validated the necessity through a consensus that the system should suggest a plan the coordinator can correct, not replace the coordinator
- **What happened:** drag-and-drop functional but state-consistency between optimistic UI updates and server mutations produced occasional stale conflict displays
- **Learned:** HITL surface needs richer real-time feedback than a thin post-hoc check; coordinator authority is meaningful only when the system surfaces what to act on
  MUST ANCHOR: Tillit/kontroll
- **Next:** expand the post-hoc check into a full deviation taxonomy

**3.5.6 Real-time Deviation Detection**

- **Origin:** designer / domain knowledge — extensions of pain points around tacit knowledge but specific deviation categories were not asked about in interviews (per §12.0.5 origin map)
- **Tried:** post-generation conflict scanner across multiple deviation categories (overbooking, overtime violations, missing competencies, expired certifications, rest-period violations, vehicle maintenance conflicts, night-work conflicts, unavailable-employee assignments); severity levels and status workflow; inline display on the planning timeline plus a dedicated deviations view
- **Why:** a meaningful HITL surface requires the system to surface *what* the coordinator should override toward — not just an empty timeline they edit blindly
- **What happened:** false positives where edge-case interactions between work-schedule and time-off produce noisy alerts (week boundaries, mid-shift absences); rest-period violations inherently noisy due to multiple regulatory definitions
- **Learned:** deviation detection materialises tacit knowledge as structured conflict data — but tuning thresholds is itself a coordination problem the system cannot fully resolve
- **Next:** with the planning surface and deviation feedback complete, expose the user-facing planning-time control

**3.5.7 User-controlled Plan-time vs Plan-quality Tradeoff**

- **Origin:** designer / Tillit/kontroll refinement — gives the coordinator agency over the planning *process*, not just over plan outcomes
- **Tried:** user-facing solver-time-budget control — coordinator selects either *fast / less accurate* (heuristic with short time limit) or *slower / more accurate* (constraint solver with longer time limit); the time-quality tradeoff is exposed as a deliberate choice rather than an internal default
- **Why:** different planning situations have different urgency-quality requirements (a sick-leave replanning under time pressure differs from next-week's planning); coordinator authority over plan generation is a Tillit/kontroll dimension distinct from plan-content override
- **What happened:** the choice surface itself raises the question of *what the user is choosing between* — bare time labels are not legible; descriptive labels ("fast suggestion" vs "best-effort plan") are clearer but smuggle in claims about quality the system cannot verify per-instance
- **Learned:** exposing a tradeoff requires explanation as interface (Miller framing) — the time control is itself a small case of explanation-driven HITL design
  MUST ANCHOR: Tillit/kontroll
- **Next:** bridge into per-company configurability of *planning rules* (the soft-constraint weight space)

**3.5.8 Configurable Soft-constraint Weights**

- **Origin:** designer / architectural — operationalises the Tilpasningsdyktighet anchor that the project committed to from the start (Admmit-mandated multi-tenant architecture); specific weight set chosen by designers, not interview-validated as the right set
- **Tried:** per-company weight configuration UI for soft constraints (workload balance, vehicle preference, transitions between consecutive assignments, priority, employee preferences); weights flow into the solver objective function
- **Why:** interviews confirmed assignment criteria differ materially across companies — Tilpasningsdyktighet means the same artefact must serve materially different operational rules
- **What happened:** hard to validate that user-chosen weight combinations don't produce degenerate solutions; UX challenge of explaining what each weight means to a coordinator without optimization vocabulary
- **Learned:** configurability for soft weights is a partial Tilpasningsdyktighet realisation — broader configurability (hard constraints, status workflow) is acknowledged as L4-adjacent and remains future work (cross-references §6.3 + §5.4 L4)
  MUST ANCHOR: Tilpasningsdyktighet
- **Next:** with eight iterations of artefact in place, the methodological question is *how* to test whether it meets the locked anchors — bridges into §3.6

---

**3.6 Evaluation Framework** (~1.5 pages, NEW per §12.0.5)

Separated from validity / reliability — describes *how* the artefact is tested, distinct from the research's epistemic limits.

- ¶1: Frame the evaluation explicitly as a "How-not-Of" test per §12.0.5. The multi-engine benchmark tests *how* solver approaches compare under realistic constraint combinations; it does not test whether the visibility gap is real (interviews surface this) or whether HITL is necessary (Admmit mandate).
  MUST EVIDENCE: §12.0.5 Findings stance — How-not-Of framing
- ¶2: Anchor-to-method mapping. Multi-engine benchmark → Effektivitet (the anchor it tests). Requirements traceability matrix → all three anchors (the artefact embodies them, traceability checks coverage). User testing → Tillit/kontroll (would test, but not done — forwarded to §5.4 L8).
  MUST ANCHOR: Effektivitet, Tillit/kontroll, Tilpasningsdyktighet
- ¶3: Synthetic dataset design — small, medium, and large instances with what each tests for. Why synthetic rather than production data (forwarded to §5.4 L5).
  MUST EVIDENCE: synthetic dataset design rationale
- ¶4: Requirements traceability matrix as coverage check — implementation status and test status per requirement.
  MUST EVIDENCE: requirements traceability matrix (implementation + test status per requirement)
- ¶5: What the evaluation does NOT test — production deployment, user-tested override flow, comparison against existing TMS. Each forwarded to a specific §5.4 limitation.

**3.7 Validity and Reliability** (~1 page, trimmed)

- ¶1: Malterud's three criteria — relevance, validity, reflexivity. (NB: source extraction 2026-05-01 confirmed the paper presents exactly three standards, not four. "Systematic critical reflection" does not appear as a standalone criterion in Malterud 2001.)
  MUST CITE: Malterud — qualitative validity (three criteria: relevance, validity, reflexivity)
- ¶2: Interview validity — purposive sample, triangulation across interviews, generalisation limits.
- ¶3: System validity — requirements traceability + algorithm benchmarking. Validation per Wieringa (cited in §3.2 — do not re-cite).
- ¶4: Researcher bias — dev team = research team; author affiliation with Admmit. Forwarded to §5.4 L3.

---

## Chapter 4 — Findings
**Owner:** Both | **Target:** ~12.5 pages | **Status:** Not started

**Purpose:** Present what was found and what was built — without interpretation.

> **Rule:** Present findings and system artefacts only. Do not interpret implications; interpretation belongs in Chapter 5.

### Sections and content

**4.1 Interview Findings** (~4 pages) — *Mikael*

- ¶1: Current planning processes — manual at varying scale and complexity across the seven interviewed companies.
  MUST EVIDENCE: interview-derived theme on manual planning practice
- ¶2: **Resource-utilization visibility gap** named as the primary surprising theme. Operator-vs-owner asymmetry as a secondary surprising finding. Both are central to the discussion in §5.1.1.
  MUST EVIDENCE: interview-derived theme on resource-utilization visibility gap
  MUST EVIDENCE: interview-derived evidence for operator-vs-owner asymmetry
- ¶3: Pain points — slow legacy software, tacit-knowledge dependency, no capacity overview. Ranked by frequency across interviews, not listed equally.
  MUST EVIDENCE: interview-derived themes on pain points (frequency-ranked)
- ¶4: Sick-leave handling — varies materially across companies from trivial to daily burden.
  MUST EVIDENCE: interview-derived theme on sick-leave handling variation
- ¶5: Attitudes toward automation — split between sceptical and positive, with a consensus that the system should suggest a plan the coordinator can correct, not replace the coordinator.
  MUST EVIDENCE: interview-derived theme on automation attitudes
- ¶6: Assignment criteria — frequency-ranked list across the seven companies (availability / position, experience, driving / rest time, competence / licence, route familiarity, equipment match, overtime status).
  MUST EVIDENCE: interview-derived assignment-criteria ranking

**4.2 Requirements** (~2 pages) — *Mikael*

- ¶1: Functional requirements derived from interviews. Each requirement carries a MoSCoW priority and an interview source.
  MUST EVIDENCE: functional requirements with MoSCoW priority and interview source per requirement
- ¶2: Non-functional requirements with target metrics.
  MUST EVIDENCE: non-functional requirements with target metrics

**4.3 Fit/Gap Analysis** (~1.5 pages) — *Mikael*

- ¶1: What existing systems provide vs. what coordinators need. Fit table.
  MUST EVIDENCE: fit-items from fit/gap analysis
- ¶2: Gap table; **Timpex- and Opter-vendor specifics absorbed here** (Timpex's slow performance under concurrent use; what each system does well — order management, invoicing, driver notification — and what neither does — automatic plan generation, planning support, decision support). Timpex and Opter are named as real Norwegian TMS; other interviewed companies use internal/custom systems described generically.
  MUST EVIDENCE: gap-items from fit/gap analysis; Timpex- and Opter-specific factual context

**4.4 System Description** (~3 pages) — *Embret*

- ¶1: Architecture overview — component decomposition, responsibilities, communication paths.
  MUST EVIDENCE: architecture documentation (component decomposition + responsibilities + communication)
- ¶2: Key features — plan view, manual override (drag-and-drop + accept/modify/reject), driver/vehicle management, multi-tenant isolation.
  MUST EVIDENCE: feature inventory matched to in-scope list
- ¶3: UI flow — what the coordinator sees and can do, including the time-quality control surface from §3.5.7.
  MUST EVIDENCE: UI walkthrough documentation
- ¶4: Technology stack with brief justification per layer.
  MUST EVIDENCE: technology stack documentation with justifications per layer

**4.5 Optimisation Algorithm** (~3.5 pages) — *Embret*

- ¶1 (NEW opener — How-not-Of framing): the multi-engine architecture is a methodologically independent test of *how* the constraint problem is best solved, not *whether* the artefact's claims about utilization are real. (Echoes §3.5.4 Learned, §3.6 ¶1, and §5.1.1 ¶4.)
  MUST ANCHOR: Effektivitet (preload via §4.5 → §5.1.1)
- ¶2: Problem formulation — input, output, decision variables.
  MUST EVIDENCE: problem formulation (input/output, constraint set, objective function)
- ¶3: Chosen approaches and justification — heuristic for instant baseline, complete solver for medium instances, metaheuristic for large instances.
  MUST EVIDENCE: solver selection rationale
  MUST CITE: solver-engine references (constraint programming, metaheuristic)
- ¶4: Hard and soft constraints modelled.
- ¶5: Objective function and weighting.
- ¶6: Known limitations of the algorithm (forwarded to §5.4 L9).
- ¶7: Benchmarking results — dataset sizes, runtime, scheduled percentage, violation counts, score comparison across engines. State explicitly if any solver was implemented but not fully benchmarked.
  MUST EVIDENCE: benchmark results per solver per dataset size

**4.6 DSR Artifacts Mapping** (~0.5 pages, NEW per §8.4 + §3.5 reference) — *Both*

A single-page table making the abstract DSRM theory of §3.2 concrete and verifiable.

- ¶1: One framing paragraph noting that the table maps each project artefact to its DSR category, and that this mapping is the concrete instantiation of the DSRM Applied bullets in §3.2.
- A table with four columns: **Construct** (anchor concepts; deviation taxonomy; soft-constraint weight schema), **Model** (data model with entity relations and multi-tenant boundary; constraint formulation), **Method** (multi-engine selection process; benchmarking framework; HITL override flow; time/quality control surface), **Instantiation** (Ressursplanlegger as deployed application).
  MUST EVIDENCE: artefact inventory categorised per DSR Construct/Model/Method/Instantiation

**4.7 Process Documentation** (~1 page, NEW, in body per locked decision) — *Both*

ChatSSB pattern (their §5.3 Administrative Results) — kept in body, not appendix, because NTNU bachelor expectations include explicit process documentation.

- §4.7.1 Sprint summary — milestones and timeline.
  MUST EVIDENCE: sprint log summary (milestones + timeline)
- §4.7.2 Key decisions — concise list with rationale, naming the decisions referenced by the §3.5 iteration narrative.
  MUST EVIDENCE: decision log (key technical and methodological decisions)
- §4.7.3 Time tracking — hours per author per task category.
  MUST EVIDENCE: time-tracking summary (hours per author per task category)

> **Note:** The SKILL.md readiness gate blocks §4.7 from being written until the process-documentation evidence is filled. This section preserves the structural slot.

---

## Chapter 5 — Discussion
**Owner:** Mikael | **Target:** ~11 pages, restructured | **Status:** Not started

**Purpose:** Interpret findings in light of theory and research questions. Organise primary findings under the three locked anchor concepts. Name limitations honestly and analyse their impact.

### Sections and content

**5.1 Primary Findings under the Anchors** (~5–6 pages, the new core)

§5.1 opens with a brief opener paragraph: "the discussion organises primary findings under the three locked anchor concepts (Effektivitet, Tillit/kontroll, Tilpasningsdyktighet) — one sub-section per anchor, names used verbatim throughout".

**5.1.1 Effektivitet** (~2 pages)

- ¶1: Visibility-gap finding as the primary surprising result. Reference the named theme in §4.1.
  MUST ANCHOR: Effektivitet
  MUST EVIDENCE: visibility-gap interview theme
- ¶2: **Operator-vs-owner asymmetry framed here** (Bainbridge) — the asymmetry IS what makes the visibility gap a finding worth surfacing. Owners and Admmit demand utilization optimization; coordinators do not articulate this need themselves. This is the configuration Bainbridge's *ironies of automation* anticipates.
  MUST CITE: Bainbridge — operator-vs-owner asymmetry
- ¶3: Three utilization dimensions (overtime, idle time between assignments, uneven driver load) — what the artefact makes visible. The visibility itself is the precondition for optimization.
- ¶4: Multi-engine benchmark as the methodologically independent How-not-Of test. Tie back to §3.6 framing — the benchmark tests *how* solver approaches compare, not whether the visibility gap is real.

**5.1.2 Tillit/kontroll** (~2 pages)

- ¶1: Three-layer HITL theory applied to override authority. Bainbridge frames the coordinator's authority over override — operator authority is the resolution to the operator-vs-owner asymmetry that motivated automation in the first place. Parasuraman situates the artefact at automation level 5–6 — system suggests, human approves — the level at which override is the constitutive interaction.
  MUST ANCHOR: Tillit/kontroll
  MUST CITE: Bainbridge — operator authority over override
  MUST CITE: Parasuraman — automation taxonomy (level 5–6 framing for HITL override)
- ¶2: Hoff & Bashir's dimensional model of trust antecedents — how trust forms over use; calibration mechanics in this artefact; why both over- and under-reliance are design failures. Layered onto Lee's foundational trust-reliance model — Hoff & Bashir refines, does not replace.
  MUST CITE: Hoff & Bashir — trust calibration
  MUST CITE: Lee — trust in automation (foundational; Hoff & Bashir is refinement)
- ¶3: Miller — explanation/transparency as design requirement. How the system surfaces algorithm reasoning (deviation alerts, scoring breakdown, the time-quality control from §3.5.7 as a small case of explanation-driven design). Amershi's Human-AI guidelines complement Miller's social-science framing with practical design heuristics.
  MUST CITE: Miller — explanation as interface
  MUST CITE: Amershi — Human-AI interaction guidelines (practical complement to Miller)
- ¶4: Tacit knowledge as the operator's irreducible role. Coordinator inspect / modify / accept / reject operationalises Tillit/kontroll concretely — vague control language is forbidden by the spine. Tacit knowledge used here as a domain concept (operational knowledge held by the coordinator beyond what the system can capture); no separate theoretical anchor required.

**5.1.3 Tilpasningsdyktighet** (~1.5 pages)

- ¶1: Cost / benefit thresholds across the seven interviewed companies — different fleet sizes, different operational rules, different willingness-to-pay.
  MUST ANCHOR: Tilpasningsdyktighet
  MUST CITE: Venkatesh — UTAUT (technology adoption thresholds across organisational contexts)
- ¶2: Fit / gap variation — different companies' assignment-criteria rankings produce different soft-constraint weight profiles.
- ¶3: Configurable soft-constraint weights as the technical mechanism (§3.5.8 result). Honest about what is *not* configurable yet — hard constraints, status workflow definitions, and per-company assignment-rule taxonomies. These are L4-adjacent and forwarded to §6.3 future work.
  MUST CITE: Mietzner — multi-tenant SaaS variability (configurability mechanism)
- ¶4: Distinct from skalerbarhet (which concerns volume). Tilpasningsdyktighet is about meaningfulness across material rule differences, not throughput.

---

**5.2 Adoption and Deployment Implications** (~1 page, **trimmed from 1.5p**)

Surviving fragment of the prior topical 5.3, repositioned as *implications* of the discussion rather than as findings.

- ¶1: Cost / benefit threshold for adoption — what the artefact must demonstrate before companies adopt.
  MUST CITE: Venkatesh — UTAUT (cost-benefit threshold framing for adoption)
- ¶2: Timpex / Opter / legacy integration gap; billing-system integration as a future requirement identified by interviewees but out of scope.
  MUST EVIDENCE: TMS-as-category framing from §2.3 reappearing here
- ¶3: Deployment-readiness — what would it take to move from validation (this thesis) to production? Forwarded to §6.3.

**5.3 Sustainability and Ethical Considerations** (~1.5 pages)

- ¶1: Introduce SusAF as the structuring framework. Five sustainability dimensions.
  MUST CITE: SusAF / sustainability awareness framework
  MUST EVIDENCE: sustainability analysis documentation
- ¶2: Sustainability effects table — benefits and harms per dimension.
- ¶3: Key dilemmas — fairness (algorithmic bias against drivers), accountability (who is responsible for an algorithm-generated assignment that goes wrong), privacy (employee data handling), working conditions (does optimization tighten driver workload?). Where a dilemma ties to a specific anchor (accountability ↔ Tillit/kontroll; working conditions ↔ Effektivitet), name the anchor verbatim.
  MUST CITE: Mittelstadt — ethics of algorithms (fairness / privacy taxonomy)
  MUST CITE: Martin — algorithmic accountability (accountability dilemma)
  MUST CITE: Lee MK — algorithmic management and worker fairness (working-conditions dilemma)
- ¶4: Map effects to the SDG framework.
  MUST CITE: un2015agenda2030
- ¶5: Ethical considerations as substantive design issues — the operator-vs-owner asymmetry is itself an ethics question (whose efficiency, whose autonomy?).
- ¶6: Limitations of the sustainability analysis — analytical, not empirical.

**5.4 Limitations** (~2.5 pages, hierarchical)

§5.4 opens with two locked elements:

1. A one-sentence note: "L1–L12 names are locked verbatim from `evaluation/reference-thesis-analysis.md` §12.0.7; synonyms (e.g., 'smaller sample' for 'L1 — Sample size (7 interviews)') drift the spine and must be flagged by reviewers."
2. The L#-to-SQ mapping block:

```
SQ1 → §5.1.1 (Effektivitet) — bounded by L1, L2, L3, L4
SQ2 → §5.1.2 (Tillit/kontroll) — bounded by L8, L10
SQ3 → §5.1.3 (Tilpasningsdyktighet) + cross-anchor — bounded by L5, L6, L7, L9, L11, L12
```

Three sub-subsections, each L# rendered as a `\paragraph{Lk — Name}` (named paragraph; no TOC bloat). Each L# paragraph names the limitation, describes what it prevents the thesis from claiming, and analyses impact on conclusions.

**5.4.1 Empirical Foundation**

- L1 — Sample size (7 interviews)
- L2 — Self-selection bias in interview sample (Admmit customers only)
- L3 — Author affiliation with Admmit
- L4 — Interview-guide coverage gap

**5.4.2 Validation and Artefact**

- L5 — Synthetic benchmarks, not production data
- L6 — No real-world deployment
- L7 — No empirical comparison against existing TMS
- L8 — No user testing with coordinators
- L9 — Algorithm evaluation against own benchmarks only

**5.4.3 Conceptual and Methodological**

- L10 — HITL as mandate, not validated level
- L11 — Single-domain (Norwegian transport)
- L12 — Boundary cases described, not quantified

**5.5 Deviations from Plan** (~0.5 pages, NEW per §8.4)

Explicit acknowledgement of where the project's actual path diverged from initial design.

- ¶1: Plan-vs-reality differences — what changed and why.
- ¶2: Why each deviation occurred and what it changed about the contribution.

**5.6 Methodology Reflection** (~0.5 pages, NEW per §8.4 + §11.6)

Single substantive paragraph naming the actual weak spot in the method — per §11.6, "find the actual weak spot in your method and name it". The writer must pick whichever weak spot is most load-bearing for the thesis (recommendation: synthetic-benchmark validation, since this is the central evaluation method for the artefact's primary anchor Effektivitet — but small interview sample, dev-team = research-team, or single-domain are also defensible choices).

---

## Chapter 6 — Conclusion
**Owner:** Both | **Target:** ~3 pages | **Status:** Not started

**Purpose:** Summarise, answer each sub-question explicitly, suggest future work tied to specific limitations, and close on a domain-level claim.

### Sections and content

**6.1 Summary** (~0.5 pages)

- ¶1: Summarise the problem and motivation from Chapter 1 in 2–3 sentences.
  MUST TRACE: Chapter 1 thesis-spine.md sentence
- ¶2: Summarise the theoretical foundation from Chapter 2 and the methodological approach from Chapter 3.
  MUST TRACE: Chapter 2 and Chapter 3 thesis-spine.md sentences
- ¶3: Summarise the findings, artefact, and discussion from Chapters 4 and 5, ending with the thesis's central qualification — the system supports but does not replace coordinator judgement, and the argument applies under stakeholder asymmetry not in low-variation fleets.
  MUST TRACE: Chapter 4 and Chapter 5 thesis-spine.md sentences

**6.2 Answers to Research Questions** (~1 page)

> **Block-quote pattern instruction (locked):** Each sub-question MUST be reproduced verbatim as a block quote (LaTeX `\begin{quote}...\end{quote}`, or `\begin{displayquote}` if the thesis loads `csquotes`), then answered in one discrete paragraph with no new material. Three SQs → three answer paragraphs, each tied to the anchor it serves.

- ¶1: Restate the main RQ verbatim as a block quote and answer it directly with a qualified statement grounded in findings + discussion. Cross-anchor.
  MUST TRACE: §5.1.1 (Effektivitet), §5.1.2 (Tillit/kontroll), §5.1.3 (Tilpasningsdyktighet)
- ¶2: SQ1 verbatim block quote, then one-paragraph answer.
  MUST TRACE: §5.1.1 (Effektivitet)
- ¶3: SQ2 verbatim block quote, then one-paragraph answer.
  MUST TRACE: §5.1.2 (Tillit/kontroll)
- ¶4: SQ3 verbatim block quote, then one-paragraph answer.
  MUST TRACE: §5.1.3 (Tilpasningsdyktighet) + cross-anchor (Effektivitet, Tillit/kontroll)
- ¶5: Contribution statement — the artefact, the requirements / findings synthesis, and the validation-based knowledge about algorithm-assisted planning under stakeholder asymmetry in this domain.

**6.3 Future Work** (~1 page)

Each item must cite a specific named limitation from §5.4. Generic items ("further research could investigate…") are red flags.

- ¶1: Driver mobile app — addresses interview-derived feature requests + L8 (no user testing on coordinator-driven flows).
  MUST TRACE: §5.4 L8
- ¶2: Billing / invoicing integration — addresses fit/gap billing gap + adoption barrier from §5.2.
  MUST TRACE: §5.2 adoption barriers
- ¶3: Production pilot with a real transport company — addresses L5 (synthetic benchmarks) + L6 (no deployment).
  MUST TRACE: §5.4 L5, L6
- ¶4: Real-time replanning for sick-leave events — addresses interview Theme on sick-leave handling + algorithmic limitations.
  MUST TRACE: §5.4 L9
- ¶5: Algorithm scaling improvements — addresses the constraint-solver scaling boundary from §3.5.3.
  MUST TRACE: §5.4 L9
- ¶6: Broader Tilpasningsdyktighet — hard-constraint and status-workflow configurability — addresses §3.5.8 partial realisation + L4 interview-guide coverage gap.
  MUST TRACE: §5.4 L4
- ¶7: Cross-domain replication — addresses L11 single-domain.
  MUST TRACE: §5.4 L11
- ¶8: Closing sentence — a domain-level claim about algorithm-assisted planning under stakeholder asymmetry in Norwegian transport (per a-grade-rubric.md Ch 6 closing-domain-claim marker), not just about the artefact.
  MUST TRACE: thesis-spine.md Chapter 6 sentence

---

## Theory→Use Cross-Reference

Verification helper for the §7 reviewer marker "every theory point reappears in analysis". Each Ch 2 concept must have at least one downstream reappearance. A concept with no reappearance is an **orphaned-theory flag** that must be fixed (or, where the orphan is intentional — e.g., a delimit-only reference — explicitly marked as such).

| Theory concept (Ch 2) | First reappearance | Subsequent |
|---|---|---|
| Resource scheduling — utilization framing (§2.1) | §5.1.1 Effektivitet | §6.2 SQ1 |
| HITL — Parasuraman taxonomy (§2.2 ¶1) | §5.1.2 ¶1 | — |
| HITL — Bainbridge operator-vs-owner (§2.2 ¶2) | §5.1.1 (asymmetry) | §5.1.2 ¶1, §6.2 SQ1+SQ2 |
| HITL — Hoff & Bashir trust calibration (§2.2 ¶3) | §5.1.2 ¶2 | §6.2 SQ2 |
| HITL — Miller explanation (§2.2 ¶4) | §5.1.2 ¶3 | §6.2 SQ2 |
| HITL — Lee trust foundation (§2.2 ¶5) | §5.1.2 ¶2 | — |
| TMS as software category (§2.3) | §4.3 Fit/Gap | §5.2 Adoption |
| DSR + DSRM (§2.4) | §3.2 DSRM Applied | §3.6 Evaluation |
| Wieringa validation vs evaluation (§2.4 ¶3) | §3.6 ¶1 | §3.7, §5.4 L5 |
| VRP delimit (§2.1 ¶4) | — (only delimit) | — |

VRP is a deliberate orphan because it is referenced *only to delimit* — Ressursplanlegger is an assignment problem, not a sequencing problem. The orphan-status is intentional and must be flagged as such, not as a coverage gap.

The outline-writing process generates and verifies this table; the red-thread reviewer checks it during chapter integration. Every theory concept added to Ch 2 in future revisions must either gain a reappearance entry or be explicitly marked as a deliberate delimit-only orphan.
