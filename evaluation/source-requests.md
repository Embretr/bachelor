# Source Requests — Controlled Source Queue

> Purpose: track source needs before they become citations in the thesis.
> This file is a queue, not a bibliography. A source request can be discovered,
> scoped, and agent-reviewed here, but it is not usable in thesis prose until a
> human has read and approved the source.
>
> **Last update: 2026-04-23** — all prior requests (SRC-001 to SRC-005) were
> resolved through the structured literature sweep in `evaluation/source-scope.md`.
> Active queue is currently empty. New requests should be added as SRC-006 onward.

---

## Status Rules

| Status | Meaning | Thesis use |
|--------|---------|------------|
| `needed` | A claim needs support, but no concrete candidate has been selected. | Not usable |
| `candidate` | One or more sources have been suggested, but not reviewed. | Not usable |
| `agent-reviewed` | An agent has assessed fit, authority, and claim coverage. | Not usable |
| `approved-read` | Human has read and approved the source, it is marked `approved-read` in `context/docs/method/literature-list.md`, and BibTeX exists in `result/references.bib`. | Usable |
| `rejected` | The source or request was assessed and rejected with a reason. | Not usable |

Hard rule: `approved-read` is the only status that permits citation in thesis prose.
Agent review can promote a request to `agent-reviewed`, but never to
`approved-read`.

---

## Request Template

```md
### SRC-xxx — Short source need

| Field | Value |
|-------|-------|
| Status | `needed` |
| Section | X.Y |
| Claim that must be supported | ... |
| Desired source type | Peer-reviewed article / textbook / official documentation / industry report |
| Search terms | ... |
| Candidates | None yet |
| Agent assessment | Not reviewed |
| Human action | Find candidates, read selected source, approve/reject |
```

---

## Active Requests

*None. All previous requests were resolved — see `evaluation/source-scope.md` and `context/docs/method/literature-list.md`.*

---

## Resolved Requests (archive)

| ID | Short description | Resolution |
|----|-------------------|------------|
| SRC-001 | Trust in automation (Ch 2.2, 5.3) | Resolved: `lee2004trust` + `hoff2015trust` approved |
| SRC-002 | TMS / logistics software (Ch 2.3, 4.3, 5.3) | Resolved: `griffis2007tms` + `heinbach2022datadriven` + `cichosz2020digital` approved |
| SRC-003 | Semi-structured qualitative interviews (Ch 3.2, 3.3) | Resolved: `kvale2015interview` + `oates2022researching` + `braun2006thematic` approved |
| SRC-004 | Agile and iterative development (Ch 3.4) | Resolved: `larman2003iterative` + `beck2001manifesto` approved |
| SRC-005 | OR-Tools, CP-SAT, and solver literature (Ch 2.1, 4.5, 5.2) | Resolved: `googleortools2026cpsat` + `perron2023cpsatlp` + `rossi2006constraint` + `timefold2026solver` + `glover1986future` + `burke2017late` approved |
