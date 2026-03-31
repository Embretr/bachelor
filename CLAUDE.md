# Cephalo — Bachelor Thesis · Claude Instructions

## Project Overview

Cephalo is a resource planning platform for traffic coordinators (trafikkledere) in Norwegian
transport companies. The system displays assignments, drivers, and vehicles, and uses an
optimisation algorithm to automatically generate a daily/weekly plan. Traffic coordinators
can review, adjust, and approve the plan via the platform.

| Field | Value |
|---|---|
| **Thesis title** | [FILL IN] |
| **Institution** | NTNU Gløshaugen — Department of Computer Science (IDI) |
| **Program** | Data Engineering (Dataingeniør) |
| **Author 1** | Embret [LAST NAME] |
| **Author 2** | Mikael [LAST NAME] |
| **Supervisor** | [FILL IN] |
| **Deadline** | [FILL IN] |
| **Language** | English |
| **Citation style** | APA 7 (biblatex-apa) |

---

## Before Writing Anything — Always Read in This Order

1. `context/context.md` — thesis identity, research question, scope, chapter status
2. `context/thesis-spine.md` — the argument thread connecting all chapters
3. `context/disposisjon.md` — what each chapter and section should contain
4. `context/ordliste.md` — domain terminology; use these terms consistently
5. The target chapter file in `kapitler/`

---

## Writing Rules

- Write in **formal, academic English**
- Use **passive or impersonal constructions** — avoid "we believe" / "we think"; prefer "it can be argued" / "the results suggest"
- Use `\parencite{key}` for (Author, Year) citations
- Use `\textcite{key}` for Author (Year) in-text citations
- Add all new sources to `bibtex/referanser.bib`
- **Never invent citations, facts, or data** — ask the user to provide sources if needed
- Stay strictly within the scope defined in `context/scope.md`
- Use the exact terminology defined in `context/ordliste.md`
- Write one section at a time — do not jump ahead

---

## Repository Structure

```
bachelor/
├── CLAUDE.md                        ← you are here — read first
├── STATUS.md                        ← current writing progress — check before starting
├── Makefile                         ← run `make` to compile PDF
├── main.tex                         ← root LaTeX file
│
├── context/                         ← ALWAYS READ BEFORE WRITING
│   ├── context.md                   ← thesis identity, RQ, stack, chapter status
│   ├── thesis-spine.md              ← one-sentence argument per chapter — the backbone
│   ├── disposisjon.md               ← section-level outlines for all chapters
│   ├── ordliste.md                  ← domain glossary
│   ├── scope.md                     ← explicit in/out of scope
│   ├── interviews-summary.md        ← distilled findings from 7 interviews
│   └── fitgap-sammendrag.md         ← fit/gap analysis
│
├── prompts/                         ← reusable prompt templates per agent role
│   ├── writer.md                    ← how to use Claude as writer agent
│   ├── redtrad.md                   ← how to use Claude as red-thread checker
│   ├── kvalitet.md                  ← how to use Claude as quality/sensor checker
│   └── context-gather.md           ← which context files to load per chapter
│
├── vurdering/                       ← grading criteria — AI checks output against these
│   ├── sensurveiledning.md          ← sensor guidelines (fill in from PDF)
│   └── vurderingskriterier.md       ← distilled grading criteria in plain text
│
├── review/                          ← output from red-thread and quality agents
│   ├── redtrad-kap1.md              ← created after chapter 1 is drafted
│   └── kvalitet-kap1.md             ← created after chapter 1 is drafted
│
├── tech/                            ← Embret owns these files
│   ├── algoritme.md                 ← algorithm: input, output, constraints, method
│   ├── arkitektur.md                ← system architecture
│   ├── datamodell.md                ← database schema and entity relations
│   ├── api-oversikt.md              ← API endpoints
│   └── tech-stack.md                ← technology choices with justifications
│
├── krav/                            ← requirements
│   ├── funksjonelle-krav.md         ← functional requirements (MoSCoW + source)
│   ├── ikke-funksjonelle-krav.md    ← non-functional requirements
│   └── kravsporing.md               ← traceability: implemented + tested
│
├── metode/                          ← research method context
│   ├── forskningsdesign.md          ← chosen method and justification
│   ├── teoriramme.md                ← theoretical framework
│   └── litteraturliste.md           ← actual sources read (feeds referanser.bib)
│
├── prosjekt/                        ← project history
│   ├── beslutningslogg.md           ← key decisions: what, why, alternatives
│   ├── sprint-logg.md               ← weekly progress log
│   └── endringslogg.md              ← changes from early MVP to now
│
├── kapitler/                        ← LaTeX chapter files — the actual thesis
│   ├── kap1-innledning.tex
│   ├── kap2-teori.tex
│   ├── kap3-metode.tex
│   ├── kap4-funn.tex
│   ├── kap5-diskusjon.tex
│   └── kap6-konklusjon.tex
│
├── bibtex/
│   └── referanser.bib               ← all references (APA 7 / biblatex)
│
└── kilder/                          ← raw PDFs, interview notes (not tracked by git)
```

---

## Writing Workflow (per chapter)

1. Check `STATUS.md` — what is done, what needs writing
2. Read `context/context.md` + `thesis-spine.md` + `disposisjon.md`
3. Load chapter-specific context from `prompts/context-gather.md`
4. Use `prompts/writer.md` — write ONE section at a time
5. After chapter is complete: run `prompts/redtrad.md`, save output to `review/`
6. Run `prompts/kvalitet.md`, save output to `review/`
7. Revise chapter based on review output
8. Run `make` to verify LaTeX compilation
9. Update `STATUS.md`

## LaTeX Conventions

- `\parencite{key}` → (Author, Year)
- `\textcite{key}` → Author (Year)
- Figures: `figure` environment with `\caption{}` and `\label{fig:name}`
- Tables: `table` + `booktabs` (`\toprule`, `\midrule`, `\bottomrule`)
- Sections: `\section{}`, `\subsection{}`, `\subsubsection{}`
- Cross-references: `\Cref{label}` (capitalised) or `\cref{label}` (lowercase)
- No hardcoded page breaks — use `\clearpage` sparingly
