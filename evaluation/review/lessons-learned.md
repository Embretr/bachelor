# Lessons Learned — Patterns from Review Feedback

> **Writers and reviewers MUST read this file before drafting or judging a section.**
> Patterns here are extracted from past `/write-section` review rounds — they are recurring failure modes the pipeline already knows about. Repeating them in a new section is a regression.
>
> **How to add an entry:** When a reviewer flags an issue that is general (not a one-off, not section-specific), add a rule below. Keep entries short: one rule, one short reason, one application note. Source the rule by listing the section/round that produced it.
>
> **How to remove or revise an entry:** When a rule turns out to be wrong or outdated, strike it through and add a dated note. Do not delete history.
>
> Owner: Mikael. Review during the post-task ritual described in `CLAUDE.md`.

---

## Source faithfulness

### Don't decorate Pinedo's headline definition with adjectives the source did not use
- **Rule:** Cite Pinedo's scheduling definition without "limited" or other qualifiers. Pinedo p. 1: "allocation of resources to tasks". The "subject to constraints" clause is on p. 7 — pair both pages, or use phrasing that covers them.
- **Why:** Source notes for `pinedo2016scheduling` explicitly flag this as a paraphrase risk; decoration that compresses two source pages into one cite is a name-drop pattern.
- **When to apply:** Any cite of `pinedo2016scheduling` for the foundational scheduling definition (currently §2.1 ¶1, possibly §3.2, §4.5).
- **Source:** §2.1 round 1 coherence review (2026-05-01).

### Don't substitute engineering terms inside source attributions
- **Rule:** When citing a foundational source for an algorithmic concept, use the source's own vocabulary. Bridge to engineering terms separately if needed.
- **Why:** Mixing "greedy first-fit" inside a Pinedo cite implies Pinedo characterised the heuristic that way; he did not. His term is "dispatching rule / constructive heuristic — one job at a time according to a priority rule".
- **When to apply:** Any cite of `pinedo2016scheduling`, `glover1986future`, `burke2017late`, or other algorithmic primary sources.
- **Source:** §2.1 round 1 coherence review (2026-05-01).

### Pinedo covers multi-machine environments — say "single-resource", not "one-machine-per-job"
- **Rule:** When contrasting our multi-resource case with Pinedo's models, the accurate label is "single-resource" (one resource type per job). "One-machine-per-job" is wrong — Pinedo covers parallel machines, job shops, flow shops.
- **Why:** A factual mischaracterisation of a primary source.
- **When to apply:** Any §2.1, §3.2, §4.5 paragraph that contrasts our multi-resource extension against textbook scheduling.
- **Source:** §2.1 round 1 quality review (2026-05-01).

### Distinguish article/paper count from study/sample count when citing reviews
- **Rule:** When citing a systematic review or meta-analysis, separate the count of articles/papers reviewed from the count of studies/samples synthesised. "Reviewed 127 studies" is not interchangeable with "reviewed 127 articles" if the source's own framing distinguishes the two. Verify both numbers against the source notes file before paraphrasing.
- **Why:** Source notes for `hoff2015trust` flag this exactly: 101 articles contain 127 studies (p. 407). Collapsing the two counts into one reads to a careful sensor as if the writer paraphrased without checking what each number names. The same conflation risk applies to any review-style source.
- **When to apply:** Any Ch 2 or Ch 3 paragraph that cites a review or meta-analysis source for its empirical scope — particularly `hoff2015trust`, `braun2006thematic`, `malterud2001lancet`, `hevner2004design`.
- **Source:** §2.2 round 1 coherence + quality reviews (2026-05-02).

### Don't claim "literature on the domain" support that BIB_SLICE does not contain
- **Rule:** Phrases like "X recurs in the literature on the domain", "the literature on Norwegian TMS names X", "established in the literature as Y" assert a literature footing. They are only acceptable when an academic source in BIB_SLICE actually makes that claim. Project-context market facts (vendor names known from glossary, supervisor briefing, or interviews) are NOT academic literature even when they are common knowledge in the project. The fix is to frame as factual description: "Within the Norwegian market, the two commercial TMS named in this thesis's domain context are X and Y." Or anchor to the project's own context (Ch 1) via a forward/backward reference.
- **Why:** This is distinct from the chapter-purity rule (which forbids importing interview material into Ch 2 prose). The new failure mode is implying *literature* support for a claim whose actual provenance is project context. A sensor reading for source rigour will treat the literature-anchor language as a verifiable claim; if BIB_SLICE does not back it, the claim is unsupported.
- **When to apply:** Any prose that names live products, vendors, or systems where the named entities are NOT cited from an academic source in BIB_SLICE. Particularly §1.1 background, §2.3 TMS landscape, §4.3 fit/gap, §5.2 adoption.
- **Source:** §2.3 round 1 coherence review (2026-05-02).

### Don't extend a country-/period-bounded statistic to other countries or periods without a covering source
- **Rule:** A statistic from one geography or one period (e.g., a 2007 US 45-firm survey) does NOT license claims about other geographies (Europe, Norway) or about the present day. Soft comparators ("a pattern compatible with what the literature describes for Europe more generally", "consistent with contemporary practice", "similar to what is reported in the European context") smuggle a generalisation past the sourced statistic's actual scope and need their own source. The fix is either (a) cut the comparator clause and keep only what the cite supports, or (b) add the temporal/geographic qualifier inside the sentence containing the statistic ("fifty per cent of non-users in their 2007 North American sample") so the reader sees the scope at the point of use.
- **Why:** Source notes for `griffis2007tms` explicitly caveat that the 50 % figure is illustrative rather than current; using the figure with a soft European comparator silently overrides that caveat. The same risk applies to any country-/period-bounded statistic — Norwegian SSB figures projected backwards or forwards, US-survey adoption rates extrapolated to Europe, single-year benchmark figures presented as steady-state.
- **When to apply:** Any chapter that cites a country-/period-bounded statistic — Ch 1 background, Ch 2.3 TMS adoption, Ch 4 findings comparing to outside benchmarks, Ch 5 discussion of adoption / cost / fairness.
- **Source:** §2.3 round 1 coherence review (2026-05-02).

### Mark chain-of-attribution definitions with "adopt" or "cite", not "define"
- **Rule:** When source X cites a definition originally from source Y (e.g., Heinbach et al. 2022 cite Gartner's De Muynck et al. 2020 for the TMS definition), the verb `\textcite{X} define ...` mis-attributes original authorship. Use `\textcite{X} adopt a definition of ... as ...` or `\textcite{X} cite a definition of ... as ...`. The cite remains on X (per BIB_SLICE, since Y may not be in our bib), but the prose is honest about provenance. Read the source notes' "Forbehold" / "Application" sections before paraphrasing — chain-of-attribution cases are flagged there explicitly.
- **Why:** Source notes for `heinbach2022datadriven` flag this exact transparency point. A sensor reading for source rigour will spot "X define Y" when X is in fact citing Y from Z, and treat it as a misattribution. The fix is a one-word verb change.
- **When to apply:** Any cite where the source notes file flags the cited claim as a quote-or-paraphrase-from-another-source. Currently affects `heinbach2022datadriven` (TMS definition from Gartner / De Muynck et al. 2020) and any other Ch 2 cite where the source notes' "Forbehold" section names a chain.
- **Source:** §2.3 round 1 coherence review (2026-05-02).

### When citing Peffers' six DSRM activities by name, use the source's wording verbatim
- **Rule:** Peffers et al. (2007, p. 46) name the six DSRM activities: (1) problem identification and motivation; (2) **objectives for a solution** (or the longer "definition of the objectives for a solution" — preposition "for", not "of"); (3) design and development; (4) demonstration; (5) evaluation; (6) communication. Do not compress the second activity to "objectives of a solution" — the preposition shift reframes the activity from "deriving objectives from the problem" to "objectives as a static category". Where the six are recited as a list, use the verbatim names; where activity (2) is named alone, the compact "objectives for a solution" is the canonical form.
- **Why:** §2.4 round 1 flagged this exact compression. The six-activity recital reappears as "DSRM Applied" bullets in §3.2 and as named activities in §3.6; terminology consistency across §2.4 → §3.2 → §3.6 is part of the spine. Source notes for `peffers2007dsrm` quote the abstract verbatim and should be the reference at write-time.
- **When to apply:** Any paragraph that names one or more of the Peffers DSRM activities — primarily §2.4 ¶1, §3.2 ¶2 + DSRM Applied bullets, §3.6, and any Ch 6 paragraph that traces back to a specific DSRM step.
- **Source:** §2.4 round 1 coherence review (2026-05-02).

---

## Chapter purity

### Theory chapters (Ch 2) must be source-anchored, not interview-grounded
- **Rule:** Do not write "the interviews indicate..." or any equivalent in Ch 2 prose. Frame utilization, trust, adoption, etc. from the literature in Ch 2; reserve interview-validated versions for Ch 4 (Findings) and Ch 5.1.x (Discussion under the relevant anchor).
- **Why:** Ch 2's role is theoretical scaffolding. Importing primary data into Ch 2 collapses the structure the thesis needs in Ch 4 and Ch 5; the same claim then has nothing fresh to say where the spine demands it.
- **When to apply:** Any Ch 2 section. The `MUST EVIDENCE: interview-derived ...` markers belong in Ch 4 outline, never in Ch 2 outline.
- **Source:** §2.1 round 1 quality review (2026-05-01); re-confirmed by supervisor 2026-05-02 (logged in `context/docs/project/supervisor-feedback.md`).

---

## Narrative framing

### Lead theory paragraphs with the human actor, not end with them
- **Rule:** In Ch 2 theory sections, introduce the human role (trafikkoordinator for scheduling, operator for HITL, planner for TMS) in the FIRST sentence of the relevant section. Do not place the actor as the last sentence of ¶1 — that reads as an AI "reveal-as-punchline".
- **Why:** Supervisor 2026-04-28 directive: theory follows the actor; the actor does not emerge from the theory. This is also captured in `writer.md` "Narrative framing comes early" but reviewers continue to find it violated when the writer leans on a textbook hook before introducing the actor.
- **When to apply:** Every Ch 2 section, plus any other section where a human role anchors the abstract content.
- **Source:** Supervisor 2026-04-28 (recorded in user memory `project_narrative_dispatcher_early.md`); §2.1 round 1 quality review (2026-05-01) confirmed it as a recurring temptation.

---

## Empirical scope

### Don't generalize from the interview sample to "the industry"
- **Rule:** Claims about Norwegian transport, transporters, or "the industry" must respect the empirical scope: 7 interviews, varied TMS adoption, varied company size. Never write "all transporters have a TMS", "Norwegian transport companies do X", or any sweeping universal. Use "several of the interviewed companies", "the interviewed sample", or — when leaving the empirical voice — "the literature reports". When a source is unclear, weaken the claim rather than strengthen it.
- **Why:** Supervisor 2026-05-02: "Ikke alle har en TMS, generelt: vær forsiktig med å påstå ting." Overstating the empirical reach is the easiest way to lose credibility with a sensor — and several interviewed companies in fact do not run a TMS.
- **When to apply:** Any chapter that touches Norwegian transport context — Ch 1 framing, Ch 2.3/2.4 (TMS coverage and adoption), Ch 4.1, Ch 4.3 fit/gap, Ch 5 discussion.
- **Source:** Supervisor 2026-05-02 (logged in `context/docs/project/supervisor-feedback.md`).

---

## Coverage

### Name existing solutions explicitly when describing a problem space
- **Rule:** When a section frames a problem domain (TMS, scheduling tools, planning interfaces, decision-support systems), name the live state-of-the-art — actual products, vendors, or systems — and what they cover. Implying state-of-the-art only through gap-talk is insufficient: the reader cannot judge a gap they cannot locate against a baseline. For Norwegian TMS the named systems are Timpex and Opter; pair with international vendors documented in the literature where relevant.
- **Why:** Supervisor 2026-05-02: "Allerede eksisterende løsninger må nevnes." A theory or background section that does not anchor to the live market reads as if it floats above reality.
- **When to apply:** Ch 2 background paragraphs that introduce a tool category; Ch 4.3 fit/gap; Ch 5.2 adoption discussion.
- **Source:** Supervisor 2026-05-02 (logged in `context/docs/project/supervisor-feedback.md`).

---

## Terminology

### A definition stated in ¶1 must be used the same way in ¶2 and onwards
- **Rule:** When a section opens with a definition (TMS as comprehensive operational solution, automation as full delegation, scheduling as resource-to-task allocation, etc.), every subsequent paragraph must use the same scope. If a narrower or broader sense is needed, mark the shift explicitly ("In the operational sense of the term, ...") and revert before the section ends. Do not let the second paragraph quietly redefine what the first established.
- **Why:** Supervisor 2026-05-02: "Første definisjon av tms er omfattende løsning, andre paragraf virker det som en begrenset definisjon: Definisjoner må konsekvent brukes likt." Implicit redefinition mid-section is a frequent reason a sensor flags "the argument drifts".
- **When to apply:** Any section that opens with a definitional paragraph — most Ch 2 sections, Ch 3 method definitions, Ch 4 system descriptions, Ch 5 discussion of contested terms.
- **Source:** Supervisor 2026-05-02 (logged in `context/docs/project/supervisor-feedback.md`).

### Pick one form of a role/actor term per section and apply it consistently
- **Rule:** Within a single section, use one English form of an actor or role term throughout (e.g. "traffic coordinator", "operator", "planner"). The Norwegian original may appear once on first mention as a parenthetical or italicised gloss ("the traffic coordinator (\textit{trafikkoordinator})"); after that, the chosen form is final until the section ends. Do not silently switch between Norwegian and English, abbreviated and full, or a generic role and a project-specific role mid-section.
- **Why:** Even single-instance mixing reads as inconsistency to a careful reviewer and to a sensor reading for terminology rigour. `writer.md` already mandates one term per concept; reviewers continue to find single-instance lapses, especially when the Norwegian original is mentally available to the writer.
- **When to apply:** Every section in every chapter. Particularly Ch 2 theory sections (where the project actor crosses with theory's generic "operator"), Ch 3 method sections (interviewer / coordinator / informant), Ch 4 findings (driver / employee / sjåfør).
- **Source:** §2.2 round 1 coherence review (2026-05-02).

### Parenthesise the abbreviation on first mention of a multi-word concept
- **Rule:** The first time a multi-word concept that will later be abbreviated appears in prose, write it with the abbreviation in parentheses: "Design Science Research Methodology (DSRM)", "Transport Management System (TMS)", "Constraint Programming SAT (CP-SAT)". Subsequent uses may take the abbreviation alone. Do not introduce the abbreviation only at second use — it lands cold for a reader following the section linearly. This applies to concept-level abbreviations, alongside the existing actor-term-form rule.
- **Why:** §2.4 round 1 ¶4 used "DSRM" without "(DSRM)" being attached to the first mention of "Design Science Research Methodology" in ¶1, forcing readers to reconstruct the link. Cold-reader legibility is a sensor-grade criterion; abbreviations are cheap to introduce correctly and expensive to chase down later.
- **When to apply:** Any chapter. Especially Ch 2 (DSR / DSRM, HITL, TMS, VRP, CP-SAT), Ch 3 (DSRM activities, MoSCoW), Ch 4 (system component abbreviations), Ch 5 (UTAUT, SusAF). For concepts that already have a glossary entry with an established abbreviation, prefer the glossary form on first mention in prose.
- **Source:** §2.4 round 1 coherence review (2026-05-02).

---

## Reader accessibility

### Gloss in-house jargon on first use, or pick plainer phrasing
- **Rule:** Internal vocabulary — "fit/gap", "anchor concept", "spine", "outline marker", "MUST CITE", and similar workflow terms — is not legible to a cold sensor. On first use in prose, gloss the term in one short clause ("the fit/gap analysis — what existing systems cover and what they do not — ...") or replace with plainer phrasing. The supervisor's preferred fix for fit/gap specifically is a table contrasting "what exists" against "what is missing"; plain prose may use that same framing.
- **Why:** Supervisor 2026-05-02: "Istedenfor fit gap, som ikke alle vet hva er og kan bli uklart: Feks tabell. Hva finnes det og hva mangler." Internal terminology is fine in planning files but lands as opaque to sensors and external readers.
- **When to apply:** Any prose section, especially Ch 2 background, Ch 4.3 fit/gap, Ch 5 discussion. The internal labels remain free to use in `fitgap-summary.md`, `outline.md`, and other planning artefacts.
- **Source:** Supervisor 2026-05-02 (logged in `context/docs/project/supervisor-feedback.md`).

---

## Flow

### Bridge between paragraphs — no abrupt topic jumps
- **Rule:** Each new paragraph must open with a bridge that names what the previous paragraph established and what this one adds (a contrast, a refinement, a consequence, a counterexample, a delimitation). Topic-switching mid-section without a bridge sentence reads as if the section were assembled from disjoint notes. The bridge sentence is one sentence, not a paragraph; it carries the joint, then the new paragraph develops the new claim normally.
- **Why:** Supervisor 2026-05-02: "Brå overgang mellom avsnitt: bør være bedre overganger." The lack of bridges is also a visible AI-tell in long-form academic prose and a frequent reason sensors mark "argument is hard to follow".
- **When to apply:** Every section longer than two paragraphs, every chapter.
- **Source:** Supervisor 2026-05-02 (logged in `context/docs/project/supervisor-feedback.md`).

---

## Structure

### Name the taxonomy explicitly in the orientation sentence, even when it is implied
- **Rule:** For paragraphs that enumerate items (constraint types, solver families, automation levels, requirement categories), state the list in the FIRST sentence. Do not assume the body's per-item sentences imply the taxonomy.
- **Why:** Orientation-before-detail is non-negotiable for technical readers; reviewers read for the explicit signpost.
- **Example:** "Three solver families are commonly applied: constructive heuristics, constraint programming, and metaheuristics. Each occupies a different point on the speed-quality tradeoff." — not "Three solver families are commonly applied to such problems and are revisited later".
- **When to apply:** Any enumerative paragraph in any chapter.
- **Source:** §2.1 round 1 quality review (2026-05-01).

### Close theory paragraphs with an explicit forward handoff to where the concept is re-applied
- **Rule:** Each Ch 2 paragraph that introduces a theoretical concept the spine relies on later (HITL layers, trust antecedents, explanation requirement, DSR cycles, etc.) should close with one explicit handoff sentence to the chapter and section where the concept is re-applied — for example "Chapter 5 returns to this in §5.1.2" or "Chapter 4's findings extend this to the Norwegian sample". Not every paragraph needs it; only those whose concept must be visibly threaded for spine traceability.
- **Why:** Cross-chapter A-marker 8 (`reference-thesis-analysis.md`) requires backward references in Ch 5/6 to close loops opened in Ch 1/2. Forward handoffs at concept-introduction time make those loops legible to reviewers without forcing a chapter-wide search. §2.2 ¶2 ("Bainbridge's argument is theoretical here; the empirical extension to Norwegian transport belongs in Chapter 4") and ¶5 ("Chapter 5 returns to this adoption question") show the pattern; ¶3 and ¶4 omitted it and the spine traceability cost was paid at review time.
- **When to apply:** Any Ch 2 paragraph that introduces a theory-anchor concept; selected Ch 3 paragraphs that introduce a methodological choice re-applied in Ch 5 (`MUST TRACE`-style spine load).
- **Source:** §2.2 round 1 coherence review (2026-05-02).

---

## How writers should use this file

1. Read every entry above before drafting.
2. For each rule that names a section type, chapter, or source key relevant to the section being written, treat it as a hard constraint.
3. After writing, do a self-check pass: walk every rule, confirm the draft honours it, fix any drift before returning.

## How reviewers should use this file

1. Read every entry above before judging.
2. Treat each rule as part of the deterministic check set: if the section violates a rule, that violation MUST appear in the JSON gate's `issues[]` (severity `minor` or `critical` depending on whether the chapter purity / spine alignment is at stake).
3. If the review surfaces a NEW recurring pattern not in this file, propose adding it to lessons-learned in the JSON `suggestions[]` array with the exact rule + reason + when-to-apply text — the orchestrator can then add it during the post-task ritual.