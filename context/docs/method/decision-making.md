# Decision-Making — Ressursplanlegger

> **Owner: Both** — Embret and Mikael fill in jointly.
> This file provides the raw material for Section 3.4 (System Development Process)
> and Section 5 (Discussion) where the soundness of project decisions is reflected on.
> Companion to `context/docs/project/decision-log.md`, which records *what* was decided.
> This file documents *how* decisions were made — the framework, criteria, and process.

---

## Why This File Exists

A bachelor thesis at A-grade level is judged not only on the artefact and the findings,
but on the rigour of the process behind them. Sensors look for evidence that decisions
were deliberate, criteria-based, and traceable — not arbitrary. This file makes the
project's decision-making process explicit so the thesis can claim that rigour with
specific evidence rather than generic phrasing.

The text in the thesis should not reproduce this file. It should distil it into a
shorter, cited account in Chapter 3.4 and reference specific decisions in Chapter 5.

---

## Decision-Making Framework

The project's decision-making is structured by the Design Science Research (DSR)
methodology adopted in `context/docs/method/research-design.md`. DSR is inherently
iterative and decision-rich: each of Peffers et al.'s (2007) six phases produces
decisions that feed the next phase, and earlier decisions can be revisited as new
evidence emerges. Three principles govern how decisions were made in this project:

1. **Evidence-grounded.** No design or scope decision is made without traceable
   grounding in either user research (interview findings, fit/gap analysis) or
   technical analysis (benchmarks, requirements traceability). When grounding is
   weak, the decision is logged as provisional and revisited.
2. **Documented at the point of decision.** Significant decisions are written into
   `context/docs/project/decision-log.md` at the time they are made, in a fixed
   format (decision, alternatives considered, reason, consequence). This protects
   against post-hoc rationalisation in Chapter 5.
3. **Reviewed against the research question.** Each non-trivial decision is checked
   against the research question and sub-questions before being adopted. Decisions
   that do not advance the RQ are rejected or deferred to future work.

These principles are an explicit operationalisation of Hevner et al.'s (2004)
guidelines for DSR — particularly *design as a search process* and *research
contribution* — applied at the granularity of individual decisions rather than the
project as a whole.

---

## Categories of Decisions

Decisions in the project fall into four categories. Each category has its own
dominant criteria and primary evidence base.

| Category | Examples | Dominant criteria | Primary evidence |
|---|---|---|---|
| **Research decisions** | Method (DSR), interview design, sampling, analysis approach | Methodological fit, validity, time available | Methodology literature; supervisor input |
| **Requirements decisions** | What the system must/should do; MoSCoW priority; in/out of scope | Interview findings; fit/gap; user value | `interviews-summary.md`, `fitgap-summary.md` |
| **Technical decisions** | Stack, algorithm choice, architecture, data model | Technical fit, performance, team skills, longevity | Benchmarks; `decision-log.md`; tech docs |
| **Process decisions** | Sprint cadence, division of work, documentation strategy, supervisor cadence | Team capacity, agile fit, deadline | Sprint log; project plan |

The four categories are not equally weighted in the thesis. Research and requirements
decisions are central to the methodology and findings chapters; technical decisions
are central to the system description and discussion; process decisions provide
context but are not themselves a research contribution.

---

## Decision Criteria

Across all categories, decisions are evaluated against an explicit set of criteria.
Not every criterion applies to every decision, but each significant decision is
checked against the relevant subset.

1. **Grounding in user research.** Does the decision follow from interview findings,
   the fit/gap analysis, or stated user needs? Decisions without this grounding are
   only justified by methodological or technical necessity.
2. **Alignment with the research question.** Does the decision help answer the main
   RQ or one of the three sub-questions? Decisions that drift outside the RQ are
   rejected or moved to future work.
3. **Methodological soundness.** Is the decision defensible against established
   research methodology — DSR, qualitative analysis, validation criteria?
4. **Technical feasibility within scope.** Can the decision be implemented within
   the project's time, skill, and infrastructure constraints? Ambitious decisions
   must be matched to a realistic plan.
5. **Reversibility.** Is the decision easy to revise if it turns out to be wrong?
   Reversible decisions can be made faster and on weaker evidence; irreversible
   decisions require stronger justification.
6. **Cost of being wrong.** What is lost if the decision is wrong? High-cost
   decisions (algorithm choice, data model) require more analysis than low-cost
   decisions (UI copy, file structure).
7. **Consistency with prior decisions.** Does the decision contradict an existing
   decision? If yes, the prior decision is either confirmed or explicitly revised
   in the decision log — never silently overridden.

Criteria 5 and 6 are adapted from the standard heuristic in software engineering
that decision rigour should match the cost of reversal (often attributed to Bezos's
"two-way / one-way door" framing, but also present in agile literature on the
"last responsible moment" — see Highsmith, 2010).

---

## Roles and Responsibilities in Decision-Making

The project has two student authors and one supervisor. Decision authority is
divided as follows:

| Role | Primary domain | Decision authority |
|---|---|---|
| **Embret** | System development, algorithm, architecture, technical stack | Final say on technical decisions within agreed scope |
| **Mikael** | User research, requirements, thesis writing, methodology | Final say on research and writing decisions within agreed methodology |
| **Both (joint)** | Research question, scope, thesis structure, discussion claims, sustainability framing | Joint decision required; no unilateral changes |
| **Supervisor (Ali Alsam)** | Methodology fit, academic standards, evaluation rigour | Advisory; consulted on major decisions; not a co-author |

Joint decisions are made through discussion until consensus is reached. The default
when consensus is not reached is to defer the decision rather than impose one — a
deferred decision is preferable to a contested one, because contested decisions tend
to be revisited and undermine the project's coherence.

---

## When Decisions Are Made

Decisions occur at three points in the project rhythm:

1. **Sprint planning.** At the start of each iteration, the team decides what to
   build, what to research, and what to defer. Decisions here are usually scoped
   and reversible.
2. **Mid-sprint adjustments.** When new evidence emerges (a failing test, a missing
   constraint, an interview insight), decisions are revised. These are logged with
   the trigger explicitly stated.
3. **Supervisor meetings.** Higher-level decisions — methodology, scope, framing,
   thesis structure — are reviewed with the supervisor on a [FILL IN — frequency,
   e.g., biweekly] cadence. The supervisor's input is treated as advisory, not
   binding, but is documented when it changes a decision.

[FILL IN — confirm cadence, meeting format, and where decisions were captured
(written notes, GitHub issues, decision log directly).]

---

## How Decisions Are Documented

Three artefacts capture the decision history of the project:

- **`context/docs/project/decision-log.md`** — The canonical record of significant
  decisions in a fixed format (decision, alternatives, reason, consequence). One
  entry per decision. Used in Ch 3.4 and Ch 5 to substantiate claims about *why*
  the system looks the way it does.
- **`context/docs/project/change-log.md`** — Records significant changes from earlier
  versions of the system to the current version, including the trigger and impact
  of each change. Captures decisions to revise.
- **`context/docs/project/sprint-log.md`** — Records weekly progress and the
  decisions taken at sprint boundaries. Provides the chronological backbone the
  decision and change logs reference.

In the thesis, the decision log is the primary source. The thesis text should
*reference* specific log entries rather than reproduce them — and Chapter 5 in
particular should pick three to five high-impact decisions and analyse them in
depth, rather than enumerate the full log.

---

## Examples of Decisions and the Criteria Applied

These examples illustrate how the criteria above produced specific outcomes. They
are not the full list — the decision log is canonical.

### Choice of optimisation approach (multi-engine architecture)

- **Decision:** Implement three solvers in parallel — greedy, OR-Tools CP-SAT,
  Timefold — rather than committing to one.
- **Criteria applied:** Cost of being wrong (high — algorithm is core), reversibility
  (low for a single-solver design), grounding in user research (interviews show a
  speed/quality trade-off matters), alignment with RQ (the RQ asks about
  "algorithm-driven" planning, plural framings supported).
- **Outcome:** Multi-engine architecture allows comparative benchmarking, which
  itself becomes a research contribution.

### Scope: invoicing integration excluded

- **Decision:** Exclude invoicing integration despite multiple interviewees citing
  it as critical for adoption.
- **Criteria applied:** Technical feasibility within scope (very low — would require
  partner agreements with Timpex/Opter), alignment with RQ (RQ is about planning
  efficiency, not financial integration), cost of being wrong (low — addressable
  in future work).
- **Outcome:** Recorded as out of scope in `context/scope.md` and surfaced as
  future work in Ch 6.3 and adoption barrier in Ch 5.3.

### Methodology: DSR over case study or pure development

- **Decision:** Adopt DSR as the overarching methodology.
- **Criteria applied:** Methodological soundness (DSR is the established paradigm
  for artefact-centred research; Peffers, 2007; Hevner, 2004), alignment with the
  RQ (the RQ asks both *what is the problem* and *how can a system address it* —
  DSR is built for that combination), reversibility (low — methodology changes
  invalidate prior work).
- **Outcome:** Documented in `research-design.md`; structures all subsequent
  research and development decisions.

[FILL IN — additional examples from the decision log as it is populated.]

---

## Trade-offs and How They Were Resolved

Decision-making in a constrained project is mostly trade-off management. Three
recurring trade-offs shaped this project and are useful to surface in Chapter 5:

1. **Breadth vs depth of user research.** Seven interviews give breadth across
   company sizes and systems, but no single company is studied in depth. Resolved
   by accepting breadth as the priority because the RQ targets the sector, not a
   specific company.
2. **Algorithm sophistication vs explainability.** A more sophisticated algorithm
   produces better plans but is harder to explain to a coordinator who must trust
   it. Resolved by the multi-engine + scoring breakdown design, which lets the
   coordinator see *why* a plan was produced.
3. **System completeness vs research depth.** Time spent building features is time
   not spent on validation, writing, or analysis. Resolved by freezing scope at the
   point where each MoSCoW *Must* requirement is implemented, then prioritising
   validation and writing.

The thesis text should name the trade-offs explicitly and show that they were
managed, not avoided.

---

## Iteration and Revision of Decisions

DSR explicitly permits revisiting earlier decisions when new evidence emerges
(Peffers et al., 2007). Within this project, three categories of revision occurred:

- **Confirmed decisions.** A prior decision was reviewed and held — the absence of
  change is itself documented to demonstrate that the decision was tested against
  new evidence.
- **Refined decisions.** A prior decision is kept in spirit but adjusted in detail
  (e.g., adjusting MoSCoW priorities as interviews surface new concerns).
- **Reversed decisions.** A prior decision is replaced. Reversals are recorded in
  the change log with the trigger event and impact analysis.

[FILL IN — examples of each category from the project history.]

---

## Threats to Decision Quality

A serious methodology section must acknowledge what could compromise decision
rigour. The following threats apply to this project:

- **Researcher–developer overlap.** The team that designs the system is the team
  that evaluates it. Decisions about what to build can be biased toward what is
  interesting to build. Mitigated by interview-grounded requirements, MoSCoW
  prioritisation tied to interview frequency, and structured requirements
  traceability.
- **Time pressure.** A bachelor project has a hard deadline. Late-project decisions
  may favour speed over rigour. Mitigated by the principle that scope is reduced
  before quality — out-of-scope features are documented as future work rather than
  rushed.
- **Confirmation bias in interpreting interviews.** The team that wrote the
  interview guide also analysed the data, which risks over-fitting findings to
  preconceived solutions. Mitigated by recording verbatim quotes in the
  interviews-summary, by having both authors review the analysis, and by making
  the fit/gap analysis explicit and traceable.
- **Sunk cost in technical decisions.** Once code is written, there is pressure to
  defend the original decision rather than reverse it. Mitigated by the change log
  pattern: reversals are explicit, not silent, and reversal cost is treated as
  acceptable when justified.
- **Single supervisor, single perspective.** Methodological feedback comes from one
  person. Mitigated by reading published DSR theses and methodology literature
  to triangulate against external standards.

---

## What This Material Supports in the Thesis

| Chapter / Section | What this material contributes |
|---|---|
| **3.4 — System Development Process** | Description of how research, requirements, and technical decisions were sequenced and documented; reference to the decision log as evidence. |
| **3.5 — Validity and Reliability** | The threats above and their mitigations; rigour of decision-making as a validity argument. |
| **5.2 — Algorithm and HITL** | Trade-off analysis between algorithm sophistication and explainability; multi-engine decision rationale. |
| **5.3 — Adoption Barriers** | Scope decisions (e.g., invoicing) framed as informed trade-offs rather than oversights. |
| **5.6 — Limitations** | Researcher–developer overlap and confirmation bias as decision-quality threats. |
| **6.3 — Future Work** | Decisions deferred to future work, traceable to specific criteria. |

---

## Sources to Cite (when this material is used in the thesis)

The thesis text drawing on this file should cite:

- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design
  Science Research Methodology for Information Systems Research. *Journal of
  Management Information Systems*, 24(3), 45–77.
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in
  Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
- Wieringa, R. J. (2014). *Design Science Methodology for Information Systems and
  Software Engineering*. Springer.
- Highsmith, J. (2010). *Agile Project Management: Creating Innovative Products*
  (2nd ed.). Addison-Wesley. — for "last responsible moment" and reversibility-
  weighted decision-making.
- [FILL IN if cited: a MoSCoW source, e.g., DSDM Consortium (2014) or Clegg & Barker
  (1994), once Mikael confirms which is in `result/references.bib`.]

> Ensure all sources cited from this file are present in `result/references.bib`
> and `context/docs/method/literature-list.md` before the corresponding thesis
> section is written.

---

## What This File Does Not Contain

- The full list of decisions — that is `context/docs/project/decision-log.md`.
- The full chronology of changes — that is `context/docs/project/change-log.md`.
- Methodological justification of DSR itself — that is
  `context/docs/method/research-design.md`.
- Validity analysis at the project level — that is Section 3.5 and the validity
  notes in `research-design.md`.

This file is the bridge between the methodology (DSR) and the artefacts of the
process (the logs). It explains the rules the project followed when generating
those artefacts.
