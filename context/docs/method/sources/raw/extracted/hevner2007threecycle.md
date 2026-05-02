# A Three Cycle View of Design Science Research (`hevner2007threecycle`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Article is 6 pages; read in full via pdftotext. All sections (Sections 1–5) covered. All three cycles and the pragmatic science argument captured. No gaps.
  - **Gaps not investigated:** None — full article read.

## Source metadata
- **BibTeX key:** `hevner2007threecycle`
- **Reference (APA 7):** Hevner, A. R. (2007). A Three Cycle View of Design Science Research. *Scandinavian Journal of Information Systems*, *19*(2), 87–92.
- **Tilgang:** Open access (AIS Electronic Library — aisel.aisnet.org)
- **Raw source:** `../hevner2007threecycle.pdf`
- **Coverage in raw:** Full article, pp. 87–92 (PDF pages 2–7; PDF page 1 = AIS cover page). PDF page offset: printed p. N = PDF page N − 85.

## Sammendrag (2–3 setninger)

Hevner presenterer DSR som bestående av tre gjensidig avhengige sykler: Relevance Cycle (binder forskning til problemkonteksten), Rigor Cycle (forankrer forskning i vitenskaplig kunnskapsbase) og Design Cycle (iterativ konstruksjon og evaluering av artefakt). Artikkelen er en kommentar til Iivari (2007) og utdyper rammeverket introdusert i Hevner et al. (2004). Kjerneargumentet er at god DSR krever synergi mellom relevans og strenghet — ikke bare praktisk nytte alene.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.4 ¶1 (DSR-definisjon) | Covered — tre-sykkel-modellen presiserer DSR-strukturen; supplement til hevner2004design |
| Ch 3.1 ¶1 (Metodologi — DSR) | Covered — tre-sykkel-modellen ramme for å beskrive metodikken |
| Ch 3.1 ¶3 (DSR-faser anvendt — tabell) | Covered — tre sykler mappes direkte til prosjektaktiviteter |
| Ch 3.4 ¶2 (Iterativ utvikling) | Partial — Design Cycle beskriver iterativ natur, men ikke sprint-spesifikt |
| Ch 3.5 ¶3 (Systemvaliditet) | Covered — «lab testing before field testing» rettferdiggjør valideringsvalget |
| Ch 5.6 ¶2 (Ikke produksjonsdistribuert) | Covered — Relevance Cycle's field testing = neste steg etter lab-validering |
| Ch 2.4 ¶2 (Hvorfor DSR passer) | Covered — Relevance Cycle og pragmatisk design science |

## Claims this source supports

### Claim: "Design Science Research must embody three identifiable cycles"

- **Suggested for:** Ch 2.4 ¶1 (best fit), Ch 3.1 ¶1, Ch 3.1 ¶3
- **Direkte sitat:** "The Relevance Cycle bridges the contextual environment of the research project with the design science activities. The Rigor Cycle connects the design science activities with the knowledge base of scientific foundations, experience, and expertise that informs the research project. The central Design Cycle iterates between the core activities of building and evaluating the design artifacts and processes of the research. I posit that these three cycles must be present and clearly identifiable in a design science research project." (p. 88 / PDF 3)
- **Parafrase:** Et DSR-prosjekt er identifiserbart som forskning — og ikke rutineutvikling — ved at alle tre sykler er til stede og synlige.
- **Forbehold:** Artikkelen er en kommentar som utdyper hevner2004design; tre-sykkel-modellen ble visuelt presentert allerede i hevner2004design (Figure 1 der), men uten detaljert beskrivelse per sykkel.
- **Anvendelse på vårt case:** De tre syklene strukturerer Ch 3.1-narrativet: Relevance Cycle = 7 intervjuer med norske transportselskaper som identifiserte planleggingsgapet og leverte krav; Rigor Cycle = litteraturgjennomgang av scheduling-teori, HITL-design og CP-modeller; Design Cycle = iterativ sprint-utvikling av Ressursplanlegger med algoritme-benchmarking som feedback.

---

### Claim: "The Relevance Cycle provides requirements and acceptance criteria from the environment"

- **Suggested for:** Ch 3.1 ¶3 (best fit), Ch 2.4 ¶2
- **Direkte sitat:** "the relevance cycle initiates design science research with an application context that not only provides the requirements for the research (e.g., the opportunity/problem to be addressed) as inputs but also defines acceptance criteria for the ultimate evaluation of the research results." (p. 89 / PDF 4)
- **Parafrase:** Relevance Cycle starter DSR ved å hente krav og akseptansekriterier fra den faktiske anvendelseskonteksten — ikke fra forskerens forutantakelser.
- **Forbehold:** Hevner skiller ikke mellom «requirements» (bruker-krav) og «acceptance criteria» (evalueringskriterier) som to separate aktiviteter; begge er del av Relevance Cycle-input.
- **Anvendelse på vårt case:** De syv semi-strukturerte intervjuene (4. mars 2026) er Relevance Cycle-inputet i denne oppgaven: de identifiserte planleggingsgapet (opportunity) og ga MoSCoW-kravene (requirements) som definerer akseptansekriteriene for Ressursplanlegger-evaluering — kravsporing i Ch 3.5 sjekker om artefaktet faktisk oppfyller disse.

---

### Claim: "The Rigor Cycle distinguishes research contributions from routine design"

- **Suggested for:** Ch 2.4 ¶1 (best fit), Ch 3.1 ¶2
- **Direkte sitat:** "It is contingent on the researchers to thoroughly research and reference the knowledge base in order to guarantee that the designs produced are research contributions and not routine designs based upon the application of well-known processes" (p. 90 / PDF 5)
- **Parafrase:** Det er forskerens ansvar å sikre at designvalgene er forankret i vitenskaplig kunnskapsbase — ellers er artefaktet et produkt, ikke en forskningsbidrag.
- **Forbehold:** «Well-known processes» er ikke definert presist; grensen mellom «routine design» og «research contribution» er pragmatisk og kontekstavhengig.
- **Anvendelse på vårt case:** Ressursplanlegger-prosjektet skiller seg fra ordinær TMS-utvikling (Timpex, Opter) nettopp ved Rigor Cycle: algoritme-designvalgene er forankret i scheduling-teori (Pinedo 2016), constraint programming (Rossi et al. 2006) og HITL-litteratur (Parasuraman & Riley 2000) — dette gjør oppgaven til et forskningsbidrag fremfor rutineutvikling.

---

### Claim: "The Design Cycle is the heart of DSR — iterative build-evaluate"

- **Suggested for:** Ch 3.4 ¶2 (best fit), Ch 3.1 ¶3
- **Direkte sitat:** "The internal design cycle is the heart of any design science research project. This cycle of research activities iterates more rapidly between the construction of an artifact, its evaluation, and subsequent feedback to refine the design further." (p. 90 / PDF 5)
- **Parafrase:** Design Cycle itererer raskere enn de to andre syklene: konstruksjon → evaluering → feedback → ny konstruksjon, inntil artefaktet er tilfredsstillende.
- **Forbehold:** «More rapidly» er relativt til Relevance og Rigor Cycles — Hevner impliserer at Design Cycle skjer i kortere iterasjoner enn de to ytre syklene, ikke at det er en rask prosess generelt.
- **Anvendelse på vårt case:** Den iterative algoritmeutviklingen (greedy → CP-SAT → Timefold) over sprints er direkte Design Cycle-arbeid: hvert solver-alternativ ble implementert, evaluert gjennom benchmarking, og resultatene feedet tilbake til neste designbeslutning (algoritmevalg, constraint-vekting, tidsbegrensning). Multiple Design Cycle-iterasjoner skjedde før noen resultater ble outputtet til Relevance Cycle.

---

### Claim: "Artifacts must be tested in laboratory situations before field testing"

- **Suggested for:** Ch 3.5 ¶3 (best fit), Ch 5.6 ¶2
- **Direkte sitat:** "artifacts must be rigorously and thoroughly tested in laboratory and experimental situations before releasing the artifact into field testing along the relevance cycle." (p. 91 / PDF 6)
- **Parafrase:** Lab-testing (eksperimentell) er et nødvendig og legitimt DSR-steg som forutgår field testing i Relevance Cycle.
- **Forbehold:** Hevner definerer ikke presist hva «laboratory situations» betyr operasjonelt — det kan inkludere alt fra benchmarking til strukturerte brukertester med testdata.
- **Anvendelse på vårt case:** Oppgavens valideringstilnærming (benchmarking av algoritmen på syntetiske datasett + kravsporing mot MoSCoW-krav) tilsvarer Hevners «laboratory and experimental situations» — dette er et legitimt og nødvendig DSR-steg, og mangelen på produksjonsdistribusjon (field testing) er ikke en metodisk svakhet, men en planmessig begrensning konsistent med DSR-fasen oppgaven er i.

---

### Claim: "Good DSR requires synergy between relevance and rigor — not practical utility alone"

- **Suggested for:** Ch 2.4 ¶2 (best fit), Ch 3.5 ¶1
- **Direkte sitat:** "it is the synergy between relevance and rigor and the contributions along both the relevance cycle and the rigor cycle that define good design science research." (p. 91 / PDF 6)
- **Parafrase:** Verken praktisk nytte alene (relevant men ikke rigid) eller akademisk stringens alene (rigid men ikke relevant) definerer god DSR — begge er nødvendige.
- **Forbehold:** Hevner gir ingen operasjonelle kriterier for å bedømme om et prosjekt har tilstrekkelig relevans vs. rigor; dette er et normativt standpunkt.
- **Anvendelse på vårt case:** Ressursplanlegger oppnår denne synergien: relevans gjennom direkte engasjement med 7 norske transportselskaper og et fungerende system; rigor gjennom forankring av algoritmedesign i scheduling-teori og HITL-litteratur — ingen av delene alene ville konstituert forskning.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| design artifact | Ressursplanlegger (web-plattform) | Det konstruerte IS-artefaktet |
| application domain | Norske transportselskaper (trafikkoordinator-kontekst) | People + org systems + technical systems |
| environment | Norsk transportsektor — daglig sjåfør/kjøretøy-planlegging | Kontekst krav hentes fra |
| knowledge base | Scheduling-teori (Pinedo), HITL-litteratur, CP-foundations (Rossi), TMS-litteratur | Grunnlag for rigor |
| field testing | Produksjonsdistribusjon (ikke gjennomført) | Neste steg i Relevance Cycle |
| laboratory / experimental testing | Algoritme-benchmarking + kravsporing | Det oppgaven faktisk gjør |
| requirements | Funksjonelle og ikke-funksjonelle krav fra intervjuer (MoSCoW) | Input fra Relevance Cycle |
| acceptance criteria | Benchmarking-målsetninger + kravdekning | Hvordan artefaktet evalueres |
| meta-artifacts | Ressursplanlegger + planleggingsalgoritmen | Design-produkter generert |
| routine design | Eksisterende TMS-systemer (Timpex, Opter) | Det Rigor Cycle skiller oss fra |
| feedback to refine the design | Benchmark-resultater som driver algoritmevalg og constraint-vekting | Iterasjon i Design Cycle |

## Forbehold og begrensninger

- **Kommentar-format, ikke primærkilde:** Artikkelen er et 6-siders kommentar-essay som respons på Iivari (2007). Tre-sykkel-modellen ble visuelt presentert i hevner2004design (Figure 1 der) — hevner2007threecycle er mer detaljert om syklene, men hevner2004design er den primære DSR-referansen. Hvis bare én kilde kan siteres for DSR, er hevner2004design riktig valg; hevner2007threecycle siteres spesifikt for tre-sykkel-modellen.
- **Ingen metodisk detaljguide:** Artikkelen gir ikke konkrete instruksjoner for hvordan man gjennomfører intervjuer, koder data, benchmarker algoritmer eller dokumenterer krav. Den er et konseptuelt rammeverk, ikke en metodehåndbok.
- **«Field testing» er ambiguøst:** Hevner definerer ikke presist hva field testing krever operasjonelt. Det kan tolkes som: (a) strukturert brukertesting med koordinatorer og testdata, eller (b) full produksjonsdistribusjon med real-world data. Oppgaven har ikke gjort noen av delene — dette er en reell begrensning.
- **Ingen mapping til Peffers (2007) six-phase DSRM:** Tre-sykkel-modellen og Peffers' seks-fase-modell er komplementære beskrivelser av DSR, men de mappes ikke direkte til hverandre. I Ch 3.1 ¶3 som etterspør en tabell over «Peffers' six phases applied», er det mer naturlig å bruke peffers2007dsrm direkte; tre-sykkel-modellen fungerer bedre som overordnet framing i ¶1.
- **Outline MUST CITE → hevner2004design, ikke hevner2007threecycle:** Alle MUST CITE-markørene i outline.md for Ch 2.4 og Ch 3.1 peker på hevner2004design, ikke hevner2007threecycle. Bruk hevner2007threecycle som supplement der tre-sykkel-modellen trenger eksplisitt kildehenvisning, eller der hevner2004design ikke er tilstrekkelig for den spesifikke påstanden.
- **Ingen transport-/logistics-eksempler:** Artikkelens eksempler og kontekst er generisk IS-forskning. All domene-mapping til norsk transportsektor er gjort av ekstraksjon, ikke av kilden.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Relevance Cycle | "inputs requirements from the contextual environment into the research and introduces the research artifacts into environmental field testing" | p. 87 / PDF 2 |
| Rigor Cycle | "provides grounding theories and methods along with domain experience and expertise from the foundations knowledge base into the research and adds the new knowledge generated by the research to the growing knowledge base" | p. 87 / PDF 2 |
| Design Cycle | "supports a tighter loop of research activity for the construction and evaluation of design artifacts and processes" | p. 87 / PDF 2 |
| Application domain | "consists of the people, organizational systems, and technical systems that interact to work toward a goal" | p. 88 / PDF 4 |

## Rammeverk og modeller

### The Three-Cycle Model of DSR (Figure 1, p. 87 / PDF 2)

| Syklus | Input | Output | Rolle i DSR |
|---|---|---|---|
| Relevance Cycle | Requirements + opportunities/problems fra environment | Field testing av artefakt; feedback til neste iterasjon | Binder forskning til virkelighetskonteksten |
| Rigor Cycle | Scientific theories, methods, domain experience & expertise | Nye meta-artefakter og kunnskap tilbake til KB | Forankrer forskning i vitenskaplig grunnlag |
| Design Cycle | Requirements (fra Relevance); teorier/metoder (fra Rigor) | Evaluert artefakt (output til begge andre sykler) | Kjernen — iterativ konstruksjon og evaluering |

**Notat om Figure 1:** Figuren er identisk med Figure 1 i Hevner et al. (2004), men artikkelen tilbyr en mer utfyllende verbal beskrivelse av hva hver syklus inneholder og betyr.

## Key arguments / lines of reasoning

### Argument: Tre sykler løser spenningen mellom relevans og strenghet i DSR

- **Premiss 1:** DSR må være både praktisk relevant (løse reelle problemer i environment) OG vitenskapelig stringent (bidra til kunnskapsbasen).
- **Premiss 2:** Disse målene kan stå i spenning — ren nytte = anvendt arbeid; ren strenghet = grunnforskning.
- **Konklusjon:** Tre-sykkel-strukturen løser spenningen: Relevance Cycle sikrer environment-bidrag; Rigor Cycle sikrer vitenskapelig bidrag; Design Cycle er der de to balanseres i artefaktkonstruksjon.
- **Sted:** pp. 88–91 (gjennomgående argument)
- **Støtter claims:** Ch 2.4 ¶2, Ch 3.1 ¶1–2

### Argument: DSR krever ikke én grunnleggende designteori — flere kildetyper er akseptabelt

- **Premiss:** Å kreve at all DSR har en «kernel theory» er urealistisk og skadelig for feltet — gode DSR-papers avvises uriktig pga. manglende grunnteori.
- **Konklusjon:** DSR-rigor kommer fra hensiktsmessig bruk av teorier OG metoder, eksisterende artefakter, analogier og rike problem-beskrivelser — ikke fra én enkelt designteori.
- **Sted:** p. 90 (§3, Rigor Cycle)
- **Sitat:** "I much prefer the direction of identifying several different sources of ideas for the grounding of design science research to include rich opportunities/problems (from the relevance cycle), existing artifacts, analogies/metaphors, and theories" (p. 90 / PDF 5)
- **Støtter claims:** Ch 3.1 ¶2 — rettferdiggjør at oppgaven bruker *multiple* teorier (scheduling, HITL, CP) som grunnlag fremfor å konstruere én samlet designteori.

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| NSF-finansierte forskningsprosjekter | Majoritet av NSF CISE-prosjekter bruker DSR — DSR er etablert paradigme | p. 91 / PDF 6 |
| Action research (Cole et al. 2005) | Eksempel på metode for field testing i Relevance Cycle | p. 89 / PDF 4 |

## Data og statistikk

Kilden presenterer ingen statistikk — teoretisk/konseptuelt essay.

## Forfatter-perspektiv / metodologi

Artikkelen er et kommentar-essay av Hevner skrevet som respons på Iivari (2007) i samme tidsskriftsnummer. Den er ikke peer-reviewed på samme måte som vanlige artikler (det er en invited commentary). Hevner er førsteforfatter av det grunnleggende hevner2004design-rammeverket og taler fra en autoritativ posisjon innen DSR.

## Spot-check verification

1. Quote "I posit that these three cycles must be present and clearly identifiable in a design science research project." (p. 88 / PDF 3) — verified via `pdftotext -f 3 -l 3 raw/hevner2007threecycle.pdf` — **PASS**
2. Quote "the relevance cycle initiates design science research with an application context that not only provides the requirements for the research (e.g., the opportunity/problem to be addressed) as inputs but also defines acceptance criteria for the ultimate evaluation of the research results." (p. 89 / PDF 4) — verified via `pdftotext -f 4 -l 4 raw/hevner2007threecycle.pdf` — **PASS**
3. Quote "artifacts must be rigorously and thoroughly tested in laboratory and experimental situations before releasing the artifact into field testing along the relevance cycle." (p. 91 / PDF 6) — verified via `pdftotext -f 6 -l 6 raw/hevner2007threecycle.pdf` — **PASS**

**Result:** 3/3 quotes verified, 0 corrections made.