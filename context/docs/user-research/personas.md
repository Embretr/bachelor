# User Personas — Ressursplanlegger

> Describes the primary users the system is designed for.
> Used in Chapter 4.1 (Interview Findings) and Chapter 4.4 (System Description).
> Owner: Mikael — derived from interviews-summary.md.
> Do not invent personas — all details are grounded in interview findings.

---

## Primary User: Traffic Coordinator (Trafikkleder)

**Role:** Plans and dispatches daily transport operations. The main user of Ressursplanlegger — the person who decides which driver takes which assignment with which vehicle, every day.

**Responsibilities:**
- Assigning drivers and vehicles to all assignments each day
- Handling sick leave and unexpected absences — finding replacement drivers, reassigning routes
- Maintaining awareness of driver availability, licence classes, competencies, and overtime status
- Knowing which drivers are experienced on which routes and with which customers
- Approving the final daily plan before drivers are notified
- Communicating assignment details to drivers (via app, phone, or push notification)

**Current tools (from interviews):**
- Timpex (Norlog Lakselv, Norlog Mo i Rana, Norlog Tana) — used for order management and invoicing, not for driver assignment
- Opter (Harlem Solutions) — order and invoicing system with driver notification app
- Own order systems (Ottem, Nordic Crane) — custom-built, no optimisation
- No system at all (Bergen Bulk Transport) — fully manual with phone calls and personal memory

Neither Timpex nor Opter generates assignment plans automatically — driver-to-assignment matching is performed manually in every interviewed company.

**Pain points (from interviews):**
- Current systems (Timpex in particular) are extremely slow, especially with multiple concurrent users
- No single view of all drivers, vehicles, and their availability — information is fragmented
- Must remember constraints from memory: who has which licence, who is experienced on which route, who is approaching overtime limits
- Sick-leave handling ranges from trivial (2–3 keystrokes) to a daily, time-consuming problem, depending on fleet size and route flexibility
- No capacity overview — cannot quickly see whether all assignments for a day are covered
- Assignment logic is entirely in the coordinator's head — if they are absent, no one else can plan effectively

**Attitude toward automation:**
Split across interviewees:
- **Positive:** Norlog Lakselv, Mo i Rana, Tana — open to algorithm-generated plans, especially for fixed/repeating routes
- **Sceptical:** Bergen Bulk Transport (cost concerns), Harlem Solutions (too much variability), Ottem (wants to maintain manual control)
- **Partially positive:** Nordic Crane — sees value but wants full override capability

Consensus across all: the system should **suggest a plan the coordinator can correct** — not replace the coordinator entirely.

**Technical proficiency:** Moderate. Comfortable using existing TMS (Timpex, Opter) and mobile apps for driver communication. Not developers — the interface must be learnable quickly. Several interviewees emphasised that low learning curve is a key adoption criterion.

**Typical workflow (current, without Ressursplanlegger):**
1. Arrive at work, review incoming assignments for the day (from order system, phone, or email)
2. Mentally assess available drivers: who is working today, who has the right licence, who knows the route
3. Assign each driver to assignments one by one, based on experience and memory
4. Check for conflicts manually: overtime limits, double-booking, vehicle availability
5. Notify drivers of their assignments (via app notification, phone call, or paper list)
6. Handle changes throughout the day: sick leave, cancellations, new urgent assignments — repeat steps 2–5

**Typical workflow (with Ressursplanlegger):**
1. Open the planning timeline for the day
2. Click "Generate plan" — algorithm assigns drivers and vehicles to all assignments
3. Review the generated plan: check for deviations flagged by the system
4. Manually adjust assignments where the coordinator's knowledge overrides the algorithm
5. Approve the plan
6. (Future) Drivers see their assignments on their own page

---

## Secondary User: Transport Manager (Transportleder / Admin)

**Role:** Oversees transport operations at a higher level. Responsible for fleet efficiency, compliance, and strategic decisions. Not involved in daily dispatch.

**Responsibilities:**
- Monitoring overall utilisation of drivers and vehicles
- Ensuring compliance with driving/rest-time regulations across the fleet
- Managing multiple departments or divisions (e.g., Ottem has 3 departments with separate coordinators)
- Making decisions about fleet size, driver hiring, and vehicle procurement
- Reviewing operational performance over time

**How they use the system:**
- Views dashboard with utilisation charts and capacity metrics — not the daily planning timeline
- Reviews completed plans and deviation logs to identify recurring problems
- Manages company settings, departments, and user access (when admin panel is built)
- Uses the system weekly or at key decision points, not multiple times per day

**Pain points (from interviews):**
- No aggregated view of how efficiently drivers and vehicles are used
- Difficult to identify patterns (e.g., recurring overtime in one department, underutilised vehicles)
- Reliance on the traffic coordinator for all operational knowledge — no visibility without asking

**Attitude toward the system:** Generally positive. Sees value in data visibility and decision support. Less concerned about daily usability, more about reporting and overview.

---

## Indirect User: Driver (Sjåfør)

**Role:** Receives assignments and executes routes. In the current system, the driver is not a user of the planning platform — they receive their assignments through other channels.

**Current notification methods (from interviews):**
- App with push notifications (Timpex Confirm, Opter order app)
- Direct phone call from the traffic coordinator (Norlog Tana, Bergen Bulk Transport)
- Paper-based assignment lists (some smaller operations)

**Interaction with the planning process:**
- Passive recipient — does not choose or decline assignments in the current workflow
- Communicates back to the coordinator only when problems arise (vehicle issues, delays, route problems)
- Prefers to receive assignments well in advance, not last-minute

**Future consideration:**
A driver-facing page within Ressursplanlegger is planned — drivers would see their own daily schedule, assigned vehicle, and assignment details. This page is **not yet implemented** and is **not in scope** for the thesis deliverable. It may be mentioned as future work.

---

## User Hierarchy and Access

| Role | Daily use | Planning access | Admin access | Data scope |
|------|:---------:|:---------------:|:------------:|:----------:|
| Traffic coordinator | Yes | Full — create, edit, approve plans | No | Own company |
| Transport manager | Weekly | Read-only overview and reports | Yes (when built) | Own company |
| Admin | As needed | None | Full | Own company |
| Driver | Daily (future) | Read-only — own schedule | No | Own assignments |

---

## Source

All persona details are traceable to `context/interviews-summary.md` (7 interviews, 4 March 2026).
No characteristics have been added that are not supported by interview data.