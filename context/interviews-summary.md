# Intervjusammendrag – Ressursplanlegger brukerundersøkelse

**Dato:** 4. mars 2026  
**Antall intervjuer:** 7  
**Målgruppe:** Transportoperatører / trafikkleder i norske transportbedrifter

---

## Intervjuoversikt

| Bedrift | System i dag | Flåte / skala | Ruter/dag | Planhorisont | Automatisering |
|--------|-------------|--------------|:---------:|-------------|---------------|
| Bergen Bulk Transport | Ingen (manuelt, telefon, hukommelse) | 8–20 sjåfører | Ukjent | Dag-til-dag | Skeptisk pga. kostnad; mener TMS blir relevant ved 15–20+ biler |
| Harlem Solutions | Opptur + kundeintegrasjoner | Ukjent | Standardruter, 1 ordre/dag auto-generert | Varierer | Skeptisk – kundeordrer varierer daglig, ingen dager er like |
| Norlog Lakselv | Timpex (kan auto-generere faste turer) | Middels | Ukjent | Faste + variable | Positiv for faste ruter; jobber med Timpex–Admin-integrasjon |
| Norlog Mo i Rana | Timpex + Admin + (Admit nevnt) | Middels | Ukjent | Ukjent | Positiv; minimerer gule lapper, alt i system |
| Norlog Tana | Trimtex | Liten (~5 ruter/dag, 7–20 mil) | ~5 | Dag-til-dag | Positiv; men sykdom er daglig problemløsning |
| Ottem | Eget ordresystem | ~45 biler, 3 avdelinger | Ukjent | ~1 min per oppdrag | Skeptisk – ordrer kanselleres, ting skjer fort |
| Nordic Crane (Svein) | Eget ordresystem (planlegger systembytte) | Kran + transport | 3–4 per sjåfør | 5 timer – 2 måneder | Delvis positiv; vil ha auto-distribusjon 18–24t før utførelse |

---

## Gjennomgående funn

### 1. Alle tildeler oppdrag manuelt
Ingen av respondentene har full automatisk tildeling. Selv bedrifter med systemer (Timpex, Opptur) gjør selve sjåfør-tildelingen manuelt. Det er dette produktet primært skal løse.

### 2. Treghet er det største problemet med eksisterende systemer
Timpex og Trimtex beskrives gjennomgående som **ekstremt trege**, spesielt med mange samtidige brukere. Norlog Mo i Rana beskriver det som "ekstremt tregt" med "gammelt grensesnitt" og sier hastighet er "100 prosent" det viktigste å forbedre. Norlog Lakselv bekrefter at ytelsen faller dramatisk med flere brukere på serveren samtidig. Dette er en klar mulighet for et moderne alternativ.

### 3. Kritisk kunnskap sitter i operatørens hode
Alle respondenter har kunnskap som ikke er formalisert:
- Hvem har rett førerkort / kompetanse
- Hvem er erfaren på hvilke ruter
- Hvem kan ta utfordrende oppdrag (vinter, scanning, farlig gods)
- Hvem nærmer seg overtidsgrenser

Et godt system må gjøre det mulig å **digitalisere og bruke denne kunnskapen ved tildeling**.

### 4. Sykdomshåndtering varierer mye
- Noen synes det er enkelt: Norlog Lakselv ("2–3 tastetrykk"), Nordic Crane ("27 sekunder")
- Norlog Tana beskriver det som **daglig, krevende problemløsning**: "jeg sitter jo egentlig med den problemløsningen hver eneste dag" — hyppige sykefravær krever korsruter og rollebytter
- Ottem peker på at ordrer kanselleres uforutsigbart, noe som krever lignende omrokkeringsevne
- Avhenger sterkt av antall tilgjengelige sjåfører, rutefleksibilitet, og om rutene krever spesialkompetanse (f.eks. scanning hos Norlog Tana)

### 5. Fakturering er tett koblet til planlegging
Timpex og Opptur brukes til fakturering. Et nytt system **må enten integrere mot eksisterende faktureringssystem eller ha egne faktureringsfunksjoner**.

### 6. Holdning til full automatisering er delt
- **Positive:** Norlog Lakselv, Mo i Rana, Tana
- **Skeptiske:** Harlem Solutions, Ottem, Bergen Bulk Transport
- **Delvis positive:** Nordic Crane

Skeptikerne peker på uforutsigbarhet i transport og behovet for menneskelig kontroll. Ottem: "i transport skjer ting fryktelig fort... sitter på et oppdrag, og så ble det kansellert." Men selv skeptikerne aksepterer forslag: "det må være noen som sitter og tenker bak meg da." Konsensus: systemet bør **foreslå en plan som operatøren kan korrigere** – ikke erstatte operatøren fullstendig.

Nordic Crane ønsker spesifikt automatisk distribusjon **18–24 timer før oppdraget** — ikke sanntid, men planleggingshorisont. De planlegger systembytte i år og håper det nye systemet har denne funksjonen.

---

## Tildelingskriterier (hva vurderes ved sjåfør-matching)

Rangert etter hyppighet nevnt på tvers av intervjuer:

1. **Tilgjengelighet / posisjon** – hvem er ledig og nærmest
2. **Erfaring** – særlig på krevende ruter
3. **Kjøre- og hviletid** – lovpålagt, kritisk
4. **Kompetanse / førerkort** – rett sertifikat for riktig oppdrag
5. **Kjennskap til rute** – spesielt relevant i nord
6. **Utstyr** – riktig bil til riktig oppdrag
7. **Overtidsstatus** – tas hensyn til, spesielt mot årsgrenser

---

## Kommunikasjon med sjåfører

- Primært via **app med push-varsler** (Timpex Confirm hos Norlog Lakselv/Mo i Rana; ordreapp hos Harlem/Opptur)
- **Telefon direkte** brukes av Norlog Tana og Bergen Bulk Transport
- Nordic Crane: sjåfører har 3–4 oppdrag per dag, kommuniserer kun ved avvik
- Kommunikasjon skjer helst kun ved avvik/problemer underveis

## Operasjonelle detaljer per bedrift

| Bedrift | Særtrekk fra intervju |
|---------|----------------------|
| Bergen Bulk | Helt manuelt; vurderer TMS først ved 15–20+ biler; "gamlemåten" |
| Harlem | Noen kunder auto-integrert med ordresystem → ordrer flyter inn automatisk |
| Norlog Lakselv | Timpex kan auto-generere faste turer/oppdrag; jobber med Admin-integrasjon |
| Norlog Mo i Rana | Bruker 3 systemer (Admin + Timpex + Admit); minimerer gule lapper; hastighet = #1 prioritet |
| Norlog Tana | ~5 ruter/dag, 7–20 mil; matvarer/temperaturkontrollert; scanning-krevende ruter; sykdom er daglig utfordring |
| Ottem | 45 biler, 3 avdelinger; ~1 min per oppdrag; ordrer kanselleres uforutsigbart; vil ha notifikasjon før auto-tildeling |
| Nordic Crane | Kran + transport; transport "mye mer krevende"; alle sjåfører har like sertifikater → erfaring avgjør; planhorisont 5t–2mnd |

---

## Adopsjonskriterier – hva skal til for at systemet tas i bruk

1. **Kostnad vs. nytte** – klart viktigst for de fleste
2. **Brukervennlighet** og lav opplæringstid
3. **Integrasjon** med eksisterende systemer (fakturering, Admin)
4. **Hastighet** – systemet må reagere raskt
5. **Tillit** – operatøren må kunne stole på planen, og enkelt overstyre den

---

## Anbefalinger til produktutvikling

- **Prioriter ytelse** – treghet er deal-breaker vs. Timpex
- **Bygg "suggest + override"** – ikke full auto; la operatøren korrigere planen
- **Digitaliser sjåførkompetanse** – førerkort, erfaring, rutehistorikk som strukturerte felter
- **Støtt sykdomshåndtering** – rask omrokkeringsflyt er høy prioritet for enkelte avdelinger
- **Integrer fakturering** – eller gjør det enkelt å koble til eksisterende løsning
- **Støtt hierarki** – flere avdelinger med egne trafikkleder (f.eks. Ottem)
- **Tidsstyrt varsling** – automatisk utsending til sjåfør X timer før oppdrag (klar etterspørsel)
