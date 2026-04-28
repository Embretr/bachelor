# Thesis Status — Ressursplanlegger

> Update this file after every writing session.
> Claude reads this at the start of every session.
> Last updated: 2026-04-23

---

## Context Files — Fill Status

| File | Owner | Status | Blocks |
|------|-------|--------|--------|
| `context/context.md` (master context) | Mikael | ✅ Complete | — |
| `context/context.md` — research question | Mikael | ✅ RQ + 3 sub-questions finalised | — |
| `context/thesis-spine.md` | Mikael | ✅ Approved draft — review after Ch 4 | — |
| `context/outline.md` | Mikael | ✅ Complete | — |
| `context/glossary.md` | Mikael | ✅ Filled | Add terms as needed |
| `context/scope.md` | Mikael | ✅ Filled | Confirm with Embret |
| `context/interviews-summary.md` | Mikael | ✅ Complete | — |
| `context/writing-style-examples.md` | Both | ⬜ Empty | Fill after first good section |
| `context/fitgap-summary.md` | Mikael | ✅ Filled (14 gaps, 5 fits, coverage matrix) | — |
| `context/docs/user-research/personas.md` | Mikael | ✅ Filled | — |
| `context/docs/user-research/user-tests.md` | Mikael | ⬜ Optional template | If empty, Ch 5.6 must state no formal user testing was conducted |
| `context/docs/user-research/ui-flow.md` | Embret | ✅ Filled | Verify against implementation/scope before Ch 4.4 |
| `context/docs/requirements/functional-requirements.md` | Mikael | ✅ Filled (42 requirements) | — |
| `context/docs/requirements/non-functional-requirements.md` | Embret | ✅ Filled | — |
| `context/docs/requirements/requirements-traceability.md` | Embret | ✅ Filled | — |
| `context/docs/method/research-design.md` | Mikael | ✅ Filled | Demo/eval phases still placeholder |
| `context/docs/method/theoretical-framework.md` | Mikael | ✅ Filled | Sources need reading confirmation |
| `context/docs/method/literature-list.md` | Mikael | ✅ 48 sources `approved-read` (2026-04-23) | — |
| `context/docs/tech/algorithm.md` | Embret | ✅ Filled | — |
| `context/docs/tech/architecture.md` | Embret | ✅ Filled | — |
| `context/docs/tech/data-model.md` | Embret | ✅ Filled | — |
| `context/docs/tech/benchmark-results.md` | Embret | ⬜ Template only | Blocks Ch 4.5 and Ch 5.2 |
| `context/docs/tech/api-overview.md` | Embret | ✅ Filled | Verify procedure names before Ch 4.4 |
| `context/docs/tech/tech-stack.md` | Embret | ✅ Filled | — |
| `context/docs/tech/codebase-overview.md` | Embret | ✅ Filled | Verify against actual codebase before Ch 4.4 |
| `context/docs/tech/flow-diagrams.md` | Embret | ✅ Filled | Verify before converting to thesis figures |
| `context/docs/project/sprint-log.md` | Both | ⬜ Template only | Blocks Ch 3.4 |
| `context/docs/project/decision-log.md` | Both | ⬜ Template only | Blocks Ch 3, 5 |
| `context/docs/project/change-log.md` | Both | ⬜ Template only | Blocks Ch 5, 6 |
| `context/docs/project/risk-log.md` | Both | ✅ Filled (10 risks) | — |
| `evaluation/a-grade-rubric.md` | Both | ✅ Complete | — |
| `evaluation/grading-guidelines.md` | Mikael | ✅ Filled (NRT criteria + NTNU-specific) | — |
| `evaluation/evaluation.md` | Both | ✅ Filled (chapter-level checklist) | — |
| `evaluation/source-requests.md` | Both | ✅ Active source queue | Resolve matching `SRC-xxx` requests before writing affected sections |

---

## Mikael's Remaining Tasks (context phase)

| Task | Priority | Status |
|------|:--------:|--------|
| Fill `context/fitgap-summary.md` | High | ✅ Done |
| Fill `evaluation/grading-guidelines.md` from PDF | High | ✅ Done |
| Fill `context/docs/project/sprint-log.md` retroactively | Medium | ⬜ Not started |
| Fill `context/docs/project/decision-log.md` | Medium | ⬜ Not started |
| Fill `context/writing-style-examples.md` (after first section) | Low | ⬜ Blocked |
| Fill `context/docs/user-research/user-tests.md` (if tests done) | Low | ⬜ Not started |
| Finalise research sub-questions in `context/context.md` | High | ✅ Done (3 sub-questions) |
| Read and confirm literature sources in `literature-list.md` | High | ✅ Done (48 approved 2026-04-23) |
| Resolve source requests for next section | High | ✅ Active queue empty |
| Fill research ethics details in `context/docs/method/research-design.md` | High | ⬜ Not started |
| Confirm scope.md with Embret | Medium | ⬜ Not started |

## Embret's Remaining Tasks (context phase)

| Task | Priority | Status |
|------|:--------:|--------|
| Fill `context/docs/tech/benchmark-results.md` | High | ⬜ Not started |
| Verify `context/docs/tech/api-overview.md` against implementation | Medium | ⬜ Not started |
| Verify `context/docs/tech/codebase-overview.md` against implementation | Medium | ⬜ Not started |
| Verify/update `context/docs/tech/flow-diagrams.md` | Medium | ⬜ Not started |
| Verify `context/docs/user-research/ui-flow.md` against implementation/scope | Medium | ⬜ Not started |
| Fill `context/docs/requirements/non-functional-requirements.md` | High | ✅ Done |
| Fill `context/docs/requirements/requirements-traceability.md` | High | ✅ Done |

---

## Chapter Writing Progress

Pipeline: `/write-section X.Y` (auto-revise up to 3 rounds + polish) → `/review-chapter N` → human approval.

Fixed pre-write activity: before any `/write-section`, resolve source requests for the next section in `evaluation/source-requests.md` and confirm all required citation keys are `approved-read` in `context/docs/method/literature-list.md` and present in `result/references.bib`.

### Status Legend
| Status | Meaning |
|--------|---------|
| `not started` | Section has no content |
| `drafted-needs-revision` | In progress — auto-revise is handling this |
| `drafted-needs-manual-fix` | Pipeline exhausted auto-fix (3 rounds or no fixable issues). Human must intervene. |
| `drafted-reviewed` | All gates passed. Ready for next section or chapter review. |
| `candidate-approved` | Chapter-level review passed. Awaiting human approval. |
| `approved` | Human approved. |

### Chapter 2 — Theory
| Section | Written | Checks | Coherence | Quality | Naturalness | Status |
|---------|:-------:|:------:|:---------:|:-------:|:-----------:|--------|
| 2.1 | ⬜ | — | — | — | — | not started |
| 2.2 | ⬜ | — | — | — | — | not started |
| 2.3 | ⬜ | — | — | — | — | not started |
| 2.4 | ⬜ | — | — | — | — | not started |
Chapter integration: not started (reset 2026-04-23; will be rewritten with new 48-source set)

### Chapter 3 — Methodology
| Section | Written | Checks | Coherence | Quality | Naturalness | Status |
|---------|:-------:|:------:|:---------:|:-------:|:-----------:|--------|
| 3.1 | ⬜ | — | — | — | — | not started |
| 3.2 | ⬜ | — | — | — | — | not started |
| 3.3 | ⬜ | — | — | — | — | not started |
| 3.4 | ⬜ | — | — | — | — | not started |
| 3.5 | ⬜ | — | — | — | — | not started |
Chapter integration: not started (reset 2026-04-23; will be rewritten with new 48-source set)

### Chapter 4 — Findings
| Section | Written | Checks | Coherence | Quality | Naturalness | Status |
|---------|:-------:|:------:|:---------:|:-------:|:-----------:|--------|
| 4.1 | ⬜ | — | — | — | — | not started |
| 4.2 | ⬜ | — | — | — | — | not started |
| 4.3 | ⬜ | — | — | — | — | not started |
| 4.4 | ⬜ | — | — | — | — | not started |
| 4.5 | ⬜ | — | — | — | — | not started |
Chapter integration: not started

### Chapter 5 — Discussion
| Section | Written | Checks | Coherence | Quality | Naturalness | Status |
|---------|:-------:|:------:|:---------:|:-------:|:-----------:|--------|
| 5.1 | ⬜ | — | — | — | — | not started |
| 5.2 | ⬜ | — | — | — | — | not started |
| 5.3 | ⬜ | — | — | — | — | not started |
| 5.4 | ⬜ | — | — | — | — | not started |
| 5.5 | ⬜ | — | — | — | — | not started |
| 5.6 | ⬜ | — | — | — | — | not started |
Chapter integration: not started

### Chapter 1 — Introduction (write after Ch 2–5)
| Section | Written | Checks | Coherence | Quality | Naturalness | Status |
|---------|:-------:|:------:|:---------:|:-------:|:-----------:|--------|
| 1.1 | ⬜ | — | — | — | — | not started |
| 1.2 | ⬜ | — | — | — | — | not started |
| 1.3 | ⬜ | — | — | — | — | not started |
| 1.4 | ⬜ | — | — | — | — | not started |
Chapter integration: not started

### Chapter 6 — Conclusion (write last)
| Section | Written | Checks | Coherence | Quality | Naturalness | Status |
|---------|:-------:|:------:|:---------:|:-------:|:-----------:|--------|
| 6.1 | ⬜ | — | — | — | — | not started |
| 6.2 | ⬜ | — | — | — | — | not started |
| 6.3 | ⬜ | — | — | — | — | not started |
Chapter integration: not started

---

## Critical Path

Before writing starts, these must be done:

```
✅ context/context.md — master context (Mikael)           → done
✅ context/glossary.md (Mikael)                            → done
✅ context/scope.md (Mikael)                               → done, needs Embret confirmation
✅ context/docs/tech/algorithm.md (Embret)                 → done
✅ context/docs/tech/architecture.md (Embret)              → done
✅ evaluation/grading-guidelines.md (Mikael)               → done
✅ context/fitgap-summary.md (Mikael)                      → done
✅ context/docs/requirements/non-functional-requirements.md (Embret) → done
✅ result/references.bib                                    → 17 entries
✅ evaluation/source-requests.md                            → SRC-001 to SRC-005 resolved; active queue empty
✅ context/docs/method/literature-list.md                    → 48 sources approved-read (2026-04-23)
⬜ context/docs/tech/benchmark-results.md                    → blocks Ch 4.5 and Ch 5.2
⬜ context/docs/method/research-design.md ethics/duration    → blocks Ch 3.2
⬜ context/docs/project/sprint-log.md                        → blocks Ch 3.4
⬜ context/docs/project/decision-log.md                      → blocks Ch 3.4 and Ch 5
⬜ context/docs/project/change-log.md                        → blocks Ch 5 and Ch 6
```

With the strengthened readiness gate, writing can only start when each section's MUST markers have concrete, `approved-read` citation keys and filled evidence files.
Immediate known blockers:
- Ch 2 source readiness is blocked until required theory/HITL/TMS sources are `approved-read`.
- Ch 3.2 source readiness is blocked until qualitative interview methodology sources are `approved-read`.
- Ch 3.4 source readiness is blocked until agile/iterative development sources are `approved-read`.
- Ch 4.5 source readiness is blocked until solver/OR-Tools/constraint programming sources are `approved-read`.
- Ch 5.5 source readiness is blocked until sustainability/SusAF/SDG sources are `approved-read`.
- Ch 2.2, 2.3, 3.4, and 4.5 need concrete source keys with `approved-read` status before writing.
- Ch 3.2 needs interview duration and research ethics details.
- Ch 3.4 needs sprint-log/decision-log context.
- Ch 4.2 needs requirement-ID consistency between requirements and traceability.
- Ch 4.5 and Ch 5.2 need benchmark-results context.
- Ch 5.6 may proceed without user tests, but must explicitly state this limitation if `user-tests.md` remains empty.
