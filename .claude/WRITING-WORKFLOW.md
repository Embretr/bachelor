# Writing Workflow — Ressursplanlegger Bachelor Thesis

> The complete process from blank section to approved chapter.

## Quick Start

```
/write-section 2.1          ← write one section (auto context + checks + 3 reviews + auto-revision)
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

## What `/write-section` Does

1. **Validates** — checks outline has ¶-plan, context files exist, glossary/refs populated
2. **Writes** — spawns writer agent with explicit context manifest
3. **Saves** — inserts into .tex file, creates round-scoped backup
4. **Checks** — deterministic hard fails + warnings (filler, transitions, em-dashes) + citation density + outline compliance
5. **Auto-fixes** — attempts to fix forbidden voice via minimal writer-fix (Step 4.5)
6. **Reviews** — 3 independent agents (coherence, quality, naturalness) with structured JSON gates
7. **Auto-revises** — if reviews fail with fixable critical issues, spawns writer with consolidated feedback (max 3 rounds)
8. **Polishes** — if reviews pass but have minor suggestions, runs one polish round with rollback
9. **Reports** — structured summary, saves review files, updates STATUS.md

## Iteration Model

### Auto-revision (critical issues)
- **Max 3 total rounds:** Round 1 = initial write. Rounds 2–3 = auto-revisions. Round 4 is never created.
- Round is incremented BEFORE spawning revision writer. Files use next_round.
- If no fixable critical issues exist → `drafted-needs-manual-fix` (pipeline stops).
- If round 3 still fails → `drafted-needs-manual-fix`.

### Polish (minor improvements)
- Runs **once** when all gates pass but suggestions/minor issues exist.
- Uses separate filenames (e.g., `round{R}-polish-quality.md`) to preserve original passing review.
- **Rollback:** If polish fails any gate, pre-polish backup is restored. Status stays `drafted-reviewed`.
- Polish NEVER triggers auto-revise. It is an isolated round.

### Deterministic auto-fix (Step 4.5)
- Forbidden voice: minimal writer-fix (not regex), preserves context. Pre-autofix backup saved.
- Placeholders, invalid citations, compilation: STOP — cannot auto-fix.
- Max 1 auto-fix attempt per round.

## Gate Logic

### Per section (`/write-section`):

| Gate | Pass criterion | Fail action |
|------|---------------|-------------|
| Hard checks | No placeholders, no forbidden voice, all citation keys valid, compile passes | Step 4.5 auto-fix attempt, then `drafted-needs-revision` if still fails |
| Coherence | All critical counts == 0, spine serves | Auto-revise (Step 6.5) |
| Quality | Grade A, depth "genuine", critical_source_issues == 0 | Auto-revise (Step 6.5) |
| Naturalness | Score ≥ 4/5 | Auto-revise (Step 6.5) |
| **All pass** | | `drafted-reviewed` → polish if suggestions exist |

### Statuses

| Status | Meaning |
|--------|---------|
| `not started` | Section has no content |
| `drafted-needs-revision` | In progress — auto-revise is handling this |
| `drafted-needs-manual-fix` | Pipeline exhausted auto-fix (3 rounds or no fixable issues). Human must intervene. |
| `drafted-reviewed` | All gates passed. Ready for next section or chapter review. |
| `candidate-approved` | Chapter-level review passed. Awaiting human approval. |
| `approved` | Human approved. |

### Per chapter (`/review-chapter`):

| Gate | Pass criterion |
|------|---------------|
| Red thread | 0 critical cross-section issues, spine aligned, RQ contribution A or B |
| Sensor | Overall grade A, no criteria at C |
| **All pass** | `candidate-approved` → human decides |

## Evidence Anchoring

The outline (`context/outline.md`) contains per-paragraph evidence markers:
- **MUST CITE:** (Ch 2, 3) — academic source from references.bib
- **MUST EVIDENCE:** (Ch 4) — empirical/system source from context/
- **MUST ANCHOR:** (Ch 5) — connect to RQ, thesis spine, or earlier chapter
- **MUST TRACE:** (Ch 6) — trace to specific section, finding, or limitation
- **MUST GROUND:** (Ch 1) — grounded in context source, detailed evidence comes later

Missing marker satisfaction is reported as a critical review issue.

## Writing Order

```
Ch 2 → Ch 3 → Ch 4.1 → 4.3 → 4.2 → 4.4 → 4.5
→ Ch 5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6
→ Ch 1.1 → 1.2 → 1.3 → 1.4
→ Ch 6.1 → 6.2 → 6.3
→ Abstract + Sammendrag
```

## Key Rules

1. **One section per `/write-section` run.** Claude loses focus after ~3000 words.
2. **Writer and reviewers never share context.** Each is a separate agent spawn.
3. **Auto-revise handles failures.** Up to 3 rounds. Human intervenes only after `drafted-needs-manual-fix`.
4. **Polish is safe.** Rollback if it regresses. Never blocks.
5. **Quality pass = A only.** B is "needs improvement", not pass.
6. **Spine sync after each chapter.** Compare what was written to thesis-spine.md. Update if needed.

## Review Storage

```
evaluation/review/sections/
├── ch2-2.1-round1-checks.md         # deterministic checks
├── ch2-2.1-round1-coherence.md      # coherence review
├── ch2-2.1-round1-quality.md        # quality review
├── ch2-2.1-round1-naturalness.md    # naturalness review
├── ch2-2.1-round1-backup.tex        # content backup
├── ch2-2.1-round1-pre-autofix.tex   # backup before deterministic fix (if any)
├── ch2-2.1-round2-...               # auto-revision round 2
├── ch2-2.1-round2-pre-polish.tex    # backup before polish
├── ch2-2.1-round2-polish-checks.md  # polish review (separate from round2)
├── ch2-2.1-round2-polish-quality.md
└── ...

evaluation/review/
├── redthread-ch2.md                 # chapter integration: red thread
└── quality-ch2.md                   # chapter integration: sensor
```
