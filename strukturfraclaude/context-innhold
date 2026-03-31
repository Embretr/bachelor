# Kontekst-oversikt for Cephalo – Bachelor GitHub Repository

> Denne filen beskriver all kontekst som skal ligge i repoet for at AI skal kunne hjelpe med rapportskriving og utvikling.
> Filer merket ✅ er på plass. Filer merket ⬜ mangler eller må lages.

---

## 🏗️ Prosjektgrunnlag

### ⬜ `context/master_context.md`
Det viktigste enkeltdokumentet i repoet. Skal besvare:
- Hva er Cephalo? (1–2 setninger, presis)
- Hvilket problem løser det? (for hvem, i hvilken kontekst)
- Hvem er målgruppen? (trafikkleder, transportleder, admin)
- Teknisk stack (frontend, backend, database, hosting)
- Overordnet arkitektur (hvordan henger delene sammen)
- Hva er det unike med løsningen vs. eksisterende systemer (Timpex, Trimtex, manuell drift)
- Prosjektstatus – hvor langt er dere kommet

### ⬜ `context/ordliste.md`
Bransje- og prosjektspesifikke begreper. For hvert begrep: hva betyr det i *vår* kontekst.
Eksempler:
- **Oppdrag** – en transportjobb med fra/til, tidspunkt, krav til kjøretøy og sjåfør
- **Rute** – en eller flere oppdrag satt sammen til en sjåførs arbeidsdag
- **Trafikkleder** – operatøren som tildeler oppdrag til sjåfører
- **Tildeling** – prosessen med å koble et oppdrag til en sjåfør og et kjøretøy
- **Optimalisering** – algoritmens prosess med å lage en plan som maksimerer fakturerte timer
- **Kjøre-/hviletid** – lovpålagte grenser for hvor mye en sjåfør kan kjøre
- **Tacit knowledge** – kunnskap operatøren har i hodet som ikke er formalisert i systemet

### ⬜ `context/scope.md`
Tydelig avgrensning av hva som er og ikke er i scope.

**I scope:**
- Planlegging og tildeling av oppdrag til sjåfører og kjøretøy
- Visning av optimalisert plan for trafikkleder
- Manuell overstyring av algoritmens forslag
- [legg til mer]

**Ikke i scope:**
- Fakturering (integrasjon kan nevnes, men ikke implementert)
- Sjåførapp / mobilklient
- GPS-sporing i sanntid
- [legg til mer]

### ⬜ `context/rapportoutline.md`
Deres versjon av innholdsfortegnelsen – ikke bare malen, men med stikkord på hva som faktisk skal inn i hvert kapittel basert på deres prosjekt. Eksempelstruktur:

```
1. Innledning
   - Bakgrunn: transportbransjen, manuell planlegging, ineffektivitet
   - Problemstilling: [skriv inn]
   - Mål: [skriv inn]
   - Avgrensninger

2. Teori
   - Vehicle Routing Problem (VRP)
   - Resource scheduling
   - Human-in-the-loop automation
   - Relevant TMS-litteratur

3. Metode
   - Forskningsdesign
   - Datainnsamling (intervjuer)
   - Utviklingsmetodikk

4. Kravanalyse
   - Brukerinnsikt fra intervjuer
   - Funksjonelle krav
   - Ikke-funksjonelle krav
   - Fit-gap analyse

5. System og arkitektur
   - Overordnet arkitektur
   - Datamodell
   - API-design
   - Optimaliseringsalgoritme

6. Implementasjon
   - Frontend
   - Backend
   - Algoritme
   - Tekniske valg og begrunnelser

7. Testing og evaluering
   - Testmetode
   - Resultater
   - Kravsporing

8. Diskusjon
   - Oppnådde mål
   - Begrensninger
   - Videre arbeid

9. Konklusjon

10. Referanser / Vedlegg
```

### ⬜ `context/skrivestil_eksempel.md`
2–4 avsnitt fra rapporten som dere er fornøyd med. AI-en bruker dette til å matche tone, formelt nivå og setningsstruktur. Legg ved ett eksempel per type avsnitt: introduksjonsavsnitt, teknisk forklaring, og et diskusjonsavsnitt.

---

## 📋 Maler og retningslinjer

### ✅ `maler/01_generelle_retningslinjer_AIT.pdf`
Generelle retningslinjer for alle studier ved fagenheten AIT.

### ✅ `maler/02_studiespesifikke_retningslinjer.pdf`
Retningslinjer spesifikke for dette studieprogrammet.

### ✅ `maler/03_mal_hovedrapport.docx`
Mal for selve rapporten i Word-format.

### ✅ `maler/04_teknisk_mal.pdf`
Font, linjeavstand, marger, sidetall, osv. AI-en bør alltid følge dette ved generering av rapporttekst.
- Legg gjerne inn nøkkelpunktene direkte i `master_context.md` så AI-en ikke trenger å lese PDF-en

### ✅ `maler/05_visjonsdokument.pdf`
### ✅ `maler/06_kravdokumentasjon.pdf`
### ✅ `maler/07_systemdokumentasjon.pdf`
### ✅ `maler/08_oblig1_forprosjektplan.pdf`
### ✅ `maler/09_oblig2_poster.pdf`
### ✅ `maler/10_oblig4_prosjekthandbok.pdf`
### ✅ `maler/13_detaljert_beskrivelse_arbeidskrav.pdf`
### ✅ `maler/14_sensurveiledning.pdf`
> **Tips:** Lag en oppsummert `maler/sensurveiledning_punkter.md` med de viktigste vurderingskriteriene i klartekst – da kan AI-en aktivt sjekke om tekst dekker dem.

### ✅ `maler/15_KI_sjekkliste.pdf`

---

## 💻 Teknisk dokumentasjon

### ✅ `tech/kodebase_oppsummering.md`
Oppsummering av eksisterende kode. Sørg for at den inneholder:
- Mappestruktur med kort forklaring av hver mappe
- De viktigste filene og hva de gjør
- Hvilke eksterne biblioteker/pakker som brukes og hvorfor

### ⬜ `tech/datamodell.md`
Beskrivelse av databaseskjemaet. For hver entitet:
- Feltnavn og datatype
- Hva feltet representerer
- Relasjoner til andre entiteter

Eksempel:
```
## Oppdrag
- id: UUID
- tittel: string
- fra_adresse: string
- til_adresse: string
- planlagt_start: datetime
- planlagt_slutt: datetime
- status: enum (ufordelt, tildelt, pågående, fullført)
- krav_kjøretøytype: string
- krav_kompetanse: string[]
- tildelt_sjåfør_id: UUID (FK → Sjåfør)
- tildelt_kjøretøy_id: UUID (FK → Kjøretøy)

## Sjåfør
- id: UUID
- navn: string
- førerkortklasser: string[]
- kompetanse: string[]
- hviletid_status: ...
- [osv.]
```

### ⬜ `tech/api_oversikt.md`
Liste over alle API-endepunkter. For hvert endepunkt:
- Metode og URL
- Hva det gjør
- Request-body (hvis relevant)
- Response-format

Eksempel:
```
GET /api/oppdrag
→ Returnerer alle oppdrag for valgt dag/uke

POST /api/oppdrag/:id/tildel
Body: { sjåfør_id, kjøretøy_id }
→ Tildeler et oppdrag manuelt

POST /api/plan/generer
Body: { dato, avdeling_id }
→ Kjører optimalisering og returnerer foreslått plan
```

### ⬜ `tech/arkitektur.md`
Overordnet beskrivelse av systemarkitekturen:
- Frontend: hvilket rammeverk, hvilke hovedkomponenter, tilstandshåndtering
- Backend: rammeverk, hvordan er det strukturert (controllers, services, osv.)
- Database: type (SQL/NoSQL), hosting
- Algoritme: kjører den i backend, separat service, eller eksternt?
- Kommunikasjon mellom lag (REST, WebSocket, osv.)
- Deploymentoppsett (lokal, sky, Kubernetes)

### ⬜ `tech/algoritme.md`
Dokumentasjon av optimaliseringsalgoritmen – dette er et eget kapittel i rapporten.
- **Problem som løses:** hvilken variant av ressursplanlegging / VRP
- **Input:** hva sendes inn (oppdrag, sjåfører, kjøretøy, constraints)
- **Output:** hva returneres (plan, score, alternativer)
- **Constraints:** kjøre-/hviletid, førerkort, tilgjengelighet, kjøretøytype
- **Målfunksjon:** hva optimaliseres (fakturerte timer, antall oppdrag, osv.)
- **Algoritme/metode:** greedy, ILP, CP-SAT, heuristikk, genetisk, osv.
- **Begrensninger:** hva klarer den ikke håndtere

### ⬜ `tech/flytdiagrammer.md`
Tekstlig eller Mermaid-beskrivelse av viktige flyter. Minst:
- Flyten fra oppdrag kommer inn til sjåfør er varslet
- Flyten for manuell overstyring av algoritmeforslag
- Flyten for sykdomshåndtering / omrokkering

Eksempel i Mermaid:
```mermaid
flowchart TD
    A[Oppdrag mottas] --> B[Lagres i database]
    B --> C[Algoritme kjøres]
    C --> D[Plan vises til trafikkleder]
    D --> E{Trafikkleder godkjenner?}
    E -->|Ja| F[Sjåfør varsles]
    E -->|Nei| G[Manuell justering]
    G --> F
```

### ⬜ `tech/tech_stack_begrunnelse.md`
For hvert teknologivalg: hva valgte dere, og hvorfor. Spesielt viktig for diskusjonskapitlet.
Eksempel:
- **Frontend:** React – valgt fordi [begrunnelse], vurderte Vue men [grunn til at vi ikke valgte det]
- **Backend:** [teknologi] – valgt fordi...
- **Database:** [teknologi] – valgt fordi...
- **Algoritme:** [bibliotek/metode] – valgt fordi...

---

## 🔬 Forskning og metode

### ⬜ `metode/forskningsdesign.md`
- Hvilken overordnet forskningsmetode brukes (designscience, aksjonsforskning, casestudie)?
- Begrunnelse for valget
- Hvordan passer metoden til et utviklingsprosjekt som dette?

### ⬜ `metode/litteraturliste.md` eller `references.bib`
Liste over faktiske kilder dere har lest og vil sitere. AI-en skal **aldri** finne på referanser – men den kan hjelpe skrive teorikapittel hvis den vet hvilke kilder som finnes.

Format (BibTeX anbefales hvis dere bruker LaTeX, ellers enkel liste):
```
- Forfatter (år). Tittel. Tidsskrift/bok. DOI/URL.
```

Viktige kategorier å ha kilder på:
- Vehicle Routing Problem (VRP) / ressursplanlegging
- Transport Management Systems (TMS)
- Human-in-the-loop automation
- Algoritmer (den typen dere bruker)
- Relevant norsk transportforskning

### ⬜ `metode/teoriramme.md`
Hvilke teorier og konsepter støtter dere dere på, og hvordan kobler de til prosjektet?
- **Vehicle Routing Problem (VRP):** hvordan er dette relevant for Cephalo
- **Resource scheduling:** generell teori om ressursplanlegging
- **Human-in-the-loop:** begrunnelse for at trafikkleder alltid kan overstyre
- **[andre teorier]**

---

## 👥 Brukerinnsikt

### ✅ `brukerinnsikt/intervjuer/` *(oppsummerte MD-filer)*
Individuelle intervjufiler per bedrift.

### ✅ `brukerinnsikt/00_sammendrag_alle_intervjuer.md`
Tverrgående funn fra alle intervjuer.

### ✅ `brukerinnsikt/fit_gap_analyse.md` (eller tabell)
Funn fra trafikkledere som er tilpasset i appen.

### ⬜ `brukerinnsikt/personas.md`
Beskriv 2–3 brukerroller systemet er designet for:

```
## Trafikkleder
- Hovedbruker av systemet
- Tildeler oppdrag daglig, håndterer sykdom og endringer
- Har mye kunnskap i hodet om sjåfører og ruter
- Teknisk nivå: middels
- Frustrasjon med dagens løsning: trege systemer, ingen kapasitetsoversikt

## Transportleder / Admin
- Overordnet ansvar, ser på statistikk og utnyttelsesgrad
- Bruker systemet ukentlig, ikke daglig
- [osv.]

## Sjåfør (indirekte bruker)
- Mottar oppdrag via varsling
- Ikke direkte bruker av planleggingsplattformen
```

### ⬜ `brukerinnsikt/brukertester.md`
Resultater fra eventuelle brukertester eller uformelle tilbakemeldinger fra trafikkledere underveis. Selv korte notater er nyttig:
- Hvem testet (rolle, kontekst)
- Hva ble testet
- Hva fungerte
- Hva fungerte ikke / tilbakemelding

### ⬜ `brukerinnsikt/ui_flyt.md`
Tekstlig gjennomgang av de viktigste skjermene og brukerflytene:
- Hva ser trafikkleder når de logger inn
- Hvordan ser de dagens plan
- Hvordan tildeler de et oppdrag manuelt
- Hvordan godkjenner / avviser de algoritmeforslaget
- Hvordan håndterer de sykdom / omrokkering

---

## 📊 Krav og evaluering

### ⬜ `krav/funksjonelle_krav.md`
Liste over funksjonelle krav. For hvert krav:
- ID (f.eks. FK-01)
- Beskrivelse
- Prioritet (MoSCoW: Must / Should / Could / Won't)
- Kilde (hvem ba om dette – intervju, veileder, eget ønske)

Eksempel:
```
| ID    | Beskrivelse                                              | Prioritet | Kilde         |
|-------|----------------------------------------------------------|-----------|---------------|
| FK-01 | Systemet skal vise alle oppdrag for valgt dag            | Must      | Alle intervjuer |
| FK-02 | Trafikkleder skal kunne tildele oppdrag manuelt          | Must      | Alle intervjuer |
| FK-03 | Algoritmen skal generere en optimalisert dagplan         | Must      | Cephalo-team  |
| FK-04 | Trafikkleder skal kunne overstyre algoritmens forslag    | Must      | Ottem, Nordic Crane |
| FK-05 | Systemet skal vise sjåførs kjøre-/hviletidsstatus        | Should    | Nordic Crane  |
```

### ⬜ `krav/ikke_funksjonelle_krav.md`
Krav til systemets egenskaper:
- Ytelse: responstid, antall samtidige brukere
- Sikkerhet: autentisering, tilgangskontroll
- Brukervennlighet: skal kunne læres på X minutter
- Skalerbarhet: skal tåle X sjåfører, Y oppdrag per dag
- Tilgjengelighet: oppetid

### ⬜ `krav/kravsporing.md`
Sporing av krav gjennom implementasjon og testing:

```
| ID    | Krav (kort)                        | Implementert | Testet | Kommentar |
|-------|------------------------------------|:------------:|:------:|-----------|
| FK-01 | Vis oppdrag for valgt dag          | ✅           | ✅     |           |
| FK-02 | Manuell tildeling                  | ✅           | ⬜     | Ikke testet med bruker ennå |
| FK-03 | Algoritmegenerert plan             | ✅           | ✅     |           |
```

---

## 📝 Prosjekthistorikk og beslutninger

### ⬜ `prosjekt/beslutningslogg.md`
Logg over viktige tekniske og metodiske valg. Format:

```
## YYYY-MM-DD – [Tema for beslutningen]
**Beslutning:** Vi valgte X
**Alternativer vurdert:** Y, Z
**Begrunnelse:** ...
**Konsekvenser:** ...
```

Eksempler på beslutninger som bør dokumenteres:
- Valg av algoritme
- Valg av teknisk stack
- Valg av å inkludere/ekskludere en feature
- Endringer i systemdesign underveis

### ⬜ `prosjekt/sprint_logg.md`
Kort per sprint / uke:
- Hva ble planlagt
- Hva ble faktisk gjort
- Hindringer / avvik

Brukes direkte til metode- og prosesskapitlet i rapporten.

### ⬜ `prosjekt/endringslogg.md`
Hva endret seg fra tidlig MVP til nåværende versjon, og hvorfor. Viktig for diskusjonskapitlet.

### ⬜ `prosjekt/risikologg.md`
Identifiserte risikoer, sannsynlighet, konsekvens og tiltak. Brukes i forprosjektplan og metodekapitlet.

```
| Risiko                          | Sannsynlighet | Konsekvens | Tiltak              |
|---------------------------------|:-------------:|:----------:|---------------------|
| Algoritmen gir dårlig plan      | Middels       | Høy        | Fallback til manuell |
| Trafikkledere tar ikke i bruk   | Lav           | Høy        | Brukertesting tidlig |
```

---

## 🎓 Referanser og tidligere besvarelser

### ✅ `referanser/tidligere_besvarelser_oppsummert.md`
Oppsummerte punkter fra tidligere A-besvarelser.
> **Tips:** Strukturer det etter kapittel (hva gjorde de bra i innledning, metode, diskusjon osv.) så AI-en kan bruke det målrettet.

### ✅ `referanser/vaar_oppgave.md` / problemstilling
### ✅ `referanser/notater.md`

---

## ⚙️ Instruksjonsfiler til AI

Disse filene styrer hvordan AI-en oppfører seg i alle sesjoner. Legg dem i rotnivå av repoet.

### ⬜ `PROMPT_GUIDE.md`
Instruksjoner til AI-en om hvordan den skal bruke konteksten:

```markdown
# Instruksjoner for AI-bruk i Cephalo-repoet

## Prosjektkontekst
- Les alltid `context/master_context.md` først
- Bruk begreper fra `context/ordliste.md` konsekvent
- Følg formatkravene i `maler/04_teknisk_mal.pdf`

## Rapportskriving
- Rapporten skrives på norsk, formelt akademisk nivå
- Bruk passiv eller upersonlig form – ikke «vi mener» men «det kan argumenteres for»
  (med mindre veilederen har sagt noe annet)
- Rapportstruktur følger `context/rapportoutline.md`
- Sitater og referanser hentes KUN fra `referanser/litteraturliste.md` – finn ikke opp referanser

## Kodeassistanse
- Kodebasen er oppsummert i `tech/kodebase_oppsummering.md`
- Teknisk stack er beskrevet i `tech/tech_stack_begrunnelse.md`
- Følg eksisterende kodestil og struktur

## Hva AI ikke skal gjøre
- Ikke finn opp referanser eller kilder
- Ikke anta noe som ikke er dokumentert i kontekstfilene
- Ikke endre scope uten at det er beskrevet i `context/scope.md`
- Ikke skriv seksjoner som er markert som «ikke i scope»
```

### ⬜ `STATUS.md`
Oversikt over hva som er skrevet, hva som pågår og hva som mangler:

```markdown
# Rapportstatus

## Ferdig (klar for innlevering)
- [ ] Ingenting ennå

## Under arbeid
- [ ] Kapittel 1 – Innledning (utkast v1)
- [ ] Kravanalyse

## Ikke startet
- [ ] Kapittel 2 – Teori
- [ ] Kapittel 5 – Arkitektur
- [ ] ...

## Godkjent av veileder
- [ ] (ingenting ennå)
```

### ⬜ `DONT.md`
Eksplisitte forbud og begrensninger for AI-en:

```markdown
# Ting AI ikke skal gjøre

- Ikke finn opp referanser – bruk kun litteraturliste.md
- Ikke skriv at systemet har funksjoner det ikke har (sjekk scope.md)
- Ikke bruk «vi» i akademisk tekst med mindre det er eksplisitt godkjent
- Ikke anta at noe er testet med mindre det er dokumentert i brukertester.md
- Ikke omformuler problemstillingen – bruk den ordrett fra vaar_oppgave.md
- Ikke generer kode i et annet språk enn det som er spesifisert i tech_stack_begrunnelse.md
- Ikke legg til krav som ikke finnes i funksjonelle_krav.md
```

---

## 📁 Anbefalt mappestruktur

```
cephalo-bachelor/
├── PROMPT_GUIDE.md
├── STATUS.md
├── DONT.md
│
├── context/
│   ├── master_context.md
│   ├── ordliste.md
│   ├── scope.md
│   ├── rapportoutline.md
│   └── skrivestil_eksempel.md
│
├── maler/
│   ├── 01_generelle_retningslinjer_AIT.pdf
│   ├── 02_studiespesifikke_retningslinjer.pdf
│   ├── 03_mal_hovedrapport.docx
│   ├── 04_teknisk_mal.pdf
│   ├── sensurveiledning_punkter.md   ← lag denne
│   └── [resten av malene]
│
├── tech/
│   ├── kodebase_oppsummering.md
│   ├── datamodell.md
│   ├── api_oversikt.md
│   ├── arkitektur.md
│   ├── algoritme.md
│   ├── flytdiagrammer.md
│   └── tech_stack_begrunnelse.md
│
├── metode/
│   ├── forskningsdesign.md
│   ├── litteraturliste.md
│   └── teoriramme.md
│
├── brukerinnsikt/
│   ├── intervjuer/
│   │   ├── 00_sammendrag_alle_intervjuer.md
│   │   ├── bergen_bulk_transport.md
│   │   ├── harlem_solutions.md
│   │   ├── norlog_lakselv.md
│   │   ├── norlog_mo_i_rana.md
│   │   ├── norlog_tana.md
│   │   ├── ottem.md
│   │   └── svein_nordic_crane.md
│   ├── fit_gap_analyse.md
│   ├── personas.md
│   ├── brukertester.md
│   └── ui_flyt.md
│
├── krav/
│   ├── funksjonelle_krav.md
│   ├── ikke_funksjonelle_krav.md
│   └── kravsporing.md
│
├── prosjekt/
│   ├── beslutningslogg.md
│   ├── sprint_logg.md
│   ├── endringslogg.md
│   └── risikologg.md
│
└── referanser/
    ├── tidligere_besvarelser_oppsummert.md
    ├── vaar_oppgave.md
    ├── notater.md
    └── litteraturliste.md
```
