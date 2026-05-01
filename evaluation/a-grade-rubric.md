# A-Grade Rubric — Ressursplanlegger Bachelor Thesis

> This is the primary quality gate. Claude reads this before every output.
> Every section produced must be evaluated against these criteria.
> If a section does not meet A criteria, revise it before outputting.
>
> Source: NTNU data engineering bachelor grading standards (general).
> Complemented by evaluation/grading-guidelines.md (official NRT sensor criteria, now filled).

---

## What Separates an A from a B

| Dimension | B — Solid | A — Exceptional |
|-----------|-----------|-----------------|
| **Argument** | Claims are supported | Every claim has a direct reference to theory, data, or the system |
| **Precision** | Concepts are described | Concepts are defined, operationalised, and connected to this project |
| **Coherence** | Chapters stand alone | Every chapter explicitly builds on the previous; nothing is repeated |
| **Analysis** | Describes what happened | Explains why it happened and what it means |
| **Limitations** | Mentioned briefly | Analysed honestly with impact on conclusions |
| **Language** | Correct and readable | Concise, variation in sentence structure, no hedging |
| **Citations** | Sufficient | Every theoretical claim has a citation; primary sources preferred |

---

## A-Grade Criteria Per Chapter

### Chapter 1 — Introduction

**An A introduction:**
- **Anchor coherence:** Names the three anchor concepts (Effektivitet, Tillit/kontroll, Tilpasningsdyktighet) verbatim in §1.2 with brief definitions; these exact names recur in Discussion and Conclusion without synonyms.
- **Visibility-gap opening:** First paragraph leads with a concrete Norwegian transport-sector fact and the resource-utilization visibility gap, not generic preamble ("the transport sector's role in Norway", "in today's digital world").
- States the problem in one crisp sentence — what, for whom, and why it matters — in the first paragraph
- Motivates the problem with concrete evidence (scale, cost, or observed inefficiency), not just assertion
- Research question is narrow, answerable, and directly traceable to the problem statement
- Sub-questions are additive — each covers a distinct dimension not covered by the main RQ; each is quotable as a single-line block quote in Ch 6
- Scope delimiters have explicit justifications — "X is out of scope because Y", not just a list
- Chapter structure section reads as a logical chain, not a table of contents

**Red flags that signal B or lower:**
- "The purpose of this thesis is to explore..." — too vague
- Research question is not a question or cannot be definitively answered
- Scope section lists what is excluded without explaining why
- First paragraph does not establish the problem — starts with context instead

---

### Chapter 2 — Theory

**An A theory chapter:**
- **Asymmetric depth and use-trace:** The most argument-load-bearing theory gets the most space (HITL section dominates given the three-layer Bainbridge / Hoff & Bashir / Miller treatment); secondary concepts get under one page; every theoretical concept introduced reappears in Findings or Discussion.
- **Three-layer HITL:** §2.2 layers Bainbridge (operator-vs-owner asymmetry, irony of automation) → Hoff & Bashir (trust-calibration model) → Miller (explanation as interface), alongside existing Parasuraman taxonomy and Lee trust foundation.
- **Utilization framing:** §2.1 frames resource scheduling under the utilization lens (overtime, idle time, load balance), not just as constraint satisfaction — preloading the Discussion's Effektivitet sub-section.
- Every theory presented is directly connected to a specific design decision or finding in the thesis
- Resource scheduling formulation is precise: problem structure (multi-resource assignment with constraints), why this characterisation fits the domain, and how it differs from adjacent problems (e.g., VRP focuses on sequencing, not assignment)
- Existing systems (TMS) are positioned against Ressursplanlegger as category — only Timpex named by name; other interviewed companies use internal/custom tools
- No theory is presented for its own sake — if it does not appear in Ch 4 or Ch 5, it should not be in Ch 2
- Primary sources are cited — textbooks for foundational theory, peer-reviewed papers for specific claims

**Red flags that signal B or lower:**
- Theory is a literature review with no connection to the system
- Scheduling problem is described generically without connecting to the specific constraints in Ressursplanlegger
- Related work describes other systems but does not compare them to Ressursplanlegger
- Human-in-the-loop is mentioned in theory but never referenced in Discussion

---

### Chapter 3 — Methodology

**An A methodology chapter:**
- **Origin story (§X.1):** Opens with a paragraph naming how the project began — Admmit's bachelor task, the team's own initiative in contacting coordinators, HITL as Admmit mandate from project start (validated by interviews, not introduced by them). Reads as a story, not a specification.
- **DSRM applied step-by-step:** Method Theory section maps Peffers' six DSRM activities to this specific project, one bullet per activity. Each bullet is 2–4 sentences naming what was actually done. (See `evaluation/reference-thesis-analysis.md` §11.5 for format.)
- **Named iterations (4–6):** Iterative Development Process contains at least four named iterations with descriptive titles (e.g., *Single-engine baseline*, *Constraint generalisation*, *Multi-engine selection*). Each iteration follows tried / why / what happened (positive AND limitations) / learned / next. Honest about failure. Each iteration carries an inline origin label (interview-driven / Admmit mandate / designer-technical) per §12.0.5.
- **Evaluation framework separate from validity:** A dedicated sub-section describes how the artefact is tested (synthetic dataset design, multi-engine "How-not-Of" benchmark) — distinct from Validity and Reliability which addresses the research's epistemic limits.
- Research paradigm is stated and justified in one clear paragraph — not just named
- DSR is connected to Ressursplanlegger explicitly: the artefact, the evaluation, the iteration
- Interview methodology is described precisely enough that it could be replicated
- Participant selection is justified: why these 7 companies, why traffic coordinators specifically
- Validity and reliability section is honest: acknowledges self-selection bias, small sample, and author affiliation with Admmit
- Every methodological choice has a "because" — not just "we chose semi-structured interviews"

**Red flags that signal B or lower:**
- DSR is described generically without connecting it to this specific project
- "7 interviews were conducted" without explaining how companies were selected
- No discussion of validity or limitations of the method
- System development process is absent or described as a sprint diary

---

### Chapter 4 — Findings

**An A findings chapter:**
- **Category split:** Findings split by category — empirical interview synthesis / artefact (Ressursplanlegger system + algorithm) / process documentation (sprint log, decisions, time tracking). No interpretation in any of them; that lives in Discussion.
- **DSR Artifacts mapping:** A dedicated table maps each project artefact to its DSR category (Construct / Model / Method / Instantiation), making the abstract DSRM theory in Ch 3.2 concrete and verifiable.
- **Multi-engine "How-not-Of" framing:** §4.5 algorithm section opens with explicit framing — the multi-engine architecture is a methodologically independent test of *how* the constraint problem is best solved, not *whether* the artefact's claims about utilization are real (per §12.0.5).
- **Visibility-gap finding surfaces in interview themes:** §4.1 names the resource-utilization visibility gap as one of the empirical themes from interviews, with operator-vs-owner asymmetry as a secondary surprising finding.
- Interview findings are presented without interpretation — facts only, in this chapter
- Pain points are ranked or weighted by frequency across interviews, not listed equally
- Requirements have explicit source tracing: each requirement is attributed to specific interview(s)
- Architecture description is precise: named components, their responsibilities, and how they communicate
- Algorithm section includes: problem formulation, input/output specification, chosen approach with justification, constraints modelled, and known limitations
- Fit/gap table is structured: for each gap, the current state, the ideal state, and how Ressursplanlegger addresses it (or does not)

**Red flags that signal B or lower:**
- Interview findings include phrases like "this suggests that" — that is interpretation, not findings
- Requirements are listed without MoSCoW priority or source
- Architecture section describes what the system does, not how it is built
- Algorithm section says "we use an optimisation algorithm" without specifying the method

---

### Chapter 5 — Discussion

**An A discussion chapter:**
- **Anchor-organised primary findings:** §5.1 contains exactly three sub-sections, one per locked anchor (5.1.1 Effektivitet, 5.1.2 Tillit/kontroll, 5.1.3 Tilpasningsdyktighet). Anchor names are used verbatim — no synonyms ("kontroll" alone, "fleksibilitet", "skalerbarhet", "human control"). Each sub-section has a `MUST ANCHOR` marker tied to exactly one anchor.
- **Operator-vs-owner asymmetry framed inside §5.1.1:** The asymmetry is the interpretive frame for the visibility-gap finding — owners demand utilization optimization, coordinators do not articulate this need themselves. Bainbridge's *ironies of automation* is cited here.
- **Three-layer HITL applied in §5.1.2:** Bainbridge frames operator authority over override; Hoff & Bashir's dimensional model of trust antecedents explains how trust forms over use; Miller motivates explanation/transparency as a design requirement.
- **Hierarchical limitations (L1–L12), each named:** §5.4 contains three named sub-subsections — Empirical Foundation (L1, L2, L3, L4), Validation and Artefact (L5–L9), Conceptual and Methodological (L10, L11, L12). Each L# is a named paragraph or `\paragraph{}`, not a buried sentence. An L#-to-SQ mapping appears at the top of §5.4.
- **Deviations and Methodology Reflection as named sections:** §5.5 names plan-vs-reality differences explicitly. §5.6 contains a self-critical paragraph naming the actual weak spot in the method (e.g., small sample, synthetic-only validation, dev-team = research-team).
- Opens by explicitly referencing the research question — the answer is developed, not stated
- Every finding in Ch 4 is either addressed or explicitly declared out of scope for discussion
- Connects findings back to specific theories from Ch 2 — not just "as discussed in Chapter 2"
- Limitations section analyses impact: "this limitation means that X conclusion must be qualified because Y"
- Adoption barriers are discussed as design problems, not just observations
- Does not introduce new facts — everything is interpretation of what was already presented

**Red flags that signal B or lower:**
- Discussion section re-describes findings instead of interpreting them
- Connections to theory are vague: "relates to the scheduling literature" without specifics
- Limitations are listed but their impact on conclusions is not discussed
- Research question is not explicitly referenced until the Conclusion

---

### Chapter 6 — Conclusion

**An A conclusion:**
- **RQ block-quote pattern:** Each sub-question is reproduced verbatim as a single-line block quote, then answered in one discrete paragraph with no new material. Three SQs → three paragraphs. Each paragraph carries a `MUST TRACE` to the originating Ch 5 sub-section AND names the anchor it serves.
- **Limitation-grounded Future Work:** Each Future Work item cites a specific named limitation from §5.4 (e.g., "addresses L8 — no user testing with coordinators"). Generic items without a named limitation grounding are red flags.
- **Closing domain claim:** Final sentence makes a claim about algorithm-assisted planning under stakeholder asymmetry in Norwegian transport, not just about the artefact ("Ressursplanlegger does X").
- First paragraph summarises the thesis in 3–5 sentences — problem, method, finding, implication
- No new analysis or claims are introduced

**Red flags that signal B or lower:**
- Sub-questions are not answered individually
- Future work is generic ("further research could investigate...")
- Conclusion introduces new material not discussed earlier
- Final paragraph is a summary of the conclusion rather than a closing claim

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

---

## Self-Evaluation Checklist

Before outputting any section, ask:

1. Does every claim have either a citation or a reference to primary data (interviews, system)?
2. Is every term from the domain defined on first use in glossary.md terms?
3. Does this section serve the chapter's thesis-spine.md sentence?
4. Is there a single sentence that could be cut without losing meaning?
5. Would an external examiner (who knows the domain but not this project) understand this clearly?
6. Does this section help answer the research question, even indirectly?

If the answer to any of these is "no" or "I'm not sure" — fix it first.

---

## Score Template for Quality Agent

When evaluating a chapter, score each criterion:

```
Criterion: [name]
Grade:     A / B / C / Cannot assess yet
Strength:  [specific quote or observation]
Weakness:  [specific quote or gap]
One fix:   [single concrete action]
```

End with:
- Overall estimated grade for this chapter
- Single most important thing to fix before submission
- Whether this chapter, as written, would pull the thesis grade up or down
