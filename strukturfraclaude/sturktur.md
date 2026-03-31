# AI-skrivesystem — Cephalo Bachelor

---

## Kjerneproblemet AI-skriving må løse

AI har null hukommelse mellom sesjoner. Kvaliteten på output er **direkte proporsjonal med kvaliteten på konteksten du gir den**. Hele systemet ditt handler derfor om én ting: gjøre kontekstinjeksjon så presis og enkel at du aldri trenger å forklare noe to ganger.

---

## Anbefalt mappestruktur

```
bachelor/
│
├── context/          ← Det AI alltid leser. Oppdateres løpende.
│   ├── context.md    ← Identitet, problemstilling, stack, status
│   ├── disposisjon.md
│   ├── ordliste.md
│   ├── scope.md
│   ├── intervju-funn.md
│   └── fitgap.md
│
├── rapport/          ← Alt output. Det som faktisk skrives.
│   ├── kapitler/
│   │   ├── kap1-innledning.tex
│   │   ├── kap2-teori.tex
│   │   └── ...
│   ├── bibtex/
│   │   └── referanser.bib
│   └── main.tex
│
├── vurdering/        ← Sensorveiledning, kriterier. AI sjekker mot dette.
│   ├── sensurveiledning.md
│   ├── vurderingskriterier.md
│   └── tidligere-besvarelser.md
│
├── tech/             ← Teknisk kontekst (Embret eier)
├── krav/
├── metode/
├── prosjekt/
│
└── prompts/          ← Gjenbrukbare promptmaler per agentrolle
    ├── writer.md
    ├── redtrad.md
    ├── kvalitet.md
    └── context-gather.md
```

---

## Skriveflyt — fase for fase

### Fase 0: Ryggraden (gjøres én gang)

Før ett eneste kapittel skrives, lager dere et dokument som aldri endres: **the thesis spine**. Dette er selve argumentasjonstråden i rapporten — én setning per kapittel som beskriver hva kapitlet *bidrar med* til den overordnede argumentasjonen.

```
# thesis-spine.md

Problemet: Trafikkledere i norske transportbedrifter planlegger manuelt,
basert på kunnskap som ikke er formalisert, med trege og utdaterte systemer.

Kapittel 1: Etablerer at problemet er reelt og viktig.
Kapittel 2: Viser at VRP-teori og human-in-the-loop er relevant ramme.
Kapittel 3: Forklarer hvordan vi samlet data og bygde systemet.
Kapittel 4: Presenterer hva vi fant og hva vi bygde.
Kapittel 5: Argumenterer for at Cephalo delvis løser problemet, men med begrensninger.
Kapittel 6: Konkluderer og peker på veien videre.
```

Alle agenter leser denne filen. Den er grunnen til at rapporten henger sammen.

---

### Fase 1: Detaljert disposisjon per seksjon

Før AI skriver noe, lager dere en **detaljert seksjonsplan** for kapitlet. Ikke bare overskrifter — men hva *hvert avsnitt* skal inneholde.

```
# Seksjonsplan: Kapittel 3 — Metodologi

## 3.1 Research Design (ca. 400 ord)
- Avsnitt 1: Definer Design Science Research (DSR), 1 setning
- Avsnitt 2: Forklar hvorfor DSR passer et utviklingsprosjekt
- Avsnitt 3: Koble til vårt prosjekt konkret — artefaktet er Cephalo
- Avsnitt 4: Begrensninger ved valget

## 3.2 Data Collection (ca. 600 ord)
- Avsnitt 1: Semi-strukturert intervju — definisjon og begrunnelse
- Avsnitt 2: Utvalg — 7 bedrifter, hvem, hvorfor disse
- Avsnitt 3: Intervjuprosessen — forberedelse, gjennomføring, opptak
- Avsnitt 4: Transkribering via Sonix.ai
...
```

Denne filen er skriveinstruksen. AI-en skriver bare det som står her — ingenting mer.

---

### Fase 2: Context gather (før hvert kapittel)

Før AI skriver, identifiserer dere hvilke kontekstfiler som er relevante for akkurat dette kapitlet. Lim dem inn i riktig rekkefølge.

```
# prompts/context-gather.md

For kapittel [X], les disse filene i denne rekkefølgen:
1. context/context.md          ← alltid først
2. context/disposisjon.md      ← alltid
3. rapport/kapitler/[forrige]  ← alltid (for kontinuitet)
4. [kapittel-spesifikke filer] ← varierer
```

| Kapittel | Ekstra kontekstfiler |
|----------|---------------------|
| 1 — Innledning | scope.md, thesis-spine.md |
| 2 — Teori | metode/teoriramme.md, metode/litteraturliste.md |
| 3 — Metode | metode/forskningsdesign.md, prosjekt/sprint-logg.md |
| 4 — Funn | intervju-funn.md, fitgap.md, tech/algoritme.md, tech/arkitektur.md |
| 5 — Diskusjon | alle kapitler skrevet hittil, thesis-spine.md, vurdering/ |
| 6 — Konklusjon | alle kapitler, thesis-spine.md |

---

### Fase 3: Writer agent

Skrivepromptens struktur er avgjørende. Bruk alltid denne malen:

```
# prompts/writer.md

Du er en akademisk skribent. Du skriver ett avsnitt om gangen,
på formell akademisk engelsk.

## Les først
[lim inn context.md]
[lim inn thesis-spine.md]
[lim inn seksjonsplan for dette kapitlet]
[lim inn forrige kapittel hvis det finnes]

## Din oppgave
Skriv [seksjon X.Y] i kapittel [N].

Seksjonsplanen sier:
[lim inn de relevante avsnittspunktene]

## Krav
- Maks [X] ord
- Bruk \parencite{} for kildehenvisninger
- Bruk bare begreper fra ordliste.md
- Ikke skriv utenfor scope.md
- Ikke skriv neste seksjon

## Kilder tilgjengelig
[lim inn relevante BibTeX-nøkler fra referanser.bib]
```

**Viktig:** Be om én seksjon om gangen, ikke ett helt kapittel. Kortere output = høyere kvalitet.

---

### Fase 4: Red thread agent

Etter hvert ferdigskrevet kapittel kjører dere rødtråd-sjekken. Dette er en separat Claude-sesjon med en helt annen instruksjon:

```
# prompts/redtrad.md

Du er en kritisk leser. Du sjekker IKKE grammatikk eller stil.
Du sjekker KUN logisk sammenheng og argumentasjonstråd.

## Les
[thesis-spine.md]
[alle kapitler skrevet hittil]

## Din oppgave
Svar på disse spørsmålene:

1. PÅSTANDER: List alle faktapåstander i [kapittel X].
   Har noen av dem mangler støtte i teori eller data?

2. KONTINUITET: Introduserer dette kapitlet begreper eller
   argumenter som ikke er satt opp i foregående kapitler?

3. SELVMOTSIGELSER: Er det noe i dette kapitlet som
   motsier noe skrevet tidligere?

4. FORANKRING: Henger kapitlets konklusjon tilbake til
   problemstillingen i context.md?

Svar med konkrete sitatreferanser, ikke generelle kommentarer.
```

Output fra denne agenten lagres i `review/redtrad-kap[N].md` og brukes til å rette kapitlet.

---

### Fase 5: Kvalitetsagent

Etter rødtråd-sjekken kjøres kvalitetssjekken mot sensorveiledningen:

```
# prompts/kvalitet.md

Du er en sensor ved NTNU. Du vurderer bacheloroppgaver.

## Les
[vurdering/sensurveiledning.md]
[vurdering/vurderingskriterier.md]
[kapittel X som skal vurderes]

## Din oppgave
Gi en kort vurdering av dette kapitlet mot hvert kriterium i
sensurveiledningen.

For hvert kriterium:
- Karakter: A / B / C / ikke vurdert ennå
- Hva er bra
- Hva mangler eller er svakt
- Konkret forslag til forbedring (én setning)

Vær ærlig og kritisk. Ikke vær snill.
```

---

## Fullstendig flyt per kapittel

```
┌─────────────────────────────────────────────────────┐
│  1. Oppdater context.md og STATUS.md                │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  2. Lag seksjonsplan (dere, ikke AI)                │
│     Hva skal hvert avsnitt si?                      │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  3. Context gather                                  │
│     Hvilke filer er relevante for dette kapitlet?   │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  4. Writer agent (én seksjon om gangen)             │
│     → Seksjon ferdig? Dere leser og godkjenner.     │
│     → Ikke OK? Gi feedback og kjør på nytt.         │
│     → OK? Gå til neste seksjon.                     │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  5. Red thread agent                                │
│     Lagre output i review/redtrad-kap[N].md         │
│     Rett kapitlet basert på funn.                   │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  6. Kvalitetsagent                                  │
│     Lagre output i review/kvalitet-kap[N].md        │
│     Rett kapitlet basert på funn.                   │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  7. Commit og oppdater STATUS.md                    │
└─────────────────────────────────────────────────────┘
```

---

## Om agent teams

Ekte autonome multi-agent systemer (der agenter kommuniserer uten at dere er i løkken) er mulig med Claude Code, men krever mer oppsett enn det er verdt for en bacheloroppgave. Det dere beskriver — ulike agenter med ulike roller — er fullt mulig å simulere manuelt med separate Claude-sesjoner og faste promptmaler. Det fungerer like bra i praksis, og dere beholder kontrollen.

Hvis dere vil eksperimentere med ekte orkestrering: Claude Code kan kjøre subagenter. Men start med manuell simulering — det er raskere å komme i gang og feilmarginen er lavere.

---

## De tre tingene som faktisk avgjør kvaliteten

1. **Seksjonsplanen er viktigere enn selve prompting-en.** Hvis dere vet nøyaktig hva hvert avsnitt skal si, vil AI alltid produsere noe brukbart. Uten den vil dere få generisk vaffel som tar lengre tid å rette enn å skrive selv.

2. **Kjør aldri writer og red thread i samme sesjon.** Writer-agenten er satt opp til å produsere — den er ikke objektiv. Red thread-agenten trenger en ren slate uten den foregående konteksten for å se feil.

3. **Oppdater thesis-spine.md etter hvert kapittel.** Hvis et ferdig kapittel endrer argumentasjonen litt, oppdater ryggraden. Den er sannhetskilden for sammenheng på tvers.
