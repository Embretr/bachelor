---
name: log-supervisor-feedback
description: "Log NTNU supervisor directives into the three-file system: chronological log, generalised rules, section-specific calibration. Usage: /log-supervisor-feedback (then paste raw notes)"
---

# Log Supervisor Feedback Pipeline

You are the orchestrator. The user has had a supervisor meeting and is providing raw notes (typically Norwegian, sometimes mixed Norwegian/English). Your job is to translate those notes into the three-file system defined in `CLAUDE.md` Critical Workflow Rule #4 — and never improvise the file targets.

## The three-file system (read CLAUDE.md #4 if anything is unclear)

| File | What goes here | Loaded by |
|------|----------------|-----------|
| `context/docs/project/supervisor-feedback.md` | Verbatim quote of every directive, dated, with scope and a pointer to the mirrored target | Session-start ritual via `context/index.md` |
| `evaluation/review/lessons-learned.md` | Generalised rules — directives that apply beyond the immediate section | Writer agent + both reviewer agents in `/write-section` |
| `context/outline.md` | Section-specific calibration — directives that bind only to one or a few sections | Writer agent at draft time |

**Memory (`/Users/mikaelstray/.claude/projects/.../memory/`) is forbidden** for supervisor directives — it is per-machine, but the thesis is co-authored. Do not save anything here.

---

## Input

The user pastes raw notes after invoking the command. If no notes were pasted, ask: "Paste the raw notes from the supervisor meeting. Include the meeting date if it is not today."

Parse:
- **Meeting date** — default to today (`date +%Y-%m-%d`) unless the user states otherwise
- **Meeting context** — one sentence the user can confirm (which sections / chapters / drafts the supervisor was reviewing). If unclear from the notes, ask before proceeding.
- **Discrete directives** — split the notes into atomic points. One directive per row.

---

## Step 1: VALIDATE

Read the three target files and `CLAUDE.md` #4 to anchor the format:

- `context/docs/project/supervisor-feedback.md` — confirm the existing structure (date heading + table + section-level calibration block)
- `evaluation/review/lessons-learned.md` — confirm the existing categories and rule format (Rule / Why / When to apply / Source)
- `context/outline.md` — confirm the existing `> **Supervisor calibration {date}**` block format used under affected section blocks

If any of the three files are missing → **STOP** and tell the user the three-file scaffolding has not been initialised. Do not create files from scratch.

---

## Step 2: CLASSIFY

For every discrete directive, classify into exactly one primary category:

| Category | Signal | Mirrored to |
|----------|--------|-------------|
| **Generalisable** | The directive describes a writing principle that applies beyond one section ("be careful with claims", "definitions consistent", "transitions") | `lessons-learned.md` (new rule) — also referenced from `supervisor-feedback.md` row |
| **Section-specific** | The directive binds to one or a few sections only ("define TMS this way in §2.3", "name Timpex in ¶2") | `outline.md` calibration block under the affected section — also referenced from `supervisor-feedback.md` row |
| **Project-context only** | The directive is a fact, decision, or stakeholder statement that does not become a writing rule (e.g., a deadline change, a new constraint from Admmit) | `supervisor-feedback.md` only |

A directive can have both generalisable AND section-specific consequences (e.g., "definitions consistent" is generalisable; "in §2.3 the TMS definition specifically must stay comprehensive" is section-specific). In that case, mirror to BOTH and reference both in the log row.

---

## Step 3: DRAFT

Produce three artefacts in memory (do not write yet):

### 3a. New log entry for `supervisor-feedback.md`

Format (match the existing 2026-05-02 entry exactly):

```
## {DATE} — {short title summarising the meeting topic}

Context: {one or two sentences naming what the supervisor was reviewing — the user confirmed this in Step 1 input}.

| # | Directive (verbatim) | Scope | Mirrored to |
|---|----------------------|-------|-------------|
| 1 | "{verbatim quote — keep Norwegian if Norwegian, English if English}" | {one phrase: empirical scope / definitional consistency / etc.} | {lessons-learned → *Rule name* + outline.md §X.Y / lessons-learned → *Rule name* / outline.md §X.Y / log only} |
| 2 | ... | ... | ... |

**Section-level calibration for the rewrite:** (only if at least one directive is section-specific)

- **§X.Y ({Section name}).** {The supervisor's actual section-specific instruction translated to plain English / Norwegian as written.}
- **§X.Y ({Section name}).** ...
```

### 3b. New rule(s) for `lessons-learned.md`

For each generalisable directive, draft a rule in this exact format:

```
## {Category — pick one of: Empirical scope / Coverage / Terminology / Reader accessibility / Flow / Source faithfulness / Chapter purity / Narrative framing / Structure — or propose a new category if none fit}

### {Short imperative rule title — verb-led, ≤90 chars}
- **Rule:** {One or two sentences. State the rule, then give a concrete contrast (do this not that) when useful.}
- **Why:** Supervisor {DATE}: "{verbatim quote}." {One sentence on the mechanism — why violating this loses credibility / drifts the argument / etc.}
- **When to apply:** {Which chapters or section types. Be specific — don't write "all writing".}
- **Source:** Supervisor {DATE} (logged in `context/docs/project/supervisor-feedback.md`).
```

If a category does not exist yet in `lessons-learned.md`, propose creating it with a `## {Category}` header and a `---` separator above and below per existing convention.

If a directive only **reinforces** an existing rule rather than introducing a new one, do NOT write a new rule — instead, append `; re-confirmed by supervisor {DATE} (logged in ...)` to the existing rule's `**Source:**` line.

### 3c. New calibration block(s) for `outline.md`

For each section that has section-specific directives, draft a block to insert immediately under the section header (after the `**X.Y Section name** (~N pages, ...)` line, before the first `- ¶1:`):

```
> **Supervisor calibration {DATE}** (full log: `context/docs/project/supervisor-feedback.md`):
> - {Directive 1 in plain prose, no quotes, actionable for the writer}
> - {Directive 2}
> - {...}
```

If a `> **Supervisor calibration {EARLIER-DATE}**` block already exists for the same section, **do not duplicate** — add a second block dated with the new date below it. Earlier guidance stays visible.

If the section also has stale `MUST EVIDENCE: interview-derived ...` markers in Ch 2 (forbidden by the chapter purity rule in `lessons-learned.md`), flag this in your draft proposal so the user can decide whether to fix in the same commit.

### 3d. Index update (only if needed)

Check `context/index.md` — if `supervisor-feedback.md` is not yet listed, add the row. If it is already listed, no change.

---

## Step 4: PROPOSE

Show the user a single message with all proposed changes. Use this exact structure:

```
## Proposed changes from supervisor meeting {DATE}

### `context/docs/project/supervisor-feedback.md` — new entry
{full text of the new entry from 3a}

### `evaluation/review/lessons-learned.md` — {N new rules / X reinforcement(s)}
{full text of each new rule from 3b, OR the diff for any reinforcement to an existing rule}

### `context/outline.md` — calibration blocks for §X.Y, §A.B, ...
{full text of each new block from 3c, with the section header it goes under}

### `context/index.md` — {row added / unchanged}

### Stale markers flagged (if any)
{list of any `MUST EVIDENCE: interview-derived` markers in Ch 2 or other purity violations the user should consider fixing in the same commit}

---

Approve all (y) / approve with edits (specify which) / abort (n)?
```

Wait for explicit user response. Do NOT write any file before approval.

---

## Step 5: WRITE

On approval (`y`):

1. **`supervisor-feedback.md`** — insert the new entry **above** the most recent existing entry (chronological order: newest first matches the existing file's ordering).
2. **`lessons-learned.md`** — append each new rule under its category header. If a new category was introduced, create the category section with `## {Category}` and `---` separators in the same style as existing categories. For reinforcements, edit the `**Source:**` line of the existing rule.
3. **`outline.md`** — insert each calibration block at the correct location (under the section header, before ¶1).
4. **`context/index.md`** — add the row if missing.

Use the `Edit` tool for files that already exist (precise insertion). Use `Write` only if a file genuinely does not exist — but per Step 1 validation, all three files must already exist or the pipeline stops.

---

## Step 6: REPORT

Print a 5-line summary:

```
Logged supervisor meeting {DATE}.
- {N} directives logged in supervisor-feedback.md
- {M} new rule(s) in lessons-learned.md (categories: ...) {+ K reinforcement(s)}
- {P} section calibration block(s) added to outline.md (sections: §X.Y, ...)
- index.md: {row added / unchanged}
- Stale markers fixed: {Y / none / deferred — listed in flagged section above}
```

End. Do not propose follow-up tasks unless the user asks.

---

## Hard rules

1. **Never store supervisor directives in user memory.** Memory is per-machine; the thesis is co-authored. The three-file system is the single source of truth.
2. **Never invent a quote.** Verbatim quotes in the log must come from the user's notes. If the notes paraphrase the supervisor, mark the row's `Directive` field as a paraphrase: `(paraphrased) {text}`.
3. **Never delete or rewrite previous supervisor entries.** Strike through with date + reason if a directive is later revised by the supervisor; do not erase history.
4. **One meeting = one log entry.** Do not split one meeting across two date headings.
5. **Cross-link rigorously.** Every row in the log table's `Mirrored to` column must point to a real target. Every new rule's `Source:` line must point back to the log. Every outline calibration block must reference the log path.
