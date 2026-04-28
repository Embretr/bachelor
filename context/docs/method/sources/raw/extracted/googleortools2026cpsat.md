# Constraint Optimization (Google OR-Tools documentation) (`googleortools2026cpsat`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Source is the official OR-Tools documentation page for constraint optimisation / CP-SAT. The relevant areas of interest for this thesis are (i) what CP and CP-SAT are, (ii) what kinds of problems they are suited for (employee scheduling, job-shop), (iii) the modelling pattern of hard constraints + objective function over integer variables, and (iv) the reported solver-status semantics (OPTIMAL / FEASIBLE / INFEASIBLE / UNKNOWN incl. time limit). All four are covered explicitly in the document. The remaining bulk of the page is per-language code listings (Python / C++ / Java / C#) of the same nurse-scheduling and `x != y` examples — these are illustrative only and contain no further conceptual claims.
  - **Gaps not investigated:** The deep code listings duplicated across four languages were skimmed but not deep-read line-by-line; they restate the same model in different syntax and add no new claims relevant to the thesis. Sections internal to OR-Tools (MPSolver, original CP solver, vehicle routing library) are referenced as adjacent tools but are out of scope for this thesis.

## Source metadata
- **BibTeX key:** `googleortools2026cpsat`
- **Reference (APA 7):** Google OR-Tools. (2026). *Constraint Optimization*. https://developers.google.com/optimization/cp (urldate: 2026-04-28)
- **Tilgang:** open (Google developer documentation)
- **Raw source:** `../googleortools2026cpsat.md` (Markdown fallback — no PDF; this is a web documentation page captured to MD)
- **Coverage in raw:** Pages bundled in the raw MD file: "Constraint Optimization" (overview), "Employee Scheduling" (nurse-scheduling example, with and without shift requests), and "CP-SAT Solver" (feasibility example with `x != y`, return-value semantics, finding all solutions). The MD has no page numbers; locator is the section heading. The file also contains some near-duplicate content (the "CP-SAT Solver" page appears twice — once around line 3156 and again around line 4050; the earlier appears to be a sub-page version, the later the full page). Quotes below are taken from the canonical first occurrence.

## Sammendrag (2–3 setninger)
Kilden er Googles offisielle OR-Tools-dokumentasjon for *constraint optimization* / CP-SAT-løseren. Den definerer constraint programming (CP) som en metode for å identifisere løsninger som tilfredsstiller vilkårlige begrensninger, posisjonerer CP-SAT som Googles primære CP-løser (basert på SAT-teknikker), og illustrerer modelleringsmønsteret for skiftplanlegging der harde betingelser (hver vakt dekkes av nøyaktig én sykepleier; ingen sykepleier har mer enn én vakt per dag) kombineres med en lineær mål-funksjon (maksimer antall innfridde skiftønsker). Hovedbidraget til oppgaven er normativ: det dokumenterer at *employee scheduling* og *job shop* er kanoniske CP-SAT-domener, og fungerer som primærkilde for å rettferdiggjøre valget av CP-SAT som en av Ressursplanleggers løsermotorer.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.1 ¶3 (hard/soft constraints, CP foundations) | covered (eksplisitt modellering med harde betingelser + lineær mål-funksjon i nurse-scheduling-eksempelet) |
| Ch 2.1 ¶4 (NP-hardness, multi-engine motivation) | partial (kilden viser kombinatorisk eksplosjon (24⁷ ≈ 4.5 mrd) som motivasjon for CP, men sier ikke "NP-hard" eksplisitt — bruk Pinedo eller Rossi for NP-hardhet) |
| Ch 2.1 ¶5 (solver comparison: CP-SAT) | covered (CP-SAT som Googles primære CP-løser, statussemantikk inkl. tidsavbrudd) |
| Ch 4.5 ¶2 (chosen approach: CP-SAT) | covered (primærkilde for CP-SAT-eksistens, scope, og kanoniske bruksområder) |
| Ch 4.5 ¶3–4 (constraints og objective function modelling) | covered (eksplisitt eksempel på `add_exactly_one`, `add_at_most_one`, lineære grenser, og `model.maximize(...)`) |

## Claims this source supports

### Claim: "CP-SAT is Google's primary OR-Tools solver for constraint programming, using SAT (satisfiability) techniques together with CP methods"
- **Suggested for:** Ch 2.1 ¶5 (solver comparison); Ch 4.5 ¶2 (chosen approach justification)
- **Direkte sitat:** "The next section describes the CP-SAT solver, the primary OR-Tools solver for constraint programming. (SAT stands for **satisfiability** : the solver uses techniques for solving SAT problems along with CP methods.)" (§"Constraint Optimization" → "Examples")
- **Parafrase:** OR-Tools' anbefalte verktøy for constraint-programmering-problemer er CP-SAT-løseren, som kombinerer SAT- og CP-teknikker.
- **Forbehold:** Dette er en posisjonering fra Googles egen dokumentasjon — det er ikke en uavhengig sammenligning av CP-løsere. For benchmarking-claim mot andre CP-løsere, se Perron & Didier (2023).
- **Anvendelse på vårt case:** Ressursplanlegger bruker CP-SAT som én av tre løsermotorer; denne kilden er primærreferansen for hva CP-SAT *er* (SAT+CP-hybrid fra Google), brukt sammen med Perron & Didier (2023) som dokumenterer CP-SAT-LP-utvidelsen som vant MiniZinc Challenge 2022.

### Claim: "Constraint programming is feasibility-driven (find a solution that satisfies the constraints) rather than objective-driven; a CP problem may not even have an objective function"
- **Suggested for:** Ch 2.1 ¶3 (hard vs soft constraints); Ch 2.1 ¶5 (CP foundations); Ch 4.5 ¶3 (constraints modelled)
- **Direkte sitat:** "CP is based on *feasibility* (finding a feasible solution) rather than optimization (finding an optimal solution) and focuses on the constraints and variables rather than the objective function. In fact, a CP problem may not even have an objective function --- the goal may be to narrow down a very large set of possible solutions to a more manageable subset by adding constraints to the problem." (§"Constraint Optimization", innledning)
- **Parafrase:** CP-paradigmet er sentrert rundt feasibility — det å finne tilstander som tilfredsstiller alle begrensninger — og ikke nødvendigvis rundt optimering av en mål-funksjon.
- **Forbehold:** Skillet er paradigmatisk; CP-SAT *kan* gjøre optimering når en `Maximize` / `Minimize`-objektiv er gitt (se neste claim). Dette claimet rettferdiggjør CP-modellets *fokus*, ikke at optimering er fraværende.
- **Anvendelse på vårt case:** Ressursplanleggers harde betingelser (kompetanse, tilgjengelighet, ingen dobbeltbooking, kjøretøytype) er feasibility-betingelser i CP-forstand — et planforslag uten brudd er gyldig før noen mål-funksjon legges på toppen; dette er det modelleringsskille som gjør CP-SAT egnet over rene LP-formuleringer.

### Claim: "CP problems can be modeled with a linear objective function over integer decision variables, and the solver maximises (or minimises) it; CP-SAT works only over integers"
- **Suggested for:** Ch 4.5 ¶4 (objective function); Ch 2.1 ¶3 (soft constraints implemented as weighted objective)
- **Direkte sitat:** "We want to optimize the following objective function. […] `model.maximize(sum(shift_requests[n][d][s] * shifts[(n, d, s)] for n in all_nurses for d in all_days for s in all_shifts))` […] Since `shift_requests[n][d][s] * shifts[(n, d, s)]` is 1 if shift `s` is assigned to nurse `n` on day `d` *and* that nurse requested that shift (and 0 otherwise), the objective is the number shift of assignments that meet a request." (§"Scheduling with shift requests" → "Objective for the example")
- **Direkte sitat (integer-restriction):** "To increase computational speed, the CP-SAT solver works over the integers. This means you must define your optimization problem using integers only. If you begin with a problem that has constraints with non-integer terms, you need to first multiply those constraints by a sufficiently large integer so that all terms are integers." (§"CP-SAT Solver", note)
- **Parafrase:** CP-SAT modellerer myke preferanser ved å multiplisere preferanse-vekter med Boolske beslutningsvariabler og maksimere summen; alle tall i modellen må være heltall (kontinuerlige verdier må skaleres).
- **Forbehold:** Heltalls-restriksjonen er en konkret modelleringsbegrensning som Ressursplanlegger må håndtere (vekter må skaleres til heltall før de sendes til CP-SAT). Den er ikke en *teoretisk* begrensning på CP, men en implementasjonsdetalj for ytelsens skyld.
- **Anvendelse på vårt case:** Ressursplanleggers myke betingelser (jevn arbeidsbelastning, sjåførpreferanser, oppdragsprioritet) implementeres som vektede ledd i CP-SAT-objektivet etter samme mønster som `shift_requests * shifts` her — dette er den kanoniske måten å gjøre "soft constraints" på i CP-SAT, og rettferdiggjør Ressursplanleggers konfigurerbare vekter (jf. `context/docs/tech/algorithm.md`).

### Claim: "Employee scheduling is a canonical application of CP, characterised by combinatorial explosion that makes brute-force enumeration impractical; CP narrows the search by tracking which solutions remain feasible as constraints are added"
- **Suggested for:** Ch 2.1 ¶1 (define scheduling — analogous domains); Ch 2.1 ¶4 (motivation for heuristic/CP approach over exhaustive search); Ch 4.5 ¶2 (chosen approach)
- **Direkte sitat:** "An example of a problem that is well-suited for CP is **employee scheduling** . The problem arises when companies that operate continuously --- such as factories --- need to create weekly schedules for their employees. Here's a very simplified example: a company runs three 8-hour shifts per day and assigns three of its four employees to different shifts each day, while giving the fourth the day off. Even in such a small case, the number of possible schedules is huge: each day, there are `4! = 4 * 3 * 2 * 1 = 24` possible employee assignments, so the number of possible weekly schedules is 24^7^, which is over 4.5 billion." (§"Constraint Optimization", innledning)
- **Direkte sitat (forts.):** "The CP method keeps track of which solutions remain feasible when you add new constraints, which makes it a powerful tool for solving large, real-world scheduling problems." (§"Constraint Optimization", innledning)
- **Parafrase:** Selv små skiftplanleggingsinstanser har milliarder av mulige løsninger; CP-paradigmet gjør problemet håndterbart ved å kontinuerlig redusere det feasible søkerommet etter hvert som betingelser legges til.
- **Forbehold:** Eksempelet er en "very simplified" sykepleier-/fabrikkinstans uten ressurs-til-ressurs-binding (ingen kjøretøy). For å forsvare valget av CP-SAT for *vår* bi-ressurs-variant (sjåfør + kjøretøy) bør kombinatorisk-eksplosjon-argumentet suppleres med Pinedo (2016) eller Rossi et al. (2006). Kilden sier ikke "NP-hard".
- **Anvendelse på vårt case:** Skala-argumentet overføres direkte: Ressursplanleggers tildelingsproblem (sjåfør × kjøretøy × oppdrag) har større kombinatorikk enn nurse-scheduling-eksempelet fordi to ressurser bindes per oppdrag — dette begrunner valget av CP-SAT (som propagerer betingelser smartere enn ren MIP) for instanser opp mot 500 oppdrag.

### Claim: "CP-SAT returns one of five status values (OPTIMAL, FEASIBLE, INFEASIBLE, MODEL_INVALID, UNKNOWN) where UNKNOWN occurs when a time limit, memory limit, or custom limit stops the solver before optimality is proven"
- **Suggested for:** Ch 2.1 ¶5 (CP-SAT "complete solver with configurable time limit, near-optimal for ≤500 assignments"); Ch 4.5 ¶5 (known limitations); Ch 4.5 ¶6 (benchmarking — interpretation of solver output)
- **Direkte sitat:** "The CP-SAT solver returns one of the status values shown in the table below. […] `OPTIMAL`: An optimal feasible solution was found. `FEASIBLE`: A feasible solution was found, but we don't know if it's optimal. `INFEASIBLE`: The problem was proven infeasible. `MODEL_INVALID`: The given CpModelProto didn't pass the validation step. […] `UNKNOWN`: The status of the model is unknown because no solution was found (or the problem was not proven INFEASIBLE) before something caused the solver to stop, such as a time limit, a memory limit, or a custom limit set by the user." (§"CP-SAT Solver" → "CP-SAT return values")
- **Parafrase:** CP-SAT skiller eksplisitt mellom *bevist optimalt*, *bare feasible*, *bevist infeasible*, og *avbrutt før konklusjon*; sistnevnte håndteres med konfigurert tidsavbrudd.
- **Forbehold:** Statusene er API-konstrater, ikke teoretiske egenskaper. Påstanden om "near-optimal within time limit" som spine bruker, er en *praktisk observasjon* som dokumentasjonen støtter via at FEASIBLE eksisterer som returverdi; det presise gapet mellom FEASIBLE-løsning og optimal-løsning rapporteres ikke her (Perron & Didier (2023) gir benchmark-tall).
- **Anvendelse på vårt case:** Ressursplanleggers benchmarking må rapportere CP-SAT-statusen for hver instans (OPTIMAL vs FEASIBLE vs UNKNOWN ved tidsavbrudd) — denne semantikken er det Ch 4.5 ¶6 må bygge på når man tolker hvorfor noen instanser når optimal og andre stopper med beste-foreløpige-løsning.

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| nurse / employee | sjåfør (driver) — og indirekte kjøretøy (vehicle) | Kilden modellerer én ressurstype per oppdrag (én sykepleier per vakt). Vårt problem binder *to* ressurser (sjåfør + kjøretøy) per oppdrag, så modellen må utvides — dette dokumenteres i `context/docs/tech/algorithm.md`. |
| shift | oppdrag (assignment) | I CP-SAT-modellen er `shifts[(n, d, s)]` en boolsk beslutningsvariabel "denne nurse jobber denne vakten denne dagen"; i Ressursplanlegger blir det `assigned[(driver, vehicle, assignment)]`. |
| shift request | sjåførpreferanse / oppdragsprioritet (myk betingelse) | Kildens vekter er 0/1 ("ønsker" / "ønsker ikke"); Ressursplanlegger bruker konfigurerbare heltallsvekter. |
| feasibility / feasible solution | gyldig plan (ingen brudd på harde betingelser) | "Feasibility" i CP = "ingen avvik" i Ressursplanlegger-terminologi. |
| `model.maximize(...)` / objective function | mål-funksjon / soft score | Sumformulering med vektede Boolske ledd er det mønsteret Ressursplanleggers `context/docs/tech/algorithm.md` følger. |
| OPTIMAL / FEASIBLE / UNKNOWN status | løsersluttstatus | Brukes direkte i benchmarking — ingen oversettelse nødvendig. |
| time limit / memory limit | konfigurerbart tidsavbrudd | Avgjørende for at CP-SAT kan brukes interaktivt: koordinatoren venter ikke 1 time på en bevist optimal løsning når en god FEASIBLE-løsning på 30 sekunder er nok. |

### Begrensninger i applikasjon

- Kilden er **dokumentasjon for en programvare-API**, ikke et akademisk arbeid. Den kan siteres som primærkilde for hva CP-SAT *er* og hvordan den *brukes*, men ikke for teoretiske påstander om CP-paradigmets formelle egenskaper (NP-hardness, kompleksitetsklasser, optimalitetsgaranti). Bruk Pinedo (2016) eller Rossi et al. (2006) for slike påstander.
- Eksempelet er **enkeltressurs-tildeling** (sykepleier → vakt). Ressursplanleggers problem er **multi-ressurs** (sjåfør + kjøretøy → oppdrag). Argumentet om at CP-SAT er egnet overføres, men ressurs-til-ressurs-binding (sjåfør X *trenger* kjøretøy Y) er ikke modellert i kildens eksempler.
- Eksempelet er **homogent i tid** (3 likeverdige skift per dag). Ressursplanleggers oppdrag har **fastsatte tidsvinduer** (start- og slutt-tid for hvert oppdrag) som krever interval-variabler / `NoOverlap`-betingelser — dette er CP-SAT-funksjonalitet som finnes, men ikke vises i den nedlastede dokumentasjonsbiten.
- Skala-eksempelet (24⁷ ≈ 4.5 mrd) er **mye mindre** enn norske transportflåter (50–500 oppdrag, 50+ sjåfører, 50+ kjøretøy) — argumentet om kombinatorisk eksplosjon overføres a fortiori, men man kan ikke sitere kilden for et konkret skala-tall som er relevant for Ressursplanlegger.
- Kilden bruker **integer-only**-modellering. Ressursplanleggers vekter er konfigurerbare heltall; eventuelle brøkvekter må skaleres. Dette må noteres i Ch 4.5 ¶3 hvis vektene bruker desimaltall internt.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Constraint optimization / constraint programming (CP) | "**Constraint optimization** , or **constraint programming** (CP), is the name given to identifying feasible solutions out of a very large set of candidates, where the problem can be modeled in terms of arbitrary constraints." | §"Constraint Optimization", innledning |
| CP — paradigmatisk fokus | "CP is based on *feasibility* (finding a feasible solution) rather than optimization (finding an optimal solution) and focuses on the constraints and variables rather than the objective function." | §"Constraint Optimization", innledning |
| CP-SAT solver | "[The] CP-SAT solver, the primary OR-Tools solver for constraint programming. (SAT stands for **satisfiability** : the solver uses techniques for solving SAT problems along with CP methods.)" | §"Constraint Optimization" → "Examples" |
| Employee scheduling | "**employee scheduling** . The problem arises when companies that operate continuously --- such as factories --- need to create weekly schedules for their employees." | §"Constraint Optimization", innledning |
| Solution printer (callback) | "a callback that you pass to the solver, which displays each solution as it is found." | §"CP-SAT Solver" → "Finding all solutions" |

## Rammeverk og modeller

### CP-SAT solver-status (5 verdier) (§"CP-SAT Solver" → "CP-SAT return values")

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| `OPTIMAL` | En optimal feasibel løsning er funnet | "An optimal feasible solution was found." | §"CP-SAT Solver" → "CP-SAT return values" |
| `FEASIBLE` | En feasibel løsning er funnet, men optimalitet er ikke bevist | "A feasible solution was found, but we don't know if it's optimal." | samme |
| `INFEASIBLE` | Problemet er bevist infeasibelt | "The problem was proven infeasible." | samme |
| `MODEL_INVALID` | Modellen passerte ikke validering | "The given CpModelProto didn't pass the validation step." | samme |
| `UNKNOWN` | Løseren stoppet (tids- / minne- / brukerlimit) før konklusjon | "no solution was found (or the problem was not proven INFEASIBLE) before something caused the solver to stop, such as a time limit, a memory limit, or a custom limit set by the user." | samme |

### Modelleringsmønster: harde betingelser + lineær mål-funksjon (§"Scheduling with shift requests")

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| Beslutningsvariabel | Boolsk variabel `shifts[(n,d,s)]` = 1 hvis sykepleier *n* jobber vakt *s* dag *d* | `shifts[(n, d, s)] = model.new_bool_var(...)` | §"A nurse scheduling problem" → "Create the variables" |
| Hard betingelse: hver vakt har nøyaktig én sykepleier | `model.add_exactly_one(...)` over alle sykepleiere for hver (dag, vakt) | "for each shift, the sum of the nurses assigned to that shift is 1" | §"A nurse scheduling problem" → "Assign nurses to shifts" |
| Hard betingelse: hver sykepleier maks én vakt per dag | `model.add_at_most_one(...)` over alle vakter for hver (sykepleier, dag) | "For each nurse, the sum of shifts assigned to that nurse is at most 1" | samme |
| Hard betingelse: jevn fordeling | Lineær grense `min_shifts_per_nurse <= sum(shifts_worked) <= max_shifts_per_nurse` | "ensures that no nurse is assigned more than one extra shift" | §"Assign shifts evenly" |
| Mål-funksjon (myk preferanse) | `model.maximize(sum(shift_requests[n][d][s] * shifts[(n,d,s)] for ...))` | "the objective is the number shift of assignments that meet a request" | §"Scheduling with shift requests" → "Objective for the example" |

## Key arguments / lines of reasoning

### Argument: CP er feasibility-drevet, ikke optimaliserings-drevet
- **Premiss(er):** (1) CP-paradigmet er definert ved å identifisere feasible løsninger blant et stort kandidat-rom. (2) En CP-modell trenger ikke en mål-funksjon — målet kan være å smalne ned settet av feasible løsninger.
- **Konklusjon:** CP-rammeverket fokuserer på betingelser og variabler først; en mål-funksjon er en valgfri tillegg som forvandler problemet til en optimerings-variant.
- **Sted:** §"Constraint Optimization", innledning
- **Hvilke claims dette støtter:** Ch 2.1 ¶3 (modelleringsskille mellom harde og myke betingelser); Ch 4.5 ¶3 (constraint-modell før objektiv-funksjon)

### Argument: Skiftplanlegging eksploderer kombinatorisk
- **Premiss(er):** (1) Selv et trivielt eksempel med 4 ansatte og 3 skift gir 24 mulige tildelinger per dag. (2) Over en uke blir det 24⁷ ≈ 4.5 mrd. (3) Reelle planleggingsbetingelser (minimum antall arbeidsdager etc.) reduserer settet, men ikke nok til at brute-force er realistisk.
- **Konklusjon:** Planleggingsproblemer trenger en metode (CP) som propagerer betingelser smart i stedet for å enumerere kandidater.
- **Sted:** §"Constraint Optimization", innledning
- **Hvilke claims dette støtter:** Ch 2.1 ¶4 (motivasjon for heuristikk/CP framfor eksakt enumerering); Ch 4.5 ¶2 (chosen approach)

### Argument: Heltalls-restriksjon i CP-SAT er en ytelsesoptimalisering, ikke en teoretisk begrensning
- **Premiss(er):** (1) CP-SAT jobber kun over heltall "to increase computational speed". (2) Brukeren må selv skalere ikke-heltallige termer ved å multiplisere med en stor heltallskonstant.
- **Konklusjon:** Modelleringsbyrden er forskjøvet til brukeren for å holde løseren rask.
- **Sted:** §"CP-SAT Solver", note
- **Hvilke claims dette støtter:** Ch 4.5 ¶3 (constraints modelled — heltalls-skalering); Ch 4.5 ¶5 (known limitations)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Nurse scheduling: 4 sykepleiere, 3 dager, 3 skift/dag | Modellering av harde betingelser (én sykepleier per skift, maks ett skift per dag) + jevn fordeling som lineær grense | §"A nurse scheduling problem" |
| Nurse scheduling med shift requests: 5 sykepleiere, 7 dager, 3 skift/dag | Modellering av myke preferanser via vektet mål-funksjon (`Maximize sum(request × assigned)`) | §"Scheduling with shift requests" |
| `x != y` over {0,1,2}³ | Minimal CP-modell + statussemantikk (OPTIMAL) + alle-løsninger-via-callback | §"CP-SAT Solver" → "Example: finding a feasible solution" og "Finding all solutions" |
| Job shop problem | Nevnt som klassisk CP-SAT-egnet problem (lenke videre, ikke utdypet på denne siden) | §"Constraint Optimization" → "Examples" |
| N-queens, cryptarithmetic | Nevnt som klassiske CP-problemer (lenker, ikke utdypet) | §"Constraint Optimization" → "Examples" |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 24⁷ ≈ 4.5 milliarder mulige ukentlige skiftplaner for 4 ansatte / 3 skift / 7 dager | antall mulige planer (kombinatorisk) | illustrasjons-tall, ingen empirisk skala | §"Constraint Optimization", innledning |
| 4! = 24 mulige tildelinger per dag for 4 ansatte / 3 skift | antall tildelinger | samme | samme |
| Number of shift requests met = 13 (out of 20) | resultat fra et konkret kjøretøy-eksempel (5 sykepleiere × 7 dager × 3 skift med 0/1-preferanser) | illustrasjon | §"Scheduling with shift requests", output |

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| MPSolver | OR-Tools' wrapper for lineær-/MIP-løsere; alternativ til CP-SAT for problemer med kontinuerlig lineær struktur. | §"Tools"; §"CP-SAT Solver" innledning |
| Original CP solver | Eldre CP-løser i OR-Tools, brukt internt i routing-biblioteket. | §"Tools" |
| Vehicle routing library | Egen OR-Tools-modul for VRP-problemer; anbefalt fremfor LP for routing. | §"Tools" |
| Linear programming (LP) | Alternativt rammeverk når problemet har lineær mål-funksjon og lineære betingelser. | §"Tools" |
| Job shop problem | Klassisk skjemaproblem som CP-SAT egner seg for. | §"Constraint Optimization" → "Examples" |
| Solution printer / callback | Mekanisme for å enumerere alle feasible løsninger ved å registrere en callback som kalles for hver løsning. | §"CP-SAT Solver" → "Finding all solutions" |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "**Constraint optimization** , or **constraint programming** (CP), is the name given to identifying feasible solutions out of a very large set of candidates, where the problem can be modeled in terms of arbitrary constraints." | §"Constraint Optimization", innledning | Ch 2.1 ¶3 / Ch 4.5 ¶2 — definisjon av CP |
| "An example of a problem that is well-suited for CP is **employee scheduling** ." | §"Constraint Optimization", innledning | Ch 2.1 ¶1 / Ch 4.5 ¶2 — empoyee scheduling som kanonisk CP-problem |
| "CP has been successfully applied in planning, scheduling, and numerous other domains with heterogeneous constraints." | §"Constraint Optimization", innledning | Ch 2.1 ¶3 — CPs anvendelses-bredde |
| "the primary OR-Tools solver for constraint programming. (SAT stands for **satisfiability** : the solver uses techniques for solving SAT problems along with CP methods.)" | §"Constraint Optimization" → "Examples" | Ch 2.1 ¶5 / Ch 4.5 ¶2 — CP-SAT identitet |
| "To increase computational speed, the CP-SAT solver works over the integers." | §"CP-SAT Solver", note | Ch 4.5 ¶3 — heltalls-modellering som modelleringsbegrensning |
| "the objective is the number shift of assignments that meet a request" | §"Scheduling with shift requests" → "Objective for the example" | Ch 4.5 ¶4 — myk preferanse som vektet sum |
| "no solution was found (or the problem was not proven INFEASIBLE) before something caused the solver to stop, such as a time limit, a memory limit, or a custom limit set by the user." | §"CP-SAT Solver" → "CP-SAT return values" | Ch 2.1 ¶5 / Ch 4.5 ¶6 — tidsavbrudd-semantikk |

## Hva kilden IKKE sier

- **NP-hardness:** Kilden viser eksponensiell vekst i søkerom (24⁷) men sier ikke "NP-hard" eksplisitt. Bruk Pinedo (2016) for NP-hardhets-claimet i Ch 2.1 ¶4.
- **Optimalitetsgap / benchmark-tall:** Dokumentasjonen sier *at* CP-SAT kan returnere FEASIBLE før OPTIMAL ved tidsavbrudd, men gir ikke kvantitative gap-estimater. For påstander om "near-optimal within time limit" (spine), bruk Perron & Didier (2023).
- **Multi-ressurs-modellering:** Eksemplene binder én ressurs (sykepleier) til én oppgave (skift). Ressursplanleggers sjåfør+kjøretøy-binding er ikke illustrert her; en sjåfør+kjøretøy-modell må enten utvides til to assignment-arrayer med kobling, eller bruke `AllowedAssignments` / interval-variabler — *dette* dokumenteres ikke i den nedlastede MD-en.
- **Tidsvinduer / interval-variabler:** Eksemplene har symbolske, likeverdige skift uten klokketid. Ressursplanleggers oppdrag har konkrete start-/slutt-tider som krever `IntervalVar` og `NoOverlap` — funksjoner som finnes i CP-SAT men ikke er beskrevet i denne kildens MD-utdrag.
- **Heuristisk vs eksakt natur:** Kilden beskriver CP-SAT som "complete" via SAT-tilnærming, men diskuterer ikke i hvilken grad CP-SAT bruker heuristisk søk under panseret. For dette, se Perron & Didier (2023).
- **Sammenligning med andre løsere:** Ingen sammenligning mot Timefold, Gurobi, CPLEX, eller andre CP-løsere. Ressursplanleggers multi-engine-rasjonale (greedy/CP-SAT/Timefold som tre punkter på ytelse-kvalitets-aksen) må bygges på andre kilder.
- **Soft constraints som distinkt konsept:** Termen "soft constraint" brukes ikke. Kilden modellerer det funksjonelt (vektet objektiv) men presenterer ikke begrepsapparatet "hard vs soft constraints" eksplisitt — for det skillet bruk Rossi et al. (2006) eller Pinedo (2016).

## Forfatter-perspektiv / metodologi

Kilden er **offisiell programvare-dokumentasjon** fra Google for OR-Tools-biblioteket. Den er normativ ("slik bruker du CP-SAT") og illustrativ ("her er et fungerende eksempel"), ikke akademisk eller komparativ. Den kan siteres som primærkilde for hva CP-SAT er og hvordan en CP-SAT-modell ser ut, men ikke for sammenligning med andre løsere eller for teoretiske kompleksitetspåstander. URL-en er hentet 2026-04-28; Google oppdaterer dokumentasjonen jevnlig, så fremtidig versjonsdrift er en mulig kilde til feil — `urldate`-feltet i bib-oppføringen er derfor avgjørende.