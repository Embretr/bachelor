# Chapter-Level Evaluation Checklist — Ressursplanlegger

> The quality agent reads this before and after reviewing any chapter.
> Based on: NRT grading criteria (grading-guidelines.md), A-grade rubric (a-grade-rubric.md),
> Malterud's four criteria, and NTNU-specific requirements.

---

## All Chapters

- [ ] Formal, academic English — no filler words, no "we believe"
- [ ] Every claim has a citation or is grounded in own data
- [ ] Consistent terminology from `context/glossary.md` — no synonyms introduced
- [ ] Correct APA 7 citations (`\parencite{}` / `\textcite{}`)
- [ ] Every paragraph has a clear topic sentence
- [ ] Transitions between paragraphs and sections are explicit
- [ ] Tense is consistent (present for theory, past for what was done)
- [ ] Section serves its chapter's thesis-spine sentence
- [ ] No scope creep — nothing outside `context/scope.md`

---

## Chapter 1 — Introduction

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Problem is clearly motivated — reader understands *why* this matters | A non-expert should grasp the problem after reading 1.1 |
| [ ] | Research question is stated precisely | Verbatim from `context/context.md` |
| [ ] | Three sub-questions are listed with brief explanation | Match context.md |
| [ ] | Scope is precisely delimited — in/out is unambiguous | Cross-check with `context/scope.md` |
| [ ] | Division of work stated (who did what) | Mikael: user research. Embret: development. |
| [ ] | Reader guide matches thesis-spine | One sentence per chapter, consistent |
| [ ] | Ressursplanlegger is introduced clearly in one paragraph | Not too detailed — that is Ch 4 |

---

## Chapter 2 — Theory

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | VRP defined and connected to this project's problem | Not just textbook VRP — mapped to driver/vehicle assignment |
| [ ] | HITL/automation levels discussed with source | Parasuraman (2000), Sheridan & Verplank (1978) |
| [ ] | TMS landscape described factually | Timpex, Trimtex, Opptur — what they do and don't do |
| [ ] | DSR methodology introduced with citations | Hevner (2004), Peffers (2007), Wieringa (2014) |
| [ ] | **Every theory introduced is used later** in Ch 4 or Ch 5 | If a theory is not referenced again, remove it |
| [ ] | Theory chapter is "pure" — no own empirical data mixed in | Findings belong in Ch 4, not here |
| [ ] | Related work is woven into sections, not a thin standalone section | Integrated into 2.1 and 2.2 |

---

## Chapter 3 — Methodology

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | DSR choice is justified — not just stated | Why DSR and not case study? Why not pure quantitative? |
| [ ] | DSR phases mapped to this project in a table | Peffers' six phases → what was done |
| [ ] | Interview process documented precisely enough to reproduce | Who, when, how many, how long, what questions, how transcribed |
| [ ] | Thematic analysis method described with citation | Braun & Clarke (2006) |
| [ ] | Validation vs evaluation distinction made explicit | Wieringa (2014) — we validate, not evaluate |
| [ ] | Malterud's four criteria addressed | Systematic reflection, relevance, validity, reflexivity |
| [ ] | Researcher bias acknowledged and mitigated | Dev team = research team → confirmation bias risk |
| [ ] | Ethical considerations mentioned | Consent, anonymisation, data handling |
| [ ] | Limitations stated honestly — not buried | Sample size, no production deployment, single-day interviews |

---

## Chapter 4 — Findings

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Interview findings presented thematically, not per-company | Themes across companies, not 7 separate summaries |
| [ ] | Findings are *presented*, not *interpreted* | Interpretation belongs in Ch 5 |
| [ ] | Requirements table with MoSCoW, source, and implementation status | Cross-check with `functional-requirements.md` |
| [ ] | Fit/gap analysis is clear — what existing systems do/don't do | Feature coverage matrix from `fitgap-summary.md` |
| [ ] | System description is technical but accessible | Architecture, data model, key components — not a code walkthrough |
| [ ] | Algorithm is documented: input, output, constraints, solvers | Reference `context/docs/tech/algorithm.md` |
| [ ] | Multi-engine comparison explained — why three solvers? | Greedy (speed), CP-SAT (quality), Timefold (scale) |
| [ ] | Conflict detection system described | What conflicts are detected, how they are displayed |

---

## Chapter 5 — Discussion

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | **Discusses, not just presents** — weighs multiple perspectives | Writing action level = "drøfte" — must argue, compare, evaluate |
| [ ] | Findings connected back to theory from Ch 2 | VRP theory → algorithm results. HITL theory → override design. |
| [ ] | Research question addressed — reader can see the answer forming | Each sub-question should be implicitly answered by the end of Ch 5 |
| [ ] | Adoption barriers discussed honestly | Invoicing gap, trust, cost, training |
| [ ] | Tacit knowledge dilemma explored | System captures some but not all — what are the implications? |
| [ ] | Sustainability section uses SusAF framework | 5 dimensions, 3 effect levels, effects table, SDG mapping |
| [ ] | Sustainability dilemmas discussed — not just positive effects | Efficiency vs deskilling, automation vs autonomy |
| [ ] | Ethical perspective included | Algorithmic fairness, accountability, privacy |
| [ ] | Limitations are specific, not generic | Not "more interviews would be better" but *why* and *what it means* |
| [ ] | Validation framing used — not evaluation claims | "The validation suggests..." not "The system proves..." |

---

## Chapter 6 — Conclusion

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Main RQ answered directly — one clear paragraph | Verbatim question, then answer |
| [ ] | All three sub-questions answered explicitly | SQ1, SQ2, SQ3 — each addressed |
| [ ] | Mirrors the introduction — reader sees the full arc | Start broad in Ch 1, end broad in Ch 6 |
| [ ] | No new information introduced | Conclusion summarises and concludes, nothing new |
| [ ] | Contributions stated clearly | What does this thesis add? (artefact + knowledge) |
| [ ] | Future work is concrete and reasoned | Not a wish list — specific next steps with justification |
| [ ] | Tone is appropriately confident but not overstated | "The thesis demonstrates..." not "The thesis proves..." |

---

## Cross-Chapter Checks (run after all chapters are drafted)

- [ ] **Red thread:** Does the argument flow logically from Ch 1 → 6? Does every chapter serve its spine sentence?
- [ ] **No orphaned theory:** Is every concept from Ch 2 referenced in Ch 4 or 5?
- [ ] **No unsupported claims in Ch 5:** Is every discussion point grounded in a finding from Ch 4?
- [ ] **Consistent terminology:** Are the same terms used throughout? (Check glossary)
- [ ] **Citation balance:** Are there chapters with suspiciously few or many citations?
- [ ] **Scope adherence:** Does any chapter describe features not in `context/scope.md`?
- [ ] **Contribution clarity:** Can a reader tell what Mikael did vs. Embret vs. what the system does?
