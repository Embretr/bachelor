# Ethical Implications and Accountability of Algorithms (`martin2019accountability`)

## Status
- [x] Notes generated from raw (Claude, 2026-05-01)
- [ ] Verified by human (Mikael, YYYY-MM-DD)
- [x] Coverage assessment: SUFFICIENT
  - **Reasoning:** The article is read in full (16 pages, pp. 835–850). All sections directly relevant to thesis areas — algorithmic accountability, value-laden design, delegation of responsibility, transparency — are extracted with verbatim quotes and page numbers. The article's primary contribution maps cleanly onto §5.3 ¶3 (accountability dilemma).
  - **Gaps not investigated:** None. All 16 pages were read.

## Source metadata
- **BibTeX key:** `martin2019accountability`
- **Reference (APA 7):** Martin, K. (2019). Ethical implications and accountability of algorithms. *Journal of Business Ethics*, *160*(4), 835–850. https://doi.org/10.1007/s10551-018-3921-3
- **Tilgang:** Open Access (Creative Commons Attribution 4.0)
- **Raw source:** `../martin2019accountability.pdf`
- **Coverage in raw:** Full article, pp. 835–850 (PDF pages 1–16). Includes abstract, all body sections, discussion and conclusion, and full reference list.

## Sammendrag (2–3 setninger)

Martin (2019) argues that algorithms are value-laden rather than neutral — they create moral consequences, reinforce or undercut ethical principles, and enable or diminish stakeholder rights. Beyond the content of their biases, algorithms also delegate roles and responsibilities within decisions: firms that design algorithms are accountable not only for the values inscribed in the algorithm but for how much responsibility individuals are permitted to take within the algorithmic decision. Critically, the more inscrutable and autonomous an algorithm is designed to be, the greater the accountability attributed to the firm that designed it — a conclusion that directly inverts the common defence that algorithmic complexity absolvs developers of responsibility.

## Areas of interest investigated

| Område | Bidrag |
|---|---|
| §5.3 ¶3 (accountability dilemma — ethics of algorithms) | **Core fit** — Martin is explicitly named as the MUST CITE for the accountability dilemma sub-point in §5.3 |
| §5.3 ¶3 (fairness / privacy taxonomy — Mittelstadt complement) | Partial — Martin covers fairness and rights; privacy is secondary here |
| §5.1.2 Tillit/kontroll — operator authority and HITL | Indirect — Martin's argument that inscrutable algorithms remove human agency maps onto the inverse of the thesis's HITL design goal |
| §2.2 HITL theory | Outside scope — Martin does not address HITL design; her frame is accountability for harms, not design for transparency |
| §5.3 ¶5 (operator-vs-owner as ethics question) | Partial — the "whose efficiency, whose autonomy?" framing resonates with Martin's stakeholder-rights argument |

## Claims this source supports

### Claim: "Firms developing algorithms are accountable for designing how large a role individual will be permitted to take in the subsequent algorithmic decision."
- **Suggested for:** §5.3 ¶3 (accountability dilemma), possibly §5.3 ¶5 (operator-vs-owner as ethics question)
- **Direkte sitat:** "firms developing algorithms are accountable for designing how large a role individual will be permitted to take in the subsequent algorithmic decision" (p. 835)
- **Parafrase:** Accountability is not only about whether an algorithm produces biased outcomes, but about who-does-what within the decision — how much agency is left to humans when the algorithm is in use.
- **Forbehold:** Martin's empirical context is criminal sentencing and social goods allocation (COMPAS algorithm), not labour-management systems. The accountability norm she identifies is normative and theoretical, not empirically validated in workplace contexts.
- **Anvendelse på vårt case:** In Ressursplanlegger, Admmit and the development team make a design choice about how much authority the traffic coordinator retains (inspect, modify, accept, reject every algorithm-generated assignment). Martin's framework positions this design choice as an accountability decision: by designing for HITL override, Admmit accepts shared responsibility for outcomes; by making the algorithm inscrutable, the firm would bear greater unilateral responsibility.

### Claim: "If an algorithm is designed to preclude individuals from taking responsibility within a decision, then the designer of the algorithm should be held accountable for the ethical implications of the algorithm in use."
- **Suggested for:** §5.3 ¶3 (accountability dilemma — central claim)
- **Direkte sitat:** "I find that if an algorithm is designed to preclude individuals from taking responsibility within a decision, then the designer of the algorithm should be held accountable for the ethical implications of the algorithm in use" (p. 835)
- **Parafrase:** The more autonomous and inscrutable an algorithm, the more moral responsibility accrues to its designers rather than to its users or "society".
- **Forbehold:** The claim is derived from normative business ethics reasoning applied to high-stakes civil-rights decisions. It is not an empirical study of how accountability is actually attributed in practice.
- **Anvendelse på vårt case:** Ressursplanlegger is explicitly designed to expose algorithm reasoning and preserve coordinator override authority — the design choice is the ethical decision Martin describes. This citation supports the argument in §5.3 that the HITL design is not merely functional but ethically necessary: by enabling inspect/modify/accept/reject, the system distributes responsibility between algorithm and coordinator rather than concentrating it in the developer.

### Claim: "Algorithms are value-laden, rather than neutral, in that algorithms create moral consequences, reinforce or undercut ethical principles, and enable or diminish stakeholder rights and dignity."
- **Suggested for:** §5.3 ¶3 (opening framing of the ethics sub-section); also usable as background in §5.3 ¶1 (SusAF framing)
- **Direkte sitat:** "I conceptualize algorithms as value-laden, rather than neutral, in that algorithms create moral consequences, reinforce or undercut ethical principles, and enable or diminish stakeholder rights and dignity" (p. 835)
- **Parafrase:** The claim that algorithms are objective or neutral is a false premise; their design encodes preferences, priorities, and exclusions.
- **Forbehold:** Martin's analysis focuses on algorithms in high-stakes public decisions (sentencing, housing, hiring). Transport assignment decisions are lower-stakes from a civil-rights perspective, but the structural argument about value-laden design still applies.
- **Anvendelse på vårt case:** Ressursplanlegger's soft-constraint weight system and objective function encode preferences — e.g., workload balance vs. driver preference vs. priority — that are not neutral. Martin's framework legitimates naming these as value choices rather than technical parameters.

### Claim: "The more the algorithm is constructed as inscrutable and autonomous, the more accountability attributed to the algorithm and the firm that designed the algorithm."
- **Suggested for:** §5.3 ¶3 (accountability dilemma); can support the argument that HITL is an ethics design requirement, not merely a usability feature
- **Direkte sitat:** "the more the algorithm is constructed as inscrutable and autonomous, the more accountability attributed to the algorithm and the firm that designed the algorithm" (p. 844)
- **Parafrase:** Inscrutability does not reduce accountability; it amplifies it and concentrates it in the developer.
- **Forbehold:** This is a normative claim about how accountability *should* be allocated in business ethics terms. It is not a legal standard or an empirically observed allocation pattern.
- **Anvendelse på vårt case:** The thesis's transparency design choices — deviation alerts, scoring breakdown, the time-quality control surface — can be argued in §5.3 as reducing the accountability burden on Admmit by enabling coordinators to take shared responsibility for algorithmic outcomes.

### Claim: "Firms make a moral choice as to the delegation of tasks and responsibilities between algorithms and individuals in design."
- **Suggested for:** §5.3 ¶3; §5.3 ¶5 (operator-vs-owner asymmetry as ethics question)
- **Direkte sitat:** "in addition to the design of value-laden biases, firms make a moral choice as to the delegation of tasks and responsibilities between algorithms and individuals in design" (p. 843)
- **Parafrase:** Every design decision about what the algorithm decides vs. what the human decides is a moral decision — whether or not the designer acknowledges it.
- **Forbehold:** Martin draws on STS scholars Latour and Akrich to make this argument; the framing is theoretical and applied to adversarial contexts (criminal sentencing). The normative weight is strongest where decisions affect fundamental rights.
- **Anvendelse på vårt case:** The Admmit mandate for HITL — formulated before interviews validated it — can be read through Martin as an ethical design decision: the system was designed to *not* preclude the coordinator from taking responsibility, a choice that distributes accountability between developer and operator.

### Claim: "Creating inscrutable algorithms precludes users from taking responsibility for the ethical implications identified above and places the responsibility of the ethical implications on the firm who developed the algorithm."
- **Suggested for:** §5.3 ¶3 (accountability dilemma); inverse argument supports HITL transparency design
- **Direkte sitat:** "Creating inscrutable algorithms precludes users from taking responsibility for the ethical implications identified above and places the responsibility of the ethical implications on the firm who developed the algorithm" (p. 844)
- **Parafrase:** When users cannot understand or override an algorithm, they cannot bear moral responsibility for its outcomes — the developer bears it all.
- **Forbehold:** Applies most forcefully to high-stakes automated decisions. For transport assignment, consequences are more mundane (suboptimal route efficiency, driver dissatisfaction) than the criminal justice harms Martin analyses.
- **Anvendelse på vårt case:** The deviation detection system and drag-and-drop override surface in Ressursplanlegger are not just UX features — by making the algorithm's reasoning visible and correctable, the system enables coordinators to own decisions, distributing moral responsibility. Martin provides the normative grounding for why this matters.

## Application to our domain — terminology mapping

| Kildens term | Vårt domene-ekvivalent | Notat |
|---|---|---|
| "inscrutable algorithm" | Black-box solver without override or explanation | Ressursplanlegger is explicitly designed *not* to be inscrutable |
| "delegation of roles and responsibilities" | HITL override flow (inspect / modify / accept / reject) | Martin's key analytical concept maps onto the four HITL actions |
| "value-laden biases" | Soft-constraint weights, objective function priorities | The weight configuration UI is a surface where value choices are made explicit |
| "individuals in the decision" | Traffic coordinator | The coordinator is the "individual" whose role must be preserved |
| "the firm developing the algorithm" | Admmit / the development team | Admmit takes on the normative obligations Martin describes by entering the transport-planning market |
| "accountability" | Tillit/kontroll (inseparable from operator authority) | Martin's accountability frame is the ethical dimension of Tillit/kontroll |
| "decision context" | Norwegian transport company planning context | Martin's social-contract argument: entering the market creates obligations to respect norms of the decision community |

## Forbehold og begrensninger

- **Domain mismatch:** Martin's primary empirical case is COMPAS — a criminal sentencing risk-assessment algorithm with profound civil-rights implications (incarceration, racial disparate impact). Ressursplanlegger operates in a much lower-stakes labour-management context. The normative weight of her accountability claims is strongest where fundamental rights are at stake; transport assignment is ethically significant but not in the same category.
- **Normative, not empirical:** This is a business ethics argument, not an empirical study. It identifies what *should* be the case regarding accountability, not what firms or courts actually do or believe.
- **No operational design guidance:** Martin identifies what firms are accountable *for*, but does not specify how to design accountable systems. The practical design implications for Ressursplanlegger must be inferred by the writer — they are not stated in the source.
- **Context of "individual in the decision":** Martin's "individuals" are defendants, job applicants, and loan seekers — people whose lives are affected by algorithmic decisions. In our context the "individual" is the coordinator (a professional operator), not an affected party. The accountability argument is still structurally applicable but operates at a different ethical intensity.
- **No transport or logistics coverage:** The source contains no sector-specific content about transport, logistics, or workforce scheduling. All domain application is inference from the general framework.

## Definisjoner gitt av kilden

| Term | Definisjon (verbatim) | Side |
|---|---|---|
| Algorithm (as value-laden) | "algorithms create moral consequences, reinforce or undercut ethical principles, and enable or diminish stakeholder rights and dignity" | 835 |
| Accountability (for algorithmic design) | "firms developing algorithms are accountable for designing how large a role individual will be permitted to take in the subsequent algorithmic decision" | 835 |
| Value-laden algorithm | "algorithms are inscribed with a preferred set of outcomes with ethical implications" | 843 |

## Rammeverk og modeller

### Firm Responsibility for Algorithms — 2×2 matrix (Fig. 4, p. 845)

| Quadrant | Role of Algorithm in Decision | Role of Decision in Society | Type of Responsibility |
|---|---|---|---|
| A | Large | Minimal | Standard Setting |
| B | Small | Minimal | Product Liability |
| C | Small | Pivotal | Contract |
| D | Large | Pivotal | Principal-Agent |

**Relevance for thesis:** Ressursplanlegger operates in a context closer to B/C than D — the algorithm plays a role in a decision (labour assignment) that has limited direct societal impact compared to sentencing or housing. This places primary responsibility closer to product liability and contract norms rather than the fiduciary-level obligations Martin describes for pivotal decisions. The writer should note this calibration rather than over-applying Martin's accountability claim.

### Three-category taxonomy of algorithmic ethical implications (pp. 837–839)

| Category | What it means | Example in source |
|---|---|---|
| Creating moral consequences | Algorithm produces disparate or unjust outcomes | COMPAS racial disparate impact |
| Reinforcing/undercutting ethical principles | Algorithm encodes or violates context-specific norms | Using parental criminal record as sentencing factor |
| Enabling/diminishing stakeholder rights and dignity | Algorithm restricts access to information or process | Defendants unable to question COMPAS scoring |

## Key arguments / lines of reasoning

### Argument: Inscrutability amplifies, not reduces, accountability
- **Premiss(er):** (1) Inscrutable algorithms are designed to minimize the role of individuals in the decision. (2) Delegating a task to a technology does not remove the associated responsibility for that task. (3) The inscrutable defence ("it's too complicated to explain") does not absolve firms.
- **Konklusjon:** Inscrutable algorithms that minimize human agency generate *more* accountability for the designer, not less.
- **Sted:** pp. 843–844
- **Hvilke claims dette støtter:** §5.3 ¶3; the inverse argument supports HITL as an ethical design requirement

### Argument: Designing an algorithm prescribes a delegation of moral responsibility
- **Premiss(er):** (1) Algorithms delegate tasks between human and non-human actors (Latour/Akrich frame). (2) Firms make a moral choice — whether acknowledged or not — about this delegation in design. (3) This choice determines who can be held responsible for algorithmic outcomes.
- **Konklusjon:** The design decision about human vs. algorithmic roles is itself a moral decision that firms cannot disclaim.
- **Sted:** pp. 840–843
- **Hvilke claims dette støtter:** §5.3 ¶3, §5.3 ¶5

### Argument: Entering a decision market creates social-contract obligations
- **Premiss(er):** (1) Firms that sell algorithms into a decision context become members of that community. (2) Membership creates obligations to respect the norms of that community's decisions. (3) A firm unwilling to abide by those norms should not be in that market.
- **Konklusjon:** Admmit, by selling Ressursplanlegger into the Norwegian transport planning context, takes on obligations to respect the norms of that decision domain — including what coordinators can reasonably expect from an algorithm-assisted tool.
- **Sted:** p. 844
- **Hvilke claims dette støtter:** §5.3 ¶3 (accountability dilemma); background for §5.3 ¶5

## Examples / case studies kilden bruker

| Eksempel | Hva det illustrerer | Side |
|---|---|---|
| COMPAS sentencing algorithm (Northpointe) | Paradigm case of value-laden, inscrutable algorithm with racial disparate impact | 835–839 |
| Latour's door hinge / hydraulic door closer | Algorithms as actants delegating tasks from humans to non-human actors | 841 |
| Latour's seat belt that "makes you moral" | Delegating task to technology removes human need to perform the task — but not the moral responsibility | 842 |
| Akrich's two-handled Angolan hoe | Scripts inscribed in technology persist beyond designer's intentions | 840 |
| University admissions ML algorithm | Value-laden biases encoded through training data | 846 |

## Data og statistikk

| Tall/data | Enhet | År/scope | Side |
|---|---|---|---|
| 44.9% vs 23.5% | Black vs. white defendants falsely labeled higher risk (COMPAS) | 2016 / US criminal justice | 838 |
| 28.0% vs 47.7% | Black vs. white defendants labeled lower risk who re-offended | 2016 / US criminal justice | 838 |
| 20% | People predicted to commit violent crimes who actually did so (COMPAS) | 2016 | 838 |

*Note: These statistics are from the criminal justice domain and cannot be cited for transport planning purposes. They are included here for completeness; the writer should use Martin's theoretical framework only, not her empirical data.*

## Forfatter-perspektiv / metodologi

Martin (2019) is a normative business ethics paper using conceptual analysis and STS theory (Latour, Akrich). It draws on case analysis of the COMPAS algorithm and secondary sources (ProPublica reporting, legal scholarship). No primary empirical data collection is conducted. The article is open access, published in the *Journal of Business Ethics* and supported by the US National Science Foundation.

## Spot-check verification

1. Quote: "firms developing algorithms are accountable for designing how large a role individual will be permitted to take in the subsequent algorithmic decision" (p. 835) — verified via `pdftotext -f 1 -l 1` on the PDF — the abstract text reads verbatim: "firms developing algorithms are accountable for designing how large a role individual will be permitted to take in the subsequent algorithmic decision" — **PASS**

2. Quote: "the more the algorithm is constructed as inscrutable and autonomous, the more accountability attributed to the algorithm and the firm that designed the algorithm" (p. 844) — verified via `pdftotext -f 10 -l 10` — text reads verbatim: "the more the algorithm is constructed as inscrutable and autonomous, the more accountability attributed to the algorithm and the firm that designed the algorithm" — **PASS**

3. Quote: "in addition to the design of value-laden biases, firms make a moral choice as to the delegation of tasks and responsibilities between algorithms and individuals in design" (p. 843) — verified via `pdftotext -f 9 -l 9` — text reads verbatim: "in addition to the design of value-laden biases, firms make a moral choice as to the delegation of tasks and responsibilities between algorithms and individuals in design" — **PASS**

4. Quote: "Creating inscrutable algorithms precludes users from taking responsibility for the ethical implications identified above and places the responsibility of the ethical implications on the firm who developed the algorithm" (p. 844) — verified via `pdftotext -f 10 -l 10` — text reads verbatim as stated — **PASS**

**Result:** 4/4 quotes verified, 0 corrections made.