# Chapter 2 — Sensor (Quality) Review (Round 1)

**Date:** 2026-05-02
**Reviewer:** chapter-sensor subagent
**Source file:** `result/chapters/ch2/ch2-theory.tex`

---

## Per-criterion grading

| Criterion | Grade | Notes |
|---|---|---|
| Asymmetric depth and use-trace | A | §2.2 dominates; §2.4 ¶3 borderline overweight |
| Three-layer HITL | A | All three required layers explicit; Bainbridge/Hoff/Miller anchored |
| Utilization framing in §2.1 | A | ¶3 reframes scheduling under utilization, names Effektivitet verbatim |
| Resource scheduling formulation | A | Multi-resource extension precise; VRP delimited via Braekers' own exclusion |
| TMS positioning (Timpex/Opter) | A | Both named; planning-step gap articulated; no Trimtex/Opptur drift |
| Theory-to-use trace | A | Forward references explicit (Hoff & Bashir's slightly implicit) |
| DSR methodology citations | A | Hevner, Peffers, Wieringa cited correctly with verified pages |

## Decisions + rationale

All decisions justified, not declared:
- Why level 5 (not 6): "The coordinator must act, not merely fail to object."
- Why HITL is structural, not usability: operator-vs-owner asymmetry.
- Why validation, not evaluation: no production deployment.
- Why DSR over positivist/interpretivist: explicit comparison and exclusion.
- Why scheduling not VRP: Braekers' own exclusion criterion.

**No "what without why" issues.**

## Definition quality

All definitions source-grounded, trimmed, domain-fit. No invented definitions.

## Source integration audit

30+ citations checked against verified source notes. **Source integration issues: 0 critical.** One soft "mixed" classification (Pinedo "dispatching rules" framing — bridge phrasing OK).

## A-markers (per Ch 2 reference-thesis pattern)

- Definitions-first sub-subsections: compliant with supervisor-approved opening device (trafikkoordinator early).
- Asymmetric sectional length: present.
- Every theory point reappears in Ch 4 or 5: forward-looking present.
- One paragraph per prior work: present.
- No throat-clearing: present.

## Anchor name drift — HARD CHECK

- Effektivitet — verbatim ¶16, ¶35. **No drift.**
- Tillit/kontroll — verbatim ¶29, ¶37. **No drift.**
- Tilpasningsdyktighet — verbatim ¶46. **No drift.**

"trust calibration" = Hoff & Bashir technical term, correctly distinguished. **Anchor drift count: 0.**

## "Accountable to coordinator" operationalisation — HARD CHECK

¶29 verbatim: "the coordinator must be able to **inspect, modify, accept, or reject** any algorithm-generated assignment". **PASS.**

## Multi-engine "How-not-Of" framing — HARD CHECK

Solver families discussed abstractly without invoking the multi-engine benchmark by that name; forward-referenced only. **PASS** (no over-claim possible).

## Understanding vs summary

Chapter consistently shows understanding, not summary:
- ¶29 *applies* Bainbridge's asymmetry frame to resource-planning.
- ¶31 draws an *implication* from Hoff & Bashir.
- ¶33 *reformulates* Miller's contrastive question in domain vocabulary.

This is the deepest single test of A vs B and the chapter passes it cleanly.

## Limitations / weaknesses bordering A

1. Hoff & Bashir transfer caveat → use-statement transition slightly abrupt.
2. Pinedo "dispatching rules" terminology bridge mildly compressed.
3. §2.4 ¶3 forward-references L5 (not yet defined). Acceptable.
4. Chapter intro paragraph missing (TODO comment line 7).

## Overall assessment

- **Estimated grade: A.** Layered argument with verified citations, applies theory rather than summarising it, names anchor concepts verbatim, operationalises RQ's accountability clause with four-action vocabulary.
- **Single most important fix:** Add the chapter-intro paragraph above §2.1.
- **Pulls thesis grade up.**

---

## JSON Gate

```json
{
  "pass": true,
  "overall_grade": "A",
  "criteria_at_C": [],
  "anchor_drift_count": 0,
  "source_audit_issues": 0,
  "most_important_fix": "Add the chapter-intro paragraph above §2.1 (currently a TODO comment in line 7) so the four sections are framed as a whole, naming the three anchors and forward-referencing the sections that use them.",
  "issues": [
    "Chapter intro paragraph missing — the four sections are not framed as a whole before §2.1 begins (line 7 TODO comment).",
    "NP-hard practical consequence in §2.1 ¶5 could be one phrase fuller ('intractable for daily fleets of 50+ resources, hence the multi-engine architecture in §4.5').",
    "Hoff & Bashir transfer caveat in §2.2 ¶3 → use-statement transition is abrupt; pair the analogy disclaimer with an explicit 'the implication this analogy supports is...' sentence.",
    "§2.4 ¶3 (Wieringa validation paragraph) is slightly overweight relative to other background sections; trim 1–2 sentences to keep §2.2 dominance unambiguous."
  ]
}
```
