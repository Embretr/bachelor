# Understanding Perception of Algorithmic Decisions (`lee2018understanding`)

## Status
- [x] Notes generated from raw (Claude, 2026-05-01)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** All 16 pages read in full. The article is a self-contained empirical study; the abstract, theory sections, results, discussion, implications, and conclusion have all been extracted. All thesis-relevant areas (§2.2 HITL trust foundation, §5.1.2 Tillit/kontroll, §5.3 algorithmic fairness / ethical considerations) are covered with verbatim quotes and page references.
  - **Gaps not investigated:** References section (pp. 14–16) — not analytically relevant; only cross-referenced to confirm the Lee & See (2004) citation the article builds on.

## Source metadata
- **BibTeX key:** `lee2018understanding`
- **Reference (APA 7):** Lee, M. K. (2018). Understanding perception of algorithmic decisions: Fairness, trust, and emotion in response to algorithmic management. *Big Data & Society*, *5*(1), 1–16. https://doi.org/10.1177/2053951718756684
- **Tilgang:** Open access (CC BY-NC-ND 4.0)
- **Raw source:** `../lee2018understanding.pdf`
- **Coverage in raw:** Full 16-page article. Printed page numbers 1–16 match PDF pages 1–16 exactly (no front-matter offset).

## Sammendrag (2–3 setninger)

Lee (2018) investigates how people perceive algorithmic versus human managerial decisions across tasks that require either "mechanical" or "human" skills, finding that algorithmic and human decisions are trusted and judged equally fair for mechanical tasks, but algorithmic decisions are perceived as less fair, less trustworthy, and more negatively emotional for human-skill tasks. The authority attributed to algorithms differs from that attributed to humans: algorithm authority is grounded in perceived efficiency and objectivity, while human managerial authority rests on positional legitimacy and social recognition. For our thesis, this is the foundational empirical study establishing the task-type-contingency of algorithm trust, and the one source in the theory stack that directly operationalises *why* a coordinator's override authority matters for coordinator trust — a coordinator assignment involves tacit judgment, not mere mechanical sorting.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.2 ¶5 (Lee — trust foundation for automation adoption) | covered — this IS the source; defines trust, establishes task-type contingency |
| Ch 5.1.2 ¶2 (Hoff & Bashir layered with Lee) | covered — Lee is the foundational layer; Hoff & Bashir refines it |
| Ch 5.3 ¶3 (algorithmic fairness / worker-conditions dilemma) | covered — fairness, dehumanisation, tracking-as-monitoring findings directly relevant |
| Ch 2.2 ¶2 (Bainbridge operator-vs-owner asymmetry) | partial — Lee does not address operator-vs-owner asymmetry; the workers studied are subject to algorithmic decisions, not operators of the algorithm. Note the distinction. |
| Ch 1.2 / 1.3 (general HITL framing) | outside scope — Lee does not theorise HITL design; studies *worker perceptions* of algorithmic management, not coordinator-as-operator design |

## Claims this source supports

### Claim 1: "Trust in algorithmic decisions is contingent on task type — equal to human trust for mechanical tasks, lower than human trust for tasks perceived to require human judgment"

- **Suggested for:** Ch 2.2 ¶5 (Lee trust foundation); Ch 5.1.2 ¶2 (Tillit/kontroll discussion, layered with Hoff & Bashir); Ch 5.3 ¶3 (ethical/fairness dilemma)
- **Direkte sitat:** "Trust can be defined as the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability. [...] With automation technology such as algorithms, establishing the right level of trust, or how much people believe in the reliability and accuracy of the technology's performance, can be a challenge, which can deter the adoption and efficacy of the technology (Lee and See, 2004)." (p. 4)
- **Parafrase:** Trust in algorithmic systems is not uniformly positive or negative; whether people trust algorithmic decisions as much as human decisions depends on whether the task is perceived as mechanical (where algorithms are trusted equally) or as requiring human judgment (where algorithms are trusted less).
- **Forbehold:** Study was conducted with US Amazon Mechanical Turk workers responding to hypothetical workplace scenarios — not actual coordinators or operators of planning tools. Findings are preliminary and scenario-based.
- **Anvendelse på vårt case:** Driver-and-vehicle assignment involves tacit coordinator judgment (who works well with whom, which driver handles sick-leave calls calmly, which vehicle a driver prefers) — the task sits in Lee's "human skills" category, meaning coordinators' default trust in Ressursplanlegger's algorithm-generated plan will be lower than trust in their own judgment; this is precisely why the inspect/modify/accept/reject override surface (Tillit/kontroll) is not optional decoration but a structural precondition for adoption.

### Claim 2: "The source of authority attributed to algorithmic versus human decisions differs even when perceived trust and fairness are equal"

- **Suggested for:** Ch 2.2 ¶5; Ch 5.1.2 ¶2; Ch 5.3 ¶5 (operator-vs-owner asymmetry as ethics question)
- **Direkte sitat:** "the source of authority in decisions varied depending on the decision-maker: the manager's authority was attributed to their position in the organization, whereas the algorithm's authority was attributed to its efficiency and lack of bias." (p. 13)
- **Parafrase:** Even when trust levels are equal, the *legitimacy basis* differs — human authority derives from positional accountability, algorithmic authority from procedural objectivity. This has implications for accountability when decisions go wrong.
- **Forbehold:** Observed in a scenario-based experiment; does not test actual coordinators' attributions in a planning tool context.
- **Anvendelse på vårt case:** When Ressursplanlegger's algorithm generates an assignment plan that the coordinator accepts, the basis of that plan's legitimacy matters for accountability: if coordinators accept plans because "the algorithm is objective" without understanding the constraints applied, accountability gaps emerge. This motivates the deviation-alert surface and the scoring breakdown in Ressursplanlegger — making the algorithm's basis of authority visible so coordinators can inspect and accept or reject on informed grounds, not on perceived objectivity alone.

### Claim 3: "Algorithms are perceived negatively when they appear unable to handle exceptions, non-quantifiable human properties, or contextual nuance"

- **Suggested for:** Ch 5.1.2 ¶4 (tacit knowledge as irreducible coordinator role); Ch 5.3 ¶3 (fairness and working-conditions dilemma)
- **Direkte sitat:** "algorithms' inability to accommodate exceptions, measure human properties commonly believed to be non-quantifiable (such as social interactions and personalities), or consider human concerns such as empathy and personal commitments, all of which contributed to distrust of algorithms and feelings of unfairness." (p. 14)
- **Parafrase:** Distrust of algorithms in managerial contexts is grounded in perceived incapacity to handle tacit, contextual, and human-relational factors — a perception that is not irrational.
- **Forbehold:** Framed from the perspective of workers being managed by algorithms, not operators using algorithms as decision-support tools. The distrust dynamic is about being subject to algorithmic authority, not about using it.
- **Anvendelse på vårt case:** Trafikkoordinatorer know contextually relevant factors (a driver's recent personal stress, a vehicle's mechanical idiosyncrasy, a route's informal complexity) that do not appear in any constraint model. Lee's finding that distrust arises precisely when these factors are not accommodated reinforces why Ressursplanlegger's HITL surface must give coordinators the ability to override any assignment: the algorithm generates from explicit constraints; the coordinator corrects from tacit ones. This maps to Tillit/kontroll's four actions (inspect, modify, accept, reject).

### Claim 4: "Algorithmic decisions in management contexts evoke concern about surveillance and loss of agency among workers"

- **Suggested for:** Ch 5.3 ¶3 (algorithmic fairness and working-conditions dilemma); Ch 5.3 ¶5 (ethics as substantive design issue)
- **Direkte sitat:** "Some expressed concern about having an algorithm as a decision-maker in the workplace, as the algorithm might make employees feel that they lacked 'agency' (P121) or were 'being watched' (P113)." (p. 11)
- **Parafrase:** Workers interpret algorithmic management not only as neutral optimisation but as a monitoring and surveillance mechanism, triggering concerns about agency and autonomy.
- **Forbehold:** This dynamic concerns workers who are *subjects* of the algorithm's decisions (employees being assigned, scheduled, evaluated). In Ressursplanlegger, the coordinator is the *operator* of the algorithm, not its subject — this is a different power relationship. However, drivers whose assignments are generated algorithmically are in Lee's "subject" position.
- **Anvendelse på vårt case:** Drivers in Norwegian transport companies whose assignments are generated by Ressursplanlegger are in the position Lee studies — they are subjects of algorithmic management, not its operators. The concern about surveillance and agency applies to how Ressursplanlegger affects driver experience, not just coordinator experience. This is a legitimate fairness and working-conditions dilemma to name in §5.3, distinct from the coordinator trust discussion in §5.1.2.

### Claim 5: "Perceptions of algorithmic decisions, regardless of actual performance, can significantly influence adoption"

- **Suggested for:** Ch 2.2 ¶5 (trust as adoption precondition); Ch 5.2 ¶1 (adoption and deployment implications)
- **Direkte sitat:** "Perceptions of algorithms, regardless of the algorithms' actual performance, can significantly influence their adoption." (p. 1, abstract)
- **Parafrase:** Adoption barriers for algorithmic systems are perception-driven, not performance-driven — a system can perform well and still fail adoption if perceptions of its fairness, trustworthiness, or legitimacy are low.
- **Forbehold:** This is from the abstract as a framing claim; the study itself tests perception dimensions but does not directly measure adoption decisions.
- **Anvendelse på vårt case:** For Ressursplanlegger, this means that even if the multi-engine solver produces provably better plans than manual assignment, coordinator adoption will depend on their perceived trust in the system's decisions — especially for tasks they regard as requiring human judgment (assignment involving tacit criteria). This reinforces the need for the explanation surface and the override mechanism as adoption prerequisites, not just ethical niceties.

### Claim 6: "Addressing algorithmic transparency and communication about algorithms to users can help create workplaces that workers can trust, find fair, and feel good about"

- **Suggested for:** Ch 2.2 ¶4 (Miller explanation complement); Ch 5.1.2 ¶3 (explanation as interface, transparency as design requirement)
- **Direkte sitat:** "Addressing these concerns both in the actual implementation of algorithms and in communication about algorithms to users can help us create workplaces that are efficient but also that workers can trust, find fair, and feel good about." (p. 14)
- **Parafrase:** Algorithmic transparency — both in system design and in how the system communicates its decisions — is the actionable response to the fairness and trust concerns the study identifies.
- **Forbehold:** Practical recommendation rather than an empirically tested design intervention; "communication about algorithms" is underspecified.
- **Anvendelse på vårt case:** This claim is the bridge from Lee's empirical findings to Miller's explanation-as-interface design prescription. In Ressursplanlegger, "communication about algorithms" takes the concrete form of deviation alerts, scoring breakdowns, and the time-quality tradeoff control (§3.5.7) — these are the mechanisms by which the algorithm communicates its basis for decisions to the coordinator.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| algorithm / algorithmic decision-maker | Ressursplanlegger's solver layer (greedy / CP-SAT / Timefold) | Lee's "algorithm" is an autonomous manager; ours is a decision-support tool. The power relationship differs — see Forbehold. |
| human manager / manager | trafikkoordinator | In our case the coordinator is both the human manager (Lee's framing) AND the operator of the algorithm — a dual role Lee's study does not address. |
| worker / employee | sjåfør (driver) | Drivers are the workers subject to algorithm-generated assignments; they are in Lee's "subject" position. |
| managerial decision | planleggingsbeslutning / tildeling | Lee's scenarios: work assignment, scheduling, hiring, evaluation. Our relevant scenario: work assignment and scheduling (mechanical-skill category). |
| mechanical skills (task type) | planlegging / ressurs-tildeling (etter eksplisitte regler) | Assignment and scheduling based on explicit constraints — qualifies as mechanical. |
| human skills (task type) | taktisk koordinatorkunnskap | Exceptions, preferences, tacit criteria — qualifies as human. |
| trust (in reliability and accuracy) | Tillit/kontroll (første dimensjon: tillit) | Lee's trust construct is about reliability/accuracy; Hoff & Bashir (2015) adds three-dimensional antecedent model. |
| fairness (perceived) | rettferdighet i tildelingsalgoritmen | Relevant for ethics discussion (§5.3), not for HITL design section. |
| agency / being watched | sjåføragentur / overvåkingsfrykt | Driver concern; relevant for §5.3 working-conditions dilemma. |

## Forbehold og begrensninger

1. **Different power position than our operator.** Lee studies workers who are *subject to* algorithmic managerial decisions. Ressursplanlegger's coordinator is an *operator* of the algorithm — using it as decision-support, with full authority to override. This is a fundamentally different power relationship. Lee's findings about trust and fairness apply most directly to *drivers* in our system, not to coordinators. The HITL design rationale requires a separate theoretical basis (Bainbridge, Parasuraman, Hoff & Bashir) — Lee is the foundational layer for why trust matters, not the authority for how HITL should be designed.

2. **Scenario-based US MTurk experiment.** Hypothetical scenarios with US workers; not Norwegian; not transport coordinators; not interactive with an actual planning tool. The findings are directionally informative but cannot be cited as direct evidence about coordinator behaviour in a Norwegian TMS context.

3. **Mechanical vs human skill categorisation — assignment task is relevant.** Lee's "work assignment" scenario (algorithmic assignment of maintenance tasks to factory floor workers) is the scenario type closest to Ressursplanlegger. That scenario showed equal trust between algorithmic and human decisions — BUT the open-response quotes reveal that even for mechanical tasks, participants noted the algorithm cannot "consider nuanced information about each individual worker's context" (P141). This nuance (equal aggregate trust, but qualitatively different trust basis) is important to reproduce accurately; citing only "equal trust for mechanical tasks" misrepresents the finding.

4. **No treatment of operator experience or learning over time.** Lee measures one-shot perceptions of algorithmic decisions without controlling for experience with the system. For Ressursplanlegger, trust is expected to develop over use (calibrated trust per Hoff & Bashir) — Lee cannot speak to that dynamic.

5. **Does not address explanation or transparency as a design intervention.** Lee recommends "communication about algorithms" as a general principle (p. 14) but does not test any specific design. Miller (2019) is the source for the design implementation of that principle.

6. **`outline.md` §5.3 ¶3 MUST CITE marker:** The marker names "Lee MK — algorithmic management and worker fairness (working-conditions dilemma)". This source confirms that fit: the dehumanisation, surveillance, and exception-handling findings (Claims 3, 4) directly support the worker-fairness and working-conditions dilemma in §5.3.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Trust (in automation context) | "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" | p. 4 |
| Perceived fairness | "treating everyone equally or equitably based on people's performance or needs" | p. 4 |
| Algorithm (operational definition used in study) | "a computational formula that autonomously makes decisions based on statistical models or decision rules without explicit human intervention" | p. 3 |

## Rammeverk og modeller

### Task-type contingency model (implicit framework, pp. 4–11)

The central analytical framework distinguishes two categories of managerial decision tasks and predicts differential trust and fairness perceptions:

| Task type | Characteristic | Algorithm trust vs human trust | Source of algorithm authority (when trusted) |
|---|---|---|---|
| Mechanical skills | Explicit, quantifiable criteria; rule-following; no subjective judgment needed | Equal | Reliability and lack of bias |
| Human skills | Tacit, contextual judgment; social nuance; exceptions; non-quantifiable factors | Lower | — (algorithm seen as incapable) |

The model is operationalised through four scenarios tested (Table 1, p. 6):
- Work assignment (mechanical) — algorithm assigns maintenance tasks based on failure data
- Work scheduling (mechanical) — algorithm schedules shift workers based on predicted customer numbers
- Hiring (human) — algorithm selects job candidates
- Work evaluation (human) — algorithm evaluates customer service call performance

**Relevance for Ressursplanlegger:** Driver-and-vehicle assignment involves both types — the explicit constraint layer (competencies, availability, no double-booking) is mechanical; the exception and preference layer (tacit coordinator knowledge) is human. The system's hybrid nature means coordinator trust will be contingent on how visible the constraint reasoning is.

## Key arguments / lines of reasoning

### Argument: Perception drives adoption independently of performance

- **Premiss 1:** Algorithmic decisions may be optimal yet still perceived as unfair or untrustworthy.
- **Premiss 2:** Perceptions of fairness and trust influence workers' willingness to cooperate with organisational decisions (via Leventhal 1980; Lee & See 2004).
- **Konklusjon:** Adoption of algorithmic management systems is as much a perception-management problem as a performance-optimisation problem.
- **Sted:** (p. 2, introduction; p. 1, abstract)
- **Hvilke claims dette støtter:** Claim 5; Ch 2.2 ¶5; Ch 5.2 ¶1

### Argument: Human authority and algorithmic authority rest on different foundations

- **Premiss 1:** Even when trust and fairness ratings are equal, people's reasons differ by decision-maker type.
- **Premiss 2:** Human authority is attributed to positional legitimacy and accountability; algorithmic authority to efficiency and objectivity.
- **Konklusjon:** Algorithmic authority is fragile in ways human managerial authority is not — a single visible error destroys perceived objectivity; a single contextual failure undermines perceived efficiency. Human managers can absorb errors via positional legitimacy.
- **Sted:** (p. 13, Discussion; p. 11, Discussion opener)
- **Hvilke claims dette støtter:** Claim 2; Ch 5.1.2; Ch 5.3 ¶5

### Argument: Transparency and communication are the design response to perceived unfairness

- **Premiss 1:** Distrust and perceived unfairness arise from algorithms appearing unable to handle exceptions, non-quantifiable factors, and human concerns.
- **Premiss 2:** These concerns can be addressed "in the actual implementation of algorithms and in communication about algorithms to users."
- **Konklusjon:** System design should address exception-visibility and algorithmic reasoning communication as first-order requirements for algorithmic management adoption.
- **Sted:** (p. 14, Implications for practice)
- **Hvilke claims dette støtter:** Claim 6; Ch 2.2 ¶4 (Miller complement); Ch 5.1.2 ¶3

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Work assignment scenario: algorithm assigns Chris to a maintenance task in manufacturing factory based on failure-rate data | Mechanical-skill algorithmic decision — equal fairness and trust as human | pp. 6, 8 |
| Work scheduling scenario: algorithm calls in Riley to work a shift based on predicted customer numbers | Mechanical-skill scheduling with short notice — equal aggregate ratings but qualitative concern about algorithm ignoring personal context | pp. 6, 8–10 |
| Hiring scenario: algorithm screens thousands of resumes on LinkedIn-style platform | Human-skill decision — algorithm perceived as less fair and trustworthy; intuition and non-quantifiable qualities cited | pp. 6, 8–9 |
| Work evaluation scenario: customer service call center algorithm evaluates employee performance by content and tone analysis | Human-skill decision — most negative outcomes; dehumanisation concern most prominent | pp. 6, 9, 11 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 228 participants after exclusions | US Amazon MTurk workers | September 2016 | p. 5 |
| Work assignment: Algorithm fairness 5.90 (SE=.20) vs Human 6.21 (SE=.22) — NS (not significant) | 7-point Likert scale | 2016 experiment | p. 8 (Table 2) |
| Work assignment: Algorithm trust 5.52 (SE=.17) vs Human 5.33 (SE=.18) — NS | 7-point Likert scale | 2016 experiment | p. 8 (Table 2) |
| Hiring: Algorithm fairness 4.2 (SE=.24) vs Human 5.78 (SE=.23) — F(1,59)=21.76, p<.0001 | 7-point Likert scale | 2016 experiment | p. 8 (Table 2) |
| Hiring: Algorithm trust 3.55 (SE=.25) vs Human 5.37 (SE=.24) — F(1,59)=26.96, p<.0001 | 7-point Likert scale | 2016 experiment | p. 8 (Table 2) |
| Work evaluation: Algorithm fairness 3.39 (SE=.20) vs Human 6.11 (SE=.22) — F(1,57)=81.6, p<.0001 | 7-point Likert scale | 2016 experiment | p. 8 (Table 2) |

## Forfatter-perspektiv / metodologi

Online between-subjects scenario experiment using Amazon Mechanical Turk (N=228 after exclusions). Participants read one of four managerial decision scenarios (work assignment, scheduling, hiring, evaluation) manipulated for decision-maker type (human/algorithmic). Both quantitative Likert ratings and qualitative open-response reasons were collected and coded thematically (Strauss & Corbin, 1990). The study is explicitly presented as a first step; the author acknowledges it needs complementing with real-world studies of actual workers affected by algorithmic management.

## Spot-check verification

1. Quote "Trust can be defined as the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability." (p. 4) — verified via `pdftotext -f 4 -l 4 raw/lee2018understanding.pdf` — PASS (quote appears verbatim on extracted page 4, under heading "Trust regarding the reliability of future decisions")

2. Quote "the source of authority in decisions varied depending on the decision-maker: the manager's authority was attributed to their position in the organization, whereas the algorithm's authority was attributed to its efficiency and lack of bias." (p. 13) — verified via `pdftotext -f 13 -l 13 raw/lee2018understanding.pdf` — PASS (text appears on printed p. 13, under "Discussion" section, "Implications for theory")

3. Quote "algorithms' inability to accommodate exceptions, measure human properties commonly believed to be non-quantifiable (such as social interactions and personalities), or consider human concerns such as empathy and personal commitments, all of which contributed to distrust of algorithms and feelings of unfairness." (p. 14) — verified via `pdftotext -f 14 -l 14 raw/lee2018understanding.pdf` — PASS (text appears verbatim on printed p. 14, first paragraph)

4. Quote "Some expressed concern about having an algorithm as a decision-maker in the workplace, as the algorithm might make employees feel that they lacked 'agency' (P121) or were 'being watched' (P113)." (p. 11) — verified via `pdftotext -f 11 -l 11 raw/lee2018understanding.pdf` — PASS (text appears on printed p. 11 under "Algorithmic and human decisions evoke similar emotion for tasks that involve mechanical skills")

**Result:** 4/4 quotes verified, 0 corrections made.