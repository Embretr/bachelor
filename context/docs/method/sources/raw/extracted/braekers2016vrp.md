# The Vehicle Routing Problem: State of the Art Classification and Review (`braekers2016vrp`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Article is 14 pages; the thesis uses this source solely as a delimitation reference (Ch 2.1 ¶4). All three functions of this citation — VRP definition, NP-hardness, and the VRP/assignment distinction — are documented with confirmed page references. Full paper read via pdftotext + visual page verification.
  - **Gaps not investigated:** Sections 5.1–5.3 (detailed classification results) are outside the thesis's area of interest. Appendix A (literature table) is irrelevant.

## Source metadata
- **BibTeX key:** `braekers2016vrp`
- **Reference (APA 7):** Braekers, K., Ramaekers, K., & Van Nieuwenhuyse, I. (2016). The vehicle routing problem: State of the art classification and review. *Computers & Industrial Engineering, 99*, 300–313. https://doi.org/10.1016/j.cie.2015.12.007
- **Tilgang:** PDF (paywalled Elsevier; PDF present in raw/)
- **Raw source:** `../braekers2016vrp.pdf`
- **Coverage in raw:** Full article, pp. 300–313. No front matter; PDF page 1 = printed page 300.
- **⚠ BibTeX key warning:** The bib entry in `result/references.bib` has an **empty key** (`@article{,`). The outline uses `\textcite{braekers2016vrp}`. The key must be filled in before compilation: change `@article{,` to `@article{braekers2016vrp,`.

## Sammendrag (2–3 setninger)
Braekers et al. (2016) presenterer en taksonomibasert gjennomgang av 277 VRP-artikler publisert mellom 2009 og 2015, klassifisert etter problemkarakteristika og løsningsmetoder. Kilden definerer det klassiske VRP som et sekvenseringsproblem — å finne minimalkostnadsruter der hvert kjøretøy besøker en mengde kunder og returnerer til depot — og slår fast at VRP er NP-hardt, noe som gjør heuristikker og metaheuristikker til de dominerende løsningsmetodene. For denne avhandlingen brukes kilden utelukkende som demarkasjonskilde: til å forklare hva VRP er, og til å vise at Ressursplanleggers problem (hvem gjør hva) er strukturelt ulikt VRP (i hvilken rekkefølge).

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.1 ¶4 (NP-hardness, VRP as adjacent area) | covered — VRP definition, NP-hardness, delimitation from assignment |
| Ch 2.1 ¶5 (metaheuristics context) | partial — general taxonomy of heuristics vs metaheuristics confirmed |
| Ch 2.1 ¶1 (adjacent domains to scheduling) | partial — VRP as analogous domain mentioned in outline; source does not address staffing/crew scheduling |

## Claims this source supports

### Claim: "VRP is NP-hard; exact algorithms are only efficient for small instances"
- **Suggested for:** Ch 2.1 ¶4 (primary); motivates heuristic approach for large-scale planning
- **Direkte sitat:** "As the VRP is an NP-hard problem (Lenstra & Rinnooy Kan, 1981), exact algorithms are only efficient for small problem instances. Heuristics and metaheuristics are often more suitable for practical applications, because real-life problems are considerably larger in scale (e.g., a company may need to supply thousands of customers from dozens of depots with numerous vehicles and subject to a variety of constraints)." (p. 300)
- **Parafrase:** VRP tilhører klassen NP-harde problemer, der eksakte algoritmer bare er effektive for små instanser; heuristikker og metaheuristikker er bedre egnet for praktiske brukstilfeller i stor skala.
- **Forbehold:** Kilden siterer Lenstra & Rinnooy Kan (1981) for NP-hardhetspåstanden; Braekers et al. viderefører en etablert resultat, de beviser det ikke selv.
- **Anvendelse på vårt case:** NP-hardhet for VRP er et nærliggende resultat — Ressursplanleggers multi-resource assignment-problem er minst like komplekst siden det legger til simultane sjåfør- og kjøretøybindinger på toppen av VRP's rute-bindinger; dette begrunner direkte valget av heuristikk (greedy) og tidsbegrenset eksakt søk (CP-SAT) fremfor garantert-optimal løser.

---

### Claim: "Classical VRP is defined as finding least-cost routes where each customer is visited exactly once and vehicles return to depot"
- **Suggested for:** Ch 2.1 ¶4 (definition basis for the delimitation argument)
- **Direkte sitat:** "The goal of the VRP is to find a set of least-cost vehicle routes such that each customer is visited exactly once by one vehicle, each vehicle starts and ends its route at the depot, and the capacity of the vehicles is not exceeded." (p. 301)
- **Parafrase:** Klassisk VRP handler om å generere minimalkostnadsruter der hvert stoppested besøkes av nøyaktig ett kjøretøy som starter og slutter i depot.
- **Forbehold:** Dette er definisjonen av Capacitated VRP (CVRP) — det enkleste tilfellet. Kilden beskriver mange varianter (VRPTW, VRPPD, MDVRP, osv.) som er mer komplekse.
- **Anvendelse på vårt case:** Definisjonen klargjør den strukturelle skilnaden til Ressursplanlegger: VRP spør «i hvilken rekkefølge skal stopp besøkes», mens Ressursplanlegger spør «hvem (sjåfør + kjøretøy) skal utføre dette oppdraget». Oppdrag i Ressursplanlegger har faste tider og steder — sekvensering er ikke en del av problemet.

---

### Claim: "VRP is explicitly delimited from scheduling/assignment problems"
- **Suggested for:** Ch 2.1 ¶4 (supports the delimitation argument directly)
- **Direkte sitat:** "the decision was made not to include any combined problems, such as inventory routing problems...problems combining routing decisions with scheduling decisions related to other activities such as machine or production scheduling" (p. 301)
- **Parafrase:** Forfatterne ekskluderer eksplisitt problemer som kombinerer ruting med maskin- eller produksjonsplanlegging, da disse representerer to separate, veletablerte problemklasser.
- **Forbehold:** Kilden trekker grensen mellom VRP og maskin/produksjonsplanlegging — dette er en annen type planlegging enn ressursallokering, men viser at VRP-feltet selv anerkjenner at ruting og planlegging/tildeling er distinkte problemklasser.
- **Anvendelse på vårt case:** Støtter direkte avhandlingens poeng om at Ressursplanleggers problem *ikke* er et VRP: VRP-litteraturen selv ekskluderer scheduling-kombinasjoner, og vår oppgave er primært scheduling/assignment (hvem), ikke routing (i hvilken rekkefølge).

---

### Claim: "Metaheuristics dominate VRP solving; classical heuristics get trapped in local optima"
- **Suggested for:** Ch 2.1 ¶5 (context for solver taxonomy — greedy vs metaheuristic)
- **Direkte sitat:** "Laporte (2009) defines classical heuristics as heuristics that do not allow the intermediate solution to deteriorate during the process of finding better (optimal) solutions. As a result, they often get trapped in local optima. Examples include construction heuristics such as the savings algorithm (Clarke & Wright, 1964), and improvement heuristics such as the λ-opt mechanism (Lin, 1965). Metaheuristics, on the other hand, include mechanisms that avoid getting trapped in local optima. Examples are Tabu Search (Glover, 1986) and Simulated Annealing (Kirkpatrick, Gelatt, & Vecchi, 1983)." (p. 302)
- **Parafrase:** Klassiske heuristikker kan bli fanget i lokale optima; metaheuristikker har mekanismer for å unnslippe disse, og dominerer i VRP-litteraturen (71 % av metodene i gjennomgangen).
- **Forbehold:** Klassifikasjonen er på VRP-litteratur, ikke på assignment-problemer. Overførbarheten av det kvantitative dominansforholdet (71 %) til vår kontekst er begrenset — men den konseptuelle distinksjonen mellom greedy/konstruksjonsheuristikk og metaheuristikk er direkte relevant.
- **Anvendelse på vårt case:** Ressursplanleggers greedy-løser er en konstruksjonsheuristikk (rask, men fanges i lokale optima), mens Timefold bruker tabu search og simulated annealing — nøyaktig de metaheuristiske mekanismene kilden nevner. Denne kilden kan brukes til å forankre den konseptuelle distinksjonen mellom solvernivåene i Ch 2.1 ¶5, men `glover1986future` er primærkilden for tabu search.

## Application to our domain

### Terminologi-mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Customer | Oppdrag (assignment) | VRP-kunder er stoppesteder med etterspørsel; våre oppdrag er jobs med faste tid og sted |
| Vehicle | Kjøretøy (vehicle) | Direkte overførbart, men VRP fokuserer på kjøretøyets rute; vi fokuserer på hvem som kjører |
| Route | Rute / arbeidsdag | I VRP = sekvens av stoppesteder; i Ressursplanlegger = sjåførens tildelte oppdrag per dag |
| Depot | Implicit — startpunkt for sjåfør | VRP-depot er eksplisitt; i Ressursplanlegger er dette ikke en modellert enhet |
| Classical heuristic | Greedy-løser | Konstruksjonsheuristikk som stoppes i lokale optima — konseptuell overensstemmelse |
| Metaheuristic | Timefold Solver | Tabu search og simulated annealing i Timefold tilsvarer VRP-litteraturens dominerende metode |
| NP-hard | Gjelder også assignment-problemet | NP-hardhet er etablert for VRP; Ressursplanleggers problem er minst like komplekst |

### Begrensninger i applikasjon

- **Domene:** VRP er et ruteproblem (sekvensering av stoppesteder). Ressursplanlegger er et tildelingsproblem (matching av ressurser til oppdrag). Kilden kan **ikke** brukes til å si noe direkte om assignment-kompleksitet — bare til å etablere det analoge strukturelle forholdet.
- **Skala:** VRP-eksemplene i kilden refererer til distribusjon av varer til kunder. Norsk transportsektor med sjåfør/kjøretøy-tildeling er ikke nevnt. Applikasjon krever eksplisitt brobygging.
- **NP-hardhet:** Kilden siterer Lenstra & Rinnooy Kan (1981) for VRP-NP-hardhet. For å påstå at *Ressursplanleggers* problem er NP-hardt trengs enten et separat argument (reduktion) eller en Pinedo-referanse for scheduling.
- **Metaheuristikk-dominans (71 %):** Gjelder VRP-litteraturen 2009-2015, ikke assignment-litteraturen. Kan ikke brukes som belegg for at metaheuristikker er best for vårt problem — kun som kontekstuell observasjon.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Vehicle Routing Problem (VRP) / CVRP | "The goal of the VRP is to find a set of least-cost vehicle routes such that each customer is visited exactly once by one vehicle, each vehicle starts and ends its route at the depot, and the capacity of the vehicles is not exceeded." | p. 301 |
| Classical heuristic | "heuristics that do not allow the intermediate solution to deteriorate during the process of finding better (optimal) solutions" | p. 302 |
| Metaheuristic | Implisitt: algoritmer med mekanismer som unngår å bli fanget i lokale optima. Eksempler: Tabu Search og Simulated Annealing. | p. 302 |

## Rammeverk og modeller

Kilden presenterer en taksonomi (Table 2) med 5 hoveddimensjoner (type studie, scenariokarakterer, fysiske problemkarakterer, informasjonskarakterer, datakarakterer) for klassifisering av VRP-varianter. Dette rammeverket er **ikke relevant** for avhandlingens bruk av kilden — den siteres som demarkasjonskilde, ikke for taxonomien.

## Key arguments / lines of reasoning

### Argument: VRP krever heuristikker ved reell skala
- **Premiss(er):** VRP er NP-hardt (Lenstra & Rinnooy Kan 1981); reelle problemer er store (tusenvis av kunder, dusinvis av depoter, mange kjøretøy, mange begrensninger).
- **Konklusjon:** Eksakte algoritmer er bare effektive for små instanser; heuristikker og metaheuristikker er bedre egnet for praksis.
- **Sted:** (p. 300)
- **Hvilke claims dette støtter:** Ch 2.1 ¶4 (motiv for heuristikk-valg), Ch 2.1 ¶5 (solver-sammenligning)

### Argument: VRP er strukturelt atskilt fra scheduling/assignment
- **Premiss(er):** VRP handler om å sekvensere ruter til stoppesteder; scheduling og produksjonsplanlegging er separate, veletablerte problemklasser.
- **Konklusjon:** Kombinerte problemer ekskluderes fra VRP-gjennomgangen fordi de representerer to uavhengige domener.
- **Sted:** (p. 301)
- **Hvilke claims dette støtter:** Ch 2.1 ¶4 (demarkasjon mellom VRP og Ressursplanleggers assignment-problem)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Coca-Cola Enterprises, Anheuser-Busch InBev | VRP-programvare brukes industrielt i stor skala | p. 300 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 277 | VRP-artikler klassifisert | 2009–juni 2015 | p. 300 |
| 71.25 % | Andel artikler som bruker metaheuristikker | 2009–2015 | p. 304 |
| 90.52 % | Andel artikler med kapasitetsbegrensede kjøretøy (CVRP-basis) | 2009–2015 | p. 304 |

## Beslektede begreper

| Begrep | Kort beskrivelse | Side |
|---|---|---|
| Capacitated VRP (CVRP) | Grunnvarianten: kjøretøy med kapasitetsbegrensning | p. 301 |
| VRP with Time Windows (VRPTW) | Kunder må besøkes innenfor definerte tidsvinduer | p. 301 |
| Heterogeneous Fleet VRP (HFVRP) | Blanding av kjøretøytyper med ulike kapasiteter | p. 301 |
| Traveling Salesman Problem (TSP) | Enkjøretøys-variant av VRP; envegs runde-tur-problem | p. 302 |
| Tabu Search | Metaheuristikk som unngår lokale optima via forbudsliste | p. 302 |
| Simulated Annealing | Metaheuristikk basert på probabilistisk aksept av dårligere løsninger | p. 302 |

## Nyttige sitater (sortert etter relevans)

| Sitat | Side | Egnet til |
|---|---|---|
| "As the VRP is an NP-hard problem (Lenstra & Rinnooy Kan, 1981), exact algorithms are only efficient for small problem instances. Heuristics and metaheuristics are often more suitable for practical applications, because real-life problems are considerably larger in scale" | p. 300 | Ch 2.1 ¶4 — NP-hardness motivation |
| "The goal of the VRP is to find a set of least-cost vehicle routes such that each customer is visited exactly once by one vehicle, each vehicle starts and ends its route at the depot, and the capacity of the vehicles is not exceeded." | p. 301 | Ch 2.1 ¶4 — VRP definition before delimitation |
| "problems combining routing decisions with scheduling decisions related to other activities such as machine or production scheduling" | p. 301 | Ch 2.1 ¶4 — VRP-feltet anerkjenner at ruting ≠ scheduling |
| "Metaheuristics, on the other hand, include mechanisms that avoid getting trapped in local optima. Examples are Tabu Search (Glover, 1986) and Simulated Annealing (Kirkpatrick, Gelatt, & Vecchi, 1983)." | p. 302 | Ch 2.1 ¶5 — kontekst for Timefold-valg |

## Hva kilden IKKE sier

- **Ingenting om assignment-problemer.** Kilden dekker kun ruting (sekvensering). Den kan ikke brukes til å si at Ressursplanleggers problem er NP-hardt — kun at VRP er det, og at de er analoge.
- **Ingenting om sjåfør-kjøretøy-matching.** VRP antar at kjøretøyet utfører jobben; hvem som *kjører* kjøretøyet er ikke en del av VRP-modellen.
- **Ingenting om norsk transportsektor.** Kilden er generisk ops-research; ingen sektorspesifikke observasjoner for norsk transport.
- **Ingenting om constraint programming.** Kilden klassifiserer eksakte metoder, klassiske heuristikker og metaheuristikker — CP-SAT (Google OR-Tools) nevnes ikke. For CP-begrunnelse, bruk `rossi2006constraint` og `googleortools2026cpsat`.
- **Ingen kvantitative mål på Timefold eller CP-SAT.** Kilden gir statistikk over VRP-litteraturens metodedominans, ikke ytelse for konkrete solvers.
- **MUST CITE-marker i outline for ¶4:** Outline bruker `braekers2016vrp` som demarkasjonskilde i ¶4. Kilden **støtter** dette — VRP er definert (p. 301), NP-hardhet bekreftet (p. 300), og kilden skiller selv VRP fra scheduling (p. 301).

## Forfatter-perspektiv / metodologi

Taxonomisk gjennomgang av VRP-litteraturen. Forfatterne klassifiserer — de bidrar ikke med ny teori om VRP-løsningsmetoder. Kildens verdi for denne avhandlingen er som autoritativ referanse for hva VRP er og at det er NP-hardt, ikke for metodologiske innsikter.