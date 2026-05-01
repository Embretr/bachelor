# Sysselsetting, registerbasert (`ssb2026sysselsetting`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The raw MD file contains the two complete statistics tables from SSB. All relevant figures for the thesis areas (transport og lagring employment count, national total) are fully visible and extracted. No further pages exist.
  - **Gaps not investigated:** None — the source is a single-page statistics summary converted to MD; all content is present.

## Source metadata
- **BibTeX key:** `ssb2026sysselsetting`
- **Reference (APA 7):** Statistisk sentralbyrå. (2026). *Sysselsetting, registerbasert*. https://www.ssb.no/arbeid-og-lonn/sysselsetting/statistikk/sysselsetting-registerbasert
- **Tilgang:** Open (SSB public statistics)
- **Raw source:** `../ssb2026sysselsetting.md`
- **Coverage in raw:** Tabell 1 (employment by county, Q4 2025) and Tabell 2 (employment by gender and industry, Q4 2025). No further tables or narrative text present. MD lacks page numbers — this is a web statistics page converted to MD.

## Sammendrag (2–3 setninger)

Statistisk sentralbyrå sin registerbaserte sysselsettingsstatistikk gir kvartalsvise tall for sysselsatte 15–74 år bosatt i Norge, fordelt på næring, kjønn og arbeidsstedsfylke. For 4. kvartal 2025 var det 137 308 sysselsatte i næringen transport og lagring, og totalt 2 872 855 sysselsatte i alle næringer. Kilden er en autoritativ offisiell statistikk som kan brukes til å kvantifisere transportnæringens størrelse og arbeidskraftbase i norsk kontekst.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 1.1 ¶1 (Transport sector's role in Norway, scale, complexity) | covered — national employment numbers for transport og lagring provide sector scale |
| Ch 1.1 ¶2 (Traffic coordinator role, workforce context) | partial — gives sector headcount but no breakdown by role within transport |
| Ch 5.5 ¶1–¶2 (Sustainability analysis — employment effects) | partial — national employment baseline relevant as context for workforce impact claims |
| Ch 2.3 ¶1–¶2 (TMS landscape, Norway context) | outside scope — source is labour statistics, not about software systems |
| Ch 3.2 ¶2 (interview participant selection — sector representativeness) | outside scope — source provides no data on coordinator counts or company distribution |

## Claims this source supports

### Claim: "Transport og lagring sysselsetter 137 308 personer i Norge (4. kvartal 2025)"
- **Suggested for:** Ch 1.1 ¶1 (transport sector's role in Norway — set the scene with sector scale)
- **Direkte sitat:** "Transport og lagring | 137 308 | 110 665 | 26 643 | 0,4 | 0,5 | 0,0" (Tabell 2, ingen sidetall — web-statistikk)
  - [Translation suggestion: "Transport and storage | 137,308 | 110,665 | 26,643 | 0.4% | 0.5% | 0.0%"]
- **Parafrase:** I fjerde kvartal 2025 var 137 308 personer sysselsatt i næringen transport og lagring i Norge. Av disse var 110 665 menn og 26 643 kvinner. Næringen vokste med 0,4 % fra 2024 til 2025.
- **Forbehold:** «Transport og lagring» er en bred næringsklasse som inkluderer langtransport, godsbil, busstransport, lagerholdere m.m. — ikke bare de norske transportselskaper som er thesis-kontekstens kjerne. Tallet kan ikke brukes som antall trafikkoordinatorer eller sjåfører alene.
- **Anvendelse på vårt case:** Sektortallet 137 308 gir kapittel 1 et konkret tallgrunnlag for å motivere problemets skala: dersom ineffektiv manuell planlegging preger norsk transportsektor, representerer et verktøy som Ressursplanlegger et potensiale som berører en arbeidsstyrke i denne størrelsesordenen.

---

### Claim: "Totalt antall sysselsatte i Norge (alle næringer) er 2 872 855 (4. kvartal 2025)"
- **Suggested for:** Ch 1.1 ¶1 (national context for transport sector's relative size); secondary use in Ch 5.5 if sustainability analysis references transport's share of Norwegian workforce
- **Direkte sitat:** "Alle næringer | 2 872 855 | 1 512 428 | 1 360 427 | 0,3 | 0,3 | 0,3" (Tabell 2, ingen sidetall)
  - [Translation suggestion: "All industries | 2,872,855 | 1,512,428 | 1,360,427 | 0.3% | 0.3% | 0.3%"]
- **Parafrase:** I 4. kvartal 2025 var det totalt 2 872 855 sysselsatte i Norge på tvers av alle næringer.
- **Forbehold:** Dette er grunnlaget for å beregne transport og lagrings andel (~4,8 % av alle sysselsatte). Teller er registerbasert og ikke direkte sammenlignbar med AKU-tall eller tall fra før 2015.
- **Anvendelse på vårt case:** Gir proporsjonsramme for transport og lagrings omfang (ca. 1 av 21 sysselsatte norske borgere); nyttig om Ch 1 vil kontekstualisere transportnæringens vekt i norsk økonomi uten å overdrive.

---

### Claim: "Transportnæringen har en sterk kjønnsskjevhet: 80,6 % menn"
- **Suggested for:** Ch 5.5 ¶5 (ethical considerations — health/working-condition effects, or diversity note); or Ch 1.1 ¶2 (describing the coordinator/driver workforce)
- **Direkte sitat:** "Transport og lagring | 137 308 | 110 665 | 26 643" (Tabell 2, ingen sidetall)
- **Parafrase:** I transport og lagring-næringen er 110 665 av 137 308 sysselsatte menn (ca. 80,6 %) og 26 643 kvinner (ca. 19,4 %).
- **Forbehold:** Kjønnsskjevheten kan nevnes men er ikke et primærfokus for denne avhandlingen; bør ikke gi uforholdsmessig plass. Gjelder hele næringen, ikke spesifikt trafikkoordinatorer.
- **Anvendelse på vårt case:** Om Ch 5.5 diskuterer arbeidsforhold og likestillingsaspekter ved digitalisering av transportplanlegging, gir dette en empirisk basis for å konstatere at næringen er mannsdominert uten å måtte referere til ukjent kilde.

---

### Claim: "Sysselsettingen i transport og lagring vokste med 0,4 % fra 2024 til 2025"
- **Suggested for:** Ch 1.1 ¶1 (growing sector, motivation for digitisation); or as contextual note
- **Direkte sitat:** "Transport og lagring | ... | 0,4 | 0,5 | 0,0" (Tabell 2, Endring 2024–2025-kolonner, ingen sidetall)
- **Parafrase:** Transport og lagring-næringen viste en samlet sysselsettingsvekst på 0,4 % fra 4. kvartal 2024 til 4. kvartal 2025, drevet av vekst blant menn (+0,5 %) mens antallet kvinner var uendret (0,0 %).
- **Forbehold:** Vekstraten er moderat og gjelder ett år; det er ikke tilstrekkelig til å hevde «sterk vekst» eller «press på kapasitet» uten ytterligere kilder.
- **Anvendelse på vårt case:** Underbygger at transportnæringen er en stabil og voksende del av norsk økonomi, noe som styrker relevansen av å utvikle planleggingsverktøy for sektoren.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Transport og lagring | Norsk transportsektor / norske transportselskaper | SSBs næringsklasse er bredere enn kun «transportselskaper»; inkluderer lager og logistikk. |
| Sysselsatte | Ansatte / arbeidstakere | SSB bruker «sysselsatte» som inkluderer både lønnstakere og selvstendig næringsdrivende. |
| 4. kvartal | Q4 / fjerde kvartal | Referanseperiode for statistikken. |
| Arbeidsstedsfylke | Geografisk fordeling | Tabell 1 gir regional fordeling — potensielt nyttig for å beskrive geografisk spredning av transportvirksomhet. |

## Forbehold og begrensninger

- **Bred næringsklasse:** «Transport og lagring» inkluderer gods- og persontransport, sjøfart, lagerholdere m.m. Avhandlingen handler om norske transportselskaper som driver sjåfør- og kjøretøytildeling — en undergruppe av denne næringsklassen. Tallet 137 308 kan ikke brukes som antall potensielle Ressursplanlegger-brukere.
- **Ingen rolledata:** Kilden gir ingen informasjon om antall trafikkoordinatorer, disponenter eller administrative ansatte i transportnæringen. Avhandlingen kan ikke bruke denne kilden til å anslå antall potensielle sluttbrukere.
- **Ingen systemdata:** Kilden sier ingenting om digitalisering, TMS-bruk, eller planleggingspraksis i næringen.
- **Sammenlignbarhet:** Fra og med 2015 bygger statistikken på a-ordningen og er ikke sammenlignbar med eldre årganger. Dette er irrelevant for thesis-bruk, men verdt å notere om historiske trender siteres.
- **Sidetall mangler:** Dette er en web-statistikkside konvertert til MD. Det finnes ingen trykte sidetall. Alle siteringer må bruke tabell-referanser og «ingen sidetall» som lokator.
- **MUST CITE-sjekk:** Ingen `MUST CITE`-markør i outline.md peker eksplisitt til `ssb2026sysselsetting`. Kilden passer naturlig inn i Ch 1.1 ¶1 som grunnlagsdata for å kontekstualisere sektorens omfang.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Populasjon | "sysselsatte 15–74 år, bosatte i Norge. Referanseperiode: 4. kvartal." | ingen sidetall (innledning) |

## Rammeverk og modeller

Kilden presenterer ingen rammeverk eller modeller — dette er en ren statistikkpublikasjon.

## Key arguments / lines of reasoning

Kilden presenterer ingen argumentasjon — dette er en deskriptiv statistikk-tabell uten analytiske resonnementer.

## Examples / case studies kilden bruker

Ingen eksempler eller case studies — ren statistikk.

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 137 308 | Sysselsatte i transport og lagring, begge kjønn | Q4 2025, bosatte 15–74 år i Norge | ingen sidetall (Tabell 2) |
| 110 665 | Sysselsatte i transport og lagring, menn | Q4 2025 | ingen sidetall (Tabell 2) |
| 26 643 | Sysselsatte i transport og lagring, kvinner | Q4 2025 | ingen sidetall (Tabell 2) |
| 0,4 % | Endring i sysselsetting transport og lagring 2024→2025 | Q4 2024 → Q4 2025 | ingen sidetall (Tabell 2) |
| 2 872 855 | Totalt antall sysselsatte, alle næringer | Q4 2025, bosatte 15–74 år i Norge | ingen sidetall (Tabell 2) |
| ~4,8 % | Transport og lagrings andel av alle sysselsatte | Q4 2025 (beregnet: 137 308 / 2 872 855) | ikke direkte oppgitt — beregnet |

## Forfatter-perspektiv / metodologi

Statistikken er registerbasert og hentes fra a-ordningen (Skatteetaten, NAV og SSB i samarbeid). Den er ikke basert på spørreskjema og er dermed ikke underlagt de vanlige feilmarginene for surveybaserte arbeidsmarkedsstatistikker. Tallene er offisielle nasjonale statistikker, og SSB er den autoritativt korrekte kilde for disse dataene.

## Spot-check verification

**Merk:** Kilden er en MD-fil (web-statistikkside), ikke en PDF. `pdftotext` er ikke tilgjengelig. Verifisering gjøres ved å lese MD-filen direkte og bekrefte at sitatene finnes i tabellene.

1. Quote "Transport og lagring | 137 308 | 110 665 | 26 643 | 0,4 | 0,5 | 0,0" — verified by re-reading Tabell 2, linje 8 i tabellen i raw/ssb2026sysselsetting.md — PASS
2. Quote "Alle næringer | 2 872 855 | 1 512 428 | 1 360 427 | 0,3 | 0,3 | 0,3" — verified by re-reading Tabell 2, linje 1 i tabellen — PASS
3. Quote "sysselsatte 15–74 år, bosatte i Norge. Referanseperiode: 4. kvartal." — verified by re-reading innledningsavsnitt i raw/ssb2026sysselsetting.md, linje 10 — PASS

**Result:** 3/3 quotes verified, 0 corrections made.

**Note on page numbers:** This source is a web page (MD fallback). No printed page numbers exist. All locators in this file use table name + "ingen sidetall". This is documented as a limitation in Source metadata.