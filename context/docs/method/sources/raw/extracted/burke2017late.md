# The Late Acceptance Hill-Climbing Heuristic (`burke2017late`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The paper is a 9-page journal article fully read. LAHC is presented in Section 2 (definition + pseudocode), with experimental properties in Sections 3–4, scale-independence in 4.4, and competition success in Section 5. Conclusions in Section 6 enumerate the algorithm's properties — these map cleanly onto the thesis areas where Timefold's metaheuristic backing is described (Ch 2.1 ¶5 and Ch 4.5 ¶2). All claims, definitions, the pseudocode framework, and the limits-of-applicability are captured.
  - **Gaps not investigated:** None — the paper has no further sections beyond what was extracted. Detailed numerical tables (Tables 3–9) are noted but only the most relevant cells were captured; the full table content is in the PDF if needed.

## Source metadata
- **BibTeX key:** `burke2017late`
- **Reference (APA 7):** Burke, E. K., & Bykov, Y. (2017). The late acceptance Hill-Climbing heuristic. *European Journal of Operational Research*, *258*(1), 70–78. https://doi.org/10.1016/j.ejor.2016.07.012
- **Tilgang:** PDF (in `raw/`)
- **Raw source:** `../burke2017late.pdf`
- **Coverage in raw:** Full paper (9 pages, printed pp. 70–78). PDF page = printed page − 69. Article structure simple enough that single page reference (e.g., `p. 71`) is unambiguous.

## Sammendrag (2–3 setninger)
Kilden introduserer Late Acceptance Hill Climbing (LAHC) — en metaheuristikk for kombinatorisk optimering der en kandidat-løsning sammenlignes med løsningen som var aktuell *Lh* iterasjoner tidligere (ikke med dagens) før den aksepteres eller forkastes. Forfatterne argumenterer for at LAHC er nesten like enkel å implementere som greedy Hill-Climbing, har én eneste justerbar parameter (historie-lengden *Lh*) som styrer CPU-tid lineært, og er skala-uavhengig — i motsetning til SA, TA og GDA som krever en problem-spesifikk «cooling schedule». Eksperimenter på TSP og Exam Timetabling, og førsteplass i International Optimisation Competition 2011, brukes som dokumentasjon på at metoden er praktisk anvendbar og ofte slår SA/TA/GDA på store instanser.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.1 ¶4 (NP-hardness, behov for heuristikk) | partial — kilden bekrefter TSP og Exam Timetabling som NP-harde og motiverer metaheuristikk-tilnærmingen, men sier ingenting om vår multi-resource-variant |
| Ch 2.1 ¶5 (Solver comparison: greedy / CP-SAT / Timefold-metaheuristikk) | covered — LAHC er en av metaheuristikkene Timefold (eks-OptaPlanner) bruker; kilden navngir OptaPlanner (Red Hat) eksplisitt som en av to real-world-systemer som har implementert LAHC |
| Ch 4.5 ¶2 (Chosen approach — Timefold-konfigurasjon) | covered — kilden gir grunnlag for å beskrive Timefolds late-acceptance-modus: én parameter *Lh* styrer CPU-tid lineært; metoden er praktiker-vennlig |
| Ch 2.2 (HITL) | outside scope — kilden er ren algoritme-teori, ingen menneske-i-løkka-aspekter |
| Ch 5.2 (Algorithm performance and HITL) | outside scope — kilden sammenligner metaheuristikker med hverandre på benchmark-problemer, ikke med menneskelige planleggere |

## Claims this source supports

### Claim: «LAHC er en metaheuristikk som aksepterer ikke-forbedrende trekk når kandidat-kostnaden er bedre enn kostnaden Lh iterasjoner tidligere»
- **Suggested for:** Ch 2.1 ¶5 (i listen over Timefolds metaheuristikker — alternativ eller supplement til tabu-search/simulated annealing); Ch 4.5 ¶2 (når Timefolds konfigurasjon beskrives).
- **Direkte sitat:** "This paper introduces a new and very simple search methodology called Late Acceptance Hill-Climbing (LAHC). It is a local search algorithm, which accepts non-improving moves when a candidate cost function is better than it was a number of iterations before." (p. 70)
- **Direkte sitat (mekanisme):** "in greedy Hill Climbing a candidate solution is compared with the immediate current one, but in the Late Acceptance Hill Climbing (LAHC) a candidate is compared with that solution, which was the current several iterations before." (p. 71)
- **Parafrase:** LAHC utvider greedy hill-climbing ved at akseptanse-kriteriet ikke sammenlignes med dagens beste løsning, men med løsningen for *Lh* iterasjoner siden — dette gir kontrollert aksept av forverringer uten en cooling schedule.
- **Forbehold:** Lh = 0 eller 1 reduserer LAHC til greedy HC; LAHC «obtains its unique properties with Lh equal to 2 and higher» (p. 72). Metoden er testet på TSP og Exam Timetabling, ikke på multi-resource-tildeling.
- **Anvendelse på vårt case:** I Ressursplanleggers Timefold-engine konfigureres «Late Acceptance»-fasen ved å sette historie-lengden *Lh*; denne verdien styrer hvor mye søke-tid Timefold bruker på fase-2 forbedring av planforslaget før koordinatoren får det presentert.

### Claim: «LAHC har én eneste algoritmisk parameter (Lh), og CPU-tid er tilnærmet lineært proporsjonal med denne parameteren»
- **Suggested for:** Ch 2.1 ¶5 (speed-quality tradeoff for metaheuristikker); Ch 4.5 ¶2 (begrunnelse for valg av late-acceptance-fase i Timefold) eller Ch 4.5 ¶6 (benchmarking — tids-budsjett pr. solver).
- **Direkte sitat:** "It is dependent on a single algorithmic parameter, which regulates the CPU time. The presented experiments have revealed that the CPU time is approximately proportional to this parameter. Correspondingly, it can be well-tuned with less effort than most modern metaheuristics. This is especially attractive to practitioners." (p. 77)
- **Direkte sitat (empirisk):** "the average processing time of runs with Lh = 50000 is approximately 10 times longer than that with Lh = 5000. Based on this, we can propose that the CPU time is linearly dependent on the history length." (p. 73)
- **Parafrase:** Den eneste parameteren brukeren må sette i LAHC er *Lh* (history length). Forfatterne dokumenterer empirisk en lineær sammenheng mellom *Lh* og CPU-tid på TSP-instansen U1817, som de utvider til en generell observasjon.
- **Forbehold:** Den lineære sammenhengen mellom *Lh* og CPU-tid er observert empirisk på de testede benchmark-problemene; vinkel-koeffisienten Time/Lh «is different for each particular instance» (p. 77).
- **Anvendelse på vårt case:** Trafikkoordinatorens tidsbudsjett for plangenerering (f.eks. 30 sek for daglig plan) kan oversettes direkte til en *Lh*-verdi i Timefold via målt vinkel-koeffisient på vår problem-instans — én parameter å justere, ikke en cooling schedule.

### Claim: «LAHC er nesten like enkel som greedy Hill-Climbing, men betydelig kraftigere; en utvikler kan erstatte HC med LAHC med minimal endring»
- **Suggested for:** Ch 2.1 ¶5 (begrunner hvorfor en metaheuristikk-fase kan tas i bruk i tillegg til greedy uten stor økning i kompleksitet); Ch 4.5 ¶2 (begrunnelse for multi-engine-arkitekturen — billig å legge til en metaheuristikk-fase).
- **Direkte sitat:** "It is almost as simple as the greedy HC, but much more powerful. So, it can be easily implemented in experimental and practical systems. Also, the developers can substitute HC in existing systems by a stronger search technique with minimum effort." (p. 77)
- **Parafrase:** Forskjellen i implementasjonskompleksitet mellom greedy HC og LAHC er at man holder en liste av lengde *Lh* med tidligere kostnader; alle andre detaljer er identiske.
- **Forbehold:** «Enkel» her gjelder algoritmen i seg selv, ikke det øvrige rammeverket (move-construction, fitness-evaluering, stopp-betingelse).
- **Anvendelse på vårt case:** Når Ressursplanlegger allerede har en greedy solver implementert, gir LAHC en oppgraderingsvei med lav kostnad — relevant for argumentet om at multi-engine-arkitekturen er pragmatisk gjennomførbar i SME-kontekst.

### Claim: «På de fleste benchmark-problemer (særlig de største) slår LAHC simulated annealing, threshold accepting og great deluge»
- **Suggested for:** Ch 2.1 ¶5 (når metaheuristikker rangeres etter speed-quality, gir kilden empirisk sammenligning); kan også støtte ¶4 om hvorfor metaheuristikk er nødvendig på store instanser.
- **Direkte sitat:** "It outperforms SA, TA and GDA on most of the benchmark problems (especially the larger sized ones). Taking into account that the competitor algorithms are well studied, but the studies on LAHC have just begun, this suggests that LAHC has significant potential for further development." (p. 77)
- **Direkte sitat (presisering):** "LAHC outperforms other methods with the larger sized problems (except for the Exam_2 dataset), while SA or TA show the best performance with the relatively smaller sized problems" (p. 75)
- **Parafrase:** I 100–120-sekunders cut-off på TSP og Exam Timetabling vinner LAHC på 5/7 TSP-instanser og 6/12 Exam-instanser. På små instanser er SA/TA noen ganger bedre.
- **Forbehold:** Sammenligningen gjelder TSP og Exam Timetabling — ikke ressurs-tildeling. Vinneren i 100–120 sek-vinduet er ikke nødvendigvis vinneren i andre tids-vinduer.
- **Anvendelse på vårt case:** Påstanden støtter at LAHC-fasen i Timefold er et fornuftig valg når Ressursplanlegger vokser til større fleeter (50+ ressurser × 100+ oppdrag) — domene-overgangen krever validering, men retningen er konsistent med Timefolds anbefaling.

### Claim: «LAHC er skala-uavhengig — rescaling av kostfunksjonen påvirker SA/TA/GDA dramatisk, men ikke LAHC»
- **Suggested for:** Ch 2.1 ¶5 (som en differensierende egenskap mellom metaheuristikker — relevant hvis Ch 5.2 trenger å forklare hvorfor noen solvere er mer robuste enn andre); kan flagges men er sannsynligvis ikke et hoved-claim.
- **Direkte sitat:** "the LAHC approach has an additional advantage (in contrast to the above cooling schedule based methods) in its scale independence. We present an example where the rescaling of a cost function in the Travelling Salesman Problem dramatically deteriorates the performance of three cooling schedule based techniques, but has absolutely no influence upon the performance of LAHC." (p. 70)
- **Direkte sitat (resonnement):** "if LAHC accepts a solution in the original problem then it also accepts this solution in the rescaled problem (and vice versa). Thus, being an extension of Hill Climbing, LAHC also inherits its scale independence. However, this is not the case for SA, TA and GDA." (p. 76)
- **Parafrase:** Fordi LAHCs akseptanse-kriterium kun avhenger av rang-sammenligning (kandidat vs. *Lh* iterasjoner siden), ikke absolutte verdier, er metoden upåvirket av monotone transformasjoner av kostfunksjonen.
- **Forbehold:** Demonstrert kun for én konkret rescaling (formel 3, U1817-datasett).
- **Anvendelse på vårt case:** Hvis Ressursplanleggers vekt-kalibrering for soft-constraints endres (en koordinator setter f.eks. workload-balanse 10× høyere), vil SA-baserte solvere kreve re-tuning av cooling-parametere; LAHC-fasen i Timefold vil i prinsippet være upåvirket. *Caveat:* dette er i utgangspunktet en perifer egenskap for vår oppgave — flagges hvis Ch 5.2 diskuterer solver-robusthet.

### Claim: «LAHC er en general-purpose metaheuristikk og bruker ikke egenskaper ved spesifikke problemtyper»
- **Suggested for:** Ch 2.1 ¶4 (når metaheuristikk-konseptet introduseres for å forklare hvorfor multi-engine-tilnærmingen er anvendelig på vår problem-klasse); Ch 4.5 ¶2 (når Timefolds konfigurasjon forklares).
- **Direkte sitat:** "It does not employ the properties of a particular type of problem and, therefore, could be positioned as a general-purpose metaheuristic. ... We expect that it can be applied to any optimization problem where other one-point search methods are applicable." (p. 77)
- **Direkte sitat (Section 3):** "The proposed LAHC does not employ the properties of any particular type of problem. Therefore, it can be thought of as a general purpose search method, i.e., a metaheuristic. We expect that it can be applied to any problem, where other local search methods (HC, SA, TA, GDA) are applicable." (p. 72)
- **Parafrase:** LAHC har ingen problem-spesifikke krav utover at man kan definere en kostfunksjon, en initialløsning og en move-operator.
- **Forbehold:** Forfatterne sier «we expect» — generaliteten er hevdet, ikke bevist for alle problemklasser. Empirisk testet kun på TSP, Exam Timetabling og Magic Square.
- **Anvendelse på vårt case:** Fordi Ressursplanleggers driver-vehicle-assignment kan formuleres med kostfunksjon (hard/soft-constraint-vekter) og swap-/reassign-moves, faller problemet innenfor LAHCs hevdede anvendelsesområde — én av flere komponenter i Timefolds search-pipeline.

### Claim: «Cooling-schedule-baserte metoder (SA/TA/GDA) har en svakhet: optimal cooling-form er problem/instans-avhengig og krever empirisk tuning per problem»
- **Suggested for:** Ch 2.1 ¶5 (som motivasjon for hvorfor en parameter-fattig metaheuristikk som LAHC er attraktiv i et SME-praktisk system).
- **Direkte sitat:** "A weak point of the cooling schedule is that its optimal form is problem/instance-dependent and generally indefinite. That is the reason for the existence of a number of empirical recommendations regarding cooling schedules, which are more or less effective for a range of studied problems. However, there is no guarantee that such a proposition will work for a new problem." (p. 71)
- **Parafrase:** Alle parametere i SA/TA/GDA — initial temperatur, cooling factor, terskel — krever per-problem-tuning fordi den optimale verdien ikke kan utledes generelt.
- **Forbehold:** Argumentet leveres som motivasjon for forfatternes egen metode; det er en kjent egenskap ved SA/TA-litteraturen, men formuleringen er forfatternes.
- **Anvendelse på vårt case:** Ressursplanleggers koordinator-bruker forventes ikke å tune solver-parametere; en metode som krever én parameter (LAHC-Lh) er praktisk fordele over en metode som krever cooling-schedule-tuning.

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Local search | Lokalt søk (intern) | Brukes i tech/algorithm.md uten oversettelse |
| Hill-Climbing (HC) | Greedy solver / hill-climbing | Vår «greedy solver» er en HC-variant; kilden bruker «greedy HC» og «HC» om hverandre |
| Late Acceptance Hill Climbing (LAHC) | Late-acceptance hill climbing (Timefold-konfig) | Glossary nevner allerede «late-acceptance hill climbing» som en av Timefolds modi |
| Metaheuristic | Metaheuristikk | Begge språk bruker termen |
| Cooling schedule | Avkjølingsplan / cooling schedule | Norsk lagt brukt i bachelor-litteratur er begrenset; behold engelsk |
| Candidate solution / current solution | Kandidat-plan / aktuell plan | I Ressursplanlegger: en plan-tilstand under solver-iterasjon |
| Cost function | Kostnadsfunksjon / objektiv-funksjon (soft + hard score) | Ressursplanleggers solver bruker en sammensatt score (hard + soft) — se algorithm.md |
| Move (e.g., double-bridge, swap) | Move (oppdrag-bytte, sjåfør-reassign) | Vårt domene har naturlige moves: bytt sjåfør på ett oppdrag, swap to oppdrag mellom sjåfører, etc. |
| TSP / Exam Timetabling | (ikke brukt i Ressursplanlegger) | Kildens benchmark-domener; nevnes kun for å forklare evidens-grunnlaget |
| History length Lh | Lh / late-acceptance history length | Direkte parameter i Timefold-konfig |
| OptaPlanner | Timefold | OptaPlanner ble fork-et til Timefold; kilden refererer til OptaPlanner som da var Red Hats prosjekt |

### Begrensninger i applikasjon

- **Single-resource fokus:** LAHC er beskrevet og testet på problemer med én løsnings-struktur (en TSP-tour, en exam-timetable). Ressursplanleggers problem har to ressurs-typer (sjåfør + kjøretøy) som må tildeles samtidig. Selve LAHC-akseptanse-kriteriet er agnostisk til løsnings-struktur, men move-operatorene må utformes spesifikt for vår multi-resource-variant — kilden gir ingen veiledning for dét.
- **Benchmark er ikke ressurs-tildeling:** TSP er sekvenseringsproblem; Exam Timetabling er tildelingsproblem mellom eksamener og timeslots/rom. Ingen er en direkte parallel til driver+vehicle assignment. LAHC-resultatene fra benchmarkene kan ikke uten videre ekstrapoleres til vårt forventede ytelses-bilde.
- **Ingen menneske-i-løkka-betraktning:** Kilden er ren algoritme-litteratur. Den sier ingenting om forklarbarhet, override-mekanismer eller koordinator-tillit. For Ch 2.2 / Ch 5.2-koblingen må en HITL-kilde (Parasuraman, Lee & See) brukes; LAHC-kilden er taus om hvordan algoritmens output presenteres for en menneskelig bruker.
- **«Single algorithmic parameter»-claimen er litt forenklet:** I praktisk Timefold-konfig kommer LAHC sammen med move-selectors, score-vekter og fase-overganger — det er fortsatt mye som må konfigureres, selv om selve LAHC-fasen har én parameter. Skal ikke siteres som om Timefold er parameter-fritt.
- **Skala-uavhengighet er en perifer egenskap her:** Siden Ressursplanleggers vekter typisk justeres sjelden og innenfor faste rammer, gir scale-independence-egenskapen ikke en stor praktisk fordel for oss. Skal ikke pumpes opp til hovedargument.
- **«Outperforms SA/TA/GDA»-claimen gjelder spesifikke benchmark-cut-offs:** Kilden viser dominans i 100–120 sek-vinduet på testede problemer. Dette kan ikke generaliseres til «LAHC er alltid bedre». Skal kvalifiseres som «på testede problem-klasser, i sammenlignede tids-vinduer».

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Late Acceptance Hill Climbing (LAHC) | "in the Late Acceptance Hill Climbing (LAHC) a candidate is compared with that solution, which was the current several iterations before." | p. 71 |
| Local search | "A family of algorithms, often labeled under the term local search, represents a wide range of techniques, across a broad spectrum of problems." | p. 70 |
| Greedy Hill-Climbing (HC) | "The simplest local search algorithm is the greedy Hill-Climbing (HC) ... HC accepts only candidates with the same or better cost than the current one." | p. 70 |
| Cooling schedule | "T is the control parameter called 'temperature' (its variation is called the cooling schedule)." | p. 70 |
| Metaheuristic (anvendt på LAHC) | "it can be thought of as a general purpose search method, i.e., a metaheuristic. We expect that it can be applied to any problem, where other local search methods (HC, SA, TA, GDA) are applicable." | p. 72 |
| History length Lh | "LAHC can employ its acceptance rule while maintaining a list of a fixed length Lh (history length) of previous values of the current cost function." | p. 71 |
| Scale independence (av LAHC) | "It is not dependent on scales in contrast to cooling-schedule based algorithms." | p. 77 |

## Rammeverk og modeller

### LAHC-algoritmen — kjernerammeverket (s. 71–72)

LAHC presenteres som en utvidelse av greedy HC ved å bytte ut akseptanse-kriteriet. Selve algoritmen er enkel nok til å skrives som ett pseudo-kode-flyt; kilden gir også formel-formen.

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| Initial fitness array | En liste med Lh kopier av initial-løsningens kostnad | `For all k∈(0...Lh-1) fk:=C(s)` (initialiseres med C(s) i hver posisjon) | p. 72 |
| Akseptanse-kriterium | Kandidat aksepteres hvis kostnaden er bedre enn kostnaden Lh iterasjoner siden, eller bedre enn dagens kostnad | Formel 1: `Ci* < Ci-Lh   eller   Ci* ≤ Ci-1` | p. 72 |
| Virtuell start (FIFO-optimalisering) | Indeksen v=i mod Lh brukes til å oppdatere fitness-array uten å flytte elementer | `v := i mod Lh` | p. 72 |
| «Better only»-oppdatering | Fitness-array oppdateres kun når Ci < fv (ikke ved verre verdier) | `If C(s)<fv then update fv:=C(s)` — forhindrer prematur konvergens | p. 72, 75 |
| Stoppe-betingelse | Minimum 100 000 iterasjoner; deretter stopp når «idle»-iterasjoner overstiger 2 % av total | `Iidle reaches 2 percent over the total number of iterations` | p. 72 |
| Lh = 0 eller 1 reduserer LAHC til greedy HC | Spesialtilfelle | — | p. 72 |

### Sammenligning med relaterte metoder (s. 70–71)

| Metode | Akseptanse-kriterium | Kontroll-parameter | Schedule? |
|---|---|---|---|
| Greedy HC | Ci* ≤ Ci | (ingen) | Nei |
| Simulated Annealing (SA) | Probabilistisk: P=exp[(C-C*)/T] | Temperatur T | Cooling schedule |
| Threshold Accepting (TA) | C* − C ≤ T | Threshold T | Schedule |
| Great Deluge (GDA) | C* ≤ B | Level B | Schedule |
| LAHC | Ci* < Ci-Lh eller Ci* ≤ Ci-1 | Historie-lengde Lh | Nei (ingen schedule) |

## Key arguments / lines of reasoning

### Argument: LAHC løser et praktisk problem ved cooling-schedule-baserte metaheuristikker
- **Premiss(er):** (1) SA, TA, GDA krever en cooling schedule som er problem-/instans-avhengig (p. 71). (2) Optimal form er ubestemt og må tunes empirisk per problem (p. 71). (3) LAHC har én parameter (Lh) og ingen schedule (p. 72, 77).
- **Konklusjon:** LAHC er praktisk overlegen når utvikleren ikke har tid eller domene-kunnskap til å tune en cooling schedule.
- **Sted:** p. 71 (svakhet ved cooling), p. 77 (LAHC-fordel)
- **Hvilke claims dette støtter:** Ch 2.1 ¶5 (begrunnelse for hvorfor parameter-fattige metaheuristikker er praktisk attraktive); Ch 4.5 ¶2 (Timefold-valg).

### Argument: Skala-uavhengighet følger fra at LAHC er en HC-utvidelse
- **Premiss(er):** (1) Greedy HC er trivielt skala-uavhengig fordi akseptanse-kriteriet kun bruker rang-sammenligning. (2) LAHCs akseptanse-kriterium er også rang-basert (sammenligner kandidat med Lh iterasjoner siden, ikke med absolutt nivå). (3) Derfor er LAHC også skala-uavhengig.
- **Konklusjon:** «being an extension of Hill Climbing, LAHC also inherits its scale independence» (p. 76).
- **Sted:** p. 76
- **Hvilke claims dette støtter:** Skala-uavhengighet-claimet (sekundær prioritet for vår thesis).

### Argument: LAHC er praktiker-attraktiv på grunn av lav tuning-kost
- **Premiss(er):** (1) CPU-tid er lineært proporsjonal med Lh (empirisk på TSP U1817, p. 73). (2) Kjenner man Time/Lh-vinkel-koeffisient fra en kort kjøring, kan man kalkulere Lh for et ønsket tids-budsjett (p. 74). (3) Dette gir tids-styring uten å løse et separat parameter-tuning-problem.
- **Konklusjon:** «it can be well-tuned with less effort than most modern metaheuristics. This is especially attractive to practitioners» (p. 77).
- **Sted:** p. 73–74, p. 77
- **Hvilke claims dette støtter:** Ch 4.5 ¶2 — praktisk valg for SME-kontekst hvor solver-tuning er en kostnad bedriften ikke vil bære.

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| TSP benchmark-instanser (Rat783–Fl3795, fra TSPLIB) | LAHC på 7 standard TSP-instanser med 783–3795 byer; sammenligning med SA/TA/GDA i 100–120 sek-vinduet | p. 72, Tabell 1, 3, 7 |
| Exam Timetabling (ITC2007, 12 datasett) | LAHC på ITC2007-konkurransen; sammenligning med SA/TA/GDA | p. 72–73, Tabell 2, 4, 8 |
| Magic Square i International Optimisation Competition 2011 | LAHC-basert algoritme vant 1. plass; SA-forsøk i utviklingsteamet feilet pga. cooling-schedule-tuning | p. 76–77 |
| VeRoLog 2014 (Vehicle Routing kompetanse) | LAHC-metode vant 1. plass | p. 71 |
| OptaPlanner (Red Hat, open source) | LAHC-metoden er innebygget i et bredt brukt planleggings-rammeverk | p. 71 |
| Rasta Converter (GitHub) | LAHC innebygget i et second real-world software system | p. 71 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| LAHC vinner 5/7 TSP-instanser i 100–120 sek-cut-off vs. SA/TA/GDA | (count) | TSPLIB-test | p. 75, Tabell 7 |
| LAHC vinner 6/12 Exam-instanser i 100–120 sek-cut-off | (count) | ITC2007 | p. 75, Tabell 8 |
| CPU-tid med Lh=50000 ≈ 10× CPU-tid med Lh=5000 | ratio | TSP/Exam-eksperimenter | p. 73 |
| LAHC oppnår 100 % suksess på Magic Square 200×200, 1000×1000, 2600×2600 (Lh=20000, 1 min) | (rate) | IOC 2011 | p. 77 |
| SA på Magic Square 1000×1000 feilet i 5 % av kjøringer; 2600×2600 feilet i opp til 62 % | (rate) | IOC 2011-forsøk | p. 76 |
| LAHC er testet på 7 TSP-instanser (783–3795 byer) og 12 Exam Timetabling-datasett | (count) | benchmark-omfang | p. 72–73, Tabell 1, 2 |

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Adaptive Memory Programming | Et bredere paradigme der tidligere søkehistorie informerer nåværende beslutninger; LAHC «can be viewed as a further variant» | p. 77 |
| Iterated Local Search / Memetic Algorithms | Hybride søkemetoder hvor LAHC kunne integreres som forbedring av greedy HC | p. 77 |
| Old Bachelor Acceptance, Weight Annealing | Andre cooling-schedule-baserte aksept-mekanismer i samme familie som GDA | p. 71 |
| Late Acceptance Randomized Descent (Abuhamdah 2010), Multiobjective Late Acceptance (Vancroonenburg & Wauters 2013) | Senere varianter / utvidelser av LAHC | p. 71 |
| Lin-Kernighan «double-bridge» move (1973) | Move-operator brukt i kildens TSP-implementasjon | p. 73 |
| Saturation Degree Graph Coloring (i Exam Timetabling) | Heuristikk brukt for å bygge initialløsning i kildens Exam-implementasjon | p. 73 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "the LAHC approach is simple, easy to implement and yet is an effective search procedure." | p. 70 | Ch 2.1 ¶5 (begrunnelse for praktisk metaheuristikk-valg) |
| "Late Acceptance Hill Climbing (LAHC) ... compared with that solution, which was the current several iterations before." | p. 71 | Definisjon i Ch 2.1 hvis LAHC nevnes eksplisitt |
| "It is dependent on a single algorithmic parameter, which regulates the CPU time." | p. 77 | Ch 4.5 ¶2 (én-parameter-egenskap er praktisk for SME-kontekst) |
| "the developers can substitute HC in existing systems by a stronger search technique with minimum effort." | p. 77 | Ch 4.5 ¶2 (multi-engine-arkitekturens lave merkostnad) |
| "It does not employ the properties of a particular type of problem and, therefore, could be positioned as a general-purpose metaheuristic." | p. 77 | Ch 2.1 ¶4–5 (generalitet av metaheuristikk-tilnærmingen) |
| "the average processing time of runs with Lh = 50000 is approximately 10 times longer than that with Lh = 5000. Based on this, we can propose that the CPU time is linearly dependent on the history length." | p. 73 | Ch 4.5 ¶2 / ¶6 (tidsbudsjett-styring) |
| "OptaPlanner, an open source project by Red Hat" | p. 71 | Bekrefter LAHCs implementasjon i Timefold-forgjengeren |

## Hva kilden IKKE sier

- **Ingen omtale av multi-resource scheduling, driver+vehicle assignment eller transport-domenet.** Kilden er ren algoritme-presentasjon; alle eksempler er TSP, Exam Timetabling, Magic Square. Når writer-agenten siterer LAHC-kilden, må anvendelsen til vårt domene gjøres eksplisitt — kilden støtter ikke direkte at LAHC er en god løsning for *vårt* problem, kun at det er en effektiv generell metaheuristikk.
- **Ingen omtale av Timefold (kun OptaPlanner).** Kilden ble publisert da rammeverket het OptaPlanner; navnet ble endret til Timefold etter at Red Hat avviklet OptaPlanner. Writer-agent må håndtere denne overgangen — kilden bekrefter LAHCs tilstedeværelse i OptaPlanner, ikke direkte i Timefold (selv om det er den samme kodelinjen).
- **Ingen sammenligning med CP-SAT eller andre constraint programming solvers.** Kilden sammenligner kun med andre lokale søk / metaheuristikker (HC, SA, TA, GDA). Påstander om «Timefold vs. CP-SAT» kan ikke støttes herfra.
- **Ingen kommentarer om soft-/hard-constraint-arkitektur eller score-modeller.** Kilden bruker en flat kostnadsfunksjon i sine eksperimenter. Ressursplanleggers BendableScore-modell (hard score + soft score) kan ikke begrunnes med denne kilden.
- **Ingen behandling av menneske-i-løkka, override eller forklarbarhet.** Kilden er taus om brukerinteraksjon med solver-output.
- **Ingen empiri på problemstørrelser tilsvarende Ressursplanlegger (50+ ressurser × 100+ oppdrag).** Kildens største testede problemer (Fl3795 TSP, 2600×2600 Magic Square) har annen struktur og benchmark-mål.
- **Ingen skala-uavhengighet-fordel for små instanser.** Forfatterne sier eksplisitt at SA/TA noen ganger slår LAHC på små instanser (p. 75) — claim om «LAHC alltid best» er feil.

## Forfatter-perspektiv / metodologi

Forfatterne er metaheuristikk-forskere ved Queen Mary University of London (Burke er en sentral skikkelse i timetabling-forskning). Kilden er en metode-introduksjon med eksperimentell validering — ikke en review eller en applied case study. Posisjonen er forfatternes egen metode, så argumentasjonen er begrunnende; sammenligningen med SA/TA/GDA er rettferdig konstruert, men forfatterne har et insentiv til å vise sin egen metode i godt lys. For vårt formål (en kort referanse til LAHC som en av Timefolds metaheuristikker) er dette uproblematisk; for et hovedargument om at LAHC er det objektivt beste valget, ville triangulering med andre kilder vært nødvendig.
