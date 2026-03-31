# A-Grade Rubric — Ressursplanlegger Bachelor Thesis

> This is the primary quality gate. Claude reads this before every output.
> Every section produced must be evaluated against these criteria.
> If a section does not meet A criteria, revise it before outputting.
>
> Source: NTNU data engineering bachelor grading standards (general).
> Update with specific sensor criteria once evaluation/grading-guidelines.md is filled.

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
- States the problem in one crisp sentence — what, for whom, and why it matters — in the first paragraph
- Motivates the problem with concrete evidence (scale, cost, or observed inefficiency), not just assertion
- Research question is narrow, answerable, and directly traceable to the problem statement
- Sub-questions are additive — each covers a distinct dimension not covered by the main RQ
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
- Every theory presented is directly connected to a specific design decision or finding in the thesis
- VRP formulation is precise: which variant (VRPTW, CVRP, etc.) and why this variant maps to the problem
- Human-in-the-loop is not just defined — it is argued as necessary for this domain with evidence
- Related work section positions Ressursplanlegger relative to existing approaches — what it adds, not just what others did
- No theory is presented for its own sake — if it does not appear in Ch 4 or Ch 5, it should not be in Ch 2
- Primary sources are cited — textbooks for foundational theory, peer-reviewed papers for specific claims

**Red flags that signal B or lower:**
- Theory is a literature review with no connection to the system
- VRP is defined but the specific variant used is not identified
- Related work describes other systems but does not compare them to Ressursplanlegger
- Human-in-the-loop is mentioned in theory but never referenced in Discussion

---

### Chapter 3 — Methodology

**An A methodology chapter:**
- Research paradigm is stated and justified in one clear paragraph — not just named
- DSR is connected to Ressursplanlegger explicitly: the artefact, the evaluation, the iteration
- Interview methodology is described precisely enough that it could be replicated
- Participant selection is justified: why these 7 companies, why traffic coordinators specifically
- Validity and reliability section is honest: acknowledges self-selection bias and small sample
- Development process is described as methodology, not just a timeline
- Every methodological choice has a "because" — not just "we chose semi-structured interviews"

**Red flags that signal B or lower:**
- DSR is described generically without connecting it to this specific project
- "7 interviews were conducted" without explaining how companies were selected
- No discussion of validity or limitations of the method
- System development process is absent or described as a sprint diary

---

### Chapter 4 — Findings

**An A findings chapter:**
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
- Opens by explicitly referencing the research question — the answer is developed, not stated
- Every finding in Ch 4 is either addressed or explicitly declared out of scope for discussion
- Connects findings back to specific theories from Ch 2 — not just "as discussed in Chapter 2"
- Limitations section analyses impact: "this limitation means that X conclusion must be qualified because Y"
- Adoption barriers are discussed as design problems, not just observations
- The section on human override is the analytical core — argues what the right balance is and why
- Does not introduce new facts — everything is interpretation of what was already presented

**Red flags that signal B or lower:**
- Discussion section re-describes findings instead of interpreting them
- Connections to theory are vague: "relates to the VRP literature" without specifics
- Limitations are listed but their impact on conclusions is not discussed
- Research question is not explicitly referenced until the Conclusion

---

### Chapter 6 — Conclusion

**An A conclusion:**
- First paragraph summarises the thesis in 3–5 sentences — problem, method, finding, implication
- Research question is answered directly with a qualified statement — not "partially" without elaboration
- Each sub-question gets its own answer, cross-referenced to the chapter where evidence was presented
- Future work is concrete and connected to the limitations identified in Ch 5 — not a generic wish list
- No new analysis or claims are introduced
- Final sentence makes a claim about the domain, not just the project

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
