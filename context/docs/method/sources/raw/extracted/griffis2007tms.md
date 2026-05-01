# Transportation Management Systems: An Exploration of Progress and Future Prospects (`griffis2007tms`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Full article read (pp. 18–32). TMS definition, functionality list, gap between motives and realized functions, non-adopter behaviour, and implementation barriers all captured. All areas of interest investigated.
  - **Gaps not investigated:** None — article is 15 pages and read in full.

## Source metadata
- **BibTeX key:** `griffis2007tms`
- **Reference (APA 7):** Griffis, S. E., & Goldsby, T. J. (2007). Transportation management systems: An exploration of progress and future prospects. *Journal of Transportation Management*, *18*(1), 18–32. https://doi.org/10.22237/jotm/1175385780
- **Tilgang:** Open access (DigitalCommons@WayneState)
- **Raw source:** `../griffis2007tms.pdf`
- **Coverage in raw:** Full article, pp. 18–32 (PDF pages 2–16). Page offset: PDF page = printed page − 16.

## Sammendrag (2–3 setninger)

Griffis & Goldsby (2007) survey 45 North American firms on their adoption of, experiences with, and views on transportation management systems (TMS). The article defines TMS as software used to plan, optimise, and execute transportation operations, and documents that the most-used TMS functions centre on shipment-level operational tasks (routing, tracking, scheduling) rather than strategic planning. Its main contribution to this thesis is a citable, widely-used TMS category definition and empirical evidence that commercial TMS focuses on the individual shipment rather than resource-level planning — establishing the gap that Ressursplanlegger fills.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.3 ¶1 (define TMS as software category) | Covered — direct definition on p. 19 |
| Ch 2.3 ¶2 (TMS landscape — what systems do well/lack) | Partial — covers functionality and gaps at the category level; does NOT describe Norwegian systems |
| Ch 2.3 ¶3 (planning gap) | Covered — p. 27 explicitly states TMS focus on individual shipment, not resource optimisation |
| Ch 5.3 (adoption barriers) | Partial — implementation issues section (p. 25) maps to integration and management-resistance barriers |

## Claims this source supports

### Claim: "TMS is software used to plan, optimise, and execute transportation operations"
- **Suggested for:** Ch 2.3 ¶1
- **Direkte sitat:** "Transportation management systems are information technologies used to plan, optimize, and execute transportation operations. A TMS can facilitate transportation management activities that take place before, during, and after the transportation movement by optimizing freight flows among multiple facilities, tracking freight in transit, and managing the freight payment process" (p. 19 / PDF 3)
- **Parafrase:** TMS is a software category covering pre-, during-, and post-transport activities: freight flow optimisation, in-transit tracking, and payment management.
- **Forbehold:** Definition is written from a shipper/freight perspective. "Transportation operations" here means moving goods between facilities, not assigning drivers to jobs within a transport company.
- **Anvendelse på vårt case:** Denne definisjonen etablerer TMS som softwarekategori i Ch 2.3 ¶1; den klargjør samtidig at Timpex og Trimtex (faktureringsfokusert) faller innenfor TMS-kategorien, mens Ressursplanlegger adresserer planleggingsdelen ("before the transportation movement") som kommersielle systemer ikke dekker for norske transportselskaper.

---

### Claim: "Commercial TMS focuses on individual-shipment operations, not multi-resource optimisation"
- **Suggested for:** Ch 2.3 ¶3 (planning gap)
- **Direkte sitat:** "most TMS offerings focus on the individual shipment as the primary unit of analysis, as indicated by the functions most commonly employed by systems in the current study. In fact, many systems do not have the ability to optimize multi-load shipments, making load consolidation a manual activity." (p. 27 / PDF 11)
- **Parafrase:** TMS systems are built around the shipment as the unit of analysis; multi-load or multi-resource optimisation falls outside the standard TMS scope and remains manual.
- **Forbehold:** "Load consolidation" in this source = combining freight from multiple shippers onto one truck; this is not the same as driver+vehicle assignment. The analogy holds structurally (both are multi-resource assignment problems left manual), not literally.
- **Anvendelse på vårt case:** Dette underbygger planleggingsgapet i Ch 2.3 ¶3: Griffis & Goldsby konstaterte allerede i 2007 at TMS-systemer ikke løser multi-ressurs-optimering — sjåfør+kjøretøy-tildeling er nøyaktig den typen problem som faller utenfor det kommersielle TMS-tilbudet, og som Ressursplanlegger fyller.

---

### Claim: "Mismatch between TMS adoption motives (strategic) and realized functionality (operational)"
- **Suggested for:** Ch 2.3 ¶3; Ch 5.3
- **Direkte sitat:** "It is interesting to note that the functionality most commonly realized does not directly overlap with the motives for TMS adoption. While motives tend to speak of high-level strategic concerns, the functions most commonly employed involve support for operations-based decisions, those involving individual shipments and transactions." (p. 25 / PDF 9)
- **Parafrase:** Firms adopt TMS for strategic reasons (consolidation, cost reduction) but end up using it for day-to-day operational tasks; strategic decision-support capabilities often go unrealised.
- **Forbehold:** Specific to freight/shipper context. "Strategic" in this article = network design, lane analysis; not directly comparable to Ressursplanlegger's planning goals.
- **Anvendelse på vårt case:** Mønsteret er gjenkjennelig i norsk transportkontekst: koordinatorer bruker eksisterende systemer (Timpex, Trimtex) til fakturering og ordreregistrering, men planlegging forblir manuell — systemer adopteres for administrative formål, ikke for planleggingsstøtte.

---

### Claim: "System incompatibility is the dominant TMS implementation challenge"
- **Suggested for:** Ch 5.3 ¶3 (integration with billing systems)
- **Direkte sitat:** "The incompatibility of systems, a perennial IT issue, appeared in 57 percent of the implementations reported by TMS users. Delays in the implementation phase of the project were also an issue for one-half of the respondents. Reluctance among the top levels of the firm to adopt a system presented problems for 43 percent of the firms installing a TMS as senior management and executives questioned the need for or value of these systems." (p. 25 / PDF 9)
- **Parafrase:** System incompatibility (57 %), implementation delays (50 %), and management resistance (43 %) are the three leading TMS implementation barriers.
- **Forbehold:** Based on 45 US firms in 2007. Percentage figures should not be presented as current norms; use as illustrative pattern evidence only.
- **Anvendelse på vårt case:** Disse tre barrierene gjenfinnes i Ressursplanleggers adopsjonssituasjon: integrasjon med faktureringssystemer (Timpex/Trimtex) er uløst, ledelsesforankring er avgjørende, og implementeringsforsinkelserrisiko er reell for SMB-ene i utvalget. Kan brukes som støtte for adopsjonsdiskusjonen i Ch 5.3, men som kontekstuell parallell — ikke som direkte empiri om norske forhold.

---

### Claim: "Half of non-TMS users manage transportation manually"
- **Suggested for:** Ch 2.3 ¶2 (background on manual practices) or Ch 5.3
- **Direkte sitat:** "Another 50 percent of non-users reported performing their transportation management activities manually rather than with a TMS." (p. 26 / PDF 10)
- **Parafrase:** Among firms without a TMS, 50 % manage transportation manually, relying on no dedicated software.
- **Forbehold:** US context, 2007. "Transportation management activities" here means freight management (routing, booking carriers), not driver scheduling.
- **Anvendelse på vårt case:** Passer som kontekstuelt bakteppe for at manuell planlegging er utbredt — men dette er kun støttebevis; primær empiri for manuell planlegging i norsk transportsektor er egne intervjufunn (interviews-summary.md Theme 1).

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Transportation management system (TMS) | TMS (samme term, bredere) | Kilden bruker for fraktstyring; vår thesis bruker for planleggingssystemer inkl. Ressursplanlegger |
| Shipper | Transportselskap / oppdragsgiver | Kildens "shipper" = selskapet som sender gods; i vår kontekst = transportselskapet selv |
| Carrier | Transportselskap / sjåfør (delvis) | Kildens "carrier" = tredjeparts fraktfører; i vår kontekst er sjåfør+kjøretøy = ressursen som tildeles |
| Shipment | Oppdrag | Kildens analyseenhet; i vår thesis = oppdrag (assignment) med fast tid og sted |
| Shipment routing | Oppdragstildeling (delvis analogt) | Kilden: hvilken rute å ta; vår thesis: hvilken sjåfør/kjøretøy som utfører oppdraget — ulik semantikk |
| Load consolidation | (Ingen direkte ekvivalent) | Kilden: slå sammen forsendelser på én bil; vår thesis: multi-ressurs-tildeling — strukturelt likt, semantisk ulikt |
| Freight payment process | Fakturering | Kildens "payment" = fraktfaktura; dette er det eksisterende norske systemer (Timpex, Trimtex) allerede dekker |
| Decision support (operational) | Planleggingsstøtte | Overlappende konsept — begge handler om operasjonell beslutningsstøtte for transportaktiviteter |

## Forbehold og begrensninger

- **Feil domene for direkte bruk:** Kilden handler om fraktstyring fra et avsenderperspektiv (gods fra A til B), ikke om tildeling av sjåfør+kjøretøy til oppdrag. "Transportation management" i kilden er ikke det samme som "ressursplanlegging" i vår thesis. Definisjonen (p. 19) kan siteres for å etablere TMS-kategorien, men kan ikke brukes til å si noe om hva Ressursplanlegger gjør eller ikke gjør.
- **Utdatert (2007):** TMS-markedet har endret seg betydelig siden 2007. Markedsandeler, adopsjonsrater og funksjonslistene i kilden er ikke representative for 2026-situasjonen. Statistikk fra kilden bør ikke presenteres som gjeldende fakta.
- **US-kontekst:** 45 nordamerikanske selskaper. Norsk regulatorisk kontekst (kjøre-og-hviletid, tariffavtaler, HMS-krav) er ikke dekket.
- **Ingen dekning av norske systemer:** Kilden nevner ikke Timpex, Trimtex, Opptur eller lignende norske systemer. Ch 2.3 ¶2 (TMS-landskapet i Norge) må støttes av andre kilder (intervjufunn, fitgap-summary.md).
- **MUST CITE-marker i Ch 2.3 ¶1 bekreftet:** Kilden støtter definisjonsformålet i ¶1. ✓
- **MUST CITE-marker i Ch 2.3 ¶1 for heinbach2022datadriven:** Den andre ¶1-kilden (heinbach2022datadriven) er ikke denne kilden — de to siteres side om side.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Transportation Management System (TMS) | "Transportation management systems are information technologies used to plan, optimize, and execute transportation operations." | p. 19 / PDF 3 |
| Collaborative Transportation Management (CTM) | "a holistic process that brings together supply chain trading partners and service providers to drive inefficiencies out of the transport planning and execution process" (Sutherland, Goldsby and Stank, 2004, cited p. 27) | p. 27 / PDF 11 |

## Rammeverk og modeller

### TMS Decision Support Hierarchy (Figure 4, p. 27 / PDF 11)

Hierarkisk modell fra strategisk til operasjonelt (figur tilpasset fra Stank and Goldsby, 2000):

| Nivå | Beslutningstype | TMS-funksjonalitet | Side |
|---|---|---|---|
| 1 (mest strategisk) | Total network and lane design | Optimization for inbound, outbound and international freight; CTM support | p. 27 / PDF 11 |
| 2 | Mode/carrier selection | Automated carrier selection | p. 27 / PDF 11 |
| 3 | Service negotiations | Connections to transportation exchanges for carrier availability and pricing | p. 27 / PDF 11 |
| 4 | Service evaluation | Carrier compliance reports and analysis | p. 27 / PDF 11 |
| 5 (mest operasjonelt) | Dock level and over-the-road decisions | Automated load building and tendering; freight processing; dynamic routing; EDI | p. 27 / PDF 11 |

**Notat:** Primærfokus for eksisterende TMS-brukere er nivå 5 (operasjonelt). Rammeverket illustrerer at planleggingsstøtte (nivå 1–2) forblir underutviklet. Nyttig som bakteppe for Ch 2.3, men må ikke overføres direkte til Ressursplanlegger-kontekst — vår "planlegging" er sjåførtildeling, ikke nettverksdesign.

## Key arguments / lines of reasoning

### Argument: Adopsjonsmotiver og realisert funksjonalitet samsvarer ikke
- **Premiss 1:** Firmaer adopterer TMS primært for strategiske formål (konsolidering, kostnadsreduksjon).
- **Premiss 2:** De funksjonene som faktisk brukes mest er operasjonelle (rutevalg, sporing, planlegging av enkeltforsendelser).
- **Konklusjon:** "The strategic objectives cannot find achievement without sufficient control at the operation level. However, review of open-ended responses suggested that the systems' promised capabilities of strategic decision support went largely unfulfilled as priorities changed or software proved ineffective in high-level analyses." (p. 28 / PDF 12)
- **Sted:** (pp. 25, 28 / PDF 9, 12)
- **Hvilke claims dette støtter:** Ch 2.3 ¶3 (planning gap); Ch 5.3 (adoption barriers)

### Argument: Manual planning persists among non-adopters
- **Premiss:** Firms that do not use TMS either rely on legacy IT or perform transportation management manually.
- **Konklusjon:** Manual management remains widespread; "Not a priority" and system integration concerns are primary reasons for non-adoption.
- **Sted:** (p. 26 / PDF 10)
- **Hvilke claims dette støtter:** Ch 2.3 ¶2 (background on manual practices)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Deloitte & Touche (2003) survey: 84% of global manufacturers rate supply chain performance "average" to "poor" | Driving motivation for supply chain IT adoption | p. 18 / PDF 2 |
| ARC: TMS investments doubled from US$468M (1998) to US$956M (2005) | TMS adoption growth as context | p. 19 / PDF 3 |
| Figure 3 (most common TMS functions): Shipment Routing 89%, Shipment Tracking 83%, Shipment Scheduling 78% | Operational focus of TMS; planning functions ranked 3rd | p. 24 / PDF 8 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 89% bruker shipment routing | % av TMS-adopterende firmaer | 2007, 45 US-firmaer | p. 24 / PDF 8 |
| 83% bruker shipment tracking | % av TMS-adopterende firmaer | 2007, 45 US-firmaer | p. 24 / PDF 8 |
| 50% av TMS-brukere outsourcer systemet (ASP) | % av TMS-adopterende firmaer | 2007, 45 US-firmaer | p. 24 / PDF 8 |
| 57% opplevde systeminkompabilitet som implementeringsproblem | % av TMS-implementeringer | 2007, 45 US-firmaer | p. 25 / PDF 9 |
| 43% hadde motstand fra ledelsen | % av TMS-implementeringer | 2007, 45 US-firmaer | p. 25 / PDF 9 |
| 50% av ikke-brukere planlegger manuelt | % av non-TMS-firmaer | 2007, 45 US-firmaer | p. 26 / PDF 10 |

**Merk:** Alle tall fra 2007-undersøkelse med 45 US-selskaper. Bruk kun som kontekstuell illustrasjon, ikke som gjeldende statistikk.

## Forfatter-perspektiv / metodologi

Exploratory survey study (N=45, US, 2007). Metodisk svak for statistisk inferens (lav responsrate 4%), men rik på kvalitative åpne svar. Forfatterne anerkjenner begrensningen og posisjonerer arbeidet eksplisitt som preliminær/deskriptiv analyse. Kildekritisk poeng: statistikk fra kilden bør ikke brukes som representative estimater — de fungerer som illustrasjon av mønster.