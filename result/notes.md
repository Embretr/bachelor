# Working Notes — Claude Writing Log

> Claude maintains this file across writing sessions.
> Log every significant decision, open question, and continuity note here.
> Per-chapter scratch lives in `result/chapters/chN/notes.md`.
> This file is read at the start of sessions to restore context between conversations.

---

## How to Use This File

After every writing session, Claude adds an entry:

```markdown
## [DATE] — Session: [what was done]

**Written:** [section X.Y — brief description]
**Decisions made:**
- [decision and why]

**Open questions / needs follow-up:**
- [question]

**Continuity notes for next session:**
- [what the next writer session needs to know]
```

---

## Session Log

## 2026-04-14 — Session: readiness workflow strengthened

**Written:** No thesis prose. Workflow and outline/context readiness were updated before further section writing.

**Decisions made:**
- `/write-section` now hard-stops on missing concrete citation keys, unread/unconfirmed sources, missing evidence context, Ch 5 anchors to unwritten sections, Ch 6 before Chapters 1–5 are drafted, Ch 4.2 requirement-ID mismatch, and technical/scope contradictions.
- Benchmark results are now a required context source for Ch 4.5 and Ch 5.2.
- Ch 3.2 now requires research ethics context; Ch 5.6 must state missing user testing as a limitation if no tests are conducted.
- Ch 6 outline now has paragraph-level planning and SQ3 is mandatory.

**Open questions / needs follow-up:**
- Authors must add/read/confirm sources in `result/references.bib` and `context/docs/method/literature-list.md`.
- Embret must fill `context/docs/tech/benchmark-results.md`.
- Research ethics details, interview duration, sprint-log, decision-log, and change-log remain blockers.

**Continuity notes for next session:**
- Do not start affected sections until the new readiness gate passes. Missing local LaTeX tools still count as a compile warning, not a writing blocker.

---

## Open Questions Across Sessions

*(Track unresolved issues that span multiple sessions)*

| # | Question | Raised | Resolved |
|---|----------|--------|---------|
| 1 | What is the exact research question? | — | ⬜ |
| 2 | What is the formal classification of the scheduling problem the algorithm solves? | — | ⬜ |
| 3 | What technology is used for the frontend? | — | ⬜ |
| 4 | What technology is used for the backend? | — | ⬜ |
| 5 | What database is used? | — | ⬜ |
| 6 | Were any formal user tests conducted? | — | ⬜ |

---

## Continuity Decisions (Standing)

*Decisions made that all future writing must be consistent with:*

### SSB-tallet 137 308 — kvalifisert bruk påkrevd

`ssb2026sysselsetting` Tabell 2 oppgir 137 308 sysselsatte i «Transport og lagring» (4. kvartal 2025). Denne næringsklassen inkluderer godstransport, persontransport, sjøfart, lagerholdere m.m. — ikke bare norske transportselskaper av typen Ressursplanlegger er laget for.

**Regler for bruk:**
- Skriv alltid «sysselsatte i transport og lagring» — aldri «sjåfører», «trafikkoordinatorer» eller «potensielle Ressursplanlegger-brukere».
- Bruk tallet til å kontekstualisere sektorens omfang i norsk økonomi (Ch 1.1 ¶1), ikke til å anslå markedsstørrelse.
- Om du beregner andel: 137 308 / 2 872 855 ≈ 4,8 % av alle sysselsatte — men merk at dette er beregnet, ikke direkte oppgitt av kilden.
- Siteringslokator: tabell-referanse + «ingen sidetall» (web-statistikk, ingen trykte sidetall).

Kilde: `context/docs/method/sources/raw/extracted/ssb2026sysselsetting.md` (Forbehold og begrensninger)

---

## Placeholder Log

*Sections with [FILL IN] or [CITATION NEEDED] that need resolution:*

| Location | Placeholder | What is needed |
|----------|-------------|---------------|
| `context/context.md` | Research question | Mikael to finalise |
| `context/context.md` | Tech stack table | Embret to fill |
| `result/chapters/ch1/ch1-introduction.tex` | 1.1 Background | Not started |
| `result/chapters/ch1/ch1-introduction.tex` | Research question | Requires context.md RQ |
