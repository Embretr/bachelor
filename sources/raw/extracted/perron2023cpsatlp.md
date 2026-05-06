# The CP-SAT-LP Solver (`perron2023cpsatlp`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The source is a 2-page invited-talk abstract (CP 2023, pp. 3:1–3:2). Every paragraph has been deep-read and every claim relevant to the thesis areas of interest is captured. There are no further pages to investigate.
  - **Gaps not investigated:** None — the source has no further content beyond the references list.

## Source metadata
- **BibTeX key:** `perron2023cpsatlp`
- **Reference (APA 7):** Perron, L., Didier, F., & Gay, S. (2023). The CP-SAT-LP solver (Invited talk). In R. H. C. Yap (Ed.), *29th International Conference on Principles and Practice of Constraint Programming (CP 2023)* (Vol. 280, pp. 3:1–3:2). Schloss Dagstuhl – Leibniz-Zentrum für Informatik. https://doi.org/10.4230/LIPIcs.CP.2023.3
- **Tilgang:** open (LIPIcs, CC-BY 4.0)
- **Raw source:** `../perron2023cpsatlp.pdf`
- **Coverage in raw:** Hele dokumentet (2 sider, p. 3:1–3:2 = PDF s. 1–2). Side 1 = abstract og hovedtekst; side 2 = referanseliste.
- **Page-mapping note:** Trykt sidetall følger LIPIcs-konvensjonen "3:1" og "3:2" (artikkel 3, side 1 og 2). PDF-side 1 = trykt side 3:1; PDF-side 2 = trykt side 3:2.

## Sammendrag (2–3 setninger)

Forfatterne (Googles Operations Research-team) presenterer CP-SAT-LP som en moderne constraint programming-løser bygget på en SAT-løser med Lazy Clause Generation, kombinert med en simplex (LP-relaksasjon) og en portefølje av parallelle arbeider-tråder. De argumenterer for at denne kombinasjonen gir state-of-the-art ytelse i CP-fellesskapet, gjennombruddsresultater på skedulerings-benchmarks, og konkurransedyktige resultater mot de beste MIP-løserne på rent integrale problemer. Bidraget til vår tese er at det utgjør den autoritative beskrivelsen av selve CP-SAT-løseren som Ressursplanlegger bruker via OR-Tools.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 4.5 ¶2 (Chosen approach and justification — algorithm) | covered (primær treff — MUST CITE bekreftet) |
| Ch 2.1 ¶4 (NP-hardness, multi-engine approach) | partial (kilden bekrefter at CP-SAT løser tunge skedulerings-instanser, men diskuterer ikke NP-hardhet i seg selv) |
| Ch 2.1 ¶5 (Solver comparison — CP-SAT som complete solver) | covered (kilden gir den autoritative beskrivelsen av hva CP-SAT-LP er og hvordan den fungerer arkitektonisk) |

## Claims this source supports

### Claim: CP-SAT-LP er en state-of-the-art constraint programming-løser med uovertruffet ytelse i CP-miljøet og gjennombruddsresultater på skedulerings-benchmarks
- **Suggested for:** Ch 4.5 ¶2 (primær — begrunnelse for valg av OR-Tools/CP-SAT); sekundært Ch 2.1 ¶5 (CP-SAT som complete solver).
- **Direkte sitat:** "All in all, CP-SAT-LP is a state-of-the-art solver, with unsurpassed performance in the Constraint Programming community, breakthrough results on Scheduling benchmarks (with the closure of many open problems), and competitive results with the best MIP solvers (on purely integral problems)." (p. 3:1)
- **Parafrase:** CP-SAT-LP regnes i 2023 som blant de fremste CP-løserne, med dokumenterte gjennombrudd på skedulerings-problemer og konkurransedyktig ytelse mot ledende MIP-løsere.
- **Forbehold:** Påstanden er forfatternes egen vurdering i en *invited talk* fra Google-teamet selv; den er ikke en uavhengig benchmark-studie. Bør anvendes som teknologivalgs-begrunnelse, ikke som "bevis" for absolutt overlegenhet.
- **Anvendelse på vårt case:** Begrunner i Ch 4.5 ¶2 hvorfor Ressursplanlegger valgte CP-SAT som mellom-engine på speed-quality-aksen — en aktivt utviklet løser med dokumentert ytelse på skedulerings-problemer (vår problemklasse) er et rasjonelt valg for instanser opp til ~500 oppdrag.

### Claim: CP-SAT-LP er en del av OR-Tools open-source optimization suite, utviklet av Googles Operations Research-team
- **Suggested for:** Ch 4.5 ¶2 (sammen med `googleortools2026cpsat`); evt. Ch 2.1 ¶5.
- **Direkte sitat:** "The CP-SAT-LP solver is developed by the Operations Research team at Google and is part of the OR-Tools [8] open-source optimization suite." (p. 3:1)
- **Parafrase:** CP-SAT-LP er Google OR-Tools' CP-løser, utviklet og vedlikeholdt av Googles OR-team.
- **Forbehold:** Ingen — dette er en faktisk redegjørelse for proveniens.
- **Anvendelse på vårt case:** Etablerer at CP-SAT-engine i Ressursplanlegger har institusjonell støtte (Google OR-team) og open-source-status — relevant for vurderingen av langsiktig vedlikeholdbarhet og lisensvalg når writer-agent forklarer teknologivalg i Ch 4.5.

### Claim: CP-SAT-LP er en rent integral constraint programming-løser bygget på en SAT-løser med Lazy Clause Generation
- **Suggested for:** Ch 2.1 ¶5 (definisjon av CP-SAT som complete solver); Ch 4.5 ¶2 (teknologivalgs-beskrivelse).
- **Direkte sitat:** "It is an implementation of a purely integral Constraint Programming solver on top of a SAT solver using Lazy Clause Generation [11]." (p. 3:1)
- **Parafrase:** Arkitektonisk: CP-laget genererer SAT-klausuler "lazily" basert på constraint-propagering, og en SAT-engine søker i klausul-databasen.
- **Forbehold:** "Purely integral" betyr at variabler er heltall — løseren håndterer ikke kontinuerlige variabler direkte. Vår modell er heltalls-basert (oppdrag/sjåfør/kjøretøy-tildelinger), så denne begrensningen er ikke bindende for oss.
- **Anvendelse på vårt case:** Underbygger at Ressursplanlegger sin tildelingsmodell (binære tilordningsvariabler med harde og myke beskrankninger) ligger innenfor CP-SAT-LPs intenderte problemklasse — en bekreftelse på at modelleringsvalget (CP-SAT framfor f.eks. en MIP-løser) passer modelltypen.

### Claim: CP-SAT-LP forbedrer chuffed-løseren på to akser: integrasjon av simplex (LP-relaksasjon) og portefølje av diverse parallelle arbeider-tråder
- **Suggested for:** Ch 4.5 ¶2 (teknisk substans for hvorfor CP-SAT-LP er konkurransedyktig).
- **Direkte sitat:** "The CP-SAT-LP solver improves upon the chuffed solver [4] in two main directions. First, it uses a simplex alongside the SAT engine. Second, it implements and relies upon a portfolio of diverse workers for its search part." (p. 3:1)
- **Parafrase:** To arkitektoniske grep skiller CP-SAT-LP fra forløperen chuffed: en LP-simplex som brukes for lineære relaksasjoner ved siden av SAT-motoren, og en portefølje-strategi der flere ulike søke-arbeidere kjøres parallelt.
- **Forbehold:** Detaljnivået er kort; for full forståelse av portefølje-strategien må man konsultere referanse [11] (Stuckey 2010) eller andre OR-Tools-publikasjoner.
- **Anvendelse på vårt case:** Forklarer hvorfor CP-SAT-LP gir nyttige resultater også når Ressursplanlegger setter en kort tids-grense (f.eks. 30 sekunder): porteføljen sikrer at flere søkestrategier prøves parallelt, og simplexen gir tighter dual bounds — så løseren returnerer ofte god kvalitet også uten å bevise optimalitet.

### Claim: Simplex-integrasjonen muliggjør innlemmelse av MIP-teknologi (presolve, dual reductions, branching, cuts, reduced cost fixing) i CP-SAT-LP
- **Suggested for:** Ch 4.5 ¶2 (teknisk substans, valgfri); Ch 2.1 ¶5 (CP-SAT som hybrid CP/SAT/MIP).
- **Direkte sitat:** "It also started the integration of MIP technology into CP-SAT-LP. This is a huge endeavour, as MIP solvers are mature and complex. It includes presolve – which was already a part of CP-SAT –, dual reductions, specific branching rules, cuts, reduced cost fixing, and more advanced techniques." (p. 3:1)
- **Parafrase:** Simplex-laget åpner for at klassiske MIP-teknikker (presolve, cuts, reduced cost fixing, etc.) kan brukes inne i CP-løseren.
- **Forbehold:** Ikke alle MIP-teknikker er fullt integrert (kilden beskriver det som et pågående "huge endeavour"). Den oppgir ikke målbar effekt på spesifikke benchmark-instans-størrelser.
- **Anvendelse på vårt case:** Bruk kun hvis writer-agent trenger å forklare hvorfor CP-SAT-LP er konkurransedyktig mot MIP-løsere — relevant hvis Ch 4.5 ¶2 nevner alternativer som Gurobi/CBC. Trolig overflødig substans for vår tese; primær-claimet "state-of-the-art" dekker behovet.

### Claim: CP-SAT-LP har muliggjort gjennombrudd på Job-Shop-problemer og Resource-Constrained Project Scheduling Problems
- **Suggested for:** Ch 2.1 ¶4 (NP-hardness, motivasjon for heuristikk); Ch 4.5 ¶2 (begrunnelse for valg).
- **Direkte sitat:** "This has enabled breakthroughs in solving and proving hard scheduling instances of the Job-Shop problems [5] and Resource Constraint Project Scheduling Problems [6, 2]." (p. 3:1)
- **Parafrase:** Konkrete benchmark-gjennombrudd er rapportert på to klassiske harde skedulerings-problemklasser (Job-Shop og RCPSP).
- **Forbehold:** Ressursplanlegger sitt problem er ikke Job-Shop og ikke klassisk RCPSP — det er multi-resource assignment med faste tidsvinduer. Påstanden viser at CP-SAT-LP håndterer relaterte tunge skedulerings-problemer godt, men er ikke direkte bevis for ytelse på vårt spesifikke problem.
- **Anvendelse på vårt case:** Brukes i Ch 2.1 ¶4 / Ch 4.5 ¶2 som *indirekte* støtte: siden vårt problem er strukturelt slektning av RCPSP (begge har ressurser med kapasitet og oppgaver med tidsvinduer), sannsynliggjør dokumenterte gjennombrudd på RCPSP at CP-SAT-LP er en fornuftig motor også for vår variant.

### Claim: Portefølje-arkitekturen kategoriserer arbeidere langs flere akser — finne primale løsninger (komplette løsere, lokal søk, Large Neighborhood Search), forbedre duale grenser, og redusere problemet via continuous probing
- **Suggested for:** Ch 4.5 ¶2 (valgfri teknisk dybde, sannsynligvis utelatt i den endelige teksten på grunn av sidebudsjett); evt. Ch 2.1 ¶5.
- **Direkte sitat:** "These workers can be categorized along multiple criteria like finding primal solutions – either using complete solvers, Local Search [7] or Large Neighborhood Search [10] –, improving dual bounds, trying to reduce the problem with the help of continuous probing." (p. 3:1)
- **Parafrase:** Porteføljen blander komplette søk, lokal-søk-heuristikker og dual-grense-forbedringer i parallelle arbeidere som deler informasjon underveis.
- **Forbehold:** Detaljnivå — ikke nødvendig substans for en bachelor-tese' Ch 4.5; bør utelates med mindre writer trenger å forklare *hvorfor* CP-SAT gir gode anytime-løsninger.
- **Anvendelse på vårt case:** Forklarer hvordan CP-SAT-LP kan returnere brukbare løsninger raskt selv på store instanser — relevant hvis Ressursplanleggers benchmark-resultater viser sub-optimal-men-god kvalitet under tidsgrense, og writer trenger å forklare mekanismen.

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| solver | løser / motor / engine | Brukt om CP-SAT-LP som programvarekomponent. I vår tekst: "CP-SAT-løser" eller "CP-SAT-motor". |
| purely integral CP solver | rent heltalls CP-løser | Vår tilordnings-modell er heltallig — variabler er binære (assigned/not assigned) eller heltalls-indekser. |
| (job-shop / RCPSP) hard scheduling instances | tunge skedulerings-instanser | Vårt problem er strukturelt beslektet (multi-ressurs skedulering med kapasitets- og kompetansebeskrankninger) men ikke identisk. |
| portfolio of diverse workers | parallell søke-strategi-portefølje | Forklarer hvorfor CP-SAT gir gode anytime-løsninger på vår tids-grense (f.eks. 30 s). |
| primal solutions | gyldige (feasible) tildelingsplaner | I vårt domene: konkrete løsninger der alle harde beskrankninger er tilfredsstilt. |
| dual bounds | optimalitets-grenser | Brukes ikke direkte i Ressursplanleggers UI, men ligger til grunn for "near-optimal within time limit"-egenskapen vi siterer. |
| Job-Shop / RCPSP | analoge skedulerings-problemklasser | Vår problemklasse er ikke disse, men har samme NP-harde struktur. Bruk kun analogisk. |

### Begrensninger i applikasjon

- Kilden er en **invited talk-abstract på 2 sider**, ikke en peer-reviewed empirisk studie. Påstander om "state-of-the-art" og "unsurpassed performance" er forfatternes egne kvalitative formuleringer og bør i tese-tekst formidles som "av forfatterne karakterisert som state-of-the-art" eller siteres med `\textcite{}` som vist forfatter-eierskap, ikke som uavhengig dokumentert sannhet.
- Kilden gir **ingen kvantitative benchmark-tall** (kjøretid, score, objektiv-verdi). Den kan derfor ikke siteres for noen tallfestet ytelse-påstand. For benchmark-tall i Ch 4.5 ¶6 må Ressursplanleggers egne målinger (`benchmark-results.md`) eller ekstern litteratur brukes.
- Kilden diskuterer **ikke NP-hardhet** eksplisitt og kan ikke siteres for NP-hardhets-påstanden i Ch 2.1 ¶4 (bruk `pinedo2016scheduling` der). Den nevner bare at problemene CP-SAT løser er "hard scheduling instances" — kvalitativt, ikke teoretisk.
- Kildens skedulerings-eksempler (Job-Shop, RCPSP) er **andre problemklasser** enn Ressursplanleggers multi-resource assignment med faste tidsvinduer. Bruk dem som strukturell analogi, ikke som direkte ekvivalens.
- Kilden er fra **Google OR-tools-teamet selv** — den har en åpenbar forfatter-bias for å fremheve egen løser. I formuleringer i tesen: bruk "ifølge OR-Tools-teamet ..." eller `\textcite{perron2023cpsatlp}` for å vise eierskap til påstanden.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| CP-SAT-LP solver | "an implementation of a purely integral Constraint Programming solver on top of a SAT solver using Lazy Clause Generation" | p. 3:1 |
| CP-SAT-LP (institusjonell) | "developed by the Operations Research team at Google and is part of the OR-Tools open-source optimization suite" | p. 3:1 |

## Rammeverk og modeller

### Portefølje-arkitekturens kategoriserings-akser (p. 3:1)

CP-SAT-LP organiserer parallelle arbeider-tråder langs disse aksene:

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| Arbeidere som finner primale løsninger | Finner gyldige (feasible) løsninger | Komplette løsere; Local Search; Large Neighborhood Search | p. 3:1 |
| Arbeidere som forbedrer duale grenser | Stramme inn optimalitets-bevis | (ingen konkret eksempel oppgitt) | p. 3:1 |
| Arbeidere som reduserer problemet | Forenkler instans-størrelsen | "continuous probing" | p. 3:1 |

Bruksnotat: Skala/struktur er mindre viktig for vårt formål enn poenget at *flere strategier kjører parallelt og deler informasjon* — som forklarer hvorfor CP-SAT-LP kan gi god kvalitet under stram tidsgrense.

## Key arguments / lines of reasoning

### Argument: Hvorfor CP-SAT-LP er konkurransedyktig — kombinasjonen av SAT-base, simplex og portefølje
- **Premiss 1:** SAT-løsere med Lazy Clause Generation er kraftige for diskrete kombinatoriske problemer (chuffed-arven).
- **Premiss 2:** Simplex (LP-relaksasjon) gir tightere duale grenser og åpner for MIP-teknikker (presolve, cuts, reduced cost fixing).
- **Premiss 3:** En portefølje av forskjellige arbeidere prøver flere strategier parallelt og deler informasjon, noe som øker robusthet og gir massive speedups parallelt.
- **Konklusjon:** Resultatet er state-of-the-art i CP-miljøet, gjennombrudds-resultater på skedulerings-benchmarks, og konkurransedyktig mot beste MIP-løsere på rent integrale problemer.
- **Sted:** (p. 3:1)
- **Hvilke claims dette støtter:** Ch 4.5 ¶2 (teknologivalgs-begrunnelse).

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Job-Shop scheduling-problemet | At CP-SAT-LP har lukket åpne harde benchmark-instanser i en klassisk skedulerings-klasse | p. 3:1 |
| Resource-Constrained Project Scheduling Problem (RCPSP) | At CP-SAT-LP håndterer ressurs-beskrankede prosjekt-skedulerings-instanser godt | p. 3:1 |

## Data og statistikk

Kilden inneholder ingen kvantitative tall, statistikk eller benchmark-resultater. Påstandene om ytelse er kvalitative ("state-of-the-art", "unsurpassed", "breakthrough", "massive speedups").

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Lazy Clause Generation (LCG) | Teknikk fra Stuckey [12] der CP-propagering inkrementelt genererer SAT-klausuler. Grunnlaget for chuffed og CP-SAT-LP. | p. 3:1 |
| chuffed solver | LCG-basert CP-løser ([4]) som CP-SAT-LP bygger videre på. | p. 3:1 |
| Linear relaxation / simplex | LP-løser brukt på den lineære delen av modellen for å produsere duale grenser. | p. 3:1 |
| MIP technology | Mixed Integer Programming-teknikker (presolve, dual reductions, branching, cuts, reduced cost fixing) integrert i CP-SAT-LP. | p. 3:1 |
| Local Search / Large Neighborhood Search | Heuristiske primal-løsnings-arbeidere i porteføljen. | p. 3:1 |
| Continuous probing | Teknikk for å redusere problem-størrelse, brukt av visse arbeidere i porteføljen. | p. 3:1 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "All in all, CP-SAT-LP is a state-of-the-art solver, with unsurpassed performance in the Constraint Programming community, breakthrough results on Scheduling benchmarks (with the closure of many open problems), and competitive results with the best MIP solvers (on purely integral problems)." | p. 3:1 | Ch 4.5 ¶2 — autoritativ begrunnelse for valg av CP-SAT |
| "The CP-SAT-LP solver is developed by the Operations Research team at Google and is part of the OR-Tools open-source optimization suite." | p. 3:1 | Ch 4.5 ¶2 — proveniens og institusjonell støtte |
| "It is an implementation of a purely integral Constraint Programming solver on top of a SAT solver using Lazy Clause Generation." | p. 3:1 | Ch 2.1 ¶5 / Ch 4.5 ¶2 — kort arkitektonisk definisjon |
| "This has enabled breakthroughs in solving and proving hard scheduling instances of the Job-Shop problems and Resource Constraint Project Scheduling Problems." | p. 3:1 | Ch 4.5 ¶2 — strukturell analogi til vårt problem |
| "The CP-SAT-LP solver improves upon the chuffed solver in two main directions. First, it uses a simplex alongside the SAT engine. Second, it implements and relies upon a portfolio of diverse workers for its search part." | p. 3:1 | Ch 4.5 ¶2 — teknisk dybde (valgfri) |

## Hva kilden IKKE sier

- **NP-hardhet:** Kilden diskuterer ikke kompleksitetsteoretisk NP-hardhet for skedulerings-problemer. For den påstanden i Ch 2.1 ¶4, bruk `pinedo2016scheduling`, ikke denne.
- **Sammenligning med Timefold eller andre metaheuristikker:** Kilden nevner kun MIP-løsere som sammenligningspunkt, ikke metaheuristiske ramme-verk som Timefold/OptaPlanner. For vår speed-quality-tradeoff-diskusjon i Ch 2.1 ¶5 må Timefold-egenskaper hentes fra `timefold2026solver`.
- **Multi-resource assignment med faste tidsvinduer:** Vår problemklasse (driver+vehicle assignment med faste oppdrag-tider) nevnes ikke spesifikt. CP-SAT-LP er ikke dokumentert "for traffic coordinator scheduling" i kilden — bare for klassiske skedulerings-benchmark-klasser.
- **Quantifierte benchmark-tall:** Ingen kjøretid, score, eller objektiv-verdier — kun kvalitative ytelse-karakteristikker.
- **API eller bruks-eksempler:** Kilden er teoretisk/arkitektonisk, ikke en bruksveiledning. For API-bruk hør hjemme i `googleortools2026cpsat`-citeringen.
- **Lisens-detaljer eller bruk i kommersielle produkter:** Kun nevnt at OR-Tools er "open-source"; ingen videre detaljer.

### Kommentar til outline MUST CITE-marker

Ch 4.5 ¶2 har `MUST CITE: \textcite{perron2023cpsatlp}` — **bekreftet**. Kilden er den autoritative beskrivelsen av CP-SAT-LP-løseren og passer som referansen som etablerer hva CP-SAT-LP er, hvem som har laget den, og dens ytelse-status. Bør siteres sammen med `googleortools2026cpsat` (selve verktøyet/API-et) og `timefold2026solver` (alternativ motor).

## Forfatter-perspektiv / metodologi

Kilden er en *Invited Talk*-abstract fra hovedutviklerne av løseren ved Google OR-Tools-teamet. Den er ikke en empirisk studie eller uavhengig benchmark, men en autoritativ teknologi-beskrivelse fra første-hands-utviklerne. Skal siteres som primærkilde for hva CP-SAT-LP *er* (definisjon, arkitektur, proveniens), ikke som uavhengig evaluering av dens ytelse.