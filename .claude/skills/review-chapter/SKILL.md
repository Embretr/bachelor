---
name: review-chapter
description: "Chapter integration check: 2 subagents (chapter-redthread + chapter-sensor) after all sections are drafted-reviewed. Usage: /review-chapter 2"
---

# Review Chapter Pipeline

You are the orchestrator for chapter-level integration review. You check that all sections work together as a coherent chapter.

You do NOT review content yourself — you spawn the `chapter-redthread` and `chapter-sensor` subagents for that.

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

If the actual length is more than 20% below or above the target range, flag this in the report. This is not an automatic hard stop, but the sensor subagent must consider whether the imbalance weakens the chapter.

### Source notes existence check
Extract every cite key used in the chapter (`grep -oE '\\(par|text)cite\{[^}]+\}' {TEX_FILE}` and parse). For each, verify the source notes file exists and is non-template via Bash:
```bash
for k in KEY1 KEY2 ...; do
  f="context/docs/method/sources/raw/extracted/$k.md"
  if [ ! -f "$f" ] || [ "$(wc -c < "$f")" -lt 500 ] || ! grep -q "Notes generated from raw" "$f"; then
    echo "MISSING: $k"
  fi
done
```

If any FAIL: this is a repository-state issue (file deleted or path wrong) — report it in the final summary as a source-notes-readiness issue. Do not block the review; the chapter-redthread and chapter-sensor subagents will assess content fit on the keys whose source notes do exist.

## Step 1.5: Precompute Slices

The chapter-level subagents need small structured inputs that should be extracted ONCE rather than reading full files in each subagent. Compute these via Bash and pass inline in the user message.

### A. SPINE_SENTENCE — chapter {N} spine + Anchor Concepts section
```bash
awk -v n="$N" '/^## /{p=0} /^## (Anchor|Anchors)/{p=1} $0 ~ "^### Chapter "n"|^### Ch "n {p=1} p' context/thesis-spine.md
```
Or: read the line matching `Chapter {N}` plus the Anchor Concepts block.

### B. RQ_BLOCK — Research Question and sub-questions
```bash
awk '/^## Research [Qq]uestion/{p=1} p && /^## /{c++} c>1{p=0} p' context/context.md
```

### C. OUTLINE_CHAPTER_SLICE — section plan for Chapter {N}
```bash
awk -v n="$N" '
  $0 ~ "^# Chapter "n" " || $0 ~ "^## Chapter "n" " {p=1; next}
  p && /^# Chapter [0-9]+ / {p=0}
  p {print}
' context/outline.md
```

### D. RUBRIC_SLICE — Chapter {N} rubric (chapter-sensor only)
```bash
awk -v ch="### Chapter $N " '
  $0 ~ "^"ch {p=1}
  p && /^### Chapter [0-9]+ / && $0 !~ "^"ch {p=0}
  p && /^---$/ {p=0}
  p {print}
' evaluation/a-grade-rubric.md
```
Always include "Cross-Chapter A Criteria" appendix.

### E. REF_ANALYSIS_SLICE — same shape as in /write-section
```bash
awk '/^## 7\. /{p=1} /^## 8\. /{p=0} p' evaluation/reference-thesis-analysis.md
awk -v ch="### Chapter $N " '/^## 3\. /{ins=1} ins && $0 ~ "^"ch {p=1} ins && /^### Chapter [0-9]+ / && $0 !~ "^"ch {p=0} ins && /^## /{ins=0; p=0} p' evaluation/reference-thesis-analysis.md
awk '/^## Cross-chapter A-markers/{p=1} p && /^## /{c++} c>1{p=0} p' evaluation/reference-thesis-analysis.md
```

### F. BIB_SLICE — only the entries cited in this chapter
```bash
keys=$(grep -oE '\\(par|text)cite\{[^}]+\}' {TEX_FILE} | sed -E 's/.*\{([^}]+)\}/\1/' | tr ',' '\n' | sort -u)
for k in $keys; do
  awk -v k="$k" 'BEGIN{p=0} $0 ~ "^@[a-z]+\\{"k"," {p=1} p; p && /^\}$/ {p=0; print ""}' result/references.bib
done
```

### G. EVALUATION_CHECKLIST — chapter {N} block
```bash
awk -v ch="## Chapter $N" '
  $0 ~ "^"ch {p=1}
  p && /^## Chapter [0-9]+/ && $0 !~ "^"ch {p=0}
  p {print}
' evaluation/evaluation.md
```

### H. TARGET_LENGTH_BLOCK — target range + actual + proportionality verdict
Construct from Step 1's proportionality check output. Format:
```
Target: {target range from outline}
Actual: ~{words} words / ~{pages} pages
Proportionality: {OK | >20% over | >20% under} — {one-line implication}
```

## Step 2: Spawn 2 Review Subagents

Spawn `chapter-redthread` and `chapter-sensor` in parallel — single message with both Agent calls. Their contexts are independent by design.

Both subagents' system prompts already contain their full check lists, JSON gate formats, anchor-drift hard checks, and the locked-source-set rule. Do NOT repeat them in the user message.

```
Agent({
  subagent_type: "chapter-redthread",
  prompt: <REDTHREAD_USER_MESSAGE>
})
```

```
Agent({
  subagent_type: "chapter-sensor",
  prompt: <SENSOR_USER_MESSAGE>
})
```

**REDTHREAD_USER_MESSAGE template:**

```
Chapter: {N} — {CHAPTER_NAME}
Target .tex: {TEX_FILE}

---

SPINE_SENTENCE (Chapter {N} spine + Anchor Concepts):
{paste output of slice A from Step 1.5 verbatim}

RQ_BLOCK (Research Question and sub-questions):
{paste output of slice B from Step 1.5 verbatim}

OUTLINE_CHAPTER_SLICE (section plan for Chapter {N}):
{paste output of slice C from Step 1.5 verbatim}

REF_ANALYSIS_SLICE (§7 Transferable A-Markers + Chapter {N} per-chapter pattern + Cross-chapter A-markers):
{paste output of slice E from Step 1.5 verbatim}

BIB_SLICE (the locked source set this chapter cited):
{paste output of slice F from Step 1.5 verbatim}

TARGET_LENGTH:
{paste slice H from Step 1.5 verbatim}

---

Files to read:
- {TEX_FILE} — the complete chapter, all sections
- For each cite key in BIB_SLICE: context/docs/method/sources/raw/extracted/{bibkey}.md
{If any earlier chapter has ≥150 words of real content:}
- {list previous chapter .tex paths} — for cross-chapter continuity
{If Chapter {N} is 5 or later:}
- evaluation/theory-usage.md (for the theory-tracker check)
```

**SENSOR_USER_MESSAGE template:**

```
Chapter: {N} — {CHAPTER_NAME}
Target .tex: {TEX_FILE}

---

RUBRIC_SLICE (Chapter {N} A-grade criteria + Cross-Chapter A Criteria):
{paste output of slice D from Step 1.5 verbatim}

REF_ANALYSIS_SLICE (§7 Transferable A-Markers + Chapter {N} per-chapter pattern + Cross-chapter A-markers):
{paste output of slice E from Step 1.5 verbatim}

EVALUATION_CHECKLIST (chapter-{N} checklist from evaluation/evaluation.md):
{paste output of slice G from Step 1.5 verbatim}

SPINE_BLOCK:
{paste full context/thesis-spine.md or use slice A — full file is small}

CONTEXT_BLOCK:
{paste relevant section of context/context.md or full file — small}

BIB_SLICE (the locked source set this chapter cited):
{paste output of slice F from Step 1.5 verbatim}

TARGET_LENGTH:
{paste slice H from Step 1.5 verbatim}

---

Files to read:
- {TEX_FILE} — the complete chapter, all sections
- evaluation/grading-guidelines.md (official NRT criteria and weighting)
- For each cite key in BIB_SLICE: context/docs/method/sources/raw/extracted/{bibkey}.md
{If any earlier chapter has ≥150 words of real content:}
- {list previous chapter .tex paths} — for cross-chapter context
{If Chapter {N} is 5 or later:}
- evaluation/theory-usage.md
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

  RED THREAD:  {PASS/FAIL} — cross-section issues: {N}, spine: {aligned/not}, RQ: {A/B/C}, anchor drift: {N}
  SENSOR:      {PASS/FAIL} — grade: {A/B/C}, weakest: {criterion}
  LENGTH:      ~{words} words / ~{pages} pages — target: {range}, deviation: {OK/>20%}
  THEORY USE:  {OK/orphaned concepts listed/not applicable}
  SOURCE USE:  {OK/issues listed} — density, orphan sources, source notes status

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
