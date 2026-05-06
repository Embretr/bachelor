# The Ethics of Algorithms: Mapping the Debate (`mittelstadt2016algorithms`)

## Status
- [x] Notes generated from raw (Claude, 2026-05-01)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The paper is a 21-page journal article read in full. All sections relevant to the thesis (conceptual map, fairness, accountability, traceability, privacy, opacity) are covered. Remaining material (machine ethics debates about autonomous agents, GDPR regulatory detail) is outside the thesis's scope.
  - **Gaps not investigated:** None — full article read.

## Source metadata
- **BibTeX key:** `mittelstadt2016algorithms`
- **Reference (APA 7):** Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L. (2016). The ethics of algorithms: Mapping the debate. *Big Data & Society*, *3*(2), 1–21. https://doi.org/10.1177/2053951716679679
- **Tilgang:** Open access (CC BY-NC)
- **Raw source:** `../mittelstadt2016algorithms.pdf`
- **Coverage in raw:** Full article, pp. 1–21. Printed page numbers match PDF page numbers (no offset).

## Sammendrag (2–3 setninger)

Mittelstadt et al. (2016) propose a prescriptive conceptual map organising the ethics of algorithms into six types of concerns — three epistemic (inconclusive evidence, inscrutable evidence, misguided evidence) and three normative/overarching (unfair outcomes, transformative effects, traceability) — and review the academic literature to show how each type manifests in practice. The paper argues that algorithms are inescapably value-laden, that their opacity complicates accountability, and that harm is difficult to trace and assign to responsible parties. Its main contribution to our thesis is providing a structured, citable taxonomy for the ethical dilemmas in §5.3 (algorithmic fairness, accountability, privacy, working conditions) and a theoretical grounding for the accountability gap that Tillit/kontroll addresses via explicit override authority.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| §5.3 (Sustainability and ethical considerations) | Covered — primary match; fairness taxonomy, accountability gap, privacy, values in design |
| §5.1.2 Tillit/kontroll (accountability for algorithmic decisions) | Partial — accountability gap and de-responsibilisation directly relevant |
| §2.2 HITL (transparency / opacity) | Partial — opacity arguments support explanation-as-interface framing; primary citation there is Miller (2019) |
| §5.1.1 Effektivitet (whose efficiency?) | Partial — value-ladenness of objective functions (§5.3 ¶5) |

## Claims this source supports

### Claim 1: Algorithms are inescapably value-laden — their parameters privilege some values and interests over others

- **Suggested for:** §5.3 ¶5 (ethical considerations as substantive design issues — operator-vs-owner asymmetry as ethics question; whose efficiency, whose autonomy?)
- **Direkte sitat:** "Algorithms are inescapably value-laden (Brey and Soraker, 2009; Wiener, 1988). Operational parameters are specified by developers and configured by users with desired outcomes in mind that privilege some values and interests over others." (p. 1)
- **Parafrase:** Algorithms do not simply optimise neutrally; every design and configuration choice embeds a value judgement about what outcomes matter.
- **Forbehold:** The paper treats this as a foundational axiom rather than an empirical finding. It does not distinguish between algorithms with fixed parameters and algorithms with user-configurable weights.
- **Anvendelse på vårt case:** Ressursplanleggers soft-constraint weights — configured per company — institutionalise that company's priorities (e.g., prioritising driver preference vs. load balance vs. overtime reduction); the operator-vs-owner asymmetry means that *owners* set what the algorithm optimises for, not the coordinators who operate it — making the choice of objective function an ethical and not merely technical decision.

---

### Claim 2: The gap between designer control and algorithm behaviour creates an accountability gap

- **Suggested for:** §5.3 ¶3 (accountability dilemma — who is responsible for an algorithm-generated assignment that goes wrong?) + §5.1.2 ¶1 (Tillit/kontroll — coordinator override authority as resolution)
- **Direkte sitat:** "The gap between the designer's control and algorithm's behaviour creates an *accountability gap* (Cardona, 2008) wherein blame can potentially be assigned to several moral agents simultaneously." (p. 11)
- **Parafrase:** As algorithms become complex and semi-autonomous, responsibility for their outputs is distributed across developers, deployers, and operators — with no single party clearly responsible.
- **Forbehold:** The paper discusses this primarily for learning algorithms (ML) and automated decision systems; Ressursplanlegger is a rule-based + constraint solver system, so the "gap" is narrower — the algorithm's decision rules are explicit. The accountability gap still applies when the coordinator accepts an algorithm-generated plan without inspecting it.
- **Anvendelse på vårt case:** In Ressursplanlegger, the coordinator's explicit inspect/modify/accept/reject authority over every algorithm-generated assignment is the design response to the accountability gap — by requiring human approval, the system ensures that a human (not only the algorithm or Admmit) bears responsibility for the final plan; the deviation taxonomy surfaces what requires attention, reducing the risk of uninspected acceptance.

---

### Claim 3: Algorithmic harm is hard to debug and responsibility is hard to assign — traceability is the overarching ethical concern

- **Suggested for:** §5.3 ¶3 (accountability dilemma) + §5.3 ¶6 (limitations of the sustainability analysis)
- **Direkte sitat:** "harm caused by algorithmic activity is hard to debug (i.e. to detect the harm and find its cause), but also that it is rarely straightforward to identify who should be held responsible for the harm caused." (p. 5)
- **Parafrase:** Even when algorithmic harm is identified, tracing it to a specific actor or design decision is structurally difficult because harm is the product of many interacting components.
- **Forbehold:** The paper focuses on large-scale data processing and ML systems; Ressursplanlegger's scope (single-company, coordinator-controlled, non-ML) limits direct application. The traceability concern is real but at a smaller scale.
- **Anvendelse på vårt case:** For Ressursplanlegger, the deviation detection system functions as a partial traceability mechanism — surfacing when and why a specific assignment violated a rule (overtime, certification, availability). However, soft assignments (coordinators manually accepting a suboptimal plan) leave no algorithmic audit trail; §5.3 should acknowledge this as a design limitation.

---

### Claim 4: Designer values are frozen into algorithm code, effectively institutionalising them

- **Suggested for:** §5.3 ¶5 (operator-vs-owner asymmetry as an ethics question)
- **Direkte sitat:** "'the values of the author [of an algorithm], wittingly or not, are frozen into the code, effectively institutionalising those values'" (p. 7; citing Macnish, 2012: 158)
- **Parafrase:** Algorithm development is not neutral; the priorities and assumptions of the development team are encoded into the system and then applied to users who may not share those values.
- **Forbehold:** This quote is from Macnish (2012) cited by Mittelstadt et al. — when citing in the thesis, cite as Mittelstadt et al. (2016) via Macnish (2012) or simply as Mittelstadt et al. (2016, p. 7) as the source of the claim.
- **Anvendelse på vårt case:** Admmit's development team designed the constraint weights and scoring logic of Ressursplanlegger; the operator-vs-owner asymmetry means coordinators (the operators) did not define what the system optimises for — their values (e.g., local route knowledge, informal driver preferences) are not encoded in the algorithm unless exposed as configurable weights. This is an ethics issue as much as a design issue.

---

### Claim 5: Opacity makes meaningful human oversight of algorithmic decisions impossible under certain conditions

- **Suggested for:** §5.1.2 ¶3 (Miller — explanation as interface; opacity as design problem) + §5.3 ¶3 (privacy / accountability)
- **Direkte sitat:** "Meaningful oversight and human intervention in algorithmic decision-making 'is impossible when the machine has an informational advantage over the operator ... [or] when the machine cannot be controlled by a human in real-time due to its processing speed and the multitude of operational variables'" (p. 6; citing Matthias, 2004: 182–183)
- **Parafrase:** When algorithms are opaque — either technically inscrutable or simply faster and more data-intensive than human cognition — the theoretical possibility of human oversight does not guarantee practical oversight.
- **Forbehold:** The opacity concern is most acute for ML algorithms with black-box behaviour; Ressursplanlegger's constraint solver is not a black box (constraint violations are explicit), but the combinatorial scoring of the objective function may still be opaque to coordinators without explanation.
- **Anvendelse på vårt case:** Ressursplanlegger's deviation taxonomy and score-breakdown surface are the design response to this opacity concern — they make the algorithm's reasoning accessible to the coordinator *at the level of actionable information* (which assignments to inspect and why), operationalising the Miller (2019) principle of explanation-as-interface.

---

### Claim 6: Delegating decisions to algorithms can de-responsibilise human actors — causing them to assume automated outputs are correct by default

- **Suggested for:** §5.1.2 ¶1 (Tillit/kontroll — over-reliance risk) + §5.3 ¶3 (accountability dilemma)
- **Direkte sitat:** "substantial trust is already placed in algorithms, in some cases affecting a *de-responsibilisation* of human actors, or a tendency to 'hide behind the computer' and assume *automated* processes are correct by default (Zarsky, 2016: 121)." (p. 12)
- **Parafrase:** Humans working alongside algorithms can over-defer, accepting outputs without genuine review — undermining the value of the human-in-the-loop by making it a rubber-stamp rather than a substantive control.
- **Forbehold:** This is framed as a sociological observation about algorithmic systems broadly, not an empirical finding about specific systems. It applies to Ressursplanlegger as a risk, not a confirmed outcome.
- **Anvendelse på vårt case:** De-responsibilisation is the failure mode that the Tillit/kontroll anchor explicitly guards against — the coordinator's accept/reject authority is only meaningful if the system surfaces *what to inspect* (deviation alerts) and ensures the coordinator cannot accept en masse without review. This is a strong argument for the deviation taxonomy as a design necessity, not a nice-to-have.

---

### Claim 7: Algorithms can produce unfair outcomes (discrimination) even from neutral-appearing, non-discriminatory inputs — through profiling and proxy variables

- **Suggested for:** §5.3 ¶3 (fairness dilemma — algorithmic bias against drivers)
- **Direkte sitat:** "Profiling, broadly defined as 'the construction or inference of patterns by means of data mining and ... the application of the ensuing profiles to people whose data match with them' (Hildebrandt and Koops, 2010: 431), is frequently cited as a source of discrimination." (p. 8)
- **Parafrase:** Algorithms that group and classify individuals based on correlational patterns can treat people according to group characteristics rather than individual circumstances, producing discriminatory effects even without explicit discriminatory intent.
- **Forbehold:** The source discusses discrimination in the context of profiling for credit scoring, insurance, policing, etc. — population-scale, data-mining systems. Ressursplanlegger assigns individuals to tasks, which is structurally similar but smaller in scale and does not use profiling in the data-mining sense. The discrimination risk comes through a different mechanism (systematic overtime assignment, consistent preference for certain drivers due to weight configurations).
- **Anvendelse på vårt case:** In driver assignment, the fairness concern is that the algorithm's objective function — which balances workload, soft preferences, and efficiency — may consistently assign overtime or less desirable shifts to specific drivers due to the interaction of their constraints (e.g., limited vehicle certifications forcing repeated assignment to the same driver), not through intent but through structural optimisation; §5.3 should name this as a design dilemma, not just a theoretical risk.

---

### Claim 8: Informational privacy concerns individuals' capacity to control information about themselves — and algorithms challenge this by constructing identity from aggregated data

- **Suggested for:** §5.3 ¶3 (privacy — employee data handling)
- **Direkte sitat:** "Informational privacy concerns the capacity of an individual to control information about herself" (p. 9)
- **Parafrase:** Privacy is not only about protecting data from external access, but about individuals' ability to define and manage what information about them is collected, aggregated, and used in decisions affecting them.
- **Forbehold:** The paper's privacy discussion centres on consumer profiling, surveillance, and identity construction from behavioural data — more intrusive than Ressursplanlegger's use of driver availability, certifications, and work-history data. The privacy concern in our case is more conventional (employee data governance) than the paper's focus.
- **Anvendelse på vårt case:** Ressursplanlegger processes personal employee data (work schedules, sick-leave windows, certification expiry dates, overtime history) to generate assignments; §5.3 should address which categories of data the system collects, who can access them, and whether the multi-tenant isolation boundary prevents data about one company's drivers from being visible to another company — a conventional data protection question anchored in the Mittelstadt et al. privacy framing.

---

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Algorithm | Ressursplanlegger's solver engines (heuristic, CP-SAT, Timefold) + the overall assignment platform | The paper uses "algorithm" broadly (construct + implementation + configuration); in our case the "configured algorithm" is the solver with company-specific constraint weights |
| Data subjects | Drivers (sjåfører) + potentially vehicles as tracked assets | The primary data subjects are drivers whose personal data (availability, certifications, work history) are processed |
| Operator | Trafikkoordinator | The human in the loop who receives algorithm-generated assignments and can inspect/modify/accept/reject |
| Designer / developer | Admmit / the bachelor team | The party whose values are "frozen into the code" via constraint design and default weight choices |
| Profiling | Driver scoring / ranking in assignment algorithm | Ressursplanlegger scores and ranks driver-assignment pairings; not population-scale profiling but analogous in structure |
| Accountability gap | The space between coordinator acceptance and Admmit's algorithm design | Partially resolved by coordinator override authority; partially remains as a structural gap |
| Traceability | Deviation detection + assignment audit log | The system's deviation taxonomy is the primary traceability mechanism |
| Transparency | Score breakdown + deviation alerts | Accessibility and comprehensibility of the algorithm's decisions to the coordinator |
| De-responsibilisation | Blind acceptance of algorithm-generated plan | The failure mode that explicit accept/reject and deviation surfacing guards against |
| Unfair outcomes | Systematic overtime or preference-disadvantage for specific drivers | Structural effect of objective function optimisation, not intentional discrimination |
| Inconclusive / inscrutable evidence | Not directly applicable | Ressursplanlegger uses explicit rule-based constraints, not statistical inference — the epistemic concerns are less acute than for ML systems |

## Forbehold og begrensninger

- **ML-centric framing:** Most of the paper's analysis (especially epistemic concerns about inconclusive evidence and inscrutable evidence) is most acute for machine learning systems. Ressursplanlegger uses constraint programming and heuristics, not ML — the epistemic concerns are significantly less severe. Writers should not over-apply the opacity / black-box arguments.
- **Population-scale scope:** The paper's fairness and privacy discussions assume large-scale, population-affecting systems. Ressursplanlegger operates at company-level (dozens of drivers), which changes the severity and nature of the concerns. Direct application requires explicit scaling-down of claims.
- **No empirical findings about transport or similar domains:** The paper is theoretical and literature-mapping; it provides the conceptual vocabulary, not empirical evidence. Our thesis cannot claim that Ressursplanlegger has caused any of the described harms — only that the design should account for the risks.
- **Discrimination ≠ algorithmic profiling:** The discrimination concern in driver assignment does not arise from profiling (the paper's main mechanism) but from optimisation under heterogeneous constraints. Distinguish these two mechanisms in §5.3.
- **Accountability gap is narrower for rule-based systems:** Because Ressursplanlegger's constraint logic is explicit and auditable, the accountability gap is structurally smaller than for ML systems. This should be acknowledged — Ressursplanlegger's coordinator override authority narrows but does not eliminate the gap.
- **Outline §5.3 MUST CITE marker is confirmed:** Mittelstadt et al. (2016) does directly support the fairness / privacy taxonomy framing in §5.3 ¶3. The fit is correct.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Informational privacy | "Informational privacy concerns the capacity of an individual to control information about herself" | p. 9 |
| Transparency (primary components) | "The primary components of transparency are *accessibility* and *comprehensibility* of information." | p. 6 |
| Transparency (full definition) | "Transparency is generally defined with respect to 'the availability of information, the conditions of accessibility and how the information ... may pragmatically or epistemically support the user's decision-making process'" (citing Turilli and Floridi, 2009: 106) | p. 6 |
| Accountability gap | "The gap between the designer's control and algorithm's behaviour creates an *accountability gap* (Cardona, 2008) wherein blame can potentially be assigned to several moral agents simultaneously." | p. 11 |
| Profiling | "the construction or inference of patterns by means of data mining and ... the application of the ensuing profiles to people whose data match with them" (citing Hildebrandt and Koops, 2010: 431) | p. 8 |

## Rammeverk og modeller

### Six-type conceptual map of ethical concerns raised by algorithms (p. 4)

The paper's central contribution. The map is intended as a prescriptive organising framework, not a theoretical model from a single domain.

| Type | Category | Description | Relevant to thesis |
|---|---|---|---|
| Inconclusive evidence | Epistemic | Algorithms produce probable but uncertain knowledge; correlations without causation | Low — CP-SAT uses explicit constraints, not statistical inference |
| Inscrutable evidence | Epistemic | Opacity of algorithm's decision-making logic; "black box" problem | Moderate — objective function scoring is not always legible to coordinator |
| Misguided evidence | Epistemic | Algorithm output cannot exceed input quality; bias in data produces bias in output | Moderate — if driver data (availability, constraints) is incomplete, assignments will be suboptimal or unfair |
| Unfair outcomes | Normative | Discriminatory effects from biased evidence or profiling, even with neutral intent | High — systematic assignment disadvantage for constrained drivers |
| Transformative effects | Normative | Algorithms change how identity, autonomy, and privacy are constructed; nudging effects | Low-moderate — Ressursplanlegger doesn't construct driver identity, but does constrain coordinators' decision space |
| Traceability | Overarching | Difficulty of identifying, attributing, and remedying algorithmic harm | High — accountability gap in accepted-but-unchecked plans; deviation taxonomy is partial response |

## Key arguments / lines of reasoning

### Argument: Algorithmic ethics cannot be solved by technical fixes alone — they require multi-dimensional solutions

- **Premiss(er):** Ethical concerns with algorithms are multi-dimensional (epistemic + normative + traceability); solving one level does not address others. A perfectly auditable, scrutable algorithm can still cause unfair outcomes.
- **Konklusjon:** "ethical concerns with algorithms are multi-dimensional and thus require multi-dimensional solutions" (p. 12)
- **Sted:** (p. 12)
- **Hvilke claims dette støtter:** §5.3 ¶6 (limitations of the sustainability analysis — the analysis is analytical, not empirical)

### Argument: De-responsibilisation is a systemic risk when humans defer to algorithmic authority

- **Premiss(er):** Algorithms receive substantial trust; humans tend to assume automated outputs are correct by default; this reduces feelings of personal responsibility.
- **Konklusjon:** This creates risk of "hiding behind the computer" — formal accountability structures (like coordinator override authority) can counteract this but require active design.
- **Sted:** (p. 12)
- **Hvilke claims dette støtter:** §5.1.2 ¶1 (Tillit/kontroll — coordinator authority as design response to de-responsibilisation)

### Argument: Values are embedded at design time, not only at use time

- **Premiss(er):** Development is not neutral; algorithm design reflects the values of the development team (and client). Parameters configured by users layer additional values on top.
- **Konklusjon:** "the values of the author [of an algorithm], wittingly or not, are frozen into the code, effectively institutionalising those values" (p. 7)
- **Sted:** (p. 7)
- **Hvilke claims dette støtter:** §5.3 ¶5 (operator-vs-owner asymmetry as an ethics question)

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Credit scoring algorithms | Unfair outcomes from opaque decision logic affecting individuals' access to financial services | pp. 6, 9 |
| Predictive policing | Discrimination through proxy variables; algorithmic harm affecting populations | pp. 5, 8 |
| Facebook EdgeRank | Designer-set weights encoding values about what content users see; traceability of responsibility | p. 10 |
| GDPR Art. 22 — right to human intervention | Regulatory response to algorithmic decision-making; explainability requirements | pp. 13–14 |

*Note: None of these examples are from transport or resource scheduling; all require domain bridging.*

## Data og statistikk

Kilden presenterer ingen statistikk — dette er en konseptuell og litteratur-kartlegging artikkel.

## Forfatter-perspektiv / metodologi

Literature review supplemented by conceptual map construction; the review covered academic literature explicitly discussing the ethical aspects of algorithms (search strategy described in Appendix 1, not reproduced in the main text). The paper's goal is prescriptive (providing an organising map) and descriptive (cataloguing themes in existing literature), not empirical. Authors are from Oxford Internet Institute and Alan Turing Institute — philosophy of information / AI ethics perspective.

## Spot-check verification

1. Quote "Algorithms are inescapably value-laden" (p. 1) — verified via `pdftotext -f 1 -l 1 mittelstadt2016algorithms.pdf` — **PASS** (line 53: "Algorithms are inescapably value-laden (Brey and")
2. Quote "harm caused by algorithmic activity is hard to debug... rarely straightforward to identify who should be held responsible" (p. 5) — verified via `pdftotext -f 5 -l 5` — **PASS** (line 43: "also that it is rarely straightforward to identify who")
3. Quote "The gap between the designer's control and algorithm's behaviour creates an accountability gap" (p. 11) — verified via `pdftotext -f 11 -l 11` — **PASS** (line 26: "between the designer's control and algorithm's behaviour creates an accountability gap (Cardona, 2008)")
4. Quote "substantial trust is already placed in algorithms, in some cases affecting a de-responsibilisation of human actors" (p. 12) — verified via `pdftotext -f 12 -l 12` — **PASS** (lines 86–87)
5. Quote "values of the author [of an algorithm], wittingly or not, are frozen into the code, effectively institutionalising those values" (p. 7) — verified via `pdftotext -f 7 -l 7` — **PASS** (lines 70–71)

**Result:** 5/5 quotes verified, 0 corrections made.