# Status — Ressursplanlegger Thesis

The full draft exists at `result/`. All chapters compile (`make` produces `main.pdf`).

## Current phase

**Feedback-driven revision.** The work is to apply per-paragraph feedback (`feedback-app/state.json`), supervisor directives (`context/supervisor-log.md`), and the rules distilled in `context/lessons-learned.md` to every section until the prose meets A-grade everywhere.

## What has happened recently

- **2026-05-06.** Repo restructured. The three folders are now `result/`, `sources/`, `context/`. Per-section review files, outline scaffolding, fit/gap analyses, requirements traceability matrices, sprint and decision logs, and other writing-phase artefacts have been removed; everything generalisable from them was harvested into `context/lessons-learned.md` first. CLAUDE.md was rewritten for the feedback-driven model. Workflow skills (`/write-section`, `/review-chapter`) and the parallel `AGENTS.md` for Codex still reflect the old generate-then-review pipeline and need a follow-up pass.
- **2026-05-04 supervisor meeting.** Plain-prose mandate (Rule 0); em-dash ban; anchor names locked to English (Efficiency, Trust/control, Adaptability); the four Trust/control actions named inline ("inspect, modify, accept, or reject"); RP abbreviation; "builds and evaluates" verb pair for the thesis-artefact relationship; "metrics" preferred over "measures"; non-coining of compound terms; chapter-synthesis hedge sentence; demand-for-artefact framed jointly across Admmit and coordinators (not one-sidedly).

## Open work

- **Plain-prose pass against Rule 0** across all drafted sections. The supervisor specifically flagged Ch 2.1–2.4 and Ch 3.1–3.7; the remaining chapters share the same patterns or were drafted after the supervisor's directives landed and need a lighter pass.
- **Process pending per-paragraph feedback** in `feedback-app/state.json`.
- **Spine sync.** Compare each chapter's actual argument against `context/thesis-spine.md`; update the spine if a chapter has shifted.
- **Workflow follow-up.** Decide whether to update or remove `.claude/skills/write-section/`, `.claude/skills/review-chapter/`, the agents under `.claude/agents/`, and the parallel `AGENTS.md`. They are stale under the new model.
