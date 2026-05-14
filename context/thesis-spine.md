 # Thesis Spine — Ressursplanlegger

> This file is the backbone of the thesis.
> Every agent reads this before writing or reviewing anything.
> Update it if the argument changes — but try not to change it.
> One sentence per chapter. No more.

---

## The Problem

The traffic coordinator at a fleet-scale Norwegian transport company solves an optimisation puzzle every working day: matching drivers and vehicles to a stream of incoming orders under hard rules (driving-hours law, vehicle capacity, customer time windows) and soft priorities (workload balance, driver preferences, customer continuity). Two structural features make the puzzle hard to support with software. First, the data needed to plan well is present in the company's systems but distributed across several tools and the coordinator's memory, with no view that assembles it; this is the *visibility gap*. Second, much of what argues for or against any specific assignment is *tacit knowledge* the coordinator carries that no current system can read off the screen. Existing Transport Management Systems (Timpex, Opter, internal tools) cover order management and invoicing but leave the assignment-planning step itself to the coordinator. The demand for an algorithm-assisted system that fills that gap is articulated jointly by Admmit (relaying the owner-side request for utilisation optimization) and by the interviewed coordinators (who welcomed an algorithm proposing assignments under conditions that keep them in charge of the result). The structural pattern in which the parties specifying automation are not the same as the parties operating it (Bainbridge 1983, *Ironies of Automation*) frames the design constraint that follows from this configuration: any system proposed must be operable by, and useful to, the coordinator who runs it.

---

## The Research Question

> To what extent can an algorithm-assisted planning platform automate the traffic coordinator's planning work in Admmit's customer companies in a way that improves resource utilisation (reducing overtime, idle time between assignments, and uneven driver load) and is perceived as useful by the coordinator who runs it?

The RQ frames the work as a balance between two simultaneous demands: utilisation gains the company can measure (overtime, idle time, uneven load), and a workflow the coordinator who runs it perceives as useful. The "preserving tacit knowledge and authority" clause carried in earlier RQ wordings (struck 2026-05-07) is now implicit: a system the coordinator perceives as useful is, by construction, one that has not displaced the tacit knowledge or the override authority on which their role depends. Two failure modes are out of scope as answers: a system that automates everything and leaves the coordinator with nothing meaningful to do (and so will not be perceived as useful), and a system that leaves the coordinator fully in charge but moves no numbers.

### Sub-questions the thesis must answer

Each sub-question is designed to be quotable verbatim as a single-line block quote in Chapter 6, answerable in one paragraph traceable to a specific Discussion anchor sub-section, and bounded by named limitations from §5.4. Updated 2026-05-06 to align with the reframed RQ; previous SQ wordings are recorded in `context/supervisor-log.md` 2026-05-06.

1. **SQ1** — *To what extent does RP reduce overtime, idle time, and uneven driver load below the level produced by current planning practice in Admmit's customer companies?* → answered in Ch 5.1.1 (Efficiency) → bounded by L1, L2, L3, L4, L5, L6, L7
2. **SQ2** — *Through what kind of interface and process can the traffic coordinator review and override every algorithm-generated assignment without making the planning workflow heavier than current practice?* → answered in Ch 5.1.2 (Control) → bounded by L8, L10
3. **SQ3** — *Through which configurable elements can RP serve companies that differ in operational rules, fleet size, and planning horizon, without changes to the code?* → answered in Ch 5.1.3 (Adaptability) and cross-anchor → bounded by L9, L11, L12

---

## Anchor Concepts

The thesis argument turns on three named concepts. Every chapter must reference at least one. Discussion (Ch 5) and Conclusion (Ch 6) MUST organise their findings under them. Anchor names are locked English proper nouns used consistently across the thesis — never re-translated to Norwegian, never split, never paraphrased (e.g. "Control" is the unit, not "control" alone). Synonyms ("effektivitet", "tillit/kontroll", "tilpasningsdyktighet", "fleksibilitet", "skalerbarhet", "human control", "operator oversight", "trust calibration") drift the spine and must be flagged by reviewers.

1. **Efficiency** — improved resource utilisation across three concrete dimensions: reduced overtime, reduced idle time between assignments, and reduced uneven load between drivers. Visibility into current utilisation is the precondition for optimization; the system's primary value is making invisible patterns legible to coordinator and owner.
2. **Control** — the coordinator's authority to review and override any algorithm-generated assignment, applying the tacit knowledge the algorithm cannot see. Trust and control are inseparable: trust is built through demonstrable control. Use the compound term verbatim. (The earlier "inspect, modify, accept, or reject" gloss was retired 2026-05-06; see `context/lessons-learned.md` *Don't list the four Control actions* and the supersession note on Sub-clause C.)
3. **Adaptability** — capacity to function meaningfully across companies with materially different operational rules, fleet composition, and assignment criteria. Distinct from "skalerbarhet" (which concerns volume).

---

## The Argument — One Sentence Per Chapter

**Chapter 1 — Introduction:**
A running example scaling from one operator to a fleet introduces the planning puzzle, the visibility gap, and the role of tacit knowledge; Ressursplanlegger is then named as the artefact this thesis builds and evaluates to support the coordinator's work, and the three anchors (Efficiency, Control, Adaptability) frame what such support has to deliver.

**Chapter 2 — Theory:**
Four theoretical foundations support the rest of the thesis: resource scheduling under utilisation-oriented constraints, with §2.2 layering five HITL sources (Parasuraman's automation taxonomy, Bainbridge's operator-vs-owner framing, Hoff and Bashir's trust-calibration model, Miller's explanation-as-interface, and Lee and See's trust foundation); Transport Management Systems used to position RP inside the existing software category and identify the planning gap RP fills; and Design Science Research as the paradigm under which both the artefact and the knowledge claims are made.

**Chapter 3 — Methodology:**
A Design Science Research process applied through Peffers' six DSRM activities — anchored in the project's origin in Admmit's bachelor task, semi-structured interviews with seven traffic coordinators contacted on the team's own initiative, six named iterations of the artefact, and an evaluation framework that combines synthetic benchmarks, auto-router run history, and requirements traceability — establishes how the research was conducted.

**Chapter 4 — Findings:**
Interview themes surface the resource-utilisation visibility gap and the role of tacit knowledge in the coordinator's daily work, alongside operator-vs-owner asymmetry as one observed structural pattern in how the demand for automation is articulated; Ressursplanlegger embodies the locked design qualities as a Next.js + tRPC + PostgreSQL platform with a multi-engine solver layer, a category-based auto-router, and a human-in-the-loop drag-and-drop timeline, with a DSR Artifacts mapping linking each project artefact to its category.

**Chapter 5 — Discussion:**
Organised under the three locked anchors — Efficiency (visibility gap, operator-vs-owner asymmetry, and synthetic solver benchmark), Control (HITL applied to override authority and tacit knowledge), Adaptability (cross-company adaptability via configurable weights and category-based auto-routing) — the discussion names twelve hierarchical limitations (L1–L12), explicit claim boundaries, and a self-critical methodology reflection.

**Chapter 6 — Conclusion:**
Each sub-question is quoted verbatim and answered in a single paragraph tied to the anchor it serves, with Future Work grounded in specific named limitations and a closing claim about the balance between automation and the coordinator's perceived utility — that algorithm-assisted planning at the scale of Admmit's customer companies is feasible inside a single deployable artefact when automation is bounded by review-and-override authority and configurability per company.

---

## How to Use This File

- **Writer agent:** Check that each section you write serves the chapter's one-sentence purpose above and references at least one anchor concept where the chapter's role requires it.
- **Red thread agent:** Verify that no chapter introduces arguments or conclusions that contradict or skip ahead of this spine, and that anchor names are used verbatim wherever they appear.
- **Quality agent:** Use this to assess whether the overall argument is coherent and whether anchor references close the loops opened in Chapter 1.

---

## Spine Status: APPROVED DRAFT

Last revised: 2026-05-13. Ch 3 sentence updated from eight named iterations to six named iterations, and the evaluation framework updated to include benchmark, auto-router run history, and traceability. Previous 2026-05-02 revision updated Ch 2 sentence to five-layer HITL (Parasuraman + Bainbridge + Hoff & Bashir + Miller + Lee) to match `result/chapters/ch2/ch2-theory.tex`; reworded TMS-as-category clause from "delimit" to "position the gap" to match what §2.3 actually does.
Previous revision 2026-04-30: Sharpened RQ + locked anchor concepts (Efficiency / Control / Adaptability) + revised sub-questions reflecting operator-vs-owner asymmetry per `evaluation/reference-thesis-analysis.md` §12.0–§12.0.7. Bainbridge (1983) added as theoretical anchor for HITL discussion.
Review again after Chapter 4 is drafted — if findings shift the argument, update the spine before writing Chapter 5.

<!--
Sub-question trace plan (updated 2026-05-06 to reflect reframed RQ + SQs):
SQ1 (utilisation-improvement question) → §5.1.1 Efficiency
      → bounded by L1 (sample size, 7 interviews),
                    L2 (self-selection bias — Admmit customers only),
                    L3 (author affiliation with Admmit),
                    L4 (interview-guide coverage gap),
                    L5 (synthetic benchmarks, not production data),
                    L6 (no real-world deployment),
                    L7 (no empirical comparison against existing TMS)
SQ2 (review-and-override question; tacit-knowledge channel) → §5.1.2 Control
      → bounded by L8 (no user testing with coordinators),
                    L10 (HITL as Admmit mandate, not validated level)
SQ3 (per-company configurability question) → §5.1.3 Adaptability (primary) + cross-anchor (Efficiency, Control)
      → bounded by L9 (algorithm evaluation against own benchmarks only),
                    L11 (single domain — Norwegian transport),
                    L12 (boundary cases described, not quantified)

Pre-2026-05-06 SQ wording (preserved here for trace; the operative SQs are the bullets above):
- SQ1 (old): "How is resource-utilisation visibility distributed across operator and owner stakeholders in current Norwegian transport-company planning practice?"
- SQ2 (old): "How can an algorithm-assisted planning system be designed so that automated optimisation improves resource utilisation while remaining operable and overridable by the traffic coordinator?"
- SQ3 (old): "To what extent and under what limitations does Ressursplanlegger demonstrate measurable improvement in resource utilisation?"
-->
