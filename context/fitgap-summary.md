# Fit/Gap Analysis — Existing TMS vs. Identified Needs

> **Owner: Mikael** — derived from interviews-summary.md and functional-requirements.md.
> Used in Chapter 4.3 (Fit/Gap Analysis) and referenced in Chapter 5.1 (Discussion).
> Compares what existing transport management systems provide against what traffic coordinators actually need.

---

## What is Being Compared

**Systems evaluated:** Timpex, Trimtex, Opptur, custom/manual systems (as used by the 7 interviewed companies)
**Requirements source:** Functional requirements derived from interviews (FK-01 through FK-42 in `context/docs/requirements/functional-requirements.md`)

---

## Fit — Needs That Existing Systems Address

| # | Need | How existing systems address it | Systems | Coverage |
|---|------|-------------------------------|---------|:--------:|
| F-01 | Order/assignment registration | Timpex, Trimtex, and Opptur all allow creating and storing transport orders | Timpex, Trimtex, Opptur | Full |
| F-02 | Invoicing and billing | All three commercial systems handle invoicing — identified by interviewees as the primary function of their current TMS | Timpex, Trimtex, Opptur | Full |
| F-03 | Driver notification | Some systems have driver-facing apps (Timpex Confirm, Opptur order app); others use phone calls | Timpex, Opptur | Partial |
| F-04 | Basic driver/vehicle data storage | All systems store some driver and vehicle information | All | Partial |
| F-05 | Assignment status tracking | Orders can be marked as completed for invoicing purposes | Timpex, Trimtex, Opptur | Partial |

---

## Gap — Needs That Existing Systems Do NOT Address

| # | Need (from interviews) | Gap description | Severity | Req ID |
|---|----------------------|-----------------|:--------:|:------:|
| G-01 | **Unified daily planning view** — see all assignments, drivers, and vehicles for a day in one timeline | No existing system provides this. Coordinators keep the overview in their heads or on paper. | **High** | FK-01, FK-11 |
| G-02 | **Algorithm-generated plan** — automatic assignment of drivers/vehicles to assignments | No existing system offers optimisation or automated plan generation. All assignment is 100% manual. | **High** | FK-03 |
| G-03 | **Conflict detection** — automated detection of overbooking, overtime, missing competencies | No existing system checks for scheduling conflicts. Coordinators must remember constraints from memory. | **High** | FK-24–FK-30 |
| G-04 | **Driver availability overview** — see who is working, on leave, or already assigned at any given time | Not available in any system. Coordinators track this mentally or via separate spreadsheets/phone calls. | **High** | FK-11, FK-12 |
| G-05 | **Competency and certification tracking** — store licence classes, ADR, crane certs with expiry dates | Timpex and Trimtex store basic driver data but do not track competencies or certifications with expiry. | **High** | FK-09, FK-10 |
| G-06 | **Capacity overview** — quickly see whether all assignments for a day are covered | No existing system provides a capacity or coverage dashboard. | **Medium** | FK-35 |
| G-07 | **Manual override of suggestions** — coordinator can adjust any algorithm suggestion | Not applicable (no system generates suggestions). But the need was stated clearly: any future system must allow full override. | **High** | FK-04 |
| G-08 | **Recurring assignments** — define assignments that repeat daily, weekly, biweekly, or monthly | Not supported. Coordinators re-enter recurring jobs manually or use copy-paste workarounds. | **Medium** | FK-05 |
| G-09 | **Sick-leave handling with replanning** — register absence and see its effect on the daily plan | No system links absence to assignment coverage. Coordinators must manually identify affected routes and reassign. | **Medium** | FK-12 |
| G-10 | **Driving/rest-time monitoring** — track how close drivers are to legal limits | No system provides this. Some coordinators use separate tachograph systems but not integrated with planning. | **Medium** | FK-30 |
| G-11 | **Vehicle maintenance tracking** — next service date, EU control, crane inspection | Not tracked in the TMS. Managed separately (spreadsheets, calendar reminders, or not at all). | **Low** | FK-15 |
| G-12 | **Utilisation metrics** — how efficiently are drivers and vehicles being used? | No existing system provides utilisation analytics. Managers have no data-driven visibility into fleet efficiency. | **Low** | FK-17, FK-37 |
| G-13 | **Multi-tenant / multi-department** — data isolation between companies or departments | Not applicable to most existing systems (single-company installations). Ottem noted the need for department-level separation. | **Low** | FK-32, FK-34 |
| G-14 | **System performance** — fast, responsive interface with concurrent users | Timpex and Trimtex are described as extremely slow when multiple users are logged in. Performance is a major pain point. | **High** | (non-functional) |

---

## Gap Summary by System

| System | Used by | What it does well | Critical gaps |
|--------|---------|-------------------|---------------|
| **Timpex** | Norlog Lakselv, Norlog Mo i Rana | Order management, invoicing, driver notification (Confirm app) | No planning, no optimisation, extremely slow, no capacity overview, no conflict detection |
| **Trimtex** | Norlog Tana | Basic order management | Same as Timpex but fewer features; slow |
| **Opptur** | Harlem Solutions | Order management, invoicing, driver app | Primarily a billing tool; no planning support at all |
| **Custom systems** | Ottem, Nordic Crane | Tailored to own operations | No standardisation, no optimisation, difficult to maintain |
| **Excel / manual** | Bergen Bulk Transport (+ elements at other companies) | Familiar, zero cost, flexible | No structure, no conflict detection, no scalability, knowledge locked in one person's head |

---

## The Core Gap

All existing systems focus on **what happens after the assignment is made** — order registration, invoicing, and delivery tracking. None of them address **the assignment decision itself** — who drives what, with which vehicle, and why.

This is the space Ressursplanlegger occupies: the gap between "an order exists" and "a driver is assigned." It is a planning and decision-support tool, not an order management or invoicing tool.

---

## Visualisation for Chapter 4.3

Consider presenting this as a feature coverage matrix:

| Capability | Timpex | Trimtex | Opptur | Custom | None | Ressursplanlegger |
|-----------|:------:|:-------:|:------:|:------:|:----:|:-----------------:|
| Order registration | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ (out of scope) |
| Invoicing | ✅ | ✅ | ✅ | Partial | ❌ | ❌ (out of scope) |
| Driver notification | ✅ | ❌ | ✅ | ❌ | ❌ | Planned |
| Daily planning timeline | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Algorithm-generated plan | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Conflict detection | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Driver availability view | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Competency tracking | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Manual override | N/A | N/A | N/A | N/A | N/A | ✅ |
| Recurring assignments | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Utilisation metrics | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Performance (speed) | ❌ | ❌ | ? | ? | N/A | ✅ |

This matrix makes the gap visually obvious: existing systems and Ressursplanlegger are complementary, not competing. They solve different problems.

---

## Implications for Discussion (Ch 5.1)

1. **Ressursplanlegger does not replace existing TMS** — it fills the planning gap. Companies would still need Timpex/Trimtex/Opptur for invoicing.
2. **Invoicing integration is the most requested missing feature** — multiple interviewees flagged this. Acknowledged as out of scope but critical for adoption.
3. **Performance is a differentiator** — if Ressursplanlegger is fast where Timpex is slow, that alone drives adoption interest.
4. **The gap is universal** — all 7 companies, regardless of size or current system, lack algorithm-assisted planning. The problem is industry-wide, not company-specific.
