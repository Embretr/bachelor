# A Model for Types and Levels of Human Interaction with Automation (`parasuraman2000automation`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Full 12-page article read. All thesis-relevant areas investigated: the 10-level LOA scale, the four-type model, human performance consequences, and automation reliability. Three spot-checks passed.
  - **Gaps not investigated:** References section and author bios only (pages 295–297) — no extractable thesis content.

## Source metadata
- **BibTeX key:** `parasuraman2000automation`
- **Reference (APA 7):** Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics—Part A: Systems and Humans*, *30*(3), 286–297. https://doi.org/10.1109/3468.844354
- **Tilgang:** PDF (downloaded via NTNU/IEEE Xplore — download confirmation visible on each page)
- **Raw source:** `../parasuraman2000automation.pdf`
- **Coverage in raw:** Full article, pp. 286–297. Printed page offset: printed p. = PDF p. + 285. Dual-page format used throughout (e.g., `p. 287 / PDF 2`).

## Sammendrag (2–3 setninger)

Parasuraman, Sheridan og Wickens presenterer en to-dimensjonal modell for å klassifisere automasjon i menneskelig–maskin-systemer: fire *typer* (informasjonsinnhenting, informasjonsanalyse, beslutning og handlingsvalg, handlingsutførelse) og ti *nivåer* per type (fra fullt manuell til fullt autonom). Modellen tilbyr primære evalueringskriterier basert på menneskelige ytelseskonsekvenser (arbeidsbelastning, situasjonsbevissthet, komplacens, ferdighetstap) og sekundære kriterier (systemets pålitelighet, kostnad ved feil beslutning). Kjerneargumentet er at valg av automasjonsnivå ikke skal drives av teknisk kapasitet alene, men av konsekvensene for operatøren som til syvende og sist må håndtere situasjoner der automasjonen svikter.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.2 ¶1 (HITL-definisjon og 10-nivå-skala) | **Covered** — Table I gir skalaen verbatim; pozisjoneringen av «system foreslår, menneske godkjenner» = nivå 5 |
| Ch 2.2 ¶2 (Hvorfor HITL er nødvendig) | **Partial** — kilden argumenterer for menneskelig kontroll pga. ytelseskostnader ved høy automasjon, men bruker ikke transport som eksempel |
| Ch 2.2 ¶4 (Tillit og adopsjon) | **Partial** — kilden nevner at upålitelighet senker tillit; selve trust-begrepet er bedre dekket av `lee2004trust` |
| Ch 5.2 ¶3 (HITL-teori i diskusjon) | **Covered** — «out-of-the-loop»-konseptet og ytelseskostnader ved høy automasjon direkte relevant |
| Ch 5.4 ¶2 (Hva kan ikke automatiseres) | **Partial** — kilden argumenterer for at menneskelig innblanding alltid trengs ved høy-risiko beslutninger |

---

## Claims this source supports

### Claim 1: Automation can be applied to four functional types, each at varying levels

- **Suggested for:** Ch 2.2 ¶1 (primary), Ch 5.2 ¶3 (secondary)
- **Direkte sitat:** "We propose that automation can be applied to four broad classes of functions: 1) information acquisition; 2) information analysis; 3) decision and action selection; and 4) action implementation. Within each of these types, automation can be applied across a continuum of levels from low to high, i.e., from fully manual to fully automatic." (p. 286 / PDF 1)
- **Parafrase:** Automasjon er ikke alt-eller-intet, men varierer langs to dimensjoner: hva slags funksjon som automatiseres og hvor mye av den som automatiseres.
- **Forbehold:** Modellen er normativ/analytisk, ikke deskriptiv — den foreskriver ikke ett riktig nivå, men gir et rammeverk for å *velge*.
- **Anvendelse på vårt case:** Ressursplanlegger automatiserer primært én type: *decision and action selection* (hvem tildeles hva), mens informasjonsinnhenting (oppdragsdata, sjåførtilgjengelighet) og handlingsutførelse (kommunikasjon til sjåfør) forblir manuelle — dette plasserer systemet som en hybrid langs de fire dimensjonene, noe som legitimerer at det beskrives som delvis automatisert heller enn fullt automatisk.

---

### Claim 2: The 10-level LOA scale for decision and action selection (Table I)

- **Suggested for:** Ch 2.2 ¶1 (primary — define scale and position Ressursplanlegger)
- **Direkte sitat (Table I verbatim, p. 287 / PDF 2):**

  > HIGH  
  > 10. The computer decides everything, acts autonomously, ignoring the human.  
  > 9. informs the human only if it, the computer, decides to  
  > 8. informs the human only if asked, or  
  > 7. executes automatically, then necessarily informs the human, and  
  > 6. allows the human a restricted time to veto before automatic execution, or  
  > 5. executes that suggestion if the human approves, or  
  > 4. suggests one alternative  
  > 3. narrows the selection down to a few, or  
  > 2. The computer offers a complete set of decision/action alternatives, or  
  > LOW  
  > 1. The computer offers no assistance: human must take all decisions and actions.

- **Parafrase:** Skalaen definerer et kontinuum fra fullt manuell (1) til fullt autonom (10). Nivå 4 = systemet foreslår én løsning, men mennesket bestemmer. Nivå 5 = systemet *gjennomfører* forslaget, men bare dersom mennesket aktivt godkjenner. Nivå 6 = systemet gjennomfører automatisk, men gir mennesket et tidsbegrenset veto.
- **Forbehold:** Skalaen ble opprinnelig utviklet for *beslutning og handlingsvalg* (kolonne 3 i modellen). For informasjonsinnhenting og -analyse gjelder et annet antall nivåer — forfatterne erkjenner dette eksplisitt (p. 288 / PDF 3).
- **Anvendelse på vårt case:** Ressursplanlegger opererer på **nivå 5** for tildeling: algoritmen genererer ett planforslag (nivå 4), men planen trer først i kraft når trafikkoordinatoren eksplisitt godkjenner — dette er presist det som beskrives som «executes that suggestion if the human approves». Nivå 6 ville vært å sende planen automatisk med mulighet for å stoppe den innen et tidsvindu — noe Ressursplanlegger bevisst ikke gjør. Dette skillet er viktig for Ch 2.2.

---

### Claim 3: High-level decision automation leads to «out-of-the-loop» unfamiliarity

- **Suggested for:** Ch 2.2 ¶2 (støtte for HITL-nødvendighet), Ch 5.2 ¶3 (diskusjon av HITL-teori)
- **Direkte sitat:** "These potential costs—reduced situation awareness, complacency, and skill degradation—collectively demonstrate that high-level automation can lead to operators exhibiting 'out-of-the-loop' unfamiliarity [47]. All three sources of vulnerability may pose a threat to safety in the event of system failure." (p. 291 / PDF 6)
- **Parafrase:** Når automasjon konsekvent tar beslutningene, mister operatøren situasjonsforståelse, begynner å stole blindt på systemet (komplacens), og forringer sine egne ferdigheter — tre effekter som til sammen gjør det vanskelig å gripe inn når systemet svikter.
- **Forbehold:** Forskningen er primært fra luftfart og prosesskontroll (kjernekraft, fly). Konsekvensenes alvorlighetsgrad er lavere i transportplanlegging, men *risikoen for de tre effektene* er strukturelt den samme.
- **Anvendelse på vårt case:** Trafikkoordinatorer som godkjenner planforslag daglig uten å inspisere dem kritisk risikerer å miste oversikten over sjåfører og oppdrag (situasjonsbevissthet) og til slutt bli avhengige av systemet på en måte som gjør dem sårbare ved algoritmesvikt. Ressursplanleggers designvalg — synlig konfliktdeteksjon, skåring, mulighet for manuell overstyring — er direkte mottiltak mot disse tre effektene.

---

### Claim 4: Complacency is the failure to monitor automation when it is highly but imperfectly reliable

- **Suggested for:** Ch 5.2 ¶3, Ch 5.3 ¶2 (trust and adoption barriers)
- **Direkte sitat:** "if automation is highly but not perfectly reliable in executing decision choices, then the operator may not monitor the automation and its information sources and hence fail to detect the occasional times when the automation fails [57], [58]. This effect of over-trust or 'complacency' is greatest when the operator is engaged in multiple tasks" (p. 291 / PDF 6)
- **Parafrase:** Komplacens er ikke likegyldighet, men en konsekvens av at pålitelig automatisering gjør aktiv overvåking til en ulønnsom strategi for operatøren — til systemet feiler.
- **Forbehold:** Effekten er størst der automasjonen håndterer sekvensielle beslutninger (f.eks. overvåke fly i ATC). Transportplanlegging er batch-basert (én plan per dag), noe som gir koordinatoren naturlige sjekkpunkter.
- **Anvendelse på vårt case:** En trafikkoordinator som stoler på at Ressursplanlegger alltid produserer gyldige planer, kan slutte å inspisere deviations og konflikter — og da miste evnen til å oppdage sjeldne men alvorlige feil (f.eks. dobbeltbooking av sjåfør uten kompetanse). Avvikspanelet i UI-et er et direkte tiltak mot dette.

---

### Claim 5: Automation reliability is a critical secondary evaluative criterion — unreliability lowers operator trust

- **Suggested for:** Ch 2.2 ¶4 (tillit og adopsjon), Ch 5.3 ¶2 (adoption barriers)
- **Direkte sitat:** "Automation reliability is an important determinant of human use of automated systems because of its influence on human trust [66] [67]. Unreliability lowers operator trust and can therefore undermine potential system performance benefits of the automation." (p. 292 / PDF 7)
- **Parafrase:** Pålitelighet er ikke bare et teknisk mål, men den mekanismen som bestemmer om operatøren faktisk benytter systemet.
- **Forbehold:** Kilden har ikke egne empiriske data om trust—det er sekundærreferanser. Lee & See (2004) `lee2004trust` er primærkilden for trust i automasjon; parasuraman2000automation brukes her kun som støttekilde for at pålitelighet er en sekundær evalueringsdimensjon.
- **Anvendelse på vårt case:** Ressursplanleggers adopsjonsbarriere er direkte avhengig av at koordinatorene opplever planforslagene som pålitelige — én feilaktig tildeling som ikke fanges opp, kan undergrave tillitten til systemet som helhet, selv om det generelt presterer godt.

---

### Claim 6: Human performance consequences are the primary evaluative criteria for automation design

- **Suggested for:** Ch 2.2 ¶1 (rammeverk for HITL-design), Ch 5.2 ¶3
- **Direkte sitat:** "The human performance consequences of particular types and levels of automation constitute primary evaluative criteria for automation design using our model." (p. 286 / PDF 1)
- **Parafrase:** Valg av automasjonsnivå skal primært begrunnes med hva som skjer med menneskelig ytelse — ikke med teknisk kapasitet eller kostnadseffektivitet alene.
- **Forbehold:** Modellen er kvalitativ — den gir ikke kvantitative terskler for når ett nivå er bedre enn et annet.
- **Anvendelse på vårt case:** Ressursplanleggers valg av nivå 5 (coordinator approval required) er nettopp begrunnet med menneskelige ytelseshensyn: koordinatorens situasjonsbevissthet og evne til å gripe inn ved avvik (jamfør intervjufunn om sykefravær og siste-minutt-endringer) taler mot høyere automasjonsnivåer.

---

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| human operator | trafikkoordinator | Personen som tar de endelige beslutningene |
| automation / computer | Ressursplanlegger (algoritmemotor) | Systemet som genererer planforslag |
| decision and action selection | tildeling (dispatch) | Hvem gjør hva — kjerneoppgaven i Ressursplanlegger |
| information acquisition | innhenting av oppdragsdata, sjåførtilgjengelighet | Inputfasen før optimering |
| information analysis | constraint-evaluering, skåring | Algoritmens vurdering av feasibility og kvalitet |
| action implementation | godkjenning av plan + kommunikasjon til sjåfør | Koordinatorens avsluttende handling |
| "suggests one alternative" (level 4) | planforslag generert av algoritmen | Systemet produserer én plan, ikke et valg av mange |
| "executes if human approves" (level 5) | koordinatoren godkjenner planen — da aktiveres den | Nøyaktig Ressursplanleggers interaksjonsmodell |
| out-of-the-loop unfamiliarity | manglende oversikt over sjåfør/oppdragsstatus | Risikoen ved passiv godkjenning uten kritisk gjennomgang |
| complacency | blind tillit til planforslaget | Koordinator som slutter å sjekke avvik |
| skill degradation | forringelse av koordinatorens planleggingsintuisjon | Risiko ved langvarig avhengighet av algoritmegenererte planer |

### Begrensninger i applikasjon

- **Domene:** Alle eksempler er fra luftfart (ATC), romfart, prosesskontroll og medisin — domener med høyere umiddelbare sikkerhetskonsekvenser per beslutning. Transportplanlegging har lavere akutt risiko, men de strukturelle effektene (komplacens, ferdighetstap) er analoge.
- **Real-time vs. batch:** Kildens operatørmodell er primært sanntidsbeslutninger (en ATC-kontroller som reagerer på en konflikt). Ressursplanlegger er batch-basert — koordinatoren planlegger for morgendagen. Konsekvensen er at komplacensrisikoen er litt annerledes strukturert: risikoen materialiseres ved avvik som oppstår *i løpet av* en dag, ikke ved én feil beslutning under tidspress.
- **Nivåskalaens rekkevidde:** Table I gjelder teknisk sett for *decision and action selection* (kolonne 3). For Ressursplanleggers informasjonsinnhenting og -analyse er nivåene ubestemt — kilden erkjenner at antall nivåer varierer mellom de fire typene.
- **Ingen transportdomene-empiri:** Kilden har ingen data fra transportplanlegging. Applikasjonen er overføring av et analytisk rammeverk, ikke empirisk validering i vår kontekst.

---

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Automation | "the full or partial replacement of a function previously carried out by the human operator" | p. 288 / PDF 3 |
| Automation (broader) | "a device or system that accomplishes (partially or fully) a function that was previously, or conceivably could be, carried out (partially or fully) by a human operator" | p. 287 / PDF 2 |
| Levels of automation | "a continuum of levels, from the lowest level of fully manual performance to the highest level of full automation" | p. 287 / PDF 2 |
| Adaptive automation | "the level (and perhaps even the type) of automation could be designed to vary depending on situational demands during operational use" | p. 289 / PDF 4 |

---

## Rammeverk og modeller

### The Four-Stage Human Information Processing Model (Fig. 1, p. 287 / PDF 2)

| Komponent | Hva det er | Side |
|---|---|---|
| Sensory Processing | Perception of raw stimuli | p. 287 / PDF 2 |
| Perception / Working Memory | Conscious perception and manipulation of information | p. 287 / PDF 2 |
| Decision Making | Selection among decision alternatives | p. 287 / PDF 2 |
| Response Selection | Implementation of the chosen action | p. 287 / PDF 2 |

*Note for writer:* This model is the basis for the four types of automation — each stage can be automated at varying levels.

---

### Levels of Automation (LOA) for Decision and Action Selection — Table I (p. 287 / PDF 2)

| Nivå | Beskrivelse | Side |
|---|---|---|
| 10 | The computer decides everything, acts autonomously, ignoring the human | p. 287 / PDF 2 |
| 9 | informs the human only if it, the computer, decides to | p. 287 / PDF 2 |
| 8 | informs the human only if asked | p. 287 / PDF 2 |
| 7 | executes automatically, then necessarily informs the human | p. 287 / PDF 2 |
| 6 | allows the human a restricted time to veto before automatic execution | p. 287 / PDF 2 |
| 5 | executes that suggestion if the human approves | p. 287 / PDF 2 |
| 4 | suggests one alternative | p. 287 / PDF 2 |
| 3 | narrows the selection down to a few | p. 287 / PDF 2 |
| 2 | The computer offers a complete set of decision/action alternatives | p. 287 / PDF 2 |
| 1 | The computer offers no assistance: human must take all decisions and actions | p. 287 / PDF 2 |

---

### Automation Design Framework (Fig. 3, p. 290 / PDF 5)

Iterative prosess:

| Steg | Innhold |
|---|---|
| 1 | Identify types of automation (acquisition / analysis / decision / action) |
| 2 | Identify candidate levels per type |
| 3 | Apply primary evaluative criteria (human performance: workload, SA, complacency, skill) |
| 4 | Apply secondary evaluative criteria (reliability, cost of decision outcomes) |
| 5 | Iterate — adjust level based on criteria, repeat for all four types |

---

## Key arguments / lines of reasoning

### Argument: Appropriate LOA is bounded — it has both a lower and upper limit

- **Premiss:** Human performance can be degraded by automation that is either too low (excessive workload) or too high (complacency, out-of-the-loop unfamiliarity).
- **Konklusjon:** "Application of our framework would determine the lower and upper bounds of automation to be 4 and 6, respectively." (p. 290 / PDF 5, using the ATC example)
- **Sted:** p. 290 / PDF 5
- **Hvilke claims dette støtter:** Ch 2.2 ¶1 (positioning), Ch 5.2 ¶3

### Argument: High-level automation for high-risk decisions requires justification

- **Premiss:** High-cost decisions (anesthesiology, air defense) can justify higher LOA only if the human operator is NOT expected to intervene.
- **Konklusjon:** "if the human operator is ever expected under abnormal circumstances to take over control, then our analysis suggests that high levels of decision automation may not be suitable because of the documented human performance costs associated with such automation." (p. 292 / PDF 7)
- **Sted:** p. 292 / PDF 7
- **Hvilke claims dette støtter:** Ch 5.2 ¶3 (why Ressursplanlegger stays at level 5)

---

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| ATC conflict detection system | Level 4 automation — suggests resolution, pilot decides | p. 287 / PDF 2 |
| Auto GCAS (fighter aircraft) | Level 7 — automatically takes control if pilot doesn't | p. 289 / PDF 4 |
| Ground Proximity Warning System (GPWS) | Level 4 — single maneuver recommended, pilot can ignore | p. 289 / PDF 4 |
| FMS data uplink | Decision vs action automation interdependence — error trapping by keeping human in action stage | p. 293 / PDF 8 |

---

## Data og statistikk

Kilden presenterer ingen statistiske data eller kvantitative mål — den er et analytisk/konseptuelt bidrag.

---

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Human-centered automation | Design approach emphasising human roles; cited as guiding concept for the paper | p. 287 / PDF 2 |
| Function allocation | Assignment of tasks between human and machine — alternative to the LOA approach | p. 294 / PDF 9 |
| Adaptive automation | LOA varies dynamically with situational demands | p. 289 / PDF 4 |
| Clumsy automation | Automation that paradoxically increases workload (difficult to engage, extensive data entry) | p. 290 / PDF 5 |
| Mode confusion | Human performance problem associated with automation, beyond the four areas discussed | p. 291 / PDF 6 |

---

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "automation does not merely supplant but changes human activity and can impose new coordination demands on the human operator" | p. 286 / PDF 1 | Ch 2.2 ¶2 åpningssetning |
| "at a low level 2, several options are provided to the human, but the system has no further say in which decision is chosen. At level 4, the computer suggests one decision alternative, but the human retains authority for executing that alternative or choosing another one. At a higher level 6, the system gives the human only a limited time for a veto before carrying out the decision choice." | p. 287 / PDF 2 | Utdypende forklaring av nivå 2, 4, og 6 — brukes som prosatekst rundt Table I |
| "automation is not all or none, but can vary across a continuum of levels" | p. 287 / PDF 2 | Ch 2.2 ¶1 — innledning til skalakonseptet |
| "Automation must therefore be designed to ensure that such potential human performance costs do not occur." | p. 291 / PDF 6 | Ch 2.2 ¶5 (HITL som designbetingelse, ikke valg) |
| "The model can be used as a starting point for considering what types and levels of automation should be implemented in a particular system." | p. 294 / PDF 9 | Konklusjon — viser at modellen er et designverktøy, ikke en fasit |

---

## Hva kilden IKKE sier

- **"Human-in-the-loop"** som eksakt terminologi brukes **ikke** i kilden. Kilden bruker «human operator», «human interaction with automation», og «human-centered automation». Writer-agent skal ikke attribuere begrepet HITL verbatim til Parasuraman et al. — det er etablert terminologi i feltet, men denne kilden definerer det ikke slik.
- **Transport eller logistikk** nevnes ikke. Alle eksempler er fra luftfart (ATC, cockpit), prosesskontroll og medisin. Overføringen til vår kontekst er applikasjon, ikke direkte attribusjon.
- **Nivå 5 som «riktig» nivå** presiseres ikke som generell anbefaling. Kilden fremhever at det rette nivået avhenger av systemkontekst og evalueringskriterier — det er vår oppgave å begrunne at nivå 5 er passende for Ressursplanlegger.
- **Trust** som eget konsept er ikke kildas hovedbidrag — den nevner trust kun som en konsekvens av pålitelighet. `lee2004trust` er primærkilden for trust i automasjon; parasuraman2000automation skal ikke bære tyngden av trust-argumentet i Ch 2.2 ¶4.
- **Informasjonsinnhentings- og analysenivåene** er ikke spesifisert i Table I (som kun gjelder beslutning/handling). Kilden erkjenner at antall nivåer varierer mellom de fire typene.
- **Outline MUST CITE marker for Ch 2.2 ¶1** peker på `\textcite{parasuraman2000automation}` — **bekreftet**: kilden støtter HITL-definisjon og 10-nivå-skala fullt ut for dette ¶-et.

---

## Forfatter-perspektiv / metodologi

Konseptuelt-analytisk bidrag basert på litteraturgjennomgang og eksempler fra luftfart (ATC). Ingen egen empirisk studie — kilden syntetiserer eksisterende forskning om menneskelig ytelse i automatiserte systemer og bygger et rammeverk. Alle empiriske påstander er støttet av referanser (ref. [1]–[83]).