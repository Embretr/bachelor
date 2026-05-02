# Session Start — Required Ritual

> Run this sequence at the start of every Claude session.
> The actual writing and reviewing is automated by `/write-section` and `/review-chapter`. This ritual is what loads the orientation context Claude needs to invoke them correctly.

---

## Step 1 — Load the backbone (always, in this order)

Read these files into the session context:

1. `context/index.md` — understand what context exists and which files map to which chapter
2. `context/context.md` — thesis identity, RQ, scope, status
3. `context/thesis-spine.md` — one-sentence argument per chapter + the locked Anchor Concepts
4. `evaluation/a-grade-rubric.md` — A criteria
5. `STATUS.md` — what is done, in progress, not started

---

## Step 2 — Decide the task

Pick the appropriate command:

| Goal | Command |
|---|---|
| Draft a new section | `/write-section X.Y` |
| Revise a section using prior reviews | `/write-section X.Y` (it auto-detects existing content and offers revise mode) |
| Integration check on a finished chapter | `/review-chapter N` |
| Extract structured notes from a source PDF | `Agent({subagent_type: "source-extractor", prompt: "Bibkey: {bibkey}"})` |
| Log supervisor feedback | `/log-supervisor-feedback` |

The skills handle prerequisite validation, deterministic checks, subagent spawning, and report generation. The user does not paste prompts manually anymore.

---

## Step 3 — Verify prerequisites if writing a new section

Before running `/write-section X.Y`, confirm:

- [ ] The section has a paragraph-level plan in `context/outline.md` (look for `- ¶` markers under §X.Y). The skill will hard-stop if missing.
- [ ] Any new MUST CITE bibkeys exist in `result/references.bib` AND have source notes in `context/docs/method/sources/raw/extracted/{bibkey}.md`. The skill validates this in Step 1c.

If anything is missing, fix it before invoking the command — the skill will refuse to start otherwise.

---

## Step 4 — Run the command and respond to the report

The skill will:
- Spawn subagents (writer, then in parallel: section-coherence + section-quality)
- Print a tight 2–3 line status line + JSON gates
- Auto-revise up to 3 rounds if reviewers fail with fixable critical issues
- Surface generalisable lessons-learned candidates for your `y / n / edit` answer

Your role: answer harvest candidates, decide on `drafted-needs-manual-fix` cases, and update `STATUS.md` only when you are satisfied with the section.

---

## After every chapter is `drafted-reviewed` for all sections

1. Run `/review-chapter N` for chapter integration check
2. **Spine sync check**: compare the chapter's actual argument against `context/thesis-spine.md`. If shifted, update the spine before moving on.
3. **Human approval**: review the chapter yourself. Mark as `approved` in STATUS.md only when you are satisfied.

---

## Subagents available (defined in `.claude/agents/`)

| Subagent | Used by | Mandate |
|---|---|---|
| `writer` | `/write-section` Step 2 | Drafts section LaTeX from outline + slices |
| `section-coherence` | `/write-section` Step 5 | Logical coherence + structure + MUST markers + theory tracker |
| `section-quality` | `/write-section` Step 5 | A-grade rubric + source integration + AI-voice (naturalness) |
| `chapter-redthread` | `/review-chapter` Step 2 | Cross-section transitions, repetition, RQ, terminology, anchor coherence |
| `chapter-sensor` | `/review-chapter` Step 2 | Per-NRT-criterion grading + A-markers + anchor drift |
| `source-extractor` | Standalone | Extracts structured notes from one source PDF |

Each subagent has its own context window — the orchestrator passes only inline slices and file paths, not full files.
