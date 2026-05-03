# Chapter 3 — Methodology — Quality Review (chapter-sensor) — RE-REVIEW (Round 3)

**Reviewer role:** External examiner (sensor) at NTNU, A-grade standard across the whole chapter.
**Date:** 2026-05-03
**Target file:** `result/chapters/ch3/ch3-method.tex`
**Trigger:** /review-chapter 3 re-run after .tex modifications since round-2 pass.

## Summary

**PASS — Grade A.** No criteria at C, anchor drift 0, source audit 0. Two sub-A friction points recorded (one minor, one cosmetic); neither is a B-pull.

## Per-criterion grading

**Origin story (§3.1) — A.** Four-paragraph narrative names Admmit's bachelor task (project OPG29), the team's own initiative in calling seven coordinators in a single day, and HITL-and-multi-tenancy as Admmit mandate predating the interviews. Reads as story not specification — the A-marker pattern.

**DSRM applied step-by-step (§3.2) — A.** All six Peffers activities each get one applied bullet of 2–4 sentences naming what was done in this project. Objective-centered initiation correctly invoked to explain non-strict activity-1 ordering. Evaluation bullet draws the validate-vs-evaluate boundary at the artefact level and forwards what is *not* validated to §3.7 by L-number.

**Named iterations (§3.5) — A.** Eight named iterations with descriptive titles. Each follows tried/why/what happened/learned/next with explicit Origin label. Limitations surfaced honestly (greedy ceiling structural; CP-SAT degrades at scale; deviation false positives at week boundaries; weight-UX legibility problem). §3.5.7 honestly reports "Bare time labels (\"ten seconds\" versus \"sixty seconds\") were not legible to a coordinator who does not think in solver-runtime budgets". Minor: §3.5.4's engine-version-snapshot insight functions as a Learned lesson but sits in What-happened bullet.

**Evaluation framework separate from validity (§3.6 vs §3.7) — A.** §3.6 covers artefact testing; §3.7 covers research's epistemic limits via Malterud's three standards. Handoff sentence — "The framework that follows in \Cref{sec:validity} addresses the research's epistemic limits rather than the artefact's; this section ends where validation ends" — makes the distinction explicit. Asymmetric anchor binding ("Effektivitet has the tightest binding... Tilpasningsdyktighet is exercised only indirectly... Tillit/kontroll sits in the same partial-coverage position") is precisely the honest scope statement an A demands.

**Research paradigm stated and justified — A.** §3.2 ¶1 names DSR explicitly, contrasts purely positivist and purely interpretive alternatives by what they could not deliver, lands on DSR as "the synthesis the project requires". Paradigm justification, not name-dropping.

**Interview methodology (replicability) — A.** §3.3 specifies purposive sampling from Admmit roster, single-day phone calls March 2026, ~15 minutes each, Norwegian, five guide topics named, broad-opening / gap-prompted convention, automated transcription with manual correction.

**Participant selection justified — A.** "the project required coordinators in the planning role at companies where algorithm-assisted planning is plausibly relevant, and Admmit's customer base supplied that population directly". Self-selection bound forwarded to L2.

**Validity and reliability honest — A.** §3.7 names L1/L2/L3/L6/L8/L9. Reflexivity paragraph explicitly states what would otherwise be concealed. Minor: ¶3 wording "the hypothesis about the visibility gap" slightly conflicts with §3.4's "named only after coding" — recommend "prior expectation" instead.

**Every methodological choice has a "because" — A.** Phone, Norwegian, 15 min, single day, purposive, automated transcription, synthetic data, Sikt-not-sought — every choice carries a stated reason. No bare "we chose X" anywhere.

## Source integration (name-dropping check)

- `hevner2004design` (p.82) — integrated; anchors DSR-as-build-and-apply-artefact claim.
- `peffers2007dsrm` (pp.46, 56 ×3) — integrated; six-activity list, sequential-not-strict caveat, entry-point typology each cited at correct page.
- `braun2006thematic` (p.77, p.81, p.87, pp.81–82, Table 2 criterion 15) — integrated; each cite tracks a specific claim.
- `malterud2001lancet` (pp. 483, 484, 485, 486) — integrated; three-standards count respected (the chapter correctly resolves the outline's "four criteria" drift).

No name-dropping detected. Wieringa correctly deferred via `\Cref{sec:dsr}` to Ch 2.

## Anchor name drift

Verified zero drift. Every Effektivitet / Tillit/kontroll / Tilpasningsdyktighet occurrence is verbatim. Grep across the chapter: 0 hits on the drift list (Trust/control, Efficiency, Adaptability, kontroll alone, fleksibilitet, skalerbarhet, human control, operator oversight, trust calibration).

## "Accountable to coordinator" operationalisation

Four-action phrasing "inspect, modify, accept, or reject" appears verbatim at §3.1 ¶3, §3.2 Objectives, §3.2 Design-and-Development, §3.5.5 Tried, §3.5 ¶1, §3.6 ¶2, §3.6 ¶4. No vague control language used as substitute.

## Multi-engine "How-not-Of" framing

§3.5.4 and §3.6 ¶1 both frame the benchmark as a methodologically independent test of *how* solvers compare, not *whether* the visibility gap is real or HITL is necessary. Neither location overclaims epistemic scope.

## Cross-chapter coherence

- §3.2 ¶1 references `\Cref{sec:dsr}` (Ch 2 §2.2) — label exists; Wieringa validation/evaluation distinction is treated there.
- §3.5.7 references `\Cref{sec:hitl}` (Ch 2 §2.1) — label exists; explanation-as-interface treatment matches.
- Forward references to `sec:effektivitet`, `sec:limitations`, `sec:future-work`, `sec:interview-findings`, `sec:requirements`, `sec:fit-gap` will resolve in Ch 4–5 when written.
- Anchor concepts threaded throughout.

## Chapter-type-specific question

Methodological discussion is genuinely critical: §3.5.7 admits time-label legibility problem; §3.5.8 admits weight-UX problem; §3.6 admits three things the benchmark cannot test; §3.7 names L1/L2/L3/L6/L8/L9. Reflective writing.

## Overall assessment

- **Estimated grade: A.**
- **Single most important fix before submission**: §3.7 reflexivity paragraph wording — change "the hypothesis about the visibility gap" to "prior expectation that a visibility gap might exist" to avoid micro-inconsistency with §3.4's inductive-coding claim. One-sentence fix; does not block A.
- **Pull on overall thesis grade**: this chapter pulls the thesis up. Strongest A-marker carrier reviewed so far — origin story, DSRM applied step-by-step, eight named iterations, separated evaluation/validity, anchor threading, four-action operationalisation, asymmetric scope statement, honest L-numbered limitations.

## Comparison to A standard — gap analysis

1. **§3.7 reflexivity wording (minor)** — "hypothesis about the visibility gap" vs §3.4's "named only after coding". Fix: "prior expectation".
2. **§3.5.4 lesson placement (cosmetic)** — engine-version-snapshot insight reads as Learned but sits in What-happened.

Sub-A friction points, not B-pulls. Chapter is at A.

---

## JSON Gate

```json
{
  "pass": true,
  "overall_grade": "A",
  "criteria_at_C": [],
  "anchor_drift_count": 0,
  "source_audit_issues": 0,
  "most_important_fix": "Soften §3.7 reflexivity wording from 'hypothesis about the visibility gap' to 'prior expectation that a visibility gap might exist' to avoid a small inconsistency with §3.4's inductive-coding claim.",
  "issues": [
    {"severity": "minor", "section": "§3.7", "type": "wording-inconsistency", "detail": "'the hypothesis about the visibility gap' in the reflexivity paragraph slightly conflicts with §3.4's claim that the visibility gap was 'named only after coding'. Recommend 'prior expectation' rather than 'hypothesis'."},
    {"severity": "cosmetic", "section": "§3.5.4", "type": "lesson-placement", "detail": "The engine-version snapshot insight functions as a Learned lesson but sits in the What-happened bullet."}
  ]
}
```
