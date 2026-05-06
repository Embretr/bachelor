# Guidelines for Human-AI Interaction (`amershi2019guidelines`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** Short 13-page conference paper read in full. All 18 guidelines reviewed; relevant ones extracted with verbatim quotes. All areas of interest investigated.
  - **Gaps not investigated:** None — paper read cover to cover.

## Source metadata
- **BibTeX key:** `amershi2019guidelines`
- **Reference (APA 7):** Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for human-AI interaction. *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*, 1–13. https://doi.org/10.1145/3290605.3300233
- **Tilgang:** PDF
- **Raw source:** `../amershi2019guidelines.pdf`
- **Coverage in raw:** Full paper (13 pages). No supplementary materials.
- **Page note:** Conference paper — printed page = PDF page (no front-matter offset). Single page format used throughout: (p. N).

## Sammendrag (2–3 setninger)

Amershi et al. (2019) propose 18 empirically validated design guidelines for human-AI interaction, derived from over 150 design recommendations and validated through three rounds of evaluation including a user study with 49 HCI practitioners across 20 AI-infused products. The guidelines are organized by when during interaction they apply: initially (expectation-setting), during interaction (contextual relevance), when wrong (correction and dismissal), and over time (adaptation and feedback). For this thesis, the most directly applicable guidelines govern error correction (G9), explainability (G11), capability transparency (G1–G2), and global user control (G17) — all of which are operationalized in Ressursplanlegger's HITL design.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.2 (Human-in-the-Loop Automation) | Covered — G9 (correction), G11 (explainability), G1–G2 (expectations), G17 (global controls) directly frame the suggest+override model |
| Ch 2.2 ¶4 (Trust and adoption) | Covered — paper addresses trust erosion from unpredictable AI behavior and the role of calibrated expectations |
| Ch 5.2 (Algorithm Performance and HITL) | Partial — G11's high violation rate across real products is a useful design benchmark for Ressursplanlegger |
| Ch 5.3 (Adoption Barriers) | Partial — trust erosion from opaque AI behavior supports the adoption barrier argument |
| Ch 5.5 ¶5 (Ethical considerations) | Covered — paper explicitly notes its ethical limitations (G5, G6 only begin to touch fairness) |
| Ch 2.2 ¶1 (Parasuraman automation levels) | Outside scope — this paper does not use Parasuraman's framework |

## Claims this source supports

### Claim 1: AI systems must make their reasoning transparent so users can correct errors and maintain trust (G11)

- **Suggested for:** Ch 2.2 ¶5 (HITL as design constraint — system must expose reasoning) — primary; Ch 5.2 ¶3 (connect to HITL theory) — secondary
- **Direkte sitat:** "Make clear why the system did what it did. Enable the user to access an explanation of why the AI system behaved as it did." (p. 3, Table 1)
- **Direkte sitat (empirisk funn):** "Guideline 11 'Make clear why the system did what it did' had one of the highest number of violations, despite the large volume of active research in the area of intelligibility and explanations." (p. 9)
- **Parafrase:** Explainability is both a recognized design requirement and a widely unmet one in deployed AI products — even as research on explanations grows, systems frequently fail to expose their reasoning in usable ways.
- **Forbehold:** Finding is from consumer-facing products (navigation, recommenders) — the stakes and frequency of use differ from a B2B planning system. Coordinators may demand more detailed reasoning than typical consumer users.
- **Anvendelse på vårt case:** Ressursplanlegger's conflict detection interface (showing which constraint a driver violates — wrong competency, unavailability, overtime limit) directly implements G11; the thesis can cite Amershi et al.'s empirical finding that G11 is frequently violated in deployed products to motivate why making constraint reasoning visible was a deliberate design priority in Ressursplanlegger.

---

### Claim 2: AI systems must support efficient correction when they are wrong (G9)

- **Suggested for:** Ch 2.2 ¶3 (the "suggest + override" design pattern) — primary
- **Direkte sitat:** "Support efficient correction. Make it easy to edit, refine, or recover when the AI system is wrong." (p. 3, Table 1)
- **Parafrase:** When an AI system produces an incorrect or unacceptable output, the user must be able to fix it with minimal friction — editing, refining, or recovering should be a first-class interaction, not an afterthought.
- **Forbehold:** "Efficient" is not quantified — what counts as efficient varies by domain. In a planning context, one-step correction (drag-and-drop reassignment) is a reasonable benchmark.
- **Anvendelse på vårt case:** G9 operationalizes Ressursplanlegger's suggest+override design — the planning interface must allow trafikkoordinatoren to reassign any algorithm-generated assignment, remove it, or replace it in as few interactions as possible; this guideline provides the normative HCI foundation for that design requirement.

---

### Claim 3: AI systems must set transparent expectations about capability and error rates (G1, G2)

- **Suggested for:** Ch 2.2 ¶4 (trust and adoption — coordinators need calibrated expectations) — primary; Ch 5.3 ¶2 (trust in algorithm output) — secondary
- **Direkte sitat G1:** "Make clear what the system can do. Help the user understand what the AI system is capable of doing." (p. 3, Table 1)
- **Direkte sitat G2:** "Make clear how well the system can do what it can do. Help the user understand how often the AI system may make mistakes." (p. 3, Table 1)
- **Parafrase:** Users need two distinct pieces of information: what the system can do (scope of capability) and how reliably it does it (quality of output). Conflating these or omitting either leads to miscalibrated trust.
- **Forbehold:** G1 and G2 were among the most misinterpreted guidelines in the user study — participants confused them with each other — suggesting they are harder to implement distinctly than they appear.
- **Anvendelse på vårt case:** Ressursplanlegger exposes three solvers with different speed-quality tradeoffs (greedy, CP-SAT, Timefold); G1+G2 imply the interface should communicate which solver is active, what size of problem it handles, and what the expected solution quality is — so coordinators calibrate their trust correctly rather than treating all algorithm outputs as equally reliable.

---

### Claim 4: AI systems must provide global controls for users to customize behavior (G17)

- **Suggested for:** Ch 2.2 ¶5 (HITL as design constraint) — primary; Ch 4.4 system description — secondary
- **Direkte sitat:** "Provide global controls. Allow the user to globally customize what the AI system monitors and how it behaves." (p. 3, Table 1)
- **Parafrase:** Beyond instance-level corrections (G9), users need the ability to configure the AI system's behavior globally — adjusting what it optimizes for, what it monitors, and how it behaves across all future outputs.
- **Forbehold:** "Global" means affecting all future instances — not to be confused with G15 (granular, per-interaction feedback). The authors revised G17 specifically because participants confused it with G15.
- **Anvendelse på vårt case:** Ressursplanlegger's configurable soft constraint weights (workload balance, driver preference matching, assignment priority) are a direct implementation of G17 — coordinatoren can globally tune the algorithm's optimization priorities rather than correcting outputs one by one; citing G17 grounds this design decision in HCI theory.

---

### Claim 5: Unpredictable AI behavior erodes user confidence and leads to abandonment

- **Suggested for:** Ch 2.2 ¶4 (trust and adoption) — primary; Ch 5.3 ¶2 (trust in algorithm output) — secondary
- **Direkte sitat:** "Inconsistent and unpredictable behaviors can confuse users, erode their confidence, and lead to abandonment of AI technology [7, 22]." (p. 2)
- **Direkte sitat (context):** "[These guidelines] can help with the design and evaluation of AI-infused systems that people can understand, trust, and can engage with effectively." (p. 2)
- **Parafrase:** AI systems that produce variable or inexplicable outputs undermine user confidence even when individual outputs are correct — consistency and predictability are preconditions for trust.
- **Forbehold:** This claim draws on Amershi et al.'s synthesis of prior work (citing [7, 22]) rather than presenting original data.
- **Anvendelse på vårt case:** For Ressursplanlegger, this motivates the G14 guideline (update and adapt cautiously) — if the algorithm's behavior changes unpredictably between planning sessions (e.g., after weight changes), coordinatorer may abandon the system even if individual outputs are better; predictable behavior is a trust prerequisite.

---

### Claim 6: Guidelines for AI interaction require specialization beyond generality for high-stakes or domain-specific systems

- **Suggested for:** Ch 5.5 ¶5 (ethical considerations — limitations of guideline-based approaches) — primary; Ch 5.6 (limitations) — secondary
- **Direkte sitat:** "We recognize that there is a tradeoff between generality and specialization, and that these guidelines might not adequately address all types of AI-infused systems." (p. 11)
- **Direkte sitat:** "Our work also intentionally focused on AI design guidelines that we believed could be easily evaluated by inspection of a system's interface. For example, we excluded broad principles such as 'build trust', and focused instead on specific and observable guidelines that are likely to contribute to building trust." (p. 11)
- **Parafrase:** The 18 guidelines are designed for interface-observable behaviors in consumer AI products. They do not cover model-level design, highly regulated domains (surgery, financial systems), or products that lack graphical UIs.
- **Forbehold:** Authors explicitly identify semi-autonomous vehicles, robot-assisted surgery, and financial systems as requiring additional specialized guidelines. Industrial planning systems share properties with these high-stakes domains.
- **Anvendelse på vårt case:** When Ch 5.5 discusses ethical considerations, citing this limitation helps bound the scope — Amershi et al.'s G5 (social norms) and G6 (social biases) are of limited applicability to Ressursplanlegger, while G9, G11, and G17 translate well; the thesis should cite only the applicable subset rather than the full framework.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| AI-infused systems | Ressursplanlegger | Paper focuses on consumer apps; Ressursplanlegger is a B2B domain-expert tool |
| User | Trafikkoordinator | Single expert user, not general public |
| AI system's actions / services | Algorithm-generated assignment plan | Discrete, reviewable plan — not continuous/proactive like recommendations |
| Correction (G9) | Manual override of assignment | Drag-and-drop reassignment, removal, or replacement |
| Efficient dismissal (G8) | Ignoring a suggested assignment | Coordinator keeps manual assignment instead |
| Disambiguation (G10) | Conflict detection and resolution | System shows constraint violations, coordinator resolves |
| Global controls (G17) | Configurable soft constraint weights | Per-system settings that affect all future generated plans |
| Explanation of behavior (G11) | Constraint reasoning / conflict detail | Why a driver was or was not assigned (competency, availability, overtime) |
| Proactive action / interrupt (G3) | Not applicable | Ressursplanlegger is pull-based (coordinator initiates planning) |
| Social norms (G5), social biases (G6) | Limited applicability | Relevant to fairness across driver assignments but not the paper's intended scope |

## Forbehold og begrensninger

- **Consumer vs. B2B context:** All 20 products tested are consumer-facing (navigation, music recommenders, email, social networks). Ressursplanlegger is a domain-expert B2B tool — the stakes, frequency of use, user expertise, and error costs are fundamentally different. Guidelines like G5 (social norms) and G6 (social biases) have limited direct applicability.
- **Interface-only scope:** The paper explicitly excludes AI model-level design decisions. All 18 guidelines concern observable interface behaviors. Claims cannot be used to justify algorithm design choices — only UI/UX choices.
- **No high-stakes or regulated domains:** Paper authors acknowledge these guidelines are insufficient for high-stakes systems. Ressursplanlegger affects driver working conditions and labour law compliance — a higher-stakes context than music recommendations.
- **G3 (time services based on context) not applicable:** Ressursplanlegger is a pull-based system — the coordinator initiates planning, the system does not proactively interrupt.
- **G5 and G6 (social norms, social biases) — limited applicability:** These are relevant to fairness in driver assignment (equity of workload), but the paper's operationalization concerns consumer UX norms and stereotype reinforcement in NLP/recommendation contexts, not labour fairness.
- **No MUST CITE markers in outline.md for this bibkey:** This source was selected for extraction based on content relevance to Ch 2.2 (HITL design). The writer agent should place it under Ch 2.2 ¶3 and ¶5 primarily.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| AI-infused systems | "systems that have features harnessing AI capabilities that are directly exposed to the end user" (footnote 1) | p. 1 |
| G9 — Support efficient correction | "Make it easy to edit, refine, or recover when the AI system is wrong." | p. 3 |
| G11 — Make clear why | "Enable the user to access an explanation of why the AI system behaved as it did." | p. 3 |
| G17 — Provide global controls | "Allow the user to globally customize what the AI system monitors and how it behaves." | p. 3 |

## Rammeverk og modeller

### 18 Human-AI Interaction Design Guidelines (p. 3, Table 1)

Organized by temporal phase of interaction:

| Phase | Guidelines | Core concern |
|---|---|---|
| Initially | G1 (capabilities), G2 (performance limits) | Setting expectations before use |
| During interaction | G3 (context timing), G4 (contextual info), G5 (social norms), G6 (bias mitigation) | In-session relevance and appropriateness |
| When wrong | G7 (efficient invocation), G8 (efficient dismissal), G9 (efficient correction), G10 (scope in doubt), G11 (explain behavior) | Error handling and recovery |
| Over time | G12 (remember interactions), G13 (learn from behavior), G14 (adapt cautiously), G15 (granular feedback), G16 (convey consequences), G17 (global controls), G18 (notify changes) | Long-term adaptation and transparency |

**Most applicable to Ressursplanlegger:** G1, G2, G9, G11, G17 (and G8, G10 as secondary).
**Not applicable or low relevance:** G3, G5, G6, G12–G13 (no persistent learning in Ressursplanlegger), G18.

**Development process:** Guidelines derived from 150+ recommendations → affinity diagramming → 20 concepts → heuristic evaluation (11 internal evaluators, 13 products) → user study (49 HCI practitioners, 20 products) → expert evaluation (11 UX experts). Four-phase validation process.

## Key arguments / lines of reasoning

### Argument: Consistency and predictability are preconditions for AI trust

- **Premisser:** AI systems frequently produce unpredictable outputs due to probabilistic models, learning over time, and context sensitivity. Users cannot apply traditional UI principles (consistency, error prevention) to AI systems.
- **Konklusjon:** Unpredictable and inconsistent AI behavior erodes confidence and causes abandonment, even when individual outputs are correct.
- **Sted:** (p. 2)
- **Hvilke claims dette støtter:** Ch 2.2 ¶4 (trust and adoption); Claim 5 above

### Argument: G11 (explainability) is widely violated despite being widely recognized as important

- **Premisser:** The study found that G11 had "one of the highest numbers of violations" across the 20 products tested, while also having very few "does not apply" responses — meaning participants could identify where explanations should appear but were absent.
- **Konklusjon:** Explainability in AI systems is a recognized need that the industry consistently fails to implement — making it a genuine design challenge rather than a solved problem.
- **Sted:** (p. 9)
- **Hvilke claims dette støtter:** Ch 2.2 ¶5 (HITL as design constraint); Claim 1 above

### Argument: Interface-observable guidelines cannot substitute for model-level ethics

- **Premisser:** Guidelines were selected to be evaluable "by inspection of a system's interface." Broad principles like "build trust" were excluded as not actionable at the interface level.
- **Konklusjon:** The 18 guidelines begin to address but do not fully cover fairness and ethical concerns — additional specialized guidelines may be needed for high-stakes domains.
- **Sted:** (pp. 11–12)
- **Hvilke claims dette støtter:** Ch 5.5 ¶5 (ethical limitations); Claim 6 above

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Navigation app — "Route chosen based on Fastest Route, shown in subtext" | Application of G11 (make clear why) — route explanation visible in UI | p. 3 |
| Music recommender — "No explanation for why this particular song was recommended" | Violation of G11 — no reasoning exposed to user | p. 9 |
| Photo organizer — "Allows users to turn on location history so AI can group photos by where you have been" | Application of G17 (global controls) — user configures AI behavior globally | p. 3 |
| E-commerce — "Feature is unobtrusive, easy to scroll past, easy to ignore" | Application of G8 (efficient dismissal) — AI suggestion easy to bypass | p. 3 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 785 examples of the 18 guidelines | applications + violations across 20 products | 2019, 49 HCI practitioners | p. 7 |
| 313 applications, 277 violations, 89 neutrals, 106 "does not apply" | counts after deduplication and adjustment | 2019, 49 HCI practitioners | p. 7 |
| G11 among highest violation counts | qualitative finding (see Figure 1b) | 2019, 20 products | p. 9 |

## Forfatter-perspektiv / metodologi

Microsoft Research study conducted by 13 authors across Microsoft and University of Washington. Guideline development used affinity diagramming on 150+ existing design recommendations, followed by three validation rounds (internal heuristic evaluation, external user study with 49 HCI practitioners, expert evaluation with 11 UX experts). The paper explicitly positions itself as synthesizing prior HCI work into actionable guidelines, not as presenting new empirical findings about AI systems' effects on users.