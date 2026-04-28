# Source Notes — Folder Guide

> **Hva dette er:** Per-kilde notater med verifiserte sitater og sidetall, brukt av writer-agentene som ground truth.
>
> **Agent-instruksjon:** `.claude/agents/source-extractor.md` (alt om hvordan ekstraksjon foregår).
> **Mal:** `_template.md`.
> **Dine raw dumps:** `raw/{bibkey}.{pdf,md}`.
> **Agentens output:** `raw/extracted/{bibkey}.md`.

## Mappestruktur

```
context/docs/method/sources/
├── README.md              — denne filen
├── _template.md           — mal agenten følger
└── raw/
    ├── {bibkey}.pdf       — dine PDF-dumps
    └── extracted/
        └── {bibkey}.md    — agentens strukturerte notater
```

---

## Konvensjoner for raw-filer (ditt ansvar)

- **Filnavn = bibkey nøyaktig.** `pinedo2016scheduling.pdf`, ikke `pinedo.pdf` eller `getfile.pdf`.
- **PDF foretrekkes.** MD som fallback bare hvis PDF er skannet/ikke-leselig.
- **Verifiser tittelside før lagring.** Hvis edisjon ikke matcher bib-entry, agenten STOPPER.
- **PDF skal være tekst-PDF, ikke bilde-skann.** Test: `Cmd+F` søk etter et synlig ord. Treff = OK. Ingen treff = må OCR-es eller pastes inn som MD.

---

## Trigger-prompt (kopier i ny sesjon per kilde)

```
Use .claude/agents/source-extractor.md to extract from raw/{bibkey}.pdf

Bibkey: {bibkey}
```

Samme prompt for alle 48 kilder, uansett type eller størrelse. Ikke legg til hint om fokusområder — det prescriber svaret og motarbeider source-of-truth-prinsippet. Agenten oppdager relevant innhold fra outline + thesis-spine + TOC + indeks selv. CITATIONS.md er tom under ekstraksjonen for å unngå confirmation bias.

---

## Coverage tracker

**Total kilder:** 48
**Notes generert:** 0 av 48
**Verifisert av Mikael:** 0 av 48

### Prioritet 1 — Ch 2 blokkere (start her)

| # | Bibkey | Required for | Status |
|:-:|---|---|:-:|
| 1 | `pinedo2016scheduling` | Ch 2.1 ¶1, ¶3, ¶7 | ⬜ |
| 2 | `rossi2006constraint` | Ch 2.1 ¶3, ¶4, Ch 4.5 ¶1 | ⬜ |
| 3 | `parasuraman2000automation` | Ch 2.2 ¶2, Ch 5.2 ¶3 | ⬜ |
| 4 | `lee2004trust` | Ch 2.2 ¶3, Ch 5.3 ¶1 | ⬜ |
| 5 | `griffis2007tms` | Ch 2.3 ¶1, Ch 4.3 ¶1 | ⬜ |
| 6 | `heinbach2022datadriven` | Ch 2.3 ¶2, Ch 4.3 ¶1 | ⬜ |
| 7 | `hevner2004design` | Ch 2.4 ¶1, Ch 3.1 ¶1, Ch 5.6 ¶1 | ⬜ |
| 8 | `peffers2007dsrm` | Ch 2.4 ¶2, Ch 3.1 ¶1 | ⬜ |
| 9 | `wieringa2014dsm` | Ch 2.4 ¶4, Ch 5.6 ¶1 | ⬜ |

### Prioritet 2 — Ch 4.5 + utvidelse Ch 2

| Bibkey | Required for |
|---|---|
| `googleortools2026cpsat`, `perron2023cpsatlp`, `timefold2026solver` | Ch 4.5 ¶2–3 |
| `glover1986future`, `burke2017late` | Ch 2.1 ¶6, Ch 4.5 ¶3 |
| `ernst2004staff` | Ch 2.1 ¶2 |
| `bainbridge1983ironies`, `hoff2015trust`, `amershi2019guidelines`, `miller2019explanation`, `nonaka1995knowledge` | Ch 2.2, 5.2, 5.4 |

### Prioritet 3 — Ch 1 + Ch 5 + Ch 3

| Tema | Bibkeys | Required for |
|---|---|---|
| Norsk kontekst (E) | `ssb2026godstransport`, `ssb2026naeringer`, `ssb2026sysselsetting`, `flotve2025transportytelser`, `nav2025bedrift`, `jensen2014norsktransport`, `kristensen2021digital` | Ch 1.1, Ch 2.3 |
| Kvalitative metoder (G) | `braun2006thematic`, `kvale2015interview`, `malterud2017kvalitative`, `oates2022researching` | Ch 3.2, 3.3, 3.5 |
| Agile (H) | `larman2003iterative`, `beck2001manifesto` | Ch 3.4 |
| TMS rest (D) | `cichosz2020digital` | Ch 2.3, 5.3 |
| VRP-avgrensing (B) | `braekers2016vrp` | Ch 2.1 ¶4 (delimitering — én sitering) |
| Bærekraft (I) | `wced1987commonfuture`, `un2015agenda2030`, `becker2015karlskrona`, `duboc2020requirements`, `hilty2015ict4s`, `seyff2022mapping` | Ch 5.5 |
| Etikk (J) | `mittelstadt2016algorithms`, `martin2019accountability`, `jobin2019landscape`, `eu2024aiact`, `lee2018understanding` | Ch 5.5 |
| DSR rest (F) | `hevner2007threecycle` | Ch 2.4 ¶3 (optional) |

---

## Oppdateringsrutine

Etter hver ekstraksjon:
1. Agent skriver `raw/extracted/{bibkey}.md` (Status: Notes generated)
2. Du verifiserer ved å åpne PDF + sammenligne sitater (5 min)
3. Marker `Verified by human` i fila
4. Sett ☑ i tabellen over
5. Etter alle 48 ekstraksjoner: bygg CITATIONS.md ved å samle "Suggested for: Ch X.Y ¶Z" fra hver `extracted/{bibkey}.md`