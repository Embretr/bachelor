### Chapter 2 — Theory

**An A theory chapter:**
- **Asymmetric depth and use-trace:** The most argument-load-bearing theory gets the most space (HITL section dominates given the three-layer Bainbridge / Hoff & Bashir / Miller treatment); secondary concepts get under one page; every theoretical concept introduced reappears in Findings or Discussion.
- **Three-layer HITL:** §2.2 layers Bainbridge (operator-vs-owner asymmetry, irony of automation) → Hoff & Bashir (trust-calibration model) → Miller (explanation as interface), alongside existing Parasuraman taxonomy and Lee trust foundation.
- **Utilization framing:** §2.1 frames resource scheduling under the utilization lens (overtime, idle time, load balance), not just as constraint satisfaction — preloading the Discussion's Effektivitet sub-section.
- Every theory presented is directly connected to a specific design decision or finding in the thesis
- Resource scheduling formulation is precise: problem structure (multi-resource assignment with constraints), why this characterisation fits the domain, and how it differs from adjacent problems (e.g., VRP focuses on sequencing, not assignment)
- Existing systems (TMS) are positioned against Ressursplanlegger as category — Timpex and Opter named by name; other interviewed companies use internal/custom tools. Neither Timpex nor Opter generates assignment plans automatically
- No theory is presented for its own sake — if it does not appear in Ch 4 or Ch 5, it should not be in Ch 2
- Primary sources are cited — textbooks for foundational theory, peer-reviewed papers for specific claims

**Red flags that signal B or lower:**
- Theory is a literature review with no connection to the system
- Scheduling problem is described generically without connecting to the specific constraints in Ressursplanlegger
- Related work describes other systems but does not compare them to Ressursplanlegger
- Human-in-the-loop is mentioned in theory but never referenced in Discussion

---


---

## Cross-Chapter A Criteria

These apply to the thesis as a whole:

**Argument coherence:**
- The thesis spine (context/thesis-spine.md) is traceable chapter by chapter
- No chapter contradicts another
- The conclusion follows logically from the findings and discussion

**Citation quality:**
- Primary sources preferred over secondary sources
- No citation for a claim that is common knowledge in the domain
- No claim left uncited that requires support
- Every citation in text appears in references.bib

**Language:**
- No hedging that weakens claims that have evidence ("it seems to be", "could possibly")
- No overclaiming that goes beyond evidence ("proves that", "definitively shows")
- No passive voice used to hide agency where agency matters ("mistakes were made")
- Consistent use of glossary.md terminology throughout

**Academic integrity:**
- All quotes are in quotation marks with page number
- Paraphrased content is cited
- The system is not described as solving problems it was not tested against

---

## Cross-chapter A-markers (source: ChatSSB 2025)

Structural patterns observed in a verified A-grade NTNU CS bachelor (Reference: `evaluation/reference-thesis-analysis.md`). Reviewers MUST check these eight patterns when assessing the thesis as a whole.

1. **Three locked anchors threaded from Ch 1 to Ch 6** — Effektivitet, Tillit/kontroll, Tilpasningsdyktighet are defined verbatim in Ch 1.2, used to organise Discussion §5.1, and named in each Conclusion RQ-answer paragraph. Synonyms anywhere are flagged as critical drift.
2. **Origin story in Method §3.1** grounding design choices in Admmit's mandate and the team's stakeholder dialogue with seven coordinators.
3. **Named iterations with descriptive titles** in Method §3.5 development section — at minimum four iterations, each with tried / why / what happened / learned / next, and an inline origin label.
4. **Hierarchical limitations in Discussion §5.4** — three named sub-subsections (Empirical L1–L4, Validation L5–L9, Conceptual L10–L12), each L# a named paragraph, not a buried sentence.
5. **Deviations from Plan section** in Discussion §5.5 making plan-vs-reality differences explicit. Most theses hide deviations; A-grade work surfaces them.
6. **Self-critical Methodology Reflection** in Discussion §5.6 naming an actual weak spot in the method, not a perfunctory acknowledgment.
7. **Conclusion that quotes each SQ verbatim** as a block quote and answers discretely in one paragraph each, with no new material.
8. **Forward references in Ch 1 paid off in their target chapter; backward references in Ch 5/6 closing loops opened in Ch 1.** The thesis reads as a single argument, not a sequence of independent chapters.
