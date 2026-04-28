# Source Notes — Workflow and Conventions

> **Purpose:** Per-source notes with verified passages from each cited source, used by writer agents to ensure citations match what sources actually say. Eliminates the "AI cites a source it has not read" risk.
>
> **Last updated:** 2026-04-26.

---

## File structure

```
context/docs/method/sources/
├── README.md              — this file (workflow)
├── _template.md           — empty mal for structured notes
├── raw/                   — Mikael's raw text dumps from sources
│   └── {bibkey}.md
└── {bibkey}.md            — Claude's structured extraction from raw
```

---

## Workflow per source

1. **Mikael:** Fetch source content (NTNU Oria, open PDF, official web page). Copy relevant passages — typically 1–3 chapters of a book, full text of an article — into `raw/{bibkey}.md`. Include page markers.
2. **Mikael:** Tell Claude: *"ekstrakt fra raw/{bibkey}.md"*.
3. **Claude:** Reads raw file, identifies passages relevant to the claims in `context/docs/method/CITATIONS.md`, writes structured notes to `{bibkey}.md`.
4. **Mikael:** Reviews extraction — verifies quotes are intact, claim-mappings are correct. Updates Status to "Verified by human".
5. Notes are now usable by the writer pipeline.

---

## Conventions for raw files

- **Page markers** are critical: include `[p. 23]` or `--- s. 23 ---` between sections so quotes can be attributed correctly.
- **Plain text only.** OCR scanned pages first; verify the OCR output before pasting.
- **Relevant chapters only**, not entire books. For Pinedo (600 pages) we need ch. 1, 3, and 4 — not the rest. Use CITATIONS.md as a guide for which claims this source must support.
- **Original language is fine:** Norwegian for TØI/SSB/Fafo, English for international papers.
- **Verbatim is best.** Paraphrasing in the raw file makes Claude's job harder and reduces verifiability.

---

## What Claude extracts (see `_template.md`)

For each source, the structured notes file contains:
- Brief summary (2–3 sentences) — what the source argues
- Claims-mapping — for each claim in CITATIONS.md this source supports, the exact passage with page reference
- Definitions the source provides for key terms
- Useful direct quotes sorted by relevance
- "What the source does NOT say" — guards against misattribution

---

## Pipeline integration

Writer agents and review agents will read `{bibkey}.md` for each cite key referenced in a section's `MUST CITE` markers (per outline.md). When the new gate is enabled in `.claude/skills/write-section/SKILL.md`, sections with unverified source notes will be blocked from writing.

---

## Coverage tracker

**Total sources:** 48
**Notes complete:** 0 (as of 2026-04-26)
**Notes verified by Mikael:** 0

### Priority for Ch 2 (start here)

| # | Bibkey | Required for | Status |
|:-:|---|---|:-:|
| 1 | `pinedo2016scheduling` | Ch 2.1 ¶1, ¶3, ¶7 | ⬜ |
| 2 | `rossi2006constraint` | Ch 2.1 ¶3, ¶4, Ch 4.5 ¶1 | ⬜ |
| 3 | `dantzig1959truck` | Ch 2.1 ¶8 | ⬜ |
| 4 | `braekers2016vrp` | Ch 2.1 ¶8 | ⬜ |
| 5 | `parasuraman2000automation` | Ch 2.2 ¶2, Ch 5.2 ¶3 | ⬜ |
| 6 | `lee2004trust` | Ch 2.2 ¶3, Ch 5.3 ¶1 | ⬜ |
| 7 | `griffis2007tms` | Ch 2.3 ¶1, ¶2, Ch 4.3 ¶1 | ⬜ |
| 8 | `heinbach2022datadriven` | Ch 2.3 ¶2, Ch 4.3 ¶1 | ⬜ |
| 9 | `hevner2004design` | Ch 2.4 ¶1, Ch 3.1 ¶1, Ch 5.6 ¶1 | ⬜ |
| 10 | `peffers2007dsrm` | Ch 2.4 ¶2, Ch 3.1 ¶1 | ⬜ |
| 11 | `wieringa2014dsm` | Ch 2.4 ¶4, Ch 5.6 ¶1 | ⬜ |

### Priority for Ch 4.5 / Ch 5 (continues)

| Bibkey | Required for |
|---|---|
| `googleortools2026cpsat`, `perron2023cpsatlp`, `timefold2026solver` | Ch 4.5 ¶2–3 |
| `glover1986future`, `burke2017late` | Ch 2.1 ¶6, Ch 4.5 ¶3 |
| `ernst2004staff` | Ch 2.1 ¶2 |
| Tema C (rest): `bainbridge1983ironies`, `hoff2015trust`, `amershi2019guidelines`, `miller2019explanation`, `nonaka1995knowledge` | Ch 2.2, 5.2, 5.4 |
| Tema E (norske rapporter): `ssb2026godstransport`, `ssb2026naeringer`, `ssb2026sysselsetting`, `flotve2025transportytelser`, `nav2025bedrift`, `jensen2014norsktransport`, `kristensen2021digital` | Ch 1.1, Ch 2.3 |
| Tema G (metode): `braun2006thematic`, `kvale2015interview`, `malterud2017kvalitative`, `oates2022researching` | Ch 3.2, 3.3, 3.5 |
| Tema H (agile): `larman2003iterative`, `beck2001manifesto` | Ch 3.4 |
| Tema D (TMS rest): `cichosz2020digital` | Ch 2.3, 5.3 |
| Tema I (bærekraft): `wced1987commonfuture`, `un2015agenda2030`, `becker2015karlskrona`, `duboc2020requirements`, `hilty2015ict4s`, `seyff2022mapping` | Ch 5.5 |
| Tema J (etikk): `mittelstadt2016algorithms`, `martin2019accountability`, `jobin2019landscape`, `eu2024aiact`, `lee2018understanding` | Ch 5.5 |
| Tema F (DSR rest): `hevner2007threecycle` | Ch 2.4 ¶3 (optional) |