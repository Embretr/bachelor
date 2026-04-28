# Workflow Improvement Log

> Claude proposes updates here after every writing session.
> Every entry requires explicit user approval before the workflow file is changed.
> This log is the record of how the system improves over time.

---

## How This Works

After every task, Claude:
1. Rates the quality of what it just produced relative to the rest of the thesis
2. Identifies any friction — missing context, unclear instructions, missing evaluation criteria
3. Proposes a concrete workflow improvement if one is warranted
4. Writes the proposal here in the format below
5. Asks: "Apply this update? (y/n)"

If the user says yes, Claude edits the relevant file immediately.
If the user says no, the proposal is logged here as rejected with a note.

---

## Proposal Format

```markdown
## [DATE] — Proposal #[N]

**Triggered by:** [what happened in the session that wasn't smooth]
**Type:** [new rule / updated rule / new context file / updated index / other]
**Proposed change to:** [CLAUDE.md / .claude/agents/X.md / context/index.md / evaluation/X.md]

**Change:**
[exact text to add, remove, or modify — be specific]

**Why this improves output:**
[one sentence — what problem this solves]

**Status:** ⬜ Pending / ✅ Applied / ❌ Rejected
**Reason (if rejected):** [user's reason]
```

---

## Applied Improvements

## 2026-04-14 — Proposal #1

**Triggered by:** Pre-writing review found that the existing pipeline could start writing even when section-specific evidence, benchmark data, ethics details, or concrete citation readiness were missing.
**Type:** updated rule / updated outline / updated context index / updated evaluation
**Applied changes to:** `.claude/skills/write-section/SKILL.md`, `.claude/skills/review-chapter/SKILL.md`, `context/outline.md`, `context/index.md`, `STATUS.md`, `evaluation/evaluation.md`

**Change:**
Added a section readiness gate for `/write-section`, benchmark and ethics blockers, Chapter 6 paragraph-level planning, stricter Ch 5/Ch 6 anchors, chapter proportionality checks, and post-Chapter-5 theory usage checks.

**Why this improves output:**
It prevents generic or unsupported thesis sections by stopping the writing pipeline before missing evidence can be written around.

**Status:** ✅ Applied

---

## 2026-04-14 — Proposal #2

**Triggered by:** Supervisor feedback that the thesis language should be simpler, more direct, less advanced, and avoid vague adverbs such as "widely used".
**Type:** updated rule
**Applied changes to:** `context/docs/method/academic-writing-guide.md`

**Change:**
Added a language rule requiring direct student-level English, fewer unnecessary adverbs, and specific scope instead of phrases such as "widely used".

**Why this improves output:**
It makes future sections match the supervisor's language expectations before they are written.

**Status:** ✅ Applied

---

## 2026-04-23 — Proposal #4

**Triggered by:** Supervisor meeting on Ch 2 (resource scheduling) exposed recurring failures the existing agents did not catch: paragraphs that mixed unrelated concepts (multi-resource + single-resource + valid driver, NP-hard + heuristics), definitions given before examples instead of after, invented or decorated definitions ("limited resources") not grounded in sources, terminology drift (driver vs employee), concepts used before introduction (VRP), decisions described without rationale, and broad source dumps rather than selective use.
**Type:** updated rule / updated agents / updated evaluation
**Applied changes to:** `.claude/agents/writer.md`, `.claude/agents/naturalness.md`, `.claude/agents/red-thread.md`, `.claude/agents/quality.md`, `.claude/skills/write-section/SKILL.md`, `.claude/skills/review-chapter/SKILL.md`, `evaluation/evaluation.md`

**Change:**
- writer.md: added a "Structure and paragraph discipline" block covering one-idea-per-paragraph, orientation-before-detail (tables/taxonomy first), broad→specific ordering, narrative framing early, sourced definitions, simple vocabulary, robot-prompt precision, glossary-locked terminology, explicit paragraph bridges, decisions-with-rationale, technical depth, selective source use, interview integration, and concept-before-use.
- naturalness.md: added patterns 11–17 (mixed-topic paragraph, definition-before-hook, invented/decorated definitions, missing transitions, terminology drift, concept-before-introduction, description-without-rationale).
- red-thread.md: added sections 5–9 covering concept placement, paragraph discipline and ordering, terminology/transitions, decisions without rationale, and source selectivity.
- quality.md: added checks for definition quality, paragraph discipline, orientation-before-detail, terminology consistency, transitions, decisions+rationale, technical depth, source selectivity, and reader precision.
- write-section SKILL coherence agent: added structure/ordering questions (7–14, 17) and a `structure_issues` JSON block with gating fields.
- review-chapter red-thread agent: added chapter-level concept placement, terminology consistency across sections, and ordering across sections.
- evaluation.md: added a "Writing discipline (sensor-visible signals)" table under All Chapters with 12 rows.

**Why this improves output:**
The rewrite of Ch 2 and future chapters will fail the same way unless the pipeline enforces these structural rules at both write-time and review-time. The new rules make the failures explicit so the writer avoids them and the reviewers flag them.

**Status:** ✅ Applied

---

## 2026-04-28 — Proposal #5

**Triggered by:** Supervisor meeting (2026-04-28) on the first draft of Ch 2.1 (Resource Scheduling). The meeting surfaced refinements that the existing rules from Proposal #4 had not made sharp enough: definitions still padded rather than trimmed to a short direct core; sources still cited generically without checking actual relevance to the surrounding claim; the trafikkoordinator buried at the end of theory sections instead of grounding the reader from the start; multi-resource, single-resource, and valid-driver collapsed into one paragraph rather than progressing one concept layer at a time; an opening that jumped to abstract definition with no story or human anchor; "employee" and "driver" mixing in the same paragraph; sources used as buckets rather than tools (extracting only the relevant slice).
**Type:** updated rule / updated agents / updated template
**Applied changes to:** `.claude/agents/writer.md`, `.claude/agents/source-extractor.md`, `.claude/agents/red-thread.md`, `.claude/agents/quality.md`, `.claude/agents/naturalness.md`, `context/docs/method/sources/_template.md`

**Change:**
- writer.md — strengthened six rules in "Structure and paragraph discipline":
  - "Paragraph = one idea (a paragraph is an info box)" — added the info-box framing and three canonical anti-examples that must each be split into separate paragraphs.
  - "Order: orientation before detail" — added "never narrow → wide" and an explicit "concept progression — one layer per paragraph" rule (simpler textbook case → general definition → our case → specific constraints), referencing the supervisor's flag of the diffuse 2.1 draft.
  - "Narrative framing comes early" — added "know the story before you write" and an explicit "trafikkoordinator (or equivalent human actor) appears early, not late" rule for Ch 2 theory sections.
  - "Definitions: short, direct, correct" — added "trim to the core" sub-rule and the replicability test.
  - "Terminology consistency" — added the "reader must never speculate" framing with concrete drift examples (employee/driver, machine/resource/vehicle, planner/dispatcher/trafikkoordinator) and a source-vocabulary translation rule.
  - "Use sources selectively" — added that a listed source may not be relevant and force-fitting is worse than `[CITATION NEEDED]`.
- source-extractor.md — Step 6 Definisjoner: extract the short core sentence verbatim, not surrounding elaboration; writer agent uses the table as drop-ins.
- _template.md — added a one-line guidance above the Definisjoner table mirroring the source-extractor rule.
- red-thread.md — section 6 (PARAGRAPH DISCIPLINE AND ORDERING) extended with an actor-placement check and a concept-progression check.
- quality.md — "Orientation before detail" extended with actor-placement and concept-progression checks; "Definition quality" extended with a trim-to-core criterion; "Source selectivity" extended with a force-fit flag.
- naturalness.md — added patterns 18 (actor introduced too late), 19 (concept-stuffed paragraph), 20 (padded definition).

**Why this improves output:**
The first 2.1 draft showed that Proposal #4's rules existed but were not sharp enough at the points the supervisor most cared about. These refinements make the failures explicit: the writer cannot bury the actor late, cannot pad a definition, cannot collapse concept layers, and cannot force-fit a citation; the reviewers will flag each of these by name.

**Status:** ✅ Applied

---

## 2026-04-14 — Proposal #3

**Triggered by:** User requested a controlled source workflow that separates source discovery and agent assessment from human approval and thesis citation use.
**Type:** new context file / updated rule / updated evaluation
**Applied changes to:** `evaluation/source-requests.md`, `context/docs/method/literature-list.md`, `.claude/skills/write-section/SKILL.md`, `.claude/skills/review-chapter/SKILL.md`, `evaluation/evaluation.md`, `context/index.md`, `STATUS.md`

**Change:**
Added a source request queue, converted the literature list into a controlled source register, required `approved-read` status plus BibTeX presence before citation, and added section/chapter source audits for unsupported claims, source fit, citation balance, orphan sources, and unapproved sources.

**Why this improves output:**
It prevents unsupported or merely suggested sources from entering thesis prose while preserving a clear queue for finding, reviewing, and approving needed literature.

**Status:** ✅ Applied

---

## Rejected Proposals

*(None yet)*

---

## Pending Proposals

*(None yet)*
