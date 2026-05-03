# Thesis Status — Ressursplanlegger

> Update this file after every writing session.
> Claude reads this at the start of every session.
> Last updated: 2026-05-03 — Ch 3 integration re-review (Round 3) PASS + all 5 polish fixes applied directly to .tex. Both reviewers had returned PASS again (redthread: 0 cross-section critical / spine aligned / RQ contribution A / 0 anchor drift / 0 source audit; sensor: Grade A / 0 criteria at C / 0 drift / 0 source audit) with 5 polish-only observations recorded. All 5 fixes now applied: (1) §3.7 ¶3 "the hypothesis about the visibility gap" → "the prior expectation that a visibility gap might exist" (resolves micro-conflict with §3.4 "named only after coding" inductive-coding claim); (2) §3.5.4 engine-version-snapshot insight relocated from What-happened to Learned ("Reproducibility in a multi-engine architecture must be enforced at the version level: engine-version snapshots recorded per benchmark run removed the silent-update inconsistency."); (3) §3.2 Design-and-Development bullet adds "hereafter called the three engines" naming convention; (4) §3.5 intro "told here as a connected narrative" → "told here as a sequence of decisions" (matches per-iteration independence honestly); (5) §3.5.4 Learned drops the explicit "set out canonically in \Cref{sec:evaluation-framework}" cross-ref (§3.6 owns canonical statement); also normalised "three solver families" → "three engines" downstream at §3.2 Demonstration bullet and §3.7 ¶3. Compile passes (41-page main.pdf unchanged); biber Unicode::UCD tooling warning persists per established convention. Word count unchanged at ~5547 words / ~15.8 pages, +17% over ~13.5p target (within 20% tolerance). Anchor verbatim-match maintained: 25 occurrences with 0 drift. Four-action operationalisation appears 7× across §3.1/§3.2/§3.5/§3.6. All 4 cite-key source notes verified content-match. Files saved: evaluation/review/redthread-ch3.md (round 3) + evaluation/review/quality-ch3.md (round 3). Chapter 3 ready for human final approval.
> Earlier 2026-05-03 — §3.7 drafted-reviewed (R1 PASS coherence + quality A/genuine/integrated, naturalness 4/5). Four-paragraph Validity & Reliability section drafted in one round; both reviewers passed with 0 critical / 0 minor issues. Coherence flagged 2 polish suggestions (§5.4 L9 widening for downstream §3.6/§3.7 test-suite-absence graft → DUPLICATE of L#-binding-scope rule, kept as forward note; ¶4 two-heterogeneous-items sentence). Quality flagged 3 polish suggestions (¶2 em-dash density 3 matched pairs in 105 words → outside §3.5/§4.5 budget scope but stylistic tic; ¶4 Malterud p. 484 polarity flip; framework-choice because for Malterud). Lessons-learned harvest: 3 NEW rules promoted — (a) § Reader accessibility "Em-dash density cap for non-bulleted prose paragraphs (>2 per 100 words is a tic)", sister to the bulleted-section em-dash budget; (b) § Source faithfulness "When a section adopts a single framework as its organising device, the framework choice itself needs a because", higher-order extension of the per-decision because rule; (c) § Source faithfulness "Preserve a source's default-vs-exception polarity when paraphrasing polarity-rich claims", triggered by Malterud p. 484 polarity flip. All 3 SECTION-SPECIFIC fixes applied in-prose: (a) ¶2 both matched-pair em-dashes converted to parentheses + adjective phrasing, ¶2 em-dash count 4→0; (b) ¶4 polarity restored to "preconceptions as separate from bias unless the researcher fails to disclose them"; (c) ¶4 awkward "hypothesis ... and HITL ... were named" recast as "Both the hypothesis ... and the prior commitment to HITL are named ...". §3.7 final word count ~378 (~1.5 pages; outline target ~250 = 1 page trimmed; +51 % over baseline, exactly at the Ch-3 +50 % silent ceiling — defensible by three distinct validity bindings × four substantive moves with rationale, comparable to §3.6 R1 +101 %, §3.4 R2 +95 %, §3.3 R1 +65 %). Compile check: pdflatex passes (40-page main.pdf, same as §3.6 because biber Unicode::UCD failure persists per the §3.2 R2 / §3.3 R1 / §3.4 R2 / §3.5 R1 / §3.6 R1 convention; cite resolution did not run, but LaTeX compiles cleanly). One new citation key (`malterud2001lancet`, used 4 times across ¶1/¶2/¶4 with page-precise refs to pp. 483, 484, 485, 486); Wieringa deferred via `\Cref{sec:dsr}` per the established defer-to-Ch-2-cite rule. All six L# forwards (L1, L2 in ¶2; L6, L8, L9 in ¶3; L3 in ¶4) match their §5.4 defining scope or grafted precedent (§3.3 ¶3 brief-duration on L1, §3.3 ¶6 researcher-developer overlap on L3, §3.6 ¶3 test-suite absence on L9, §3.6 ¶4 override flow on L8). Ch 3 sections all complete (§3.1–§3.7); ready for `/review-chapter 3` integration check after the user's spine-sync review.
> Earlier 2026-05-03 — §3.6 drafted-reviewed (R1 PASS coherence + quality A/genuine/integrated, naturalness 5/5). Five-paragraph evaluation-framework section drafted in one round; both reviewers passed with 0 critical/0 minor issues. Coherence flagged 2 polish suggestions (¶1 Wieringa redirect attached to second name-drop; ¶1/¶5 colloquial "tests" vs Wieringa-committed "validate" — borderline, classified as DUPLICATE of existing § Terminology cross-chapter terminology-lock rule and skipped). Quality flagged 1 polish suggestion (¶1 long sentence rhythm). Section-specific fixes applied in-prose: (a) ¶1 long sentence on asymmetry split at "It also embodies"; (b) "(see \Cref{sec:dsr})" appended after "in Wieringa's sense" in ¶1 closing for inline cite-defer visibility. §3.6 final word count ~757 (~3 pages; outline target ~1.5 pages = ~375; +101% over baseline, above the Ch-3 +50% silent ceiling — defensible by five rationale-bearing decisions × four explicit L#-forwarding gaps × asymmetric anchor-mapping role, comparable to §3.4 R2 +95% precedent). Compile check: pdflatex passes (40-page main.pdf, +2 from §3.5's 38); biber Unicode::UCD tooling failure persists per the §3.2 R2 / §3.3 R1 / §3.4 R2 / §3.5 R1 convention. Zero new citations — Wieringa deferred via `\Cref{sec:dsr}` per the established defer-to-Ch-2-cite rule. All five L# forwards (L5/L6/L7/L8 from outline + L9 added in ¶4 per requirements-traceability.md L9 binding) match their §12.0.7 defining scope.
> Earlier 2026-05-03 — §3.5 drafted-reviewed (R1 PASS coherence + quality A/genuine/integrated, naturalness 4/5). Eight-iteration narrative (§3.5.1 Schema → §3.5.8 Configurable Soft-constraint Weights) drafted in one round; both reviewers passed with 0 critical issues. Coherence flagged 2 minor (§3.5.5 four-action compression to three buttons; §3.5.8 L4-adjacent graft hedge — non-fixable in §3.5, tracked as §5.4 outline note). Quality flagged 3 minor (em-dash overuse — 8 across 8 sub-subsections, tic-pattern; §3.5.5 four-action narrowed; §3.5.4 "best meets Effektivitet" abstract at point of use). Lessons-learned harvest applied: NEW rule under § Reader accessibility — "Em-dash budget for narrative sections with bulleted iteration / finding / decision structure" (cap parenthetical `---` at one per sub-subsection in §3.5, §4.5, §4.7, §5.1.x, §5.4 L#; lone trailing em-dashes are the tic, matched-pair are exempt; replace with commas for apposition, colons for orientation, parentheses for true aside, sentence break otherwise). Section-specific fixes applied in-prose: (a) §3.5.5 Tried bullet restored to four-action lock ("inspect / modify / accept / reject"); (b) §3.5.4 Why bullet concretised — "best meets Effektivitet on the metrics that the framework in §3.6 operationalises (scheduled-assignment count, soft-constraint penalty, runtime within budget)"; (c) all 8 em-dashes removed from §3.5 — 6 lone parentheticals → commas/colons (lines 36, 48, 61, 73, 87, 95), matched-pair on line 61 → comma + "where" clause, CP-SAT acronym gloss → dropped dash entirely. §3.5 final word count ~1950 (~7.8 pages; outline target ~5 pages = ~1250; +56 % over baseline, just above the Ch-3 +50 % silent ceiling — defensible by 8 iterations × "every choice has a because" rubric demand × tried/why/what-happened/learned/next pattern, comparable to §3.4 R2 +95 % precedent). Compile check: pdflatex passes (38-page main.pdf, was 32 in §3.4 R2 — added 6 pages from §3.5); biber Unicode::UCD tooling failure persists per the §3.2 R2 / §3.3 R1 / §3.4 R2 convention.
> Earlier 2026-05-03 — §3.4 drafted-reviewed (R2 PASS A/genuine/integrated, naturalness 4/5; R1 failed coherence on one fixable critical: "themes" used for two distinct objects within ¶1 — interview-guide topics AND TA analytic outputs both labelled "themes" with matching count "five", silently equating pre-coded scaffolds with constructed analytic outputs and contradicting the inductive positioning the same paragraph claims; auto-revise R2 fixed by renaming guide-topic occurrences to "guide topics" and naming three canonical analytic themes inline (visibility gap, operator-vs-owner asymmetry, automation scepticism with override preference). R2 introduced one new minor cross-section drift (§3.3 still used "themes" for guide topics in three places) plus one minor naturalness regression (em-dash count 1→3). Both addressed in harvest pass: §3.3 lines 41/45/47 renamed "themes" → "guide topics" / "topics" / "topic coverage"; §3.4 ¶1 open em-dash list-expansion converted to parenthetical (em-dash count back to 1, the supervisor-sanctioned matched-pair fit/gap gloss in ¶2). Lessons-learned harvest applied: NEW rule under § Terminology — "Distinguish interview-guide topics from TA analytic-output themes" (reserve "themes" for six-phase TA analytic outputs; use "guide topics" / "topics" for pre-coded scaffolds; renaming in only one section displaces the drift cross-section). Section-specific R2 minors (also addressed): TA-choice because-clause added with page-anchored two-part rationale (theoretical flexibility p. 81 + accessibility p. 77); MoSCoW because-clause added (clear stakeholder-negotiable boundary); FK glossed inline as "functional-requirements register (IDs FK-01 through FK-42)". Final §3.4 prose ~488 words (~1.95 pages; outline target ~1 page = ~250; +95 % over baseline, +30 % over Ch 3 +50 % silent ceiling — defensible by "every choice has a because" demand × five methodological decisions, comparable to §3.3 R1 +65 % precedent). Compile check: pdflatex passes (32-page main.pdf); biber Unicode::UCD tooling failure persists per the §3.2 R2 / §3.3 R1 convention.
> Earlier 2026-05-03 — §3.3 drafted-reviewed (R1 PASS coherence + quality A/genuine/integrated, naturalness 4/5). No critical issues; 5 coherence + 6 quality minor issues, all addressed. Lessons-learned harvest applied: (a) NEW rule under § Reader accessibility — "Don't reference an appendix that does not exist — commit to creating it, or rephrase the location"; (b) NEW rule under § Source faithfulness — "When forwarding a finding to a named L# limitation, the L#'s defined scope must cover what is forwarded"; (c) NEW rule under § Source faithfulness — "The because-clause must match the actual rationale — coincidental adjacent facts are not the cause". User-directed scope change: Sonix.ai removed from §3.3 prose AND `research-design.md` (transcription described generically as "automated transcription"; cloud-disclosure-to-L3 binding therefore moot for §3.3 specifically, but the L#-binding-scope rule was promoted for future sections). Section-specific fixes applied in-prose: actor terms unified to "coordinator" / "the seven coordinators" (¶2's "informants in the operator role" replaced with "coordinators in the planning role"); bridges added at ¶2 / ¶3 / ¶6 openings; geographic spread (Bergen, Mo i Rana, Lakselv, Tana) added to ¶2; appendix reference rephrased to "the project's working notes"; ¶6 Sikt because-clause realigned to consultation-framing-as-cause; Sikt parenthetical gloss added; all six em-dash pairs removed (split sentences or colon); ¶6 long-sentence rhythm broken with short sentences. Final word count 619 (was 659; outline target ~375; +65% — comparable to §3.2 R2 +30% precedent, defensible by "every choice has a because" rubric demand × six methodological decisions). Compile check: pdflatex passes (31-page main.pdf); biber Unicode::UCD tooling failure persists per the §3.2 R2 convention.
> Earlier 2026-05-03 — §3.2 drafted-reviewed (R2 PASS A/genuine/integrated, naturalness 5/5; R1 failed coherence on three fixable critical issues: anchor-binding-verb-requires, redundancy-with-2-4, evaluation-bullet-test-vs-validate; auto-revise R2 fixed all three plus four R1 minors in one pass). Lessons-learned harvest applied: (a) existing rule "Bind artefact elements to anchors with transparent verbs, not metaphors" extended with Sub-clause A (anchors cannot be the grammatical subject of imperative verbs `requires`/`demands`/`mandates`) and Sub-clause B (when describing what was decided/built/fixed, name the artefact element, not the anchor); (b) NEW rule under § Source faithfulness — "Defer to a Ch 2 cite via cross-reference rather than re-citing the same primary-source pages downstream"; (c) NEW rule under § Terminology — "Cross-chapter terminology lock for Ch 2-committed vocabulary distinctions" (Wieringa validate, Bainbridge asymmetry, Hoff & Bashir three-dimensional, Miller explanation, Tilpasningsdyktighet over skalerbarhet/fleksibilitet). Section-specific Demonstration-bullet axis added inline ("small fleets of around ten drivers through to multi-department operations of around forty-five vehicles"). Final word count 729 (~2.6 pages, +30% over outline target ~2 pages — expansion is in places reviewers asked the writer to expand: Communication bullet 1→3 sentences, closing-paragraph Peffers p. 56 four-entry-points framing). One residual minor (anchor-binding collapsed in closing paragraph) was promoted to the new Sub-clause B rule and not patched in §3.2 prose this round; the rule will catch the same pattern in future sections, and §3.2 can be touched up at chapter-integration time. Compile check: biber Unicode::UCD environment error treated as tooling warning per SKILL spec (latexmk + pdflatex installed, biber binary's Perl module broken).
> Earlier 2026-05-02 — §3.1 drafted-reviewed (R1 PASS A/genuine/n/a, naturalness 5/5). Lessons-learned harvest applied: new rule "Bind artefact elements to anchors with transparent verbs, not metaphors" added under § Terminology in `evaluation/review/lessons-learned.md`. Two §3.1 polish fixes applied (¶2→¶3 bridge front-loaded, ¶4 dense five-Cref sentence split into three, anchor metaphor "technical substrate of Tilpasningsdyktighet" replaced with transparent verb "enables Tilpasningsdyktighet by isolating per-customer configuration"). Spine synced: Ch 3 sentence updated from "four to six named iterations" to "eight named iterations" to match chapter scaffold (§3.5.1–§3.5.8) and §3.1 ¶4 prose.
> Earlier 2026-05-01: bib refactor + outline marker additions per `context/docs/method/source-fitting-plan.md`: REPLACE malterud2017kvalitative→malterud2001lancet; ADD flotve2025transportytelser, polanyi1966tacit, orlikowski1991studying, venkatesh2003utaut, mietzner2009variability; DROP larman2003iterative, beck2001manifesto, wced1987commonfuture, hilty2015ict4s, eu2024aiact, walsham1995interpretive, seyff2022mapping, jobin2019landscape, jensen2014norsktransport. Bib now 43 entries (was 48). 14 new MUST CITE markers in outline.md. Chapter scaffolding (.tex) restructured to match new outline (Ch 1 §1.2 added, Ch 4 §4.6+§4.7 added, Ch 5 anchor-organised with §5.1.1/5.1.2/5.1.3 + §5.5/§5.6 + Ch 3 8-subsection iteration scaffold).

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
| 2.1 | ✅ R1 | PASS | PASS | A / genuine / integrated | 5/5 | drafted-reviewed |
| 2.2 | ✅ R1 | PASS | PASS | A / genuine / integrated | 5/5 | drafted-reviewed |
| 2.3 | ✅ R2 | PASS | PASS | A / genuine / integrated | 5/5 | drafted-reviewed |
| 2.4 | ✅ R1 | PASS | PASS | A / genuine / integrated | 5/5 | drafted-reviewed |
Chapter integration: candidate-approved (2026-05-02 — sensor PASS A; redthread originally FAIL on spine mismatch + minor structure gaps; all 7 issues fixed manually without re-review per user instruction: (1) spine Ch 2 sentence updated to five-layer HITL, (2) chapter-intro paragraph added, (3) §2.1→§2.2 bridge sentence added, (4) §2.3→§2.4 bridge sentence added, (5) NP-hard consequence expanded with multi-engine motivation, (6) Hoff & Bashir analogy paired with explicit use-statement, (7) §2.4 ¶3 Wieringa paragraph trimmed by ~1 sentence. New word count ~3041 / ~8.7 pages, target ~8.5 pages. Anchor drift remains 0; no forbidden synonyms. PDF compiles. See `evaluation/review/redthread-ch2.md` and `evaluation/review/quality-ch2.md`. Awaiting human approval.)

### Chapter 3 — Methodology
| Section | Written | Checks | Coherence | Quality | Naturalness | Status |
|---------|:-------:|:------:|:---------:|:-------:|:-----------:|--------|
| 3.1 | ✅ R1 | PASS | PASS | A / genuine / n/a | 5/5 | drafted-reviewed |
| 3.2 | ✅ R2 | PASS | PASS (R1 FAIL → R2 PASS) | A / genuine / integrated | 5/5 | drafted-reviewed |
| 3.3 | ✅ R1 | PASS | PASS | A / genuine / integrated | 4/5 | drafted-reviewed |
| 3.4 | ✅ R2 | PASS | PASS (R1 FAIL → R2 PASS) | A / genuine / integrated | 4/5 | drafted-reviewed |
| 3.5 | ✅ R1 | PASS | PASS | A / genuine / integrated | 4/5 | drafted-reviewed |
| 3.6 | ✅ R1 | PASS | PASS | A / genuine / integrated | 5/5 | drafted-reviewed |
| 3.7 | ✅ R1 | PASS | PASS | A / genuine / integrated | 4/5 | drafted-reviewed |
Chapter integration: candidate-approved (2026-05-03 — Round 3 re-review confirms PASS after .tex modifications since Round 2; both reviewers PASS again. Round 2 PASS was achieved after 18 surgical edits applied to the .tex directly. Round 2 redthread PASS / 0 cross-section issues / 0 anchor drift / 0 source-audit / spine aligned / RQ contribution A; only one optional polish observation (§3.3 ¶4 line 47 is now a 159-word semicolon-chained sentence with phone/Norwegian/15-min rationales — grammatically correct and parallel-structured, optional split before '; and the fifteen-minute target', non-blocking). Round 2 sensor PASS / Grade A / 0 drift / 0 source-audit / empty issues array; explicitly notes "the chapter pulls the thesis grade up by a wider margin than Round 1". Round 1 had FAILED redthread on 1 critical (§3.2 line 35 anchor-binding violation — Sub-clause B pattern recurrence) plus 11 minor polish; round 2 fixed all 12 redthread items + all 5 sensor gap-to-A items in one editing pass. Key fixes: (a) §3.2 closing rewritten to "Admmit's mandate fixed HITL and the multi-tenant architecture --- the artefact elements operationalising Tillit/kontroll and Tilpasningsdyktighet ---" (anchors are realised properties, not artefact elements); (b) §3.5 terminology locked to "HITL surface" (was mixed with "operator surface"/"planning surface"); (c) §3.5.4 ¶Learned compressed to one-clause forward reference, §3.6 ¶1 carries canonical "how-not-whether" statement; (d) CP-SAT acronym moved to first mention in §3.2; (e) §3.5.8 "L4-adjacent" → "configurability gap" (drops half-defined L# binding); (f) §3.1 ¶3 forward Cref redirected sec:dsr-dsrm → sec:iterations; (g) §3.3 ¶3 topic guide reproduced in-thesis (was deferred to "project's working notes"); (h) §3.3 ¶4 phone/Norwegian/15-min rationales added; (i) §3.3 ¶6 implicit-consent and no-anonymisation justified honestly within consultation framing; (j) §3.1 ¶1 dual-role configuration made explicit ("for the two-student team... with both students contributing to both workstreams"); (k) §3.6 ¶3 synthetic dataset sizes anchored to interviewed fleet ranges (small below smallest, medium at small-operator end, large exceeds largest 45-vehicle fleet); (l) §3.4 ¶3 L1/L2 forwarding trimmed to single mention. Round 2 confirmed 7 inspect/modify/accept/reject operationalisations (up from 6), 25 verbatim anchor occurrences across the three anchors with 0 drift. Final word count ~5538 (was 5371; +167 words from rationale and empirical-anchor additions), ~15.8 pages, target ~13.5 pages, +17% within 20% tolerance. Compile passes (41-page main.pdf). See `evaluation/review/redthread-ch3.md` and `evaluation/review/quality-ch3.md`. Awaiting human approval.)

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
