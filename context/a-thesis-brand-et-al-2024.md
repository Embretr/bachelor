---
name: Benchmark A-thesis — Brand, Gran & Gudvangen (2024)
description: NTNU bachelor thesis on ML-based 5G underperformance prediction with SimulaMet as industry partner; DSR with Hevner three-cycle, honest mid-project pivot, separate Societal Impact chapter
type: reference
---

# Benchmark A-Thesis — Brand, Gran & Gudvangen (2024)

**Authors:** Nicolai Hollup Brand, Callum Gran, Trym Hamer Gudvangen
**Title:** Predicting Underperformance In 5G Cellular Networks Using Supervised Machine Learning Based on End-User Data
**Institution:** NTNU, Department of Computer Science
**Supervisor:** Olav Alseth Skundberg (NOT Ali Alsam — outside our supervisor's pool)
**Co-supervisor:** Azza Hassan Mohamed Ahmed (SimulaMet)
**Submitted:** May 2024
**Industry partner:** Simula Metropolitan Center for Digital Engineering AS (SimulaMet)
**Length:** 151 pages

---

## Why this file is here

Third benchmark thesis, kept alongside `a-thesis-amundsen-remoy-2025.md` (prose voice) and `a-thesis-trana-jorgensen-2025.md` (DSR structure). **Not a citation source** for our thesis (different topic, different supervisor pool). Loaded for structural and stylistic comparison.

This thesis differs from the other two benchmarks in important ways:

- Different supervisor (Skundberg, not Alsam) — A-grade prose discipline transferable across pools
- Industry partner is a research institution (SimulaMet) rather than a commercial firm
- ML-experimental thesis rather than software-system thesis: results are F1-scores and confusion matrices, not artefact features
- DSR framed through Hevner's three-cycle model rather than Peffers' six DSRM activities — a precedent for picking a DSR variant that fits the project rather than defaulting to Peffers
- Mid-project pivot from fault diagnosis to underperformance prediction, acknowledged openly in the front matter and again in §5.6.3 (Setbacks)

Use this file when comparing pivot framing, mid-project setback reporting, separate-chapter Societal Impact treatment, or Hevner-cycle DSR framing. Use `a-thesis-trana-jorgensen-2025.md` for Peffers DSRM and iteration narration; use `a-thesis-amundsen-remoy-2025.md` for prose voice and Ch 1 structural moves.

---

## Structural summary

The thesis runs eight numbered chapters plus front matter and appendix:

- **Front matter:** Abstract, Sammendrag, Preface, Assignment Details, Contents, Figures, Tables, Acronyms.
- **Ch 1 Introduction:** Background → Research Questions → Structure.
- **Ch 2 Theory:** Cellular Communication, Statistical Methods, Machine Learning Preliminaries (datasets, validation, metrics, optimisation, explainability, supervised algorithms, deep learning).
- **Ch 3 Method:** Planning and Deciding the Research, Research Approach (scientific method + DSR research design), Development Approach, Preliminary Setup (data collection, exploratory analysis, dataset selection, merging, wrangling, feature engineering, defining underperformance, addressing imbalance, model choice, validation metrics), Conducting Research Experiments (one subsection per RQ).
- **Ch 4 Results:** Model Comparison, Time Granular Measurements, Centralized vs Distributed Models, Understanding Model Predictions. Each subsection maps directly to one experiment.
- **Ch 5 Discussion:** Comparing the ML Model Types, Time Granular Measurements, Centralized vs Distributed Models, Understanding Model Predictions, Supplementing Self-Healing Systems with End-User Data, Reflection on Methodology (Reproducibility, Validity, Setbacks).
- **Ch 6 Conclusion:** Each sub-question quoted, answered, then the main RQ wrapped at the end.
- **Ch 7 Societal Impact:** Separate short chapter with explicit positive AND negative implications as bullets.
- **Ch 8 Further Work:** Grounded extensions, not generic "further research could investigate".
- **Appendix A:** Interview with Experts (Telenor).

The chapter ordering is non-standard: Discussion (Ch 5), Conclusion (Ch 6), Societal Impact (Ch 7), Further Work (Ch 8). Conclusion sits before Societal Impact and Further Work rather than absorbing them.

---

## Key A-grade signals (transferable lessons)

1. **Pivot framing in front matter.** "Assignment Details" page (used as the template for our own Task Description) quotes the original SimulaMet brief verbatim, then says in three sentences that the task pivoted, what direction it pivoted to, and that some questions explored fall outside the original scope. No litigation, no apology, no defensiveness. The directness is itself an A-grade signal — the thesis tells the reader the truth and trusts them to keep reading.

2. **Sub-question threading across the entire thesis.** Each of the three sub-questions travels Ch 1 (motivation) → Ch 3 (its experimental design) → Ch 4 (its results subsection) → Ch 5 (its discussion subsection) → Ch 6 (its conclusion paragraph). The reader can hold one SQ in mind and follow it cleanly through the document. We do something similar with anchors and SQs (SQ1↔Efficiency, SQ2↔Control, SQ3↔Adaptability), but our threading is currently less mechanical — the SQ-to-section pointers in our Ch 5 §5.4 limitations preface help, but the Ch 4 findings sections aren't named after the SQs.

3. **Setbacks as a named subsection.** §5.6.3 lists what went wrong honestly: dataset wasn't pre-labelled as expected (forced the pivot), labelling process had to be invented, HPC downtime, scope had to narrow. Each setback is named, the consequence is named, and the response is named. Our §5.7 (Methodology Reflection) goes deep on the synthetic-benchmark weakness but doesn't have a comparable inventory of operational setbacks. Worth considering whether to add a "Setbacks" treatment that names: the original single-day interview plan that became a fortnight, the multi-engine architecture that wasn't in scope at start, the user testing that didn't happen.

4. **Reflection on Methodology with three named pillars.** §5.6 splits into Reproducibility, Validity, Setbacks. Each is a separate subsection, each addresses one specific concern. Our §5.7 currently runs as one continuous prose argument. Splitting along Malterud's three pillars (Relevance, Validity, Reflexivity) would mirror the same discipline.

5. **Societal Impact as its own short chapter.** Ch 7 is two pages of bullets: three positive implications, two negative implications, each in three to five lines. The brevity is the point — the thesis names effects without padding them with theory. Our §5.3 (Sustainability) operationalises SusAF across five dimensions plus four ethical dilemmas plus three SDG mappings, which is more analytically dense but less digestible. The benchmark format (positive bullets, negative bullets, done) is worth considering for a tighter pass on §5.3.

6. **Further Work bullets are grounded, not generic.** Ch 8 lists six concrete extensions, each tied to a specific finding or limitation in the thesis. Generic items ("further research could investigate") do not appear. Our §6.3 already follows this rule per CLAUDE.md ("Generic items are not on this list"); the benchmark confirms it.

7. **Hevner three-cycle DSR over Peffers DSRM.** §3.2.2 picks the Hevner three-cycle framing (Relevance, Design, Rigor) rather than Peffers' six activities, and acknowledges that the project prioritises the Design cycle "due to time limitations". The choice is justified out loud rather than defaulted to. Our thesis defaults to Peffers DSRM applied through six activities; the precedent for picking the framework that fits the project (and saying so) is useful if a future revision wants to make our methodology choice more deliberate.

8. **Industry interview as triangulation, not as primary data.** §3.2.2 and Appendix A document an interview with Telenor used to verify that the research questions are of industry interest and to anchor the explainability requirement. The interview is one of several inputs, not the empirical foundation. Our seven coordinator interviews carry more weight in our thesis than the Telenor interview does in theirs, but the precedent for using an industry interview as a triangulation point inside a DSR frame is the same.

9. **Decision criteria as a table, not as prose.** §3.1 (Planning and Deciding the Research) presents the criteria for selecting research direction (Academic relevance, Industry relevance, Feasibility, Novelty, Ethics, Motivation) as a two-column table with description text. The table makes the decision process auditable. Our Ch 3 currently narrates choices in prose; some of the decisions in §3.5 (iterations) and §3.6 (evaluation framework) might benefit from a similar audit-trail table.

10. **Conclusion before Societal Impact and Further Work.** The thesis closes its main argument in Ch 6 (Conclusion), then opens Ch 7 (Societal Impact) and Ch 8 (Further Work) as separate concerns. This keeps the conclusion focused on what the thesis claims, not on what it gestures toward. Our Ch 6 currently bundles Conclusion (§6.1, §6.2) and Future Work (§6.3) in the same chapter, which is conventional but does mean the closing claim has to compete with the future-work list. Worth being aware of.

---

## What is structurally different from ours

- **ML-experimental rather than software-system.** Their results chapter is F1-scores, ROC curves, and confusion matrices. Ours is feature inventories, requirements counts, and benchmark wall-clock figures. The two thesis types ask different questions of their evaluation chapters — they need to defend an experimental design; we need to defend an artefact-plus-validation framework.
- **Three authors, not two.** Their §3.1 explicitly addresses team roles, work distribution, and Jira-tracked timesheets. Our §4.6.3 (Time Tracking) covers similar ground in two paragraphs.
- **No multi-tenant, no HITL, no anchor concepts.** Their thesis is a research project; ours is a system project under industry constraints. Their structural moves transfer where they don't depend on the system-thesis frame; the rest is reference, not template.
- **Hevner three-cycle, not Peffers six-activity DSRM.** Different DSR framing. Our Peffers framing is locked, but the precedent for an A-grade thesis using a different DSR variant is on file.
- **Industry partner is a research institution.** SimulaMet is non-commercial and contributes a dataset rather than a deployment expectation. Admmit is commercial and contributes a deployment expectation (HITL + multi-tenant) plus a customer roster for interviews. The industry-partner relationships read differently in the front matter.
- **151 pages vs our 75.** Their thesis is substantially longer because the methodology chapter walks through dataset construction, feature engineering, and ML preliminaries in detail. Length is not the signal — the discipline of every page earning its place is.

---

## Quick comparison snapshot

| Dimension | Brand et al. (2024) | Trana & Jørgensen (2025) | Amundsen & Remøy (2025) | Ours |
|---|---|---|---|---|
| Supervisor | Skundberg | Alsam | Alsam | Alsam |
| Industry partner | SimulaMet (research) | SSB (statistics agency) | (none — public discourse) | Admmit (commercial) |
| Paradigm | DSR (Hevner three-cycle) | DSR (Peffers DSRM, 6 activities, 8 iterations) | Mixed-methods qualitative + computational | DSR (Peffers DSRM, 6 activities, 8 iterations) |
| Empirical core | Telecoms end-user dataset + Telenor interview | LLM benchmarks + user testing | YouTube comments + interviews | Seven coordinator interviews + multi-engine benchmark |
| Sub-questions | 3 (each → one experiment) | 3 (each → DSR activity) | 3 (each → data source) | 3 (each → anchor concept) |
| Pivot acknowledged | Yes, in front matter and §5.6.3 | No (no pivot) | No (no pivot) | No (operationalised, not pivoted) |
| Societal/sustainability | Ch 7 separate, bulleted | SusAF chapter | Within discussion | §5.3 SusAF + ethics |
| Length | 151 pp | ~120 pp | ~100 pp | 75 pp |
