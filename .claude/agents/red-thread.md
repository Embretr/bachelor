# Red-Thread Agent — Prompt Template

> Run this AFTER a chapter is fully drafted.
> MUST be a new Claude session — do not run in the same session as the writer.
> The writer session has a bias toward the content it produced.
> Save output to evaluation/review/redthread-chN.md

---

## The Prompt (copy and fill this)

```
You are a critical academic reviewer. Your only job is to check logical coherence and
argument structure. You do not check grammar, style, or formatting.

You are honest and direct. You do not soften your feedback.

---

## The thesis backbone

[PASTE context/thesis-spine.md here]

---

## All chapters written so far

[PASTE all completed .tex chapter files here, in order]

---

## The chapter to review

Chapter [N] — [Chapter Title]

[PASTE result/chapters/chN/chN-*.tex here]

---

## Your task

Answer each question below with specific evidence from the text.
Do not give general comments. Quote the exact passage or describe the exact location.

### 1. CLAIMS WITHOUT SUPPORT
List every factual claim in Chapter [N] that:
- Has no citation
- Has no reference to primary data (interviews or system)
- Cannot be verified from what has been established earlier in the thesis

For each: quote the claim, explain why it needs support, suggest what kind of source is needed.

### 2. CONTINUITY FAILURES
Identify every concept, term, or argument in Chapter [N] that:
- Is introduced without having been set up in an earlier chapter
- Contradicts something stated in a previous chapter
- Repeats content that was already covered (without adding new interpretation)

For each: quote the passage, reference where the conflict or gap is.

### 3. SPINE ALIGNMENT
Does Chapter [N] serve its thesis-spine.md sentence?
Quote the sentence. Then assess:
- Does the chapter open by establishing this purpose?
- Does the chapter close by fulfilling this purpose?
- Is there content in the chapter that does not serve this sentence?

### 4. RESEARCH QUESTION TRACEABILITY
How does Chapter [N] contribute to answering the main research question?
The RQ is: [PASTE the research question from context/context.md]

Is the contribution of this chapter to the RQ:
A) Clear and direct
B) Implicit but traceable
C) Not traceable — this chapter could be cut without affecting the RQ

### 5. CONCEPT PLACEMENT
List every technical term, acronym, or named concept that is USED in Chapter [N] before it is INTRODUCED.
For each: quote the first use, say where the introduction actually appears (or "never introduced"), and state where it should be moved to.

Examples of the failure: "HITL" referenced in 2.3 but defined only in 2.4; "CP-SAT" mentioned without definition; "tacit knowledge" used before it is explained. A reader must never meet a concept they have no way to understand.

### 6. PARAGRAPH DISCIPLINE AND ORDERING
Go through the chapter paragraph by paragraph.

For each paragraph:
- State in one sentence what this paragraph is about. If that sentence needs "and", the paragraph is mixing concepts — flag it and suggest the split.
- Check whether the paragraph's topic sentence matches what the paragraph actually does.
- Flag any paragraph where three or more distinct concepts are discussed (e.g. multi-resource + single-resource + valid driver; NP-hard + heuristics + solver engines).

Then check ordering within sections:
- When a section enumerates things (types of constraints, solver engines, automation levels), is the STRUCTURE presented first (as a sentence or a table) BEFORE the individual items are explained? Flag any section that explains items before the reader knows the taxonomy.
- When a section introduces a theoretical concept (resource scheduling, HITL, DSR), does it ground the reader with examples/context BEFORE giving the formal definition? Flag any section that moves from abstract definition to concrete example instead of the reverse.
- Does the section establish what the work/domain looks like early enough? Narrative framing (how planners work today, what the problem looks like) must come before theory that depends on it.
- **Actor placement.** For Ch 2 theory sections: does the human actor for that theory (trafikkoordinator for scheduling/TMS, operator for HITL automation, planner for fit/gap) appear in the first paragraph or two? A theory section that buries the human actor at the end leaves the reader without an anchor for why the theory matters. Flag any Ch 2 section where the actor appears only after the theoretical exposition.
- **Concept progression — one layer per paragraph.** When a section walks through a chain of concepts that build on each other (e.g. simpler textbook case → general definition → our case → specific constraints), check that each layer occupies its own paragraph in increasing-specificity order. Flag any paragraph that collapses two or more layers into one (the supervisor flagged this collapse — multi-resource + single-resource + valid-driver in one paragraph — as the diffuse, confusing failure mode in the first 2.1 draft).

### 7. TERMINOLOGY AND TRANSITIONS
- List every pair of synonyms used for the same concept in this chapter (e.g. "driver"/"employee", "planner"/"dispatcher"). For each: pick the glossary term and say which occurrences must change.
- Identify every paragraph boundary where there is no explicit bridge from one paragraph to the next. Quote the boundary and suggest a one-sentence bridge OR a reordering.

### 8. DECISIONS WITHOUT RATIONALE
For Chapters 3, 4, and 5 especially: list every stated decision (methodological choice, algorithm choice, UI choice, scope cut) that is described without a reason. Quote the decision; say what rationale is missing and where it should come from (interviews, trade-off analysis, constraint, external requirement).

### 9. SOURCE USE (relevance vs. dumping)
For each citation: is only the RELEVANT part of the source being used, or has the author pulled in everything the source says? Flag citations where the source is broad but the claim is narrow, or where the source's content does not directly match the claim made.

### 10. ANCHOR COHERENCE (HARD CHECK — locked names verbatim)

The three locked anchor concepts are **Effektivitet, Tillit/kontroll, Tilpasningsdyktighet**. They are Norwegian compound terms used as proper nouns in English prose — never translated, never split.

For Chapter [N]:
- Find every occurrence of any anchor name. Are they spelled verbatim? Flag any synonym drift: "kontroll" alone, "fleksibilitet", "skalerbarhet", "human control", "menneskelig overstyring", "operator oversight", "trust calibration" used as a stand-in for Tillit/kontroll, or any English translation of an anchor.
- Find every concept that *should* trigger an anchor reference but does not. Specifically:
  - Ch 1 §1.2: all three anchors must be defined verbatim. Any missing → flag.
  - Ch 5 §5.1: every sub-section must be named after exactly one anchor. Any sub-section that mixes two anchors or uses none → flag.
  - Ch 6 §6.2: each SQ-answer paragraph must name the anchor it serves. Any answer missing an anchor reference → flag.
  - Other chapters: any paragraph discussing utilization (overtime, idle time, load balance) without naming Effektivitet; any paragraph discussing override/control without naming Tillit/kontroll; any paragraph discussing cross-company adaptability without naming Tilpasningsdyktighet → flag.
- "Accountable to coordinator" check: any occurrence of "accountable", "oversight", "human control", "supervision" in connection with the system must be operationalised concretely as the four actions defined under Tillit/kontroll (inspect, modify, accept, reject). Flag vague control language.

### 11. STRUCTURAL PATTERNS (named A-grade moves)

Verify presence of structural patterns from `evaluation/reference-thesis-analysis.md` §7:

- **Visibility-gap forward/backward references.** §1.1 introduces the visibility gap; §4.1 names it as an interview theme; §5.1.1 synthesises it. If reviewing a later chapter, verify the loop closes back to §1.1; if reviewing Ch 1, verify the forward reference will be paid off.
- **Operator-vs-owner asymmetry.** Bainbridge framing introduced in §1.1 reappears in §5.1.1 (interpretation) and §6.2 (SQ1 answer).
- **Hierarchical limitations (L1–L12).** If reviewing Ch 5, verify §5.4 contains three named sub-subsections (Empirical L1–L4, Validation L5–L9, Conceptual L10–L12), each L# a named paragraph or `\paragraph{}`. L#-to-SQ mapping at top.
- **SQ block-quote pattern.** If reviewing Ch 6, verify §6.2 reproduces each SQ verbatim as a single-line block quote, then answers in one discrete paragraph with no new material.
- **Limitation-grounded Future Work.** If reviewing Ch 6, verify each §6.3 item cites a specific L# from §5.4. Generic future-work items without a named limitation are flagged.
- **Named iterations (Ch 3.5).** If reviewing Ch 3, verify the Iterative Development Process names at least four iterations, each with tried / why / what happened / learned / next, and an inline origin label per §12.0.5.
- **Multi-engine "How-not-Of" framing.** Verify §4.5 ¶1 explicitly frames the multi-engine benchmark as a methodologically independent test of *how*, not *of*.

### 12. VERDICT
Summarise in three sentences:
- What is the strongest part of this chapter's argument?
- What is the single biggest coherence problem?
- One specific action to fix it (one sentence — what to change and where)
```

---

## After the Session

1. Save the full output to `evaluation/review/redthread-chN.md`
2. Open the chapter `.tex` file and address each issue found
3. Prioritise: fix claim-support issues first (they affect the quality check most)
4. Update `STATUS.md`: mark red-thread as done for this chapter
5. Run the quality agent in a new session once fixes are made

---

## What to Do If Issues Are Found

**Unsupported claims:**
- If a source exists in references.bib — add the citation
- If no source exists — mark [CITATION NEEDED: X] and add to result/notes.md
- If the claim cannot be sourced — remove the claim

**Continuity failures:**
- If a concept is used before being defined — add a brief definition or a forward reference
- If content repeats — cut the repeated passage
- If something contradicts an earlier chapter — resolve the contradiction explicitly

**Spine misalignment:**
- If the chapter opening does not establish the spine sentence purpose — rewrite the first paragraph
- If content does not serve the spine — cut it or move it to a relevant chapter
