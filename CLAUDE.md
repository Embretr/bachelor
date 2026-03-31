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

## Before Writing Anything — Always Read These First

1. `context/context.md` — thesis title, research question, scope, chapter status
2. `context/disposisjon.md` — what each chapter should contain
3. `context/ordliste.md` — domain terminology used consistently throughout the thesis
4. The target chapter file in `kapitler/`

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

---

## Repository Structure

```
bachelor/
├── CLAUDE.md                     ← you are here — read first
├── Makefile                      ← run `make` to compile PDF
├── main.tex                      ← root LaTeX file
│
├── context/
│   ├── context.md                ← START HERE — thesis identity, scope, status
│   ├── disposisjon.md            ← chapter outlines with content notes
│   ├── ordliste.md               ← domain glossary — use these terms consistently
│   ├── scope.md                  ← explicit in-scope / out-of-scope list
│   ├── intervju-funn.md          ← distilled interview findings (7 interviews)
│   └── fitgap-sammendrag.md      ← fit/gap analysis from user research
│
├── tech/
│   ├── algoritme.md              ← optimisation algorithm: input, output, constraints
│   ├── arkitektur.md             ← system architecture overview
│   ├── datamodell.md             ← database schema and entity relationships
│   ├── api-oversikt.md           ← API endpoints
│   └── tech-stack.md             ← technology choices with justifications
│
├── krav/
│   ├── funksjonelle-krav.md      ← functional requirements with MoSCoW priority
│   ├── ikke-funksjonelle-krav.md ← non-functional requirements
│   └── kravsporing.md            ← requirements traceability matrix
│
├── metode/
│   ├── forskningsdesign.md       ← research method and justification
│   ├── teoriramme.md             ← theoretical framework (VRP, scheduling, etc.)
│   └── litteraturliste.md        ← actual sources read (feeds bibtex/referanser.bib)
│
├── prosjekt/
│   ├── beslutningslogg.md        ← log of key technical/design decisions
│   ├── sprint-logg.md            ← weekly progress log
│   └── endringslogg.md           ← changes from early MVP to current version
│
├── kapitler/
│   ├── kap1-innledning.tex
│   ├── kap2-teori.tex
│   ├── kap3-metode.tex
│   ├── kap4-funn.tex
│   ├── kap5-diskusjon.tex
│   └── kap6-konklusjon.tex
│
├── bibtex/
│   └── referanser.bib
│
└── kilder/                       ← raw PDFs, interview notes (not tracked by git)
```

---

## Workflow for Writing a Chapter

1. Read `context/context.md` → `context/disposisjon.md` → `context/ordliste.md`
2. Read any relevant context files (e.g. `context/intervju-funn.md` for Chapters 3–4)
3. Read the existing content of the target chapter file in `kapitler/`
4. Write or continue the chapter in LaTeX
5. Run `make` to verify compilation

## LaTeX Conventions

- `\parencite{key}` → (Author, Year)
- `\textcite{key}` → Author (Year)
- Figures: `figure` environment with `\caption{}` and `\label{fig:name}`
- Tables: `table` + `booktabs` (`\toprule`, `\midrule`, `\bottomrule`)
- Sections: `\section{}`, `\subsection{}`, `\subsubsection{}`
- Cross-references: `\Cref{label}` (capitalised) or `\cref{label}` (lowercase)
- No hardcoded page breaks — use `\clearpage` sparingly
