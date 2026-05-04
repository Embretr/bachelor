# Chapter-Level Evaluation Checklist — Ressursplanlegger

> The quality agent reads this before and after reviewing any chapter.
> Based on: NRT grading criteria (grading-guidelines.md), A-grade rubric (a-grade-rubric.md),
> Malterud's four criteria, and NTNU-specific requirements.

---

## All Chapters

- [ ] **Anchor names verbatim:** the three locked English proper nouns are **Efficiency**, **Trust/control**, **Adaptability** — used consistently across the thesis, never re-translated to Norwegian, never split, never paraphrased. **Synonym drift is critical:** "effektivitet", "tillit/kontroll", "tilpasningsdyktighet", "control" alone, "fleksibilitet", "skalerbarhet", "human control", "menneskelig overstyring", "operator oversight", "trust calibration" — flag and reject.
- [ ] **No Trimtex or Opptur references:** They are factual errors. Only **Timpex** and **Opter** are named as real Norwegian TMS. Other interviewed companies use internal/custom tools. Neither Timpex nor Opter generates assignment plans automatically.
- [ ] Formal, academic English — no filler words, no "we believe"
- [ ] Every claim has a citation or is grounded in own data
- [ ] Consistent terminology from `context/glossary.md` — no synonyms introduced (no "driver"/"employee" drift, no "planner"/"dispatcher" drift)
- [ ] Correct APA 7 citations (`\parencite{}` / `\textcite{}`)
- [ ] Every cited source has a verified notes file at `context/docs/method/sources/raw/extracted/{bibkey}.md` and is present in `result/references.bib`
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
| [ ] | Concept introduced before first use | No term or acronym (CP-SAT, HITL, tacit knowledge) appears before it is defined in this or an earlier section. |
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
| [ ] | Source notes status | A source is usable in thesis prose only when its notes file at `context/docs/method/sources/raw/extracted/{bibkey}.md` exists, is filled, and is verified by human. |

---

## Chapter 1 — Introduction

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | **Visibility-gap opening** | First paragraph leads with a concrete Norwegian transport-sector fact and the resource-utilization visibility gap, not with "the transport sector's role in Norway" or "growing complexity" preamble. |
| [ ] | **§1.2 Anchor Concepts present and verbatim** | Three anchor concepts (Efficiency, Trust/control, Adaptability) defined verbatim with brief definitions in §1.2. Names match `context/glossary.md`. |
| [ ] | **Bainbridge framing** | Bainbridge (1983) referenced as the theoretical anchor for the operator-vs-owner asymmetry, somewhere in §1.1 or §1.3. |
| [ ] | Problem is clearly motivated — reader understands *why* this matters | A non-expert should grasp the problem after reading 1.1 |
| [ ] | Research question is stated precisely | Verbatim from `context/context.md` |
| [ ] | Three sub-questions listed; each is quotable as single-line block quote in Ch 6 | Match context.md and spine.md. Each SQ tied to one anchor. |
| [ ] | Scope is precisely delimited — in/out is unambiguous | Cross-check with `context/scope.md` |
| [ ] | Division of work stated (who did what) | Mikael: user research. Embret: development. |
| [ ] | Reader guide matches thesis-spine | One sentence per chapter, consistent |
| [ ] | Ressursplanlegger is introduced clearly in one paragraph | Not too detailed — that is Ch 4 |

---

## Chapter 2 — Theory

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | **Asymmetric depth** | HITL section dominates (longest); secondary concepts get under one page. Most argument-load-bearing theory gets the most space. |
| [ ] | **Three-layer HITL** | §2.2 layers Bainbridge (operator-vs-owner asymmetry) → Hoff & Bashir (trust calibration) → Miller (explanation), alongside Parasuraman taxonomy and Lee trust foundation. All three new sources cited. |
| [ ] | **Utilization framing in §2.1** | Resource scheduling reframed under utilization lens (overtime, idle time, load balance), not just constraint satisfaction. Preloads Ch 5.1.1 vocabulary. |
| [ ] | Resource scheduling defined and connected to this project's problem | Multi-resource assignment with constraints — mapped to driver/vehicle assignment, not generic textbook scheduling |
| [ ] | TMS as software category | Timpex and Opter named as real Norwegian TMS; others described generically as internal/custom tools. No Trimtex or Opptur. Neither Timpex nor Opter generates plans automatically. |
| [ ] | DSR methodology introduced with citations | Hevner (2004), Peffers (2007), Wieringa (2014) |
| [ ] | **Every theory introduced is used later** in Ch 4 or Ch 5 | If a theory is not referenced again, remove it |
| [ ] | Theory chapter is "pure" — no own empirical data mixed in | Findings belong in Ch 4, not here |
| [ ] | VRP referenced only as one-paragraph delimit | §2.1 ¶4 — not expanded |

---

## Chapter 3 — Methodology

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | **§3.1 Origin story** | Opens with paragraph naming Admmit's bachelor task offer, the team's own initiative in cold-contacting seven coordinators, HITL as Admmit mandate from project start (validated by interviews, not introduced by them). Reads as a story, not a specification. |
| [ ] | **§3.2 DSRM applied step-by-step** | Each of Peffers' six DSRM activities gets one bullet (2–4 sentences) naming what was actually done in this project. Format per `evaluation/reference-thesis-analysis.md` §11.5. |
| [ ] | **§3.5 Named iterations (4–6)** | Iterative Development Process contains at least four named iterations with descriptive titles. Each iteration follows: tried / why / what happened (positive AND limitations) / learned / next. Each carries an inline origin label per §12.0.5 (interview-driven / Admmit mandate / designer-technical). |
| [ ] | **§3.6 Evaluation Framework** | Separate from §3.7 Validity. Describes how the artefact is tested. Multi-engine benchmark explicitly framed as a "How-not-Of" test per §12.0.5. |
| [ ] | DSR choice is justified — not just stated | Why DSR and not case study? Why not pure quantitative? |
| [ ] | Interview process documented precisely enough to reproduce | Who, when, how many, how long, what questions, how transcribed |
| [ ] | Thematic analysis method described with citation | Braun & Clarke (2006) |
| [ ] | Validation vs evaluation distinction made explicit | Wieringa (2014) — we validate, not evaluate |
| [ ] | Malterud's four criteria addressed | Systematic reflection, relevance, validity, reflexivity |
| [ ] | Researcher bias acknowledged and mitigated | Dev team = research team + author affiliation with Admmit → confirmation bias risk |
| [ ] | Ethical considerations documented precisely | Consent, anonymisation/company naming, data storage, transcription-tool handling, Sikt/NSD status |
| [ ] | Limitations stated honestly — not buried | Sample size, no production deployment, single-day interviews |

---

## Chapter 4 — Findings

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | **Category split** | Findings split by category — empirical interview synthesis / artefact (system + algorithm) / process documentation. No interpretation in any of them. |
| [ ] | **DSR Artifacts mapping table** | Dedicated sub-section with table mapping each project artefact to its DSR category (Construct / Model / Method / Instantiation). |
| [ ] | **§4.5 multi-engine "How-not-Of" framing** | First paragraph of §4.5 explicitly frames the multi-engine benchmark as a methodologically independent test of *how* the constraint problem is best solved, not *whether* the artefact's claims about utilization are real (per §12.0.5). |
| [ ] | **Visibility-gap finding present in §4.1** | Resource-utilization visibility gap is named as an empirical theme, with operator-vs-owner asymmetry as a secondary finding. |
| [ ] | **§4.7 Process Documentation** | Sprint log summary, key decisions, time tracking — present in body (not appendix) per ChatSSB pattern. |
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
| [ ] | **§5.1 anchor-organised primary findings** | Three sub-sections, one per locked anchor: 5.1.1 Efficiency, 5.1.2 Trust/control, 5.1.3 Adaptability. Anchor names verbatim — no synonyms. Each sub-section has a `MUST ANCHOR` marker tied to exactly one anchor. |
| [ ] | **§5.1.1 includes operator-vs-owner asymmetry** | Bainbridge framing applied here — visibility gap is the manifestation of asymmetry (owners demand, coordinators don't articulate). Not a standalone section. |
| [ ] | **§5.1.2 three-layer HITL applied** | Bainbridge frames operator authority over override; Hoff & Bashir for trust calibration over use; Miller for explanation/transparency. Tacit-knowledge content absorbed here. |
| [ ] | **§5.4 hierarchical limitations (L1–L12)** | Three named sub-subsections: 5.4.1 Empirical Foundation (L1, L2, L3, L4), 5.4.2 Validation and Artefact (L5–L9), 5.4.3 Conceptual and Methodological (L10, L11, L12). Each L# is a named paragraph or `\paragraph{}`, not a buried sentence. **L#-to-SQ mapping at top of §5.4.** |
| [ ] | **L1–L12 each present and named** | Verify all twelve appear by name; none missing. Verify ordering matches §12.0.7. |
| [ ] | **§5.5 Deviations from Plan** | Explicit named section acknowledging plan-vs-reality differences. |
| [ ] | **§5.6 Methodology Reflection** | Self-critical paragraph naming an actual weak spot (small sample, synthetic-only validation, dev-team = research-team, or similar). Not a perfunctory acknowledgment. |
| [ ] | **Discusses, not just presents** — weighs multiple perspectives | Writing action level = "drøfte" — must argue, compare, evaluate |
| [ ] | Findings connected back to theory from Ch 2 | Resource scheduling / constraint programming theory → algorithm results. HITL theory → override design. |
| [ ] | Algorithm performance discussion is grounded in benchmark evidence | Ch 5.1.1 uses Ch 4.5 + `benchmark-results.md`, not unsupported performance claims |
| [ ] | Adoption barriers discussed honestly | Invoicing gap, trust, cost, training. Now in §5.2 Adoption and Deployment Implications. |
| [ ] | Sustainability section uses SusAF framework | §5.3 — 5 dimensions, 3 effect levels, effects table, SDG mapping |
| [ ] | Sustainability dilemmas discussed — not just positive effects | Efficiency vs deskilling, automation vs autonomy |
| [ ] | Ethical perspective included | Algorithmic fairness, accountability, privacy |
| [ ] | Validation framing used — not evaluation claims | "The validation suggests..." not "The system proves..." |

---

## Chapter 6 — Conclusion

| Check | What sensor looks for | How to verify |
|:-----:|----------------------|---------------|
| [ ] | **§6.2 SQ block-quote pattern** | Each sub-question reproduced verbatim as a single-line block quote, then answered in one discrete paragraph with no new material. Three SQs → three paragraphs. |
| [ ] | **Anchor-tied SQ answers** | Each SQ-answer paragraph carries a `MUST TRACE` to the originating Ch 5 sub-section AND names the anchor it serves. SQ1 → §5.1.1 Efficiency; SQ2 → §5.1.2 Trust/control; SQ3 → §5.1.3 Adaptability (and cross-anchor where relevant). |
| [ ] | **Limitation-grounded Future Work** | Each Future Work item cites a specific named limitation from §5.4 (e.g., "addresses L8 — no user testing with coordinators"). Generic items without limitation grounding flagged. |
| [ ] | **Closing domain claim** | Final sentence makes a claim about algorithm-assisted planning under stakeholder asymmetry in Norwegian transport — not just about the artefact. |
| [ ] | Main RQ answered directly — one clear paragraph | Verbatim question, then answer |
| [ ] | Mirrors the introduction — reader sees the full arc | Start broad in Ch 1, end broad in Ch 6 |
| [ ] | No new information introduced | Conclusion summarises and concludes, nothing new |
| [ ] | Contributions stated clearly | What does this thesis add? (artefact + knowledge) |
| [ ] | Tone is appropriately confident but not overstated | "The thesis demonstrates..." not "The thesis proves..." |

---

## Cross-Chapter Checks (run after all chapters are drafted)

- [ ] **Anchor traceability:** Each of the three locked anchors (Efficiency, Trust/control, Adaptability) appears verbatim in: §1.2 (defined), §5.1 (one sub-section per anchor), §6.2 (each SQ-answer names the anchor it serves). No synonyms anywhere.
- [ ] **Visibility-gap red thread:** The visibility-gap finding introduced in §1.1 is named again in §4.1 interview themes and synthesised in §5.1.1 Efficiency. Loop closed.
- [ ] **Operator-vs-owner asymmetry red thread:** The asymmetry framed in §1.1 (Bainbridge) reappears as a finding in §4.1, is interpreted in §5.1.1, and is named in §6.2 SQ1's answer.
- [ ] **L1–L12 forward references in Future Work:** Each item in §6.3 cites a specific L# from §5.4.
- [ ] **Red thread:** Does the argument flow logically from Ch 1 → 6? Does every chapter serve its spine sentence?
- [ ] **No orphaned theory:** Is every concept from Ch 2 referenced in Ch 4 or 5? Check `evaluation/theory-usage.md` for tracking.
- [ ] **Post-Ch 5 orphan check:** After Chapter 5, any theory still marked `planned` or unused in `evaluation/theory-usage.md` must be connected or removed.
- [ ] **No unsupported claims in Ch 5:** Is every discussion point grounded in a finding from Ch 4?
- [ ] **Consistent terminology:** Are the same terms used throughout? (Check glossary)
- [ ] **Citation balance:** Are there chapters with suspiciously few or many citations?
- [ ] **Scope adherence:** Does any chapter describe features not in `context/scope.md`?
- [ ] **Contribution clarity:** Can a reader tell what Mikael did vs. Embret vs. what the system does?
- [ ] **Proportionality:** Actual chapter word/page counts are within ±20% of outline targets, unless a clear reason is documented.
