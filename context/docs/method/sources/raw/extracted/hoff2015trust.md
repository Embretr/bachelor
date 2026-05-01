# Trust in Automation: Integrating Empirical Evidence on Factors That Influence Trust (`hoff2015trust`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Full 28-page article read from abstract through conclusion and references. All three thesis-relevant areas (Ch 2.2 trust/adoption, Ch 5.3 adoption barriers, Ch 5.2 HITL performance) have been investigated. All major constructs (three-layered model, design recommendations, performance factors) are captured with verbatim quotes and page references.
  - **Gaps not investigated:** References section (pp. 429–434) — bibliography only, no claims to extract.

## Source metadata
- **BibTeX key:** `hoff2015trust`
- **Reference (APA 7):** Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors, 57*(3), 407–434. https://doi.org/10.1177/0018720814547570
- **Tilgang:** PDF
- **Raw source:** `../hoff2015trust.pdf`
- **Coverage in raw:** Full article, pp. 407–434 (PDF pages 1–28). Page offset: printed p. N = PDF page (N − 406).

## Sammendrag (2–3 setninger)

Hoff og Bashir (2015) gjennomfører en systematisk gjennomgang av 101 empiriske artikler (127 studier) om tillit til automatisering, publisert 2002–2013, og syntetiserer funnene i en tre-lags-modell: disposisjonell tillit (stabile individuelle trekk), situasjonell tillit (kontekstavhengige faktorer) og lært tillit (erfaringsbasert, dynamisk). Artikkelen identifiserer fem designfaktorer for pålitelig automatisering — utseende, brukervennlighet, kommunikasjonsstil, transparens/tilbakemelding og kontrollgrad — og konkluderer med at passende kalibrert tillit reduserer både overtillit (misuse) og undertillit (disuse). Bidragets kjerne er at tillit til automatisering er en dynamisk prosess, ikke en statisk egenskap, og at systemdesign kan påvirke alle tre lagene.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.2 ¶4 (trust and adoption) | Covered — empirisk grunnlag for tillit-kalibrering som supplement til Lee & See (2004) |
| Ch 5.3 ¶2 (usability and trust in algorithm output) | Covered — transparens og kontrollnivå som direkte designfaktorer |
| Ch 5.2 ¶3 (HITL theory and reliance) | Covered — trust vs. reliance-distinksjonen og situasjonelle faktorer |
| Ch 5.4 ¶2 (what cannot be automated) | Partial — eksperttillit/self-confidence-interaksjon er relevant |
| Ch 2.2 ¶1 (10-level automation scale) | Partial — bekrefter Parasuraman et al. (2000) men ikke primærkilde |

## Claims this source supports

### Claim 1: "Trust in automation is variably formed across three interdependent layers: dispositional, situational, and learned"
- **Suggested for:** Ch 2.2 ¶4 (first use of trust concept); Ch 5.3 ¶2 (explaining why individual coordinators vary in adoption)
- **Direkte sitat:** "Our analysis revealed three broad sources of variability in human–automation trust: the human operator, the environment, and the automated system. These variables respectively reflect the three different layers of trust identified by Marsh and Dibben (2003): dispositional trust, situational trust, and learned trust." (p. 413 / PDF 7)
- **Parafrase:** Tillit til automatisering er ikke én størrelse, men varierer langs tre dimensjoner: stabile individuelle trekk (disposisjonell), kontekstsensitive faktorer (situasjonell) og erfaring med det konkrete systemet (lært).
- **Forbehold:** Modellen er induktivt konstruert fra studier som primært bruker militære og luftfarts-domener; overføring til norsk transportdispatch er ikke validert.
- **Anvendelse på vårt case:** Hos trafikkoordinatorer vil disposisjonell tillit variere mellom individer (noen er skeptiske til automatisering generelt — jf. Ottem-caset), situasjonell tillit vil øke ved høy arbeidsbyrde (sykefravær), og lært tillit vil bygges opp over tid etter hvert som koordinatoren ser at Ressursplanleggers planer er presise.

---

### Claim 2: "Appropriate trust reduces misuse (overtrusting) and disuse (undertrusting)"
- **Suggested for:** Ch 2.2 ¶4 (trust and adoption); Ch 5.3 ¶2 (adoption barriers)
- **Direkte sitat:** "Accidents can occur when operators misuse automation by overtrusting it, or disuse automation as a result of undertrusting it (Parasuraman & Riley, 1997)." (p. 407 / PDF 1)
- **Parafrase:** Feil kalibrert tillit — enten for høy eller for lav — fører til suboptimal bruk av automatisering.
- **Forbehold:** Kilden kontekstualiserer misuse/disuse primært for sikkerhetskritiske systemer (luftfart, militær); konsekvensene i transportdispatch er planleggingsfeil, ikke ulykker.
- **Anvendelse på vårt case:** For Ressursplanlegger er overtrusting konkret: en koordinator som godkjenner alle planforslag uten override mister det kritiske overblikket som HITL-designet forutsetter. Undertrusting er like konkret: en koordinator som ignorerer algoritmens forslag og planlegger manuelt mister effektivitetsgevinsten systemet er ment å gi.

---

### Claim 3: "Transparency — exposing system reasoning — facilitates appropriate trust and reduces misuse/disuse"
- **Suggested for:** Ch 2.2 ¶5 (HITL as design constraint); Ch 5.3 ¶2 (trust in algorithm output)
- **Direkte sitat:** "Transparency refers to the degree to which 'the inner workings or logic [used by] the automated systems are known to human operators to assist their understanding about the system' (Seong & Bisantz, 2008, p. 611). Numerous studies have shown that designing systems that provide users with accurate, ongoing feedback about their reliability or how they operate can better facilitate appropriate trust." (p. 423 / PDF 17)
- **Parafrase:** Systemer som synliggjør sin egen logikk og pålitelighet fremmer kalibrert tillit hos operatøren.
- **Forbehold:** "Accurate, ongoing feedback" forutsetter at systemet faktisk kan kommunisere sin pålitelighet — Ressursplanlegger eksponerer konflikter og poengsum, men ikke full algoritmisk begrunnelse.
- **Anvendelse på vårt case:** Ressursplanleggers konfliktdeteksjon og poengfordeling (score breakdown) eksponerer algoritmens indre logikk — dette er nettopp den mekanismen Hoff & Bashir empirisk knytter til kalibrert tillit og redusert disuse; det begrenser risikoen for at koordinatorer avviser systemet uten grunn.

---

### Claim 4: "Level of control over automation affects perceived trustworthiness; mid-level control (system informs while acting) is perceived as more trustworthy than full autonomy"
- **Suggested for:** Ch 2.2 ¶3 (suggest + override design pattern); Ch 5.2 ¶4 (is suggest + override the right design?)
- **Direkte sitat:** "automation that takes over functions while providing information to the operator (~Level 7 automation) is perceived as more trustworthy than automation that takes over functions without providing any information to the operator (~Level 10 automation)" (p. 424 / PDF 18)
- **Parafrase:** Operatører stoler mer på automatisering som informerer dem enn på automatisering som handler stille.
- **Forbehold:** Nivå-referansen bruker Parasuraman et al. (2000) 10-trinns-skala; Ressursplanlegger er på nivå 5–6, ikke 7 — distinksjon gjelder analogt.
- **Anvendelse på vårt case:** Ressursplanleggers "suggest + approve"-modell (koordinatoren godkjenner eller overstyrer) er empirisk begrunnet: full automatisering av planlegging ville redusert koordinatorens opplevde tillit, mens nåværende design gir kontroll og informasjon som understøtter tillit.

---

### Claim 5: "Learned trust has two phases: initial (pre-interaction, reputation-based) and dynamic (real-time, performance-based)"
- **Suggested for:** Ch 5.3 ¶2 (adoption barriers — trust in algorithm output); Ch 5.3 ¶4 (what would production deployment require)
- **Direkte sitat:** "Learned trust represents an operator's evaluations of a system drawn from past experience or the current interaction. This layer of trust is directly influenced by the operator's preexisting knowledge and the automated system's performance." (p. 420 / PDF 14)
- **Parafrase:** Lært tillit deles i initial lært tillit (før bruk, basert på rykte og kunnskap om systemet) og dynamisk lært tillit (under bruk, basert på sanntidsytelse).
- **Forbehold:** Den dynamiske tillitens sensitivitet for feil avhenger av domenets risikoprofil; feil i planleggingssystemer er reversible, noe som kan dempe tillitsfall.
- **Anvendelse på vårt case:** For Ressursplanlegger innebærer dette at onboarding-perioden er kritisk: koordinatorens initielle lærte tillit baseres på demonstrasjoner og ryktet systemet har, mens dynamisk tillit bygges (eller brytes) gjennom de første dagenes faktiske planforslag.

---

### Claim 6: "Automation errors early in an interaction have a disproportionately large negative impact on trust"
- **Suggested for:** Ch 5.3 ¶2 (adoption barriers); Ch 5.3 ¶4 (production requirements)
- **Direkte sitat:** "automation errors that occur early in the course of an interaction have a greater negative impact on trust than errors occurring later (Manzey et al., 2012; Sanchez, 2006). This finding suggests that first impressions with automation are important, and early errors can have a lasting impact on the trust formation process." (p. 426 / PDF 20)
- **Parafrase:** Tidlige feil setter varige spor i tillitsbyggingen — mer enn sene feil.
- **Forbehold:** Effekten er dokumentert i laboratoriesettinger; i feltsituasjoner kan kontekstkunnskap dempe negative tillitseffekter.
- **Anvendelse på vårt case:** Under pilottesting av Ressursplanlegger bør systemet presenteres med testcases der det presterer godt — ikke med de vanskeligste edge-casene — for å unngå at tidlige planleggingsfeil setter permanent preg på koordinatorenes tillit.

---

### Claim 7: "Expert operators rely less on automation than novices; self-confidence and trust interact to determine manual vs. automated control preference"
- **Suggested for:** Ch 5.4 ¶2 (what cannot be automated — tacit knowledge dimension); Ch 5.3 ¶2 (adoption varies by coordinator expertise)
- **Direkte sitat:** "research has shown that individuals with greater subject matter expertise are less likely to rely on automation than novice operators are (Fan et al., 2008; Sanchez, Rogers, Fisk, & Rovira, 2011)." (p. 417 / PDF 11)
- **Parafrase:** Operatører med domeneekspertise stoler mer på egen vurdering enn på automatisering, sammenlignet med nybegynnere.
- **Forbehold:** "Subject matter expertise" skilles fra "experience with specific automated system" — erfarne koordinatorer er eksperter på domenet, ikke nødvendigvis på Ressursplanlegger.
- **Anvendelse på vårt case:** Erfarne trafikkoordinatorer med lang praksis vil sannsynligvis ha lavere initial reliance på Ressursplanlegger enn nyansatte — dette er en strukturell adopsjonsbremse som ikke løses av systemforbedringer alene, men krever opplæring og tid.

---

### Claim 8: "Trust guides but does not completely determine reliance"
- **Suggested for:** Ch 5.2 ¶3 (HITL theory — trust vs. use); Ch 5.3 ¶2 (adoption barriers)
- **Direkte sitat:** "Trust guides—but does not completely determine—reliance" (Lee & See, 2004, p. 51, sitert i Hoff & Bashir, p. 427 / PDF 21)
- **Parafrase:** Tillit er nødvendig, men ikke tilstrekkelig for at operatøren faktisk bruker automatiseringen; andre faktorer (tid, alternativkostnad, organisasjonskultur) spiller også inn.
- **Forbehold:** Sitert som Lee & See via Hoff & Bashir — bør primærkilden (lee2004trust) brukes der mulig.
- **Anvendelse på vårt case:** Selv om koordinatorer stoler på Ressursplanlegger, kan de velge manuell planlegging under tidspress eller ved mangel på støtte fra ledelsen — dette er relevant for å forstå adopsjonsgapet mellom demonstrert tillit og faktisk daglig bruk.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| operator | trafikkoordinator | Den menneskelige aktøren som interagerer med systemet |
| automated system | Ressursplanlegger (spesifikt planleggingsalgoritmen og forslagsgrensesnittet) | Kilden bruker "automated system" bredt; vi bruker det om selve plangeneratorkomponenten |
| decision aid / decision support system | Ressursplanlegger | Kilden studerer primært decision aids; Ressursplanlegger er av denne typen |
| misuse (overtrusting) | Godkjenning uten gjennomgang | Koordinator aksepterer planforslag uten å bruke override-funksjonaliteten |
| disuse (undertrusting) | Ignorering av algoritmens forslag | Koordinator planlegger manuelt til tross for tilgjengelig algoritmisk støtte |
| reliance | Faktisk bruk av planforslaget | Atferdsbasert utfall av tillit — om koordinatoren faktisk følger planen |
| trust | Tillit | Koordinatorens holdning til at Ressursplanlegger vil hjelpe dem nå planleggingsmålet |
| initial learned trust | Innledende erfaring med Ressursplanlegger | Hva koordinatoren tror om systemet basert på demonstrasjon, opplæring og rykte |
| dynamic learned trust | Løpende erfaringsbasert tillit | Tilliten som justeres dag-for-dag basert på planforslagenes kvalitet |
| transparency | Konfliktvisning og poengforklaring | Ressursplanleggers UI-elementer som synliggjør algoritmens resonneringsprosess |

## Forbehold og begrensninger

- **Domeneforskjell:** Studiene i denne gjennomgangen er primært fra militære, luftfarts- og laboratoriedomener (se Tabell 1, pp. 412 / PDF 6). Transportdispatch er ikke representert. Overføringen til norsk SME-kontext (8–45 kjøretøy, enkelt-koordinator-operasjoner) er ikke validert.
- **Type automatisering:** 74,8 % av studiene omhandlet "decision selection"-automatisering (Tabell 2, p. 412 / PDF 6), noe som er konsistent med Ressursplanleggers rolle — men de empiriske funnene er ikke testet i planleggingssystemer for transportdispatch spesifikt.
- **Outline MUST CITE:** Ch 2.2 ¶4 har MUST CITE på lee2004trust, ikke hoff2015trust. Hoff & Bashir supplerer lee2004trust empirisk — de kan siteres side om side: lee2004trust for det konseptuelle rammeverket, hoff2015trust for de empiriske faktorene.
- **Tillit ≠ Reliance:** Kilden er tydelig på at tillit ikke fullt ut predikerer reliance (p. 427 / PDF 21). Thesis bør ikke bruke "tillit" og "bruk" synonymt.
- **Ingen norsk kulturkontekst:** Kilden nevner kulturvariasjoner i tillit (pp. 413–414 / PDF 7–8) men har ikke studier fra Norden. Skandinaviske koordinatorer kan ha atypisk høy autonomiorienterng — dette er uspesifisert.
- **Situasjonell tillit og organisasjonskultur (p. 415 / PDF 9):** Kilden viser at sosiale normer fra kolleger påvirker tillitsatferd. For Ressursplanlegger betyr dette at lederens holdning kan veie tyngre enn selve systemkvaliteten under innføringen — men dette er ikke operasjonalisert i kilden.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Trust (in automation) | "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (Lee & See, 2004, gjengitt) | p. 409 / PDF 3 |
| Transparency | "the degree to which 'the inner workings or logic [used by] the automated systems are known to human operators to assist their understanding about the system'" (Seong & Bisantz, 2008) | p. 423 / PDF 17 |
| Learned trust | "an operator's evaluations of a system drawn from past experience or the current interaction" | p. 420 / PDF 14 |
| Dispositional trust | "an individual's enduring tendency to trust automation" | p. 413 / PDF 7 |
| Reliability (of automation) | "the consistency of an automated system's functions" | p. 424 / PDF 18 |

## Rammeverk og modeller

### Tre-lags-modell for tillit til automatisering (Figure 6, p. 427 / PDF 21)

| Lag | Hva det er | Typiske faktorer | Stabilitet |
|---|---|---|---|
| Dispositional Trust | Individets grunnleggende tilbøyelighet til å stole på automatisering | Kultur, alder, kjønn, personlighetstrekk | Stabil over tid og situasjoner |
| Situational Trust | Kontekstsensitiv tillit som varierer mellom interaksjoner | Systemtype, oppgavekompleksitet, arbeidsmengde, opplevd risiko, selvtillit, stemning | Varierer mellom situasjoner |
| Learned Trust (Initial) | Tillit basert på kunnskap om systemet *før* interaksjon | Preeksisterende kunnskap, systemets rykte, brand, forståelse av systemet | Endres ikke under enkeltinteraksjoner |
| Learned Trust (Dynamic) | Tillit som justeres *under* interaksjon basert på sanntidsytelse | Pålitelighet, validitet, prediktabilitet, avhengighet, feilinformasjon, timing av feil | Kan endre seg raskt under en interaksjon |

### Design recommendations for trustworthy automation (Table 3, p. 425 / PDF 19)

| Designfaktor | Anbefaling |
|---|---|
| Appearance/anthropomorphism | Øk antropomorfisme for å fremme tillit; tilpass til brukerens alder, kjønn og kultur |
| Ease of use | Forenkle grensesnittet; øk saliensen av automatisk tilbakemelding |
| Communication style | Kommunikasjonsstil (høflighet, kjønn, tone) påvirker tillit |
| Transparency/feedback | Gi nøyaktig, løpende tilbakemelding om pålitelighet og situasjonsfaktorer |
| Level of control | Tilpass kontrollnivå til brukerens psykologiske profil og oppgavedynamikk |

### Miljøfaktorer som styrker trust–reliance-forholdet (Figure 4, p. 418 / PDF 12)

Styrken av sammenhengen mellom tillit og reliance øker (fra LOW til HIGH) med:
- Kompleksiteten av automatiseringen
- Graden av nyhet i situasjonen
- Operatørens evne til å sammenligne automatisert vs. manuell ytelse
- Operatørens grad av beslutningsfrihet

## Key arguments / lines of reasoning

### Argument 1: Tillit er dynamisk og kan kalibreres via design
- **Premisser:** Tillit varierer langs tre lag; design-features påvirker særlig situasjonell og lært tillit; transparens og tilbakemelding er empirisk knyttet til kalibrert tillit.
- **Konklusjon:** Systemdesign kan aktivt forme tillitsnivå — feil design produserer enten over- eller undertillit.
- **Sted:** pp. 422–425 / PDF 16–19
- **Hvilke claims dette støtter:** Ch 2.2 ¶4, ¶5; Ch 5.3 ¶2

### Argument 2: Ekspertoperatørers lavere reliance er domene-ekspertise, ikke system-ekspertise
- **Premisser:** Subject matter expertise (domene) og system experience (lært tillit) er distinkte faktorer. Erfarne bønder stolte mindre på automatisering fordi de hadde domeneekspertise, ikke fordi de kjente systemet.
- **Konklusjon:** Lav initial reliance hos erfarne koordinatorer er en strukturell adopsjonsbremse — ikke en design-feil.
- **Sted:** pp. 418, 421 / PDF 12, 15
- **Hvilke claims dette støtter:** Ch 5.3 ¶2; Ch 5.4 ¶2

### Argument 3: Tidlige feil setter varige tillitsspor
- **Premisser:** Initial interaction experiences dominerer trust formation; feil på "lette" oppgaver er mer skadelig enn feil på vanskelige.
- **Konklusjon:** Onboarding-strategi bør presentere systemet på oppgaver det mestrer godt, for å etablere positiv lært tillit tidlig.
- **Sted:** p. 426 / PDF 20
- **Hvilke claims dette støtter:** Ch 5.3 ¶2, ¶4

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Costa Concordia-forlis (2012) | Undertrusting: kapteinen stolte ikke på navigasjonssystemet | p. 408 / PDF 2 |
| Turkish Airlines flight 1951 (2009) | Overtrusting: piloter stolte blindt på autopiloten etter feilmåling | p. 408 / PDF 2 |
| Eldre voksne og decision aids (Ho et al., 2005) | Alder påvirker reliance-atferd: eldre stolte mer, men kalibrerte ikke bedre | p. 414 / PDF 8 |
| Erfarne bønder og automatiske alarmer (Sanchez et al., 2011) | Domeneekspertise → lavere reliance på automatisering | pp. 417–418, 421 / PDF 11–12, 15 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 101 artikler, 127 studier inkludert i gjennomgangen | Studier | Jan 2002 – Jun 2013 | p. 407 / PDF 1 |
| 74,8 % av studiene omhandlet "decision selection"-automatisering | Andel av 127 studier | 2002–2013 | p. 412 / PDF 6 |
| 34 % målt tillit via reliance-atferd; 4 % via selvrapport; 62 % begge | Andel av 127 studier | 2002–2013 | p. 412 / PDF 6 |
| 33 av 127 studier manipulerte design features eksperimentelt | Antall studier | 2002–2013 | p. 427 / PDF 21 |

## Forfatter-perspektiv / metodologi

Systematisk litteraturgjennomgang (ikke empirisk primærstudie). Inkluderingskriterier: (1) resultat av et human-subjects-eksperiment, (2) deltakerne interagerte med et automatisert system for å nå et mål, (3) tillit (eller tillitsatferd) ble målt. Syntesen er induktiv — tre-lags-modellen er konstruert fra funnene, ikke en a priori teori. Artikkelen siterer Lee & See (2004) som konseptuell grunnstein og bygger videre med empiri fra 2002–2013.