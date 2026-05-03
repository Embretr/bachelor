# Workflow Improvement Log

> Claude proposes updates here after every writing session.
> Every entry requires explicit user approval before the workflow file is changed.
> This log is the record of how the system improves over time.

---

## 2026-05-03 — Five-fix bundle after §3.3 review (8 minor issues, 2 regressions of documented rules)

**Triggered by:** §3.3 round 1 surfaced 11 minor issues across both reviewers. Two were regressions of documented lessons-learned rules (term-drift line 120, bridges line 174), three were new generalisable patterns now promoted, six were section-specific. Root-cause analysis identified five workflow leaks.

**Status:** APPLIED 2026-05-03 (user instruction "ja fiks alle 5").

**Changes:**

1. **`.claude/skills/write-section/SKILL.md` Step 2 USER_MESSAGE template** — added a `SECTION-SPECIFIC CALIBRATION` block with hard caps (≤5 bullets, ≤300 words) and explicit "do not repeat writer.md / lessons-learned / rubric / BIB_SLICE rules" instruction. Reason: §3.3 brief had 9 CRITICAL CONSTRAINTS, ~4 of which were repetition of standing rules — competing for writer attention with section-specific calibration.

2. **`.claude/skills/write-section/SKILL.md` Step 4 length check** — added Chapter-3 calibration: silent-INFO band raised to ±50 % for §3.x sections, since the rubric "every methodological choice has a because" + the lessons-learned "decisions without rationale" check together inflate Ch 3 sections by 30–60 % over outline page-targets. Reason: §3.2 +30 %, §3.3 +65 % both produced length warnings that were flagged as "defensible" — the warning is structurally noise.

3. **`.claude/agents/section-coherence.md` + `.claude/agents/section-quality.md`** — added "Regression escalation rule (HARD)": findings within the agent's domain that match a documented `lessons-learned.md` rule (same chapter scope / source key / paragraph type / named pattern) escalate to `severity: critical, fixable: true` regardless of how minor the local instance feels. Triggers auto-revise instead of silently shipping. Reason: §3.3 shipped as `drafted-reviewed` despite repeating two documented rules.

4. **`evaluation/review/lessons-learned.md`** — added top-level Index (by chapter, by source key, by paragraph type) so writer/reviewer can scan applicable rules without reading the whole file. The "When to apply" prose per rule is preserved unchanged. Reason: lessons-learned grew to ~13 rules; topic-sorted format makes "what applies HERE" hard to extract.

5. **`.claude/agents/section-coherence.md` + `.claude/agents/section-quality.md`** — added explicit "Domain ownership" lists. Coherence owns terminology/bridges/structure/spine/evidence-markers/theory-tracker. Quality owns rubric/depth/source-integration/definition/technical-depth/naturalness/anchor-drift. Quality must NOT add structure findings to `issues[]` — only mention in `notes` for cross-validation. Reason: both reviewers flagged term-drift and bridges in §3.3, inflating issue count and creating dedup work.

**Why this improves output:**

- (1) keeps writer attention on section-specific calibration instead of repeating already-loaded rules.
- (2) eliminates structurally-expected length warnings that were noise, not signal.
- (3) regressions of documented rules now block ship, forcing one R2 polish pass instead of letting the pattern recur in future sections.
- (4) reduces lessons-learned scan time; rules stay enforceable without growing the file's read cost linearly.
- (5) eliminates duplicate minor flags between reviewers; cleaner harvest, faster decisions.

**Risk assessment:**

- (1) writer might miss legitimate section-specific guidance if orchestrator over-trims. Mitigation: the SKILL.md note allows up to 5 bullets when genuinely section-specific.
- (2) Ch 3 sections might genuinely overshoot by 70 %+; warning still fires above +50 %.
- (3) regression escalation may fire on borderline matches. Mitigation: rule body says "Exception: if the rule's 'When to apply' scope explicitly excludes this section, do not escalate."
- (4) index needs maintenance when rules are added/removed. Process note added to file header.
- (5) one structural issue might glip past coherence and not be re-flagged by quality. Mitigation: quality still mentions in `notes`, and the chapter-redthread agent will catch chapter-level structural drift later.

**Test:** next `/write-section` run will exercise all five changes. Re-run `/write-section 3.4` (next in writing order) to verify.

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

## 2026-05-02 — Proposal #6

**Triggered by:** Audit of which evaluation files each review agent loads showed `evaluation/theory-usage.md` was only consulted by `/review-chapter` (Ch 5+), not by `/write-section`. Orphan- and missing-theory drift would therefore only surface after every section in a chapter is `drafted-reviewed`, forcing late re-opens.
**Type:** updated rule / updated skill
**Applied changes to:** `.claude/skills/write-section/SKILL.md`

**Change:**
- Section coherence agent (Agent 1): for Ch 4, 5, 6 sections, read `evaluation/theory-usage.md` and run a "theory-tracker check" — every theoretical concept the section invokes must be tracked in the matrix; flag `theory_missing_from_tracker` for missing entries; list rows whose status should change from `planned` to `connected` for manual update.
- Added JSON fields `theory_missing_from_tracker` (counter) and `theory_tracker_updates` (list) to the coherence output schema.
- Updated coherence pass condition (both inline gate text and Step 6 gate parsing) to require `theory_missing_from_tracker == 0`.

**Why this improves output:**
Catches orphan/missing theory drift at section time instead of chapter time, removing one round of late revision when `/review-chapter 5` runs.

**Status:** ✅ Applied

---

## 2026-05-02 — Proposal #7

**Triggered by:** §2.1 round 1 token cost was ~300–400 k. Audit showed the orchestrator and three agents (writer + 2 reviewers) each loaded full `outline.md` (~53 kB), `a-grade-rubric.md` (~17 kB), `reference-thesis-analysis.md` (~61 kB), `references.bib` (~16 kB), and the orchestrator additionally loaded all 6 source notes (~163 kB) just to validate `wc -c ≥ 500` and the `Notes generated from raw` marker. Steps 1c and 4 also duplicated source-notes validation. None of these reads contributed to output quality.
**Type:** updated rule / updated skill
**Applied changes to:** `.claude/skills/write-section/SKILL.md`

**Change:**
- New **Step 1.5: PRECOMPUTE SLICES** — orchestrator extracts §X.Y plan, Chapter N rubric slice, §7 / per-chapter / cross-chapter ref-analysis slice, and per-key bib entries via `awk` once per pipeline run. The slices are pasted inline in writer + reviewer prompts.
- **Source-notes validation moved to Bash** in Step 1c (existence + `wc -c ≥ 500` + `grep -q "Notes generated from raw"`). The orchestrator no longer Reads the file content. Step 4 stops re-validating what Step 1c already validated; it only checks any new keys the writer introduced.
- Writer and both reviewer prompts now state "DO NOT READ THESE FULL FILES" for outline / rubric / ref-analysis / bib, with the slice provided inline. Source notes themselves are still read by writer/reviewer (necessary for cite faithfulness).
- Removed `source_requests` array from coherence and quality JSON gates.
- Removed all "Run extraction (see source-extractor.md)" / "user runs source-extractor" / "report as source request" prompts. The thesis-source set is locked (39 extracted notes); cite-related issues now resolve to "use a different existing key from BIB_SLICE" or "remove/weaken the claim".
- Deduplicated the two "Evidence readiness" blocks in Step 1c.
- Step 6 report dropped `SOURCE GATE` and `SOURCE NEEDS` lines.

**Why this improves output:**
Estimated 300–400 k tokens saved per `/write-section` run (≈50 % reduction) with zero quality impact — slices contain everything the agents actually used. Locking the source set also removes a class of false suggestions where reviewers proposed "add a new source" that would never be acted on.

**Status:** ✅ Applied

---

## 2026-05-02 — Proposal #8

**Triggered by:** User question — "når review agentene gir tilbakemelding, blir dette videreført slik at det brukes i videre skriving dersom aktuelt/det gjelder skriving generelt?" Audit revealed the lessons-learned loop existed (writer + both reviewers load `lessons-learned.md`) but the *capture* of new patterns was a soft ritual in `CLAUDE.md` post-task step 4 — easy to forget. A clean PASS-PASS section would jump to `STATUS.md` update without ever scanning `suggestions[]`, losing generalisable wisdom.
**Type:** new pipeline step / updated skill + ritual
**Applied changes to:** `.claude/skills/write-section/SKILL.md`, `CLAUDE.md`

**Change:**
- New **Step 6.6: LESSONS-LEARNED HARVEST** — mandatory step after every final round (whether `drafted-reviewed` or `drafted-needs-manual-fix`). Scans both reviewers' `issues[]` (severity: minor) + `suggestions[]` + `notes` / `weakest_aspect` / `fix`.
- **Deterministic GENERAL-vs-SECTION-SPECIFIC classifier** with 7 GENERAL triggers (names a source key/type, names a chapter or chapter-type, names a paragraph type, names a phrase to ban/prefer, names a structural pattern, cites the writing-action-level for a chapter-type, supervisor-style directive). When in doubt, classify GENERAL. Critical issues are *not* harvested (they were either auto-revised or escalated).
- **Hard prompt format**: prints the candidate with verbatim source quote + proposed `lessons-learned.md` entry (Rule / Why / When to apply / Source) + `Apply? (y / n / edit)`. Orchestrator waits per candidate; no batching, no auto-apply. `y` appends to `lessons-learned.md` under the closest existing heading; `n` logs decline reason in the round file; `edit` accepts user-revised text.
- Status update to `STATUS.md` happens **only after** every candidate has been answered.
- `CLAUDE.md` post-task ritual #4 rewritten to point at Step 6.6 (no more duplicate informal description that could drift).

**Why this improves output:**
Closes the feedback loop with mechanical guarantee. Every reviewer suggestion that has cross-section value now has a forced moment of human triage before the pipeline ends — turning a one-off review into a permanent rule that fires automatically on every subsequent `/write-section`. This compounds: each section's reviewers benefit from every prior section's harvested lessons, and the writer is never told the same thing twice.

**Status:** ✅ Applied

---

## Rejected Proposals

*(None yet)*

---

## Pending Proposals

*(None yet)*
