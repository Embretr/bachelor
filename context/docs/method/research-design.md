# Research Design — Ressursplanlegger

> Source-of-truth for Chapter 3 (Methodology). The thesis text elaborates on these points with proper citations from `result/references.bib`. Updated 2026-05-01 to reflect the post-audit bib (41 entries), new outline structure (8 named iterations, anchor-organised Ch 5, How-not-Of evaluation framing), and honest framing of the brief stakeholder consultations.

---

## Chosen Method

**Method:** Design Science Research (DSR), applied through Peffers' six-activity DSRM.

**Definition:** DSR is a research paradigm in which the researcher creates and evaluates an artefact — a system, model, or method — to address an identified problem. The research contribution lies in both the artefact itself and the knowledge generated through designing and evaluating it.

**Key references (in `result/references.bib`):**

- `hevner2004design` — foundational DSR paper (seven guidelines, rigor/relevance frame)
- `hevner2007threecycle` — the three-cycle view (relevance, design, rigor)
- `peffers2007dsrm` — six-activity DSR process model
- `wieringa2014dsm` — design-cycle / empirical-cycle distinction; validation vs evaluation

**IS research-paradigm anchor:** `orlikowski1991studying` — positivist / interpretive / critical paradigm taxonomy. Used in §2.4 ¶2 + §3.2 ¶1 to justify why DSR fits this artefact-plus-knowledge structure better than positivist or interpretivist alternatives alone.

---

## Justification

**Why DSR fits this project.** The thesis combines (a) investigating a real-world problem through stakeholder consultation and (b) building a software system to address that problem. DSR explicitly accounts for artefact creation as a research outcome and structures the process around iterating between problem understanding and solution design. The validation of the artefact against requirements derived from interviews produces generalisable knowledge about algorithm-assisted resource planning under stakeholder asymmetry in Norwegian transport.

**Why not interpretivist case study alone.** A case study would document the problem and context but exclude the design and construction of a solution. Since the primary contribution is a working system with a multi-engine optimisation algorithm, a method that explicitly accounts for artefact creation is needed (Orlikowski & Baroudi 1991 covers this paradigm distinction).

**Why not purely positivist quantitative.** The research question requires understanding how traffic coordinators work, what they need, and how they respond to algorithm-assisted workflow. These are substantive questions that quantitative measurement alone cannot answer. The quantitative elements (synthetic-dataset benchmarks, solution scores) are embedded within the broader DSR framework.

---

## How DSRM Is Applied (per project)

The DSR process follows Peffers et al. (2007) six activities, applied to *this* project rather than discussed in the abstract. Each row maps an activity to project-specific content + the anchor it serves (Effektivitet / Tillit/kontroll / Tilpasningsdyktighet).

| DSRM Activity | What was done | Anchor |
|---|---|---|
| **1. Problem Identification and Motivation** | Brief semi-structured interviews (~15 min each) with seven traffic coordinators surfaced the *resource-utilization visibility gap* and the *operator-vs-owner asymmetry*. Admmit's bachelor task brief established the HITL principle and multi-tenant scope from the start. | Effektivitet (gap) + Tillit/kontroll (HITL mandate) |
| **2. Objectives of a Solution** | Locked anchor concepts as the operational objectives — Effektivitet (overtime, idle time, load balance), Tillit/kontroll (inspect / modify / accept / reject — the four operator actions on every algorithm-generated assignment), Tilpasningsdyktighet (cross-company adaptability via configurable weights and rules). Functional + non-functional requirements derived through MoSCoW + interview-source traceability. | All three |
| **3. Design and Development** | Eight named iterations (§3.5.1 – §3.5.8) — schema scaffolding → greedy baseline → CP-SAT generalisation → multi-engine selection → HITL drag-and-drop surface → real-time deviation taxonomy → user-controlled time/quality tradeoff → per-company configurable soft-constraint weights. Documented in `sprint-log.md` with origin labels per §12.0.5 (Admmit-mandate / interview-validated / designer / mixed). | All three (different iterations preload different anchors) |
| **4. Demonstration** | Working system demonstrated to Admmit (oppdragsgiver) and to the NTNU supervisor. Demonstration to traffic coordinators was *not* conducted — see §5.5 Deviations / §5.4 L8. | — |
| **5. Evaluation** | Framed as a methodologically independent **"How-not-Of"** test (§3.6, §12.0.5) — the multi-engine benchmark on synthetic small/medium/large datasets tests *how* solver approaches compare under realistic constraint combinations, not *whether* the visibility gap is real (interviews surface this) or *whether* HITL is necessary (Admmit mandate). Requirements traceability matrix as the coverage check. Validation, not field evaluation (Wieringa 2014). | Effektivitet (primary) |
| **6. Communication** | This thesis + recommendations to Admmit on deployment and configurability. | All three |

---

## Data Collection Methods

### Brief stakeholder consultations (interviews)

- **Purpose:** Understand current planning practices, pain points, and attitudes toward automation. Surface themes — not statistically generalise.
- **Participants:** Seven traffic coordinators / transport managers from Norwegian transport companies of varying size and system maturity, contacted directly on the team's own initiative (Admmit did not broker introductions).
- **Date:** Single day, March 2026.
- **Format:** Phone calls, recorded.
- **Duration:** Approximately 15 minutes per call. Total cumulative interview time: roughly 105 minutes across the seven companies.
- **Transcription:** Automated transcription with manual review and correction of segments used for analysis.
- **Interview guide structure:** Five themes — current tools/workflow, assignment criteria, sick-leave handling, automation attitudes, adoption criteria. Open questions within each theme.
- **Honest framing:** Brief duration (~15 min) means the interviews surfaced themes but cannot support deep methodological claims. The framing is *exploratory stakeholder consultation as DSRM Step 1 input*, not full Kvale-style interview craft.

### Thematic analysis (Braun & Clarke 2006)

- **Purpose:** Identify recurring themes across the seven consultations to inform requirements (DSRM Step 2 input).
- **Method:** Transcripts were analysed thematically — familiarisation, coding, theme generation, theme review. Despite Braun & Clarke's paper being published in *Qualitative Research in Psychology*, the method is domain-agnostic and is the canonical reference for thematic analysis across IS, HCI, education, and healthcare research.
- **Scope honesty:** With ~105 min total audio and seven informants, the analysis is pragmatic theme identification rather than full reflexive thematic analysis. This is appropriate for DSRM Step 1 evidence; flagged as L1 in §5.4.
- **Output:** `context/interviews-summary.md` — distilled findings organised by theme.

### Fit/gap analysis

- **Purpose:** Compare what existing systems provide against what coordinators need (DSRM Step 2 input).
- **Input:** Interview findings + factual context on Timpex and Opter (the two commercial Norwegian TMS named in the consultation pool). Other interviewed companies use internal/custom tools described generically — their specific identities are not relevant to the thesis argument.
- **Output:** `context/fitgap-summary.md` — fit table and gap table.

---

## Research Ethics — honest framing

> The project was conducted as an industry consultation under Admmit's brief and NTNU supervision rather than as formal research with Sikt/NSD registration. The framing below is honest about what was and was not done; this is a defensible bachelor-scope position when stated transparently.

- **Sikt/NSD status:** No formal Sikt/NSD registration was made. The project was treated as industry consultation under Admmit's bachelor task brief and NTNU institutional supervision. No special-category personal data per GDPR was collected — conversations covered work practices, system use, and assignment criteria only.
- **Informed consent:** Consent was implicit through participants agreeing to take the call and answer questions. No formal consent form was administered. Recording was conducted without an explicit consent step before recording began. *This is an honest limitation; flagged in §5.4 L3 (researcher–developer overlap and informal study procedures).*
- **Anonymisation:** No formal anonymisation protocol was applied. Only Timpex and Opter (vendors, not customers) are named as real Norwegian TMS in the thesis. The seven interviewed companies are referenced generically (size, sector, system maturity) without naming.
- **Data storage:** Recordings and transcriptions are stored locally on the project author's device. Access is limited to the project author and supervisor. All recordings and transcriptions will be deleted after thesis submission and grading.
---

## System Development Approach

- **Methodology:** Iterative DSR development across eight named iterations (§3.5.1 – §3.5.8). Iteration boundaries are conceptual — each iteration ends when its substrate stabilises enough to motivate the next.
- **Division of work:** Embret — system development and algorithm implementation. Mikael — user research, requirements, fit/gap analysis, and thesis writing. Both contribute to discussion and analysis.
- **Tooling:** GitHub for version control and issue tracking. No separate project-management tool.
- **Source documents:**
  - `context/docs/project/sprint-log.md` — eight iteration narratives (Origin / Tried / Why / What happened / Learned / Next).
  - `context/docs/project/decision-log.md` — twelve numbered key decisions (D1–D12).
  - `context/docs/project/change-log.md` — confirmed deviations from plan (sick-leave replanning, user testing).

---

## Validation vs Evaluation (Wieringa 2014)

The distinction is critical for how the thesis frames its results:

- **Field evaluation:** Investigating the artefact as applied by real stakeholders in production — i.e., deployed in a real transport company with coordinators using it daily. *Not possible* within the thesis timeframe.
- **Validation:** Predicting how the artefact will interact with its context *without* observing it in real-world deployment — through synthetic-dataset benchmarking, requirements traceability, and design walkthroughs. *This is what the thesis does.*

**Implication for writing:** Chapter 5 is framed as validation. Use language like "the validation suggests…" / "based on the benchmarks, the algorithm is expected to…" — never claim real-world impact that has not been measured. Acknowledge explicitly that field evaluation would require production deployment and is forwarded to §6.3 future work + §5.4 L5–L7.

---

## Validity and Reliability (§3.7)

Malterud's (2001) three standards for qualitative research validity — *relevance*, *validity*, *reflexivity* — adapted to the DSR context. (Note: earlier drafts of this file referenced "four criteria" by conflating "systematic critical reflection" as a separate standard; the source extraction confirmed Malterud 2001 presents exactly three.)

| Standard | Application in this project |
|---|---|
| **Relevance** | The consultations surfaced themes (visibility gap, operator-vs-owner asymmetry) that map directly to the artefact's locked anchors and to validation outcomes — relevance to the research question is traceable. Systematic critical reflection on what each iteration produced is documented across §3.5 (each "Learned" bullet) and §5.6 (Methodology Reflection). |
| **Validity** | Bounded by L1 (n=7 brief consultations), L2 (Admmit-customer self-selection bias), L3 (researcher = developer = consultation operator), L4 (interview-guide coverage gap). Each L# is named in §5.4. |
| **Reflexivity** | The §12.0.5 origin map distinguishes Admmit-mandated from interview-validated from designer-driven decisions, making the team's role in shaping the artefact transparent. |

System validity is bounded additionally by requirements traceability + algorithm benchmarking (validation per Wieringa 2014).

---

## Limitations of This Method (preview of §5.4)

The full L1–L12 list with hierarchical groupings lives in `evaluation/reference-thesis-analysis.md` §12.0.7 and is rendered in §5.4 (Limitations). Preview, organised by group:

**Empirical Foundation (L1–L4):**

- **L1 — Sample size and brief duration:** Seven brief stakeholder consultations (~15 min each) provide rich theme-surfacing but cannot claim statistical generalisability.
- **L2 — Self-selection bias:** All seven companies are Admmit customers; non-customer perspectives absent.
- **L3 — Researcher–developer overlap and informal study procedures:** The development team is the research team; consent and anonymisation procedures were informal rather than formal.
- **L4 — Interview-guide coverage gap:** Specific deviation categories (rest-period definitions, vehicle-maintenance conflicts) not asked about; deviation taxonomy is designer/domain-knowledge, not interview-validated.

**Validation and Artefact (L5–L9):**

- **L5 — Synthetic benchmarks, not production data**
- **L6 — No real-world deployment**
- **L7 — No empirical comparison against existing TMS**
- **L8 — No user testing with coordinators** (anchored to §5.5 deviation D12)
- **L9 — Algorithm evaluation against own benchmarks only**

**Conceptual and Methodological (L10–L12):**

- **L10 — HITL as Admmit mandate, not validated level**
- **L11 — Single domain (Norwegian transport)**
- **L12 — Boundary cases described, not quantified**

---

## Deviations from Plan (preview of §5.5)

Two confirmed deviations from the original project plan, both due to time constraints. Full narratives in `context/docs/project/change-log.md`:

- **D11 — Real-time sick-leave replanning dropped.** Originally planned partial-resolve replanning; dropped for time. Forwarded to §6.3.
- **D12 — User testing with traffic coordinators dropped.** Originally planned three-coordinator walkthroughs; dropped for time. Anchors §5.4 L8.