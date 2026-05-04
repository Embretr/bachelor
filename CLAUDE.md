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

Use the automated pipeline:

```
/write-section 2.1
```

This single command:
1. Validates prerequisites (outline plan, context files, glossary, references)
2. Spawns the `writer` subagent that reads its own context
3. Saves output to the correct .tex file
4. Runs deterministic checks (placeholders, forbidden phrases, citation keys, compilation)
5. Spawns 2 review subagents in parallel — `section-coherence` and `section-quality` (the latter includes the AI-voice / naturalness check) — each with its own JSON gate
6. Reports pass/fail status and updates STATUS.md

If the section already has content, you choose: **revise** (recommended) or **overwrite**.

See `.claude/skills/write-section/SKILL.md` for the full pipeline specification.

### Reviewing a completed chapter

After all sections in a chapter are `drafted-reviewed`:

```
/review-chapter 2
```

This runs 2 integration subagents (`chapter-redthread` + `chapter-sensor`) that assess the chapter as a whole.
If it passes → `candidate-approved`. **You** make the final approval decision.

See `.claude/skills/review-chapter/SKILL.md` for details.

### Writing order

```
2.1 → 2.2 → 2.3 → 2.4 → 3.1 → 3.2 → 3.3 → 3.4 → 3.5
→ 4.1 → 4.3 → 4.2 → 4.4 → 4.5 → 5.1 → 5.2 → 5.3
→ 5.4 → 5.5 → 5.6 → 1.1 → 1.2 → 1.3 → 1.4 → 6.1 → 6.2 → 6.3
→ Abstract + Sammendrag (last)
```

Ch 1 is written after Ch 2–5 (so the intro matches what was actually written).
Ch 6 is written last.

---

## Critical Workflow Rules

These rules are non-negotiable. They override convenience and save more time than they cost.

### 0. Plain prose is the primary criterion (supervisor 2026-05-04)

Every section, every paragraph, every sentence must be **clear, simple, and direct**. This rule overrides every other stylistic preference. Before any other workflow rule kicks in, the prose has to satisfy four checks:

1. **Open broad, narrow to one clear message.** The section starts with a framing the reader can already grasp, then narrows in stages to the one specific claim it exists to make. Name that one message in a single sentence before drafting; if you cannot, the section is not ready.
2. **Build understanding, not vocabulary.** Our prose is OURS, not the sources'. Where a source uses a heavy academic term ("combinatorial complexity", "stochastic dispatch", "epistemic asymmetry"), paraphrase plainly first; the technical term, if it appears at all, comes second in parentheses or a follow-on. The goal is a reader with limited technical background understanding on first pass — not adding words, not sounding smart.
3. **Open abstract concepts with everyday-life intuition.** When a paragraph introduces an abstract or technical concept, the FIRST sentence anchors the reader in an everyday situation (a head nurse on a paper rota, a passenger waiting for a delayed train, a parent juggling pickups). Only then move to the technical name. Einstein did not open relativity with "combinatorial complexity"; he opened with a person on a platform watching a train.
4. **Sequence the argument linearly — no cross-winds.** The section's paragraphs read as one line of thought going in one direction. The reader must never feel the argument is being pulled sideways while they were going forwards. If two adjacent paragraphs would have to be read together to make sense, one of them is in the wrong place.

A section that fails any of the four is not A-grade no matter how strong its source rigour or anchor coverage. The full statements live as rules in `evaluation/review/lessons-learned.md` ("Top-of-stack mandate" block + the four named rules under Structure / Reader accessibility / Flow). Existing drafts (Ch 2.1–2.4, Ch 3.1–3.7) are flagged in `STATUS.md` for a plain-prose pass before final submission; new sections satisfy the rules at draft time.

### 1. Section plan before writing — always

The section plan (`context/outline.md`) is more important than the prompt itself. If you know exactly what each paragraph should say, the output will always be usable. Without it, the result will be generic filler that takes longer to fix than to write from scratch. **Never start writing a section unless `context/outline.md` contains a concrete, paragraph-level plan for that section.** If the plan is missing or vague, stop and ask the user to fill it in before proceeding.

### 2. Writer and reviewers must never share a context

The writer subagent is set up to produce — it is not objective. Reviewers need a clean slate without the writer's framing to see flaws. The `/write-section` and `/review-chapter` skills enforce this automatically by spawning each agent as an independent subagent (fresh context window per spawn). Do not bypass that by pasting the writer's output back into a reviewer prompt or by running reviewer checks in the same conversation as the writer.

### 3. Update thesis-spine.md after every chapter

If a finished chapter shifts the argument even slightly, update `context/thesis-spine.md` immediately. The spine is the single source of truth for cross-chapter coherence. If it drifts out of sync with what was actually written, every subsequent chapter risks building on a stale foundation. **After completing any chapter draft, compare what was written against the spine and update if needed — before moving on.**

### 4. Supervisor feedback flows from log to lessons-learned

All NTNU supervisor directives are logged in `context/docs/project/supervisor-feedback.md` (chronological, dated, verbatim). When a directive is generalisable beyond the immediate section, mirror it as a rule in `evaluation/review/lessons-learned.md` so the `writer`, `section-coherence`, and `section-quality` subagents all enforce it automatically (each reads `lessons-learned.md` per their system prompt). When a directive is section-specific, mirror it as a `> **Supervisor calibration**` note under the relevant block in `context/outline.md` so the writer sees it at draft time. Cross-link both directions. **Never store supervisor directives only in user memory** — memory is per-machine, but the thesis is co-authored. The log is the single source of truth across collaborators and sessions.

### 5. Anchor Concept Coherence

The three anchor concepts defined in `context/thesis-spine.md` and `context/glossary.md` are the spine of the thesis argument:

- **Efficiency** — improved resource utilization (overtime, idle time, load balance)
- **Trust/control** — coordinator's ability to inspect, modify, accept, or reject any algorithm-generated assignment
- **Adaptability** — capacity to function meaningfully across companies with different operational rules

These are **English proper nouns used consistently across the thesis** — never re-translated to Norwegian, never split, never replaced with synonyms. Where the spine demands them:

- **Ch 1 §1.2** MUST define all three verbatim
- **Ch 5 §5.1** MUST organise its Primary Findings under them (one sub-section per anchor: 5.1.1 Efficiency, 5.1.2 Trust/control, 5.1.3 Adaptability)
- **Ch 6 §6.2** MUST connect each SQ-answer paragraph to the anchor it serves
- **Other chapters** MUST reference at least one anchor where structurally relevant

**Drift from the locked names is a critical issue.** Synonyms — "effektivitet", "tillit/kontroll", "tilpasningsdyktighet", "fleksibilitet", "skalerbarhet", "control" alone, "human control", "operator oversight", "trust calibration", or any other paraphrase — must be flagged by reviewers and refused by writers. The locked terms are exactly: **Efficiency**, **Trust/control**, **Adaptability**. The `/write-section` readiness gate (Step 1c in `.claude/skills/write-section/SKILL.md`) hard-fails on synonym drift in MUST ANCHOR markers.

**The phrase "accountable to the traffic coordinator"** in the research question must always be operationalised in prose by the four concrete actions defined under **Trust/control**: inspect, modify, accept, or reject. Vague control language ("human oversight", "operator supervision") is forbidden.

**Theoretical anchor for HITL**: Bainbridge (1983) *Ironies of Automation* (`bainbridge1983ironies`). Where Human-in-the-Loop is theorised or discussed, layer Bainbridge (operator-vs-owner asymmetry) with Hoff & Bashir 2015 (trust calibration) and Miller 2019 (explanation as interface).

---

## After Every Task — Required Post-Task Ritual

### When using `/write-section` (automated pipeline)

The pipeline handles quality ranking, deterministic checks, and review automatically.
After the pipeline reports, the only manual steps are:

1. **Read the pipeline report** — check the status and any flagged issues
2. **If `drafted-needs-revision`** — fix issues and re-run `/write-section X.Y` (revise mode)
3. **If `drafted-reviewed`** — answer the LESSONS-LEARNED HARVEST candidates, then move to the next section
4. **Lessons-learned capture** is now a hard pipeline step (Step 6.6 in `.claude/skills/write-section/SKILL.md`) — the orchestrator surfaces every generalisable reviewer minor-issue / suggestion as a `Apply? (y / n / edit)` candidate before declaring the section complete. Your role is to answer per candidate; the orchestrator never auto-applies. Section-specific findings stay in the round file automatically.

### After completing a chapter (all sections `drafted-reviewed`)

1. Run `/review-chapter N` for integration check
2. **Spine sync check:** Compare the chapter's actual argument against `context/thesis-spine.md`. If the chapter shifted the argument, update the spine **now** — before moving to the next chapter.
3. **Human approval:** Review the chapter yourself. Mark as `approved` in STATUS.md only when you are satisfied.

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
- Run the writer and reviewers in the same context — they are spawned as independent subagents on purpose
- Make changes that do not improve the thesis grade
- **Replace, split, or paraphrase anchor names** — the locked English proper nouns are **Efficiency**, **Trust/control**, **Adaptability**. Never write the old Norwegian forms ("Effektivitet", "Tillit/kontroll", "Tilpasningsdyktighet"), never split the slash compound ("control" alone), and never paraphrase ("efficiency gains", "operator oversight", "fleksibilitet", "skalerbarhet")
- **Reference Trimtex or Opptur** as Norwegian transport management systems — they are factual errors (frequent transcription confusions for Timpex and Opter respectively). Only **Timpex** and **Opter** are real Norwegian TMS named in the interview pool; other interviewed companies use internal/custom tools described generically. Neither Timpex nor Opter generates assignment plans automatically — both are order/invoicing tools

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
│   └── review/                  ← output from review agents
│       ├── sections/            ← per-section reviews (ch2-2.1-round1-*.md)
│       ├── redthread-chN.md     ← chapter-level red thread
│       └── quality-chN.md       ← chapter-level sensor
│
├── .claude/                     ← Claude Code agent and skill definitions
│   ├── commands/
│   │   ├── write-section.md     ← /write-section 2.1 — entry point
│   │   └── review-chapter.md    ← /review-chapter 2 — entry point
│   ├── agents/                  ← registered subagents (YAML frontmatter)
│   │   ├── writer.md            ← drafts one section at a time
│   │   ├── section-coherence.md ← section-level coherence reviewer
│   │   ├── section-quality.md   ← section-level A-grade + naturalness reviewer
│   │   ├── chapter-redthread.md ← chapter-level integration reviewer
│   │   ├── chapter-sensor.md    ← chapter-level external examiner
│   │   └── source-extractor.md  ← extracts notes from one source PDF
│   ├── skills/
│   │   ├── write-section/SKILL.md  ← full write+check+review pipeline
│   │   ├── review-chapter/SKILL.md ← chapter integration check
│   │   ├── session-start.md     ← ritual: what to load at session start
│   │   └── context-gather.md    ← which files to load per chapter/section
│   └── WRITING-WORKFLOW.md      ← complete workflow documentation
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
