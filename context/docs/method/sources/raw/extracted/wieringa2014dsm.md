e# Design Science Methodology for Information Systems and Software Engineering (`wieringa2014dsm`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Ch.1 (DSR definition and framework), Ch.3 (design cycle and §3.1.5 validation vs. evaluation), Ch.5 (implementation evaluation and problem investigation), and Ch.7 (treatment validation methods) were deep-read. These chapters cover every thesis area of interest for this source. Chapters on statistical inference, case study methods, and conceptual frameworks (Parts III–V) were skimmed via TOC and keyword grep; they have no bearing on the thesis claims attributed to this source.
  - **Gaps not investigated:** Parts III–V (Chs. 8–20) — contain statistical methods, sampling theory, and research-method details that are not relevant to the thesis sections citing this source.

## Source metadata
- **BibTeX key:** `wieringa2014dsm`
- **Reference (APA 7):** Wieringa, R. J. (2014). *Design science methodology for information systems and software engineering*. Springer.
- **Tilgang:** PDF (local)
- **Raw source:** `../wieringa2014dsm.pdf`
- **Coverage in raw:** Full book, 327 PDF pages. PDF page offset: for printed pages 3–23, PDF = printed + 15; for printed pages 27+, PDF = printed + 12 (a blank Part-I divider page causes the offset to shift by 3 between printed p.23 and p.27). All citations in this file use printed page numbers with dual-format notation.

## Sammendrag (2–3 setninger)

Wieringa (2014) is a methodology textbook for design science research (DSR) in information systems and software engineering. It defines DSR as the iterative design and investigation of artefacts in context, structures this through the *design cycle* (problem investigation → treatment design → treatment validation) as a subset of the *engineering cycle* (which also includes implementation and evaluation), and provides a detailed treatment of the distinction between *validation* (predicting artefact behaviour before real-world deployment) and *evaluation* (studying an implemented artefact in the field). The book's main contribution to the thesis is to provide the methodological vocabulary for justifying why the project validates rather than evaluates Ressursplanlegger, and for explaining what the design cycle consists of.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.4 (DSR theory — definition, artefact, design cycle) | **covered** — Ch.1 and Ch.3 provide definitions and framework |
| Ch 3.1 (DSR phases applied — design cycle structure) | **covered** — Ch.3 maps phases; design cycle table in footnote 2 (p.34) directly links to Peffers et al. |
| Ch 3.4 (system development — iterative DSR process) | **partial** — agile iteration through design cycle mentioned (p.32), no deeper treatment |
| Ch 3.5 (validity and reliability — validation vs. evaluation) | **covered** — §3.1.5 (pp.31–32) is the primary locus; Ch.7 expands with research methods |
| Ch 5.6 (limitations — validation not evaluation) | **covered** — §3.1.5 provides exact vocabulary for framing limitation |

## Claims this source supports

### Claim 1: Validation predicts artefact behaviour before deployment; evaluation studies an implemented artefact in the field

- **Suggested for:** Ch 2.4 ¶3 (MUST CITE: define validation vs. evaluation; bridge to Ch.3); Ch 3.1 ¶4 (MUST CITE: thesis validates, not evaluates); Ch 3.5 ¶3 (system validity — validation via requirements traceability + benchmarking)
- **Direkte sitat:** "To validate a treatment is to justify that it would contribute to stakeholder goals if implemented. [...] Validation is contrasted with evaluation, which is the investigation of a treatment as applied by stakeholders in the field." (p. 31 / PDF 43)
- **Parafrase:** Validation is pre-deployment justification; evaluation is post-deployment field study. The two require different research goals and research approaches.
- **Forbehold:** Wieringa's framing is general (not specific to algorithm benchmarking or requirements traceability); the thesis must explicitly state which validation method is used (single-case mechanism experiment = benchmarking) to be precise.
- **Anvendelse på vårt case:** Ressursplanlegger is validated — not evaluated — because the system has not been deployed in a real transport company; benchmarking against synthetic datasets and requirements traceability are validation instruments (single-case mechanism experiments on artefact prototypes against modelled contexts), not field evaluations.

### Claim 2: The design cycle consists of problem investigation, treatment design, and treatment validation — and is a subset of the full engineering cycle

- **Suggested for:** Ch 2.4 ¶2 (why DSR fits this project); Ch 3.1 ¶3 (phases table)
- **Direkte sitat:** "The design cycle consists of problem investigation, treatment design, and treatment validation. [...] Design science research projects do not perform the entire engineering cycle but are restricted to the design cycle." (pp. 27, 31 / PDF 39, 43)
- **Parafrase:** DSR restricts itself to the first three phases of the engineering cycle; the implementation and evaluation phases belong outside the research project.
- **Forbehold:** Wieringa explicitly notes that "transferring new technology to the market may be done after the research project is finished but is not part of the research project" (p.31 / PDF 43) — this frames the production deployment of Ressursplanlegger as post-research, not as a limitation in the negative sense.
- **Anvendelse på vårt case:** The three-phase design cycle maps directly onto the project: (1) problem investigation = interviews + requirements + fit/gap analysis; (2) treatment design = Ressursplanlegger architecture + algorithm; (3) treatment validation = benchmarking + requirements traceability. The absence of a production deployment is structurally expected in DSR, not a research flaw.

### Claim 3: Design science studies artefacts in context — the interaction between artefact and problem context is the object of study

- **Suggested for:** Ch 2.4 ¶1 (define DSR — artefact in context); Ch 3.1 ¶2 (why DSR fits)
- **Direkte sitat:** "Design science is the design and investigation of artifacts in context. The artifacts we study are designed to interact with a problem context in order to improve something in that context." (p. 3 / PDF 18)
- **Parafrase:** DSR's contribution is always relational — artefact alone is insufficient; the interaction between artefact and context is what matters.
- **Forbehold:** Wieringa's artefact concept is deliberately broad (algorithms, methods, conceptual structures) — the thesis must state explicitly that Ressursplanlegger is an artefact in this sense (a software system).
- **Anvendelse på vårt case:** Ressursplanlegger (artefact) is studied in interaction with the planning workflow of Norwegian traffic coordinators (problem context); the research question specifically asks how the system supports coordinators — i.e., how the artefact–context interaction improves the problem, which is exactly Wieringa's object of study definition.

### Claim 4: Validation research uses validation models — a model of the artefact interacting with a model of the problem context

- **Suggested for:** Ch 3.5 ¶3 (system validity justification); Ch 2.4 ¶3 (bridge from theory to method)
- **Direkte sitat:** "A validation model consists of model of the artifact interacting with a model of the problem context [...] The targets of a validation model are all possible artifact implementations interacting with real-world problem contexts." (p. 61 / PDF 73)
- **Parafrase:** Validation is not done on the real-world implementation but on a model of it; the results are then generalised by analogy to the population of possible real-world deployments.
- **Forbehold:** The page number for this claim is in Ch.7 (p.61 / PDF 73); it is a deeper elaboration of the concept introduced in §3.1.5. The thesis may cite only §3.1.5 and not need to cite Ch.7 explicitly unless the thesis discusses validation models in detail.
- **Anvendelse på vårt case:** The benchmarking datasets used to test Ressursplanlegger are a model of the problem context (synthetic fleet data representing typical transport-company planning instances); the running system under test is the artefact model. Benchmarking results generalise by analogy to potential real-world fleets.

### Claim 5: The key distinction between validation and evaluation is researcher control — in validation, researchers experiment with a model; in evaluation, stakeholders use the artefact independently

- **Suggested for:** Ch 3.5 ¶3; Ch 5.6 ¶2 (limitation framing)
- **Direkte sitat:** "The key point in distinguishing validation from evaluation is that in evaluation researchers study an artifact in the real world that is used by stakeholders independently from the researchers, whereas in validation, researchers experiment with a model of how stakeholders would use the artifact in the real world." (p. 34 / PDF 46 — footnote 3)
- **Parafrase:** Validation ≠ evaluation because of who controls the use: researchers control validation; stakeholders independently drive evaluation.
- **Forbehold:** This quote is from a footnote (p.34, note 3), not from the main text; it is nonetheless authoritative. Cite as (p. 34) — the footnote is on the printed page.
- **Anvendelse på vårt case:** In this thesis, no transport company operates Ressursplanlegger independently; all testing is researcher-controlled (benchmarking, requirements traceability). This makes the study a validation study, and the absence of independent stakeholder use is the structural reason — not merely a limitation to apologise for.

### Claim 6: Technical action research is a special case of validation research done in the field

- **Suggested for:** Ch 3.5 ¶3 (situating this thesis's methodology)
- **Direkte sitat:** "A special case is technical action research, which is a method to test a new artifact in the real world by using it to solve a real-world problem (Chap. 19). This is validation research, done in the field. The artifact is still under development and is not used by stakeholders independently from a research context." (p. 31 / PDF 43)
- **Parafrase:** Even field testing can be validation (not evaluation) if researchers remain in control and the artefact is not handed over to stakeholders independently.
- **Forbehold:** This claim is secondary — the thesis does not do TAR. It is useful only to close off a possible reader objection ("why not test in the field?") by showing that even TAR remains validation.
- **Anvendelse på vårt case:** The thesis did not conduct TAR; this claim is useful in Ch.5.6 to note that even a field pilot would have been validation (not evaluation) unless a company used the system independently.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Artifact | Ressursplanlegger (the software system) | Wieringa uses "artifact" broadly; in our case it is a web-based planning platform |
| Problem context | Planning workflow of Norwegian traffic coordinators | Includes coordinators, fleets, assignments, constraints |
| Treatment | Ressursplanlegger deployed for planning use | "Treatment" = the artifact interacting with the problem context |
| Stakeholders | Traffic coordinators, transport company management | Wieringa's stakeholders = anyone affected by the artifact |
| Design cycle | The three project phases: interviews → system design → benchmarking | Directly maps to problem investigation / treatment design / treatment validation |
| Validation | Benchmarking + requirements traceability (pre-deployment testing) | Validation methods used: single-case mechanism experiments |
| Evaluation | Production deployment where coordinators use the system independently | Not conducted in this thesis — framed as future work |
| Engineering cycle | Full cycle including production deployment and post-deployment evaluation | Only the design cycle (first 3 tasks) is in scope |
| Design theory | The thesis's claim that Ressursplanlegger improves planning efficiency | Generated by validation; to be confirmed by future evaluation |
| Implementation (Wieringa's sense) | Technology transfer = production deployment at a transport company | Different from "implementation" in software sense; clarify in thesis text |
| Single-case mechanism experiment | Algorithm benchmarking on synthetic datasets | Validation method; researcher-controlled; artefact exposed to modelled contexts |

## Forbehold og begrensninger

- **Wieringa does not use "validate" in the sense of "user acceptance testing" or "usability testing."** Validation in his framework is strictly about predicting whether the artefact would contribute to stakeholder goals if implemented — not about UX. The thesis should not cite Wieringa to justify usability claims.
- **The source does not address quantitative performance benchmarking specifically.** Wieringa's validation methods (expert opinion, mechanism experiments, TAR, statistical experiments) are general categories. The thesis must state explicitly that benchmarking is a single-case mechanism experiment in Wieringa's classification.
- **Wieringa does not address OR-tools, constraint programming, or algorithmic systems specifically.** Every application to the thesis's algorithm domain is an inference by the writer; the source itself provides only the methodological vocabulary.
- **The design cycle does not prescribe iterative development (agile).** Wieringa notes that agile development is a possible execution of the engineering cycle (p.32 / PDF 44), but this is a brief mention, not a treatment. Do not cite Wieringa to justify agile sprint structure — use Larman or another source.
- **No guidance on qualitative interview methodology.** Ch.5 mentions interviews as one tool for problem investigation but does not elaborate. For interview methodology, cite Kvale or Braun & Clarke.
- **Wieringa's framework is structurally compatible with Hevner et al. (2004) and Peffers et al. (2007), but they are not interchangeable.** Wieringa explicitly notes differences from Hevner et al. (p.7 / PDF 22: "This is similar to the framework of Hevner et al. [3], but it contains some important differences"). For the thesis, use Hevner (2004) for the general DSR framework and Wieringa (2014) for the validation-vs-evaluation distinction — do not mix their terminologies without noting the source.
- **The "MUST CITE: wieringa2014dsm" markers in outline.md appear in Ch 2.4 ¶3 and Ch 3.1 ¶4 and Ch 3.5 ¶3.** All three are confirmed supported by the source's actual content.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Design science | "Design science is the design and investigation of artifacts in context." | p. 3 / PDF 18 |
| Validation (of a treatment) | "To validate a treatment is to justify that it would contribute to stakeholder goals if implemented." | p. 31 / PDF 43 |
| Evaluation (of a treatment) | "evaluation [...] is the investigation of a treatment as applied by stakeholders in the field." | p. 31 / PDF 43 |
| Design cycle | "The design cycle consists of problem investigation, treatment design, and treatment validation." | p. 33 / PDF 45 (summary bullet) |
| Artifact | "An artifact is something created by people for some practical purpose." | p. 29 / PDF 41 |

## Rammeverk og modeller

### The Engineering Cycle (p. 27 / PDF 39)

Five-phase rational problem-solving cycle:

| Fase | Beskrivelse | Tilhører |
|---|---|---|
| Problem investigation | What phenomena must be improved? Why? | Engineering cycle + design cycle |
| Treatment design | Design artefact(s) that could treat the problem | Engineering cycle + design cycle |
| Treatment validation | Would these designs treat the problem? | Engineering cycle + design cycle |
| Treatment implementation | Apply the treatment to the original problem context | Engineering cycle only (outside DSR project) |
| Implementation evaluation | How successful was the treatment? May trigger new cycle | Engineering cycle only (outside DSR project) |

**Note:** Design science research projects are restricted to the first three phases (= the design cycle). Implementation and evaluation occur after the research project ends.

### The Design Cycle as a Subset (p. 30 / PDF 42)

> "With respect to real-world problems, design science projects are always restricted to the first three tasks of the engineering cycle: problem investigation, treatment design, and treatment validation. We call these three tasks the design cycle."

---

### Validation Research Methods (Ch. 7, pp. 63–67 / PDF 75–79)

Wieringa identifies four validation research methods:

| Method | Description | Side |
|---|---|---|
| Expert opinion | Experts imagine artefact in context and predict effects; useful for early weeding out of bad designs | p. 63 / PDF 75 |
| Single-case mechanism experiment | Researcher applies stimuli to a validation model and explains response via internal mechanisms; testing, simulation | p. 64 / PDF 76 |
| Technical action research (TAR) | Artefact prototype used in a real-world problem to help a client; validation in the field | p. 65 / PDF 77 |
| Statistical difference-making experiment | Compares average outcomes across samples; does not require mechanism understanding | p. 65 / PDF 77 |

**Relevant for thesis:** Benchmarking = single-case mechanism experiment. Expert opinion is not explicitly done. TAR and statistical experiments are not conducted.

## Key arguments / lines of reasoning

### Argument: Validation and evaluation require different research approaches because they have different goals

- **Premiss(er):** (1) Validation goal = predict how artefact interacts with context *without* observing a real-world implementation. (2) Evaluation goal = investigate how *implemented* artefacts interact with real-world context. (3) These goals presuppose different availability of data and different research contexts.
- **Konklusjon:** Validation is experimental/laboratory; evaluation is field research. A thesis that has not deployed a system is doing validation, not evaluation — this is a structural fact, not a deficit.
- **Sted:** (pp. 31–32 / PDF 43–44)
- **Hvilke claims dette støtter:** Ch 2.4 ¶3; Ch 3.1 ¶4; Ch 3.5 ¶3; Ch 5.6 ¶2

### Argument: DSR projects produce both a designed artefact and knowledge about artefact-in-context interactions

- **Premiss(er):** A design science project iterates over two activities: designing artefacts to help stakeholders, and empirically investigating artefact performance in context. Both activities produce outputs — a design and knowledge.
- **Konklusjon:** DSR's dual contribution is appropriate when a project both builds a tool and investigates its properties.
- **Sted:** (Preface, pp. v–vi / PDF 6–7; p. 3 / PDF 18)
- **Hvilke claims dette støtter:** Ch 2.4 ¶2 (why DSR fits this project — contribution is both artefact and knowledge)

### Argument: The design cycle does not prescribe execution sequence — agile iteration is a valid execution

- **Premiss(er):** The engineering cycle defines a logical structure of tasks, not a process order. Multiple execution sequences are valid.
- **Konklusjon:** Agile development (many sequential passes through the cycle) is one valid way to execute the design cycle.
- **Sted:** (p. 32 / PDF 44)
- **Hvilke claims dette støtter:** Ch 3.4 ¶1 (briefly — iterative development consistent with DSR)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| DOA (Direction of Arrival) project | Algorithm design and validation by simulation; multiple validation passes | pp. 3, 15, 62–63 / PDF 18, 27, 74–75 |
| DLC (Data Location Compliance) project | Method design validated by expert opinion from consultants | pp. 3, 28, 61–62 / PDF 18, 40, 73–74 |
| MARP (Multi-Agent Route Planning) | Algorithm validation via simulation of Schiphol airport | pp. 28, 64 / PDF 40, 76 |
| ARE (Agile Requirements Engineering) | Knowledge questions without artefact design goal | pp. 15, 44 / PDF 27, 56 |

Note: None of these examples are from transport logistics or driver assignment. All application to Ressursplanlegger is by analogy — as Wieringa's framework itself expects.

## Data og statistikk

*Kilden presenterer ingen statistikk — ren metodologisk teori.*

## Forfatter-perspektiv / metodologi

Wieringa writes as a methodology theorist drawing on philosophy of science (fallibilism, middle-range theory), industrial engineering, and information systems research. The book is explicitly prescriptive — it gives guidelines, not descriptions of practice. The framework is grounded in engineering tradition (engineering cycle from Cross, Roozenburg & Eekels) combined with design science literature (Hevner et al., Peffers et al.). The book is used widely as a methodology reference in IS/SE research.

## Spot-check verification

1. Quote "To validate a treatment is to justify that it would contribute to stakeholder goals if implemented." (p. 31 / PDF 43) — verified via `pdftotext -f 43 -l 43 context/docs/method/sources/raw/wieringa2014dsm.pdf` — **PASS** (quote appears verbatim in §3.1.5)

2. Quote "Design science is the design and investigation of artifacts in context." (p. 3 / PDF 18) — verified via `pdftotext -f 18 -l 18 context/docs/method/sources/raw/wieringa2014dsm.pdf` — **PASS** (quote appears verbatim in §1.1 opening)

3. Quote "The design cycle consists of problem investigation, treatment design, and treatment validation." (p. 33 / PDF 45) — verified via `pdftotext -f 45 -l 45 context/docs/method/sources/raw/wieringa2014dsm.pdf` — **PASS** (appears as summary bullet in §3.3)

4. Quote "The key point in distinguishing validation from evaluation is that in evaluation researchers study an artifact in the real world that is used by stakeholders independently from the researchers, whereas in validation, researchers experiment with a model of how stakeholders would use the artifact in the real world." (p. 34 / PDF 46) — verified via `pdftotext -f 46 -l 46 context/docs/method/sources/raw/wieringa2014dsm.pdf` — **PASS** (appears in footnote 3 on p.34)

**Result:** 4/4 quotes verified, 0 corrections made.