# Future Paths for Integer Programming and Links to Artificial Intelligence (`glover1986future`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The paper is a 17-page article. All sections were read; the section that anchors the thesis citation (Section 5 "Tabu Search", pp. 541–547) was deep-read. The other sections (controlled randomization including simulated annealing, learning strategies, induced decomposition) were read in full so the contribution to Ch 2.1 ¶5 (metaheuristics in Timefold) is properly contextualised.
  - **Gaps not investigated:** None — the paper is short and was read end-to-end.

## Source metadata
- **BibTeX key:** `glover1986future`
- **Reference (APA 7):** Glover, F. (1986). Future paths for integer programming and links to artificial intelligence. *Computers & Operations Research, 13*(5), 533–549. https://doi.org/10.1016/0305-0548(86)90048-1
- **Tilgang:** PDF (open) — `raw/glover1986future.pdf`
- **Raw source:** `../glover1986future.pdf`
- **Coverage in raw:** Hele artikkelen (s. 533–549). PDF s. 1 = printed s. 533, dvs. PDF-side = trykt side − 532.

## Sammendrag (2–3 setninger)
Glover argumenterer for at fremtiden for heltallsprogrammering (IP) og kombinatorisk optimering ligger i å kombinere OR-metoder med AI-prinsipper for å transcendere lokal optimalitet i komplekse problemer. Han presenterer fire klasser av strategier — kontrollert randomisering (inkl. simulated annealing), læringsstrategier, indusert dekomposisjon og **tabu search** — der tabu search introduseres formelt som en "meta-heuristikk" som forbyr utvalgte trekk for å unngå sykling og slippe ut av lokale optima. Kjerneintroduksjonen av tabu search-rammeverket og termen "meta-heuristic" stammer fra denne artikkelen.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.1 ¶4 (NP-hardness / motivasjon for heuristikk) | covered — Glover argumenterer eksplisitt for at konvergens-garantier må vike for fleksibilitet ved kombinatorisk kompleksitet |
| Ch 2.1 ¶5 (Timefold metaheuristic; tabu search og simulated annealing) | covered — opprinnelseskilden for tabu search og rammeverket "metaheuristic"; gir også Glovers kritikk av simulated annealing |
| Ch 2.2 (HITL) | outside scope — paperet diskuterer "human pattern recognizer in the loop" kort (s. 540), men dette er ikke HITL-design slik Ressursplanlegger forstår begrepet |
| Ch 2.4 (DSR) | outside scope |

## Claims this source supports

### Claim: "Tabu search is a meta-heuristic superimposed on another heuristic, designed to transcend local optimality by forbidding or penalising selected moves."
- **Suggested for:** Ch 2.1 ¶5 (Timefold-metaheuristikken bruker tabu search); subsidiært Ch 2.1 ¶4 (begrunnelse for hvorfor heuristikker trengs)
- **Direkte sitat:** "Tabu search may be viewed as a 'meta-heuristic' superimposed on another heuristic. The approach undertakes to transcend local optimality by a strategy of forbidding (or, more broadly, penalizing) certain moves." (p. 541 / PDF 9)
- **Parafrase:** Tabu search er en metaheuristikk som styrer en underliggende lokal-søk-heuristikk ved å forby reverseringer av nylige trekk.
- **Forbehold:** Glover behandler tabu search som synonymt med en tidligere "oscillating assignment"-strategi (s. 541) — moderne litteratur skiller disse, men det berører ikke vårt bruk.
- **Anvendelse på vårt case:** Når Ressursplanleggers Timefold-motor bruker tabu search på multi-resource scheduling-problemet, er tabu-listen mekanismen som hindrer at solveren reverserer en nylig sjåfør/kjøretøy-tildeling og dermed sykler rundt det samme lokale optimum — viktig fordi flåtestørrelser på 50+ ressurser har et stort lokalt-optimum-landskap der enkel hill-climbing låser seg.

### Claim: "Cycling avoidance is the primary purpose of marking moves tabu — and this is achieved by recording recent moves on a tabu list whose order determines when restrictions expire."
- **Suggested for:** Ch 2.1 ¶5 (mekanismebeskrivelse av tabu search hvis vi går i detalj)
- **Direkte sitat:** "The purpose of classing a move forbidden—i.e. 'tabu'—is chiefly to prevent cycling. In view of the mechanism adopted for this purpose, the approach might alternatively be called 'weak inhibition' search, for the moves it holds tabu are generally a small fraction of those available, and a move loses its tabu status to become once again accessible after a relatively short time." (p. 541 / PDF 9)
- **Parafrase:** Tabu-status er midlertidig; bare en liten brøkdel av mulige trekk er forbudt på et gitt tidspunkt.
- **Forbehold:** Detaljen om "weak inhibition" og kontrast til branch-and-bound er sannsynligvis for teknisk for ¶5; bruk bare hvis ¶ utvider beskrivelsen av Timefold internt.
- **Anvendelse på vårt case:** Ressursplanleggers Timefold-konfig setter tabu-listestørrelse implisitt; mekanismen forklarer hvorfor solveren kan utforske *nærliggende* tildelingsendringer rett etter at et lokalt optimum er nådd, i stedet for å låse seg.

### Claim: "After reaching a local optimum, tabu search continues by accepting the best non-tabu move — even if it is non-improving — rather than restarting or randomising."
- **Suggested for:** Ch 2.1 ¶5 (forklarer hvorfor metaheuristikker beats greedy/lokalsøk på store instanser)
- **Direkte sitat:** "By this orientation, the procedure initially heads directly to a local optimum. Local optimality, however, is not a condition that leads to disruption of the search process (as by immediately invoking a 'restart' or 'shakeup' response), since the ability to identify a best available move remains." (p. 542 / PDF 10)
- **Parafrase:** Tabu search avbryter ikke ved lokalt optimum; den velger bare neste beste trekk og holder kursen via tabu-lister.
- **Forbehold:** Dette skiller tabu search fra simulated annealing (som aksepterer dårligere trekk probabilistisk) og random restart — kontrasten er nyttig hvis ¶5 vil sammenligne metaheuristikker.
- **Anvendelse på vårt case:** På Ressursplanleggers store ukeplaner — der greedy låser seg på første tilfeldige feasible løsning og CP-SAT er for treg — er det nettopp denne "fortsett å bevege deg etter lokalt optimum"-egenskapen som gjør Timefold relevant for instanser over ~500 oppdrag.

### Claim: "Empirical results indicate that tabu list sizes around 7 (range 5–9, occasionally up to 12) are effective and approximately problem-independent."
- **Suggested for:** Ch 2.1 ¶5 (kun hvis ¶ trenger en konkret detalj om tuning av Timefold-tabu-search) — ellers bare bakgrunn
- **Direkte sitat:** "Two general conclusions concerning the use of separate tabu lists, which interestingly appear to be independent of the application, have emerged from experiment: (1) each tabu list should have the same value of m (i.e. the same size), though small variations seem relatively unimportant; (2) the best value for m is approx. 7 (though all values from 5 to 9, and up to 12 in the case of [35], appear to work well)." (p. 543 / PDF 11)
- **Parafrase:** Empirisk er tabu-listestørrelse på ca. 7 nær-optimal og lite avhengig av problemtype.
- **Forbehold:** Glovers eksperimenter er fra 1986 på små instanser (144 binærvariabler). Moderne implementasjoner (inkl. Timefold) bruker langt mer sofistikerte minne-strukturer. Bruk bare som historisk forankring.
- **Anvendelse på vårt case:** Detaljer om tabu-listestørrelse er sannsynligvis for finkornet for thesis-nivået; nevnes bare hvis Embret eksplisitt vil dokumentere Timefold-tuning i Ch 4.5.

### Claim: "Heuristic methods that lack formal convergence proofs can still outperform exact methods on large combinatorial problems, because flexibility is essential when problem complexity exceeds what rigid procedures can handle."
- **Suggested for:** Ch 2.1 ¶4 (NP-hardness — motivasjon for heuristisk multi-engine-tilnærming)
- **Direkte sitat:** "In brief, effective strategies for combinatorial problems can require methods that formal theorems are unable to justify. […] In the face of combinatorial complexity, there must be freedom to depart from the narrow track that logic single-mindedly pursues, even on penalty of losing the guarantee that a desired destination will ultimately be reached." (pp. 534–535 / PDF 2–3)
- **Parafrase:** For komplekse kombinatoriske problemer er metoder uten konvergens-bevis ofte mer effektive enn metoder med slike bevis.
- **Forbehold:** Argumentet er filosofisk og programmatisk, ikke et formelt resultat. Bruk det som *motivasjon* for valg av Timefold/heuristikk, ikke som "bevis" for at heuristikk er bedre.
- **Anvendelse på vårt case:** Begrunner direkte hvorfor Ressursplanlegger har en metaheuristikk-motor (Timefold) ved siden av en eksakt CP-SAT — for instanser der CP-SAT timer ut, må en fleksibel metaheuristikk overta selv uten optimalitetsgaranti.

### Claim: "Tabu search produced solutions roughly 15× better than iterative-improvement local optima on a real-world resource-allocation problem, and beat a commercial mixed-IP solver running 150× longer."
- **Suggested for:** Ch 2.1 ¶5 (empirisk støtte for at metaheuristikker slår både greedy og eksakte løsere på passende instanser); kan også brukes i Ch 4.5 ¶6 hvis Timefold-benchmark skal kontekstualiseres mot litteraturen
- **Direkte sitat:** "Table 1 shows the dramatic difference between local optima found by the iterative improvement heuristic and solutions obtained by tabu search. The overall average for the local optima exceeds that for tabu search by a factor of nearly 15 to 1." (p. 546 / PDF 14). Også: "the tabu search procedure took 4 CPU seconds and obtained a solution with an objective function value of 1.0. The MPS code, by contrast, was taken off the machine after 600 CPU seconds, having obtained a solution with an objective function value of 21.0." (p. 546 / PDF 14)
- **Parafrase:** På et realistisk ressurs-tildelingsproblem var tabu search dramatisk bedre enn både lokalsøk og en kommersiell eksakt løser med 150× mer CPU-tid.
- **Forbehold:** Resultatene er fra 1986 på et problem med 144 binærvariabler og 40 begrensninger. Moderne MIP-solvere (Gurobi, OR-Tools CP-SAT) er mange størrelsesordener bedre enn 1986-MPS-koden Glover sammenlignet med. Sammenligningen forblir kvalitativt nyttig (metaheuristikk er konkurransedyktig på praktiske problemer) men må ikke leses som "tabu search slår CP-SAT".
- **Anvendelse på vårt case:** Demonstrerer det tidligste empiriske argumentet for at metaheuristikker er praktisk verdifulle på ressurs-tildelingsproblemer som ligner Ressursplanleggers (objekter til bokser med vektmål — samme strukturelle form som oppdrag til sjåfører med kapasitetsbegrensninger).

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| meta-heuristic | metaheuristikk | Glover myntet termen i denne artikkelen (s. 541); brukes uendret i Ressursplanleggers Timefold-dokumentasjon |
| move | trekk / tildelings-endring | I tabu search betyr "move" en lokal endring (f.eks. bytte to elementer); i Ressursplanlegger tilsvarer det å reassigne en sjåfør eller bytte kjøretøy mellom to oppdrag |
| tabu list | tabu-liste | Direkte oversettelse; samme konsept i Timefold |
| local optimum | lokalt optimum | Direkte oversettelse |
| object / box | oppdrag / sjåfør+kjøretøy | Glovers eksperiment-domene (s. 545–546): vektede objekter tildeles bokser med kapasitet — strukturelt analogt til oppdrag tildelt sjåfør+kjøretøy med kompetanse/tidsbegrensninger |
| aspiration level | aspirasjonsnivå | Aspirasjonskriteriet som lar tabu-trekk likevel velges hvis de gir tilstrekkelig forbedring (s. 543) |
| cycling | sykling | Når et søk gjentar samme sekvens trekk i en løkke; tabu search forhindrer dette |
| iterative improvement / local search heuristic | hill-climbing / lokalsøk | Underliggende heuristikk som tabu search styrer |

### Begrensninger i applikasjon

- **Domeneforskjell — IP versus scheduling.** Glover skriver om heltallsprogrammering generelt (knapsack, plant location, TSP, channel-load assignment). Ressursplanlegger er multi-resource scheduling med tidsvinduer. Strukturen er tett beslektet (begge er NP-harde kombinatoriske problemer med diskrete tildelingsbeslutninger), men Glovers spesifikke eksempler kan ikke siteres som "scheduling-resultat".
- **År og benchmark-realisme.** Resultatene fra 1986 (Honeywell DPS-8, MPS-koden) er ikke direkte sammenlignbare med moderne solvere. Bruk Glover som *opprinnelse for tabu-search-konseptet* og som motivasjon, ikke som benchmark for hva moderne metaheuristikker faktisk leverer.
- **Glover snakker ikke om Vehicle Routing eller om HITL.** Han nevner TSP som anvendelsesområde for læringsstrategier (s. 538), men ikke VRP og ikke koordinator-i-loopen. Kildens bidrag er strengt på solver-mekanikk-nivå, ikke på system-design-nivå.
- **"Synonymt med oscillating assignment".** Glover behandler tabu search og oscillating assignment som samme strategi (s. 541). Senere litteratur skiller disse. Det er trygt å sitere Glover som "introduserer tabu search"; det er ikke trygt å sitere ham for moderne tabu search-varianter (Reactive Tabu Search, Path Relinking osv.) — disse kom senere.
- **Empiriske resultater er på små instanser.** Eksperimentet bruker 144 binærvariabler og 40 begrensninger (s. 545). Ressursplanleggers reelle instanser har 50+ ressurser × oppdrag-antall som gir tusenvis av binærvariabler. Generaliseringen er strukturell, ikke kvantitativ.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Tabu search (meta-heuristic) | "Tabu search may be viewed as a 'meta-heuristic' superimposed on another heuristic. The approach undertakes to transcend local optimality by a strategy of forbidding (or, more broadly, penalizing) certain moves." | p. 541 / PDF 9 |
| Tabu (status av et trekk) | "The purpose of classing a move forbidden—i.e. 'tabu'—is chiefly to prevent cycling." | p. 541 / PDF 9 |
| Tabu list (formålet) | "The function of such lists is not to prevent a move from being repeated, but to prevent it from being reversed, and the prohibition against reversal is conditional rather than absolute" | p. 542 / PDF 10 |
| Aspiration level | "A(z) may be interpreted as the aspiration level of the objective function value next to be reached when the current value is z. […] the strategy of the aspiration list is to permit a move to override its tabu status if it succeeds in improving z to the value A(z)." | p. 543 / PDF 11 |
| Simulated annealing (Glovers parafrase) | "the path to an optimal state likewise begins from one of diffuse randomization, somewhat removed from optimality, where nonimproving moves are initially accepted with a relatively high probability which is gradually decreased over time." | pp. 535–536 / PDF 3–4 |

## Rammeverk og modeller

### Glovers fire strategier for å transcendere lokal optimalitet (s. 535 / PDF 3)

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| Controlled randomization | Random restart eller "random shakeup"; simulated annealing er en spesialisert variant | Simulated annealing for kombinatorisk optimering | p. 535 / PDF 3 |
| Learning strategies | Lære fra tidligere forsøk hvilke beslutningsregler / variabler / trekk som gir best resultat ("strongly determined" og "consistent" variabler) | Job-shop scheduling med probabilistisk regelvelging; TSP "good things share common features" | pp. 536–540 / PDF 4–8 |
| Induced decomposition | Skape (ikke bare finne) struktur i problemet, f.eks. via lagdeling og auxiliary variabler | Generaliserte nettverksstrukturer fra zero-one IP | pp. 540–541 / PDF 8–9 |
| Tabu search | Metaheuristikk som forbyr reversering av nylige trekk for å unngå sykling | Channel-load optimering for U.S. Bureau of Land Management | pp. 541–547 / PDF 9–15 |

### Tabu search-mekanikk (s. 542–544 / PDF 10–12)

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| Tabu list (sirkulær) | Recorder de m siste trekkene; nyeste skyver ut eldste | Adjacent-value moves for IP: separate "up" og "down" lister | p. 542 / PDF 10 |
| Tabu list size m | Empirisk best ca. 7; fungerer i 5–9 (opp til 12) | Channel-load eksperiment | p. 543 / PDF 11 |
| Aspiration criterion (enkel) | Tabu-trekk tillates hvis det forbedrer best-så-langt-verdi | — | pp. 542–543 / PDF 10–11 |
| Aspiration list A(z) | Mer fleksibelt aspirasjonsnivå indeksert på objektivverdi z | A(z) = z − 1 initielt; oppdateres til Min[A(z'), z" − 1] | p. 543 / PDF 11 |
| Equivalent / null moves | Trekk som er strukturelt like; må flagges samtidig som tabu | Knapsack: bytte to like-vektede objekter er null move | p. 543 / PDF 11 |
| Feasibility/optimality split | E(x) = aF(x) + bO(x); a, b justeres dynamisk under søket | "Outside in" og "inside out" heuristikker | p. 544 / PDF 12 |

## Key arguments / lines of reasoning

### Argument: Lokal optimalitet er kjerneproblemet for heuristikker
- **Premiss:** Diskrete optimeringsproblemer har mange lokale optima.
- **Premiss:** Enkle hill-climbing/lokalsøk-heuristikker stopper på første lokale optimum.
- **Konklusjon:** Strategier for å *transcendere* lokal optimalitet er det sentrale designkriteriet for gode heuristikker.
- **Sted:** p. 535 / PDF 3
- **Hvilke claims dette støtter:** Ch 2.1 ¶4 (begrunner heuristikk-tilnærming generelt) og ¶5 (motivasjon for at Timefold finnes ved siden av greedy)

### Argument: Konvergensgarantier er ikke gratis — de pålegger rigiditet
- **Premiss:** Metoder med formelt bevisbare konvergens-egenskaper må være rigid strukturert.
- **Premiss:** Rigiditet er ineffektivt mot kombinatorisk kompleksitet.
- **Konklusjon:** Noen ganger er fleksible heuristikker uten konvergens-garanti mer effektive enn eksakte metoder.
- **Sted:** pp. 534–535 / PDF 2–3
- **Hvilke claims dette støtter:** Ch 2.1 ¶4 (multi-engine-tilnærmingen — hvorfor man har både eksakte og heuristiske solvere)

### Argument: Tabu search prefererer best tilgjengelig trekk over randomisering
- **Premiss:** "Random" trekk er bare verdifulle hvis man ikke kan identifisere et bedre trekk.
- **Premiss:** Tabu search kan alltid identifisere det beste ikke-tabu trekket.
- **Konklusjon:** Tabu search trenger ikke randomisering; tabu-listen er nok mekanisme for å unngå sykling og slippe ut av lokale optima.
- **Sted:** pp. 541–542 / PDF 9–10
- **Hvilke claims dette støtter:** Ch 2.1 ¶5 (kontrast mellom tabu search og simulated annealing — hvis ¶5 vil utdype hvorfor begge eksisterer i Timefolds repertoar)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Channel-load optimering for U.S. Bureau of Land Management (vektede disk-pakker tildelt kanaler) | Hovedkasusen for tabu search; 144 binærvariabler, 9 startløsninger; tabu search ~15× bedre enn iterative-improvement, og 4 CPU-sek slo MPS på 600 CPU-sek | pp. 545–546 / PDF 13–14 |
| Plant location problem | Trekk har én retning ("from-to"); illustrerer asymmetriske tabu-lister | p. 542 / PDF 10 |
| TSP 2-OPT | Slett to ikke-tilstøtende kanter, legg til to nye; tabu kan markere én av de slettede kantene | pp. 542–543 / PDF 10–11 |
| Job-shop scheduling (læringsstrategier) | Probabilistisk og parametrisk læring av lokale beslutningsregler | pp. 536–537 / PDF 4–5 |
| Employee scheduling (referanse [35]) | Tabu-parameter som svinger antall ansatte rundt det optimale | p. 544 / PDF 12 |
| Architectural design (kluster-plassering, ref [87]) | Andre real-world tabu search-anvendelse | p. 542 / PDF 10 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| Tabu list size m ≈ 7 (range 5–9, opp til 12) | antall trekk | empirisk fra Glovers eksperimenter | p. 543 / PDF 11 |
| Tabu search vs lokalt optimum: gjennomsnittsforhold ~15:1 | objektiv-funksjons-verdi-ratio | 16 testproblemer × 9 startløsninger | p. 546 / PDF 14 |
| Tabu search: 4 CPU-sekunder, objektiv = 1.0 | tid + objektivverdi | Honeywell DPS-8, ekstra BLM-problem | p. 546 / PDF 14 |
| MPS (kommersiell mixed-IP): 600 CPU-sekunder, objektiv = 21.0 | tid + objektivverdi | samme problem | p. 546 / PDF 14 |
| Cycling observert ved m ≤ 4 (sykluslengde 14–30 trekk) | trekk per syklus | channel-load eksperiment | p. 544 / PDF 12 |
| Cycling forsvant ved m = 5 | tabu list size | samme | p. 544 / PDF 12 |

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Simulated annealing | Probabilistisk akseptering av forverrende trekk; Glover er kritisk til metoden | pp. 535–536 / PDF 3–4 |
| Random restart / random shakeup | Eldre randomiserings-strategier som tabu search delvis erstatter | p. 535 / PDF 3 |
| Strongly determined / consistent variables | Variabler som beholder verdi på tvers av gode løsninger; basis for læringsstrategier | pp. 538–539 / PDF 6–7 |
| Branch-and-bound | "Strong inhibition" search som kontrast til tabu search ("weak inhibition") | p. 541 / PDF 9 |
| Surrogate constraints / Lagrangean relaxation | Klassiske OR-strategier referert som bakgrunn | pp. 533–534, 540 / PDF 1–2, 8 |
| Oscillating assignment strategy | Glovers tidligere strategi som tabu search "implementerer" | p. 541 / PDF 9 |
| Aspiration level search | Variant av "best move"-utvelgelse når full evaluering er for dyr | p. 542 / PDF 10 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "Perhaps the most conspicuous limitation of a heuristic method for problems involving discrete alternatives is the ability to become trapped at a local optimum." | p. 535 / PDF 3 | Ch 2.1 ¶4 — motivasjon for hvorfor multi-engine / heuristisk søk |
| "From this point of view, it is useful to organize the exploration of good methods for discrete problems around strategies for transcending local optimality." | p. 535 / PDF 3 | Ch 2.1 ¶5 — rammen for å diskutere metaheuristikker |
| "Tabu search may be viewed as a 'meta-heuristic' superimposed on another heuristic. The approach undertakes to transcend local optimality by a strategy of forbidding (or, more broadly, penalizing) certain moves." | p. 541 / PDF 9 | Ch 2.1 ¶5 — den primære definisjonssitatet for tabu search |
| "The purpose of classing a move forbidden—i.e. 'tabu'—is chiefly to prevent cycling." | p. 541 / PDF 9 | Ch 2.1 ¶5 — kort mekanisme-utdyping |
| "the procedure initially heads directly to a local optimum. Local optimality, however, is not a condition that leads to disruption of the search process" | p. 542 / PDF 10 | Ch 2.1 ¶5 — kontrast til greedy-stop-på-lokalt-optimum |
| "[the best value for m is approx. 7] though all values from 5 to 9, and up to 12 […] appear to work well" | p. 543 / PDF 11 | Bare hvis Ch 4.5 vil dokumentere konkret tabu-tuning |
| "the tabu search procedure took 4 CPU seconds and obtained a solution with an objective function value of 1.0. The MPS code, by contrast, was taken off the machine after 600 CPU seconds" | p. 546 / PDF 14 | Ch 2.1 ¶5 / Ch 4.5 — empirisk støtte for at metaheuristikker er praktisk konkurransedyktige |
| "effective strategies for combinatorial problems can require methods that formal theorems are unable to justify" | p. 534 / PDF 2 | Ch 2.1 ¶4 — filosofisk forankring for fleksibel-heuristikk-tilnærming |

## Hva kilden IKKE sier

- **Sier ingenting om vehicle routing problem (VRP) som sådan.** Glover nevner TSP, knapsack, plant location, channel-load assignment og job-shop scheduling. Ikke VRP. Sitater må ikke fremstilles som om Glover har anvendt tabu search på VRP — det skjedde i senere arbeider av andre forfattere.
- **Sier ingenting om multi-resource scheduling med tidsvinduer.** Glovers nærmeste eksempel er employee scheduling (referanse [35], egen artikkel samme nummer). Vårt problem er strengere — flere typer ressurser per oppgave samtidig — og Glover dekker ikke det direkte.
- **Sier ingenting om late-acceptance hill climbing.** Timefolds dokumentasjon nevner tabu search, simulated annealing og late-acceptance hill climbing. Glover dekker bare de to første (og kritiserer simulated annealing skarpt). LAHC kom senere.
- **Sier ingenting om CP-SAT eller constraint programming-baserte solvere.** Constraint programming som disiplin er knapt nevnt; Glover snakker om IP-relaksasjoner, ikke om Boolean satisfiability solvers.
- **Sier ingenting om Human-in-the-Loop som designprinsipp.** Glover nevner kort "human pattern recognizer in the loop" (s. 540 / PDF 8) som en del av læringsstrategier — ikke som en designfilosofi for beslutningsstøttesystemer. Dette er ikke det samme som Parasuramans HITL-rammeverk og må ikke siteres for det.
- **Sier ingenting om benchmarking-resultater for moderne metaheuristikker.** Tallene fra 1986 (4 vs 600 CPU-sek på Honeywell) er historisk interessante men sier ingenting om hvordan Timefold presterer på moderne maskinvare — ikke siter dem som en samtidig benchmark.
- **Sier ingenting om Norge eller transportbransjen.** Selvsagt — men nevnes for fullstendighet siden domenet ditt er nettopp dette.
- **Outline `MUST CITE`-markører som peker til Glover:** Ingen `MUST CITE: \textcite{glover1986future}` finnes i outline.md per d.d. Sannsynligvis fordi outline ikke skiller ut Glover spesifikt — Ch 2.1 ¶5 nevner "Timefold metaheuristic (tabu search, simulated annealing)" uten eksplisitt sitat-marker. Glover er den korrekte primærkilden for *tabu search* som konsept; kan legges til i outline ved behov.

## Forfatter-perspektiv / metodologi

Glover er en av grunnleggerne av moderne metaheuristikk-feltet (særlig tabu search og scatter search). Artikkelen er programmatisk og semi-formell: en blanding av konseptuell argumentasjon, litteraturreferanser og ett konkret empirisk eksperiment (channel-load-problemet). Den er ikke en rigorøs sammenlignende studie — den introduserer rammeverk og argumenterer for dem. Bruk den som *opprinnelseskilde* for tabu search og som filosofisk motivasjon for fleksible heuristikker, ikke som empirisk benchmark.