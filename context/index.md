# Context Index — What Exists and When to Load It

> Claude reads this first in every session.
> Use it to decide which files to load for the current task.
> Do not read every file — load only what is relevant.

---

## Always Load (every session, every task)

| File | Content | Status |
|------|---------|--------|
| `context/context.md` | Thesis identity, research question, tech stack, scope summary, chapter status | Partially filled — RQ still placeholder |
| `context/thesis-spine.md` | One sentence per chapter describing its argument contribution | Draft — review after RQ is finalised |

---

## Load When Writing (load before starting any chapter)

| File | Content | Load for |
|------|---------|----------|
| `context/outline.md` | Section-level outlines with content notes and word targets | All chapters |
| `context/glossary.md` | Domain glossary — only use these terms | All chapters |
| `context/scope.md` | What is explicitly in/out of scope | All chapters |
| `context/writing-style-examples.md` | Approved passages for tone and voice matching | All chapters (once filled) |

---

## Chapter-Specific Context

| File | Content | Load for |
|------|---------|----------|
| `context/interviews-summary.md` | Distilled findings from 7 interviews — pain points, ranking, attitudes | Ch 1, 3, 4, 5 |
| `context/fitgap-summary.md` | Fit/gap analysis comparing current systems to needs | Ch 4.3 |
| `context/docs/requirements/functional-requirements.md` | Functional requirements (MoSCoW + source) | Ch 4.2 |
| `context/docs/requirements/non-functional-requirements.md` | Non-functional requirements | Ch 4.2 |
| `context/docs/requirements/requirements-traceability.md` | Which requirements are implemented and tested | Ch 4.2, 5 |
| `context/docs/method/research-design.md` | Chosen research method with justification | Ch 3.1 |
| `context/docs/method/literature-list.md` | Sources read — feeds references.bib | Ch 2, 3 |
| `context/docs/method/theoretical-framework.md` | VRP, human-in-the-loop, resource scheduling theory notes | Ch 2 |
| `context/docs/project/sprint-log.md` | Weekly progress log | Ch 3.4 |
| `context/docs/project/decision-log.md` | Key technical and methodological decisions | Ch 3, 5 |
| `context/docs/project/change-log.md` | Evolution from early MVP to current system | Ch 5, 6 |
| `context/docs/tech/algorithm.md` | Algorithm: input, output, constraints, method, limitations | Ch 4.5, 5.2 |
| `context/docs/tech/architecture.md` | System architecture: frontend, backend, database, hosting | Ch 4.4 |
| `context/docs/tech/data-model.md` | Database schema and entity relations | Ch 4.4 |
| `context/docs/tech/api-overview.md` | API endpoints | Ch 4.4 |
| `context/docs/tech/tech-stack.md` | Technology choices with justifications | Ch 4.4 |
| `context/docs/tech/flow-diagrams.md` | Mermaid flow diagrams for key system flows | Ch 4.4 |
| `context/docs/tech/codebase-overview.md` | Directory structure, key files, external dependencies | Ch 4.4 |
| `context/docs/user-research/personas.md` | User roles: traffic coordinator, transport manager, driver | Ch 4.1, 4.4 |
| `context/docs/user-research/user-tests.md` | User testing feedback (if conducted) | Ch 5.3, 5.5 |
| `context/docs/user-research/ui-flow.md` | Screen-by-screen UI walkthrough | Ch 4.4 |
| `context/docs/project/risk-log.md` | Identified risks and mitigation | Ch 3.5, 5.5 |

---

## Evaluation Files (load before self-evaluating any output)

| File | Content | When |
|------|---------|------|
| `evaluation/a-grade-rubric.md` | Detailed A criteria per chapter — primary quality gate | Before every output |
| `evaluation/evaluation.md` | Chapter-level checklist | Before every output |
| `evaluation/grading-guidelines.md` | Official sensor guidelines | When doing quality check |
| `evaluation/workflow-improvements.md` | Log of proposed and applied workflow changes | After every task |

---

## Context File Status

Files are filled in varying degrees. Use this to know what can be relied upon:

| File | Fill Status | Notes |
|------|------------|-------|
| `context/context.md` | ~70% | RQ, tech stack, chapter status need filling |
| `context/thesis-spine.md` | Draft | Review when RQ finalised |
| `context/outline.md` | Complete | Detailed section plans ready for all 6 chapters |
| `context/glossary.md` | Template ready | Fill in before writing starts |
| `context/scope.md` | Template ready | Fill in before writing starts |
| `context/writing-style-examples.md` | Empty | Fill after first good section is written |
| `context/interviews-summary.md` | Complete | 7 interviews distilled |
| `context/fitgap-summary.md` | Unknown | Check before writing ch4 |
| `context/docs/requirements/functional-requirements.md` | Empty template | Mikael to fill from interviews |
| `context/docs/tech/algorithm.md` | Empty template | Embret to fill — blocks ch4.5 |
| `context/docs/tech/architecture.md` | Empty template | Embret to fill — blocks ch4.4 |
| `context/docs/tech/codebase-overview.md` | Empty template | Embret to fill |
| `context/docs/tech/flow-diagrams.md` | Draft diagrams | Embret to verify/update |
| `context/docs/user-research/personas.md` | Empty template | Mikael to fill from interviews |
| `context/docs/user-research/user-tests.md` | Empty template | Mikael to fill |
| `context/docs/user-research/ui-flow.md` | Empty template | Embret to fill |
| `context/docs/project/risk-log.md` | Draft entries | Both to verify and extend |
| `evaluation/grading-guidelines.md` | Empty | Mikael to fill from PDF |
| `evaluation/a-grade-rubric.md` | Complete | General NTNU A criteria — use until PDF is filled |

---

## Quick Load Guide Per Chapter

```
Ch 1 — Introduction:
  context.md + thesis-spine.md + outline.md + scope.md + glossary.md + interviews-summary.md

Ch 2 — Theory:
  context.md + thesis-spine.md + outline.md + glossary.md
  + docs/method/theoretical-framework.md + docs/method/literature-list.md

Ch 3 — Methodology:
  context.md + thesis-spine.md + outline.md + glossary.md
  + docs/method/research-design.md + docs/project/sprint-log.md + interviews-summary.md

Ch 4 — Findings:
  context.md + thesis-spine.md + outline.md + glossary.md
  + interviews-summary.md + fitgap-summary.md
  + docs/requirements/functional-requirements.md + docs/requirements/non-functional-requirements.md
  + docs/tech/algorithm.md + docs/tech/architecture.md + docs/tech/tech-stack.md

Ch 5 — Discussion:
  context.md + thesis-spine.md + outline.md + glossary.md
  + All completed chapter .tex files
  + evaluation/a-grade-rubric.md + evaluation/grading-guidelines.md

Ch 6 — Conclusion:
  context.md + thesis-spine.md + glossary.md
  + All completed chapter .tex files
  + evaluation/a-grade-rubric.md
```
