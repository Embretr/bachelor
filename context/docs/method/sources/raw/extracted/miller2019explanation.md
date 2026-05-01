# Explanation in Artificial Intelligence: Insights from the Social Sciences (`miller2019explanation`)

## Status
- [x] Notes generated from raw (Claude, 2026-04-28)
- [x] Spot-check verified (independent Opus pass, 2026-04-28): 5/5 quotes confirmed verbatim against PDF; interpretability definition page corrected from p. 1 to p. 8.
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** All areas of interest investigated. Sections 1–2 (philosophical foundations), 2.3 (contrastive explanation), 2.6 (XAI implications), 4.6.6 (trust and explanation evaluation), 5.1 (conversational model), 5.3 (social explanation and XAI), and Section 6 (conclusions) are fully read and extracted. Sections 3 (social attribution) and 4 (cognitive processes, detailed attribution models) are outside the thesis areas of interest — they concern how people attribute behaviour in general, not how AI systems should explain decisions. These were skimmed and found not to contribute to the relevant thesis sections.
  - **Gaps not investigated:** Section 3 (social attribution detail), Section 4 (cognitive models in detail, beyond the four findings already captured from the introduction). These sections are relevant to deep XAI implementation but not to how the thesis uses this source.

## Source metadata
- **BibTeX key:** `miller2019explanation`
- **Reference (APA 7):** Miller, T. (2019). Explanation in artificial intelligence: Insights from the social sciences. *Artificial Intelligence*, *267*, 1–38. https://doi.org/10.1016/j.artint.2018.07.007
- **Tilgang:** PDF (raw file present)
- **Raw source:** `../miller2019explanation.pdf`
- **Coverage in raw:** Full paper, pp. 1–38. PDF page numbers equal printed page numbers (no front matter offset).

## Sammendrag (2–3 setninger)

Miller argues that most explainable AI research relies on researchers' own intuitions about what constitutes a "good" explanation, ignoring a large body of work in philosophy, cognitive psychology, and social science. He identifies four key properties of human explanation — contrastiveness, selectivity, social embeddedness, and causal (rather than probabilistic) framing — and argues that XAI must adopt these insights to generate explanations that people actually find useful and that build trust. For the thesis, the source provides the theoretical grounding for why Ressursplanlegger's UI must expose its reasoning contrastively (e.g., "why was driver A assigned rather than driver B?"), and why generating trust through explanation is a first-class design criterion.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| Ch 2.2 ¶4 (trust in algorithm output) | covered — trust is lost without understandable explanations |
| Ch 2.2 ¶5 (HITL — system must expose reasoning) | covered — explanation as first-class design criterion for trust |
| Ch 5.3 ¶2 (adoption barriers — trust in algorithm output) | covered — sceptical users will distrust both decisions and explanations |
| Ch 5.5 ¶5 (ethical considerations — accountability, transparency) | partial — transparency as ethical requirement mentioned; not the paper's main focus |

---

## Claims this source supports

### Claim 1: "Trust is lost when users cannot understand traces of observed behaviour or decisions"

- **Suggested for:** Ch 2.2 ¶4 (trust); Ch 5.3 ¶2 (adoption barriers)
- **Direkte sitat:** "trust is lost when users cannot understand traces of observed behaviour or decisions" (p. 3)
- **Parafrase:** AI applications suffer limited uptake precisely because users cannot understand why a system made a particular decision; building transparent and explainable systems is the running hypothesis for restoring trust.
- **Forbehold:** The paper makes this claim in the context of AI applications broadly (machine learning classifiers, autonomous agents) — it is not specific to transport planning. The claim is widely accepted in XAI literature and is treated as background motivation.
- **Anvendelse på vårt case:** For trafikkoordinatorer som vurderer om de skal bruke Ressursplanlegger, er det avgjørende at plansystemet kan vise *hvorfor* en bestemt sjåfør ble tildelt et oppdrag — ikke bare hva resultatet ble. Uten dette vil koordinatorer som allerede er sceptiske til automatisering (jf. Ch 4.1 intervjufunn) ikke ha noe grunnlag for å kalibrere tillit til algoritmens output.

---

### Claim 2: Explanations are contrastive — users ask "Why P rather than Q?", not "Why P?"

- **Suggested for:** Ch 2.2 ¶5 (HITL — system must expose reasoning); Ch 5.3 ¶2 (adoption barriers — understanding override decisions)
- **Direkte sitat:** "an explanation is always of the form 'Why P rather than Q?', in which P is the target event and Q is a counterfactual contrast case that did not occur, even if the Q is implicit in the question. This is called contrastive explanation." (p. 9)
- **Parafrase:** People do not ask for explanations of events per se; they ask why this outcome occurred instead of some expected alternative. Answering "Why P?" by citing all causes of P is cognitively overwhelming; answering "Why P rather than Q?" by citing only the differences between P and Q is far simpler and more useful.
- **Forbehold:** Miller reviews social science literature, not a study of transport planners or scheduling systems. The claim is a general cognitive science finding with strong empirical backing from multiple fields, but application to planning interfaces requires design work beyond what this paper covers.
- **Anvendelse på vårt case:** I Ressursplanlegger er det naturlige spørsmålet fra en trafikkoordinator ikke "hvorfor ble sjåfør A tildelt?", men "hvorfor ble sjåfør A tildelt *i stedet for* sjåfør B?" (som koordinatoren ville valgt manuelt). Et forklaringsgrensesnitt som bare viser tildeling, uten å tilby en kontrastiv begrunnelse (f.eks. "A ble valgt fordi han er nærmere og har riktig kompetanse, mens B mangler kjøreseddel for dette kjøretøyet"), vil ikke møte det kognitive behovet koordinatoren har.

---

### Claim 3: If the goal is to generate trust, simplicity, generality, and coherence of explanations must be treated as first-class criteria — "beside or even above likelihood"

- **Suggested for:** Ch 2.2 ¶5 (HITL — system must expose reasoning); Ch 5.3 ¶2 (adoption barriers — trust)
- **Direkte sitat:** "if the goal of an explanatory agent is to generate trust between itself and its human observers, these criteria should be considered as first-class criteria in explanation generation beside or even above likelihood. For example, providing simpler explanations that increase the likelihood that the observer both understands and accepts the explanation may increase trust better than giving more likely explanations." (p. 28)
- **Parafrase:** When generating explanations for humans, the statistical likelihood of a cause matters less than whether the explanation is simple, general, and coherent. A technically less probable explanation that is understandable builds more trust than the objectively most-likely causal chain.
- **Forbehold:** Miller's recommendation is prescriptive (how XAI systems *should* work), not an empirical result from a specific system. It is grounded in reviewed empirical literature but not tested in a planning-specific context.
- **Anvendelse på vårt case:** Ressursplanleggers conflict-detection UI bør vise forenklede forklaringer (f.eks. "Sjåfør A har ikke gyldig kjøreseddel for dette kjøretøyet") fremfor en komplett scoring-breakdown med vekter og numeriske verdier. Koordinatoren trenger å forstå og godkjenne forklaringen — ikke re-derivere algoritmen. Dette rettferdiggjør et bevisst valg om å skjule den fulle scoringsmekanismen og bare vise de avgjørende konfliktene.

---

### Claim 4: Explanations are social — they are a conversation between explainer and explainee, not a one-way causal attribution

- **Suggested for:** Ch 2.2 ¶5 (system design — expose reasoning interactively); Ch 5.3 ¶2 (adoption barriers)
- **Direkte sitat:** "Explanations are social — they are a transfer of knowledge, presented as part of a conversation or interaction, and are thus presented relative to the explainer's beliefs about the explainee's beliefs." (p. 3)
- **Parafrase:** Explanation is not just the output of a causal attribution algorithm — it is a communicative act that must be tailored to what the explainee already knows and what question they are actually asking. Good AI explanations should be interactive and context-aware.
- **Forbehold:** The full conversational model (Section 5) implies interactive dialogue between system and user, which is beyond what Ressursplanlegger's current UI supports. The weaker version — that explanation output must be contextually relevant and not merely a raw causal chain — applies directly.
- **Anvendelse på vårt case:** Ressursplanleggers forklaringer av konflikter og tildeling bør presenteres kontekstuelt: kun de konfliktene og begrunnelsene som er relevante for den koordinatoren og den konkrete planen, ikke et generisk dump av alle algoritmens outputs. Dette gjelder særlig ved overstyring — systemet bør kommunisere konsekvensene av en manuell endring i termer koordinatoren kjenner (sjåfør, oppdrag, tid), ikke i interne constraint-termer.

---

### Claim 5: Sceptical users will also distrust explanations provided by a system — "explainees will be aware of this goal [trust-building] … trust levels are low"

- **Suggested for:** Ch 5.3 ¶2 (adoption barriers); Ch 2.2 ¶4 (trust and adoption)
- **Direkte sitat:** "it is clear that we should quite often assume from the outset that trust levels are low. If explainees are sceptical of the decisions made by a system, it is not difficult to imagine that they will also be sceptical of explanations provided, and could interpret explanations as biased." (p. 34)
- **Parafrase:** Users who distrust an AI system's decisions are not automatically won over by explanations — they will also distrust the explanations, treating them as self-serving justifications rather than genuine transparency. Explanation alone does not solve adoption.
- **Forbehold:** This is a theoretical implication from the implicature literature (Dodd and Bradshaw), not a controlled study of planning systems.
- **Anvendelse på vårt case:** Koordinatorer som allerede er skeptiske til automatisering (jf. intervjufunn i Ch 4.1, særlig Ottem-scepticismen) vil muligens avvise algoritmens begrunnelser som "alt for enkel" eller "feil prioritering". Dette er et argument for at Ressursplanlegger ikke bare trenger god forklaring, men at koordinatoren må ha reell og synlig mulighet til å overstyre — slik at forklaringen oppleves som et informasjonstilbud, ikke en forsvarsstrategi.

---

### Claim 6: Explaining a planning system requires addressing "why P rather than not-P" at the final/goal level — why this action was chosen over alternatives given the optimisation criteria

- **Suggested for:** Ch 2.2 ¶5 (system must expose reasoning); Ch 4.5 ¶4 (objective function explanation)
- **Direkte sitat:** "questions related to the model are relevant, or why particular actions were taken rather than others, which may depend on the particular optimisation criteria used (e.g. cost vs. time), and these require efficient/mechanistic explanations." (p. 12)
- **Parafrase:** For AI planning systems, the most relevant why-questions concern why one action (plan) was chosen over another given specific optimisation goals — not the low-level hardware computation or the abstract formal model. Users of planning systems will naturally ask mechanistic and final-cause questions.
- **Forbehold:** Miller uses a robotic search-and-rescue planner as the example domain. Ressursplanlegger's domain (driver/vehicle assignment with soft constraint scoring) maps well to the mechanistic/final-cause level, but the exact question types will differ.
- **Anvendelse på vårt case:** Koordinatoren vil typisk spørre: "Hvorfor ble sjåfør A prioritert foran sjåfør B for dette oppdraget?" — et spørsmål på *final/mechanistic* nivå (hva er tildeligningslogikken, hva er vektene?). Ressursplanlegger bør ikke eksponere grunnleggende schedulingteori, men den konkrete scoring-begrunnelsen: f.eks. "A ble valgt fordi han hadde lavest samlet reisetid og riktig kompetanse; B ble ikke valgt fordi han allerede har fullt timeantall i dag."

---

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| Explainer | Ressursplanlegger (algoritmen + UI) | Systemet som genererer forklaringen |
| Explainee | Trafikkoordinator | Brukeren som mottar og evaluerer forklaringen |
| Decision / action | Tildeling (sjåfør + kjøretøy → oppdrag) | Kilden bruker "decision" generisk; vårt case er en spesifikk tildelingshandling |
| Foil (Q) | Alternativ sjåfør/kjøretøy koordinatoren forventer | Den implisitte kontrasten bak koordinatorens spørsmål |
| Causal attribution | Scoringsmekanisme / constraint-evaluering | Teknisk grunnlag for tildeling, men ikke i seg selv en forklaring |
| Trust | Tillitt til algoritmen / adopsjon av Ressursplanlegger | Operasjonalisert gjennom faktisk bruk og vilje til å følge forslag |
| Conversational model | Kontekstuell feedback i UI | Full dialog ikke implementert; relevant i svakere form som kontekstsensitiv visning |
| Explanatory agent | Ressursplanlegger | Systemet i rollen som forklarer |

---

## Forbehold og begrensninger

- **Domene:** Kilden er en teoristudie av forklaring i AI generelt, basert på sosialvitenskapelig litteratur. Den presenterer ingen empiriske resultater fra planleggingssystemer eller transport. All anvendelse på Ressursplanlegger er bridges utviklet under ekstraksjon.
- **Conversational model:** Kildens sterkeste anbefalinger handler om interaktiv, dialogbasert forklaring (seksjon 5). Ressursplanlegger er ikke et dialogsystem. Den svakere versjonen av kravet — at forklaringer må være kontekstuelt relevante og tailored til brukeren — gjelder direkte, men den fullstendige conversational XAI-implementasjonen gjør ikke det.
- **Scope mismatch for ethics (Ch 5.5):** Kilden nevner kort at etiske/sosiale konsekvenser er viktige for transparens og forklaring (s. 13), men dette er ikke en analyse av algoritmisk rettferdighet eller bærekraft slik Ch 5.5 krever. Kilden støtter ikke direkte SDG-mapping eller SusAF-rammeverket. Bruk kun for den generelle transparens-poenget.
- **No direct MUST CITE markers for this bibkey in outline.md** — extraction is based on relevance assessment from thesis areas, not a pre-set claim list. Suggested fits are derived from content match only.
- **Sections 3 and 4 (Social attribution and Cognitive processes):** These contain detailed models of how humans attribute behaviour and select explanations. They are relevant to deep XAI system design, but beyond the thesis's scope. Not extracted.

---

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Explanation (everyday) | "to explain decisions made by itself or another agent to a person … 'Everyday' explanations are the explanations of why particular facts (events, properties, decisions, etc.) occurred" | p. 3 |
| Contrastive explanation | "an explanation is always of the form 'Why P rather than Q?', in which P is the target event and Q is a counterfactual contrast case that did not occur" | p. 9 |
| Foil | "the foil being the event that did not [occur]" — i.e. the implicit counterfactual contrast case in a why-question | p. 9 |
| Interpretability | "the degree to which an observer can understand the cause of a decision" | p. 8 |
| Justification | "A justification explains why a decision is good, but does not necessarily aim to give an explanation of the actual decision-making process" | p. 8 |

---

## Rammeverk og modeller

### Four major findings on human explanation (p. 3)

These are Miller's headline synthesis from over 250 reviewed social science publications. They apply directly to how an AI planning system should structure explanations.

| Finding | Hva det er | Implikasjon for XAI | Side |
|---|---|---|---|
| 1. Contrastive | Explanations answer "Why P rather than Q?" — the foil Q is always (implicitly) present | Systems must support contrastive queries, not just causal attribution | p. 3 |
| 2. Selected (biased) | People expect 1–2 causes, not a complete causal chain; selection is cognitively biased | Systems should not overwhelm users with all causes — select the most relevant difference | p. 3 |
| 3. Social | Explanations are conversations — they transfer knowledge between explainer and explainee, tailored to context | Explanation output must be contextually relevant and responsive to the user's actual question | p. 3 |
| 4. Causal > Probabilistic | Statistical relationships are less effective than causal framing; likelihood of cause matters less than explanatory relevance | Do not present probability scores as explanations; present causal/constraint-based reasons | p. 3 |

### Hilton's Conversational Model of Explanation (p. 29)

| Stage | Hva det er | Side |
|---|---|---|
| Diagnosis | Explainer determines why an action/event occurred (causal attribution) | p. 29 |
| Explanation presentation | Social process of conveying this to someone; must "resolve a puzzle in the explainee's mind" | p. 29 |
| Cooperative principles (Grice's maxims) | Quality, Quantity, Relation, Manner — guide how explanations should be communicated | p. 29 |

---

## Key arguments / lines of reasoning

### Argument 1: XAI cannot solve the trust problem by causal attribution alone

- **Premiss 1:** Most XAI research focuses on causal attribution — identifying and displaying a causal chain for a decision.
- **Premiss 2:** Causal attribution is not the same as explanation; displaying a causal chain to a lay user does not constitute an explanation they can use.
- **Premiss 3:** Social science shows explanation is contrastive, selected, and social — properties a raw causal chain does not have.
- **Konklusjon:** Explainable AI systems that present causal chains are only solving "the easiest part of the problem" (p. 11). Systems that aim to build trust must also address how explanations are structured and communicated.
- **Sted:** pp. 11–12 (§2.6.1)
- **Hvilke claims dette støtter:** Ch 2.2 ¶5; Ch 5.3 ¶2

### Argument 2: For trust-building, simplicity > accuracy of cause

- **Premiss 1:** The goal of an explanatory agent is sometimes to generate trust, not just to transfer the true cause.
- **Premiss 2:** Simpler explanations are more likely to be understood and accepted.
- **Konklusjon:** A planning system aiming at trust-based adoption should prioritise simple, coherent, contrastive explanations over technically complete scoring breakdowns.
- **Sted:** p. 28 (§4.6.6)
- **Hvilke claims dette støtter:** Ch 2.2 ¶5; Ch 5.3 ¶2

---

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| Arthropod classification algorithm (spider vs. beetle) | Running example throughout; used to illustrate contrastive questions ("Why spider instead of beetle?") vs. plain-fact questions | pp. 4, 12 |
| Robotic search-and-rescue planning | Shows that planning systems need explanations at the final/goal level (why this action over alternatives) — not just mechanistic/formal levels | p. 12 |
| AI planning for optimisation criteria | "For AI planning agents that optimise some metric, such as cost, the explanation that action a was chosen over action b because it had lower cost is a CHR explanation" | p. 19 (§3.6.2) |
| Recommender system for songs (Kulesza et al.) | Shows soundness vs. completeness vs. overwhelming trade-off; complete but unsound reduced trust | p. 26–27 |

---

## Data og statistikk

Kilden presenterer ingen kvantitative data om adopsjonsrater, feil, eller statistikker som er direkte relevante for thesis-spine. Kildene den siterer (Kulesza et al.) inneholder brukersstudieresultater om forklaringskvalitet, men disse er sekundære.

---

## Forfatter-perspektiv / metodologi

Miller gjennomfører en bred litteraturgjennomgang (over 250 artikler fra filosofi, kognitiv psykologi og sosialpsykologi) og destillerer teoretiske implikasjoner for XAI. Artikkelen er programmatisk og normativ — den foreskriver hva XAI *bør* gjøre, grunnlagt i empirisk sosialvitenskapelig litteratur, men inneholder ingen egne primærstudier eller evalueringer av spesifikke systemer.

## Spot-check verification

Verifisert 2026-04-28 av uavhengig Opus-pass mot `raw/miller2019explanation.pdf`. PDF-side = trykt side (ingen front matter-offset, artikkelen begynner på s. 1).

1. "due to ethical concerns [2] and a lack of trust on behalf of their users [166,101]" (p. 1) — `pdftotext -f 1 -l 1` — PASS
2. "Explanations are contrastive — they are sought in response to particular counterfactual cases" (p. 3) — `pdftotext -f 3 -l 3` — PASS
3. "It is clear that we should quite often assume from the outset that trust levels are low" (p. 34) — `pdftotext -f 34 -l 34` — PASS
4. "the solution to explainable AI is not just 'more AI'" (p. 2) — `pdftotext -f 2 -l 2` — PASS
5. Grice's four maxims and "Make your conversational contribution as much as is required..." (p. 29) — `pdftotext -f 29 -l 29` — PASS
6. Interpretability-definisjonen — opprinnelig oppført på p. 1, korrigert til p. 8 etter verifisering. Millers kanoniske definisjon "the degree to which an observer can understand the cause of a decision" står på p. 8.

**Result:** 5/5 spot-check quotes verified, 1 correction made (Interpretability page reference: p. 1 → p. 8).