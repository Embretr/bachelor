# {Title} (`{bibkey}`)

## Status
- [ ] Notes generated from raw (Claude, YYYY-MM-DD)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [ ] Coverage assessment: SUFFICIENT / INSUFFICIENT
  - **Reasoning:** [why this extraction is enough — or not — to write the cited sections]
  - **Gaps not investigated:** [chapters/sections not read and why]

## Source metadata
- **BibTeX key:** `{bibkey}`
- **Reference (APA 7):** [paste from references.bib]
- **Tilgang:** open / paywalled / NTNU Oria / PDF
- **Raw source:** `../{bibkey}.{pdf,md}`
- **Coverage in raw:** hvilke kapittel/seksjoner/sider raw-filen dekker

## Sammendrag (2–3 setninger)
Hva argumenterer kilden for? Hva er kjernekonseptet?

## Areas of interest investigated

Fra outline.md og thesis-spine.md, hvilke områder ble vurdert for denne kilden:

| Område | Bidrag |
|---|---|
| Ch X.Y (topic) | covered / outside scope / partial |

## Claims this source supports

Hvert claim er en påstand kilden eksplisitt gjør, som er relevant for thesis-områder. Sortert etter relevans (mest sentrale først).

### Claim: "[claim som kilden gjør]"
- **Suggested for:** Ch X.Y ¶Z (basert på outline-tema-match — én eller flere ¶, rangert)
- **Direkte sitat:** "..." (s. N)
- **Parafrase:** ...
- **Forbehold:** scope eller limitations som påvirker bruken
- **Anvendelse på vårt case:** Én konkret setning om hvordan dette claimet anvendes på Ressursplanlegger / norske trafikkoordinatorer.

### Claim: "..."
- ...

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| | | |

## Forbehold og begrensninger

Slått sammen: hva kilden *ikke* dekker, og hva i kildens kontekst som gjør den ikke direkte overførbar til vårt case. Brukes for å unngå misattribusjon og over-applikasjon.

- ...

## Definisjoner gitt av kilden

> Hold definisjonene **korte, direkte og riktige**. Hent den presise kjernesetningen verbatim. Maks 3–5 entries — bare termer som faktisk er sentrale i thesis-spine eller som direkte støtter en claim.

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| | | |

## Rammeverk og modeller

For strukturerte rammeverk kilden presenterer (10-nivå-skala, X dimensjoner, Y-fase prosess, etc.). Tom seksjon hvis kilden ikke har slike rammeverk.

### [Rammeverk-navn] (s. X)

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| | | | |

## Key arguments / lines of reasoning

Kildens egne resonnementer — ikke isolerte claims, men HVORDAN den argumenterer. Bruk når writer-agent skal bygge en paragraf rundt et claim.

### Argument: [kort tittel]
- **Premiss(er):** ...
- **Konklusjon:** ...
- **Sted:** (s. N)
- **Hvilke claims dette støtter:** Ch X.Y ¶Z

## Examples / case studies kilden bruker

Konkrete eksempler eller cases — nyttig hvis writer trenger å illustrere et konsept. Tom seksjon hvis kilden ikke har relevante eksempler.

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| | | |

## Data og statistikk

(Bare for rapporter / empiriske kilder. Tom seksjon hvis kilden ikke har statistikk.)

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| | | | |

## Forfatter-perspektiv / metodologi

Kort om kildens metodikk eller posisjon (hvis relevant for hvordan vi bruker den). 1–2 setninger.

## Spot-check verification

Obligatorisk per Step 10.5 i source-extractor.md. Minimum 3 sitater verifisert mot PDF via `pdftotext`. Hvis seksjonen mangler er ekstraksjonen ikke fullført.

1. Quote "..." (s. N) — verified via `pdftotext -f N -l N raw/{bibkey}.pdf` — PASS / FAIL [+ correction made if FAIL]
2. ...
3. ...

**Result:** M/M quotes verified, K corrections made.