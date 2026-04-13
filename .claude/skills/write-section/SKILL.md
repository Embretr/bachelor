---
name: write-section
description: "Write one thesis section: auto context loading, deterministic checks, 3-agent review. Usage: /write-section 2.1"
---

# Write Section Pipeline

You are the orchestrator. You coordinate writing one section of the bachelor thesis.
You do NOT write thesis content yourself — you spawn a writer agent for that.
You do NOT review content yourself — you spawn review agents for that.

## Input

A section number like `2.1`. Parse it to derive:
- Chapter number (e.g., `2`)
- Section number within chapter (e.g., `1`)
- Chapter name: 1=Introduction, 2=Theory, 3=Methodology, 4=Findings, 5=Discussion, 6=Conclusion
- Target .tex file: `result/chapters/ch{N}/ch{N}-{name}.tex`

## Step 1: VALIDATE

### 1a. Check outline plan
Read `context/outline.md`. Find the section plan for `{X.Y}`. It must have ¶-markers (lines starting with `- ¶`).
If the plan is missing or only has generic bullet points → **STOP**: "Section {X.Y} needs a paragraph-level plan in outline.md before writing. Add ¶-numbered paragraphs."

### 1b. Check critical context files
Read `.claude/skills/context-gather.md` — find the table for Chapter {N}. Identify all files listed.

Check each file. Classify as CRITICAL or OPTIONAL:

**CRITICAL (hard stop if missing or template-only):**
- `context/outline.md` — already checked
- `context/glossary.md` — must have real terms (not just template headers)
- `result/references.bib` — must have ≥3 real entries (not just the example entry)
- Section-specific sources from context-gather.md for this chapter

**OPTIONAL (skip with note):**
- `context/writing-style-examples.md`
- Previous chapter .tex file
- `context/docs/user-research/user-tests.md`

For each critical file: Read it. If it contains mainly `[FILL IN]` placeholders or is <50 words → **STOP**: "Critical file {path} is not filled. Fill it before writing section {X.Y}."

### 1c. Check existing content
Read the target .tex file. Find the `\section{...}` block for this section.
Determine if it has "real content": ≥150 words AND not only comments (`%`) AND no `[Main research question]` or `[Sub-question]` or `[Topic Area]` placeholders.

If real content exists, ask the user:
1. **"Revise existing section using previous reviews"** (RECOMMENDED)
2. "Overwrite from outline" (fresh write)
3. "Abort"

Track which round this is. Check `evaluation/review/sections/` for existing `ch{N}-{X.Y}-round*` files. The new round = max existing round + 1 (or 1 if none exist).

## Step 2: WRITE

Build an explicit context manifest for the writer agent. Read `.claude/skills/context-gather.md` to determine which files the writer needs for this chapter.

Spawn ONE agent:

```
You are writing section {X.Y} of Chapter {CHAPTER} — {CHAPTER_NAME} for a bachelor thesis at NTNU.

YOUR INSTRUCTIONS:
Read `.claude/agents/writer.md` for your complete writing rules. Follow them exactly.

REQUIRED FILES — read ALL of these before writing:
- context/context.md — thesis identity, research question
- context/thesis-spine.md — the backbone argument
- context/outline.md — find section {X.Y}, follow the ¶-plan EXACTLY
- context/glossary.md — use ONLY these terms, no synonyms
- result/references.bib — cite ONLY sources listed here
{FOR EACH chapter-specific file from context-gather.md:}
- {file path} — {why it's needed}

CONTINUITY:
Read `{TEX_FILE}` to see what's already written in this chapter.
{If previous chapter .tex has ≥150 words of real content:}
Read `{PREV_TEX}` for voice and style matching.

{If revise mode:}
REVISION MODE: You are revising an existing section, not writing fresh.
Read the current content in `{TEX_FILE}` section {X.Y}.
Read the previous review feedback:
{List all evaluation/review/sections/ch{N}-{X.Y}-round{R-1}-*.md files}
Fix the issues identified in the reviews while preserving what works well.

OUTPUT:
Return ONLY the LaTeX for section {X.Y}.
Start with \section{...}, end when section content is complete.
No \chapter{}, no preamble, no \begin{document}, no other sections.
```

## Step 3: SAVE

Take the writer agent's output.
Find the correct position in the .tex file — between the `\section{...}` header for this section and the next `\section{...}` (or end of file).
Replace the existing content (comments or previous draft) with the writer's output using Edit.

Save a backup: `evaluation/review/sections/ch{N}-{X.Y}-round{R}-backup.tex`
(Contains the previous content of this section, if any.)

## Step 4: DETERMINISTIC CHECKS

Run these checks directly (no agent needed). Use Grep and Bash.

### Hard Fails
Check the section content (between its `\section{}` and the next) for:

1. **Placeholders**: Grep for `[FILL IN` and `[CITATION NEEDED`
2. **Forbidden voice**: Grep for `we believe`, `we think`, `we found` (case-insensitive)
3. **Citation keys**: Extract all `\parencite` and `\textcite` commands. For each, extract the citation key(s). Verify each key exists in `result/references.bib`.
   Handle: `\parencite{key}`, `\parencite{key1,key2}`, `\parencite[see][p.~12]{key}`, `\textcite{key}`
4. **Compilation**: Run `make` via Bash. Check exit code.
   - If `latexmk` or `pdflatex` is not installed: report as **WARNING** ("LaTeX not installed — compile check skipped"), NOT as hard fail. The section can still proceed to review.
   - If LaTeX IS installed and `make` fails: that IS a hard fail.

### Warnings
Check for:
1. **Filler phrases**: Grep for `it is important to note`, `it is worth noting`
2. **Repeated transitions**: Count occurrences of "Furthermore", "Moreover", "Additionally" — warn if any appears 3+ times in the section

### Save results
Write check results to `evaluation/review/sections/ch{N}-{X.Y}-round{R}-checks.md`:
```
# Deterministic Checks — Section {X.Y} Round {R}

## Hard Fails
- Placeholders: {PASS/FAIL — details}
- Forbidden voice: {PASS/FAIL — details}
- Citation keys: {PASS/FAIL — missing keys listed}
- Compilation: {PASS/FAIL}

## Warnings
- Filler phrases: {list if any}
- Repeated transitions: {list if any}
```

**If ANY hard fail → STOP here.** Do not run review agents. Report failures to user. Mark section as `drafted-needs-revision` in STATUS.md. User must fix and re-run `/write-section`.

## Step 5: REVIEW (3 agents)

Only reached if all hard checks pass.

Spawn three agents as independent tasks. Run in parallel if the tool supports it; sequentially otherwise. **Do not share context between reviewers.**

### Agent 1 — Section Coherence

```
You are checking logical coherence of ONE section of a bachelor thesis.

Read the section from `{TEX_FILE}` — only the content under \section{...} for section {X.Y}.
Read `context/thesis-spine.md` — find the sentence for Chapter {N}.
Read `context/context.md` — find the Research Question and sub-questions.
If there are previous sections in this chapter (before {X.Y}), read them too for continuity.

Answer these questions with specific evidence:
1. Does this section follow logically from the previous section (or chapter opening)?
2. Does every factual claim have a citation (\parencite or \textcite) or reference to primary data?
3. Does this section serve the chapter's one-sentence spine purpose?
4. Are there concepts or terms used that haven't been introduced in this or a previous section?

For each issue found: quote the exact passage, explain the problem, suggest a fix.

End your response with this JSON block (REQUIRED):
```json
{"unsupported_claims": 0, "spine_serves": true, "logic_issues": 0, "pass": true}
```
Pass: unsupported_claims == 0 AND spine_serves == true AND logic_issues == 0
```

### Agent 2 — Section Quality

```
You are an examiner assessing ONE section of a bachelor thesis for A-grade quality.

Read the section from `{TEX_FILE}` — only section {X.Y}.
Read `evaluation/evaluation.md` — find the checklist for Chapter {N}.
Read `evaluation/a-grade-rubric.md` — what separates A from B.
Read `context/docs/method/academic-writing-guide.md` — the "Writing Action Levels" section.

IMPORTANT — respect the chapter's writing action level:
- Chapter 1 (Intro): EXPLAIN. Clear motivation, precise RQ, scope.
- Chapter 2 (Theory): EXPLAIN. Depth of theoretical understanding. Do not require critical discussion.
- Chapter 3 (Method): EXPLAIN + JUSTIFY. Methodological reasoning, transparency, reflexivity.
- Chapter 4 (Findings): DESCRIBE + ANALYSE. Do NOT penalise for lack of interpretation — findings should be presented precisely. Assess accuracy, source grounding, structure.
- Chapter 5 (Discussion): DISCUSS. Require critical argumentation, weighing, connection to theory.
- Chapter 6 (Conclusion): SUMMARISE. RQ answered, contributions clear, future work concrete.

Assess:
1. Is this section at A-level for the appropriate writing action level?
2. Are sources integrated into the argument (not name-dropped)?
3. Does it meet the relevant checklist items from evaluation.md?

For each weakness: quote the passage, explain what's missing, suggest a specific fix.

End your response with this JSON block (REQUIRED):
```json
{"quality_grade": "A", "weakest_aspect": "none", "fix": "none needed", "pass": true}
```
Pass: quality_grade == "A"
B = needs improvement (not catastrophic, but not A-ready)
C = major quality gap
```

### Agent 3 — Naturalness

```
You are checking if a thesis section sounds like a competent student wrote it, not AI.

Read `.claude/agents/naturalness.md` for your complete 10-point checklist.
Read the section from `{TEX_FILE}` — only section {X.Y}.
Optionally read `context/docs/method/academic-phrases.md` for reference.

Go paragraph by paragraph. For each AI-sounding passage: quote it, identify the pattern, suggest a rewrite.

End your response with this JSON block (REQUIRED):
```json
{"naturalness_score": 4, "ai_patterns": 1, "top_issues": ["minor hedging pattern in ¶3"], "pass": true}
```
Pass: naturalness_score >= 4
```

## Step 6: REPORT

Save review outputs to:
- `evaluation/review/sections/ch{N}-{X.Y}-round{R}-coherence.md`
- `evaluation/review/sections/ch{N}-{X.Y}-round{R}-quality.md`
- `evaluation/review/sections/ch{N}-{X.Y}-round{R}-naturalness.md`

Parse the JSON gate blocks from each agent's response.

Determine status:

| Condition | Status |
|-----------|--------|
| All hard checks pass + coherence pass + quality A + naturalness ≥4 | `drafted-reviewed` |
| Any hard check fails | `drafted-needs-revision` |
| Coherence fails | `drafted-needs-revision` |
| Quality B | `drafted-needs-revision` (below A standard) |
| Quality C | `drafted-needs-revision` (major quality gap) |
| Naturalness <4 | `drafted-needs-revision` |

Print summary:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SECTION {X.Y} — {TITLE} — Round {R}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Written to: {TEX_FILE}
  Word count: ~{N} words

  HARD CHECKS:   {PASS/FAIL — details if fail}
  COHERENCE:     {PASS/FAIL — unsupported: N, spine: ✓/✗}
  QUALITY:       {A/B/C} — {weakest aspect}
  NATURALNESS:   {score}/5 — {top issue if any}

  WARNINGS:      {list if any}

  STATUS: {drafted-reviewed | drafted-needs-revision}

  {If drafted-reviewed:}
  ✅ Section {X.Y} is ready.
  → Write next section with /write-section {next}
  → Or /review-chapter {N} when all sections of this chapter are done.

  {If drafted-needs-revision:}
  ⚠️ Issues to fix:
    1. [{source}] {description}
    2. [{source}] {description}
    ...
  → Fix and run /write-section {X.Y} again (choose "revise" mode).
  → Or fix manually and re-run /write-section {X.Y}.
```

Update STATUS.md — find or create the section tracking table for Chapter {N}. Update the row for section {X.Y} with current results.
