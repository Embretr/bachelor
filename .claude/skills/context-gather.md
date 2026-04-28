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
| `context/docs/method/sources/raw/extracted/{bibkey}.md` | For each cite key — verified passages and application notes |
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
| `context/docs/method/academic-writing-guide.md` | Writing rules — load when writing any chapter |
| `context/docs/method/sustainability-analysis.md` | Load when writing Ch 5.5 (Sustainability) |
| `result/chapters/ch2/ch2-theory.tex` | Continuity |

---

## Chapter 4 — Findings

### Always load for any Ch 4 section
| File | Why |
|------|-----|
| `context/outline.md` — Ch 4 section | Section plan |
| `context/glossary.md` | Terminology |
| `result/chapters/ch3/ch3-method.tex` | Continuity |

### Section-specific critical context

| Section | Critical files | Optional files |
|---------|---------------|----------------|
| **4.1** Interview Findings | `context/interviews-summary.md`, `context/intervju/*.md` (individual transcripts) | — |
| **4.2** Requirements | `context/docs/requirements/functional-requirements.md`, `context/docs/requirements/non-functional-requirements.md` | `context/docs/requirements/requirements-traceability.md` |
| **4.3** Fit/Gap | `context/fitgap-summary.md`, `context/interviews-summary.md` | — |
| **4.4** System Description | `context/docs/tech/architecture.md`, `context/docs/tech/tech-stack.md`, `context/docs/tech/data-model.md` | `context/docs/tech/api-overview.md`, `context/docs/tech/codebase-overview.md`, `context/docs/user-research/ui-flow.md`, `context/docs/tech/flow-diagrams.md` |
| **4.5** Algorithm | `context/docs/tech/algorithm.md`, `context/docs/tech/benchmark-results.md` | — |

---

## Chapter 5 — Discussion

### Always load for any Ch 5 section
| File | Why |
|------|-----|
| `context/outline.md` — Ch 5 section | Section plan |
| `context/glossary.md` | Terminology |
| `result/chapters/ch2/ch2-theory.tex` | Theory to connect findings back to |
| `result/chapters/ch4/ch4-findings.tex` | The findings being interpreted |
| `evaluation/a-grade-rubric.md` — Ch 5 section | A criteria for discussion |

### Section-specific critical context

| Section | Critical files | Optional files |
|---------|---------------|----------------|
| **5.1** Pain Points | `context/interviews-summary.md`, `context/fitgap-summary.md` | — |
| **5.2** Algorithm & HITL | `context/docs/tech/algorithm.md`, `context/docs/tech/benchmark-results.md` | — |
| **5.3** Adoption Barriers | `context/interviews-summary.md` | `context/docs/user-research/user-tests.md` |
| **5.4** Tacit Knowledge | `context/interviews-summary.md` | — |
| **5.5** Sustainability | `context/docs/method/sustainability-analysis.md` | — |
| **5.6** Limitations | `context/docs/method/research-design.md`, `context/docs/project/risk-log.md` | `result/chapters/ch3/ch3-method.tex` |

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
| `evaluation/theory-usage.md` | Theory tracking — flag orphaned theories (Ch 5+) |
| All completed chapters in order | The full argument chain |
| The chapter being reviewed | The subject of review |

---

## For Quality Sessions

| File | Why |
|------|-----|
| `evaluation/a-grade-rubric.md` | Primary grading standard |
| `evaluation/grading-guidelines.md` | Official sensor criteria |
| `evaluation/theory-usage.md` | Theory tracking — verify connections |
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
