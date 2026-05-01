# A Design Science Research Methodology for Information Systems Research (`peffers2007dsrm`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Full article read (pp. 45–77). All sections relevant to the thesis — including the six-phase process model, definitions, practice rules, entry points, and evaluation discussion — have been captured. The case studies (pp. 57–70) were read but are low priority for citation purposes; the methodology and evaluation sections are fully covered.
  - **Gaps not investigated:** References section (pp. 74–77) not extracted — not needed for claims.

## Source metadata
- **BibTeX key:** `peffers2007dsrm`
- **Reference (APA 7):** Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, *24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302
- **Tilgang:** PDF (open access reprint via Taylor & Francis)
- **Raw source:** `../peffers2007dsrm.pdf`
- **Coverage in raw:** Full article, pp. 45–77 (PDF pages 2–35). Includes abstract, introduction, DSRM development rationale, six-phase process model (Figure 1), four case study demonstrations, evaluation of DSRM, discussion, and conclusion.

## Sammendrag (2–3 setninger)

Peffers et al. (2007) presenterer en fullstendig metodologi for design science-forskning (DSRM) i informasjonssystemer, bestående av seks aktiviteter: problemidentifikasjon og motivasjon, definisjon av løsningsmål, design og utvikling, demonstrasjon, evaluering og kommunikasjon. Artikkelen argumenterer for at mangelen på et slikt felles rammeverk har hemmet utbredelsen av design science-forskning i IS-disiplinen, og at DSRM gir både en nominell prosessmodell og en mental modell for presentasjon av forskningsresultater. Metodologien demonstreres retrospektivt gjennom fire casestudier med ulike inngangspoeng til prosessen.

## Areas of interest investigated

Fra outline.md og thesis-spine.md, hvilke områder ble vurdert for denne kilden:

| Område | Bidrag |
|---|---|
| Ch 2.4 ¶1 (DSR definition) | covered — primary citation for DSR definition alongside hevner2004design |
| Ch 2.4 ¶2 (Why DSR fits this project) | partial — supports general rationale, hevner2004design more directly cited here |
| Ch 3.1 ¶1 (State the methodology — DSR) | covered — primary citation for six-phase DSRM model |
| Ch 3.1 ¶3 (DSR phases applied — table) | covered — six activities described in detail |
| Ch 3.1 ¶4 (Validation vs. evaluation) | outside scope — Wieringa (2014) is primary source for this distinction |

## Claims this source supports

### Claim: "Design science creates and evaluates IT artifacts intended to solve identified organizational problems"
- **Suggested for:** Ch 2.4 ¶1; Ch 3.1 ¶1
- **Direkte sitat:** "Design science . . . creates and evaluates IT artifacts intended to solve identified organizational problems" (p. 49)
- **Parafrase:** DSR er den forskningsparadigmen som skaper og evaluerer IT-artefakter med formål å løse identifiserte organisasjonsproblemer.
- **Forbehold:** Peffers et al. siterer Hevner et al. [20] for denne definisjonen; den er altså sekundær fra en annen kilde (Hevner 2004), men gjengitt verbatim her.
- **Anvendelse på vårt case:** Ressursplanlegger er eksplisitt en IT-artefakt designet for å løse et identifisert organisasjonsproblem (manuell ressursplanlegging hos norske transportselskaper) — definisjonen passer direkte.

### Claim: "The DS process includes six steps: problem identification and motivation, definition of the objectives for a solution, design and development, demonstration, evaluation, and communication"
- **Suggested for:** Ch 2.4 ¶1; Ch 3.1 ¶1; Ch 3.1 ¶3 (table)
- **Direkte sitat:** "The DS process includes six steps: problem identification and motivation, definition of the objectives for a solution, design and development, demonstration, evaluation, and communication." (p. 46, abstract)
- **Parafrase:** DSRM strukturerer design science-forskning i seks nominelt sekvensielle aktiviteter.
- **Forbehold:** Prosessen er nominelt sekvensiell, men forfatterne understreker at forskere ikke alltid følger den fra aktivitet 1 til 6 — man kan starte i nesten ethvert trinn.
- **Anvendelse på vårt case:** Ressursplanlegger-prosjektet kan kartlegges direkte mot alle seks aktiviteter: problem (manuell planlegging) → mål (effektiv tildeling) → design og utvikling (systembygging) → demonstrasjon (benchmarking) → evaluering (kravsporing) → kommunikasjon (denne avhandlingen).

### Claim: "The DSRM presents a nominal process model for doing DS research and a mental model for presenting and evaluating DS research in IS"
- **Suggested for:** Ch 2.4 ¶1; Ch 3.1 ¶1
- **Direkte sitat:** "it provides a nominal process model for doing DS research, and it provides a mental model for presenting and evaluating DS research in IS." (p. 46, abstract)
- **Parafrase:** DSRM fyller to hull: det gir en prosessmodell for gjennomføring og en mental modell for presentasjon av forskningsresultater.
- **Forbehold:** "Nominal" betyr her at dette er én god måte å gjøre det på, ikke den eneste.
- **Anvendelse på vårt case:** Denne avhandlingen bruker DSRM både som gjennomføringsramme (Kapittel 3) og som struktureringsmodell for rapportering av funn.

### Claim: "This process is structured in a nominally sequential order; however, there is no expectation that researchers would always proceed in sequential order from activity 1 through activity 6"
- **Suggested for:** Ch 3.1 ¶3
- **Direkte sitat:** "This process is structured in a nominally sequential order; however, there is no expectation that researchers would always proceed in sequential order from activity 1 through activity 6." (p. 56)
- **Parafrase:** Prosessen har fire mulige inngangspoeng, og i praksis starter mange prosjekter ikke med problemidentifikasjon.
- **Forbehold:** Det pekes på fire konkrete inngangspoeng (problem-centered, objective-centered, design- and development-centered, client-/context-initiated).
- **Anvendelse på vårt case:** Ressursplanlegger-prosjektet startet primært problem-centered (observasjon av manuell planlegging) men fikk også inngangspoeng fra klientkontekst (industribehov). Dette er legitimt innenfor DSRM.

### Claim: "Activity 5: Evaluation. Observe and measure how well the artifact supports a solution to the problem."
- **Suggested for:** Ch 3.1 ¶4; Ch 3.5 ¶3
- **Direkte sitat:** "Activity 5: Evaluation. Observe and measure how well the artifact supports a solution to the problem. This activity involves comparing the objectives of a solution to actual observed results from use of the artifact in the demonstration." (p. 56)
- **Parafrase:** Evaluering i DSRM-forstand innebærer måling av hvor godt artefakten løser problemet, sammenlignet med de mål som ble satt i aktivitet 2.
- **Forbehold:** DSRM-evaluering kan ta mange former — fra kvantitative ytelsesmål til logisk bevis. Peffers skiller ikke mellom «validation» og «evaluation» slik Wieringa (2014) gjør; Wieringa er den korrekte kilden for dette skillet.
- **Anvendelse på vårt case:** Benchmarking og kravsporing er Ressursplanleggers evalueringsmekanismer — begge passer inn i DSRM aktivitet 5 uten at det er snakk om produksjonsdeploy.

### Claim: "A design science research artifact can be any designed object in which a research contribution is embedded in the design"
- **Suggested for:** Ch 2.4 ¶1; Ch 3.1 ¶1
- **Direkte sitat:** "Conceptually, a design research artifact can be any designed object in which a research contribution is embedded in the design." (p. 55)
- **Parafrase:** Artefakter i DSR er ikke begrenset til programvare — de kan være konstrukter, modeller, metoder eller instansiasjoner.
- **Forbehold:** Bred definisjon — relevant å sitere for å legitimere at Ressursplanlegger (en webapplikasjon) er en gyldig DSR-artefakt.
- **Anvendelse på vårt case:** Ressursplanlegger som webbasert planleggingsplattform er en instansiasjon i DSR-forstand, med forskningsbidrag innebygd i designvalgene (multi-engine algoritme, human-in-the-loop-grensesnitt).

### Claim: "A methodology is 'a system of principles, practices, and procedures applied to a specific branch of knowledge'"
- **Suggested for:** Ch 3.1 ¶1
- **Direkte sitat:** "A methodology is 'a system of principles, practices, and procedures applied to a specific branch of knowledge'" (p. 49)
- **Parafrase:** En metodologi skiller seg fra en prosessmodell alene ved å inkludere principper, praksisregler og prosedyrer.
- **Forbehold:** Peffers siterer DMReview [13] for denne definisjonen.
- **Anvendelse på vårt case:** Brukes for å introdusere DSR som metodologi (ikke bare metode) i seksjon 3.1 — gir akademisk tyngde til valget av DSRM.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Artifact | Ressursplanlegger (webapplikasjon) | Spesifikt en instantiation i DSRM-terminologi |
| Problem identification and motivation | Intervjuer med trafikkoordinatorer → identifikasjon av manuell planlegging som problem | Aktivitet 1 i DSRM |
| Define objectives for a solution | Kravspesifikasjon (MoSCoW) | Aktivitet 2 i DSRM |
| Design and development | Systembygging (iterative sprints, algoritme) | Aktivitet 3 i DSRM |
| Demonstration | Benchmarking på syntetiske datasett | Aktivitet 4 i DSRM |
| Evaluation | Kravsporing + benchmarkresultater | Aktivitet 5 i DSRM |
| Communication | Denne avhandlingen | Aktivitet 6 i DSRM |
| Problem-centered initiation | Observasjon av manuell koordinatorpraksis som forskningsutgangspunkt | Det dominerende inngangspoeng i dette prosjektet |
| Organizational problem | Treghet og nøkkelpersonavhengighet i ressursplanlegging | Direkte kartleggbar |

## Forbehold og begrensninger

- Artikkelen er skrevet generelt for IS-forskning og bruker eksempler fra helsedata, programvareutvikling og VoIP — ikke transport eller logistikk. Domenebroen må bygges eksplisitt i avhandlingsteksten.
- Peffers skiller ikke mellom «validation» og «evaluation» på den måten Wieringa (2014) gjør. For argumentet om at denne avhandlingen *validerer* (heller enn *evaluerer*) Ressursplanlegger, er Wieringa (2014) den riktige kilden.
- Modellen er normativ, ikke deskriptiv — den beskriver hva som er en god måte å gjøre DS-forskning på, ikke nødvendigvis hva alle DS-prosjekter faktisk gjør.
- Artikkelen er fra 2007 og er en av de tidlige kanoniske DSR-kildene. Den er ikke den seneste, men er den mest siterte prosessmodellen og derfor riktig å bruke som primærhenvisning.
- Artikkelen adresserer ikke validering av artefakter som *ikke* er deployert i produksjon — dette hullet dekkes av Wieringa (2014).

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Design science (IS) | "Design science . . . creates and evaluates IT artifacts intended to solve identified organizational problems" | 49 |
| Methodology | "a system of principles, practices, and procedures applied to a specific branch of knowledge" | 49 |
| DS artifact | "Conceptually, a design research artifact can be any designed object in which a research contribution is embedded in the design." | 55 |

## Rammeverk og modeller

### DSRM Six-Activity Process Model (Figure 1, p. 54)

| Aktivitet | Kort beskrivelse | Ressurser som kreves |
|---|---|---|
| 1. Problem identification and motivation | Define the specific research problem and justify the value of a solution | Knowledge of the state of the problem and importance of its solution |
| 2. Define the objectives for a solution | Infer objectives from problem definition and knowledge of what is possible and feasible | Knowledge of the state of problems and current solutions |
| 3. Design and development | Create the artifact (constructs, models, methods, or instantiations) | Knowledge of theory that can be brought to bear in a solution |
| 4. Demonstration | Demonstrate the use of the artifact to solve one or more instances of the problem | Effective knowledge of how to use the artifact to solve the problem |
| 5. Evaluation | Observe and measure how well the artifact supports a solution to the problem | Knowledge of relevant metrics and analysis techniques |
| 6. Communication | Communicate the problem, artifact, utility, novelty, rigor, and effectiveness to relevant audiences | Knowledge of the disciplinary culture |

### Four Research Entry Points (p. 56)

| Inngangspoeng | Starter med | Trigger |
|---|---|---|
| Problem-centered initiation | Activity 1 | Observation of problem or future research suggestion |
| Objective-centered solution | Activity 2 | Industry/research need for an artifact |
| Design- and development-centered approach | Activity 3 | Existence of artifact not yet formally applied to a problem |
| Client-/context-initiated solution | Activity 4 | Observing a practical solution that worked |

## Key arguments / lines of reasoning

### Argument: Mangelen på en felles metodologi har hemmet DS-forskning i IS
- **Premiss(er):** DS-forskning i IS har eksistert i 15 år men blitt lite adoptert; mange IS-baserte DS-arbeider har publisert i ingeniørtidsskrifter eller brukt ad hoc-begrunnelser for sin gyldighet.
- **Konklusjon:** En felles metodologi (DSRM) vil legitimere DS-forskning i IS og gjøre det lettere for forfattere, reviewere og redaktører å gjenkjenne og vurdere slik forskning.
- **Sted:** (pp. 47–50)
- **Hvilke claims dette støtter:** Ch 2.4 ¶1; Ch 3.1 ¶1

### Argument: DSRM er ikke den eneste mulige metodologien for DS-forskning
- **Premiss(er):** Det er minst fem andre typer DSRM som kan tenkes; DSRM bør ikke brukes som en rigid ortodoksi.
- **Konklusjon:** DSRM presenterer én god generell metodologi, men kontekstspesifikke varianter kan være velbegrunnede.
- **Sted:** (pp. 73–74)
- **Hvilke claims dette støtter:** Ch 3.1 ¶1 (moderat tone rundt metodologivalg)

### Argument: DSR og aksjonsforskning har substansielle likheter men ulike kjernefokus
- **Premiss(er):** Begge paradigmene deler antagelser om ontologi, epistemologi og aksiologi; men i DSR er design og bevis på nytte det sentrale, mens i aksjonsforskning er det organisasjonskonteksten og aktiv problemløsning.
- **Konklusjon:** DSRM kan brukes som struktur for et aksjonsforskning-studie, men de er metodologisk og konseptuelt forskjellige.
- **Sted:** (pp. 71–72)
- **Hvilke claims dette støtter:** Ch 3.1 ¶2 (kontrast med andre paradigmer)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| CATCH Data Warehouse (health data) | Problem-centered initiation → full DSRM process | pp. 57–60 |
| MBA Technologies software reuse measure | Objective-centered initiation → DSRM process | pp. 60–63 |
| CGUsipClient (SIP/VoIP application) | Design- and development-centered initiation | pp. 63–67 |
| Digia IS planning method | Client-/context-initiated initiation | pp. 67–70 |

## Data og statistikk

(Ikke aktuelt — konseptuell/metodologisk artikkel uten empiriske statistikker relevante for avhandlingen.)

## Forfatter-perspektiv / metodologi

Artikkelen bruker selv en design science-tilnærming til utvikling av metodologien: forfatterne bygger konsensus fra syv representativt valgte arbeider (Tabell 1, s. 53), designer DSRM basert på felles elementer, og demonstrerer den retrospektivt på fire casestudier. Den er dermed normativ og konseptuell, ikke empirisk i tradisjonell forstand.

## Spot-check verification

1. Quote "The DS process includes six steps: problem identification and motivation, definition of the objectives for a solution, design and development, demonstration, evaluation, and communication." (p. 46) — verified via `pdftotext -f 3 -l 3` — PASS (quote appears verbatim in abstract on printed p. 46)

2. Quote "Activity 5: Evaluation. Observe and measure how well the artifact supports a solution to the problem. This activity involves comparing the objectives of a solution to actual observed results from use of the artifact in the demonstration." (p. 56) — verified via `pdftotext -f 13 -l 13` — PASS (quote appears verbatim on printed p. 56)

3. Quote "Design science . . . creates and evaluates IT artifacts intended to solve identified organizational problems" (p. 49) — verified via `pdftotext -f 6 -l 6` — PASS (quote appears verbatim on printed p. 49, attribution to [20] confirmed)

4. Quote "This process is structured in a nominally sequential order; however, there is no expectation that researchers would always proceed in sequential order from activity 1 through activity 6." (p. 56) — verified via `pdftotext -f 13 -l 13` — PASS (quote appears verbatim on printed p. 56)

5. Quote "A methodology is 'a system of principles, practices, and procedures applied to a specific branch of knowledge'" (p. 49) — verified via `pdftotext -f 6 -l 6` — PASS (quote appears verbatim on printed p. 49)

**Result:** 5/5 quotes verified, 0 corrections made.
