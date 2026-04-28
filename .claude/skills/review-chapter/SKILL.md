---
name: review-chapter
description: "Chapter integration check: 2 agents (red-thread + sensor) after all sections are drafted-reviewed. Usage: /review-chapter 2"
---

# Review Chapter Pipeline

You are the orchestrator for chapter-level integration review. You check that all sections work together as a coherent chapter.

**This is NOT a rewrite trigger.** It is a health check before human approval.

## Input

A chapter number like `2`. Derive:
- Chapter name: 1=Introduction, 2=Theory, 3=Methodology, 4=Findings, 5=Discussion, 6=Conclusion
- .tex file: `result/chapters/ch{N}/ch{N}-{name}.tex`

## Step 1: Verify Prerequisites

Read STATUS.md. Find the section tracking table for Chapter {N}.
ALL sections must have status `drafted-reviewed`.

If any section is `drafted-needs-revision`, `drafted-needs-manual-fix`, or `not started`:
→ **STOP**: "Cannot review Chapter {N}. These sections are not ready: {list}. Run /write-section for each first."

Read the .tex file. Verify every `\section{...}` has real content (≥150 words, not just comments).

### Proportionality check
Read the chapter target length in `context/outline.md`. Estimate the chapter word count from the `.tex` file, excluding comments, commands, bibliography, and appendices. Use approximately 350 words per thesis page for a rough page estimate.

If the actual length is more than 20% below or above the target range, flag this in the report. This is not an automatic hard stop, but the sensor agent must consider whether the imbalance weakens the chapter.

### Post-Chapter-5 theory usage check
If reviewing Chapter 5 or later, read `evaluation/theory-usage.md`. Check whether every theory introduced in Chapter 2 is either:
- used in Chapter 4 or 5,
- explicitly marked `reference only`, or
- flagged for removal/reconnection.

For Chapter 5, unresolved orphaned theories are a review issue and must be included in the report.

### Chapter-level source audit
Read `context/docs/method/literature-list.md`, `evaluation/source-requests.md`, and `result/references.bib`.

Check:
- citation density by section, and flag suspiciously low or suspiciously high citation density,
- orphan sources: sources cited in the chapter but not clearly used to support a claim,
- any citation key that is not `approved-read` in `literature-list.md`,
- unresolved `SRC-xxx` requests that apply to the chapter,
- theories or frameworks used without an approved source.

Unapproved sources and unresolved source requests are review issues. This pipeline
never promotes a source to `approved-read`.

## Step 2: Spawn 2 Review Agents

Launch both as independent tasks (parallel if supported, sequential otherwise).

### Agent 1 — Chapter Red Thread

```
You are a critical academic reviewer checking the coherence of an ENTIRE chapter.

Read `.claude/agents/red-thread.md` for your full assessment structure (5 parts).

The chapter to review: read `{TEX_FILE}` — the complete file, all sections.
The thesis backbone: read `context/thesis-spine.md`
The research question: read `context/context.md` — Research Question section.
Previous chapters: read `result/chapters/ch{1..N-1}/*.tex` files that have real content.
Read `context/outline.md` for the chapter target length and section plan.
Read `context/docs/method/literature-list.md`, `evaluation/source-requests.md`, and `result/references.bib` for source approval and source-request status.
If reviewing Chapter 5 or later, read `evaluation/theory-usage.md` and check for orphaned theories.

Focus on CHAPTER-LEVEL issues that section reviews cannot catch:
1. Transitions between sections — do they flow or feel disconnected?
2. Repetition — is the same point made in multiple sections?
3. Spine alignment — does the chapter AS A WHOLE serve its spine sentence?
4. RQ contribution — how does this chapter contribute to answering the research question?
5. Missing elements — is anything promised in the chapter intro not delivered?
6. Proportion — is the chapter length within the target range, or does imbalance weaken the argument?
7. For Ch 5+: are all Chapter 2 theories used, marked as reference-only, or clearly flagged for removal?
8. Source audit — are citation density, orphan sources, unresolved source requests, and unapproved citation keys acceptable?
9. Concept placement across sections — is every technical term, acronym, or named concept introduced BEFORE its first use at the chapter level? A concept defined only in a later section is a placement bug that section reviews miss. Examples: VRP, CP-SAT, tacit knowledge, HITL. Quote each misplacement and state where the introduction should move to.
10. Terminology consistency across the chapter — list any pair of synonyms used across sections for the same concept ("driver"/"employee", "planner"/"dispatcher", "solver"/"engine"). Every drift is an issue.
11. Ordering across sections — does the chapter move from concrete/broad to abstract/specific where appropriate (e.g. Ch 2 opens with examples of resource scheduling in other domains BEFORE the formal definition)? Does narrative framing (how the work is done today) appear early enough in the chapter? Flag misordering at the chapter level.

For each issue: quote the passage, reference the section, suggest a fix.

End with JSON (REQUIRED):
```json
{"cross_section_issues": 0, "spine_aligned": true, "rq_contribution": "A", "source_audit_issues": 0, "pass": true}
```
Pass: cross_section_issues == 0 AND source_audit_issues == 0 AND spine_aligned AND rq_contribution in ["A", "B"]
```

### Agent 2 — Chapter Sensor

```
You are an external examiner (sensor) grading an ENTIRE chapter of a bachelor thesis.

Read `.claude/agents/quality.md` for your assessment structure.
Read `evaluation/grading-guidelines.md` for official NRT criteria and weighting.
Read `evaluation/a-grade-rubric.md` for A-grade standards.
Read `evaluation/evaluation.md` for chapter-specific checklist.

The chapter: read `{TEX_FILE}` — all sections as a whole.
Context: read `context/context.md` and `context/thesis-spine.md`.
Previous chapters: read completed `result/chapters/ch{1..N-1}/*.tex`.
Read `context/outline.md` for target length and `evaluation/theory-usage.md` for theory tracking when reviewing Chapter 5 or later.
Read `context/docs/method/literature-list.md`, `evaluation/source-requests.md`, and `result/references.bib` for source approval and source-request status.

Grade the ENTIRE chapter against NRT criteria. Consider:
- Does the chapter demonstrate the expected level of insight for its role?
- Is the overall quality consistent, or are there weak sections pulling it down?
- Does the chapter contribute to the thesis earning an A?
- Is the chapter proportionate to its role in the thesis (not too thin, not over-expanded)?
- For Chapter 5 or later: does the discussion use the theories introduced in Chapter 2, or are there orphaned concepts?
- Does the source use meet A-grade standards: claim coverage, source fit, authority, integration, reuse sanity, and no orphan sources?
- Are any theories, frameworks, or empirical claims supported by citations that are not `approved-read`?

For each NRT criterion relevant to this chapter: give a grade and one-sentence justification.

End with JSON (REQUIRED):
```json
{"overall_grade": "A", "criteria_at_C": [], "source_audit_issues": 0, "most_important_fix": "none", "pass": true}
```
Pass: overall_grade == "A" AND criteria_at_C is empty AND source_audit_issues == 0
```

## Step 3: Report

Save outputs to:
- `evaluation/review/redthread-ch{N}.md`
- `evaluation/review/quality-ch{N}.md`

Parse JSON gates.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CHAPTER {N} — {NAME} — INTEGRATION REVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  RED THREAD:  {PASS/FAIL} — cross-section issues: {N}, spine: {aligned/not}, RQ: {A/B/C}
  SENSOR:      {PASS/FAIL} — grade: {A/B/C}, weakest: {criterion}
  LENGTH:      ~{words} words / ~{pages} pages — target: {range}, deviation: {OK/>20%}
  THEORY USE:  {OK/orphaned concepts listed/not applicable}
  SOURCE USE:  {OK/issues listed} — density, orphan sources, approved-read status, unresolved SRC requests

  {If both pass:}
  ✅ Chapter {N} is CANDIDATE FOR HUMAN APPROVAL.
  → Review it yourself, then mark as "approved" in STATUS.md.

  {If any fail:}
  ⚠️ Issues found:
    1. {issue — which section, what to fix}
    2. ...
  → Run /write-section {X.Y} in revise mode for affected sections.
  → Then re-run /review-chapter {N}.
```

Update STATUS.md:
- Both pass → chapter row = `candidate-approved`
- Any fail → chapter row = `reviewed-needs-revision`

**Human makes final approval decision. This pipeline never auto-approves.**
