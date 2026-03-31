# Ressursplanlegger — Bachelor Thesis · Claude Instructions

## The Mandate

This thesis must receive an A. Every word Claude produces is evaluated against that standard before it is written. If a change does not move the thesis closer to an A, it is not made.

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

```
[1] LOAD CONTEXT
    → context/index.md → identify relevant files
    → load: context.md + thesis-spine.md + outline.md + chapter-specific files

[2] CHECK EVALUATION
    → evaluation/a-grade-rubric.md: what does an A look like for this section?
    → evaluation/evaluation.md: chapter-specific checklist

[3] WRITE
    → One section at a time — never a whole chapter
    → Follow the outline in context/outline.md exactly
    → Use only terms from context/glossary.md
    → Cite only sources in result/references.bib

[4] SELF-EVALUATE
    → Does this section serve the chapter's thesis-spine.md sentence?
    → Does it meet the A criteria in evaluation/a-grade-rubric.md?
    → Is there any unfounded claim, vague sentence, or missed citation?
    → If any answer is no → revise before outputting

[5] OUTPUT
    → Paste into the correct `result/chapters/chN/chN-*.tex` file
    → Update result/notes.md: what was written, what decisions were made, what needs follow-up
```

### Revising an existing section

```
[1] Load the section to revise
[2] Load evaluation/a-grade-rubric.md — identify the specific criterion to improve
[3] Make only the changes that move towards A
[4] Do not introduce new scope, new claims, or new citations without checking context/scope.md
```

### Running a red-thread check

```
→ Open a NEW session — do not run in the same session as the writer
→ Follow .claude/agents/red-thread.md exactly
→ Save output to evaluation/review/redthread-chN.md
```

### Running a quality check

```
→ Open a NEW session after the red-thread check is done
→ Follow .claude/agents/quality.md exactly
→ Save output to evaluation/review/quality-chN.md
```

---

## After Every Task — Required Post-Task Ritual

Run this at the end of every writing or revision session, before closing.

### Step 1 — Quality ranking

Rate the section or change just made:

```
QUALITY RANKING
Section written:     [section X.Y — title]
Grade of this output: [A / B / C]
Reasoning:           [one sentence — why this grade]
Relative to thesis:  [better than / same as / weaker than other sections written]
Weakest element:     [the single sentence or claim most likely to be questioned by an examiner]
```

If the grade is B or lower — propose a revision before closing.

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
File to edit:     [CLAUDE.md / .claude/agents/X.md / context/index.md / evaluation/X.md]

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

## What Claude Must Never Do

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
├── CLAUDE.md                    ← you are here — read every session
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
├── .claude/                     ← Claude Code agent and skill definitions
│   ├── agents/
│   │   ├── writer.md            ← writer agent template
│   │   ├── red-thread.md        ← red-thread agent template
│   │   └── quality.md           ← quality/examiner agent template
│   └── skills/
│       ├── session-start.md     ← ritual: what to load at session start
│       └── context-gather.md    ← which files to load per chapter
│
└── result/                      ← the thesis
    ├── notes.md                 ← working notes Claude maintains
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
