# Research Design — Ressursplanlegger

> **Owner: Mikael** — fill in before writing Chapter 3.
> This file provides the raw material for Section 3.1 (Research Design).
> The thesis text should elaborate on these points with proper citations.

---

## Chosen Method

**Method:** Design Science Research (DSR)

**Definition:** Design Science Research is a research paradigm in which the researcher creates and evaluates an artefact — a system, model, or method — to address an identified problem. The research contribution lies in both the artefact itself and the knowledge generated through designing and evaluating it.

**Key reference:** Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.

**Secondary reference:** Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.

> Ensure both references are in `result/references.bib`.

---

## Justification

**Why DSR fits this project:**
This thesis combines two activities: (1) investigating a real-world problem through user research, and (2) building a software system to address that problem. DSR is designed precisely for this combination — it treats the artefact (Ressursplanlegger) as a research outcome and structures the process around iterating between problem understanding and solution design. The evaluation of the artefact against user needs produces generalisable knowledge about algorithm-assisted resource planning in transport.

**Why not qualitative case study alone:**
A pure case study would document the problem and context but would not include the design and construction of a solution. Since the primary contribution of this thesis is a working system with an optimisation algorithm, a method that explicitly accounts for artefact creation is needed.

**Why not purely quantitative:**
The research question requires understanding how traffic coordinators work, what they need, and how they respond to an algorithm-assisted workflow. These are qualitative questions that cannot be answered through quantitative measurement alone. The quantitative elements (algorithm benchmarks, solution scores) are embedded within the broader DSR framework.

---

## How the Method Is Applied

The DSR process follows the six-phase model from Peffers et al. (2007):

| DSR Phase | What was done in this project |
|-----------|-------------------------------|
| **1. Problem identification** | Semi-structured interviews with 7 traffic coordinators across Norwegian transport companies. Identified manual assignment, tacit knowledge dependency, and legacy system limitations as core problems. |
| **2. Define objectives** | Derived functional and non-functional requirements from interview findings. Conducted fit/gap analysis comparing existing systems to identified needs. Defined the objective: a platform that automates initial plan generation while keeping the coordinator in control. |
| **3. Design & development** | Iterative development of Ressursplanlegger: planning interface, multi-engine optimisation (greedy, OR-Tools, Timefold), conflict detection, driver/vehicle management. Agile sprints with continuous refinement based on emerging understanding of the domain. |
| **4. Demonstration** | [FILL IN — how was the system demonstrated? E.g., demo to interviewees, walkthrough with supervisor, live test with sample data] |
| **5. Evaluation** | [FILL IN — how was the system evaluated? E.g., user testing with traffic coordinators, algorithm benchmarks on synthetic datasets, comparison against requirements traceability matrix] |
| **6. Communication** | This thesis — presenting the problem, solution, and findings to an academic audience. |

> Phases 4 and 5 must be filled in once demonstration and evaluation are completed.

---

## Data Collection Methods

### Semi-structured interviews
- **Purpose:** Understand current planning practices, pain points, and attitudes toward automation.
- **Participants:** 7 traffic coordinators / transport managers from Norwegian companies of varying size and system maturity.
- **Date:** 4 March 2026.
- **Format:** Phone interviews, recorded with consent.
- **Duration:** [FILL IN — e.g., 30–60 minutes per interview]
- **Transcription:** Automated transcription via Sonix.ai, followed by manual review and correction.
- **Interview guide:** Covered current tools, daily workflow, assignment criteria, pain points, sick-leave handling, attitude toward automation, and adoption criteria.

### Thematic analysis
- **Purpose:** Identify recurring themes across interviews to inform requirements.
- **Method:** Transcripts were analysed thematically — identifying, coding, and grouping recurring topics.
- **Output:** `context/interviews-summary.md` — distilled findings organised by theme.

### Fit/gap analysis
- **Purpose:** Compare what existing systems provide against what coordinators need.
- **Input:** Interview findings + existing system capabilities (Timpex, Trimtex, Opptur).
- **Output:** `context/fitgap-summary.md` — fit table and gap table.

---

## System Development Approach

- **Methodology:** Agile, iterative development with informal sprints.
- **Division of work:** Embret — system development and algorithm implementation. Mikael — user research, requirements, and thesis writing.
- **Interleaving:** User research findings fed directly into development priorities. Requirements were refined as the system took shape.
- **Tools:** GitHub for version control, [FILL IN — project management tool if any].
- **Sprint log:** `context/docs/project/sprint-log.md`

---

## Validation vs Evaluation (Wieringa, 2014)

This distinction is critical for how the thesis frames its results:

- **Evaluation:** Investigating the artifact as applied by real stakeholders in the field — i.e., deployed in a real transport company with real coordinators using it daily. This is **not possible** within the thesis timeframe.
- **Validation:** Predicting how the artifact will interact with its context *without* observing it in real-world deployment. This is what the thesis does — through prototyping, algorithm benchmarking, and comparison against requirements derived from interviews.

**Implication for writing:** Chapter 5 must be framed as validation, not evaluation. Use language like "the validation suggests" and "based on the benchmarks, the algorithm is expected to..." — never claim real-world impact that has not been measured. Acknowledge explicitly that evaluation would require production deployment (future work).

**Reference:** Wieringa, R. J. (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.

> Add this reference to `result/references.bib` and `context/docs/method/literature-list.md`.

---

## Limitations of This Method

- **No production deployment:** The system was not deployed in a real transport company during the thesis period. Evaluation is based on demonstration and benchmarking, not on real-world operational data. This limits the strength of claims about practical impact.
- **Small sample size:** Seven interviews provide rich qualitative data but cannot claim statistical generalisability to the entire Norwegian transport sector.
- **Researcher–developer overlap:** The development team is also the research team. This creates a risk of confirmation bias — the researchers may unconsciously design the evaluation to favour the system they built. Mitigated by using structured requirements traceability and, where possible, external feedback.
- **Single iteration:** DSR ideally involves multiple design–evaluate cycles. Time constraints limited this project to one full cycle. A second iteration with production data would strengthen the findings.
- **Validation, not evaluation:** Following Wieringa's (2014) distinction, this thesis validates the artifact through prototyping and benchmarking — it does not evaluate it through real-world deployment. Claims about practical impact are predictions, not observations.