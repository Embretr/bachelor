# Context Gather — Which Files to Load Per Chapter

> Use this before starting a writer session.
> Load files in the order listed — order matters for context coherence.
> Always load the "Always" files first, then the chapter-specific files.

---

## Always Load (every chapter, every session)

1. `context/context.md` — thesis identity and research question
2. `context/thesis-spine.md` — the backbone argument
3. `context/disposisjon.md` — chapter outlines
4. `context/ordliste.md` — domain glossary

---

## Chapter-Specific Files

### Chapter 1 — Introduction
| File | Why |
|------|-----|
| `context/scope.md` | Needed to write the scope section accurately |
| `context/interviews-summary.md` | Gives overview of what the thesis is based on |

### Chapter 2 — Theory
| File | Why |
|------|-----|
| `metode/teoriramme.md` | Contains the theoretical framework to expand on |
| `metode/litteraturliste.md` | Sources available for citation |
| `bibtex/referanser.bib` | BibTeX keys for `\parencite{}` |

### Chapter 3 — Methodology
| File | Why |
|------|-----|
| `metode/forskningsdesign.md` | Research method documentation |
| `prosjekt/sprint-logg.md` | Development process for section 3.4 |
| `context/interviews-summary.md` | Interview process details for section 3.2 |

### Chapter 4 — Findings
| File | Why |
|------|-----|
| `context/interviews-summary.md` | Source for sections 4.1–4.3 |
| `context/fitgap-sammendrag.md` | Source for section 4.3 |
| `krav/funksjonelle-krav.md` | Source for section 4.2 |
| `krav/ikke-funksjonelle-krav.md` | Source for section 4.2 |
| `tech/arkitektur.md` | Source for section 4.4 |
| `tech/algoritme.md` | Source for section 4.5 |
| `tech/tech-stack.md` | Supporting context for section 4.4 |

### Chapter 5 — Discussion
| File | Why |
|------|-----|
| `kapitler/kap1-innledning.tex` | For continuity and anchoring |
| `kapitler/kap2-teori.tex` | Theory to connect findings back to |
| `kapitler/kap3-metode.tex` | Method limitations for section 5.5 |
| `kapitler/kap4-funn.tex` | The findings to interpret |
| `vurdering/sensurveiledning.md` | Ensure discussion meets grading criteria |

### Chapter 6 — Conclusion
| File | Why |
|------|-----|
| All completed `kapitler/` files | Must summarise the whole thesis |
| `context/context.md` | Research questions must be answered verbatim |
| `vurdering/sensurveiledning.md` | Conclusion is a graded criterion |

---

## Also Load: Previous Chapter (for continuity)

When writing any chapter after Chapter 1, always paste the most recently
completed chapter. This ensures Claude does not repeat itself and maintains
a consistent voice and terminology.

---

## Practical Tip

For long context (Chapter 5+), the total pasted text may be very long.
If Claude seems to lose track of earlier instructions, start a new session
and paste only the most relevant 2–3 files rather than everything.
