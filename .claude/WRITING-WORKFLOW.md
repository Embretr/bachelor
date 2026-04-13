# Writing Workflow — Ressursplanlegger Bachelor Thesis

> The complete process from blank section to approved chapter.

## Quick Start

```
/write-section 2.1          ← write one section (auto context + checks + 3 reviews)
/write-section 2.2          ← repeat for each section in the chapter
/write-section 2.3
/write-section 2.4
/review-chapter 2           ← chapter integration check (2 agents)
→ Human marks approved      ← you decide when it's done
```

## Architecture

```
.claude/
├── commands/
│   ├── write-section.md       # /write-section 2.1 — entry point
│   └── review-chapter.md      # /review-chapter 2 — entry point
├── skills/
│   ├── write-section/SKILL.md # full pipeline logic
│   └── review-chapter/SKILL.md # chapter integration logic
└── agents/
    ├── writer.md              # writer prompt template
    ├── red-thread.md          # chapter-level coherence template
    ├── quality.md             # chapter-level grading template
    └── naturalness.md         # AI-detection checklist
```

## Evidence Anchoring Model

The outline (`context/outline.md`) contains per-paragraph evidence markers:
- **MUST CITE:** (Ch 2–3) — specific literature sources required
- **MUST EVIDENCE:** (Ch 4) — each finding traces to a specific data source
- **MUST ANCHOR:** (Ch 5) — each claim points to Ch 4 finding AND/OR Ch 2 theory
- **MUST TRACE:** (Ch 6) — each conclusion traces to a sub-question and chapter evidence

The pipeline checks these deterministically (Step 4) and via reviewer judgment (Step 5).

## What `/write-section` Does

1. **Validates** — checks outline has ¶-plan, context files exist, glossary/refs populated
2. **Writes** — spawns writer agent with explicit context manifest
3. **Saves** — inserts into .tex file, creates round-scoped backup
4. **Checks** — deterministic hard fails (placeholders, forbidden voice, citation keys, compile) + warnings (filler, transitions, em-dashes) + citation density listing + outline compliance (¶ count, evidence key check)
5. **Reviews** — 3 independent agents (coherence, quality, naturalness) with JSON gates. Agents have chapter-type-specific questions and depth/source assessment.
6. **Reports** — structured summary, saves review files, updates STATUS.md

If section already has content → asks: revise (recommended) or overwrite.

## What `/review-chapter` Does

1. **Verifies** all sections are `drafted-reviewed`
2. **Spawns** 2 agents: red-thread (cross-section coherence) + sensor (NRT grading)
3. **Reports** — candidate-approved or needs-revision

## Gate Logic

### Per section (`/write-section`):

| Gate | Pass criterion | Fail action |
|------|---------------|-------------|
| Hard checks | No [FILL IN], no [CITATION NEEDED], no "we believe/think/found", all citation keys valid, `make` passes | `drafted-needs-revision` — skip reviews |
| Coherence | 0 critical unsupported claims, spine serves, 0 critical logic issues. Minor issues reported but don't block. | `drafted-needs-revision` |
| Quality | Grade = A AND depth = "genuine" AND critical_source_issues = 0. "mixed" source_integration doesn't auto-fail. | `drafted-needs-revision` (B = below A standard, C = major gap) |
| Naturalness | Score ≥ 4/5. Reports em-dashes and inflated vocab counts. | `drafted-needs-revision` |
| **All pass** | | `drafted-reviewed` |

Additional checks (informational, not gates):
- **Citation density**: lists paragraphs without citations (reviewer decides which need them)
- **Outline compliance**: ¶ count match + evidence key presence
- **Em-dashes**: listed as warning with locations

### Per chapter (`/review-chapter`):

| Gate | Pass criterion |
|------|---------------|
| Red thread | 0 critical cross-section issues, spine aligned, RQ contribution A or B, 0 orphaned theories |
| Sensor | Overall grade A, no criteria at C, depth = "genuine" |
| **All pass** | `candidate-approved` → human decides |

## Writing Order

```
Ch 2 → Ch 3 → Ch 4.1 → 4.3 → 4.2 → 4.4 → 4.5
→ Ch 5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6
→ Ch 1.1 → 1.2 → 1.3 → 1.4
→ Ch 6.1 → 6.2 → 6.3
→ Abstract + Sammendrag
```

Ch 1 after Ch 2–5 (intro matches what was actually written).
Ch 6 last (answers the RQ based on everything above).

## Key Rules

1. **One section per `/write-section` run.** Claude loses focus after ~3000 words.
2. **Writer and reviewers never share context.** Each is a separate agent spawn.
3. **No auto-fix, no auto-approval.** All failures reported to human. Human decides.
4. **Revise mode loads previous reviews.** Re-running `/write-section X.Y` on existing content uses feedback from the last round.
5. **Quality pass = A only.** B is "needs improvement", not pass. This thesis targets A.
6. **Spine sync after each chapter.** Compare what was written to thesis-spine.md. Update if needed.

## Review Storage

```
evaluation/review/sections/
├── ch2-2.1-round1-checks.md       # deterministic check results
├── ch2-2.1-round1-coherence.md    # section coherence review
├── ch2-2.1-round1-quality.md      # section quality review
├── ch2-2.1-round1-naturalness.md  # naturalness review
├── ch2-2.1-round1-backup.tex      # previous content backup
├── ch2-2.1-round2-...             # second round (if revised)
└── ...

evaluation/review/
├── redthread-ch2.md               # chapter integration: red thread
└── quality-ch2.md                 # chapter integration: sensor
```
