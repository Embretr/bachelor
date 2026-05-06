# Trust in Automation: Designing for Appropriate Reliance (`lee2004trust`)

## Status
- [x] Notes generated from raw (Claude, 2026-05-01)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The full article was read end-to-end (pp. 50–80). All major sections were deep-read: trust definition, appropriateness framework (calibration/resolution/specificity), context factors, analytic/analogical/affective processes, dynamic model of trust and reliance, display effects, and design implications. All thesis areas of interest (Ch 2.2 HITL and Ch 5.1.2 Tillit/kontroll) are fully covered.
  - **Gaps not investigated:** None — article read in full.

## Source metadata
- **BibTeX key:** `lee2004trust`
- **Reference (APA 7):** Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392
- **Tilgang:** PDF (provided in raw/)
- **Raw source:** `../lee2004trust.pdf`
- **Coverage in raw:** Full article, pp. 50–80. PDF is image-based (scanned); pdftotext extracts only the copyright watermark. All quotes verified visually via Read tool against specific PDF pages. PDF page index = printed page − 49 (PDF p. 1 = printed p. 50).
- **Page-mapping note:** PDF page N = printed page N + 49. E.g., printed p. 54 = PDF p. 5. All citations use printed page numbers per source-extractor quality rules.

---

## Sammendrag (2–3 setninger)

Lee and See (2004) present a multidisciplinary review of trust in automation, developing a conceptual model that integrates organisational, sociological, interpersonal, psychological, and neurological perspectives. The central argument is that trust guides reliance on automation — particularly when complexity makes complete understanding impractical — and that the goal for design is *appropriate* reliance, achieved through calibrated, high-resolution, and high-specificity trust rather than simply greater trust. The paper's primary contribution to this thesis is its foundational definition of trust as an attitude, its operationalisation of appropriateness via calibration/resolution/specificity, and its design guidance for making automation trustable — all of which frame how Ressursplanlegger must support the trafikkoordinator's reliance on algorithm-generated plans.

---

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.2 ¶5 — Lee trust foundation (HITL theory layer) | **Covered** — foundational definition, appropriateness framework, dynamic model |
| Ch 5.1.2 ¶2 — Hoff & Bashir refinement layer (Lee as base) | **Covered** — Lee's trust-reliance model is the base that Hoff & Bashir refines; documented here |
| Ch 2.2 ¶6 — HITL as design constraint (expose reasoning) | **Covered** — "Make Automation Trustable" design principles directly support this |
| Ch 5.1.2 ¶3 — Miller complement (explanation as interface) | **Partial** — Lee addresses display characteristics and information provision; Miller handles social-science framing of explanation. Cross-reference only. |
| Ch 2.1 (scheduling theory) | **Outside scope** — article does not address scheduling |
| Ch 2.3 (TMS category) | **Outside scope** — article does not address transport management systems |
| Ch 2.4 (DSR methodology) | **Outside scope** — article does not address research methodology |

---

## Claims this source supports

### Claim 1: Trust is the attitude that an agent will help achieve an individual's goals in a situation characterised by uncertainty and vulnerability

- **Suggested for:** Ch 2.2 ¶5 (Lee trust foundation); Ch 5.1.2 ¶2 (when Lee is introduced as the base that Hoff & Bashir refines)
- **Direkte sitat:** "A simple definition of trust consistent with these considerations is *the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability.*" (p. 54)
- **Parafrase:** Trust is an attitude — not an intention or behaviour — that orients an individual toward relying on an agent when the outcome matters and cannot be guaranteed.
- **Forbehold:** The definition is intentionally broad to cover both human-human and human-automation trust. For automation specifically, the "agent" lacks intentionality (p. 66), which is a key difference the source discusses at length.
- **Anvendelse på vårt case:** For the trafikkoordinator, the agent in this definition is Ressursplanlegger's algorithm — the attitude of trusting the system's assignment suggestions determines whether the coordinator relies on algorithm-generated plans or overrides them entirely, making trust the mediating variable between system capability and actual use.

---

### Claim 2: Appropriate trust requires calibration, resolution, and specificity — not simply more trust

- **Suggested for:** Ch 2.2 ¶5 (Lee trust foundation); Ch 5.1.2 ¶2 (applied to how coordinator trust forms in Ressursplanlegger)
- **Direkte sitat:** "*Calibration* refers to the correspondence between a person's trust in the automation and the automation's capabilities (Lee & Moray, 1994; Muir, 1987). [...] *Overtrust* is poor calibration in which trust exceeds system capabilities; with *distrust*, trust falls short of the automation's capabilities." (p. 55)
- **Parafrase:** The goal of design is not to maximise trust but to ensure that the level of trust matches actual automation capability at each level of detail and at each moment in time. Good calibration, high resolution, and high specificity together constitute appropriate trust.
- **Forbehold:** Calibration, resolution, and specificity are normative ideals — the source does not provide a simple metric for measuring them in operational contexts. Achieving all three simultaneously is difficult.
- **Anvendelse på vårt case:** Ressursplanlegger's algorithm generates different quality outputs depending on instance size and solver selection (greedy vs. CP-SAT vs. Timefold). Appropriate trust requires that the coordinator's reliance reflects these actual capability differences — not blanket trust or blanket distrust. The time-quality tradeoff control (§3.5.7) is one mechanism for supporting calibration by making algorithm capability explicit at plan-generation time.

---

### Claim 3: Trust influences reliance but does not determine it — other factors (workload, self-confidence, time pressure) mediate between trust and reliance action

- **Suggested for:** Ch 5.1.2 ¶2 (when discussing why trust does not mechanically produce reliance); Ch 2.2 ¶5
- **Direkte sitat:** "Trust combines with other attitudes and expectations, such as subjective workload, effort to engage, perceived risk, and self-confidence to form the intention to rely on the automation." (p. 67)
- **Parafrase:** Trust is one input to reliance, not its sole cause. The dynamic model (Figure 4) shows trust feeding into intention formation, which is further modified by workload and time pressure before translating into reliance action.
- **Forbehold:** The source draws primarily on aviation, process control, and navigation domains. Whether the same mediating variables operate for traffic coordinators doing planning work (as opposed to real-time supervisory control) requires care in application.
- **Anvendelse på vårt case:** A trafikkoordinator may trust Ressursplanlegger's algorithm but fail to rely on it under time pressure (sick-leave replanning scenario) or when workload from other tasks is high. This means Effektivitet gains from the algorithm depend not only on building calibrated trust but also on reducing the effort required to engage the system — a design implication for the HITL surface.

---

### Claim 4: Trustworthy automation must reveal its performance, process, and purpose — not just perform well

- **Suggested for:** Ch 2.2 ¶6 (HITL as design constraint — expose reasoning); Ch 5.1.2 ¶3 (complement to Miller on explanation)
- **Direkte sitat (design principles list, p. 74):**
  - "Design for appropriate trust, not greater trust."
  - "Show the past performance of the automation."
  - "Show the process and algorithms of the automation by revealing intermediate results in a way that is comprehensible to the operators."
  - "Show the purpose of the automation, design basis, and range of applications in a way that relates to the users' goals."
  - "Train operators regarding its expected reliability, the mechanisms governing its behavior, and its intended use."
- **Parafrase:** Making automation trustable requires communicating the basis of trust across all three dimensions — performance (what it does), process (how it decides), and purpose (why it was designed this way) — because operators cannot build appropriate trust without information at all three levels.
- **Forbehold:** These principles are design aspirations developed from laboratory and field research across diverse domains. The source does not provide validated metrics for whether a specific interface achieves them. Applying them to Ressursplanlegger requires domain translation.
- **Anvendelse på vårt case:** Ressursplanlegger's deviation alerts expose performance failures; the scoring breakdown exposes process (how the algorithm weighted constraints); the time-quality control communicates capability limits to the coordinator. Together, these directly operationalise Lee & See's three-dimension information framework — performance, process, and purpose — as concrete HITL interface features.

---

### Claim 5: Misuse (over-reliance) and disuse (under-reliance) are both failures of trust calibration, and both undermine the value of automation

- **Suggested for:** Ch 2.2 ¶5 (framing the misuse/disuse risk in the HITL theory section); Ch 5.1.2 ¶2
- **Direkte sitat:** "*Misuse* refers to the failures that occur when people inadvertently violate critical assumptions and rely on automation inappropriately, whereas *disuse* signifies failures that occur when people reject the capabilities of automation." (p. 50)
- **Parafrase:** Poorly calibrated trust produces one of two failure modes: the operator trusts too much (misuse — over-reliance) or too little (disuse — under-reliance). Either failure eliminates the value of the automation.
- **Forbehold:** The misuse/disuse framing was developed primarily for safety-critical, real-time supervisory contexts (aviation, process control). In planning contexts, the consequences of misuse are less immediately catastrophic but still real (incorrect assignment plans that go undetected).
- **Anvendelse på vårt case:** For Ressursplanlegger, misuse means the coordinator accepts algorithm-generated plans without reviewing deviations — a risk especially when cognitive workload is high. Disuse means coordinators revert to fully manual planning and the system's Effektivitet gains are never realised. The HITL design must guard against both: the deviation scanner guards against misuse; transparent algorithm reasoning guards against disuse by making the system's logic legible.

---

### Claim 6: Trust in automation develops dynamically — it is conditioned by the worst behaviours of a system, and initial levels of trust have lasting effects

- **Suggested for:** Ch 5.1.2 ¶2 (dynamic trust formation relevant to coordinator adoption)
- **Direkte sitat:** "Trust is a nonlinear function of automation performance and the dynamic interaction between the operator and the automation. It tends to be conditioned by the worst behaviors of an automated system (Muir & Moray, 1996)." (p. 72)
- **Parafrase:** A single conspicuous failure can disproportionately reduce trust, and low initial trust from early failures can persist even when the system later performs well (nonlinear, hysteresis-like dynamics).
- **Forbehold:** The source notes that trust recovery after faults occurs over time (not instantaneously) and that chronic failures lead to permanent distrust. The dynamics described are based primarily on lab and process-control studies.
- **Anvendelse på vårt case:** For Ressursplanlegger's deployment, this means early coordinator interactions with the algorithm are disproportionately important. A conspicuous greedy-heuristic failure (e.g., assigning a driver without a required competence) could condition lasting distrust even after switching to the CP-SAT solver. This justifies surfacing the solver selection control early in onboarding and providing training on the algorithm's expected reliability boundaries.

---

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Operator | Trafikkoordinator | Lee uses "operator" for the human who monitors and intervenes in automated systems; in our case this is the traffic coordinator who plans assignments |
| Automation / automated system | Ressursplanlegger's algorithm (solver layer) | The automation in our case is the multi-engine solver that generates assignment plans |
| Trustee | Ressursplanlegger (the algorithm as the trusted agent) | |
| Trustor | Trafikkoordinator | The human whose goal-achievement depends on trusting the system |
| Reliance action | Accept / use the algorithm-generated plan | In our HITL framing: the coordinator's act of accepting (rather than modifying or rejecting) an assignment suggestion |
| Misuse | Over-reliance — accepting plans without reviewing deviations | |
| Disuse | Under-reliance — reverting to fully manual planning, ignoring algorithm suggestions | |
| Calibration | Correspondence between coordinator's trust level and actual algorithm capability per solver and instance size | |
| Resolution | Degree to which the coordinator's trust differentiates between algorithm capability levels (greedy vs CP-SAT) | |
| Functional specificity | Trust focused on a specific solver engine / constraint type, not the whole system | |
| Temporal specificity | Trust adjustment speed as coordinator accumulates experience with the system | |
| Performance (basis of trust) | Algorithm's demonstrated assignment quality and deviation-detection accuracy | |
| Process (basis of trust) | Algorithm's constraint logic and scoring breakdown — how it decides | |
| Purpose (basis of trust) | Why Ressursplanlegger was designed — to improve resource utilization while preserving coordinator authority | |
| Display characteristics | Ressursplanlegger's planning UI — deviation alerts, scoring breakdown, time-quality control surface | |

---

## Forbehold og begrensninger

- **Domain gap — real-time vs. planning contexts:** Lee & See's research base is predominantly real-time supervisory control (aviation, process control, vehicle navigation). Ressursplanlegger is used for *planning* — the coordinator has more time to deliberate, errors are not immediately safety-critical, and the interaction is less continuous. The dynamic trust model still applies, but the timescale and urgency of trust-mediated reliance decisions differ. Claims about temporal dynamics of trust should be qualified accordingly.
- **Intentionality difference — automation lacks it:** The source extensively discusses (pp. 66–67) how automation lacks intentionality, which is the most fundamental difference between human-human and human-automation trust. The source does not resolve this gap but flags it as a limitation of extending the trust concept to automation. For our thesis, this means Lee & See's definition functions as a foundational framework that Hoff & Bashir (2015) supplements with more automation-specific antecedents.
- **No empirical data on planning/scheduling domains:** Lee & See do not study trust in resource planning or scheduling systems. All empirical evidence cited is from aviation, maritime, process control, and vehicle navigation. Application to Ressursplanlegger is by theoretical extension, not domain match.
- **Self-confidence as confound:** The source identifies self-confidence as a critical mediating variable between trust and reliance (pp. 70–71). Coordinators with high self-confidence in their own manual planning ability may disuse the algorithm even when they trust it. This variable is not addressed in the thesis's interview data and represents a limitation (adjacent to L8 — no user testing with coordinators).
- **No specific treatment of multi-tenant or cross-company trust:** The source does not address how trust forms when the same automation is used across organisations with different operational rules — directly relevant to the Tilpasningsdyktighet anchor. The Tilpasningsdyktighet discussion must draw on other sources for cross-company trust formation.
- **outline.md MUST CITE marker — confirmed fit:** The outline marks `MUST CITE: Lee — trust in automation (foundational)` at Ch 2.2 ¶5 and Ch 5.1.2 ¶2. Both fits are confirmed. The source supports the foundational definition and the calibration framework directly.

---

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Trust (operational definition) | "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" | p. 54 |
| Calibration | "the correspondence between a person's trust in the automation and the automation's capabilities" | p. 55 |
| Overtrust | "poor calibration in which trust exceeds system capabilities" | p. 55 |
| Distrust | trust "falls short of the automation's capabilities" | p. 55 |
| Resolution | "how precisely a judgment of trust differentiates levels of automation capability" | p. 55–56 |
| Specificity (functional) | "the degree to which trust is associated with a particular component or aspect of the trustee" | p. 56 |
| Misuse | "the failures that occur when people inadvertently violate critical assumptions and rely on automation inappropriately" | p. 50 |
| Disuse | "failures that occur when people reject the capabilities of automation" | p. 50 |
| Automation (for trust purposes) | "technology that actively selects data, transforms information, makes decisions, or controls processes" | p. 50 |

---

## Rammeverk og modeller

### Three-dimensional appropriateness framework (pp. 55–56)

The source defines appropriate trust along three dimensions. All three must be simultaneously high for appropriate reliance:

| Dimension | What it is | Design implication | Page |
|---|---|---|---|
| **Calibration** | Match between trust level and actual automation capability | Show past performance data; communicate capability limits | p. 55 |
| **Resolution** | How finely trust differentiates capability levels | Support trust at multiple levels (per solver, per constraint type) | p. 55–56 |
| **Functional specificity** | Trust targeted at specific components, not the whole system | Allow coordinators to trust the deviation scanner separately from the solver | p. 56 |
| **Temporal specificity** | Trust reflects moment-to-moment capability changes, not only long-term averages | Update coordinator expectations when context changes (sick-leave vs. routine planning) | p. 56 |

### Three-dimensional basis of trust (pp. 58–60, Table 1)

The basis of trust — what information supports trust formation — is organised along three dimensions (synthesised from Table 1 and surrounding text):

| Basis | What it covers | Automation equivalent | Page |
|---|---|---|---|
| **Performance** | What the automation does; reliability, predictability, ability | Assignment quality, violation rates, benchmark results | p. 59 |
| **Process** | How the automation decides; algorithms, operating principles | Constraint logic, scoring breakdown, solver selection | p. 59 |
| **Purpose** | Why the automation was designed; designer intent, intended use | Reducing overtime / idle time / load imbalance while preserving coordinator authority | p. 59 |

### Dynamic model of trust and reliance (Figure 4, p. 68)

A closed-loop conceptual model with five nodes:

| Node | Role | Page |
|---|---|---|
| Information assimilation and Belief formation | Inputs from display about automation performance/process/purpose | p. 67–68 |
| Trust evolution | Dynamic update of trust attitude based on beliefs | p. 67–68 |
| Intention formation | Trust + workload + self-confidence + perceived risk → intention to rely | p. 67 |
| Reliance action | Actual decision to use or override the automation | p. 67–68 |
| Display ↔ Automation feedback loop | Reliance enables observation of automation behavior, which updates beliefs | p. 68 |

Key property: the model is explicitly closed-loop — reliance generates experience that updates trust, not a one-way causal chain.

### "Make Automation Trustable" — design principles (p. 74)

Verbatim bullet list from the source:

1. "Design for appropriate trust, not greater trust."
2. "Show the past performance of the automation."
3. "Show the process and algorithms of the automation by revealing intermediate results in a way that is comprehensible to the operators."
4. "Simplify the algorithms and operation of the automation to make it more understandable."
5. "Show the purpose of the automation, design basis, and range of applications in a way that relates to the users' goals."
6. "Train operators regarding its expected reliability, the mechanisms governing its behavior, and its intended use."
7. "Carefully evaluate any anthropomorphizing of the automation, such as using speech to create a synthetic conversational partner, to ensure appropriate trust."

---

## Key arguments / lines of reasoning

### Argument: Trust is needed precisely because complexity makes complete understanding impossible

- **Premiss 1:** As automation becomes more complex, complete understanding of its behaviour becomes impractical.
- **Premiss 2:** Trust functions as a social decision heuristic that supplants supervision when direct observation is impractical.
- **Konklusjon:** Trust is not a substitute for understanding, but it is a necessary mechanism for managing reliance when full understanding is unachievable.
- **Sted:** pp. 51–52
- **Hvilke claims dette støtter:** Ch 2.2 ¶5; Ch 5.1.2 ¶2

### Argument: Appropriate trust, not greater trust, is the design goal

- **Premiss 1:** Misuse (over-reliance from overtrust) and disuse (under-reliance from distrust/low trust) are both costly failures.
- **Premiss 2:** The design goal is therefore not to maximise trust but to calibrate it to actual system capability.
- **Premiss 3:** Calibration, resolution, and specificity are the measurable dimensions of appropriate trust.
- **Konklusjon:** Design should aim at making automation trustable (by communicating its true capabilities) rather than merely making it appear trustworthy.
- **Sted:** pp. 55–56, 74
- **Hvilke claims dette støtter:** Claim 2; Ch 2.2 ¶6; Ch 5.1.2 ¶2

### Argument: Trust develops dynamically and is conditioned by worst-case behaviour

- **Premiss:** Trust in automation evolves in a closed-loop process; negative interactions have a greater influence than positive ones (negativity bias consistent with Kramer, 1999).
- **Konklusjon:** Initial deployment experience and first failures are disproportionately important for long-term trust calibration.
- **Sted:** pp. 67–70, 72
- **Hvilke claims dette støtter:** Claim 6; Ch 5.1.2 ¶2

---

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Airbus A320 autopilot crash (Sparaco, 1995) | Misuse — pilots trusted autopilot even as it crashed the plane | p. 50 |
| Royal Majesty cruise ship grounding (NTSB, 1997) | Disuse of available navigation information combined with misplaced trust | p. 50 |
| Pasteurisation plant operators (Lewandowsky et al., 2000) | Trust in human collaborators vs. automation shows asymmetry in delegation behaviour | pp. 65–66 |
| Situation-specific reliability training for air traffic controllers (Masalonis, 2000) | Training enhanced appropriateness of trust in decision aids | p. 72 |
| Aircraft predictor reliability disclosure to pilots (Wickens et al., 2000) | Knowing a predictor was not completely reliable helped pilots calibrate trust and allocate attention appropriately | p. 72 |

---

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| Time-series analysis accounts for 60–86% of variance in operators' reliance patterns | % variance explained | Study by Lee & Moray, 1994 | p. 70 |
| Trust drop-off threshold: below ~70–90% reliability, trust declines rapidly | % reliability threshold (context-dependent) | Kantowitz et al., 1997a; Moray et al., 2000; Fox, 1996 | p. 72 |

---

## Forfatter-perspektiv / metodologi

This is a theoretical review paper, not an empirical study. Lee and See synthesise research from organisational science, social psychology, neuropsychology, and human factors to build a multidisciplinary conceptual model. The paper's claims are supported by citation to primary studies rather than original data collection. This means all quantitative findings cited (e.g., reliability thresholds) are from third-party studies and should be attributed to those studies, not to Lee & See, if used as empirical evidence.

---

## Spot-check verification

1. Quote "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (p. 54) — verified via Read tool on PDF p. 5 (= printed p. 54) — **PASS**

2. Quote "*Calibration* refers to the correspondence between a person's trust in the automation and the automation's capabilities" (p. 55) — verified via Read tool on PDF p. 6 (= printed p. 55) — **PASS**

3. Quote "Design for appropriate trust, not greater trust." and surrounding bullet list (p. 74) — verified via Read tool on PDF p. 25 (= printed p. 74) — **PASS**

**Note on pdftotext:** `pdftotext` was run on this PDF and returned only the copyright watermark on every page. The PDF is image-based (scanned). All spot-check verification was therefore performed using the Read tool to fetch specific PDF pages and visually confirming quote presence. Page mapping confirmed: PDF page index = printed page − 49 (PDF p. 1 = printed p. 50, PDF p. 5 = printed p. 54, etc.).

**Result:** 3/3 quotes verified, 0 corrections made.