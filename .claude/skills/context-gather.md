# Context Gather — Which Files to Load Per Chapter

> Use context/index.md for the canonical, up-to-date file map.
> This file is the detailed reference for context loading decisions.

---

## Always Load (every session)

| File | Why |
|------|-----|
| `context/context.md` | Thesis identity, RQ, scope, system description |
| `context/thesis-spine.md` | The backbone — every section must serve this |
| `evaluation/a-grade-rubric.md` | A criteria — read before every output |
| `STATUS.md` | Current progress — avoid writing what is already done |

---

## Chapter 1 — Introduction

| File | Why |
|------|-----|
| `context/outline.md` — Ch 1 section | Section plan with content notes |
| `context/scope.md` | Needed to write 1.3 accurately |
| `context/glossary.md` | Terminology for consistent use |
| `context/interviews-summary.md` | Motivation for section 1.1 |

---

## Chapter 2 — Theory

| File | Why |
|------|-----|
| `context/outline.md` — Ch 2 section | Section plan |
| `context/glossary.md` | Terminology |
| `context/docs/method/theoretical-framework.md` | Theory notes to expand into the chapter |
| `context/docs/method/literature-list.md` | Sources available for citation |
| `result/references.bib` | BibTeX keys for `\parencite{}` |
| `result/chapters/ch1/ch1-introduction.tex` | Continuity — Ch 2 must build on Ch 1 |

---

## Chapter 3 — Methodology

| File | Why |
|------|-----|
| `context/outline.md` — Ch 3 section | Section plan |
| `context/glossary.md` | Terminology |
| `context/docs/method/research-design.md` | Research method documentation |
| `context/docs/project/sprint-log.md` | Development process for section 3.4 |
| `context/interviews-summary.md` | Interview process details for sections 3.2–3.3 |
| `result/chapters/ch2/ch2-theory.tex` | Continuity |

---

## Chapter 4 — Findings

| File | Why |
|------|-----|
| `context/outline.md` — Ch 4 section | Section plan |
| `context/glossary.md` | Terminology |
| `context/interviews-summary.md` | Source for sections 4.1 |
| `context/fitgap-summary.md` | Source for section 4.3 |
| `context/docs/requirements/functional-requirements.md` | Source for section 4.2 |
| `context/docs/requirements/non-functional-requirements.md` | Source for section 4.2 |
| `context/docs/tech/architecture.md` | Source for section 4.4 |
| `context/docs/tech/algorithm.md` | Source for section 4.5 — Embret must fill this first |
| `context/docs/tech/tech-stack.md` | Supporting context for section 4.4 |
| `context/docs/tech/data-model.md` | Supporting context for section 4.4 |
| `result/chapters/ch3/ch3-method.tex` | Continuity |

---

## Chapter 5 — Discussion

| File | Why |
|------|-----|
| `context/outline.md` — Ch 5 section | Section plan |
| `context/glossary.md` | Terminology |
| `result/chapters/ch1/ch1-introduction.tex` | Research question and motivation |
| `result/chapters/ch2/ch2-theory.tex` | Theory to connect findings back to |
| `result/chapters/ch3/ch3-method.tex` | Method limitations for section 5.5 |
| `result/chapters/ch4/ch4-findings.tex` | The findings being interpreted |
| `evaluation/a-grade-rubric.md` — Ch 5 section | A criteria for discussion |
| `evaluation/grading-guidelines.md` | Ensure discussion meets grading criteria |

---

## Chapter 6 — Conclusion

| File | Why |
|------|-----|
| `context/outline.md` — Ch 6 section | Section plan |
| `context/thesis-spine.md` | Answers must match the backbone |
| All completed `result/chapters/` files | Must summarise the whole thesis |
| `context/context.md` | Research questions must be answered verbatim |
| `evaluation/a-grade-rubric.md` — Ch 6 section | A criteria for conclusion |
| `evaluation/grading-guidelines.md` | Conclusion is a graded criterion |
| `evaluation/review/redthread-ch*.md` | Issues found — ensure they are resolved |
| `evaluation/review/quality-ch*.md` | Quality findings — ensure they are resolved |

---

## For Red-Thread Sessions

| File | Why |
|------|-----|
| `context/thesis-spine.md` | The coherence standard |
| `context/context.md` | The research question |
| All completed chapters in order | The full argument chain |
| The chapter being reviewed | The subject of review |

---

## For Quality Sessions

| File | Why |
|------|-----|
| `evaluation/a-grade-rubric.md` | Primary grading standard |
| `evaluation/grading-guidelines.md` | Official sensor criteria |
| `context/thesis-spine.md` | Coherence context |
| `context/context.md` | Thesis identity and RQ |
| All completed chapters | Full thesis context |
| The chapter being reviewed | The subject of review |

---

## Practical Notes

- Do not paste more than 4–5 files in one session — long context degrades Claude's focus
- For Chapter 5+, paste only the most relevant 2–3 chapters rather than all of them
- Always paste the previous chapter for continuity — this is the single highest-impact action
- If Claude seems to lose track of earlier instructions, start a new session with fewer files
