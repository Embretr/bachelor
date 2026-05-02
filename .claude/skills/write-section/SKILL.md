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
1. Every `MUST CITE` marker must contain concrete BibTeX key(s) OR a clear source-type description that maps unambiguously to one bibkey present in `result/references.bib` (per `context/outline.md`'s "Source-independence note": type-described markers are fitted at write-time from the existing extracted source notes — we do not add new sources).
2. Every required citation key must exist in `result/references.bib`. Validate via Bash: `grep -cE "^@[a-z]+\\{KEY," result/references.bib` for each key.
3. Every required citation key must have a verified source notes file at `context/docs/method/sources/raw/extracted/{bibkey}.md`. **Validate via Bash, NOT Read** (the orchestrator does not need to load the file content — the writer and reviewer agents will read the substance themselves). Required gates:
   - File exists
   - `wc -c < {path}` is ≥ 500
   - `grep -q "Notes generated from raw" {path}` returns 0
   Single combined Bash idiom:
   ```bash
   for k in KEY1 KEY2 ...; do
     f="context/docs/method/sources/raw/extracted/$k.md"
     if [ ! -f "$f" ] || [ "$(wc -c < "$f")" -lt 500 ] || ! grep -q "Notes generated from raw" "$f"; then
       echo "FAIL: $k"
     fi
   done
   ```
   If any FAIL is printed, **STOP** with that list. The thesis-source set is locked (39 entries extracted, see STATUS.md). A missing source notes file means either the path is wrong or the file was deleted — escalate to the user; do not propose extraction.
4. The source notes file is the ground truth. The writer and reviewer agents read it; the orchestrator does not.

**Evidence readiness — hard stop if any fail:**
1. Every `MUST EVIDENCE` / `MUST GROUND` source file must exist and contain section-specific evidence, not only generic background.
2. A required evidence file is not ready if it is <50 words, mostly comments/templates, or contains unresolved placeholders needed by this section (`[FILL IN]`, `[CITATION NEEDED]`, `TODO`, or template-only rows).
3. If evidence is missing, **STOP** and list exactly what information must be filled before writing.
4. Do not write around missing support by weakening the claim, deleting the claim, or inserting `[CITATION NEEDED]`. The fix is for the user to fill the evidence file from the existing artefact / interview material — not to introduce new external sources.

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

## Step 1.5: PRECOMPUTE SLICES (orchestrator-only, Bash)

The writer and the two reviewer agents all need the same handful of small excerpts from large files. Loading the full files in each agent context wastes ~200–300 k tokens per pipeline run. Instead, the orchestrator extracts the slices ONCE via Bash and pastes them inline in the agent prompts. **No agent reads `context/outline.md`, `evaluation/a-grade-rubric.md`, `evaluation/reference-thesis-analysis.md`, or `result/references.bib` in full** — they receive the relevant slice inline and the file path for optional drill-down.

Compute these slices with Bash and capture stdout. Store them in shell variables (or a temp file under `evaluation/review/sections/.tmp/round{R}/`) for re-use across the writer and the two reviewers.

### A. `OUTLINE_SLICE` — §X.Y plan
```bash
# Build the regex inside awk's BEGIN block — passing `^\*\*X.Y ` through
# `awk -v` strips the backslashes (awk -v processes escape sequences), so
# the anchor collapses to `^**X.Y ` which ERE treats as `^` followed by an
# unanchored `X.Y ` substring match. That used to pollute the slice with
# trailing rows from later tables/notes (e.g. `(§2.4 ¶3)` in §3 reappearance
# table). Building the regex inside awk preserves the literal asterisks.
awk -v xy="$XY" '
  BEGIN { sec = "^\\*\\*" xy " " }
  $0 ~ sec {p=1}
  p && /^\*\*[0-9]+\.[0-9]+ / && $0 !~ sec {p=0}
  p && /^---$/ {p=0}
  p {print}
' context/outline.md
```
Sanity-check the slice: it must start with `**$XY ` and contain no later `**X.Y ` heading for any other section. If it does, the awk anchor regressed — fix it before continuing.
Also include the "Evidence Marker Taxonomy" header block (lines 9–21 of outline.md) so the writer/reviewer can interpret MUST markers without loading the whole file. If section is in Ch 5 or Ch 6, also include the chapter's opening locked elements (e.g. §5.4 L1–L12 list, §6.2 block-quote pattern).

### B. `RUBRIC_SLICE` — Chapter N rubric
```bash
awk -v ch="### Chapter $N " '
  $0 ~ "^"ch {p=1}
  p && /^### Chapter [0-9]+ / && $0 !~ "^"ch {p=0}
  p && /^---$/ {p=0}
  p {print}
' evaluation/a-grade-rubric.md
```
Always also include the "Cross-Chapter A Criteria" and "Cross-chapter A-markers (source: ChatSSB 2025)" sections (small, ~30 lines).

### C. `REF_ANALYSIS_SLICE` — only the parts reviewers need
```bash
# §7 Transferable A-Markers (always)
awk '/^## 7\. /{p=1} /^## 8\. /{p=0} p' evaluation/reference-thesis-analysis.md
# §3 Per-Chapter Patterns — only the Ch N sub-section
awk -v ch="### Chapter $N " '/^## 3\. /{ins=1} ins && $0 ~ "^"ch {p=1} ins && /^### Chapter [0-9]+ / && $0 !~ "^"ch {p=0} ins && /^## /{ins=0; p=0} p' evaluation/reference-thesis-analysis.md
# Cross-chapter A-markers (always)
awk '/^## Cross-chapter A-markers/{p=1} p && /^## /{c++} c>1{p=0} p' evaluation/reference-thesis-analysis.md
```

### D. `BIB_SLICE` — only the entries the writer/reviewer actually need
The orchestrator already knows the cite-key set from the outline-slice MUST CITE markers (and from the writer's output during Step 4). Extract just those entries:
```bash
for k in KEY1 KEY2 ...; do
  awk -v k="$k" 'BEGIN{p=0} $0 ~ "^@[a-z]+\\{"k"," {p=1} p; p && /^\}$/ {p=0; print ""}' result/references.bib
done
```

### E. `SOURCE_NOTES_PATHS` — list of paths only
The orchestrator does NOT read source notes content. It only enumerates the paths and passes them to the writer/reviewer with the instruction "read these to verify cite faithfulness". The writer/reviewer reads them on demand:
```
For each cite key in this section, read context/docs/method/sources/raw/extracted/{key}.md.
```

These slices replace the corresponding "Read full file" instructions in the writer and reviewer prompts below. The full file path is still printed alongside each slice as `(SLICE FROM: <path>; read full file ONLY if you need more than this slice)` — agents may drill in only when necessary.

## Step 2: WRITE

Spawn the `writer` subagent. Its system prompt (in `.claude/agents/writer.md`) already contains all the writing rules — do NOT repeat them in the user message. The user message carries only the per-section inputs and slices.

Read `.claude/skills/context-gather.md` to determine which chapter-specific context files the writer should read.

```
Agent({
  subagent_type: "writer",
  prompt: <USER_MESSAGE constructed below>
})
```

**USER_MESSAGE template:**

```
Section: {X.Y}, Chapter {N} — {CHAPTER_NAME}
Target .tex: {TEX_FILE}
Mode: {fresh | revise | auto-revise}
Target length: ~{WORD_COUNT} words

---

OUTLINE_SLICE (§{X.Y} ¶-plan + Evidence Marker Taxonomy header):
{paste output of slice A from Step 1.5 verbatim}

BIB_SLICE (only keys you may cite — adding any other key is a hard fail):
{paste output of slice D from Step 1.5 verbatim}

RUBRIC_SLICE (Chapter {N} A-grade criteria + cross-chapter A-markers):
{paste output of slice B from Step 1.5 verbatim}

---

Files to read:
- context/context.md
- context/thesis-spine.md
- context/glossary.md
- evaluation/review/lessons-learned.md
- For each cite key in BIB_SLICE: context/docs/method/sources/raw/extracted/{bibkey}.md
- {TEX_FILE} — to see what is already written in this chapter
{If previous chapter .tex has ≥150 words of real content:}
- {PREV_TEX} — for voice and terminology matching
- Chapter-specific files from .claude/skills/context-gather.md table for Chapter {N}:
{FOR EACH file from context-gather.md: list path + one-line why}

---

{If mode == revise:}
REVISE MODE: read the previous review files and fix the issues raised, preserving what works:
- evaluation/review/sections/ch{N}-{X.Y}-round{R-1}-coherence.md
- evaluation/review/sections/ch{N}-{X.Y}-round{R-1}-quality.md
- evaluation/review/sections/ch{N}-{X.Y}-round{R-1}-checks.md

{If mode == auto-revise:}
AUTO-REVISION MODE: fix ONLY these consolidated critical issues. Do NOT rewrite passages that passed review.
ISSUES TO FIX:
{Paste consolidated critical issues from Step 6.5}
```

The writer's system prompt handles output format (LaTeX only, starts with \section{}), source rules, anchor rules, glossary discipline, paragraph discipline, and self-check. The orchestrator does not repeat them.

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
3. **Citation keys**: Extract all `\parencite` and `\textcite` commands from the writer output (regex must match `\parencite` not `\parcite`). For each, extract the citation key(s). Verify each key exists in `result/references.bib`.
   Handle: `\parencite{key}`, `\parencite{key1,key2}`, `\parencite[see][p.~12]{key}`, `\textcite{key}`
   Compare the extracted key set against the set already validated in Step 1c. If the writer added keys not in the Step 1c set, flag those as "new keys to validate" and run the Bash gate from Step 1c #3 only on those new keys (do not re-validate the keys 1c already checked).
4. **Source notes**: This check is satisfied by Step 1c (Bash validation already ran for the Step 1c key set) plus the diff in #3 above. **The orchestrator does NOT re-Read source notes content here.** If #3 flagged new keys, those are validated by the same Bash idiom; if any FAIL, that is a hard fail.
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
- Invalid citation key — list missing keys. The thesis-source set is locked — instruct the writer to use a different existing key from BIB_SLICE rather than introducing a new one. Never auto-add to references.bib.
- Missing source notes — list bibkeys whose source notes file is missing or unfilled. This is a repository-state error (file deleted or path wrong); escalate to the user, do not propose extraction.
- Compilation fail — show LaTeX error output; user fixes manually.

Mark section as `drafted-needs-revision` in STATUS.md. Do not run review agents. Manual fix is faster and safer than automated retry for these cases.

**If no hard fails:** Proceed to Step 5.

## Step 5: REVIEW (2 agents)

Only reached if all hard checks pass.

Spawn `section-coherence` and `section-quality` subagents in parallel — single message with both Agent calls. **Their contexts are independent by design (each is a fresh subagent). Never share state between them.**

Both subagents' system prompts already contain:
- Their full check list and JSON gate format
- The "thesis-source set is locked" rule (use existing BIB_SLICE keys, never propose new sources)
- The "if pass: false, at least one critical issue" rule
- Source-notes verification instructions (read `context/docs/method/sources/raw/extracted/{bibkey}.md`)

The orchestrator only passes per-section inputs. Do NOT repeat the rules.

**Build the common base, then spawn:**

```
Agent({
  subagent_type: "section-coherence",
  prompt: <COHERENCE_USER_MESSAGE>
})
```

```
Agent({
  subagent_type: "section-quality",
  prompt: <QUALITY_USER_MESSAGE>
})
```

**COHERENCE_USER_MESSAGE template:**

```
Section: {X.Y}, Chapter {N}
Target .tex: {TEX_FILE}

---

OUTLINE_SLICE (§{X.Y} ¶-plan + Evidence Marker Taxonomy header):
{paste output of slice A from Step 1.5 verbatim}

REF_ANALYSIS_SLICE (§7 Transferable A-Markers + Chapter {N} per-chapter pattern + Cross-chapter A-markers):
{paste output of slice C from Step 1.5 verbatim}

BIB_SLICE (the locked source set — your fixes must reference EXISTING keys only):
{paste output of slice D from Step 1.5 verbatim}

---

Files to read:
- {TEX_FILE} — only the content under \section{...} for §{X.Y}
- context/thesis-spine.md
- context/context.md
- evaluation/review/lessons-learned.md
- For each cite key used in the section: context/docs/method/sources/raw/extracted/{bibkey}.md
{If Chapter {N} is 4, 5, or 6:}
- evaluation/theory-usage.md (for the theory-tracker check)
{If there are previous sections in this chapter before {X.Y}:}
- {previous section .tex content for continuity}
```

**QUALITY_USER_MESSAGE template:**

```
Section: {X.Y}, Chapter {N}
Target .tex: {TEX_FILE}

---

OUTLINE_SLICE (§{X.Y} ¶-plan + Evidence Marker Taxonomy header):
{paste output of slice A from Step 1.5 verbatim}

RUBRIC_SLICE (Chapter {N} A-grade criteria + cross-chapter A-markers):
{paste output of slice B from Step 1.5 verbatim}

REF_ANALYSIS_SLICE (§7 Transferable A-Markers + Chapter {N} per-chapter pattern + Cross-chapter A-markers):
{paste output of slice C from Step 1.5 verbatim}

BIB_SLICE (the locked source set — your fixes must reference EXISTING keys only):
{paste output of slice D from Step 1.5 verbatim}

---

Files to read:
- {TEX_FILE} — only the content under \section{...} for §{X.Y}
- evaluation/evaluation.md (chapter-{N} checklist)
- evaluation/review/lessons-learned.md
- context/docs/method/academic-writing-guide.md (Writing Action Levels section)
- For each cite key used in the section: context/docs/method/sources/raw/extracted/{bibkey}.md
```

## Step 6: REPORT

Save review outputs to:
- `evaluation/review/sections/ch{N}-{X.Y}-round{R}-coherence.md`
- `evaluation/review/sections/ch{N}-{X.Y}-round{R}-quality.md`

Parse the JSON from each agent's response.

### Gate parsing
- **Coherence**: Pass if all critical counts == 0 AND spine_serves == true AND theory_missing_from_tracker == 0.
- **Quality**: Pass if quality_grade == "A" AND depth_assessment == "genuine" AND critical_source_issues == 0 AND naturalness_score >= 4.

Determine status:

| Condition | Status |
|-----------|--------|
| All gates pass | `drafted-reviewed` |
| Any coherence critical > 0 or spine false | `drafted-needs-revision` |
| Quality grade B/C or depth "surface" or critical_source_issues > 0 or naturalness_score < 4 | `drafted-needs-revision` |

Print summary — keep it tight, three lines max for the happy path:

```
§{X.Y} R{R} → {STATUS} · {N} words · {TEX_FILE}
checks ✓ · coherence ✓ ({Nc} minor) · quality {A|B|C} {genuine|surface} {integrated|mixed|name-dropped} {nat}/5
warnings: {list short, comma-separated, or "none"}
```

If anything failed, replace the matching line with the concrete failure(s):
- `checks ✗` → list each failed check (placeholders / forbidden voice / invalid keys / compile error) with one-line detail
- `coherence ✗` → list the critical issues with paragraph + one-line diagnosis
- `quality ✗` → state which gate failed (grade B/C, surface, name-dropped, naturalness <4) with the specific failing field

Skip lines with nothing to say (no warnings → drop the warnings line entirely).

→ Go to Step 6.5.

## Step 6.5: AUTO-REVISE

### Auto-revise (if drafted-needs-revision)

**Max 3 total rounds.** Round 1 = initial write, round 2–3 = auto-revisions. Round 4 must never be created.

```
IF status == "drafted-needs-revision" AND round < 3:
  1. Collect all issues where severity == "critical" AND fixable == true
     from coherence and quality JSON.
     A "weak/wrong source fit" is fixable when an alternative key exists in BIB_SLICE — the writer just swaps to that key. If no alternative exists, the fix is to weaken/remove the claim.

  2. IF no fixable critical issues exist:
       Status: "drafted-needs-manual-fix"
       Report: "Review failed but no fixable critical issues. Manual intervention required." If the blocker is repository-state (e.g. a source notes file is missing), name the file and tell the user to restore it; do not propose source extraction.
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
  → Run Step 6.6 LESSONS-LEARNED HARVEST before declaring complete.

  {If drafted-needs-revision (should not happen — auto-revise handles this):}
  ⚠️ Issues to fix — auto-revise will attempt...

  {If drafted-needs-manual-fix:}
  🛑 Pipeline exhausted auto-fix attempts (max 3 rounds). Manual intervention required.
  Remaining issues:
    1. [{source}] {description}
    2. [{source}] {description}
  → Fix manually and run /write-section {X.Y} again.
  → Still run Step 6.6 LESSONS-LEARNED HARVEST on the latest round's reviews — manual-fix sections often produce the most generalisable patterns.
```

## Step 6.6: LESSONS-LEARNED HARVEST (mandatory, runs after final round)

This step prevents generalisable reviewer wisdom from being lost when a section passes (`drafted-reviewed`) or stalls (`drafted-needs-manual-fix`). It is **not optional** — the orchestrator does not declare the pipeline complete until this step has run.

**When to run:**
- After every final round (whether status is `drafted-reviewed` or `drafted-needs-manual-fix`).
- Skip during intermediate auto-revise rounds — those will be re-reviewed and a fresh harvest will run on the final round.

**What to scan:**
- Coherence agent JSON: `issues[]` where `severity == "minor"`, plus all `suggestions[]`, plus `notes`.
- Quality agent JSON: `issues[]` where `severity == "minor"`, plus all `suggestions[]`, plus `weakest_aspect`/`fix`.
- Critical issues are NOT harvested here — they were either auto-revised away or escalated to manual-fix; the harvesting target is the wisdom that does not gate the section.

**Classification (deterministic — apply exactly):**

A finding is **GENERAL** (→ propose adding to `evaluation/review/lessons-learned.md`) if ANY of these is true:
1. It names a source bibkey or source TYPE (`pinedo2016scheduling`, "any algorithmic primary source", "interview-derived theme") and the rule applies to other sections that cite the same key/type.
2. It names a chapter or chapter-type (`Ch 2 theory sections`, `any methodology section`, `findings chapters`).
3. It names a paragraph type (`definitional paragraphs`, `taxonomy paragraphs`, `transition paragraphs`, `RQ-answer paragraphs`).
4. It names a phrase or word to ban / prefer (`"interviews indicate"`, `"limited"`, `"first-fit"`, `"various"`).
5. It names a structural pattern (actor-as-punchline, decoration-in-cite-paraphrase, definition-consistency, taxonomy-after-detail, late-narrative-framing).
6. It cites the writing-action-level for a chapter-type (`EXPLAIN-level chapters`, `DISCUSS-level chapters`).
7. It is a supervisor-style directive that applies beyond the immediate section.

A finding is **SECTION-SPECIFIC** (→ leave in the round file, do not surface) if ALL of these are true:
- It only references §X.Y or ¶N (no broader pattern claim).
- It points at a single sentence/transition unique to this draft.
- It would not apply to any other section in the thesis writing-order.

**If in doubt, classify as GENERAL.** A false positive costs one user `n` keystroke; a false negative loses the rule forever.

**Dedup against existing rules first.** Before listing a GENERAL candidate, grep `evaluation/review/lessons-learned.md` for substantively similar content — same headline phrase, same source bibkey, or same chapter+pattern combination. If a match exists, skip the candidate and log it in the round file as "already promoted in {existing rule heading}". Only surface NEW patterns to the user.

**Print three separate lists.** Each item has enough detail that the user can decide without asking for `detail N` in the typical case. Skip lists that have zero items.

```
━━ HARVEST §{X.Y} R{R} ━━

GENERALISABLE → propose adding as permanent rule in lessons-learned.md ({K} candidates)

  1. PROPOSED RULE: {one-line rule headline, ≤ 80 chars}                       [{src}]

     What it means in practice:
       {2–3 sentence concrete explanation in plain language — what would change
       in writing if this rule was enforced. Use a tiny before/after example
       where it helps the user grasp it.}

     What the reviewer flagged:
       "{verbatim quote from reviewer JSON, ≤ 200 chars; trim to the part that
       triggered this candidate}"

     If you approve:
       Added under § {target heading in lessons-learned.md}. Will be enforced on
       {specific sections — e.g. §2.2, §5.1.2, §6.2} and checked by writer +
       both reviewers on every future /write-section run touching {scope}.

  2. PROPOSED RULE: {headline}                                                  [{src}]

     What it means in practice:
       {explanation}

     What the reviewer flagged:
       "{verbatim quote}"

     If you approve:
       Added under § {heading}. Will be enforced on {scope}.

  → reply: y N  |  n N  |  y all  |  n all  |  edit N  |  detail N

─────────────────────────────────────────

SECTION-SPECIFIC → fix in §{X.Y} only? ({L} findings)
  3. {one-line of what reviewer flagged}                               [{src}]
     where: {paragraph + short anchor passage from prose}
     fix:   {reviewer's suggested fix, or "manual judgement needed"}

  4. {one-line}                                                        [{src}]
     where: {paragraph + anchor}
     fix:   {suggestion}

  → reply: fix N  |  fix all  |  skip N  |  detail N

─────────────────────────────────────────

DUPLICATES → already in lessons-learned, skipped ({D} items)
  5. {headline} → § {existing rule heading}
  6. {headline} → § {existing rule heading}
```

If a list is empty, omit the entire block (heading + items). If everything is empty, print: `✅ No reviewer findings this round.`

**Source short-forms in `[{src}]`:**
- `coh.sug2` = coherence agent, suggestions[2]
- `qua.iss1 minor` = quality agent, issues[1] severity:minor
- `coh.notes`, `qua.weakest`, `qua.fix` = top-level fields

**User response handling:**

For GENERALISABLE list:
- `y N` / `y all` / `y N,M` → append full entry (Rule / Why / When to apply / Source) under closest existing heading in `evaluation/review/lessons-learned.md` (Source faithfulness / Chapter purity / Narrative framing / Structure / Empirical scope / Coverage / Terminology / Reader accessibility — new heading only if none fits). Cross-link in the round file: "→ promoted to lessons-learned § {heading} on {YYYY-MM-DD}".
- `n N` / `n all` → log declined items in the round file as "considered, declined" + reason if supplied.
- `edit N` → ask the user for revised rule text; apply that.
- `detail N` → print the verbatim reviewer passage + the full proposed lessons-learned entry. Wait for follow-up.

For SECTION-SPECIFIC list:
- `fix N` / `fix all` → open the section .tex at the flagged location and propose the suggested fix. Wait for user confirmation per edit (do not auto-edit prose).
- `skip N` / `skip all` → log as "noted, not acted on" in the round file. The reviewer's flag stays visible there for future re-revision passes.
- `detail N` → print the verbatim reviewer passage + surrounding context.

**Default behaviour when user response is ambiguous or absent:** print the lists, wait. Do not auto-apply, do not auto-edit prose.

**Only after every item has been resolved (applied, declined, or explicitly deferred):** update STATUS.md and end the pipeline. Print the round file path so the user can re-read declined items later.

Update STATUS.md — find or create the section tracking table for Chapter {N}. Update the row for section {X.Y} with current results.
