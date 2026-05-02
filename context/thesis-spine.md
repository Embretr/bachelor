 # Thesis Spine — Ressursplanlegger

> This file is the backbone of the thesis.
> Every agent reads this before writing or reviewing anything.
> Update it if the argument changes — but try not to change it.
> One sentence per chapter. No more.

---

## The Problem

Norwegian transport companies operate without systematic visibility into resource utilization: overtime is handled reactively, and load balancing across drivers depends on traffic coordinators' memory and intuition rather than any structured overview. Demand for algorithm-assisted planning thus comes primarily from owners and the business side, not from the coordinators who must operate any such system — a configuration that mirrors Bainbridge's (1983) *ironies of automation*. Tacit knowledge dependency and slow legacy software are downstream consequences of this visibility gap, not its origin.

---

## The Research Question

> How can an algorithm-assisted resource planning platform improve resource utilization in Norwegian transport companies (reducing overtime, idle time between assignments, and uneven driver load) while remaining accountable to the traffic coordinator who operates it?

### Sub-questions the thesis must answer

Each sub-question is designed to be quotable verbatim as a single-line block quote in Chapter 6, answerable in one paragraph traceable to a specific Discussion anchor sub-section, and bounded by named limitations from §5.4.

1. **SQ1** — *How is resource-utilization visibility distributed across operator and owner stakeholders in current Norwegian transport-company planning practice?* → answered in Ch 5.1.1 (Effektivitet) → bounded by L1, L2, L3, L4
2. **SQ2** — *How can an algorithm-assisted planning system be designed so that automated optimisation improves resource utilization while remaining operable and overridable by the traffic coordinator?* → answered in Ch 5.1.2 (Tillit/kontroll) → bounded by L8, L10
3. **SQ3** — *To what extent and under what limitations does Ressursplanlegger demonstrate measurable improvement in resource utilization?* → answered in Ch 5.1.3 (Tilpasningsdyktighet) and cross-anchor → bounded by L5, L6, L7, L9, L11, L12

---

## Anchor Concepts

The thesis argument turns on three named concepts. Every chapter must reference at least one. Discussion (Ch 5) and Conclusion (Ch 6) MUST organise their findings under them. Anchor names are Norwegian compound terms used as proper nouns in English prose — never translated, never split (e.g. "Tillit/kontroll" is the unit, not "Tillit" alone). Synonyms ("kontroll" alone, "fleksibilitet", "skalerbarhet", "human control", "menneskelig overstyring") drift the spine and must be flagged by reviewers.

1. **Effektivitet** — improved resource utilization across three concrete dimensions: reduced overtime, reduced idle time between assignments, and reduced uneven load between drivers. Visibility into current utilization is the precondition for optimization; the system's primary value is making invisible patterns legible to coordinator and owner.
2. **Tillit/kontroll** — the coordinator's ability to inspect, modify, accept, or reject any algorithm-generated assignment. Trust and control are inseparable: trust is built through demonstrable control. Use the compound term verbatim.
3. **Tilpasningsdyktighet** — capacity to function meaningfully across companies with materially different operational rules, fleet composition, and assignment criteria. Distinct from "skalerbarhet" (which concerns volume).

---

## The Argument — One Sentence Per Chapter

**Chapter 1 — Introduction:**
Norwegian transport companies operate without systematic visibility into resource utilization, a gap whose articulation skews toward owners rather than the coordinators who must operate any algorithm-assisted system — the configuration Bainbridge's *ironies of automation* anticipates, and the configuration Ressursplanlegger is designed to address.

**Chapter 2 — Theory:**
Resource scheduling under utilization-oriented constraints, a five-layer human-in-the-loop theory (Parasuraman's automation taxonomy, Bainbridge's operator-vs-owner framing, Hoff and Bashir's trust-calibration model, Miller's explanation-as-interface, and Lee and See's trust foundation), and Design Science Research provide the theoretical foundation; vehicle routing theory is referenced only to delimit and TMS-as-category is used to position the gap the artefact fills.

**Chapter 3 — Methodology:**
A Design Science Research process applied through Peffers' six DSRM activities — anchored in the project's origin in Admmit's bachelor task, semi-structured interviews with seven traffic coordinators contacted on the team's own initiative, four to six named iterations of the artefact, and a separate evaluation framework that benchmarks solver approaches under realistic constraint combinations — establishes how the research was conducted.

**Chapter 4 — Findings:**
Interview themes surface the resource-utilization visibility gap and the operator-vs-owner asymmetry that makes it a finding worth surfacing, and Ressursplanlegger embodies the locked design qualities as a Next.js + tRPC + PostgreSQL platform with a multi-engine solver layer (greedy / OR-Tools CP-SAT / Timefold) and a human-in-the-loop drag-and-drop timeline, with a DSR Artifacts mapping linking each project artefact to its category.

**Chapter 5 — Discussion:**
Organised under the three locked anchors — Effektivitet (visibility gap, operator-vs-owner asymmetry, multi-engine "How-not-Of" benchmark), Tillit/kontroll (three-layer HITL applied to override authority and tacit knowledge), Tilpasningsdyktighet (cross-company adaptability via configurable constraint weights) — the discussion names twelve hierarchical limitations (L1–L12), explicit deviations from plan, and a self-critical methodology reflection.

**Chapter 6 — Conclusion:**
Each sub-question is quoted verbatim and answered in a single paragraph tied to the anchor it serves, with Future Work grounded in specific named limitations and a closing claim about algorithm-assisted planning under stakeholder asymmetry in Norwegian transport.

---

## How to Use This File

- **Writer agent:** Check that each section you write serves the chapter's one-sentence purpose above and references at least one anchor concept where the chapter's role requires it.
- **Red thread agent:** Verify that no chapter introduces arguments or conclusions that contradict or skip ahead of this spine, and that anchor names are used verbatim wherever they appear.
- **Quality agent:** Use this to assess whether the overall argument is coherent and whether anchor references close the loops opened in Chapter 1.

---

## Spine Status: APPROVED DRAFT

Last revised: 2026-05-02. Updated Ch 2 sentence to five-layer HITL (Parasuraman + Bainbridge + Hoff & Bashir + Miller + Lee) to match `context/outline.md` §2.2 and the drafted `result/chapters/ch2/ch2-theory.tex`; reworded TMS-as-category clause from "delimit" to "position the gap" to match what §2.3 actually does.
Previous revision 2026-04-30: Sharpened RQ + locked anchor concepts (Effektivitet / Tillit/kontroll / Tilpasningsdyktighet) + revised sub-questions reflecting operator-vs-owner asymmetry per `evaluation/reference-thesis-analysis.md` §12.0–§12.0.7. Bainbridge (1983) added as theoretical anchor for HITL discussion.
Review again after Chapter 4 is drafted — if findings shift the argument, update the spine before writing Chapter 5.

<!--
Sub-question trace plan (verified by task 12 outline rebuild):
SQ1 → §5.1.1 Effektivitet
      → bounded by L1 (sample size, 7 interviews),
                    L2 (self-selection bias — Admmit customers only),
                    L3 (author affiliation with Admmit),
                    L4 (interview-guide coverage gap)
SQ2 → §5.1.2 Tillit/kontroll
      → bounded by L8 (no user testing with coordinators),
                    L10 (HITL as Admmit mandate, not validated level)
SQ3 → §5.1.3 Tilpasningsdyktighet (primary) + cross-anchor (Effektivitet, Tillit/kontroll)
      → bounded by L5 (synthetic benchmarks, not production data),
                    L6 (no real-world deployment),
                    L7 (no empirical comparison against existing TMS),
                    L9 (algorithm evaluation against own benchmarks only),
                    L11 (single domain — Norwegian transport),
                    L12 (boundary cases described, not quantified)
-->
