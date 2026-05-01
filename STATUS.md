# Thesis Status — Ressursplanlegger

> Update this file after every writing session.
> Claude reads this at the start of every session.
> Last updated: 2026-05-01 — bib refactor + outline marker additions per `context/docs/method/source-fitting-plan.md`: REPLACE malterud2017kvalitative→malterud2001lancet; ADD flotve2025transportytelser, polanyi1966tacit, orlikowski1991studying, venkatesh2003utaut, mietzner2009variability; DROP larman2003iterative, beck2001manifesto, wced1987commonfuture, hilty2015ict4s, eu2024aiact, walsham1995interpretive, seyff2022mapping, jobin2019landscape, jensen2014norsktransport. Bib now 43 entries (was 48). 14 new MUST CITE markers in outline.md. Chapter scaffolding (.tex) restructured to match new outline (Ch 1 §1.2 added, Ch 4 §4.6+§4.7 added, Ch 5 anchor-organised with §5.1.1/5.1.2/5.1.3 + §5.5/§5.6 + Ch 3 8-subsection iteration scaffold).

---

## Context Files — Fill Status

| File | Owner | Status | Blocks |
|------|-------|--------|--------|
| `context/context.md` (master context) | Mikael | ✅ Complete | — |
| `context/context.md` — research question | Mikael | ✅ RQ + 3 sub-questions finalised | — |
| `context/thesis-spine.md` | Mikael | ✅ Approved draft — review after Ch 4 | — |
| `context/outline.md` | Mikael | ✅ Restructured 2026-04-30 (Phase 5 / Task 12) | Source-fitting task pending — type-based MUST CITE / MUST EVIDENCE markers need bib-key / evidence-path resolution before any section can be written |
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
| `context/docs/method/sources/raw/extracted/` | Mikael + agent | ✅ 39 of 39 source notes generated | All extractions complete after Polanyi/Nonaka drop |
| `context/docs/tech/algorithm.md` | Embret | ✅ Filled | — |
| `context/docs/tech/architecture.md` | Embret | ✅ Filled | — |
| `context/docs/tech/data-model.md` | Embret | ✅ Filled | — |
| `context/docs/tech/benchmark-results.md` | Embret | ⬜ Template only | Blocks Ch 4.5 and Ch 5.2 |
| `context/docs/tech/api-overview.md` | Embret | ✅ Filled | Verify procedure names before Ch 4.4 |
| `context/docs/tech/tech-stack.md` | Embret | ✅ Filled | — |
| `context/docs/tech/codebase-overview.md` | Embret | ✅ Filled | Verify against actual codebase before Ch 4.4 |
| `context/docs/tech/flow-diagrams.md` | Embret | ✅ Filled | Verify before converting to thesis figures |
| `context/docs/project/sprint-log.md` | Both | ✅ Filled (8 iteration narratives per §3.5) | — |
| `context/docs/project/decision-log.md` | Both | ✅ Filled (12 decisions D1–D12) | — |
| `context/docs/project/change-log.md` | Both | ✅ Filled (2 deviations: D11 sick-leave, D12 user testing) | — |
| `context/docs/project/risk-log.md` | Both | ✅ Filled (10 risks) | — |
| `evaluation/a-grade-rubric.md` | Both | ✅ Complete | — |
| `evaluation/grading-guidelines.md` | Mikael | ✅ Filled (NRT criteria + NTNU-specific) | — |
| `evaluation/evaluation.md` | Both | ✅ Filled (chapter-level checklist) | — |
| `context/docs/method/CITATIONS.md` | Mikael | ⬜ Empty during extraction phase | Will be assembled from extracted source notes after all 48 sources done |

---

## Mikael's Remaining Tasks (context phase)

| Task | Priority | Status |
|------|:--------:|--------|
| Fill `context/fitgap-summary.md` | High | ✅ Done |
| Fill `evaluation/grading-guidelines.md` from PDF | High | ✅ Done |
| Fill `context/docs/project/sprint-log.md` retroactively | Medium | ✅ Done (2026-05-01) |
| Fill `context/docs/project/decision-log.md` | Medium | ✅ Done (2026-05-01) |
| Fill `context/writing-style-examples.md` (after first section) | Low | ⬜ Blocked |
| Fill `context/docs/user-research/user-tests.md` (if tests done) | Low | ⬜ Not started |
| Finalise research sub-questions in `context/context.md` | High | ✅ Done (3 sub-questions) |
| Generate source notes via `/source-extractor` for all bib keys | High | ✅ Done — 39 of 39 (post Polanyi/Nonaka drop) |
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

Fixed pre-write activity: before any `/write-section`, confirm that every required citation key in the section has a verified source notes file at `context/docs/method/sources/raw/extracted/{bibkey}.md` and is present in `result/references.bib`.

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
Chapter integration: not started (reset 2026-05-01; ch2-theory.tex cleared, all sections to be rewritten against new outline)

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
✅ result/references.bib                                    → 39 entries (post 2026-05-01 audit + qualitative-methodology trim + Polanyi/Nonaka drop)
⬜ context/docs/method/CITATIONS.md                          → empty; assembled from source notes after all extractions
✅ context/docs/method/sources/raw/extracted/                → 39 of 39 source notes generated
⬜ context/docs/tech/benchmark-results.md                    → blocks Ch 4.5 and Ch 5.2
⬜ context/docs/method/research-design.md ethics/duration    → blocks Ch 3.2
⬜ context/docs/project/sprint-log.md                        → blocks Ch 3.4
⬜ context/docs/project/decision-log.md                      → blocks Ch 3.4 and Ch 5
⬜ context/docs/project/change-log.md                        → blocks Ch 5 and Ch 6
```

With the strengthened readiness gate, writing can only start when each section's MUST CITE keys have verified source notes in `sources/raw/extracted/` and evidence files are filled.

### Source-extraction status — ✅ all 39 entries extracted

All MUST CITE keys in the outline have verified source notes. Tacit-knowledge references in §1.1 ¶3, §3.5.6, and §5.1.2 ¶4 are now domain-concept usage (no theoretical anchor required) after dropping Polanyi and Nonaka & Takeuchi due to PDF unavailability — captured in `context/glossary.md` "Tacit knowledge" entry.

### Other content blockers
- ~~Ch 3.3 ¶6 needs interview duration and research ethics details~~ → ✅ honest framing added to `research-design.md` (industry consultation, no Sikt/NSD, ~15 min/interview).
- ~~Ch 3.5 §3.5.1–§3.5.8 origin/learned bullets need `sprint-log.md` and `decision-log.md`~~ → ✅ both filled 2026-05-01.
- ~~Ch 4.2 needs requirement-ID consistency between `functional-requirements.md` and `requirements-traceability.md`~~ → ✅ rebuilt 2026-05-01: 42 FK-IDs aligned across both files; pipeline gate for §4.2 passes.
- Ch 4.5 ¶7 and Ch 5.2 need `benchmark-results.md` filled (Embret, in progress).
- ~~Ch 5.5 (Deviations from Plan) needs `change-log.md`~~ → ✅ filled with D11 + D12.
- Ch 5.6 may proceed without user tests; L8 explicitly anchors this in §5.4 (no separate `user-tests.md` content needed).
