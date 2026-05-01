# Design Science in Information Systems Research (`hevner2004design`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The paper is the canonical DSR framework source. All sections relevant to Ch 2.4 and Ch 3.1 have been read in full. The guidelines framework, the build-and-evaluate cycle, the artefact taxonomy, and the validation/evaluation discussion are all fully extracted.
  - **Gaps not investigated:** The three exemplar case analyses (pp. 91–97) were read but are not cited in the thesis outline — they were skimmed for any transferable claims and none were found.

## Source metadata
- **BibTeX key:** `hevner2004design`
- **Reference (APA 7):** Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, *28*(1), 75–105. https://doi.org/10.2307/25148625
- **Tilgang:** PDF
- **Raw source:** `../hevner2004design.pdf`
- **Coverage in raw:** Complete article, pp. 75–105. Abstract, Introduction, Framework for IS Research, Guidelines 1–7, Application to exemplars (Gavish & Gerdes; Aalst & Kumar; Markus, Majchrzak & Gasser), Discussion and Conclusions.

## Sammendrag (2–3 setninger)

Hevner et al. (2004) establishes Design Science Research (DSR) as a legitimate and necessary paradigm in IS research alongside behavioural science, arguing that knowledge and understanding of a problem domain and its solution are achieved through the building and evaluation of purposeful IT artefacts. The paper presents a conceptual framework for IS research and seven guidelines for conducting, evaluating, and communicating DSR. Its main contribution is to provide clear criteria — particularly around artefact creation, problem relevance, rigorous evaluation, and novelty — that distinguish valid DSR from routine system building.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.4 ¶1 (DSR definition) | Fully covered — defines DSR, two paradigms, artefact types |
| Ch 2.4 ¶3 (validation vs evaluation) | Partially covered — evaluation methods taxonomy present; validation/evaluation distinction not explicitly made in Hevner; see Wieringa |
| Ch 3.1 ¶1 (methodology — DSR citation) | Fully covered — standard citation target |
| Ch 3.1 ¶2 (why DSR fits) | Covered — problem relevance guideline and build+evaluate argument |
| Ch 3.1 ¶4 (validation vs evaluation) | Partially covered — Hevner discusses evaluation methods but does not use Wieringa's validation/evaluation distinction |
| Ch 5.1–5.6 (discussion) | Outside scope — Hevner does not cover transport planning or algorithm assessment |

## Claims this source supports

### Claim 1: "In the design-science paradigm, knowledge and understanding of a problem domain and its solution are achieved in the building and application of the designed artefact."
- **Suggested for:** Ch 2.4 ¶1; Ch 3.1 ¶1
- **Direkte sitat:** "knowledge and understanding of a design problem and its solution are acquired in the building and application of an artifact" (p. 82)
- **Parafrase:** DSR generates knowledge not by observing existing phenomena but by constructing a purposeful artefact and studying what is learned through that construction and use.
- **Forbehold:** The claim applies to IS research broadly; whether any given artefact constitutes DSR depends on novelty, problem relevance, and rigorous evaluation (per the other six guidelines).
- **Anvendelse på vårt case:** Ressursplanlegger is the designed artefact through which knowledge about algorithm-assisted driver/vehicle assignment is acquired; the thesis is the research output produced by building and evaluating that artefact.

### Claim 2: "Two paradigms characterise IS research — behavioural science (seeks truth) and design science (seeks utility) — and both are necessary."
- **Suggested for:** Ch 2.4 ¶1; Ch 3.1 ¶2
- **Direkte sitat:** "The goal of behavioral-science research is truth. The goal of design-science research is utility." (p. 80)
- **Parafrase:** Behavioural science explains and predicts; design science creates effective artefacts. The two are inseparable: utility informs theory and truth informs design.
- **Forbehold:** The paper argues both paradigms are necessary for IS research as a whole; this thesis applies only the design-science paradigm, which is appropriate when the contribution is a novel artefact addressing a practical problem.
- **Anvendelse på vårt case:** Choosing DSR as the research paradigm for Ressursplanlegger is justified because the contribution is the planning artefact itself and the knowledge gained through building and validating it — not a predictive theory of coordinator behaviour.

### Claim 3: "Design-science research must produce a viable artefact in the form of a construct, a model, a method, or an instantiation."
- **Suggested for:** Ch 2.4 ¶1; Ch 3.1 ¶1
- **Direkte sitat:** "The result of design-science research in IS is, by definition, a purposeful IT artifact created to address an important organizational problem." (p. 82)
- **Parafrase:** The artefact is not incidental to DSR — it is its core output and must be formally described and demonstrably applicable.
- **Forbehold:** "Artifacts constructed in design-science research are rarely full-grown information systems that are used in practice. Instead, artifacts are innovations that define the ideas, practices, technical capabilities, and products through which [...] information systems can be effectively and efficiently accomplished" (p. 83). Ressursplanlegger is a prototype/instantiation — this framing is accurate.
- **Anvendelse på vårt case:** Ressursplanlegger is an instantiation — a working prototype system — which is the most concrete artefact type in the taxonomy; this legitimises building a prototype (rather than producing a theory) as the research contribution.

### Claim 4: "Design-science research addresses wicked problems — those characterised by unstable requirements, complex interactions among subcomponents, and dependence on human cognitive and social abilities."
- **Suggested for:** Ch 2.4 ¶2; Ch 3.1 ¶2
- **Direkte sitat:** "Design-science research in IS addresses what are considered to be *wicked problems* (Brooks 1987, 1996; Rittel and Webber 1984). That is, those problems characterized by [...] unstable requirements and constraints based upon ill-defined environmental contexts [and] complex interactions among subcomponents of the problem and its solution" (p. 81)
- **Parafrase:** DSR is the appropriate paradigm precisely when problems resist stable, fully-specifiable solutions — when creativity, iteration, and heuristic search are required.
- **Forbehold:** The wicked-problem framing comes from Brooks and Rittel/Webber, not Hevner's own original claim; it is used here to motivate DSR. The transport planning problem in this thesis has some but not all features of a wicked problem (requirements were elicited and stabilised through interviews).
- **Anvendelse på vårt case:** Driver and vehicle assignment involves unstable requirements (sick leave, cancellations, weather), complex constraint interactions (competency, availability, vehicle type), and dependence on coordinator tacit knowledge — features that map directly onto the wicked-problem characterisation and justify DSR over a purely analytical approach.

### Claim 5: "The utility, quality, and efficacy of a design artefact must be rigorously demonstrated via well-executed evaluation methods."
- **Suggested for:** Ch 2.4 ¶3; Ch 3.1 ¶4; Ch 3.5 ¶3
- **Direkte sitat:** "The utility, quality, and efficacy of a design artifact must be rigorously demonstrated via well-executed evaluation methods." (p. 83, Table 1, Guideline 3)
- **Parafrase:** Producing the artefact is insufficient; its value must be shown through appropriate evaluation — analytical, experimental, observational, testing, or descriptive.
- **Forbehold:** Hevner lists five evaluation categories (Table 2, p. 86): observational, analytical, experimental, testing, descriptive. This thesis uses analytical (benchmarking) and testing (requirements traceability) — both are legitimate per the framework. Hevner does not use the term "validation" in the Wieringa sense; the validation/evaluation distinction used in Ch 3.1 and 2.4 must cite Wieringa, not Hevner.
- **Anvendelse på vårt case:** Algorithm benchmarking (comparing greedy, OR-Tools, Timefold on dataset sizes and schedule quality) corresponds to the analytical/experimental evaluation methods endorsed by Hevner; requirements traceability corresponds to descriptive/informed argument evaluation.

### Claim 6: "Design science is inherently iterative; heuristic search strategies produce feasible, good designs."
- **Suggested for:** Ch 3.4 ¶2; Ch 4.5 ¶2
- **Direkte sitat:** "Design science is inherently iterative. The search for the best, or optimal, design is often intractable for realistic information systems problems. Heuristic search strategies produce feasible, good designs that can be implemented in the business environment." (p. 88)
- **Parafrase:** Because optimal solutions are computationally infeasible for realistic problem sizes, DSR embraces heuristics and satisficing — finding a solution that is good enough rather than provably optimal.
- **Forbehold:** Hevner is speaking about the design process as a whole (how the researcher searches for a good artefact design), not specifically about algorithmic heuristics. However, the claim is applicable at both levels.
- **Anvendelse på vårt case:** The multi-engine solver approach (greedy for instant baseline, CP-SAT for near-optimal, Timefold for large instances) directly instantiates the heuristic search principle — the system does not pursue a provably optimal solution but produces feasible, good plans within a practical time limit.

### Claim 7: "Effective design-science research must provide clear and verifiable contributions in the design artefact, design foundations, and/or design methodologies."
- **Suggested for:** Ch 2.4 ¶2; Ch 6.2 ¶5
- **Direkte sitat:** "Effective design-science research must provide clear and verifiable contributions in the areas of the design artifact, design foundations, and/or design methodologies." (p. 83, Table 1, Guideline 4)
- **Parafrase:** Research contribution in DSR can be the artefact itself, novel constructs/methods/models that extend the knowledge base, or new evaluation methodologies — one or more must be present.
- **Forbehold:** This thesis's contribution is primarily the artefact (Ressursplanlegger as an instantiation) and the knowledge generated through the requirements process and validation — not a new design methodology.
- **Anvendelse på vårt case:** The thesis contribution is the instantiation (Ressursplanlegger), the structured requirements synthesis from seven coordinator interviews, and the validation findings — all of which map onto Hevner's three contribution types and can be stated explicitly in Ch 6.2.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| IT artifact | Ressursplanlegger | The planning platform is the instantiation artefact |
| Instantiation | Prototype system (Ressursplanlegger) | Most concrete artefact type in Hevner's taxonomy |
| Business need / organisational problem | Inefficient manual driver/vehicle assignment | The problem motivating the artefact |
| Environment (people, organisations, technology) | Traffic coordinators, Norwegian transport SMEs, legacy TMS | The context in which the artefact must perform |
| Heuristic search | Multi-engine solver (greedy / CP-SAT / Timefold) | Both the design process and the artefact's internal logic use heuristics |
| Evaluate / justify | Benchmarking + requirements traceability | The two primary evaluation methods used in this thesis |
| Knowledge base | Scheduling theory, constraint programming, HITL literature | What is drawn on (rigor side of Figure 2) |
| Wicked problem | Daily planning with sick leave, tacit knowledge, unstable constraints | Partial mapping — see caveats |
| Build and evaluate cycle | Iterative sprint development with requirement refinement | Consistent with Hevner's generate/test cycle |

## Forbehold og begrensninger

- **Hevner does not distinguish validation from evaluation in the Wieringa sense.** The thesis uses "validation" (predicting behaviour through benchmarking and traceability, without production deployment) as a specific methodological choice. This distinction must cite Wieringa (2014), not Hevner.
- **Hevner's framework is normative, not descriptive.** The seven guidelines prescribe what good DSR looks like; they do not describe what was done in this thesis. The thesis must apply the guidelines actively (show how each is met) rather than just citing the framework.
- **The exemplar cases (pp. 91–97) are not relevant.** GDSS, workflow languages, and emergent knowledge processes are entirely different domains; no transfer to transport planning is possible.
- **Hevner does not cover algorithm design, constraint programming, or transport logistics.** The source is a methodology paper; all domain-specific content must come from other sources.
- **"Wicked problems" is attributed by Hevner to Rittel and Webber (1984) and Brooks (1987, 1996)** — do not cite Hevner as the originator of this concept.
- **The paper was written in 2004.** The specific IT artefacts it discusses (GDSS, EKP tools, workflow languages) are obsolete; only the methodological framework and guidelines transfer.
- **Production deployment requirement:** Hevner's Guideline 2 (Problem Relevance) implies research must ultimately be applicable in a real organisational setting. This thesis explicitly does not deploy Ressursplanlegger in production — this is acknowledged as a limitation in Ch 5.6 and Ch 3.1.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Design science (purpose) | "The design-science paradigm seeks to extend the boundaries of human and organizational capabilities by creating new and innovative artifacts." | p. 75 (abstract) |
| IT artifact (types) | "IT artifacts are broadly defined as *constructs* (vocabulary and symbols), *models* (abstractions and representations), *methods* (algorithms and practices), and *instantiations* (implemented and prototype systems)." | p. 77 |
| Design-science research (core principle) | "knowledge and understanding of a design problem and its solution are acquired in the building and application of an artifact" | p. 82 |
| Wicked problems | "Design-science research in IS addresses what are considered to be *wicked problems* [...] characterized by unstable requirements and constraints based upon ill-defined environmental contexts [and] complex interactions among subcomponents of the problem and its solution" | p. 81 |
| Utility (DSR goal) | "The goal of design-science research is utility." | p. 80 |

## Rammeverk og modeller

### IS Research Framework — Figure 2 (p. 80)

The framework has three columns: Environment (left), IS Research (centre), Knowledge Base (right), connected by Relevance (left arrow) and Rigor (right arrow).

| Komponent | Hva det er | Eksempel kilden gir | Side |
|---|---|---|---|
| Environment | The problem space: people, organisations, technology | Roles, strategies, infrastructure, development capabilities | p. 79 |
| IS Research — Develop/Build | Creating theories and artefacts | Instantiations, models, methods | p. 80 |
| IS Research — Justify/Evaluate | Assessing utility of artefact or truth of theory | Case study, experiment, simulation, field study | p. 80 |
| Knowledge Base — Foundations | Prior theories, frameworks, constructs, methods | Scheduling theory, constraint programming (for this thesis) | p. 80 |
| Knowledge Base — Methodologies | Data analysis techniques, formalisms, validation criteria | Interview analysis (Braun & Clarke), benchmarking | p. 80 |
| Relevance | Business needs drive research | Problem identified through coordinator interviews | p. 79 |
| Rigor | Appropriate application of knowledge base | Using established solver benchmarking criteria | p. 80 |

### Seven Design-Science Research Guidelines — Table 1 (p. 83)

| Guideline | Beskrivelse | Side |
|---|---|---|
| 1: Design as an Artifact | "Design-science research must produce a viable artifact in the form of a construct, a model, a method, or an instantiation." | p. 83 |
| 2: Problem Relevance | "The objective of design-science research is to develop technology-based solutions to important and relevant business problems." | p. 83 |
| 3: Design Evaluation | "The utility, quality, and efficacy of a design artifact must be rigorously demonstrated via well-executed evaluation methods." | p. 83 |
| 4: Research Contributions | "Effective design-science research must provide clear and verifiable contributions in the areas of the design artifact, design foundations, and/or design methodologies." | p. 83 |
| 5: Research Rigor | "Design-science research relies upon the application of rigorous methods in both the construction and evaluation of the design artifact." | p. 83 |
| 6: Design as a Search Process | "The search for an effective artifact requires utilizing available means to reach desired ends while satisfying laws in the problem environment." | p. 83 |
| 7: Communication of Research | "Design-science research must be presented effectively both to technology-oriented as well as management-oriented audiences." | p. 83 |

### Design Evaluation Methods — Table 2 (p. 86)

| Kategori | Metode | Relevans for denne thesis |
|---|---|---|
| 1. Observational | Case study; field study | Not used (no production deployment) |
| 2. Analytical | Static analysis; architecture analysis; optimisation; dynamic analysis | Benchmarking falls here |
| 3. Experimental | Controlled experiment; simulation | Simulation with artificial datasets (benchmarking) |
| 4. Testing | Functional (black box); structural (white box) | Requirements traceability partially maps here |
| 5. Descriptive | Informed argument; scenarios | Use-case walkthrough of planning workflow |

## Key arguments / lines of reasoning

### Argument: Why DSR is distinct from routine system building
- **Premiss 1:** Routine design applies existing knowledge to known problems using established best-practice artefacts from the knowledge base.
- **Premiss 2:** Design-science research addresses unsolved problems or solves known problems in more effective or efficient ways.
- **Konklusjon:** "The key differentiator between routine design and design research is the clear identification of a contribution to the archival knowledge base of foundations and methodologies." (p. 81)
- **Sted:** p. 81
- **Hvilke claims dette støtter:** Ch 2.4 ¶2; Ch 3.1 ¶2

### Argument: Build-and-evaluate as the core DSR research cycle
- **Premiss 1:** Design science creates artefacts; behavioural science produces theories. Both are evaluated, and the evaluation feeds back into refinement.
- **Premiss 2:** "This build-and-evaluate loop is typically iterated a number of times before the final design artifact is generated." (p. 78)
- **Konklusjon:** The researcher must be cognisant of evolving both the design process and the design artefact as part of the research — the artefact is not fixed at the start.
- **Sted:** p. 78
- **Hvilke claims dette støtter:** Ch 3.4 ¶2 (iterative development); Ch 2.4 ¶2

### Argument: Heuristics are the appropriate strategy for wicked IS problems
- **Premiss 1:** Optimal solutions are often computationally intractable for realistic IS problems.
- **Premiss 2:** "Heuristic search strategies produce feasible, good designs that can be implemented in the business environment."
- **Premiss 3:** The design task involves "constructing an artifact that 'works well' for the specified class of problems." (p. 89)
- **Konklusjon:** Satisficing — finding a solution that is good enough rather than optimal — is a legitimate and appropriate DSR strategy.
- **Sted:** p. 88–89
- **Hvilke claims dette støtter:** Ch 3.1 ¶2; Ch 4.5 ¶2 (algorithm justification)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Gavish & Gerdes (1998) — GDSS anonymity mechanisms | Instantiation artefact; formal proof as evaluation; cost-benefit analysis | pp. 91–93 |
| Aalst & Kumar (2003) — XRL workflow language | Artefact as construct + method; formal semantics as rigour basis | pp. 93–95 |
| Markus, Majchrzak & Gasser (2002) — TOP Modeler | Action research variant of DSR; iterative deployment; commercial instantiation | pp. 95–97 |

Note: None of these examples are relevant for citation in the thesis — they illustrate the framework in domains unrelated to transport planning.

## Data og statistikk

(Not applicable — this is a conceptual/methodological paper. No empirical data or statistics are presented.)

## Forfatter-perspektiv / metodologi

This is a research essay (conceptual/normative), not an empirical study. The authors draw on IS design theory (March and Smith 1995; Walls et al. 1992), engineering design literature (Simon 1996; Brooks 1987), and three exemplar IS papers to develop and illustrate the framework. The guidelines are prescriptive (what good DSR should do), not derived from systematic empirical observation.

## Spot-check verification

1. Quote "knowledge and understanding of a design problem and its solution are acquired in the building and application of an artifact" (p. 82) — verified via `pdftotext -f 9 -l 9 raw/hevner2004design.pdf` — **PASS** (found at line 28 of PDF page 9 = printed p. 82)

2. Quote "The goal of design-science research is utility." (p. 80) — verified via `pdftotext -f 2 -l 31 raw/hevner2004design.pdf | grep "goal of design"` — **PASS** (found, confirmed on PDF page 7 = printed p. 80)

3. Quote "Design-science research in IS addresses what are considered to be *wicked problems*" (p. 81) — verified via `pdftotext -f 8 -l 8 raw/hevner2004design.pdf` — **PASS** (found in body text of PDF page 8 = printed p. 81: "Design-science research in IS addresses what are considered to be wicked problems (Brooks 1987, 1996; Rittel and Webber 1984)")

4. Table 1 Guideline 3 quote "The utility, quality, and efficacy of a design artifact must be rigorously demonstrated via well-executed evaluation methods." (p. 83) — verified via `pdftotext -f 10 -l 10 raw/hevner2004design.pdf` — **PASS** (Table 1 found on PDF page 10 = printed p. 83, Guideline 3 row confirmed)

5. Quote "Design science is inherently iterative. The search for the best, or optimal, design is often intractable for realistic information systems problems. Heuristic search strategies produce feasible, good designs that can be implemented in the business environment." (p. 88) — verified via `pdftotext -f 15 -l 15 raw/hevner2004design.pdf` — **PASS** (found verbatim under Guideline 6 heading on PDF page 15 = printed p. 88)

**Result:** 5/5 quotes verified, 0 corrections made.