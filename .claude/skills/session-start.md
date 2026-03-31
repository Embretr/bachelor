# Session Start — Required Ritual

> Run this sequence at the start of every Claude session.
> Do not skip steps. Do not combine with writing in the same message.
> This ritual is what makes the workflow repeatable and coherent.

---

## Step 1 — Load the backbone (always, in this order)

Paste these files into the session context:

1. `context/index.md` — understand what context exists
2. `context/context.md` — thesis identity, RQ, scope, status
3. `context/thesis-spine.md` — one-sentence argument per chapter
4. `evaluation/a-grade-rubric.md` — A criteria (read carefully)
5. `STATUS.md` — what is done, in progress, not started

---

## Step 2 — State the task

Tell Claude exactly what the task is, in one sentence:

```
Task: Write section [X.Y] of Chapter [N] — [section title]
```

or:

```
Task: Revise section [X.Y] — [what is wrong and what should be better]
```

or:

```
Task: Run red-thread check on Chapter [N] (new session, no writer context)
```

---

## Step 3 — Load chapter-specific context

Use `context/index.md` Quick Load Guide to identify which files to load.

Paste the relevant files into the session.

For writing:
- `context/outline.md` — section plan for this chapter
- `context/glossary.md` — domain glossary
- Chapter-specific files (see index.md)
- Previous chapter .tex file (for continuity)

For review:
- The chapter .tex file to be reviewed
- `evaluation/grading-guidelines.md` (if filled)
- Previous review output from `evaluation/review/`

---

## Step 4 — Verify prerequisites

Before Claude starts writing, verify:

- [ ] The section to write has a detailed plan in `context/outline.md`
- [ ] The research question is known (from `context/context.md`)
- [ ] Any technical claims (algorithm, architecture) have source files in `context/docs/tech/`
- [ ] Any interview claims have source in `context/interviews-summary.md`
- [ ] Any citations needed have BibTeX keys in `result/references.bib`

If a prerequisite is missing, note it as `[FILL IN: X needed]` in the output and continue.

---

## Step 5 — Write or review

Follow the appropriate prompt template:
- Writing: `.claude/agents/writer.md`
- Red-thread: `.claude/agents/red-thread.md` (new session only)
- Quality: `.claude/agents/quality.md` (new session only, after red-thread)

---

## After the Session

- Paste completed section into the correct `result/chapters/` file
- Update `result/notes.md` with: what was written, decisions made, open questions
- Update `STATUS.md`: mark section as drafted / reviewed / revised
- Commit with: `git commit -m "ch[N]: draft section [X.Y] — [section title]"`

---

## Session Types — What Each Does

| Session type | What it does | Can be combined with? |
|---|---|---|
| **Writer** | Produces new text for one section | Nothing else |
| **Red-thread** | Checks argument coherence, no grammar | Nothing else |
| **Quality** | Grades chapter against A criteria | Nothing else |
| **Revision** | Fixes specific issues from red-thread/quality | Can be combined with writer for minor fixes |
| **Context update** | Updates a context file with new information | Always safe to combine |

Red-thread and quality MUST be separate sessions from the writer. The writer session has a bias toward producing content; the reviewer session needs a clean perspective.
