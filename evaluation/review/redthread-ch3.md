# Chapter 3 — Methodology — Red-thread Review (round 3, re-run)

Reviewer: chapter-redthread agent
Date: 2026-05-03
Target: result/chapters/ch3/ch3-method.tex
Trigger: /review-chapter 3 re-run after .tex modifications since round-2 pass.

## Summary

**PASS.** Spine aligned, anchor drift 0, source audit 0, RQ contribution A, 0 cross-section critical issues. Three minor polish observations recorded; none failing-grade.

## 1. Cross-section transitions

Each section opens with an explicit reference to a prior section:
- §3.2 opens: "Cref{sec:defining-task} mapped where each design choice originated; this section names the research paradigm under which those choices were operationalised."
- §3.3 opens: "The Problem-Identification activity laid out in Cref{sec:dsr-dsrm} drew its empirical input from a single instrument..."
- §3.4 opens: "The seven interviews described in Cref{sec:data-collection} produced roughly 105 minutes of audio..."
- §3.5 opens: "The artefact described in Cref{sec:dsr-dsrm} was built across eight named iterations..."
- §3.6 opens: "The eight iterations in Cref{sec:iterations} produced an artefact whose claims now need a framework to test them against."
- §3.7 opens: "Cref{sec:evaluation-framework} bounded what the artefact's evaluation can claim; this section bounds what the surrounding research can claim."

No rough boundaries.

## 2. Repetition across sections

Mild repetition but not damaging. The "How-not-Of"/how-not-whether framing is restated three times (§3.2 Evaluation bullet; §3.5.4 Why and Learned; §3.6 ¶1). Spine-endorsed thread but borderline. The four-action operationalisation appears six times — mandated by the Tillit/kontroll spine binding, not a coherence issue. The "105 minutes" appears twice — trivial.

## 3. Spine alignment

Match check on the Ch 3 spine sentence:
- DSR + DSRM applied: §3.2 ✓
- Admmit's bachelor task origin: §3.1 ¶1 ✓
- Seven coordinators contacted on team's own initiative: §3.1 ¶2, §3.3 ✓
- Eight named iterations: §3.5.1–§3.5.8 ✓
- Separate evaluation framework benchmarking solver approaches: §3.6 ✓

Chapter opens with origin (§3.1) and closes with validity bounds (§3.7) — fulfilling "establishes how the research was conducted." Spine alignment STRONG.

## 4. RQ traceability

Each SQ has its method base addressed:
- SQ1 (visibility distribution): §3.3 + §3.4 (interview method + thematic analysis) ✓
- SQ2 (operable + overridable design): §3.5.5 (HITL Surface) + §3.5.7 (plan-time/quality) + §3.6 ¶2 (Tillit/kontroll partial coverage) ✓
- SQ3 (extent + limitations of measurable improvement): §3.6 (multi-engine benchmark + traceability matrix + named L5–L9 forwards) ✓

RQ contribution: **A** (clear and direct).

## 5. Promised vs delivered

§3.1 ¶4 promises: "the research paradigm... interview and analysis... eight named iterations... evaluation framework... validity bounds." All delivered.
§3.2's six DSRM bullets — delivered.
§3.5's eight iterations with tried/why/what happened/learned/next — delivered.
§3.6's asymmetric anchor binding (¶1 promise, ¶2 delivery) — delivered.
§3.6 ¶5's three not-tested forwards (L6/L7/L8) — delivered.

No broken promises.

## 6. Proportionality

Target ~13.5 pages; actual ~5547 words / ~15.8 pages = +17%, within 20% tolerance. §3.5 expansion structurally justified by 8 iterations × 6-bullet move. §3.2 expansion justified by the "single most copyable A-grade move" pattern.

## 7. Cross-section concept placement

First-use audit:
- HITL — §3.1 ¶3 with full operational definition ✓
- CP-SAT — §3.2 Design and Development bullet, expanded parenthetically ✓
- Timefold — §3.2, contextualised as "metaheuristic" ✓
- Greedy heuristic — §3.2 → expanded in §3.5.2 ✓
- DSR/DSRM — DSR §3.1 contextually, full def deferred to Cref{sec:dsr}; DSRM §3.2 ¶2 with six activities ✓
- MoSCoW — §3.4 ¶2 with parenthetical definition ✓
- Sikt — §3.3 ¶6 with definition ✓
- Multi-tenant — §3.1 ¶3 explained ✓
- Anchors (Effektivitet/Tillit/kontroll/Tilpasningsdyktighet) — operationalised at §3.1 ¶4 and full operational definitions in §3.2 Objectives bullet ✓
- L# forwards (L1, L2, L3, L5, L6, L7, L8, L9) — referenced consistently with `\Cref{sec:limitations}` ✓
- tRPC, PostgreSQL, Next.js, OR-Tools — stack-level, NTNU CS reader vocabulary ✓

No undefined-on-first-use concept.

## 8. Cross-section terminology consistency

Spot audit:
- "traffic coordinator" / "coordinator" — consistent ✓
- "engine" vs "solver" vs "solver family" vs "solver registry" — somewhat interchangeable across §3.2, §3.5.3–§3.5.4, §3.6. Reader can disambiguate from context. Mild but acceptable.
- "driver" vs "employee" — schema uses "employees", operational use "drivers". Acceptable.
- "assignment" — consistent ✓
- "override flow" / "HITL flow" / "inspect/modify/accept/reject flow" — multiple labels; the four-action label is the spine-locked one. Mild paraphrase drift, not critical.
- "customer" / "company" — §3.1 ¶1 says "customers", rest "companies" / "customer companies". Acceptable.

## 9. Ordering

Origin → paradigm → instrument → analysis → iterations → evaluation → validity. Recommended A-grade reference pattern. Taxonomies stated before enumeration in §3.5 intro, §3.6 ¶3, §3.7 ¶1. PASS.

## 10. Anchor coherence (HARD CHECK)

**Verbatim usages confirmed:**

Effektivitet — §3.2 Objectives + Problem-identification cross-ref; §3.5.4 Why + Learned; §3.6 ¶2 + ¶5. ✓
Tillit/kontroll — §3.1 ¶4; §3.2 Objectives; §3.5.5 Learned; §3.5.7 Origin + Why; §3.6 ¶2 + ¶5. ✓
Tilpasningsdyktighet — §3.1 ¶4; §3.2 Objectives + Communication; §3.5.8 Origin + Why + Learned; §3.6 ¶2. ✓

**Drift check (synonyms / English / splits):**
- "Trust/control" — none.
- "Efficiency" — none.
- "Adaptability" — none.
- "kontroll" alone (without Tillit/) — none.
- "fleksibilitet" — none.
- "skalerbarhet" — none.
- "human control", "operator oversight", "trust calibration", "menneskelig overstyring" — none.

The phrase "operator stance" in §3.6 ¶1 is design-position description, not control-language drift. "Coordinator authority" appears multiple times always paired with the four-action operationalisation.

**Anchor drift count: 0.** PASS.

## 11. Structural patterns (named A-grade moves)

- Origin-story §3.1: present (Admmit OPG29, team's cold-call initiative, HITL-as-mandate before interviews) ✓
- DSRM applied step-by-step: present (six bullets, 2–4 sentences each, applied to this project) ✓
- Iterations named with descriptive titles: present (eight iterations, six-bullet pattern) ✓
- Inline origin label per iteration: present (Admmit-mandate, designer-technical, mixed) ✓
- Honest about failure: §3.5.1 substrate gaps; §3.5.2 greedy ceiling; §3.5.3 quality degradation; §3.5.4 inconsistencies; §3.5.5 stale conflict displays; §3.5.6 false positives; §3.5.7 illegible time labels; §3.5.8 weight UX problem ✓
- Evaluation distinct from validity: §3.6 / §3.7 separation with explicit handoff ✓
- Multi-engine "How-not-Of" framing: §3.2 + §3.5.4 + §3.6 ✓

L1/L2/L3/L5/L6/L7/L8/L9 forward references with `\Cref{sec:limitations}` pre-build the §5.4 forward references — strong A-grade move. PASS.

## 12. Source audit

Citation density: §3.1 0 (origin story); §3.2 5 of hevner+peffers; §3.3 0 (mechanics); §3.4 6 of braun; §3.5 0 (narrative); §3.6 0 (Wieringa via Cref defer); §3.7 4 of malterud. All density choices appropriate.

Content match per source notes:
- **hevner2004design** p.82 — paraphrase with citation; matches "knowledge ... acquired in the building and application of an artifact" ✓
- **peffers2007dsrm** pp.46, 56, 56 — six-activity list, no-strict-sequence (verbatim), four-entry-points table ✓
- **braun2006thematic** p.81, p.77, p.87, pp.81–82, Table 2 criterion 15 — flexibility / accessibility / six phases / positioning room / active-not-emerged framing ✓
- **malterud2001lancet** p.483 (three standards), p.485 (purposive sampling), p.486 (bounded transferability), p.484 (preconceptions-not-bias) — all verbatim with correct page anchors ✓

All citations content-match the source notes. Wieringa correctly deferred via `\Cref{sec:dsr}` per the locked rule. No drift.

**Source audit issues: 0.** PASS.

## 13. Verdict (three sentences)

**Strongest part of the chapter's argument**: The eight named iterations in §3.5 are honest, structured, and each carries an explicit origin label (Admmit / interview-validated / designer-technical / mixed) plus a "Learned" bullet that names a real failure mode — this is precisely the A-grade reference pattern, and §3.5.4's commitment to "How-not-Of" framing threads cleanly into §3.6's asymmetric anchor binding.

**Single biggest coherence problem**: The mild drift among "engine" / "solver" / "solver family" / "solver registry" labels in §3.2, §3.5.3–§3.5.4, §3.6 — readers can follow it, but a glossary fix would tighten it. Below the threshold for failing the chapter.

**One specific action to fix it**: In §3.2 Design-and-Development bullet add a one-clause definition: "a multi-engine solver layer — a greedy heuristic, the OR-Tools CP-SAT constraint solver, and the Timefold metaheuristic, hereafter called the three engines — invoked as subprocesses." Then use "engine" consistently. (Polish-grade, not coherence-failing.)

---

## JSON Gate

```json
{
  "pass": true,
  "cross_section_issues": 0,
  "spine_aligned": true,
  "rq_contribution": "A",
  "anchor_drift_count": 0,
  "source_audit_issues": 0,
  "orphaned_theories": 0,
  "issues": [
    {
      "severity": "minor",
      "category": "terminology_consistency",
      "location": "§3.2 Design-and-Development bullet; §3.5.3–§3.5.4; §3.6",
      "issue": "Mild interchangeable use of 'engine', 'solver', 'solver family', 'solver registry'. Below failing threshold; reader can disambiguate from context.",
      "suggestion": "Add a one-clause naming convention in §3.2 ('hereafter called the three engines') and use 'engine' consistently downstream."
    },
    {
      "severity": "minor",
      "category": "transition_polish",
      "location": "§3.5 intro to §3.5.1",
      "issue": "§3.5 intro framing 'told here as a connected narrative' slightly oversells how connected per-iteration narratives feel — each §3.5.x reads independently.",
      "suggestion": "Optional. Tighten §3.5 intro to 'told here as a sequence of decisions' rather than 'connected narrative'."
    },
    {
      "severity": "minor",
      "category": "repetition",
      "location": "§3.5.4 Why and Learned + §3.6 ¶1",
      "issue": "Triple restatement of the how-not-whether/How-not-Of framing. Spine-endorsed thread, but borderline.",
      "suggestion": "Optional. In §3.5.4 'Learned' bullet, drop the explicit cross-ref since §3.6 owns the canonical statement; let the iteration's Learned bullet stay tightly local."
    }
  ],
  "verdict": "Strongest part: the eight named iterations in §3.5 each carry an explicit origin label and an honest Learned bullet, precisely the A-grade reference pattern; the how-not-whether framing threads cleanly from §3.5.4 into §3.6's asymmetric anchor binding. Single biggest issue: mild drift among 'engine' / 'solver' / 'solver family' labels — readers can follow it, but a glossary fix in §3.2 would tighten the chapter. Fix: add 'hereafter called the three engines' to §3.2 Design and development bullet and use 'engine' consistently in §3.5.3, §3.5.4, and §3.6."
}
```
