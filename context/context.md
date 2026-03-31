# Thesis Context — Ressursplanlegger

> **IMPORTANT:** Keep this file up to date. Both authors and Claude rely on it.
> Paste this file at the start of every new Claude chat session.

---

## Identification

| Field | Value |
|---|---|
| **Title** | [FILL IN] |
| **Subtitle** | [FILL IN or remove] |
| **Institution** | NTNU Gløshaugen — Department of Computer Science (IDI) |
| **Program** | Data Engineering (Dataingeniør) |
| **Author 1** | Embret [LAST NAME] — primary responsibility: system development |
| **Author 2** | Mikael [LAST NAME] — primary responsibility: user research |
| **Supervisor** | [FILL IN] |
| **Submission deadline** | [FILL IN] |
| **Language** | English |
| **Citation style** | APA 7 |

---

## The System — What is Ressursplanlegger?

Ressursplanlegger is a web-based resource planning platform developed for traffic coordinators
(trafikkledere) in Norwegian transport companies. The platform displays assignments,
drivers, and vehicles in a unified interface. A scheduling optimisation algorithm
automatically generates a daily plan, which the traffic coordinator can review, manually
adjust, and approve. The goal is to replace manual, error-prone planning processes and
improve the utilisation of drivers and vehicles.

**The core problem Ressursplanlegger solves:**
Traffic coordinators in Norwegian transport companies currently assign jobs to drivers
manually, relying heavily on personal knowledge (tacit knowledge) about driver competence,
licence classes, working hours, and route familiarity. Existing systems (Timpex, Trimtex)
are slow, lack optimisation, and do not support capacity overviews. Ressursplanlegger automates
initial plan generation and provides the coordinator with tools to refine it.

---

## Research Question / Problem Statement

> [FILL IN — be precise. Example:]
> How can an algorithm-driven resource planning platform support traffic coordinators
> in Norwegian transport companies in assigning drivers and vehicles to assignments
> more efficiently than current manual processes?

Sub-questions:
1. [FILL IN]
2. [FILL IN]

---

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | [FILL IN] |
| Backend | [FILL IN] |
| Database | [FILL IN] |
| Algorithm | [FILL IN] |
| Hosting | [FILL IN] |

---

## User Research Summary

Seven semi-structured interviews conducted 4 March 2026 with traffic coordinators:

| # | Company | System | Scale |
|---|---|---|---|
| 1 | Bergen Bulk Transport | None (manual) | 8–20 drivers |
| 2 | Harlem Solutions | Opptur | Unknown |
| 3 | Norlog Lakselv | Timpex | Medium |
| 4 | Norlog Mo i Rana | Timpex + Admin | Medium |
| 5 | Norlog Tana | Trimtex | Small (far north) |
| 6 | Ottem | Own system | ~45 vehicles, 3 depts |
| 7 | Nordic Crane (Svein) | Own system | Crane + transport |

Full findings in `context/interviews-summary.md`.

---

## Scope — Short Version

See `context/scope.md` for the full list.

**In scope:** Planning interface, algorithm-generated plan, manual override, driver/vehicle profiles, sick-leave handling.

**Out of scope:** Driver mobile app, GPS tracking, billing/invoicing, multi-company SaaS, payroll integration.

---

## Current Chapter Status

| Chapter | Status | Owner | Notes |
|---|---|---|---|
| 1 — Introduction | Not started | Mikael | |
| 2 — Theory | Not started | Mikael | |
| 3 — Methodology | Not started | Mikael | |
| 4 — Findings | Not started | Both | |
| 5 — Discussion | Not started | Mikael | |
| 6 — Conclusion | Not started | Both | |

---

## What Claude Must NOT Do

- Invent references or citations — only use sources from `context/docs/method/literature-list.md`
- Claim the system has features not listed in `context/scope.md`
- Rephrase or alter the research question — use it verbatim from this file
- Use "we believe" or "we think" — use impersonal academic constructions
- Assume something has been tested unless it appears in `context/docs/requirements/requirements-traceability.md`
- Write content for the other author's chapter without being explicitly asked
