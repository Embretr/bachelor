# Godstransport med lastebil (`ssb2026godstransport`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Raw file contains the full downloaded content from the SSB statistics page (Tabell 1–3). This is a web page source — there is no additional document to read. All three tables have been extracted and data points verified against the raw MD file. Every thesis area of interest has been investigated.
  - **Gaps not investigated:** Tabell 4–8 (international transport by Norwegian trucks, transport by foreign trucks in Norway) — excluded from raw file as explicitly out of scope per the download note.

## Source metadata
- **BibTeX key:** `ssb2026godstransport`
- **Reference (APA 7):** Statistisk sentralbyrå. (2026). *Godstransport med lastebil*. https://www.ssb.no/transport-og-reiseliv/landtransport/statistikk/godstransport-med-lastebil
- **Tilgang:** Open (public SSB statistics page)
- **Raw source:** `../ssb2026godstransport.md` (MD fallback — downloaded as structured tables, no PDF available)
- **Coverage in raw:** Tabell 1 (quarterly snapshot Q4 2025, national vs. international), Tabell 2 (quarterly time series 2021–2025, all transport performance indicators), Tabell 3 (national transport by commodity type, quarterly 2021–2025). Tabell 4–8 excluded from raw as out of scope.

## Sammendrag (2–3 setninger)

SSB publiserer kvartalsvise statistikker over godstransport med norske lastebiler, med tall for transportarbeid (tonnkm), transportmengde (tonn), kjøretøykilometer, tomkjøringsprosent og gjennomsnittlig transportlengde. Dataene dekker nasjonal leie- og egentransport samt internasjonal transport. Kildens bidrag til avhandlingen er å etablere sektorens makroskala — nasjonal leietransport alene utgjorde ca. 252 millioner tonn og 22 milliarder tonnkm i 2025 — og å dokumentere operasjonelle indikatorer (tomkjøring ~28 %) som gir kontekst for planleggingsutfordringer i norsk veigodstransport.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 1.1 ¶1 (Transport sector's role in Norway, scale, complexity) | Covered — sector volume data establishes scale |
| Ch 1.1 ¶4 (Consequences of inefficiency) | Partial — tomkjøring rate is an indirect efficiency indicator; no causal link to planning practices in this source |
| Ch 5.5 ¶2–4 (Sustainability, SDGs, transport emissions) | Partial — volume data contextualises road freight's footprint; no emissions figures in this source |
| Ch 2.3 (TMS landscape — background context) | Outside scope — no TMS or software content |
| Ch 4.1 (Interview findings on current practices) | Outside scope — aggregate statistics, no company-level data |

## Claims this source supports

### Claim: "Nasjonal leietransport utgjorde om lag 252 millioner tonn og 22 milliarder tonnkm i 2025"

- **Suggested for:** Ch 1.1 ¶1 (best fit — establishes sector scale); Ch 5.5 ¶2 (sustainability context for road freight volume)
- **Direkte sitat:** "2025 | 2 051,0 | 252,4 | 22 008,1 | 27,9 | 87,2" (Tabell 2, rad: nasjonal leie- og egentransport, 2025)
- **Parafrase:** I 2025 transporterte norske lastebiler ca. 252 millioner tonn gods nasjonalt, med et samlet transportarbeid på 22 008 millioner tonnkm og et kjøretøykilometervolum på 2 051 millioner km.
- **Forbehold:** Tallene dekker både leietransport og egentransport (for eget regning). Kun leietransport (83,9 % av transportarbeidet) er direkte relevant for de fleste transportselskaper som bruker trafikkkoordinatorer.
- **Anvendelse på vårt case:** Disse volumtallene underbygger at norsk veigodstransport er en stor og operasjonelt krevende sektor, og gir grunnlag for å hevde at planleggingseffektivitet på selskapsnivå har aggregerte konsekvenser for logistikkkjeden.

---

### Claim: "Nasjonal leietransport dominerer med 83,9 % av samlet transportarbeid"

- **Suggested for:** Ch 1.1 ¶1 (sector structure background); Ch 1.1 ¶2 (context for traffic coordinator role)
- **Direkte sitat:** "Nasjonal leietransport | 4 851,5 | 83,9 | -4,6 | 14,9" (Tabell 1, Q4 2025)
- **Parafrase:** Nasjonal leietransport — der transportselskaper frakter gods for andre — utgjorde 83,9 % av samlet norsk lastebiltransportarbeid i Q4 2025.
- **Forbehold:** Tabell 1 er et øyeblikksbilde (Q4 2025), ikke et årsgjennomsnitt. Andelen varierer noe kvartal for kvartal, men er stabil over tid.
- **Anvendelse på vårt case:** At leietransport dominerer tilsier at de selskapene Ressursplanlegger er bygget for (transportselskaper som utfører oppdrag for andre) utgjør kjernen av sektoren — dette gir berettigelse for at ressursplanlegging er et sentralt problem i den norske godstransportsektoren.

---

### Claim: "Tomkjøringsprosenten for nasjonal leie- og egentransport lå på ca. 27–29 % i perioden 2021–2025"

- **Suggested for:** Ch 5.5 ¶2 (sustainability — inefficiency indicator); Ch 1.1 ¶4 (consequence of planning inefficiency — indirect)
- **Direkte sitat:** "2025 | 2 051,0 | 252,4 | 22 008,1 | 27,9 | 87,2" (Tabell 2, kolonne Tomkjøring (%))
- **Parafrase:** Mellom 2021 og 2025 kjørte norske lastebiler 27–29 % av kjøretøykilometerne uten last (tomkjøring).
- **Forbehold:** SSB-dataene etablerer tomkjøring som et eksisterende, stabilt fenomen i sektoren, men kilden gjør ingen årsaksanalyse. Kilden sier ikke at planleggingsproblemer forårsaker tomkjøring — sammenhengen må argumenteres av avhandlingen selv, med referanse til tomkjøringsdataene som kontekstuell bakgrunn.
- **Anvendelse på vårt case:** En vedvarende tomkjøringsprosent på ~28 % indikerer strukturell ressursutnyttelsessvakhet i sektoren; bedre koordinering av sjåfør- og kjøretøytildelinger — noe Ressursplanlegger adresserer — kan potensielt bidra til å redusere unødvendig tomkjøring på selskapsnivå.

---

### Claim: "Gjennomsnittlig transportlengde per tonn var ca. 87 km i 2025 for nasjonal transport"

- **Suggested for:** Ch 1.1 ¶1 (sector characteristics — short-haul dominated); Ch 5.5 ¶2 (sustainability context)
- **Direkte sitat:** "2025 | 2 051,0 | 252,4 | 22 008,1 | 27,9 | 87,2" (Tabell 2, kolonne Gj.snittlig transportlengde pr. tonn (km))
- **Parafrase:** I 2025 var gjennomsnittlig transportlengde per tonn for nasjonal norsk lastebiltransport 87,2 km — kortere enn internasjonal transport (337 km), noe som indikerer at nasjonal veigodstransport er kortdistansedominert.
- **Forbehold:** Gjennomsnittet skjuler stor spredning mellom vareslagene (f.eks. malm/stein vs. næringsmidler). Kilden gir ikke per-rute- eller per-selskapsdata.
- **Anvendelse på vårt case:** Kortdistansekarakter (87 km) betyr at daglig ressursallokering — ikke ruteoptimalisering — er den kritiske planleggingsoppgaven; sjåfører gjennomfører mange oppdrag per dag innenfor et begrenset geografisk område, noe som øker kompleksiteten av tildeling snarere enn ruting — nettopp det Ressursplanlegger løser.

---

### Claim: "Nasjonal transport utgjorde 94,2 % av samlet norsk lastebiltransportarbeid i Q4 2025"

- **Suggested for:** Ch 1.1 ¶1 (scope framing — thesis focuses on national transport context)
- **Direkte sitat:** "Nasjonal leie- og egentransport | 5 443,5 | 94,2 | -5,5 | 5,4" (Tabell 1, Q4 2025)
- **Parafrase:** I Q4 2025 sto nasjonal leie- og egentransport for 94,2 % av samlet transportarbeid utført av norske lastebiler.
- **Forbehold:** Q4-tall; årsandelen for 2025 er konsistent (nasjonal leie- og egentransport ca. 22 008 av totalt ca. 23 528 mill. tonnkm = ca. 94 %).
- **Anvendelse på vårt case:** Bekrefter at avhandlingens fokus på nasjonale transportselskaper treffer kjernen av norsk godstransport — ikke et nisjesegment.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Nasjonal leietransport | Transportselskaper som utfører oppdrag for andre | Direkte relevant — dette er selskapstypene med trafikkkoordinatorer |
| Nasjonal egentransport | Egentransport (utenfor scope) | Selskaper som frakter egne varer — sjelden trafikkkoordinatorer i vår forstand |
| Transportarbeid (mill. tonnkm) | Sektorskalering / volumindikator | Brukes for å begrunne sektorens størrelse |
| Tomkjøring (%) | Ressursutnyttelse / kjøretøyutnyttelse | Indirekte indikator på planleggingseffektivitet — kan kobles til koordineringsproblematikk |
| Transportmengde (mill. tonn) | Godsmengde | Volumstørrelse for sektor |
| Lastebil | Kjøretøy | Direkte ekvivalent |
| Sjåfør (implisitt) | Sjåfør | Ikke eksplisitt i kilden, men lastetransport forutsetter sjåfører |
| Gj.snittlig transportlengde pr. tonn (km) | Oppdragslengde | Indikerer kortdistansekarakter av nasjonal transport |

## Forbehold og begrensninger

- **Ingen data på planleggingspraksis:** Kilden sier ingenting om hvordan transportselskaper planlegger ressurser, bruker TMS-systemer, eller koordinerer sjåfører. Den kan ikke brukes til å støtte påstander om planleggingspraksis eller koordinatorrollen.
- **Aggregerte tall — ingen SME-nivådata:** Dataene dekker alle norske lastebiler samlet. De syv selskapene i intervjustudien (8–45 kjøretøy) er ikke representert separat. SSB-tallene gir makrokontekst, ikke selskapsspesifikke innsikter.
- **Ingen årsaksanalyse:** Tomkjøring kan ha mange årsaker (tomretur etter leveranse, strukturelle geografi-årsaker) og er ikke direkte koblet til planleggingsineffektivitet i kilden. Avhandlingen må argumentere koblingen eksplisitt.
- **Ingen emisjonsdata:** For diskusjonen i Ch 5.5 (bærekraft) finnes ingen CO₂- eller utslippsdata i dette kildematerialet. Utslippsargumentet må støttes av en annen kilde.
- **Nedlasting kun Tabell 1–3:** Tabell 4–8 (internasjonal transport og utenlandske lastebiler i Norge) er ikke i raw-filen — men er heller ikke relevant for avhandlingens nasjonale fokus.
- **Outline MUST CITE:** Kilden er ikke markert med MUST CITE i outline.md. Den er en supplerende kontekstkilde til Ch 1.1.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Transportarbeid | Målt i mill. tonnkm (kilden bruker begrepet uten eksplisitt definisjon — enheten definerer innholdet) | Tabell 2, header |
| Tomkjøring (%) | Andel av kjøretøykilometer kjørt uten last | Tabell 2, header |
| Nasjonal leietransport | Transport utført for andre mot betaling, innenfor Norge | Tabell 1 |
| Nasjonal egentransport | Transport av egne varer, innenfor Norge | Tabell 1 |

## Rammeverk og modeller

Kilden presenterer ingen rammeverk eller modeller. Det er en statistikkside med tabelldata.

## Key arguments / lines of reasoning

### Argument: Sektorskalens implikasjon for planleggingsrelevans

- **Premiss(er):** Nasjonal leietransport utgjorde ~252 mill. tonn og 22 mrd. tonnkm i 2025; ca. 28 % av kjøringen er tomkjøring.
- **Konklusjon:** (Avhandlingens slutning, ikke kildens eksplisitte argument) Sektoren er stor nok til at marginale effektivitetsforbedringer i planlegging har samfunnsøkonomisk og miljømessig relevans.
- **Sted:** Tabell 1 og 2
- **Hvilke claims dette støtter:** Ch 1.1 ¶1, Ch 5.5 ¶2

*Merk: Kilden fremlegger ikke dette argumentet selv — den er en statistikkpublikasjon uten fortolkningsavsnitt. Argumentet konstrueres av avhandlingen basert på kildens tall.*

## Examples / case studies kilden bruker

Kilden inneholder ingen eksempler eller case studies. Det er tabellbasert statistikk.

## Data og statistikk

| Tall/data | Enhet | År/scope | Tabell-referanse |
|---|---|---|---|
| 252,4 | Mill. tonn (nasjonal leie- og egentransport) | 2025 (årssum) | Tabell 2 |
| 22 008,1 | Mill. tonnkm (nasjonal leie- og egentransport) | 2025 (årssum) | Tabell 2 |
| 2 051,0 | Mill. kjøretøykilometer (nasjonal leie- og egentransport) | 2025 (årssum) | Tabell 2 |
| 27,9 | % tomkjøring (nasjonal leie- og egentransport) | 2025 (årssum) | Tabell 2 |
| 87,2 | km gjennomsnittlig transportlengde per tonn | 2025 (årssum) | Tabell 2 |
| 83,9 | % andel av samlet transportarbeid (nasjonal leietransport) | Q4 2025 | Tabell 1 |
| 94,2 | % andel av samlet transportarbeid (nasjonal leie- og egentransport) | Q4 2025 | Tabell 1 |
| 4 851,5 | Mill. tonnkm (nasjonal leietransport) | Q4 2025 | Tabell 1 |
| 5 443,5 | Mill. tonnkm (nasjonal leie- og egentransport) | Q4 2025 | Tabell 1 |
| -6,7 | % endring (samlet transport 4.kv.2024–4.kv.2025) | Q4 2024 → Q4 2025 | Tabell 1 |
| 261,9 | Mill. tonn (nasjonal leie- og egentransport) | 2023 (årssum) | Tabell 2 |
| 22 617,0 | Mill. tonnkm (nasjonal leie- og egentransport) | 2023 (årssum) | Tabell 2 |

**Vareslagsdata (Tabell 3, 2025-årstall, transportmengde mill. tonn):**

| Vareslag | Transportmengde (mill. tonn) | Transportarbeid (mill. tonnkm) | År |
|---|---|---|---|
| I alt | 252,4 | 22 010,2 | 2025 |
| Jordbruks-, skogbruks- og fiskeprodukter | 32,7 | 3 145,4 | 2025 |
| Nærings- og nytelsesmidler | 28,5 | 5 333,9 | 2025 |
| Kull, koks, olje og kjemiske produkter | 22,5 | 1 967,6 | 2025 |
| Malm, stein, grus, sand, leire, sement m.m. | 127,0 | 5 150,5 | 2025 |
| Andre bearbeidete varer og stykkgods | 41,7 | 6 412,8 | 2025 |

## Forfatter-perspektiv / metodologi

Statistisk sentralbyrå (SSB) er Norges offisielle statistikkprodusent. Lastebilundersøkelsen er basert på utvalgsundersøkelse blant norske transportselskaper. Fotnote i kilden angir at utvalgsplanen ble endret i 3. kv. 2015 og at beregningsopplegg ble lagt om i 1. kv. 2016 — dette begrenser full sammenlignbarhet med eldre data, men er ikke relevant for avhandlingens bruk av 2021–2025-data.

## Spot-check verification

Dette er en MD-fallback fra en nettside (SSB statistikkside) — ingen PDF eksisterer. `pdftotext` er ikke tilgjengelig. Verifisering er gjennomført ved direkte sammenligning av siterte datapunkter mot råfilen (`ssb2026godstransport.md`) med grep.

1. Data "252,4 mill. tonn, 22 008,1 mill. tonnkm, tomkjøring 27,9 %" (Tabell 2, 2025-årssum) — verified via `grep "252\|22 008\|27,9" raw/ssb2026godstransport.md` — **PASS** (linje 34 i råfilen bekrefter alle tre verdier på samme rad)
2. Data "Nasjonal leietransport | 4 851,5 | 83,9" (Tabell 1, Q4 2025) — verified via `grep "leietransport\|4 851\|83,9" raw/ssb2026godstransport.md` — **PASS** (linje 19 i råfilen)
3. Data "22 617,0 mill. tonnkm" (Tabell 2, 2023-årssum) — verified via `grep "22 617" raw/ssb2026godstransport.md` — **PASS** (linje 32 og 84 i råfilen)

**Result:** 3/3 data points verified, 0 corrections made.