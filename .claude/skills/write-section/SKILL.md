---
name: write-section
description: "Write one thesis section: auto context loading, deterministic checks, 2-agent review, auto-revision. Usage: /write-section 2.1"
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

Initialise: `round = 1`.

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

### 1c. Section readiness gate

Run this gate before writing. It catches missing evidence before a writer can produce generic text or cite sources without verified content.

Read the paragraph plan for section `{X.Y}` in `context/outline.md`. Extract every `MUST CITE`, `MUST EVIDENCE`, `MUST GROUND`, `MUST ANCHOR`, and `MUST TRACE` marker for that section.

**Citation readiness — hard stop if any fail:**
1. Every `MUST CITE` marker must contain concrete BibTeX key(s), such as `\textcite{key}` or `\parencite{key}`.
2. If a `MUST CITE` marker is generic (e.g. "trust source", "agile/iterative methodology source", "OR-Tools/solver literature" without a key), **STOP**: "Section {X.Y} has a generic MUST CITE marker in paragraph {¶}. Replace with a concrete bibkey in outline.md before writing."
3. Every required citation key must exist in `result/references.bib`.
4. Every required citation key must have a verified source notes file at `context/docs/method/sources/raw/extracted/{bibkey}.md`. The file must:
   - Exist
   - Be ≥500 bytes (not template-only)
   - Contain "Notes generated from raw" in the Status block
   If any are missing or unfilled, **STOP** and list which keys lack source notes. Tell the user: "Source notes incomplete for: {keys}. Run extraction (see `.claude/agents/source-extractor.md`) before writing this section."
5. The source notes file is the ground truth. Do not invent passages or cite a source whose notes are missing.

**Evidence readiness — hard stop if any fail:**
1. Every `MUST EVIDENCE` / `MUST GROUND` source file must exist and contain section-specific evidence, not only generic background.
2. A required evidence file is not ready if it is <50 words, mostly comments/templates, or contains unresolved placeholders needed by this section (`[FILL IN]`, `[CITATION NEEDED]`, `TODO`, or template-only rows).
3. If evidence is missing, **STOP** and list exactly what information must be filled before writing.
4. Do not write around missing support by weakening the claim, deleting the claim, or inserting `[CITATION NEEDED]`.

**Evidence readiness — hard stop if any fail:**
1. Every `MUST EVIDENCE` / `MUST GROUND` source file must exist and contain section-specific evidence, not only generic background.
2. A required evidence file is not ready if it is <50 words, mostly comments/templates, or contains unresolved placeholders needed by this section (`[FILL IN]`, `[CITATION NEEDED]`, `TODO`, or template-only rows).
3. If evidence is missing, **STOP** and list exactly what information must be filled before writing.
4. Do not write around missing support by weakening the claim, deleting the claim, or inserting `[CITATION NEEDED]`. Missing support must become a source request with section, paragraph, and claim.

**Anchor and trace readiness — hard stop if any fail:**

1. **Locked anchor name validation (hard fail on synonym).** Every `MUST ANCHOR` marker that names an anchor concept must use one of three locked names verbatim: **Effektivitet**, **Tillit/kontroll**, **Tilpasningsdyktighet**. Anchor tags that are synonyms or paraphrases — e.g. `MUST ANCHOR: kontroll`, `MUST ANCHOR: human control`, `MUST ANCHOR: fleksibilitet`, `MUST ANCHOR: skalerbarhet`, `MUST ANCHOR: efficiency`, `MUST ANCHOR: trust calibration`, `MUST ANCHOR: oversight` — are a hard fail. **STOP** with the message: "Section {X.Y} has a MUST ANCHOR marker `{tag}` that is not one of the locked anchor names (Effektivitet / Tillit/kontroll / Tilpasningsdyktighet). Update outline.md before writing."

2. **Cross-chapter trace targets exist.** For Chapter 5, each `MUST ANCHOR` to Ch 2, Ch 3, or Ch 4 must point to a section that already contains real drafted content (≥150 words, not only comments/placeholders). If the referenced section is not drafted, **STOP** and tell the user which section must be written first.

3. **Chapter 5 sub-section anchor structure.** For sections under §5.1 (anchor-organised primary findings — §5.1.1 Effektivitet, §5.1.2 Tillit/kontroll, §5.1.3 Tilpasningsdyktighet), the section must have at least one `MUST ANCHOR` marker tied to **exactly one** locked anchor whose name matches the sub-section's intended anchor (e.g. §5.1.1 → Effektivitet only). If a §5.1.x section has no `MUST ANCHOR` to a locked name, or anchors to two anchors at once, **STOP**.

4. **Chapter 6 RQ-answer trace structure.** For Chapter 6, all Chapters 1–5 must contain real drafted content before writing starts. Section 6.2 must explicitly answer the main research question and all three sub-questions from `context/context.md`; SQ3 is not optional. **Each RQ-answer paragraph must have a `MUST TRACE` marker that (a) points to its originating Ch 5 sub-section AND (b) names the anchor it serves verbatim.** A `MUST TRACE` that names no anchor or names a synonym is a hard fail. Each SQ must be reproduced verbatim as a single-line block quote in the prose, then answered in one paragraph.

**Cross-file consistency — hard stop if any fail:**
1. For Section 4.2, compare requirement IDs in `context/docs/requirements/functional-requirements.md` against `context/docs/requirements/requirements-traceability.md`. If the same IDs describe different requirements, or implemented/tested status cannot be traced, **STOP**.
2. For technical/system sections (4.4, 4.5, 5.1, 5.2, 5.3, 5.4, 6.3), compare referenced context files against `context/scope.md` and `context/context.md`. **STOP** if they contradict each other on hosting, implemented features, 2FA, driver-facing features, billing/invoicing, admin UI, or user testing.
3. Missing local LaTeX tools remain a warning during Step 4, not a hard stop here.

### 1d. Check existing content
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
- context/docs/method/sources/raw/extracted/{bibkey}.md — for each MUST CITE key in this section, read the verified source notes
{FOR EACH chapter-specific file from context-gather.md:}
- {file path} — {why it's needed}

EVIDENCE MARKERS:
All MUST markers (MUST CITE, MUST EVIDENCE, MUST ANCHOR, MUST TRACE, MUST GROUND) in outline.md for this section must be satisfied. Missing marker satisfaction is a review issue.
If a planned claim lacks a source with verified notes, STOP and report the gap with section and paragraph. Do not write around it and do not insert `[CITATION NEEDED]`.

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

{If auto-revise mode:}
AUTO-REVISION MODE: Fix ONLY the issues listed below. Do not rewrite passages that passed review.
ISSUES TO FIX:
{Paste consolidated critical issues from Step 6.5}

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
4. **Source notes**: For every extracted citation key, verify that `context/docs/method/sources/raw/extracted/{bibkey}.md` exists and is filled (≥500 bytes, contains "Notes generated from raw"). Missing or unfilled notes are hard fails.
5. **Compilation**: Run `make` via Bash. Check exit code.
   - If `latexmk` or `pdflatex` is not installed: report as **WARNING** ("LaTeX not installed — compile check skipped"), NOT as hard fail. The section can still proceed to review.
   - If LaTeX IS installed and `make` fails: that IS a hard fail.

### Warnings
Check for:
1. **Filler phrases**: Grep for `it is important to note`, `it is worth noting`
2. **Repeated transitions**: Count occurrences of "Furthermore", "Moreover", "Additionally" — warn if any appears 3+ times in the section
3. **Em-dashes**: Grep for `—` (em-dash) in the generated section text (not in .bib, comments, or review files). List all occurrences with line numbers. WARNING, not hard fail.
4. **Section length vs outline target**: Parse the section's page target from `context/outline.md` (format: `(~X pages)` or `(~X–Y pages)`). Convert to words using ~250 words per page. Count actual words in the drafted section (exclude LaTeX commands, comments, citations themselves). Compare:
   - Within target range → PASS (silent)
   - Within ±20 % of target → INFO (logged, not warning)
   - Outside ±20 % → WARNING with target, actual, deviation. Do NOT hard fail. Cutting good content for length is worse than overshooting.
   - If outline has no target → skip silently, do not invent a target.

### Citation Density Listing
List all paragraphs (by ¶-number) that have zero `\parencite` or `\textcite` citations AND zero references to primary data sources. This is a **listing only** — the reviewer in Step 5 decides which need citations.

### Outline Compliance (deterministic part)
1. **Paragraph count**: Count paragraphs vs ¶-markers in outline.md. Flag mismatch.
2. **Evidence key check**: Read MUST CITE/EVIDENCE/ANCHOR/TRACE/GROUND markers from outline. For each, check if required source appears in section text. Flag missing.

### Save results
Write check results to `evaluation/review/sections/ch{N}-{X.Y}-round{R}-checks.md`:
```
# Deterministic Checks — Section {X.Y} Round {R}

## Hard Fails
- Placeholders: {PASS/FAIL — details}
- Forbidden voice: {PASS/FAIL — details}
- Citation keys: {PASS/FAIL — missing keys listed}
- Source notes: {PASS/FAIL — keys missing source notes listed}
- Compilation: {PASS/FAIL/WARNING}

## Warnings
- Filler phrases: {list if any}
- Repeated transitions: {list if any}
- Em-dashes: {count and locations, or "none found"}
- Section length: target {X words from outline}, actual {Y words}, deviation {±Z %} — {PASS/INFO/WARNING/skipped (no target)}

## Citation Density
- Paragraphs without citations: {list or "all paragraphs have citations"}

## Outline Compliance
- Paragraph count: outline specifies {N}, section has {M} — {MATCH/MISMATCH}
- Evidence keys: {list of missing required sources, or "all required sources present"}
```

**If ANY hard fail:** Report failures to user with concrete fix instructions per failure type:
- Forbidden voice ("we believe", "we think", "we found") — quote occurrence with line number; user revises in writer session.
- Placeholders ([FILL IN], [CITATION NEEDED]) — list each with section/paragraph; cannot auto-fix.
- Invalid citation key — list missing keys; user adds entries to references.bib (academic integrity: never auto-add).
- Missing source notes — list bibkeys whose source notes file is missing or unfilled; user runs source-extractor or selects different source.
- Compilation fail — show LaTeX error output; user fixes manually.

Mark section as `drafted-needs-revision` in STATUS.md. Do not run review agents. Manual fix is faster and safer than automated retry for these cases.

**If no hard fails:** Proceed to Step 5.

## Step 5: REVIEW (2 agents)

Only reached if all hard checks pass.

Spawn two agents as independent tasks. Run in parallel if supported; sequentially otherwise. **Do not share context between reviewers.**

**All reviewers share this rule:**
> If `pass: false`, at least one item in `issues[]` MUST have `severity: "critical"`. If the issue cannot be fixed automatically, set `fixable: false`.
> Check that all MUST markers from the outline ¶-plan for this section are satisfied. If a required source or anchor is missing, report it as a critical issue.
> If a claim needs a source whose notes are missing, weak, or mismatched, report the claim as a source need with section and paragraph. Do not suggest writing around the missing source.

### Agent 1 — Section Coherence

```
You are checking logical coherence of ONE section of a bachelor thesis.

Read the section from `{TEX_FILE}` — only the content under \section{...} for section {X.Y}.
Read `context/thesis-spine.md` — find the sentence for Chapter {N} and the Anchor Concepts section.
Read `context/context.md` — find the Research Question and sub-questions.
Read `context/outline.md` — find the ¶-plan for section {X.Y}. Use this for outline compliance.
Read `evaluation/reference-thesis-analysis.md` §7 — transferable A-markers (per-chapter and cross-chapter patterns to verify).
For each cite key used in the section, read `context/docs/method/sources/raw/extracted/{bibkey}.md` to verify the cited claim matches what the source actually says.
If there are previous sections in this chapter (before {X.Y}), read them too for continuity.

Answer these questions with specific evidence:
1. Does this section follow logically from the previous section (or chapter opening)?
2. Does every factual claim have a citation (\parencite or \textcite) or reference to primary data?
3. Does this section serve the chapter's one-sentence spine purpose?
4. Are there concepts or terms used that haven't been introduced in this or a previous section? (HITL, CP-SAT, tacit knowledge, etc. must be defined BEFORE first use.)

OUTLINE COMPLIANCE (reviewer judgment):
5. Does each paragraph cover the topic specified in its ¶-plan from outline.md?
6. Is the outline's logical progression followed, or did the writer reorganise?

STRUCTURE AND PARAGRAPH DISCIPLINE:
7. For each paragraph: state in one sentence what it is about. If the sentence needs "and", the paragraph mixes concepts — report as critical issue with a split suggestion. Typical failure: multi-resource + single-resource + valid driver in one paragraph; NP-hard + heuristics + solver engines in one paragraph.
8. For sections enumerating items (constraint types, solver engines, automation levels, requirement categories): is the taxonomy stated first (as a sentence or table) BEFORE the items are explained? If not, report as critical issue.
9. When a theoretical concept is introduced, does the section move from concrete examples to formal definition (broad → specific), rather than the reverse? If the writer leads with the definition before the reader has a hook, report as issue.
10. Does narrative framing (how the work is done today, what the artefact does) arrive early enough that the reader can follow the theory? Late framing is an issue.
11. Definitions: is each definition short, direct, and sourced? Flag invented definitions and flag qualifiers the source did not use ("limited resources", "complex constraints"). Flag domain words taken from sources unchanged ("each machine") when they do not fit our domain.
12. Terminology consistency: list every pair of synonyms used for the same concept in this section ("driver"/"employee"; "planner"/"dispatcher"; "solver"/"engine"). Every drift is an issue.
13. Transitions: every paragraph boundary must have an explicit bridge. "Furthermore"-style filler does not count. Report boundaries that require the reader to re-orient.
14. Decisions: for every stated decision (method, algorithm, architecture, UI, scope), is the reason also stated? "What" without "why" is a critical issue for Ch 3, 4, and 5.

EVIDENCE MARKER CHECK:
15. Are all MUST markers from the outline satisfied? If any required source or anchor is missing, report as critical issue.
16. For any unsupported claim, report: section {X.Y}, paragraph number, exact claim, source type needed, and whether a `SRC-xxx` request already exists.
17. Selective source use: for each citation, is only the relevant part of the source being used? Flag citations where the source is broad but the claim is narrow, or where the cited source's content does not match the surrounding claim.

CHAPTER-TYPE-SPECIFIC QUESTIONS — answer the ones for Chapter {N}:
- Ch 2: "Is every theory introduced here used in Ch 4 or Ch 5? If not referenced later, flag as orphaned."
- Ch 3: "Is every methodological choice justified with a reason, not just stated?"
- Ch 4: "Are findings presented without interpretation? Flag any evaluative language (good, bad, effective, insufficient)."
- Ch 5: "Every major claim must be anchored in a Ch 4 finding, Ch 3 limitation, Ch 2 theory, or documented system evidence."
- Ch 6: "Does every conclusion claim trace back to evidence presented in Ch 4–5?"

For each issue: quote the passage, classify as CRITICAL or MINOR, suggest a fix.

IMPORTANT: If pass is false, at least one issue in issues[] MUST have severity "critical".

End your response with this JSON block (REQUIRED):
```json
{
  "pass": true,
  "unsupported_claims": {"critical": 0, "minor": 0},
  "spine_serves": true,
  "logic_issues": {"critical": 0, "minor": 0},
  "orphaned_concepts": 0,
  "structure_issues": {
    "mixed_paragraphs": 0,
    "taxonomy_after_detail": 0,
    "definition_before_hook": 0,
    "late_narrative_framing": 0,
    "concept_before_introduction": 0,
    "missing_transitions": 0,
    "decisions_without_rationale": 0,
    "terminology_drift": 0,
    "invented_or_decorated_definitions": 0,
    "selective_source_use_failures": 0
  },
  "source_requests": [],
  "issues": [],
  "suggestions": [],
  "notes": ""
}
```
Pass: all critical counts == 0 AND spine_serves == true AND every field under structure_issues == 0.
```

### Agent 2 — Section Quality

```
You are an examiner assessing ONE section of a bachelor thesis for A-grade quality.

Read the section from `{TEX_FILE}` — only section {X.Y}.
Read `evaluation/evaluation.md` — find the checklist for Chapter {N}.
Read `evaluation/a-grade-rubric.md` — what separates A from B, including the "Cross-chapter A-markers" appendix.
Read `evaluation/reference-thesis-analysis.md` §7 — transferable A-markers from the reference A-grade thesis (ChatSSB 2025). Score the section under review against the relevant patterns.
Read `.claude/agents/naturalness.md` — the 10-point AI-pattern checklist. Apply this as part of your assessment (em-dashes, inflated vocabulary, hedging stacks, formulaic transitions, etc.).
Read `context/docs/method/academic-writing-guide.md` — the "Writing Action Levels" section.
Read `context/outline.md` — find MUST markers for this section.
For each cite key used in the section, verify against `context/docs/method/sources/raw/extracted/{bibkey}.md` that the cited claim matches the verified source notes.

IMPORTANT — respect the chapter's writing action level:
- Chapter 1 (Intro): EXPLAIN. Clear motivation, precise RQ, scope.
- Chapter 2 (Theory): EXPLAIN. Depth of theoretical understanding.
- Chapter 3 (Method): EXPLAIN + JUSTIFY. Methodological reasoning, transparency.
- Chapter 4 (Findings): DESCRIBE + ANALYSE. No interpretation. Assess accuracy, source grounding.
- Chapter 5 (Discussion): DISCUSS. Critical argumentation, weighing, connection to theory.
- Chapter 6 (Conclusion): SUMMARISE. RQ answered, contributions clear, future work concrete.

Assess:
1. Is this section at A-level for the appropriate writing action level?
2. **Source integration check** — for each citation:
   a. Is the cited claim specific (page/chapter reference) or generic?
   b. Does the sentence BEFORE or AFTER connect it to the thesis argument?
   c. Could the citation be removed without weakening the paragraph? If yes, it's name-dropped.
   Classify: "integrated" / "mixed" / "name-dropped"
3. **Citation auditor** — flag all of the following as source issues:
   a. name-dropping,
   b. claims supported by weak, wrong, or only tangentially relevant sources,
   c. paragraphs that make source-dependent claims without a necessary source,
   d. too many citations without analysis or connection to the thesis argument,
   e. any source cited where the source notes file at `context/docs/method/sources/raw/extracted/{bibkey}.md` is missing or unfilled, or where the cited claim does not match the documented passages.
4. Does it meet the relevant checklist items from evaluation.md?
5. **Evidence marker check** — are all MUST markers from outline satisfied?
6. If a claim needs a new or better source, report it as a source request need with section, paragraph, claim, and desired source type.

CHAPTER-TYPE-SPECIFIC QUESTIONS — answer for Chapter {N}:
- Ch 2: "Does the writer show understanding or just summarise? Look for: comparisons, limitations, application to this project."
- Ch 5: "Is the discussion genuinely critical? Look for: tensions, alternative interpretations, what the data does NOT show."

DEPTH ASSESSMENT — classify as "genuine" or "surface":
Signs of A-level depth (genuine):
- Claims qualified with conditions
- Multiple perspectives before author's position
- Limitations of cited theory acknowledged
- Project-specific examples illustrate abstract concepts
- Could NOT be written from just reading abstracts

Signs of B-level (surface):
- Claims without qualification
- Single perspective
- Theory summarised but not applied
- Generic examples
- Reads like textbook summary

IMPORTANT: If pass is false, at least one issue in issues[] MUST have severity "critical".

End your response with this JSON block (REQUIRED):
```json
{
  "pass": true,
  "quality_grade": "A",
  "depth_assessment": "genuine",
  "source_integration": "integrated",
  "critical_source_issues": 0,
  "source_requests": [],
  "weakest_aspect": "none",
  "fix": "none needed",
  "naturalness_score": 5,
  "ai_patterns": 0,
  "em_dashes_found": 0,
  "inflated_vocab_count": 0,
  "issues": [],
  "suggestions": []
}
```
Pass: quality_grade == "A" AND depth_assessment == "genuine" AND critical_source_issues == 0 AND naturalness_score >= 4.
"mixed" source_integration doesn't auto-fail — but critical_source_issues must be 0.
```

## Step 6: REPORT

Save review outputs to:
- `evaluation/review/sections/ch{N}-{X.Y}-round{R}-coherence.md`
- `evaluation/review/sections/ch{N}-{X.Y}-round{R}-quality.md`

Parse the JSON from each agent's response.

### Gate parsing
- **Coherence**: Pass if all critical counts == 0 AND spine_serves == true.
- **Quality**: Pass if quality_grade == "A" AND depth_assessment == "genuine" AND critical_source_issues == 0 AND naturalness_score >= 4.

Determine status:

| Condition | Status |
|-----------|--------|
| All gates pass | `drafted-reviewed` |
| Any coherence critical > 0 or spine false | `drafted-needs-revision` |
| Quality grade B/C or depth "surface" or critical_source_issues > 0 or naturalness_score < 4 | `drafted-needs-revision` |

Print summary:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SECTION {X.Y} — {TITLE} — Round {R}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Written to: {TEX_FILE}
  Word count: ~{N} words

  HARD CHECKS:   {PASS/FAIL}
  COHERENCE:     {PASS/FAIL} — unsupported: {N crit}/{N minor}, spine: ✓/✗
  QUALITY:       {A/B/C} — depth: {genuine/surface}, sources: {integrated/mixed/name-dropped}, naturalness: {score}/5 (em-dashes: {N}, inflated vocab: {N})

  WARNINGS:      {list if any}
  SOURCE GATE:   {approved/unresolved} — {unapproved keys or SRC ids}
  SOURCE NEEDS:  {section/paragraph/claim list, or "none"}
  CITATION DENSITY: {paragraphs without citations}
  OUTLINE COMPLIANCE: ¶ count {MATCH/MISMATCH}, evidence keys {status}

  STATUS: {drafted-reviewed | drafted-needs-revision | drafted-needs-manual-fix}
```

→ Go to Step 6.5.

## Step 6.5: AUTO-REVISE

### Auto-revise (if drafted-needs-revision)

**Max 3 total rounds.** Round 1 = initial write, round 2–3 = auto-revisions. Round 4 must never be created.

```
IF status == "drafted-needs-revision" AND round < 3:
  1. Collect all issues where severity == "critical" AND fixable == true
     from coherence and quality JSON.
     Missing source notes, generic MUST CITE markers, and weak/wrong source fit are NOT fixable automatically unless a replacement source with verified notes already exists.

  2. IF no fixable critical issues exist:
       Status: "drafted-needs-manual-fix"
       Report: "Review failed but no fixable critical issues. Manual intervention required." If the blocker is source-related, list the required source notes file that needs to be created or updated.
       Update STATUS.md. STOP.

  3. Set next_round = round + 1 BEFORE spawning writer.
     All SAVE/CHECK/REVIEW files use next_round.

  4. Build consolidated feedback block from fixable critical issues only.

  5. Spawn writer agent in AUTO-REVISION MODE (see Step 2 template).

  6. GOTO Step 3 (SAVE with next_round) → Step 4 → Step 5 → Step 6
     (Step 6 will re-enter Step 6.5 if still failing.)

IF round >= 3 AND status == "drafted-needs-revision":
  Status: "drafted-needs-manual-fix"
  Report remaining issues. Update STATUS.md. STOP.
```

### Final report

After auto-revise completes (or is skipped):

```
  {If drafted-reviewed:}
  ✅ Section {X.Y} is ready.
  → Write next section with /write-section {next}
  → Or /review-chapter {N} when all sections of this chapter are done.

  {If drafted-needs-revision (should not happen — auto-revise handles this):}
  ⚠️ Issues to fix — auto-revise will attempt...

  {If drafted-needs-manual-fix:}
  🛑 Pipeline exhausted auto-fix attempts (max 3 rounds). Manual intervention required.
  Remaining issues:
    1. [{source}] {description}
    2. [{source}] {description}
  → Fix manually and run /write-section {X.Y} again.
```

Update STATUS.md — find or create the section tracking table for Chapter {N}. Update the row for section {X.Y} with current results.
