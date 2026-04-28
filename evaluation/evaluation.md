# Chapter-Level Evaluation Checklist — Ressursplanlegger

> The quality agent reads this before and after reviewing any chapter.
> Based on: NRT grading criteria (grading-guidelines.md), A-grade rubric (a-grade-rubric.md),
> Malterud's four criteria, and NTNU-specific requirements.

---

## All Chapters

- [ ] Formal, academic English — no filler words, no "we believe"
- [ ] Every claim has a citation or is grounded in own data
- [ ] Consistent terminology from `context/glossary.md` — no synonyms introduced (no "driver"/"employee" drift, no "planner"/"dispatcher" drift)
- [ ] Correct APA 7 citations (`\parencite{}` / `\textcite{}`)
- [ ] All cited sources are `approved-read` in `context/docs/method/literature-list.md` and present in `result/references.bib`
- [ ] Every paragraph has a clear topic sentence
- [ ] Transitions between paragraphs and sections are explicit (bridge ideas, not "Furthermore" filler)
- [ ] Tense is consistent (present for theory, past for what was done)
- [ ] Section serves its chapter's thesis-spine sentence
- [ ] No scope creep — nothing outside `context/scope.md`

### Writing discipline (sensor-visible signals)

These derive from advisor feedback on Ch 2. Violations are usually visible within the first page.

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Paragraph = one idea | No paragraph mixes two or three unrelated concepts (e.g. multi-resource + single-resource + valid driver; NP-hard + heuristics + solver engines). State in one sentence what each paragraph is about — if the sentence needs "and", split the paragraph. |
| [ ] | Orientation before detail | For enumerable content (constraint types, solver engines, automation levels, requirement categories), the taxonomy is presented first (as a sentence or table) BEFORE the items are explained. |
| [ ] | Broad → specific ordering | When a theoretical concept is introduced, the reader is grounded with concrete examples/context BEFORE the formal definition, not after. |
| [ ] | Narrative framing early | If a chapter or section depends on understanding how the work is done today (how planners plan, what the artefact does), that context appears in the first paragraphs, not halfway down. |
| [ ] | Definitions are short, direct, and sourced | Every definition is short, taken from (or paraphrased from) a cited source, and free of qualifiers the source did not use ("limited", "complex", "various"). No invented definitions. |
| [ ] | Simple vocabulary | Simple words preferred. Complex terms ("competencies", "tacit knowledge") are introduced and explained, not used as if self-explanatory. |
| [ ] | Robot-prompt precision | The reader never has to speculate about the meaning of a sentence. Adjectives are justified ("limited" — limited how, and according to whom?). Domain words taken from sources ("each machine") are translated to our terms (vehicles, drivers) or their mapping is stated. |
| [ ] | Decisions have rationale | Every described decision (methodological, algorithmic, architectural, UI, scope) states the reason, not just the choice. "The system lets the planner set a time limit BECAUSE interviews showed..." — not just the first half. |
| [ ] | Technical depth where required | For algorithm, constraints, solver choice, NP-hardness, architecture: the text goes beyond description (trade-offs, limitations, rejected alternatives). |
| [ ] | Concept introduced before first use | No term or acronym (VRP, CP-SAT, tacit knowledge) appears before it is defined in this or an earlier section. |
| [ ] | Selective source use | Each citation supports the exact claim being made, not the source's general topic. Broad sources are not used as blanket coverage for narrow claims. |
| [ ] | Interviews integrated | Where theory or discussion has an obvious interview connection, that connection is made explicit in the same paragraph or the next, not as a separate aside. |

---

## Source Quality Checks

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Claim coverage | Each source-dependent claim is supported by either an approved citation, interview data, requirements evidence, benchmark data, or documented system evidence. |
| [ ] | Source fit | The cited source directly supports the claim being made, not merely the general topic. |
| [ ] | Authority | Foundational claims use authoritative textbooks, primary papers, official documentation, or high-quality peer-reviewed sources. |
| [ ] | Integration | Citations are interpreted and connected to Ressursplanlegger; they are not name-dropped. |
| [ ] | Reuse sanity | The same source is not used to support unrelated claims beyond its scope. |
| [ ] | No orphan sources | Every cited source clearly supports a claim in the surrounding sentence or paragraph, and every bibliography/source-list entry planned for the chapter is either used, deferred, or removed. |
| [ ] | Approval status | `candidate` and `agent-reviewed` sources are treated as unusable until manually marked `approved-read`. |

---

## Chapter 1 — Introduction

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Problem is clearly motivated — reader understands *why* this matters | A non-expert should grasp the problem after reading 1.1 |
| [ ] | Research question is stated precisely | Verbatim from `context/context.md` |
| [ ] | Three sub-questions are listed with brief explanation | Match context.md |
| [ ] | Scope is precisely delimited — in/out is unambiguous | Cross-check with `context/scope.md` |
| [ ] | Division of work stated (who did what) | Mikael: user research. Embret: development. |
| [ ] | Reader guide matches thesis-spine | One sentence per chapter, consistent |
| [ ] | Ressursplanlegger is introduced clearly in one paragraph | Not too detailed — that is Ch 4 |

---

## Chapter 2 — Theory

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | VRP defined and connected to this project's problem | Not just textbook VRP — mapped to driver/vehicle assignment |
| [ ] | HITL/automation levels discussed with source | Parasuraman (2000), Sheridan & Verplank (1978) |
| [ ] | TMS landscape described factually | Timpex, Trimtex, Opptur — what they do and don't do |
| [ ] | DSR methodology introduced with citations | Hevner (2004), Peffers (2007), Wieringa (2014) |
| [ ] | **Every theory introduced is used later** in Ch 4 or Ch 5 | If a theory is not referenced again, remove it |
| [ ] | Theory chapter is "pure" — no own empirical data mixed in | Findings belong in Ch 4, not here |
| [ ] | Related work is woven into sections, not a thin standalone section | Integrated into 2.1 and 2.2 |

---

## Chapter 3 — Methodology

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | DSR choice is justified — not just stated | Why DSR and not case study? Why not pure quantitative? |
| [ ] | DSR phases mapped to this project in a table | Peffers' six phases → what was done |
| [ ] | Interview process documented precisely enough to reproduce | Who, when, how many, how long, what questions, how transcribed |
| [ ] | Thematic analysis method described with citation | Braun & Clarke (2006) |
| [ ] | Validation vs evaluation distinction made explicit | Wieringa (2014) — we validate, not evaluate |
| [ ] | Malterud's four criteria addressed | Systematic reflection, relevance, validity, reflexivity |
| [ ] | Researcher bias acknowledged and mitigated | Dev team = research team → confirmation bias risk |
| [ ] | Ethical considerations documented precisely | Consent, anonymisation/company naming, data storage, transcription-tool handling, Sikt/NSD status |
| [ ] | Limitations stated honestly — not buried | Sample size, no production deployment, single-day interviews |

---

## Chapter 4 — Findings

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Interview findings presented thematically, not per-company | Themes across companies, not 7 separate summaries |
| [ ] | Findings are *presented*, not *interpreted* | Interpretation belongs in Ch 5 |
| [ ] | Requirements table with MoSCoW, source, and implementation status | Cross-check with `functional-requirements.md` |
| [ ] | Fit/gap analysis is clear — what existing systems do/don't do | Feature coverage matrix from `fitgap-summary.md` |
| [ ] | System description is technical but accessible | Architecture, data model, key components — not a code walkthrough |
| [ ] | Algorithm is documented: input, output, constraints, solvers | Reference `context/docs/tech/algorithm.md` |
| [ ] | Multi-engine comparison explained — why three solvers? | Greedy (speed), CP-SAT (quality), Timefold (scale) |
| [ ] | Solver benchmarking results are presented with limits | Dataset sizes, runtime, scheduled %, violations, score; source `benchmark-results.md` |
| [ ] | Conflict detection system described | What conflicts are detected, how they are displayed |

---

## Chapter 5 — Discussion

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | **Discusses, not just presents** — weighs multiple perspectives | Writing action level = "drøfte" — must argue, compare, evaluate |
| [ ] | Findings connected back to theory from Ch 2 | VRP theory → algorithm results. HITL theory → override design. |
| [ ] | Algorithm performance discussion is grounded in benchmark evidence | Ch 5.2 uses Ch 4.5 + `benchmark-results.md`, not unsupported performance claims |
| [ ] | Research question addressed — reader can see the answer forming | Each sub-question should be implicitly answered by the end of Ch 5 |
| [ ] | Adoption barriers discussed honestly | Invoicing gap, trust, cost, training |
| [ ] | Tacit knowledge dilemma explored | System captures some but not all — what are the implications? |
| [ ] | Sustainability section uses SusAF framework | 5 dimensions, 3 effect levels, effects table, SDG mapping |
| [ ] | Sustainability dilemmas discussed — not just positive effects | Efficiency vs deskilling, automation vs autonomy |
| [ ] | Ethical perspective included | Algorithmic fairness, accountability, privacy |
| [ ] | Limitations are specific, not generic | Not "more interviews would be better" but *why* and *what it means* |
| [ ] | Validation framing used — not evaluation claims | "The validation suggests..." not "The system proves..." |

---

## Chapter 6 — Conclusion

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | Main RQ answered directly — one clear paragraph | Verbatim question, then answer |
| [ ] | All three sub-questions answered explicitly | SQ1, SQ2, SQ3 — each addressed |
| [ ] | SQ3 is treated as mandatory, not conditional | Must answer extent addressed + limitations |
| [ ] | Mirrors the introduction — reader sees the full arc | Start broad in Ch 1, end broad in Ch 6 |
| [ ] | No new information introduced | Conclusion summarises and concludes, nothing new |
| [ ] | Contributions stated clearly | What does this thesis add? (artefact + knowledge) |
| [ ] | Future work is concrete and reasoned | Not a wish list — specific next steps with justification |
| [ ] | Tone is appropriately confident but not overstated | "The thesis demonstrates..." not "The thesis proves..." |

---

## Cross-Chapter Checks (run after all chapters are drafted)

- [ ] **Red thread:** Does the argument flow logically from Ch 1 → 6? Does every chapter serve its spine sentence?
- [ ] **No orphaned theory:** Is every concept from Ch 2 referenced in Ch 4 or 5? Check `evaluation/theory-usage.md` for tracking.
- [ ] **Post-Ch 5 orphan check:** After Chapter 5, any theory still marked `planned` or unused in `evaluation/theory-usage.md` must be connected or removed.
- [ ] **No unsupported claims in Ch 5:** Is every discussion point grounded in a finding from Ch 4?
- [ ] **Consistent terminology:** Are the same terms used throughout? (Check glossary)
- [ ] **Citation balance:** Are there chapters with suspiciously few or many citations?
- [ ] **Scope adherence:** Does any chapter describe features not in `context/scope.md`?
- [ ] **Contribution clarity:** Can a reader tell what Mikael did vs. Embret vs. what the system does?
- [ ] **Proportionality:** Actual chapter word/page counts are within ±20% of outline targets, unless a clear reason is documented.
