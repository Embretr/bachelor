# Ressursplanlegger — Bachelor Thesis · Claude Instructions

## The Mandate

This thesis must receive an A. Every word Claude produces is evaluated against that standard before it is written. If a change does not move the thesis closer to an A, it is not made.

The full thesis draft already exists in `result/`. The work now is **revision driven by feedback**: applying what supervisor directives, per-paragraph feedback, and distilled review patterns have established as our voice — to every section, until the prose meets the standard everywhere.

---

## The Three-Folder System

The repo holds three things and three things only:

| Folder | Purpose |
|---|---|
| `result/` | The thesis itself — `.tex` files, `references.bib` |
| `sources/` | Source materials — primary literature notes (`raw/extracted/`), interview transcripts (`interviews/`) |
| `context/` | The feedback corpus — what we have decided the thesis should be |

`context/` is closed at five files (plus the live feedback layer at `feedback-app/state.json`):

- `context/thesis-spine.md` — argument backbone, one sentence per chapter
- `context/glossary.md` — locked terms, including anchor concept definitions
- `context/lessons-learned.md` — generalised rules distilled from feedback rounds; the operative voice
- `context/supervisor-log.md` — chronological NTNU supervisor directives, verbatim
- `context/rubric.md` — A-grade criteria the thesis is judged against

These together are the only context loaded at session start. **Anything not in this list is not context** — it is either in the result, in a source, or it does not belong in this repo.

---

## Before Every Session — Required Ritual

1. Read `STATUS.md` — current revision phase
2. Read `context/lessons-learned.md` — the operative voice
3. Read `context/supervisor-log.md` — recent supervisor directives
4. Read `context/thesis-spine.md` — argument backbone
5. Read `context/glossary.md` — locked terms (anchor concepts)
6. Read `context/rubric.md` — what an A looks like for the section under work
7. Load the relevant `result/chapters/chN/chN-*.tex` for the section being touched
8. Load relevant source notes from `sources/raw/extracted/<bibkey>.md` for any cite involved

Skip nothing. The thesis is co-authored across machines — every session reloads the full corpus so no participant operates from stale context.

---

## The Operating Model — Feedback-Driven Revision

The work is no longer "draft a section, review it, distil the review". The draft exists. The work is now:

1. **Read the feedback** — per-paragraph notes in `feedback-app/state.json` and supervisor directives in `context/supervisor-log.md`.
2. **Locate the rule** — find the `lessons-learned.md` entry the feedback maps to, or add a new one if the pattern is general (one rule, one short reason, one application note, sourced).
3. **Apply across the corpus** — revise the targeted section AND every other section the rule touches. `lessons-learned.md` indexes "When to apply" for every rule; partial application is the most common way drift returns.
4. **Verify against the rubric** — walk `context/rubric.md` for the affected sections.

The goal is convergence: the prose everywhere reflects what the feedback corpus says the prose should be.

### When new per-paragraph feedback arrives

Per-paragraph feedback comes in through the feedback-app web server. When the user says "process the pending feedback":

1. Read `feedback-app/state.json`.
2. For every entry where `feedback` is set and `suggestion` is null/missing:
   - Draft a LaTeX rewrite that applies the feedback while honouring every rule in `context/lessons-learned.md`.
   - Preserve LaTeX commands (`\textcite`, `\parencite`, `\Cref`, `\textit`, math). No new headings or labels. Make only the changes the feedback requests; do not refactor unrelated wording.
   - Write the rewrite into `suggestion`, set `status: "ready"`.
3. For every entry where `summary` is null/missing and `paragraph` exists:
   - Write a one-sentence summary (≤20 words, plain English) of what the paragraph informs the reader of, into `summary`.
4. Save `state.json` back (preserving JSON formatting, UTF-8). Report counts.

The user reviews each suggestion in the web app and clicks Apply or Reject. **Claude does not touch `.tex` files in this loop** — the web app's Apply button does.

To add summaries for paragraphs the user has not yet given feedback on, the user can ask "summarise the paragraphs in `<file>`". Parse the file with the same paragraph splitter the server uses (split on blank lines, skip heading-only / comment-only chunks), compute each paragraph's 16-char hash, and create entries in `state.json` with `summary` filled in. Do not invent feedback or suggestions on paragraphs the user has not commented on.

### When supervisor feedback arrives

1. Append the directive to `context/supervisor-log.md` — chronological, dated, verbatim.
2. If the directive is general: mirror it as a rule in `context/lessons-learned.md` with **Why:** and **When to apply:** lines and a source attribution back to the supervisor-log entry.
3. If the directive is section-specific: apply directly to the target section.
4. Cross-link both directions (the log entry references the lessons-learned rule, the rule cites the log entry's date).

**Never store supervisor directives only in user memory.** Memory is per-machine; the thesis is co-authored. The log is the single source of truth across collaborators and sessions.

---

## Rule 0 — Plain prose is the primary criterion (supervisor 2026-05-04)

Every section, every paragraph, every sentence must be **clear, simple, and direct**. This rule overrides every other stylistic preference. Before any other rule kicks in, the prose has to satisfy four checks:

1. **Open broad, narrow to one clear message.** The section starts with a framing the reader can already grasp, then narrows in stages to the one specific claim it exists to make. Name that one message in a single sentence before drafting; if you cannot, the section is not ready.
2. **Build understanding, not vocabulary.** Our prose is OURS, not the sources'. Where a source uses a heavy academic term ("combinatorial complexity", "stochastic dispatch", "epistemic asymmetry"), paraphrase plainly first; the technical term, if it appears at all, comes second in parentheses or a follow-on. The goal is a reader with limited technical background understanding on first pass.
3. **Open abstract concepts with everyday-life intuition.** When a paragraph introduces an abstract or technical concept, the FIRST sentence anchors the reader in an everyday situation (a head nurse on a paper rota, a passenger waiting for a delayed train, a parent juggling pickups). Only then move to the technical name.
4. **Sequence the argument linearly — no cross-winds.** The section's paragraphs read as one line of thought going in one direction. The reader must never feel the argument is being pulled sideways while they were going forwards.

A section that fails any of the four is not A-grade no matter how strong its source rigour or anchor coverage. Full statements live in `context/lessons-learned.md` (Top-of-stack mandate plus the four named rules).

---

## Anchor Concept Coherence

Three anchor concepts spine the thesis argument. They are **English proper nouns used consistently across the thesis** — never re-translated to Norwegian, never split, never paraphrased.

- **Efficiency** — improved resource utilization (overtime, idle time, load balance)
- **Trust/control** — coordinator's ability to inspect, modify, accept, or reject any algorithm-generated assignment
- **Adaptability** — capacity to function meaningfully across companies with different operational rules

Where the spine demands them:

- **Ch 1 §1.2** defines all three verbatim
- **Ch 5 §5.1** organises Primary Findings under them (5.1.1 Efficiency, 5.1.2 Trust/control, 5.1.3 Adaptability)
- **Ch 6 §6.2** connects each SQ-answer paragraph to the anchor it serves
- Other chapters reference at least one anchor where structurally relevant

**Drift from the locked names is a critical issue.** Synonyms — "effektivitet", "tillit/kontroll", "tilpasningsdyktighet", "fleksibilitet", "skalerbarhet", "control" alone, "human control", "operator oversight", "trust calibration" — must be flagged on read and refused on write. Locked terms verbatim: **Efficiency**, **Trust/control**, **Adaptability**.

The phrase "accountable to the traffic coordinator" in the research question is always operationalised by the four concrete actions defined under Trust/control: **inspect, modify, accept, or reject**. Vague control language ("human oversight", "operator supervision") is forbidden. Where the four are referenced, name them inline; do not write "the four actions defined under Trust/control".

**Theoretical anchor for HITL**: Bainbridge (1983) *Ironies of Automation* (`bainbridge1983ironies`), layered with Hoff & Bashir 2015 (trust calibration) and Miller 2019 (explanation as interface).

---

## Writing Rules

- Write in **formal, academic English**.
- Use **passive or impersonal constructions** — avoid "we believe" / "we think"; prefer "it can be argued" / "the results suggest" / "the interviews indicate".
- Use `\parencite{key}` for (Author, Year) citations; `\textcite{key}` for Author (Year) in-text.
- Add all new sources to `result/references.bib` — never invent a source.
- Use the exact terminology defined in `context/glossary.md`.
- **Never use em dashes** (`---`, `—`) anywhere in thesis output. Replace with commas, parentheses, colons, semicolons, or full stops. En dashes (`--` for ranges) remain allowed.

## LaTeX Conventions

- Figures: `figure` environment with `\caption{}` and `\label{fig:name}`.
- Tables: `table` + `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
- Sections: `\section{}`, `\subsection{}`, `\subsubsection{}`.
- Cross-references: `\Cref{label}` (capitalised) or `\cref{label}` (lowercase).
- No hardcoded page breaks — use `\clearpage` sparingly.

## Compiling

```
make        # compile once → main.pdf
make watch  # auto-recompile on save
make clean  # remove build artefacts
```

After every `.tex` edit, run `make` and report compile status before ending the turn.

---

## What Claude Must Never Do

- Invent references or data — use only sources in `result/references.bib` and `sources/raw/extracted/`.
- Use "we believe", "we think", "we found" — use impersonal academic constructions.
- Write outside the scope of the section under work — not the next section, not the chapter introduction.
- Change the research question — use it verbatim from the .tex.
- Make changes that do not improve the thesis grade.
- **Replace, split, or paraphrase anchor names** — locked terms are **Efficiency**, **Trust/control**, **Adaptability**. Never write the old Norwegian forms, never split the slash compound, never paraphrase ("efficiency gains", "operator oversight", "fleksibilitet", "skalerbarhet").
- Use em dashes (`---`, `—`) — banned everywhere in thesis output.
- **Reference Trimtex or Opptur** as Norwegian transport management systems — they are factual errors (frequent transcription confusions for Timpex and Opter respectively). Only **Timpex** and **Opter** are real Norwegian TMS named in the interview pool; other interviewed companies use internal/custom tools described generically. Neither Timpex nor Opter generates assignment plans automatically — both are order/invoicing tools.
- **Reference the writing pipeline in thesis prose** — phrasings like "the four actions defined under Trust/control" or "this section is structured around X" belong in lessons-learned, not in the thesis.
- **Add new files to `context/`** — context is closed at the five files listed above. New rules go into `lessons-learned.md`; new directives go into `supervisor-log.md`; new terms go into `glossary.md`. Splitting into more files re-creates the bloat that was removed.
- **Recreate deleted scaffolding** — outline files, fit/gap docs, requirement traceability matrices, sprint logs, decision logs, per-section review files. The draft has absorbed what these said; the feedback corpus carries forward what is operative.

---

## Repository Structure

```
bachelor/
├── CLAUDE.md                    ← you are here
├── STATUS.md                    ← current revision phase
├── Makefile                     ← run `make` to compile PDF
├── main.tex                     ← root LaTeX file
│
├── context/                     ← feedback corpus — five files, closed
│   ├── thesis-spine.md          ← argument backbone (one sentence per chapter)
│   ├── glossary.md              ← locked terms (incl. anchor concept defs)
│   ├── lessons-learned.md       ← generalised rules distilled from feedback
│   ├── supervisor-log.md        ← NTNU supervisor directives (chronological)
│   └── rubric.md                ← A-grade criteria
│
├── sources/                     ← source materials
│   ├── raw/                     ← primary materials and stub notes
│   │   └── extracted/           ← deep-read extracted notes per source
│   ├── interviews/              ← interview transcripts (8 files)
│   ├── README.md
│   └── _template.md             ← source-extraction template
│
├── result/                      ← the thesis
│   ├── chapters/
│   │   ├── ch1/ch1-introduction.tex
│   │   ├── ch2/ch2-theory.tex
│   │   ├── ch3/ch3-method.tex
│   │   ├── ch4/ch4-findings.tex
│   │   ├── ch5/ch5-discussion.tex
│   │   └── ch6/ch6-conclusion.tex
│   └── references.bib
│
└── feedback-app/                ← per-paragraph feedback web server (Python)
    ├── server.py
    ├── state.json               ← live feedback layer
    └── ...
```

Build artefacts (`main.aux`, `main.pdf`, `main.log`, etc.) and the project artefact's own code (`ressursplanlegger/` submodule) live alongside but are not part of the thesis-revision corpus.
