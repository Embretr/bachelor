# Theoretical Framework — Cephalo

> **Owner: Mikael** — fill in before writing Chapter 2.
> For each theory: what is it, and how does it connect to Cephalo specifically.

---

## Vehicle Routing Problem (VRP)

**What it is:**
The VRP is an optimisation problem in which a set of vehicles must serve a set of
customers, minimising total cost subject to constraints. First formulated by
[Dantzig & Ramser, 1959].

**Relevant variants:**
- VRPTW (with time windows) — most relevant to Cephalo
- Multi-depot VRP — relevant if Norlog's multi-department structure is modelled
- [FILL IN other variants if relevant]

**How it connects to Cephalo:**
[2–3 sentences — how does the assignment planning problem in Cephalo map to VRP?
What are the "customers" (assignments), "vehicles" (drivers + trucks), and "cost" (billable hours)?]

**Key sources to find:**
- Toth, P., & Vigo, D. (Eds.). (2002). *The Vehicle Routing Problem*. SIAM.
- [FILL IN — add to referanser.bib once found]

---

## Resource Scheduling

**What it is:**
[2–3 sentences — general definition of resource scheduling in operations research]

**How it connects to Cephalo:**
[2 sentences — how is assigning drivers and vehicles a resource scheduling problem?]

**Key sources to find:**
- [FILL IN]

---

## Human-in-the-Loop (HITL) Automation

**What it is:**
Human-in-the-loop refers to systems where a human retains the ability to review,
correct, or override automated decisions before they take effect.

**Why it matters for Cephalo:**
[2–3 sentences — connect to the interview finding that all coordinators want to
maintain control, and to Ottem's explicit scepticism about full automation]

**Design implication:**
The system should present the algorithm's output as a suggestion, not a decision.

**Key sources to find:**
- [FILL IN — search "human-in-the-loop decision support systems" or similar]

---

## Transport Management Systems (TMS)

**What it is:**
[2 sentences — definition of TMS as a software category]

**Existing systems in the Norwegian context:**
| System | Used by | Key limitation |
|--------|---------|---------------|
| Timpex | Norlog (Lakselv, Mo i Rana) | Very slow with many users |
| Trimtex | Norlog Tana | Slow, limited features |
| Opptur | Harlem Solutions | Primarily a billing tool |

**Gap Cephalo addresses:**
None of the above systems include optimisation-based plan generation or structured
decision support for traffic coordinators.

**Key sources to find:**
- [FILL IN — look for TMS industry overviews or academic reviews]

---

## Design Science Research (DSR)

**What it is:**
[2 sentences — connect to metode/forskningsdesign.md]

**Key source:**
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in
  information systems research. *MIS Quarterly*, 28(1), 75–105.
