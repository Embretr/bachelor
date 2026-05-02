# Chapter 2 — Red Thread Review (Round 1)

**Date:** 2026-05-02
**Reviewer:** chapter-redthread subagent
**Source file:** `result/chapters/ch2/ch2-theory.tex`

---

## 1. Cross-section transitions

**§2.1 → §2.2**: No bridge sentence. §2.1 closes on solver families and a forward reference to §4.5; §2.2 opens with "A traffic coordinator who reviews and approves every algorithm-generated plan…" — the leap from solver-family taxonomy to HITL is abrupt. **Fix**: add one bridge sentence at the end of §2.1 noting that solver capability alone does not specify how the coordinator interacts with the plan.

**§2.2 → §2.3**: Reasonable. The actor-anchored bridge ("The traffic coordinator who builds the daily plan does so inside…") works.

**§2.3 → §2.4**: Missing bridge. §2.3 ends with "the discussion returns to it under Tilpasningsdyktighet in §5.1.3"; §2.4 opens "Design Science Research is the research paradigm…". **Fix**: add a one-sentence bridge framing DSR as the methodology for studying an artefact that fills the gap §2.3 just identified.

## 2. Repetition across sections

No load-bearing repetition. The "visibility" framing reuse (§2.1 ¶3 → §2.2 ¶5) is a deliberate spine callback. Pass.

## 3. Spine alignment

Coverage check vs spine sentence:
- Resource scheduling under utilization-oriented constraints — §2.1 ¶3 explicitly does this. ✓
- Three-layer HITL — spine claims **three** layers; chapter delivers Bainbridge + Hoff & Bashir + Miller + **Lee** + Parasuraman = **five** (matching outline §2.2). **The spine sentence and outline disagree.** Critical drift.
- DSR — §2.4. ✓
- VRP and TMS as delimit-only — §2.1 ¶5 delimits VRP cleanly. §2.3 does positioning work, not just delimitation. Minor spine drift; not critical.

The chapter has no opening paragraph (TODO comment line 7). Structural absence at chapter level.

## 4. Research-question traceability

- SQ1 (visibility distribution) — Bainbridge frame (§2.2 ¶2) and Effektivitet (§2.1 ¶3) preload.
- SQ2 (algorithm-assisted, accountable/overridable) — §2.2 ¶6 operationalises four actions; HITL theory layer serves SQ2.
- SQ3 (measurable improvement) — §2.4 validation-vs-evaluation prepares the empirical claim envelope.

**Verdict: A — clear and direct.** Chapter is RQ-load-bearing.

## 5. Promised vs delivered

All forward references concrete and tracked. No promise unfulfilled. Pass.

## 6. Proportionality

Target ~8.5 pages. Actual ~2810 words / 8 pages, with §2.2 longest (5+1 paragraphs matching outline). Within tolerance. Pass.

## 7. Cross-section concept placement

- HITL — defined on first use (§2.2). ✓
- Tabu search / LAHC — cited without unpacking; acceptable given §4.5 forward reference.
- Constraint programming — inline definition. ✓
- NP-hard — brief gloss. ✓
- Trafikkoordinator — never glossed; resolves once Ch 1 §1.1 introduces actor.
- Tillit/kontroll, Tilpasningsdyktighet — first appear without in-chapter definition; rely on §1.2.
- DSR — defined on first use (§2.4 ¶1). ✓
- Effektivitet — operationalised on first use (§2.1 ¶3). ✓

## 8. Cross-section terminology consistency

driver/employee/staff, assignment/task, resource, plan/schedule, solver/engine/algorithm, traffic coordinator — all consistent. No "dispatcher" drift. Pass.

## 9. Cross-section ordering

- Trafikkoordinator in first sentence of §2.1. ✓
- Adjacent-domain example (charge nurse) before formal def — meets supervisor calibration 2026-04-28.
- §2.2 paragraph order matches outline (Parasuraman → Bainbridge → Hoff → Miller → Lee → design). ✓

## 10. Anchor coherence (HARD CHECK)

- **Effektivitet** — verbatim ¶16, ¶35. ✓
- **Tillit/kontroll** — verbatim ¶29, ¶37; four actions (inspect, modify, accept, reject) verbatim ¶29.
- **Tilpasningsdyktighet** — verbatim ¶46. ✓

Forbidden synonyms: Efficiency / Trust/control / Adaptability / fleksibilitet / skalerbarhet / human control / menneskelig overstyring / human oversight / operator oversight — none appear. "trust calibration" used as Hoff & Bashir technical term, correctly distinguished from Tillit/kontroll. ✓

**Anchor drift count: 0.**

## 11. Structural patterns (named A-grade moves)

- Definitions-first per subsection. ✓
- Asymmetric depth proportional to load (§2.2 longest). ✓
- Forward references explicit per theory point.
- Visibility-gap forward reference. ✓
- Operator-vs-owner asymmetry verbatim. ✓

Pass.

## 12. Source audit

Citation density appropriate across all sections. No orphan sources. All cited claims verified against source notes (30+ citations checked). **Source audit issues: 0.**

## 13. Theory-tracker check

Not applicable for Ch 2 (Ch 5 not yet written). Skip.

## 14. Verdict

**Strongest part**: §2.2 HITL — rigorously sourced, every layer operationalised, Tillit/kontroll invoked at the right moment with four actions verbatim.

**Single biggest coherence problem**: Spine sentence (3-layer) and chapter (5-layer, matching outline) disagree on HITL layers. Spine-vs-outline-vs-prose mismatch.

**Specific action**: Update `context/thesis-spine.md` Ch 2 spine sentence to "five-layer human-in-the-loop theory" naming all five sources (Parasuraman, Bainbridge, Hoff & Bashir, Miller, Lee), matching outline and chapter content. Then verify Ch 5 §5.1.2 and Ch 6 §6.2 plans treat all five as layers.

Secondary minor issues: missing chapter-intro paragraph and §2.1→§2.2 / §2.3→§2.4 bridge sentences.

---

## JSON Gate

```json
{
  "pass": false,
  "cross_section_issues": 3,
  "spine_aligned": false,
  "rq_contribution": "A",
  "anchor_drift_count": 0,
  "source_audit_issues": 0,
  "orphaned_theories": 0,
  "issues": [
    {
      "id": "spine-layer-count-mismatch",
      "severity": "critical",
      "type": "spine_alignment",
      "where": "context/thesis-spine.md Ch 2 vs result/chapters/ch2/ch2-theory.tex §2.2",
      "quote_spine": "a three-layer human-in-the-loop theory (Bainbridge's operator-vs-owner framing, Hoff and Bashir's trust-calibration model, Miller's explanation-as-interface)",
      "quote_chapter": "§2.2 delivers five layers: Parasuraman (¶1) + Bainbridge (¶2) + Hoff & Bashir (¶3) + Miller (¶4) + Lee (¶5)",
      "fix": "Update context/thesis-spine.md Ch 2 sentence to 'five-layer human-in-the-loop theory' naming all five sources, matching context/outline.md §2.2 description ('Five-layer HITL theory: Parasuraman taxonomy + Lee trust foundation + Bainbridge operator-owner asymmetry + Hoff & Bashir trust calibration + Miller explanation. Layered, not replaced.'). Then verify Ch 5 §5.1.2 and Ch 6 §6.2 outline plans reference the five-layer structure consistently."
    },
    {
      "id": "missing-chapter-intro",
      "severity": "minor",
      "type": "structure",
      "where": "result/chapters/ch2/ch2-theory.tex line 7-8",
      "quote_chapter": "% Chapter-intro paragraph (above §2.1) to be regenerated during /review-chapter 2.",
      "fix": "Add a 4-6 sentence chapter introduction immediately before \\section{Resource Scheduling} that (a) names the four foundations the chapter establishes, (b) signals asymmetric depth proportional to argumentative load, (c) flags VRP and TMS as referenced only to delimit, (d) names the three anchor concepts Effektivitet, Tillit/kontroll, Tilpasningsdyktighet that the chapter preloads."
    },
    {
      "id": "missing-bridge-sentences",
      "severity": "minor",
      "type": "transition",
      "where": "result/chapters/ch2/ch2-theory.tex §2.1→§2.2 boundary (line 22→24) and §2.3→§2.4 boundary (line 46→48)",
      "fix": "Add one bridge sentence at end of §2.1 ¶6 noting that solver capability is necessary but not sufficient — the human-in-the-loop configuration of §2.2 specifies how the coordinator interacts with whatever plan a solver produces. Add one bridge sentence at end of §2.3 ¶3 noting that establishing what TMS systems do not cover does not yet specify the research paradigm under which the missing artefact is built and investigated; that is the work of §2.4."
    }
  ],
  "verdict": "Chapter 2 is technically excellent in source fidelity (zero unsupported claims, every page anchor verified, anchor concepts used verbatim with the four operationalised Tillit/kontroll actions present) and structurally sound at the section level — but the chapter delivers five HITL layers while the spine sentence still describes three, producing a documented spine-vs-outline-vs-prose mismatch that will mislead every downstream chapter that quotes the spine. Update the spine to five layers (matching the outline and the .tex), then add the missing chapter intro and the two bridge sentences flagged above."
}
```
