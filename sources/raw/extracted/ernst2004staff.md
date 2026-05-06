# Staff Scheduling and Rostering: A Review of Applications, Methods and Models (`ernst2004staff`)

## Status
- [x] Notes generated from raw on 2026-04-28
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The paper is a 25-page journal-length review article. Sections 1–5 (pp. 3–21) were read in full; pages 22–27 are bibliography. All areas of interest from the outline (Ch 2.1 ¶1–¶5 and Ch 2.2 ¶1, ¶4) were investigated. The taxonomy, hard/soft constraint distinction, decision-support / partial-automation framing, and the heuristics-vs-CP-vs-MP method comparison are all captured.
  - **Gaps not investigated:** The reference list (pp. 22–27) was not read line by line — citations to other works are not extracted. Section 3.4–3.10 (application areas outside transportation) was skim-read because it covers domains (call centres, health care, military, retail) that do not directly inform Ressursplanlegger's design.

## Source metadata
- **BibTeX key:** `ernst2004staff`
- **Reference (APA 7):** Ernst, A. T., Jiang, H., Krishnamoorthy, M., & Sier, D. (2004). Staff scheduling and rostering: A review of applications, methods and models. *European Journal of Operational Research, 153*(1), 3–27. https://doi.org/10.1016/S0377-2217(03)00095-X
- **Tilgang:** PDF (open / publisher)
- **Raw source:** `../ernst2004staff.pdf` (25 sider, journalartikkel)
- **Coverage in raw:** Hele substantielle innhold lest (pp. 3–21 / PDF 1–19): Section 1 Introduction, Section 2 Problem classification and models (taksonomi), Section 3 Application areas (transportasjon i detalj, øvrige skummet), Section 4 Solution methods (alle delseksjoner), Section 5 Future trends and conclusions. Referanselisten (pp. 22–27 / PDF 20–25) ikke lest i detalj. **PDF-side = printed side − 2** (PDF 1 = trykt s. 3) — alle sidehenvisninger nedenfor er trykte sidetall etterfulgt av PDF-side, f.eks. `(p. 3 / PDF 1)`.

## Sammendrag (2–3 setninger)
Ernst, Jiang, Krishnamoorthy og Sier presenterer en bred review av staff scheduling / personnel rostering — definert som prosessen med å konstruere arbeidsplaner som dekker en organisasjons etterspørsel. Artikkelen utvikler en seks-modul taksonomi (demand modelling, days off, shift, line of work, task assignment, staff assignment), gjennomgår anvendelsesområder (transport, helse, kundesentre, m.fl.), og sammenlikner løsningsmetoder (matematisk programmering, constraint programming, metaheuristikker, AI/decision support). Bidraget til denne oppgaven er (a) en kanonisk definisjon av personnel scheduling som kan plassere Ressursplanlegger innenfor staff scheduling-faget, (b) hard/soft constraint-distinksjonen, (c) en eksplisitt argumentasjon for at decision support / partiell automatisering reduserer "black box"-tillitsproblemet, og (d) sammenligningskriterier for CP, metaheuristikker og MP som direkte støtter multi-engine-arkitekturen.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.1 ¶1 (definere resource scheduling) | covered — gir en *staff scheduling*-spesifikk definisjon som komplementerer Pinedos generelle scheduling-definisjon |
| Ch 2.1 ¶2 (multi-resource scheduling) | partial — Ernst behandler bare staff-allokering (én ressurstype). Beslektet domene (crew + vehicle scheduling) er nevnt, men kombinert driver+kjøretøy-tildeling er ikke kildens fokus |
| Ch 2.1 ¶3 (hard og soft constraints) | covered — eksplisitt definisjon med penalty-formulering |
| Ch 2.1 ¶4 (NP-hardness, multi-engine motivasjon) | partial — Ernst sier ikke "NP-hard" eksplisitt for rostering, men beskriver problemene som "highly constrained and complex" og argumenterer empirisk for at heuristikker er metoden av valg ved "messy real world" rostering |
| Ch 2.1 ¶5 (solver-sammenligning: greedy / CP / metaheuristikker) | covered — eksplisitt sammenligning av CP-styrker, metaheuristikk-styrker og MP-svakheter, samt hybridtilnærminger |
| Ch 2.2 ¶1, ¶4 (HITL, trust) | covered — Ernst gir et direkte argument for at decision support / partiell automatisering adresserer "black box"-tillit; supplerer Parasuraman/Lee fra et OR-perspektiv |
| Ch 2.3 (TMS) | outside scope — Ernst diskuterer ikke transport management-systemer som programvarekategori |
| Ch 4.5 (algoritme) | partial — kan brukes som korroberende kilde for hybrid CP+heuristikk-tilnærminger og set covering-formuleringer dersom relevant; ikke primær |

## Claims this source supports

### Claim: "Personnel scheduling is the construction of work timetables that allocate staff to satisfy demand for goods or services"
- **Suggested for:** Ch 2.1 ¶1 (definisjon av resource scheduling, sekundær-/komplementærsitering ved siden av Pinedo)
- **Direkte sitat:**
  > "Personnel scheduling, or rostering, is the process of constructing work timetables for its staff so that an organisation can satisfy the demand for its goods or services. The first part of this process involves determining the number of staff, with particular skills, needed to meet the service demand. Individual staff members are allocated to shifts so as to meet the required staffing levels at different times, and duties are then assigned to individuals for each shift." (p. 3 / PDF 1)
- **Parafrase:** Personnel scheduling (synonym med rostering) er prosessen med å konstruere arbeidsplaner for staben slik at organisasjonens etterspørsel kan dekkes. Prosessen omfatter både å fastsette nødvendige bemanningsnivåer og å tildele konkrete personer (med rette ferdigheter) til arbeid på rett tidspunkt.
- **Forbehold:** Ernst behandler primært én ressurstype (staff). Vår oppgave tildeler både sjåfør og kjøretøy — kjøretøy som ressurstype faller utenfor Ernsts ramme.
- **Anvendelse på vårt case:** Ressursplanlegger er en staff scheduling-applikasjon i Ernsts forstand: trafikkoordinatoren konstruerer en arbeidsplan (rute) per sjåfør slik at oppdragsetterspørselen dekkes. Det utvider rammen til å også omfatte kjøretøy-tildeling — en multi-resource utvidelse av Ernsts single-resource definisjon.

### Claim: "Hard constraints must be satisfied; soft constraints may be violated and are typically modelled as penalty terms in the objective function"
- **Suggested for:** Ch 2.1 ¶3 (hard og soft constraints, sammen med Rossi 2006)
- **Direkte sitat:**
  > "Often there is a distinction between hard and soft constraints. The former *must* be satisfied, while the latter may be violated, though it is generally undesirable to do so. Modelling soft constraints usually involves the inclusion of penalty terms in the objective function." (p. 8 / PDF 6, §2.4)
- **Parafrase:** Ernst beskriver hard/soft-distinksjonen som en standard egenskap ved rostering-modeller: harde begrensninger må oppfylles for at en løsning skal være feasible, mens myke begrensninger uttrykkes som straffeterm i objektivfunksjonen og kan brytes mot en kostnad.
- **Forbehold:** Ingen — distinksjonen er presentert som etablert praksis innen rostering, ikke som forfatternes nyvinning. Kan også siteres for at konstruksjonen "vekt × brudd" mappes til straffeterm i objektivfunksjon.
- **Anvendelse på vårt case:** Ressursplanlegger bruker eksakt denne strukturen: harde constraints (førerkortklasse, tilgjengelighet, dobbeltbooking, kjøretøykrav) gjør planen ugyldig hvis brutt; myke constraints (workload-balanse, sjåførpreferanser) summeres som vektede straffeterm i scorefunksjonen. Ernst gir det rostering-spesifikke ankeret for denne modelleringen — Rossi gir det generelle CP-teoretiske ankeret.

### Claim: "Heuristics are the method of choice for messy real-world rostering with complex objectives and side constraints"
- **Suggested for:** Ch 2.1 ¶4 (NP-hardness motiverer heuristikk), Ch 2.1 ¶5 (solver-tradeoff)
- **Direkte sitat:**
  > "[Heuristics] tend to be relatively robust. While they cannot be guaranteed to produce an optimal solution, they can usually produce a reasonably good solution for a wide range of input data in a limited amount of running time. By comparison many integer programming approaches run the risk of not returning any feasible solutions for a long time." (p. 18 / PDF 16, §4.4)

  > "Hence heuristics are generally the method of choice for rostering software designed to deal with messy real world objectives and constraints that do not solve easily with a mathematical programming formulation. However they generally don't work very well if the rostering problem is highly constrained unless the constraints can be built directly into the heuristic … For more highly constrained problems CP approaches tend to work better." (p. 18 / PDF 16, §4.4)
- **Parafrase:** Heuristikker (greedy, simulated annealing, tabu search, GA) er robuste, gir gode-nok løsninger raskt, og er foretrukket når reelle rostering-problemer har komplekse mål og side-begrensninger som matematisk programmering ikke håndterer effektivt. CP er imidlertid bedre når problemet er svært constraint-tungt.
- **Forbehold:** Sitatet sier ikke "NP-hard" eksplisitt — den teoretiske NP-hardness-anker hentes fra Pinedo. Ernst gir den *empiriske* / *praktiske* begrunnelsen.
- **Anvendelse på vårt case:** Ressursplanleggers multi-engine-arkitektur (greedy + CP-SAT + Timefold) gjenspeiler nøyaktig Ernsts observasjon: greedy/Timefold (heuristikk) for de "messy" virkelige tildelingsproblemene; CP-SAT for instanser hvor begrensningene er hovedutfordringen. Ernst støtter dermed at *valget mellom* metodene er begrunnet i hvor "messy" vs. "highly constrained" instansen er — ikke i én generelt overlegen metode.

### Claim: "Decision-support / partial-automation rostering reduces the 'black box' trust problem of fully automated systems"
- **Suggested for:** Ch 2.2 ¶1 (HITL design pattern), Ch 2.2 ¶4 (trust og adopsjon)
- **Direkte sitat:**
  > "Several decision support systems have been developed to assist rostering staff in their task. For example [135] uses a neighbourhood search strategy to improve solutions with a user-selectable degree of automation that provides a range of options from fully manual rostering to complete automation." (p. 17 / PDF 15, §4.2)

  > "The decision support approach to rostering is particularly beneficial when there are a number of human factors that cannot be codified in software and need to be left to the discretion of the person in charge of rostering. In some cases these partial automation approaches also provide a useful first step from a completely manual system in organisations where the lack of trust into a 'black box' rostering engine is a significant issue." (p. 17 / PDF 15, §4.2)
- **Parafrase:** Beslutningstøttesystemer som tillater brukeren å velge automatiseringsgrad — fra full manuell til full automatisk — er særlig nyttige (a) når menneskelige faktorer ikke kan kodifiseres i programvaren, og (b) som overgangstrinn i organisasjoner som ikke stoler på et fullt automatisert "black box"-system.
- **Forbehold:** Dette er ikke Ernsts egen empiriske studie — det er en *bemerkning* om en designtilnærming i feltet. Som korroberende kilde for HITL-argumentet er det likevel verdifullt fordi det gir en rostering-spesifikk artikulering av "trust"-utfordringen som komplementerer Lee & See sin generelle automation-trust litteratur.
- **Anvendelse på vårt case:** Trafikkoordinatorenes taus kunnskap om sjåførers preferanser, kunderelasjoner og rutekjennskap er præsis det Ernst kaller "human factors that cannot be codified in software". Ressursplanleggers HITL-design (algoritmen genererer forslag, koordinatoren overstyrer) implementerer "user-selectable degree of automation" og adresserer dermed eksplisitt det Ernst identifiserer som adopsjonsbarrieren i SMEs uten erfaring med automatisert rostering.

### Claim: "Six-module taxonomy of the rostering process: demand modelling, days off, shift, line of work, task assignment, staff assignment"
- **Suggested for:** Ch 2.1 ¶1 eller ¶2 (klassifisering av problemet — kan brukes til å posisjonere Ressursplanlegger som primært et task assignment + staff assignment-problem på task-based demand)
- **Direkte sitat:**
  > "Module 5: Task assignment. It may be necessary to assign one or more tasks to be carried out during each shift. These tasks may require particular staff skills or levels of seniority and must therefore be associated with particular lines of work." (p. 6 / PDF 4)

  > "Module 6: Staff assignment. This module involves the assignment of individual staff to the lines of work. Staff assignment is often done during construction of the work lines." (p. 6 / PDF 4)

  > "*Task based demand.* In this case demand is obtained from lists of individual tasks to be performed. Tasks are usually defined in terms of a starting time and duration, or a time window within which the task must be completed, and the skills required to perform the task. In some cases tasks may be associated with locations." (p. 5 / PDF 3)
- **Parafrase:** Ernsts taksonomi deler rostering i seks moduler. Vårt problem faller primært under Modul 5 (task assignment) og Modul 6 (staff assignment), drevet av task-based demand der hvert oppdrag har starttid, varighet, tidsvindu, kompetansekrav og lokasjon.
- **Forbehold:** Ernst forutsetter at "tasks" tildeles innenfor allerede konstruerte "lines of work" (skift/dager). Vår modell konstruerer ruta direkte fra sett av oppdrag for én dag — vi gjør ikke days-off, shift eller line-of-work-konstruksjon (Moduler 2–4 er utenfor vårt scope).
- **Anvendelse på vårt case:** Posisjonering: Ressursplanlegger er ikke et generelt rostering-system. Det er spesifikt en task assignment + staff assignment-løser på task-based demand med fast tids- og lokasjonsstruktur. Dette plasserer oss eksakt — gir oss en faglig plassering som er smalere enn "scheduling" generelt og ekskluderer vagt-relaterte problemer som nurse rostering eller flight crew pairing.

### Claim: "Future rostering systems will require integrated frameworks combining CP, heuristic search, integer programming and simulation"
- **Suggested for:** Ch 2.1 ¶5 (multi-engine speed-quality tradeoff), Ch 4.5 ¶2 (begrunnelse for multi-engine valg)
- **Direkte sitat:**
  > "we will see a more integrated approach to roster solution developments. For example, it will be necessary to consider integrated solution frameworks that include CP, heuristic search, integer programming and simulation approaches to solve a multitude of subproblems within the context of solving the complex rostering problems of the future." (p. 21 / PDF 19, §5)
- **Parafrase:** Ernst spår eksplisitt at framtidige rostering-løsninger vil kreve integrerte rammeverk som kombinerer flere metodeklasser (CP, heuristikker, IP, simulering) snarere enn å satse på én enkelt metode.
- **Forbehold:** Dette er en framtidstrend-spådom, ikke et empirisk funn. Bør siteres som "Ernst et al. anticipated …" snarere enn som etablert resultat.
- **Anvendelse på vårt case:** Ressursplanleggers multi-engine-arkitektur (greedy + CP-SAT + Timefold) er en konkret realisering av nettopp den integrerte tilnærmingen Ernst forutser. Sitering støtter den arkitektoniske begrunnelsen.

## Application to our domain

Hver kilde er skrevet om et annet domene enn vårt. Dette seksjonen bygger broen.

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| personnel scheduling / rostering | sjåfør- og kjøretøytildeling for trafikkoordinatorer | Ernst bruker termene synonymt; vi spesifiserer at det også omfatter kjøretøy |
| staff / employee | sjåfør | direkte oversettelse |
| task | oppdrag | direkte; Ernsts definisjon (starttid, varighet, tidsvindu, kompetansekrav, evt. lokasjon) matcher våre oppdrag eksakt |
| skill / qualification | førerkortklasse + kompetanse (ADR, kran, etc.) | bredere kategori i kilden; spesifikt definert i vår domene |
| line of work / work line | rute (én sjåførs arbeidsdag) | Ernsts definisjon spenner ofte uker/måneder; vår rute er én dag |
| shift | (ikke direkte ekvivalent) | Ressursplanlegger arbeider ikke med skift som rosteringsenhet — vi tildeler oppdrag direkte |
| demand | sett av oppdrag for planleggingsdagen | Ernst skiller task-based / shift-based / flexible demand; vårt problem er rent task-based |
| Module 5 (task assignment) + Module 6 (staff assignment) | algoritmens kjerneoppgave: tildel sjåfør+kjøretøy til oppdrag | Ernsts taksonomi plasserer oss her |
| decision support tool / rostering tool | Ressursplanlegger | Ernst bruker disse termene synonymt for samme klasse system |
| black box rostering engine | fullt automatisert plansystem uten menneskelig override | Ernst bruker eksplisitt frasen i tillit-kontekst |
| user-selectable degree of automation | algoritmens forslag som koordinatoren overstyrer | direkte mapping til Ressursplanleggers HITL-modell |

### Begrensninger i applikasjon

Ting i kildens kontekst som gjør at den IKKE er direkte overførbar til vårt case:

- **Single-resource fokus.** Ernst behandler tildeling av staff til oppgaver. Ressursplanlegger tildeler både sjåfør *og* kjøretøy. Dette gjør vårt problem multi-resource — strengt vanskeligere enn Ernsts ramme. Sitering må derfor anvendes med en eksplisitt utvidelse, ikke som direkte mapping.
- **Multi-day rostering vs. én-dags planlegging.** Ernsts arbeid er primært om rosters som spenner uker/måneder (cyclic rosters, lines of work, days-off scheduling). Ressursplanlegger genererer dagsplaner. Modulene 2 (days off), 3 (shift), 4 (line of work) er ikke vårt scope. Bare Modul 1 (demand modelling, trivielt for oss siden oppdrag kommer fra ordresystem), Modul 5 (task assignment) og Modul 6 (staff assignment) er relevante.
- **Crew rostering ≠ vårt problem.** Section 3.1 (Transportation systems) handler om airline / bus / rail crew — der "tasks" er flyturer eller bussrunder med både temporale OG spatiale features, og crew må returnere til hjembase. Ressursplanleggers oppdrag har faste lokasjoner og tider; sjåføren returnerer ikke nødvendigvis til base, og det er ingen "pairing"-problem. Crew rostering-eksempler bør ikke siteres som direkte parallel.
- **Fra 2004 — pre-moderne open-source CP-SAT.** Ernsts CP-diskusjon (§4.3) er teoretisk og forutdaterer Google OR-Tools (2010) og moderne lazy-clause SAT-solvere. Når vi siterer Ernst for at "CP-tilnærminger fungerer bedre på sterkt constraint-tunge problemer", anvendes det på en moderne implementasjon (CP-SAT) som har betydelig forbedrede egenskaper sammenlignet med 2004-tidens tilstand.
- **Workforce optimisation / cost-minimering vs. assignment-kvalitet.** Ernsts dominerende objektiv er kostnadsminimering (set covering, lønnskostnader). Vårt primære objektiv er dekning av oppdrag og myke kvalitetsmål (workload-balanse, preferanser) — ikke arbeidskostnad. Mappes ikke 1-til-1.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Personnel scheduling / rostering | "Personnel scheduling, or rostering, is the process of constructing work timetables for its staff so that an organisation can satisfy the demand for its goods or services." | p. 3 / PDF 1 |
| Hard constraints | "[constraints that] *must* be satisfied" | p. 8 / PDF 6 |
| Soft constraints | "[constraints that] may be violated, though it is generally undesirable to do so. Modelling soft constraints usually involves the inclusion of penalty terms in the objective function." | p. 8 / PDF 6 |
| Task based demand | "demand is obtained from lists of individual tasks to be performed. Tasks are usually defined in terms of a starting time and duration, or a time window within which the task must be completed, and the skills required to perform the task. In some cases tasks may be associated with locations." | p. 5 / PDF 3 |
| Demand modelling | "the process of translating some predicted pattern of incidents into associated duties and then using the duty requirements to ascertain a demand for staff" | p. 5 / PDF 3 |
| Metaheuristics | "Metaheuristics form an important class of methods that solve hard, and usually, combinatorial/discrete optimisation problems. Typically, these methods are used to solve problems that cannot be solved by traditional heuristics such as steepest descent or greedy local search." | p. 17 / PDF 15 |

## Rammeverk og modeller

### Six-module taxonomy of the rostering process (pp. 5–6 / PDF 3–4, §2.1)

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| Module 1: Demand modelling | Bestemme hvor mange ansatte som trengs på ulike tidspunkter — basert på task / flexible / shift-based demand | "for example, six morning shifts may be needed to cover the demand between 6 am and 2 pm" | p. 5 / PDF 3 |
| Module 2: Days off scheduling | Bestemme hvilke hviledager som skal interpolere mellom arbeidsdager | (ingen konkret) | p. 6 / PDF 4 |
| Module 3: Shift scheduling | Velg gode skift-kombinasjoner og antall ansatte per skift | nurse scheduling, ambulanse | p. 6 / PDF 4 |
| Module 4: Line of work construction | Konstruer en sekvens av plikter / skift over en periode for hver ansatt (cyclic / acyclic / stint-based) | tour scheduling, crew rostering | p. 6 / PDF 4 |
| Module 5: Task assignment | Tildel én eller flere oppgaver til hvert skift, gitt nødvendige skills/seniority | (generell) | p. 6 / PDF 4 |
| Module 6: Staff assignment | Tildel individuelle ansatte til lines of work | (generell) | p. 6 / PDF 4 |

### Three demand types (p. 5 / PDF 3, §2.1)

| Type | Definisjon (verbatim) | Anvendelse på vårt case |
|---|---|---|
| Task based | "demand is obtained from lists of individual tasks to be performed. Tasks are usually defined in terms of a starting time and duration, or a time window within which the task must be completed, and the skills required to perform the task." | Direkte vår modell: oppdrag = task, med starttid/varighet/tidsvindu/kompetansekrav |
| Flexible | "the likelihood of future incidents is less well known and must be modelled using forecasting techniques. Requests for service may have random arrival rates and possibly random service times." | Ikke vårt case — vi har et kjent oppdragssett ved planleggingsstart |
| Shift based | "the demand is obtained directly from a specification of the number of staff that are required to be on duty during different shifts." | Ikke vårt case |

### Solution method comparison (§4.2–§4.5, pp. 16–20 / PDF 14–18)

| Metode | Styrke | Svakhet | Side |
|---|---|---|---|
| Constraint Programming (CP) | "particularly useful when the problem is highly constrained and/or when any feasible solution will suffice even if it is not optimal" | "less likely to produce good solutions for problems where the main challenge is to find an optimal or near optimal solution out of a vast number of feasible solutions" | p. 17 / PDF 15 |
| Metaheuristics (SA, TS, GA) | "relatively robust", produserer "reasonably good solution for a wide range of input data in a limited amount of running time", "easy to deal with complex objectives" | "don't work very well if the rostering problem is highly constrained" | p. 18 / PDF 16 |
| Mathematical programming (set covering, B&B, column generation) | lavest kostnad / optimal når den lykkes; modnest teori | "limiting in what constraints and objectives can be expressed", "difficult and time consuming" å implementere | pp. 18–19 / PDF 16–17 |
| Hybrid (CP + IP, CP + heuristikk) | kombinerer fleksibilitet i CP med optimaliseringskraft i IP / hastighet i heuristikk | "more research is required to determine the best way to combine" | p. 17 / PDF 15 |

## Key arguments / lines of reasoning

### Argument: Heuristikker er foretrukket for "messy real world" rostering, men CP er bedre for sterkt constraint-tunge problem
- **Premiss(er):** (1) Reelle rostering-problem har komplekse mål og uregelmessige side-begrensninger som er vanskelig å uttrykke i MP. (2) Heuristikker er robuste og produserer rimelige løsninger raskt. (3) Heuristikker bryter sammen når problemet er svært constraint-tungt med mindre constraints kan bygges direkte inn i nabolagsoperatoren. (4) CP håndterer constraint-tunge problem bedre.
- **Konklusjon:** Valg av metode er ikke "én er best" — det avhenger av om instansen er messy-objektiv-dominert eller constraint-dominert.
- **Sted:** §4.4 (p. 18 / PDF 16); §4.3 (p. 17 / PDF 15)
- **Hvilke claims dette støtter:** Ch 2.1 ¶4–¶5 (multi-engine speed-quality tradeoff og NP-hardness-respons)

### Argument: Decision support / partial automation løser tillitsproblemet med fullt automatiserte rostering-systemer
- **Premiss(er):** (1) En del menneskelige faktorer (preferanser, kontekstkunnskap) kan ikke kodifiseres i programvare. (2) Organisasjoner uten erfaring med automatisert rostering har lav tillit til "black box"-systemer. (3) Bruker-konfigurerbar automatiseringsgrad gir en glidende overgang fra manuell til automatisk.
- **Konklusjon:** Decision support-tilnærmingen er særlig nyttig som adopsjonsbro, ikke bare som permanent design.
- **Sted:** §4.2 (p. 17 / PDF 15)
- **Hvilke claims dette støtter:** Ch 2.2 ¶1, ¶4 (HITL design og trust/adopsjon)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Airline crew scheduling med tre-stegs decomposition (pairing generation → pairing optimisation → crew rostering) | Standardrammeverk for komplekst rostering; viser hvordan stor probleminstans dekomponeres | p. 10 / PDF 8 |
| Police shift scheduling med tabu-restriksjoner og lokal søk | Bruk av metaheuristikk på sterkt regulert (4 days/10 timer, 5 days/8 timer) skiftproblem | p. 13 / PDF 11 |
| Engineer scheduling [21] — oppgaver med starttid, varighet, lokasjon; objektiv: maksimere fullført arbeid og minimere reisetid | Tett analog til vårt problem (task-based demand med lokasjon) | p. 15 / PDF 13, §3.9 |
| Postal delivery / nurse scheduling / call centre | Variasjonsbredden i applikasjonsområder | pp. 11–14 / PDF 9–12 |

## Data og statistikk

Ikke aktuelt — review-artikkel uten egen empirisk data.

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Crew pairing generation / optimisation | To av tre faser i airline crew rostering — kombinerer flyturer til tildelbare "pairings" | p. 10 / PDF 8 |
| Set covering formulation | Dominerende MP-formulering for rostering: "Many problems in staff scheduling and rostering can be described in this unified format" — kolonner = mulige duties, hver oppgave/kunde må dekkes minst én gang | p. 19 / PDF 17 |
| Column generation | Teknikk for å håndtere svært store set covering-formuleringer ved iterativ generering av lovende kolonner | p. 19 / PDF 17 |
| Stint | Forhåndsdefinert sekvens av skift og hviledager (f.eks. DDNN, OOO) | p. 8 / PDF 6 |
| Cyclic vs acyclic rosters | Cyclic: alle ansatte i en klasse går gjennom samme rotasjon. Acyclic: individuelle planer | p. 8 / PDF 6 |
| Tour scheduling | Konstruksjon av lines of work for fleksibel demand | p. 6 / PDF 4 |
| Set covering (eksplisitt om generalitet) | "The set covering/partitioning model is so general that many problems in staff scheduling and rostering can be described in this unified format. Days-off, shift, tour scheduling [32], crew scheduling [17] and crew rostering [66,94] are such examples." | p. 19 / PDF 17 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "It is extremely difficult to find good solutions to these highly constrained and complex problems and even more difficult to determine optimal solutions that minimise costs, meet employee preferences, distribute shifts equitably among employees and satisfy all the workplace constraints." | p. 3 / PDF 1 | Ch 2.1 ¶1 eller ¶4 — autoritativ formulering av problemets vanskelighetsgrad |
| "In many organisations, the people involved in developing rosters need decision support tools to help provide the right employees at the right time and at the right cost while achieving a high level of employee job satisfaction." | p. 3 / PDF 1 | Ch 2.1 ¶1 eller Ch 2.2 — motivasjon for DSS |
| "It is usually not computationally practical to deal simultaneously with all the modules required to generate a roster, though such an approach is desirable from the perspective of creating the best overall rosters. Decomposing the problem into several separate modules makes it more tractable …" | p. 7 / PDF 5 | Ch 2.1 — beslutning om problemdekomposisjon |
| "[CP is] less likely to produce good solutions for problems where the main challenge is to find an optimal or near optimal solution out of a vast number of feasible solutions." | p. 17 / PDF 15 | Ch 2.1 ¶5 — begrensning ved CP, motiverer metaheuristikk |
| "In some cases these partial automation approaches also provide a useful first step from a completely manual system in organisations where the lack of trust into a 'black box' rostering engine is a significant issue." | p. 17 / PDF 15 | Ch 2.2 ¶4 — adopsjonsbarriere og trust |
| "we will see a more integrated approach to roster solution developments. For example, it will be necessary to consider integrated solution frameworks that include CP, heuristic search, integer programming and simulation approaches …" | p. 21 / PDF 19 | Ch 2.1 ¶5 eller Ch 4.5 ¶2 — multi-engine fremtidsspådom |

## Hva kilden IKKE sier

- **NP-hardness for rostering er ikke formelt etablert hos Ernst.** Forfatterne kaller problemene "highly constrained and complex" (p. 3) og argumenterer empirisk for at exact methods er upraktiske, men gir ingen formell kompleksitetsanalyse. NP-hardness-anker hentes fra Pinedo, ikke Ernst.
- **Multi-resource (driver+vehicle) tildeling er ikke kildens fokus.** Ernsts ramme er staff-allokering. Ressursplanlegger utvider problemet til to ressurstyper — kilden gir foundational støtte, men ikke direkte modell for det multi-resource tilfellet.
- **Vehicle Routing Problem (VRP) er ikke dekket her.** Ernst nevner "vehicle scheduling" sammen med crew scheduling, men VRP-formuleringen (Dantzig-Ramser) er utenfor reviewets scope. (VRP er kun en kort avgrensningsreferanse i denne avhandlingen — ikke en kjerneteori — og dekkes av `braekers2016vrp` i 2.1 ¶4.)
- **Spesifikke algoritmer (CP-SAT, Timefold) er ikke nevnt.** Ernst er fra 2004 og refererer til "constraint programming" og "metaheuristikker" på generisk nivå. Bruk Perron/OR-Tools-kilder og Timefold-dokumentasjon for spesifikke implementasjonshenvisninger.
- **Norsk transportsektor / SME-kontekst er ikke nevnt.** Reviewets transportkapittel handler nesten utelukkende om internasjonal flyselskap-, jernbane- og masstransitkrev-rostering. Skala (Hong Kong telefon, AT&T, m.v.) er typisk større enn norske transportbedrifter med 8–45 kjøretøy.
- **Outline `MUST CITE`-markører (sjekk):** outline.md har ingen eksplisitt `MUST CITE: \textcite{ernst2004staff}`-markør for denne kilden i 2.1 eller 2.2 (per dagens outline). Den er foreslått som *komplementær / korroberende* sekundærkilde til Pinedo (2.1 ¶1, ¶4, ¶5) og til Parasuraman/Lee (2.2 ¶1, ¶4). Hvis writer-agent ønsker en ekstra referanse fra rostering-domenet (i tillegg til Pinedos machine-scheduling-domene), er Ernst en velvalgt — særlig for hard/soft constraints (2.1 ¶3) og for trust/black-box-argumentet (2.2 ¶4).

## Forfatter-perspektiv / metodologi

Operations Research-perspektiv. Forfatterne er fra CSIRO Mathematical and Information Sciences (Australia) og skriver innen OR-tradisjonen. Reviewet er litteraturbasert (ingen egen empiri), strukturerer feltet via en taksonomi de selv foreslår, og favoriserer matematisk-programmerings- og metaheuristisk metode-perspektiv. Tydelig at de IKKE ser AI/CP som hovedstrøm: "It should be noted that the literature is heavily skewed towards mathematical programming and metaheuristic approaches for rostering as opposed to CP and other techniques arising out of artificial intelligence research." (p. 15 / PDF 13). Posisjonsmessig er artikkelen *autoritativt* sitert som standard-review for staff scheduling og bør brukes som overordnet kontekstkilde, ikke som teknisk implementasjonsreferanse.