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

If any section is `drafted-needs-revision` or `not started`:
→ **STOP**: "Cannot review Chapter {N}. These sections are not ready: {list}. Run /write-section for each first."

Read the .tex file. Verify every `\section{...}` has real content (≥150 words, not just comments).

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
{If Chapter N >= 5:} Read `evaluation/theory-usage.md` — check for orphaned theories.

Focus on CHAPTER-LEVEL issues that section reviews cannot catch:
1. Transitions between sections — do they flow or feel disconnected?
2. Repetition — is the same point made in multiple sections?
3. Spine alignment — does the chapter AS A WHOLE serve its spine sentence?
4. RQ contribution — how does this chapter contribute to answering the research question?
5. Missing elements — is anything promised in the chapter intro not delivered?

CHAPTER-TYPE-SPECIFIC QUESTIONS — answer the ones for Chapter {N}:
- Ch 2: "Is every theory introduced here used in Ch 4 or Ch 5? If a theory is not referenced later, flag it as orphaned. Check against evaluation/theory-usage.md if it exists."
- Ch 3: "Is every methodological choice justified with a reason, not just stated? Are there unjustified decisions?"
- Ch 4: "Are findings presented without interpretation? Flag any evaluative language across the chapter (good, bad, effective, insufficient)."
- Ch 5: "Every major analytical claim must be anchored in either a Ch 4 finding, Ch 3 methodological limitation, Ch 2 theory, or documented system evidence. Check evaluation/theory-usage.md — are all theories from Ch 2 connected? Flag any orphaned theories."
- Ch 6: "Does every conclusion claim trace back to evidence presented in Ch 4–5? Are the research questions answered with specific references?"

For each issue: quote the passage, reference the section, classify as CRITICAL or MINOR, suggest a fix.

End with JSON (REQUIRED):
```json
{"cross_section_issues": {"critical": 0, "minor": 0}, "spine_aligned": true, "rq_contribution": "A", "orphaned_theories": 0, "pass": true, "notes": ""}
```
Pass: all critical counts == 0 AND spine_aligned AND rq_contribution in ["A", "B"]
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

Grade the ENTIRE chapter against NRT criteria. Consider:
- Does the chapter demonstrate the expected level of insight for its role?
- Is the overall quality consistent, or are there weak sections pulling it down?
- Does the chapter contribute to the thesis earning an A?

CHAPTER-TYPE-SPECIFIC QUESTIONS — answer the ones for Chapter {N}:
- Ch 2: "Does the writer show understanding of the theory or just summarise it? Look for: comparisons between theories, identification of limitations, application to this specific project."
- Ch 3: "Is the methodology section transparent enough that another researcher could replicate the study? Are ethical considerations addressed?"
- Ch 4: "Are all findings grounded in specific data sources? Is the presentation systematic and free from interpretation?"
- Ch 5: "Is the discussion genuinely critical? Look for: tensions between findings and theory, alternative interpretations, acknowledgment of what the data does NOT show."
- Ch 6: "Are research questions answered concretely with references to specific findings? Is future work grounded in identified limitations?"

For each NRT criterion relevant to this chapter: give a grade and one-sentence justification.

End with JSON (REQUIRED):
```json
{"overall_grade": "A", "depth_assessment": "genuine", "source_integration": "integrated", "criteria_at_C": [], "most_important_fix": "none", "pass": true}
```
Pass: overall_grade == "A" AND criteria_at_C is empty AND depth_assessment == "genuine"
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

  RED THREAD:  {PASS/FAIL} — cross-section: {N critical}/{N minor}, spine: {aligned/not}, RQ: {A/B/C}, orphaned theories: {N}
  SENSOR:      {PASS/FAIL} — grade: {A/B/C}, depth: {genuine/surface}, sources: {integrated/mixed/name-dropped}, weakest: {criterion}

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
