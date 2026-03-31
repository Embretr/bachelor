# Bachelor Thesis — Claude Code Instructions

## Project Overview
This is a collaborative bachelor thesis project. Two authors share this repository via GitHub and use Claude Code to assist with writing.

**Language:** English
**Citation style:** APA 7 (biblatex-apa)
**Institution:** NTNU Gløshaugen — Department of Computer Science (IDI)
**Program:** Data Engineering (Dataingeniør)

## How to Help

Before writing or editing any chapter, always read:
1. `context/context.md` — thesis title, problem statement, scope, and current status
2. `context/disposisjon.md` — chapter outline and what each chapter should contain
3. The relevant chapter file in `kapitler/`

When writing academic content:
- Write in formal, academic English
- Follow APA 7 citation format: use `\parencite{key}` for parenthetical and `\textcite{key}` for in-text citations
- Add new sources to `bibtex/referanser.bib`
- Stay within the scope defined in `context/context.md`
- Do not invent facts, citations, or data — ask the user to provide sources

## Repository Structure

```
bachelor/
├── CLAUDE.md                  ← you are here
├── Makefile                   ← run `make` to compile PDF
├── main.tex                   ← root LaTeX file, includes all chapters
├── context/
│   ├── context.md             ← START HERE before any writing task
│   ├── disposisjon.md         ← chapter outlines
│   ├── intervju-funn.md       ← interview findings (if applicable)
│   └── fitgap-sammendrag.md   ← fit/gap analysis (if applicable)
├── kapitler/
│   ├── kap1-innledning.tex    ← Introduction
│   ├── kap2-teori.tex         ← Theory / Literature Review
│   ├── kap3-metode.tex        ← Methodology
│   ├── kap4-funn.tex          ← Findings / Results
│   ├── kap5-diskusjon.tex     ← Discussion
│   └── kap6-konklusjon.tex    ← Conclusion
├── bibtex/
│   └── referanser.bib         ← all references
└── kilder/                    ← raw source files (PDFs, interview notes)
```

## Workflow for Writing a Chapter

1. Read `context/context.md` and `context/disposisjon.md`
2. Read the existing content of the target chapter file
3. Write or continue the chapter in LaTeX
4. Run `make` to verify compilation

## LaTeX Conventions

- Use `\parencite{key}` for (Author, Year) citations
- Use `\textcite{key}` for Author (Year) citations
- Figures: use the `figure` environment with `\caption` and `\label`
- Tables: use the `table` + `booktabs` environment
- Sections: `\section`, `\subsection`, `\subsubsection`
- Never hardcode page breaks — use `\clearpage` sparingly
