# Lessons Learned — Patterns from Review Feedback

> **Writers and reviewers MUST read this file before drafting or judging a section.**
> Patterns here are extracted from past `/write-section` review rounds — they are recurring failure modes the pipeline already knows about. Repeating them in a new section is a regression.
>
> **How to add an entry:** When a reviewer flags an issue that is general (not a one-off, not section-specific), add a rule below. Keep entries short: one rule, one short reason, one application note. Source the rule by listing the section/round that produced it. After adding the rule body, also add it to the index below under the relevant chapter/section scopes.
>
> **How to remove or revise an entry:** When a rule turns out to be wrong or outdated, strike it through and add a dated note. Do not delete history. Remove the entry from the index too.
>
> Owner: Mikael. Review during the post-task ritual described in `CLAUDE.md`.

---

## Index — which rules apply to which sections

Use this to find the rules that touch the section you are writing or reviewing. Read the full rule body in the section below before drafting/judging. The same rule may appear under several scopes.

**By chapter:**

- **Ch 1 (Introduction):** Empirical scope — interview-sample generalisation • Reader accessibility — gloss in-house jargon, parenthesise abbreviations, no false-appendix references • Terminology — actor-term consistency • Coverage — name existing solutions when framing a problem space.
- **Ch 2 (Theory):** Source faithfulness — Pinedo decoration, Pinedo single-resource label, Pinedo engineering-term substitution, review article/study count, literature-anchor language, country-/period-bounded statistics, chain-of-attribution definitions, Peffers DSRM activity names verbatim, polarity preservation in source paraphrase • Chapter purity — no interview material in Ch 2 • Narrative framing — actor early, not as punchline • Coverage — name existing solutions • Terminology — definition consistency, actor-term consistency, parenthesise abbreviations, cross-chapter terminology lock • Structure — name taxonomy explicitly, close theory paragraphs with forward handoff • Reader accessibility — gloss in-house jargon, no false-appendix references.
- **Ch 3 (Methodology):** Source faithfulness — Peffers DSRM activity names verbatim, defer to Ch 2 cite via cross-reference, L#-binding scope, because-clause matches actual cause, framework-as-organiser needs because, polarity preservation in source paraphrase • Terminology — definition consistency, actor-term consistency, parenthesise abbreviations, cross-chapter terminology lock, anchor-binding verbs (Sub-clauses A + B), guide-topics-vs-TA-themes distinction • Empirical scope — interview-sample generalisation • Flow — bridges between paragraphs • Structure — close theory/method paragraphs with forward handoff (selected paragraphs) • Reader accessibility — no false-appendix references, gloss in-house jargon (§3.7).
- **Ch 4 (Findings):** Source faithfulness — review article/study count (when synthesising), L#-binding scope • Empirical scope — interview-sample generalisation • Terminology — actor-term consistency, definition consistency, guide-topics-vs-TA-themes distinction (§4.1) • Flow — bridges between paragraphs • Reader accessibility — no false-appendix references (§4.1–§4.4) • Coverage — name existing solutions (§4.3 fit/gap).
- **Ch 5 (Discussion):** Source faithfulness — defer to Ch 2 cite, L#-binding scope, because-clause matches actual cause, framework-as-organiser needs because (§5.1.2, §5.5), country-/period-bounded statistics, literature-anchor language, polarity preservation in source paraphrase • Terminology — anchor-binding verbs (Sub-clauses A + B), cross-chapter terminology lock, actor-term consistency • Empirical scope — interview-sample generalisation • Flow — bridges between paragraphs • Coverage — name existing solutions (§5.2 adoption) • Reader accessibility — gloss in-house jargon (§5.2, §5.3, §5.5, §5.6).
- **Ch 6 (Conclusion):** Source faithfulness — defer to Ch 2 cite (TRACE rather than re-cite), L#-binding scope, because-clause matches actual cause • Terminology — anchor-binding verbs, cross-chapter terminology lock • Empirical scope — interview-sample generalisation • Reader accessibility — no em dashes.

**By source key (cite-rule applicability):**

- `pinedo2016scheduling` → Pinedo decoration, single-resource label, engineering-term substitution.
- `hoff2015trust` → review article/study count, polarity preservation in paraphrase.
- `braun2006thematic` → review article/study count, framework-as-organiser needs because (§3.4).
- `malterud2001lancet` → review article/study count, three-criteria-not-four, framework-as-organiser needs because (§3.7), polarity preservation in paraphrase (p. 484 preconceptions/bias, p. 486 transferability).
- `hevner2004design` → review article/study count, defer to Ch 2 cite.
- `hevner2007threecycle` → polarity preservation in paraphrase (lab-before-field default).
- `peffers2007dsrm` → DSRM activity names verbatim, defer to Ch 2 cite.
- `bainbridge1983ironies` → polarity preservation in paraphrase (operator-vs-owner default).
- `heinbach2022datadriven` → chain-of-attribution definitions.
- `griffis2007tms` → country-/period-bounded statistics.
- Bainbridge / Hoff & Bashir / Miller / Lee / Wieringa / Orlikowski → defer to Ch 2 cite.

**By paragraph type (any chapter):**

- **Definitional opening paragraphs** → definition consistency, anchor-binding verbs.
- **Qualitative-method / findings paragraphs (any section that touches TA outputs)** → distinguish interview-guide topics from TA analytic-output themes.
- **Enumerative paragraphs** → name taxonomy explicitly in orientation sentence.
- **Theory-introduction paragraphs (Ch 2 + Ch 3)** → close with forward handoff, lead with human actor.
- **Decision/rationale paragraphs (Ch 3 + Ch 5)** → because-clause matches actual cause, anchor-binding verbs (Sub-clause B).
- **Framework-as-organiser opening paragraphs** → framework choice itself needs a one-clause because.
- **Cite paraphrase paragraphs** → don't decorate the source, don't substitute engineering terms, distinguish article/study count, chain-of-attribution, preserve source's default-vs-exception polarity.
- **Limitation-binding paragraphs (any section forwarding to L#)** → L#-binding scope must cover.
- **Artefact-location paragraphs (interview guide, table, matrix)** → no false-appendix references.
- **Any paragraph, any section** → no em dashes (`---`, `—`) ever; replace with commas, parentheses, colons, semicolons, or a sentence break.

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

### Defer to a Ch 2 cite via cross-reference rather than re-citing the same primary-source pages downstream
- **Rule:** If §2.x has already cited Orlikowski p. 5 (paradigm comparison), Hevner p. 82 (DSR foundation), Wieringa (validate-vs-evaluate), Bainbridge (operator-vs-owner), Hoff & Bashir (trust antecedents), Miller (explanation as interface), Lee (trust foundation), or any other primary source for a claim, downstream sections (§3.2, §3.6, §3.7, §5.1.x, §6.2) reference §2.x via `\Cref{sec:...}` rather than re-citing the same primary-source pages. The downstream section's value-add is the project-specific application of the cited concept, not the citation itself. Where a downstream section needs a different page or a different aspect of the same source, the cite is fine; where it would only restate the §2.x claim, defer.
- **Why:** §3.2 round 1 reproduced §2.4 ¶2's paradigm comparison nearly verbatim with two identical Orlikowski p. 5 citations and the same Hevner p. 82 framing. Re-citing the same primary-source pages in two adjacent chapters reads as not having decided where the argument lives. The fix compressed §3.2 ¶1 from six sentences to four and dropped the duplicate Orlikowski cites; the IS-paradigm-comparison MUST CITE marker is satisfied by the `\Cref{sec:dsr}` cross-reference (the marker requires the source TYPE be present in the thesis, not in every chapter that references it).
- **When to apply:** §3.2 ¶1 (DSR + paradigm reminder — defer Orlikowski + half of Hevner to §2.4), §3.6 ¶1 (validation-vs-evaluation — defer Wieringa to §2.4 ¶3), §3.7 (Wieringa already deferred per outline), §5.1.1 ¶2 (Bainbridge — re-cite is acceptable here because §5.1.1 is the discussion's primary anchor for Bainbridge; this rule does not block primary discussion cites), §5.1.2 ¶1–¶3 (Bainbridge / Hoff & Bashir / Miller / Lee — re-cite acceptable for the same reason), §6.2 (RQ-answer paragraphs should TRACE rather than re-cite).
- **Source:** §3.2 round 1 coherence review (2026-05-03).

### When forwarding a finding to a named L# limitation, the L#'s defined scope must cover what is forwarded
- **Rule:** Many methods/findings paragraphs end with `... named as L# in \Cref{sec:limitations}`. Each L# at §5.4 has a fixed defining scope (e.g. L1 = "Sample size and brief duration", L2 = "Self-selection bias in interview sample (Admmit customers only)", L3 = "Researcher–developer overlap and informal study procedures", L8 = "No user testing with coordinators"). Before binding a new finding to L#, verify the L# definition actually covers the new case. If it does not, choose one of: (a) widen the L# definition in the §5.4 outline (and propagate to `research-design.md` Limitations preview), or (b) add a half-clause that explicitly grafts the new instance onto the L# scope, or (c) drop the L# binding and carry the finding without a forwarded limitation. Do not silently fold a categorically distinct concern under an L# whose name does not cover it — a careful sensor will read the L# definition in §5.4 and see the seam.
- **Why:** §3.3 round 1 ¶6 bound a third-party-processor (cloud) disclosure gap to L3 ("researcher–developer overlap and informal study procedures"). Cloud-processor disclosure is a GDPR-transparency category, not a researcher-developer-overlap category; the binding read as forced. The fix in this case was to remove the disclosure clause entirely (the project chose not to use a cloud-processor at thesis-writing time), but the underlying rule generalises: any L#-binding sentence is a small claim about category fit between the local finding and the §5.4 limitation, and the claim must hold.
- **When to apply:** Every section that forwards to an L1–L12 limitation. Particularly Ch 3 method sections (§3.1 ¶3 → L3/L10, §3.3 ¶2 → L2, §3.3 ¶4 → L1, §3.3 ¶6 → L3, §3.6 ¶3 → L5, §3.7 ¶4 → L3), Ch 4 findings sections that bind interview-coverage gaps to L4 or sample-size to L1, Ch 5 anchor sub-sections that bound RQ answers, and Ch 6 RQ-answer paragraphs whose `MUST TRACE` lands on a limitation.
- **Source:** §3.3 round 1 coherence review (2026-05-03).

### Preserve a source's default-vs-exception polarity when paraphrasing polarity-rich claims
- **Rule:** When a source presents a claim in "X is Y unless Z" or "X is not A unless B" form, the source's foregrounding (the default) and the exception are part of the meaning, not just stylistic packaging. A logically-equivalent inversion ("X is A only when B") flips which side of the claim is the rhetorical anchor and reads as a small misrepresentation to a careful sensor reading the source side-by-side. Keep the source's polarity in the paraphrase; if the inversion is needed for sentence flow, attach a short clause that restores the source's framing.
  - BEFORE: "treats preconceptions as bias only when they go undisclosed" (inverts Malterud's polarity — anchors on bias as the default).
  - AFTER: "treats preconceptions as separate from bias unless the researcher fails to disclose them" (preserves Malterud's polarity — anchors on not-bias as the default).
  - Source: \textcite[p.~484]{malterud2001lancet} — "Preconceptions are not the same as bias, unless the researcher fails to mention them."
- **Why:** §3.7 round 1 quality review flagged ¶4's polarity flip on Malterud p. 484. Logically equivalent, but the source's foregrounding is "preconceptions are not bias" (default = not-bias; exception = undisclosed → bias); the thesis paraphrase made bias the rhetorical anchor and disclosure the carve-out. Polarity flips are a class of paraphrase failure that does not show up on a casual read but a sensor reading the source verbatim sees immediately. The same risk applies to any default-vs-exception source claim — Bainbridge on operator-vs-owner asymmetry (p. 775), Hoff & Bashir on dispositional/situational/learned trust antecedents (p. 432), Hevner on validation-before-evaluation (p. 91).
- **When to apply:** Any cite paraphrase of a polarity-rich source claim. Particularly `malterud2001lancet` (p. 484 preconceptions/bias; p. 486 transferability vs population-applicability), `bainbridge1983ironies` (operator-vs-owner default), `hoff2015trust` (three-dimensional trust antecedent default), `hevner2007threecycle` (lab-before-field default), and any source where a default-vs-exception structure is the load-bearing form of the claim. Check by reading the verbatim quote in the source notes file before paraphrasing — the source notes' "Direkte sitat" field preserves the source's polarity by design.
- **Source:** §3.7 round 1 quality review (2026-05-03).

### The because-clause must match the actual rationale — coincidental adjacent facts are not the cause
- **Rule:** The Ch 3 rubric demands "every methodological choice has a because". The because-clause must name the actual cause of the choice, not a fact that happens to be true alongside it. When the real cause is a framing decision (e.g. "this was conducted as industry consultation under Admmit's brief, not formal research"), use that framing as the because; do not redirect the because to a downstream property (e.g. "no special-category personal data was collected") that is evidence the framing is defensible but is not itself the cause. Coincidental-fact because-clauses read to a careful sensor as either reverse-engineered justifications or as the writer not having located the actual cause; the realignment is usually a single sentence rewrite.
  - BEFORE: "No formal Sikt registration was made, since the conversations covered work practices, system use, and assignment criteria only, with no special-category personal data was collected."
  - AFTER: "The project was conducted as an industry consultation under Admmit's bachelor task brief rather than as formal research, and on that basis no Sikt registration was sought; the conversations covered work practices, system use, and assignment criteria only, and no special-category personal data was collected."
- **Why:** §3.3 round 1 ¶6 placed the Sikt-non-registration because-clause on the absence of special-category data. Sikt evaluates whether *any* personal data is processed, not just special-category — so the actual exemption follows from the consultation framing already named in the same paragraph, not from the data-type fact. The same paragraph already had the correct because available; it had simply been used as a follow-on rather than as the cause. This is a precision failure that recurs whenever an honest-framing decision is justified by a coincidentally-true property of the choice.
- **When to apply:** Any "because" clause for a methodological, ethical, or scoping decision. Particularly §3.3 (Sikt rationale, anonymisation rationale, automated-transcription rationale), §3.5 every iteration's "Why" bullet, §3.6 (How-not-Of framing), §3.7 (Malterud-three-criteria rationale), §5.4 every L# limitation explanation, §5.6 (Methodology Reflection self-criticism). The check is: state the rationale, then ask "is this the actual cause, or a fact that happens to be true alongside it?"; if the latter, find the actual cause and state that.
- **Source:** §3.3 round 1 quality review (2026-05-03).

### When a section adopts a single framework as its organising device, the framework choice itself needs a because
- **Rule:** The "every methodological choice has a because" rubric demand usually fires on per-decision rationale (sample size, sampling strategy, analysis method per phase, etc.). A higher-order decision the rule misses unless explicitly named is the **framework-as-organiser** choice: when a section adopts a single named framework (Malterud's three standards in §3.7, Braun & Clarke's six-phase TA in §3.4, SusAF in §5.5, MoSCoW in §3.4, Hoff & Bashir's three-dimensional trust in §5.1.2) as its structural device — the device that determines the section's paragraph order, sub-headings, or load-bearing claims — the framework choice itself is a methodological decision and needs a one-clause because at first naming. The because should explain why *this* framework rather than a competing one in the same domain (Lincoln & Guba over Malterud, Charmaz over Braun & Clarke, etc.), or what about the project's structure made this framework the apt fit. A single half-clause is enough; the because does not need its own paragraph.
  - BEFORE: "The framework used is \textcite{malterud2001lancet}'s three standards for qualitative inquiry."
  - AFTER (one option): "Malterud's three standards are the chosen framework because they map directly to the three load-bearing claims this section must defend — a research question's relevance, a purposive sample's validity, and a researcher-developer configuration's reflexivity."
- **Why:** §3.7 round 1 quality review flagged ¶1 naming Malterud's three standards as the section's structural device without explaining why Malterud rather than Lincoln & Guba or Mays & Pope. The implicit because (the standards happen to map to the section's three downstream paragraphs) was acceptable for §3.7 at +51 % silent-ceiling pressure, but the same omission would not be acceptable for §3.4 (TA framework choice) or §5.5 (sustainability framework choice) where multiple competing frameworks exist in the literature and the choice is more contested.
- **When to apply:** Any section that adopts a single named framework as its organising device. Particularly §3.4 (Braun & Clarke vs Charmaz / Strauss-Corbin / Smith IPA for thematic analysis; MoSCoW vs Kano for requirements prioritisation), §3.7 (Malterud vs Lincoln & Guba / Mays & Pope for qualitative validity), §5.5 (SusAF vs LCA / KARTA for sustainability scoping), §5.1.2 (Hoff & Bashir vs Lee & See / Mayer-Davis-Schoorman for trust modelling). The because does not need to defeat all competitors; it needs to name what made the chosen framework the apt fit for *this section's structural job*.
- **Source:** §3.7 round 1 quality review (2026-05-03).

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

### Bind artefact elements to anchors with transparent verbs, not metaphors
- **Rule:** When a sentence ties a concrete artefact element (a UI feature, an architectural property, an algorithmic capability) to one of the three locked anchor names, use a functional verb — `enables`, `realises`, `implements`, `operationalises`, `delivers` — not a metaphor — `is the substrate of`, `is the foundation of`, `is the scaffolding for`, `embodies the spirit of`. The functional verb names the causal relationship; the metaphor only hints at it. If the verb needs qualification (how it enables, by what mechanism), add a `by ...` clause rather than reaching for a metaphor.
  - **Sub-clause A — anchors cannot be the grammatical subject of imperative verbs.** The anchor name itself must NOT be the grammatical subject of `requires`, `demands`, `mandates`, or any other imperative verb. The artefact element is the subject; the anchor is the realised property. BEFORE: "Efficiency requires that the artefact reduce overtime"; AFTER: "Efficiency is realised by the artefact reducing overtime". This rule applies inside relative clauses too: "the configurability surface that Adaptability requires" inverts the binding — rewrite as "the configurability surface through which Adaptability is delivered".
  - **Sub-clause B — when describing what was decided/built/fixed, name the artefact element, not the anchor.** Where §3.1 has carefully separated the artefact element (HITL, multi-tenant architecture) from the anchor it operationalises (Trust/control, Adaptability), downstream paragraphs must preserve that distinction. BEFORE: "Admmit's mandate fixed Trust/control and Adaptability"; AFTER: "Admmit's mandate fixed HITL and the multi-tenant architecture (the artefact elements operationalising Trust/control and Adaptability)". The anchors are the realised properties, not the things Admmit decided.
- **Why:** Anchor-binding sentences are spine-load-bearing across §1.2, §2.2 (HITL), §3.1, §4.4, §4.5, every §5.1.x sub-section, §6.2. A metaphorical bind reads as decorative compression to a sensor reading for argumentative discipline; the same sentence with `enables` is judged transparent. Example from §3.1 round 1: BEFORE — "the multi-tenant architecture is the technical substrate of Adaptability"; AFTER — "the multi-tenant architecture enables Adaptability by isolating per-customer configuration in a single deployed instance". Sub-clauses A and B emerged from §3.2 round 1 + round 2: the same anchor-binding category includes inverted constructions and artefact-element-vs-anchor-property collapse, both of which a strict sensor would flag.
- **When to apply:** Any sentence in any chapter that names a locked anchor (Efficiency, Trust/control, Adaptability) and ties an artefact element to it. Particularly §1.2 (anchor definitions), §3.1 ¶4 (origin → anchor binding), §3.2 (DSRM Applied "Objectives" bullet + closing-paragraph project-ordering caveat), §4.4–4.5 (system features → anchor), §5.1.1/§5.1.2/§5.1.3 (every sub-section), §6.2 (RQ-answer paragraphs).
- **Source:** §3.1 round 1 coherence review (2026-05-02); sub-clauses A + B added from §3.2 round 1 + round 2 reviews (2026-05-03).

### Parenthesise the abbreviation on first mention of a multi-word concept
- **Rule:** The first time a multi-word concept that will later be abbreviated appears in prose, write it with the abbreviation in parentheses: "Design Science Research Methodology (DSRM)", "Transport Management System (TMS)", "Constraint Programming SAT (CP-SAT)". Subsequent uses may take the abbreviation alone. Do not introduce the abbreviation only at second use — it lands cold for a reader following the section linearly. This applies to concept-level abbreviations, alongside the existing actor-term-form rule.
- **Why:** §2.4 round 1 ¶4 used "DSRM" without "(DSRM)" being attached to the first mention of "Design Science Research Methodology" in ¶1, forcing readers to reconstruct the link. Cold-reader legibility is a sensor-grade criterion; abbreviations are cheap to introduce correctly and expensive to chase down later.
- **When to apply:** Any chapter. Especially Ch 2 (DSR / DSRM, HITL, TMS, VRP, CP-SAT), Ch 3 (DSRM activities, MoSCoW), Ch 4 (system component abbreviations), Ch 5 (UTAUT, SusAF). For concepts that already have a glossary entry with an established abbreviation, prefer the glossary form on first mention in prose.
- **Source:** §2.4 round 1 coherence review (2026-05-02).

### Distinguish interview-guide topics from TA analytic-output themes

- **Rule:** When a section discusses both pre-coded interview-guide structure AND constructed analytic outputs of thematic analysis, the two object types MUST carry distinct labels. Reserve "themes" for analytic outputs of the six-phase TA (constructed during Phases 3–5). Use "guide topics" / "topics" for the pre-coded scaffolds the interviewer worked through during each call. Naming both with the same word ("themes") and the same count silently equates pre-coded scaffolds with analytic outputs and contradicts any inductive positioning the section claims. Renaming in only one section displaces the drift cross-section, so the convention must hold across every section that references both object types.
- **Why:** §3.4 round 1 used "the five themes that anchored each call" for guide topics AND "the analysis identified five themes across the seven transcripts" for analytic outputs within one paragraph. The same word + same count silently equated the two — a sensor reading for terminology rigour and methodological coherence sees the seam, and either reading (themes lifted from guide → secretly deductive; or themes coincidentally converged on guide → suspiciously tidy) undermines inductive positioning. The §3.4 round 2 fix renamed only §3.4 ¶1 to "guide topics", which displaced the drift to §3.3 (still using "themes" for guide topics in three places). Round 2 closed the loop by renaming both sections.
- **When to apply:** Any qualitative-method or findings section that discusses both interview-guide structure and TA outputs. Particularly §3.3 (Data Collection), §3.4 (Data Analysis), §4.1 (Interview Findings), §5.1.x (Discussion), §5.6 (Methodology Reflection). Also: any future writing that names a count of items from one type — verify whether the count refers to pre-coded structure or to analytic outputs before letting it travel.
- **Source:** §3.4 round 1 + round 2 coherence reviews (2026-05-03).

### Cross-chapter terminology lock for Ch 2-committed vocabulary distinctions
- **Rule:** When Ch 2 commits the thesis to one side of a vocabulary distinction — Wieringa "validate" (predict deployed behaviour) over "evaluate" (deploy in production); Bainbridge "operator-vs-owner asymmetry" over "stakeholder mismatch" / "demand asymmetry"; Hoff & Bashir three-dimensional "trust antecedents" over generic "trust"; Miller "explanation as interface" over "transparency" alone; Adaptability over "skalerbarhet" / "fleksibilitet" — every downstream chapter uses that committed vocabulary, not the alternatives. Activity / section / heading labels are exempt where they originate elsewhere (e.g. the DSRM activity name "Evaluation" is from Peffers, not from the thesis vocabulary), but the body describing what the activity does *in this thesis* must use the committed verb.
- **Why:** §3.2 round 1 used "tested for / test of / not tested" three times in the Evaluation bullet where §2.4 ¶3 had explicitly committed the thesis to Wieringa's "validate". The Evaluation bullet header is the DSRM activity label and stays; the bullet body must use the committed verb. The fix in round 2 rewrote the bullet with "validated against / validation instrument / not validated". Vocabulary drift across chapters is a sensor-visible discipline failure even when no individual sentence is wrong.
- **When to apply:** Any chapter that re-engages a Ch 2 vocabulary commitment. Particularly §3.2 (Wieringa validation; Bainbridge asymmetry as DSRM-Applied Problem-Identification framing), §3.6 (Wieringa validation; "How-not-Of" framing), §3.7 (Wieringa validation; Malterud's three criteria, not four), §4.5 (algorithm benchmarking — "validation" not "test" / "evaluation"), §5.1.1 (Bainbridge asymmetry verbatim), §5.1.2 (Hoff & Bashir three-dimensional, Miller explanation as interface, Lee trust foundation), §6.2 (RQ-answer paragraphs must use the committed vocabulary verbatim).
- **Source:** §3.2 round 1 coherence review (2026-05-03).

---

## Reader accessibility

### Gloss in-house jargon on first use, or pick plainer phrasing
- **Rule:** Internal vocabulary — "fit/gap", "anchor concept", "spine", "outline marker", "MUST CITE", and similar workflow terms — is not legible to a cold sensor. On first use in prose, gloss the term in one short clause ("the fit/gap analysis — what existing systems cover and what they do not — ...") or replace with plainer phrasing. The supervisor's preferred fix for fit/gap specifically is a table contrasting "what exists" against "what is missing"; plain prose may use that same framing.
- **Why:** Supervisor 2026-05-02: "Istedenfor fit gap, som ikke alle vet hva er og kan bli uklart: Feks tabell. Hva finnes det og hva mangler." Internal terminology is fine in planning files but lands as opaque to sensors and external readers.
- **When to apply:** Any prose section, especially Ch 2 background, Ch 4.3 fit/gap, Ch 5 discussion. The internal labels remain free to use in `fitgap-summary.md`, `outline.md`, and other planning artefacts.
- **Source:** Supervisor 2026-05-02 (logged in `context/docs/project/supervisor-feedback.md`).

### Hard rule: abbreviate Ressursplanlegger as RP after first mention
- **Rule:** The artefact name **Ressursplanlegger** is defined exactly once at its first prose mention in the thesis as `Ressursplanlegger (hereafter RP)`, and the abbreviation **RP** is used in every subsequent body-prose mention thereafter. The first mention is currently in Ch 2 §preamble; it will move to Ch 1 once that chapter is drafted, at which point the Ch 2 expansion is removed. Section labels (e.g. `sec:ressursplanlegger`), code identifiers, file paths (`/ressursplanlegger`), and the title page keep the full name. Context files (`context/glossary.md`, `context/thesis-spine.md`, `context/outline.md`) keep the full name as the canonical glossary term.
- **Why:** User directive 2026-05-04. The full name is long, repeats heavily across every chapter, and reads as a stylistic tic when used eight to fifteen times per chapter. The abbreviation defined once at the start gives a single canonical reference and lets every later sentence be shorter without losing identity.
- **When to apply:** Every section, every draft, every revision pass. Writers must produce `RP` in body prose after the canonical first mention; reviewers must flag any unintroduced `Ressursplanlegger` in body prose (other than the canonical first mention) and any `RP` that appears before its definition. When Ch 1 is drafted, the writer moves the `Ressursplanlegger (hereafter RP)` definition to its first prose mention there and changes the Ch 2 §preamble first-line back to `RP pairs an algorithm...`.
- **Source:** User directive 2026-05-04 (logged in `context/docs/project/supervisor-feedback.md` if persisted; preserved here as the enforceable rule for writers/reviewers).

### Hard rule: never use em dashes anywhere in the thesis
- **Rule:** Em dashes (LaTeX `---`, Unicode `—`) are forbidden in all thesis output. This applies to every chapter, every section, every paragraph, bulleted or prose, lone or matched-pair, gloss / apposition / pivot / parenthetical / acronym-expansion alike. Replace with commas (apposition: "configurable time budget, a property that matters"), parentheses (true aside: "(coordinator experience of the visibility gap, not its prevalence)"), colons (orientation: "windows: week boundaries and mid-shift absences"), semicolons (clause joining), or a full stop (sentence break). Acronym-expansion em-dashes (`CP-SAT (Constraint Programming --- Satisfiability)`) are noise next to the surrounding parens and should drop the dash entirely. En dashes (`--` for number ranges, e.g. `pp.~75--105`) remain allowed; the ban is only on em dashes.
- **Why:** User directive 2026-05-04 ("never ever use em dashes") superseding the prior soft caps (≤1 per sub-subsection in bulleted sections; ≤2 per 100 words in prose). Em dashes had become a stylistic crutch across drafted Ch 2, Ch 3, and Ch 5; the user reads them as AI-voice tell. A hard ban is unambiguous to enforce and removes the recurring pattern at source.
- **When to apply:** Every section, every revision pass. Writers must never type `---` or `—`; reviewers must flag any occurrence as a critical issue. Existing drafts (Ch 2, Ch 3, Ch 5) are being swept clean.
- **Source:** User directive 2026-05-04 (replaces §3.5 round 1 budget rule and §3.7 round 1 density-cap rule, both 2026-05-03).

### Don't reference an appendix that does not exist — commit to creating it, or rephrase the location
- **Rule:** When the outline calls for an artefact (interview guide, decision log, deviation table, requirements traceability matrix, etc.) to live "in the appendix", the section text must NOT make that reference unless the appendix actually exists in the .tex tree (a real `\appendix` block with a `\label{app:...}` the prose can `\Cref{}`). The honest fallback when the appendix is unwritten is to either (a) create the appendix now and reference `\Cref{app:X}`, or (b) rephrase to a working-notes location that is not implicitly public ("documented in the project's working notes" rather than "in the project repository alongside the analysis notes"). The repository-pointer phrasing reads as evasive to a sensor — readers cannot access the project repository at submission time, so the prose either over-promises an appendix or implies a citable artefact a sensor cannot see.
  - BEFORE: "The full topic guide is documented in the project repository alongside the analysis notes."
  - AFTER (option a): "The full topic guide is reproduced in `\Cref{app:interview-guide}`." (with the appendix actually written)
  - AFTER (option b): "The full topic guide is documented in the project's working notes."
- **Why:** §3.3 round 1 ¶3 said "documented in the project repository alongside the analysis notes" while the outline expected an appendix. No appendix existed at draft time. The repository-pointer is honest about not having an appendix but reads as a soft promise of accessibility the thesis cannot keep.
- **When to apply:** Any section that forwards an artefact location. Particularly §3.3 (interview guide / topic guide), §3.7 (Malterud-three-criteria table if rendered as one), §4.2 (requirements traceability matrix if rendered separately), §4.7 (process documentation table set), §5.3 (sustainability effects table). Decide artefact-by-artefact: is this a thesis appendix or a working-notes pointer?
- **Source:** §3.3 round 1 coherence + quality review (2026-05-03).

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