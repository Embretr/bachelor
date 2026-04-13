# Ressursplanlegger — Bachelor Thesis · Codex Instructions

## The Mandate

This thesis must receive an A. Every word Codex produces is evaluated against that standard before it is written. If a change does not move the thesis closer to an A, it is not made.

---

## The Three-Folder System

The entire workflow rests on three folders:

| Folder | Purpose | When to read |
|---|---|---|
| `context/` | Everything about the project — what it is, what was found, what was built | Before writing anything |
| `evaluation/` | Everything about how the work is judged — grading criteria, quality checks | Before and after writing |
| `result/` | The thesis itself — `.tex` files, references, working notes | When writing or revising |

**Never write without loading context. Never output without checking evaluation.**

---

## Before Every Session — Required Ritual

Run this sequence at the start of every session, every time:

```
1. Read context/index.md           → understand what context exists
2. Read context/context.md         → thesis identity and research question
3. Read context/thesis-spine.md    → the argument backbone
4. Read evaluation/a-grade-rubric.md → A-grade criteria
5. Load chapter-specific files     → see context/index.md for which ones
6. Read STATUS.md                  → current progress, what is done/in-progress
```

Do not skip any of these. If a file is missing, note it and continue with what exists.

---

## The Strict Workflow (per task)

### Writing a new section

Use the automated pipeline (works in both Claude Code and Codex):

```
/write-section 2.1
```

This single command validates, writes, checks, and reviews the section automatically.
See `.claude/skills/write-section/SKILL.md` for the full pipeline specification.
If section has existing content, choose: revise (recommended) or overwrite.

### Reviewing a completed chapter

After all sections in a chapter are `drafted-reviewed`:

```
/review-chapter 2
```

Runs 2 integration agents (red-thread + sensor). Human makes final approval.
See `.claude/skills/review-chapter/SKILL.md` for details.

### Writing order

```
2.1 → 2.2 → 2.3 → 2.4 → 3.1 → 3.2 → 3.3 → 3.4 → 3.5
→ 4.1 → 4.3 → 4.2 → 4.4 → 4.5 → 5.1 → 5.2 → 5.3
→ 5.4 → 5.5 → 5.6 → 1.1 → 1.2 → 1.3 → 1.4 → 6.1 → 6.2 → 6.3
→ Abstract + Sammendrag (last)
```

---

## Critical Workflow Rules

These rules are non-negotiable. They override convenience and save more time than they cost.

### 1. Section plan before writing — always

The section plan (`context/outline.md`) is more important than the prompt itself. If you know exactly what each paragraph should say, the output will always be usable. Without it, the result will be generic filler that takes longer to fix than to write from scratch. **Never start writing a section unless `context/outline.md` contains a concrete, paragraph-level plan for that section.** If the plan is missing or vague, stop and ask the user to fill it in before proceeding.

### 2. Writer and red-thread must never share a session

The writer agent is set up to produce — it is not objective. The red-thread agent needs a clean slate without the preceding context to see flaws. Running both in the same session contaminates the review. **Always open a new, separate Codex session for red-thread and quality checks.** This is already stated in the workflow above, but it bears repeating: violating this rule invalidates the review.

### 3. Update thesis-spine.md after every chapter

If a finished chapter shifts the argument even slightly, update `context/thesis-spine.md` immediately. The spine is the single source of truth for cross-chapter coherence. If it drifts out of sync with what was actually written, every subsequent chapter risks building on a stale foundation. **After completing any chapter draft, compare what was written against the spine and update if needed — before moving on.**

---

## After Every Task — Required Post-Task Ritual

### When using `/write-section` (automated pipeline)

The pipeline handles quality ranking, checks, and review automatically.
After the pipeline reports:

1. **If `drafted-needs-revision`** — fix issues and re-run `/write-section X.Y` (revise mode)
2. **If `drafted-reviewed`** — move to the next section

### After completing a chapter (all sections `drafted-reviewed`)

1. Run `/review-chapter N` for integration check
2. **Spine sync check:** Compare chapter argument against `context/thesis-spine.md`. Update if shifted.
3. **Human approval:** Mark `approved` in STATUS.md only when you are satisfied.

### Step 2 — Workflow reflection

After every session, check:

- Was any context missing that would have improved the output?
- Was any instruction in the prompts unclear or insufficient?
- Did the evaluation criteria miss something relevant to this section?
- Was there a better order to load context files?

If yes to any — write a proposal in the format below.

### Step 3 — Workflow improvement proposal

If a workflow improvement is identified, present it exactly in this format:

```
---
WORKFLOW UPDATE PROPOSED

Triggered by:     [what happened — what was missing or unclear]
Change type:      [new rule / updated rule / new context file / updated index entry]
File to edit:     [AGENTS.md / .claude/agents/X.md / context/index.md / evaluation/X.md]

Proposed change:
[exact text to add or replace — quote the current text if modifying existing content]

Why this improves output:
[one sentence]

Apply this update? (y/n)
---
```

**Wait for explicit user response before editing any workflow file.**
If the user says yes → make the edit immediately, then log it in `evaluation/workflow-improvements.md`.
If the user says no → log the rejection in `evaluation/workflow-improvements.md` with their reason.

Do not propose more than two improvements per session.
Do not propose trivial changes (spelling, formatting) — only changes that affect output quality.

---

## What the AI Must Never Do

- Invent references, citations, or data — use only sources in `result/references.bib`
- Claim the system has features not in `context/scope.md`
- Use "we believe", "we think", "we found" — use impersonal academic constructions
- Write outside the scope of the current section — not the next section, not the chapter introduction
- Assume something is tested unless it appears in `context/docs/requirements/requirements-traceability.md`
- Change the research question — use it verbatim from `context/context.md`
- Run writer and red-thread in the same session — they require separate contexts
- Make changes that do not improve the thesis grade

---

## Repository Structure

```
bachelor/
├── AGENTS.md                    ← you are here — read every session
├── STATUS.md                    ← progress tracker — read every session
├── Makefile                     ← run `make` to compile PDF
├── main.tex                     ← root LaTeX file
│
├── context/                     ← ALWAYS READ BEFORE WRITING
│   ├── index.md                 ← MAP: what is in context/ and when to load it
│   ├── context.md               ← thesis identity, research question, stack, scope
│   ├── thesis-spine.md          ← one-sentence argument per chapter
│   ├── outline.md               ← section-level outlines with content notes
│   ├── glossary.md              ← domain glossary — use these terms only
│   ├── scope.md                 ← explicit in/out of scope
│   ├── interviews-summary.md    ← distilled findings from 7 interviews
│   ├── fitgap-summary.md        ← fit/gap analysis
│   └── docs/                   ← supporting documentation (see index.md)
│       ├── requirements/        ← functional + non-functional requirements
│       ├── method/              ← research design, literature, theoretical framework
│       ├── project/             ← sprint log, decision log, change log
│       └── tech/                ← algorithm, architecture, data model, API, stack
│
├── evaluation/                  ← READ BEFORE AND AFTER WRITING
│   ├── a-grade-rubric.md        ← detailed A criteria per chapter — primary quality gate
│   ├── grading-guidelines.md    ← official sensor guidelines (fill from PDF)
│   ├── evaluation.md            ← distilled chapter-level checklist
│   └── review/                  ← output from red-thread and quality agents
│       ├── redthread-chN.md
│       └── quality-chN.md
│
├── .claude/                     ← Codex agent and skill definitions
│   ├── agents/
│   │   ├── writer.md            ← writer agent template
│   │   ├── red-thread.md        ← red-thread agent template
│   │   └── quality.md           ← quality/examiner agent template
│   └── skills/
│       ├── session-start.md     ← ritual: what to load at session start
│       └── context-gather.md    ← which files to load per chapter
│
└── result/                      ← the thesis
    ├── notes.md                 ← working notes Codex maintains
    ├── references.bib           ← all references (APA 7 / biblatex)
    └── chapters/
        ├── ch1/
        │   ├── ch1-introduction.tex
        │   └── notes.md
        ├── ch2/
        │   ├── ch2-theory.tex
        │   └── notes.md
        ├── ch3/
        │   ├── ch3-method.tex
        │   └── notes.md
        ├── ch4/
        │   ├── ch4-findings.tex
        │   └── notes.md
        ├── ch5/
        │   ├── ch5-discussion.tex
        │   └── notes.md
        └── ch6/
            ├── ch6-conclusion.tex
            └── notes.md
```

---

## Writing Rules

- Write in **formal, academic English**
- Use **passive or impersonal constructions** — avoid "we believe" / "we think"; prefer "it can be argued" / "the results suggest" / "the interviews indicate"
- Use `\parencite{key}` for (Author, Year) citations
- Use `\textcite{key}` for Author (Year) in-text citations
- Add all new sources to `result/references.bib` — never invent a source
- Stay strictly within the scope defined in `context/scope.md`
- Use the exact terminology defined in `context/glossary.md`
- Write one section at a time — do not jump ahead

## LaTeX Conventions

- Figures: `figure` environment with `\caption{}` and `\label{fig:name}`
- Tables: `table` + `booktabs` (`\toprule`, `\midrule`, `\bottomrule`)
- Sections: `\section{}`, `\subsection{}`, `\subsubsection{}`
- Cross-references: `\Cref{label}` (capitalised) or `\cref{label}` (lowercase)
- No hardcoded page breaks — use `\clearpage` sparingly

## Compiling

```
make        # compile once → main.pdf
make watch  # auto-recompile on save
make clean  # remove build artefacts
```
