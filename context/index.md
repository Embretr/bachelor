# Context Index — What Exists and When to Load It

> Claude reads this first in every session.
> Use it to decide which files to load for the current task.
> Do not read every file — load only what is relevant.

---

## Always Load (every session, every task)

| File | Content | Status |
|------|---------|--------|
| `context/context.md` | Thesis identity, research question, tech stack, scope summary | ✅ Complete — RQ + 3 sub-questions |
| `context/thesis-spine.md` | One sentence per chapter describing its argument contribution | ✅ Approved draft — review after Ch 4 |

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
| `context/current-practice.md` | How traffic coordinators do resource planning today — workflow, tooling, gaps | Ch 1, 4.1, 4.3, 5.1 |
| `context/fitgap-summary.md` | Fit/gap analysis comparing current systems to needs | Ch 4.3 |
| `context/docs/requirements/functional-requirements.md` | Functional requirements (MoSCoW + source) | Ch 4.2 |
| `context/docs/requirements/non-functional-requirements.md` | Non-functional requirements | Ch 4.2 |
| `context/docs/requirements/requirements-traceability.md` | Which requirements are implemented and tested | Ch 4.2, 5 |
| `context/docs/method/research-design.md` | Chosen research method with justification | Ch 3.1 |
| `context/docs/method/CITATIONS.md` | Empty during extraction; populated from extracted source notes after all sources are done | After extractions |
| `context/docs/method/sources/raw/extracted/{bibkey}.md` | Verified source notes — read for each cite key | All chapters |
| `context/docs/method/theoretical-framework.md` | Resource scheduling, constraint programming, human-in-the-loop, TMS, DSR theory notes | Ch 2 |
| `context/docs/project/sprint-log.md` | Weekly progress log | Ch 3.4 |
| `context/docs/project/decision-log.md` | Key technical and methodological decisions | Ch 3, 5 |
| `context/docs/method/decision-making.md` | Decision-making framework, criteria, roles, trade-offs, threats | Ch 3.4, 3.5, 5 |
| `context/docs/project/change-log.md` | Evolution from early MVP to current system | Ch 5, 6 |
| `context/docs/tech/algorithm.md` | Algorithm: input, output, constraints, method, limitations | Ch 4.5, 5.2 |
| `context/docs/tech/benchmark-results.md` | Solver benchmark datasets, runtime, solution quality, limitations | Ch 4.5, 5.2 |
| `context/docs/tech/architecture.md` | System architecture: frontend, backend, database, hosting | Ch 4.4 |
| `context/docs/tech/data-model.md` | Database schema and entity relations | Ch 4.4 |
| `context/docs/tech/api-overview.md` | API endpoints | Ch 4.4 |
| `context/docs/tech/tech-stack.md` | Technology choices with justifications | Ch 4.4 |
| `context/docs/tech/flow-diagrams.md` | Mermaid flow diagrams for key system flows | Ch 4.4 |
| `context/docs/tech/codebase-overview.md` | Directory structure, key files, external dependencies | Ch 4.4 |
| `context/intervju/` | Full interview transcriptions (7 files) + summary | Ch 4.1 — primary data source |
| `context/docs/user-research/personas.md` | User roles: traffic coordinator, transport manager, driver | Ch 4.1, 4.4 |
| `context/docs/user-research/user-tests.md` | User testing feedback (if conducted) | Ch 5.3 |
| `context/docs/user-research/ui-flow.md` | Screen-by-screen UI walkthrough | Ch 4.4 |
| `context/docs/project/risk-log.md` | Identified risks and mitigation | Ch 3.5, 5.6 |
| `context/docs/method/sustainability-analysis.md` | SusAF analysis, SDG mapping, dilemmas, writing guide | Ch 5.5 |
| `context/docs/method/academic-writing-guide.md` | Writing rules: paragraph structure, flow, action levels, language | All chapters |
| `context/docs/method/academic-phrases.md` | Phrase bank for academic writing — transitions, hedging, argumentation, conclusions | Reference when writing — not loaded routinely |

---

## Evaluation Files (load before self-evaluating any output)

| File | Content | When |
|------|---------|------|
| `evaluation/a-grade-rubric.md` | Detailed A criteria per chapter — primary quality gate | Before every output |
| `evaluation/evaluation.md` | Chapter-level checklist | Before every output |
| `evaluation/grading-guidelines.md` | Official sensor guidelines | When doing quality check |
| `evaluation/workflow-improvements.md` | Log of proposed and applied workflow changes | After every task |
| `evaluation/formal-requirements.md` | Deliverables, deadlines, AI policy, contribution attribution | Final submission checklist only — not loaded during writing |
| `evaluation/theory-usage.md` | Theory tracking matrix — which theories from Ch 2 are used where | Red-thread/quality checks for Ch 5+ |

---

## Fixed Pre-Write Activities

Before `/write-section X.Y`, always:

1. Confirm `context/outline.md` has a concrete paragraph-level plan for the section.
2. Confirm every required citation key has a verified source notes file at `context/docs/method/sources/raw/extracted/{bibkey}.md` and is present in `result/references.bib`.
3. Confirm section-specific evidence files are filled and not template-only.

Missing source notes block thesis writing.

---

## Context File Status

Files are filled in varying degrees. Use this to know what can be relied upon:

| File | Fill Status | Notes |
|------|------------|-------|
| `context/context.md` | ✅ Complete | RQ + 3 sub-questions, tech stack, system description |
| `context/thesis-spine.md` | ✅ Approved draft | Review after Ch 4 is drafted |
| `context/outline.md` | ✅ Complete | Paragraph-level plans for Ch 1–6; includes readiness markers |
| `context/glossary.md` | ✅ Filled | Core terms + algorithm + system terms |
| `context/scope.md` | ✅ Filled | Needs Embret confirmation |
| `context/writing-style-examples.md` | ⬜ Empty | Fill after first good section is written |
| `context/interviews-summary.md` | ✅ Complete | 7 interviews distilled + per-company operational details |
| `context/current-practice.md` | ✅ Filled | Workflow + gaps in current resource planning, reconstructed from 7 interviews |
| `context/fitgap-summary.md` | ✅ Filled | 14 gaps, 5 fits, coverage matrix |
| `context/docs/requirements/functional-requirements.md` | ✅ Filled | 42 requirements with MoSCoW and implementation status |
| `context/docs/requirements/non-functional-requirements.md` | ✅ Filled | Embret — 9+ NFRs with targets |
| `context/docs/requirements/requirements-traceability.md` | ✅ Filled | Embret — implementation + test status |
| `context/docs/method/sources/raw/extracted/` | ⬜ 0 of 48 source notes generated | Each cite key needs verified notes before its section can be written |
| `context/docs/tech/algorithm.md` | ✅ Filled | Embret — 3 solvers, constraints, scoring |
| `context/docs/tech/architecture.md` | ✅ Filled | Embret — full architecture with diagrams |
| `context/docs/tech/tech-stack.md` | ✅ Filled | Embret — all layers with justification |
| `context/docs/tech/data-model.md` | ✅ Filled | Embret — entity relationships |
| `context/docs/tech/benchmark-results.md` | ⬜ Template | Blocks Ch 4.5 and Ch 5.2 until benchmark numbers are filled |
| `context/docs/tech/codebase-overview.md` | ✅ Filled | Verify against actual codebase before Ch 4.4 |
| `context/docs/tech/flow-diagrams.md` | ✅ Filled | Verify before converting diagrams to thesis figures |
| `context/docs/tech/api-overview.md` | ✅ Filled | Verify procedure names before Ch 4.4 |
| `context/docs/user-research/personas.md` | ✅ Filled | 4 user roles from interviews |
| `context/docs/user-research/user-tests.md` | ⬜ Optional template | Fill if user tests are conducted; if empty, Ch 5.6 must state this limitation |
| `context/docs/user-research/ui-flow.md` | ✅ Filled | Verify against implemented UI and scope before Ch 4.4 |
| `context/docs/project/risk-log.md` | ✅ Filled | 10 risks |
| `context/docs/project/sprint-log.md` | ⬜ Template | Both — fill retroactively for Ch 3.4 |
| `context/docs/project/decision-log.md` | ⬜ Template | Both — fill for Ch 3.4 and Ch 5 |
| `context/docs/method/decision-making.md` | ✅ Filled (framework + threats) | Both — confirm cadence + add examples |
| `context/docs/project/change-log.md` | ⬜ Template | Both — fill for Ch 5 and Ch 6 |
| `evaluation/grading-guidelines.md` | ✅ Filled | NRT criteria + NTNU-specific + weighting |
| `evaluation/a-grade-rubric.md` | ✅ Complete | A criteria per chapter |
| `evaluation/evaluation.md` | ✅ Filled | Chapter-level checklist with sensor questions |
| `context/docs/method/CITATIONS.md` | ⬜ Empty during extraction phase | Will be assembled from extracted source notes after all 48 sources done; backup at `CITATIONS-pre-extraction-backup.md` |
| `evaluation/formal-requirements.md` | ✅ Filled | Deliverables, deadlines, documentation |

---

## Quick Load Guide Per Chapter

```
Ch 1 — Introduction:
  context.md + thesis-spine.md + outline.md + scope.md + glossary.md + interviews-summary.md

Ch 2 — Theory:
  context.md + thesis-spine.md + outline.md + glossary.md
  + docs/method/theoretical-framework.md
  + docs/method/sources/raw/extracted/{bibkey}.md (per cite key in section — once extracted)

Ch 3 — Methodology:
  context.md + thesis-spine.md + outline.md + glossary.md
  + docs/method/research-design.md + docs/method/decision-making.md
  + docs/project/sprint-log.md + docs/project/decision-log.md + interviews-summary.md
  + docs/method/sources/raw/extracted/{bibkey}.md (per cite key — once extracted)

Ch 4 — Findings:
  context.md + thesis-spine.md + outline.md + glossary.md
  + interviews-summary.md + fitgap-summary.md
  + docs/requirements/functional-requirements.md + docs/requirements/non-functional-requirements.md
  + docs/tech/algorithm.md + docs/tech/benchmark-results.md
  + docs/tech/architecture.md + docs/tech/tech-stack.md
  + docs/method/sources/raw/extracted/{bibkey}.md (per cite key — once extracted)

Ch 5 — Discussion:
  context.md + thesis-spine.md + outline.md + glossary.md
  + docs/tech/benchmark-results.md for 5.2
  + docs/method/sources/raw/extracted/{bibkey}.md (per cite key — once extracted)
  + All completed chapter .tex files
  + evaluation/a-grade-rubric.md + evaluation/grading-guidelines.md

Ch 6 — Conclusion:
  context.md + thesis-spine.md + glossary.md
  + All completed chapter .tex files
  + evaluation/a-grade-rubric.md
```
