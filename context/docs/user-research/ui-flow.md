# UI Flow — Ressursplanlegger

> Describes the main screens and user flows as they are implemented.
> Used in Chapter 4.4 (System Description) when describing the interface.
> Owner: Embret (implementation) + Mikael (user perspective).
> Ground every screen in what is actually built, not what is planned.

---

## Main Screens

### 1. Plan View — `/ressursplanlegger` (Main Screen)

**What the traffic coordinator sees:**
A Gantt-style planning timeline. Employees are listed on the vertical axis; the current day's time is on the horizontal axis. Each assignment appears as a coloured block in the row of the assigned employee. Unassigned assignments appear in a sidebar panel on the left or below. A date picker allows the coordinator to navigate between days. The plan's status (draft / approved) is shown in the header. Conflict badges appear inline on assignments that have violations.

**Key actions available:**
- Drag an assignment block to a different employee row to reassign
- Click an assignment to open the detail panel
- Click "Generate plan" to trigger the algorithm (engine selector: greedy / OR-Tools / Timefold)
- Click "Approve plan" to confirm the current plan (sets all assignments to `approved`)
- Navigate to a different date via the date picker
- View active violations via a "Deviations" indicator in the header

**Date selection:** A date picker component in the page header. Clicking a date reloads the timeline for that day.

---

### 2. Assignment Detail Panel

**What the coordinator sees:**
A slide-over or modal panel showing full assignment details: customer, project, description, location, time window, priority, required vehicle type, and required competencies. The currently assigned employee and vehicle are shown with dropdown selectors for reassignment.

**Key actions:**
- Select a different employee from a dropdown filtered by competency match and availability for the assignment's time window
- Select a different vehicle from a dropdown filtered by type and active status
- Edit assignment fields (description, time window, priority)
- Save changes or cancel

**Validation:**
Soft-warning behaviour. If the selected employee already has an overlapping assignment, or lacks a required competency, a warning badge appears on the assignment after saving — but the system does not block the save. The coordinator has final authority. Hard constraint violations are shown clearly but are not enforced as blocking errors.

---

### 3. Employee Profile — `/ansatte/[id]`

A dedicated page per employee. The coordinator can view and edit:
- Personal details (name, role, department, phone, email)
- Employment percentage and contracted hours per week
- Default assigned vehicle
- Work schedule (per weekday: start time, end time, available flag)
- Time-off periods (vacation, sick leave, other) — add/remove entries
- Certifications (licence class, expiry date, validity)
- Competencies (add/remove from company-defined competency list)
- Assignment history and utilisation percentage

---

### 4. Vehicle Profile — `/kjoretoy/[id]`

A dedicated page per vehicle. The coordinator can view and edit:
- Vehicle details (name, type, capacity, department)
- Status: active / maintenance / out_of_service (with immediate effect on algorithm exclusion)
- Upcoming dates: next service, EU control, crane inspection, lease expiry
- Required competencies (what certifications a driver must have to operate this vehicle)
- Attached trailers
- Utilisation percentage

---

### 5. Algorithm Result Review

The algorithm output appears directly in the planning timeline (`/ressursplanlegger`). After the algorithm runs, the timeline updates to show the suggested employee and vehicle for each assignment. The coordinator sees the same Gantt view — there is no separate "algorithm result" screen. A solution score (scheduled %, hard violations, soft score) is shown in a summary panel after the run. The coordinator can accept the plan as-is, adjust individual assignments, or re-run the algorithm.

---

### 6. Deviation Viewer — `/avvik`

A table listing all active constraint violations for the current company. Each row shows:
- Violation type (overbooking, missing competence, overtime, etc.)
- Affected assignment (customer, project, date)
- Affected employee or vehicle
- Suggested resolution (if applicable)

The coordinator can click through to the affected assignment to resolve the violation.

---

### 7. Dashboard Overview — `/oversikt`

A summary page showing:
- Today's plan status (how many assignments are scheduled / unassigned / approved)
- Employee utilisation chart (Recharts bar chart)
- Vehicle utilisation chart
- Upcoming certification expiries
- Recent constraint violations

---

### 8. Settings — `/innstillinger`

User preferences: language (Norwegian / English), timezone, notification settings (conflict alerts, email notifications), and two-factor authentication toggle. Company settings: company name, industry type, number of employees.

---

## Navigation Structure

The application uses a persistent sidebar navigation (visible on all dashboard pages):

```
Sidebar
├── Ressursplanlegger  → /ressursplanlegger  (Main planning timeline)
├── Oversikt           → /oversikt           (Dashboard)
├── Alle oppdrag       → /alle-oppdrag       (Assignment list view)
├── Ansatte            → /ansatte/[id]       (Employee profiles)
├── Kjøretøy           → /kjoretoy/[id]      (Vehicle profiles)
├── Avvik              → /avvik              (Deviation viewer)
├── Optimalisering     → /optimalisering-historikk  (Optimisation history)
└── Innstillinger      → /innstillinger      (Settings)

Auth pages (no sidebar):
├── /login
├── /register
└── /accept-invitation
```

---

## Screens Not Yet Implemented

| Screen | Status | Notes |
|--------|--------|-------|
| Driver mobile app | ⬜ Out of scope | Drivers are notified through external channels |
| GPS / route tracking | ⬜ Out of scope | No live location data |
| Weekly / monthly planning view | ⬜ Not implemented | Planning is per-day only |
| Billing / invoicing | ⬜ Out of scope | No financial module |
| Integration with Timpex / Trimtex | ⬜ Out of scope | No external system connectors |
