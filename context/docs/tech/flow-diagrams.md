# System Flow Diagrams — Ressursplanlegger

> Describes the main operational flows in the system.
> Used in Chapter 4.4 (System Description) and Chapter 5.
> Owner: Embret — fill this before Chapter 4 is written.
> Use Mermaid syntax — renders in GitHub and can be referenced in the thesis as figures.

---

## Flow 1: Assignment to Confirmed Plan

> The main flow: how an assignment enters the system and ends up as a confirmed driver assignment.

An assignment is created by the coordinator (or imported) with a date, time window, required vehicle type, required competencies, and priority. The assignment is stored in the database with status `planned`. The coordinator then triggers the optimisation algorithm for that date. The algorithm returns a suggested employee and vehicle for each assignment. The coordinator reviews the suggestions on the planning timeline, makes any manual adjustments, and approves the plan. Assignments move to status `approved`.

```mermaid
flowchart TD
    A[Coordinator creates assignment\nor imports job order] --> B[Assignment stored in DB\nstatus: planned]
    B --> C[Coordinator triggers\nalgorithm on date]
    C --> D[Algorithm fetches employees,\nvehicles, constraints from DB]
    D --> E[Algorithm returns\nsuggested assignments]
    E --> F[Planning timeline updated\nwith suggestions]
    F --> G{Coordinator\nreviews plan}
    G -->|Satisfied| H[Coordinator approves plan\nstatus: approved]
    G -->|Needs adjustment| I[Coordinator makes\nmanual changes]
    I --> J[System re-runs\nconflict detection]
    J --> G
```

---

## Flow 2: Manual Assignment Override

> What happens when the coordinator manually changes an algorithm-generated assignment.

The coordinator can override any algorithm suggestion at any time by clicking on an assignment in the timeline. A detail panel opens where the coordinator selects a different employee or vehicle. The available choices are filtered by competency match and availability. When the coordinator saves, the assignment is updated in the database and conflict detection reruns on the affected assignments. If a violation is detected (e.g. the selected employee is already occupied), a warning is shown — but the system does not block the save (soft-warning behaviour; the coordinator has final authority).

```mermaid
flowchart TD
    A[Coordinator clicks assignment\non timeline] --> B[Assignment detail panel opens]
    B --> C[Coordinator selects\nnew employee or vehicle]
    C --> D[Dropdown filtered by:\ncompetency match + availability]
    D --> E[Coordinator saves]
    E --> F[Assignment updated in DB]
    F --> G[Conflict detection\nreruns on affected assignments]
    G --> H{Violations\ndetected?}
    H -->|No| I[Timeline updates cleanly]
    H -->|Yes| J[Violation badge shown\non assignment in timeline]
    J --> K[Coordinator sees warning\nbut assignment is saved]
```

---

## Flow 3: Sick Leave Handling

> What happens when a driver calls in sick and their assignments need reassignment.

The coordinator registers a sick-leave period for the employee via the employee profile or the time-off management interface. The system marks the employee as unavailable for the sick-leave period. Assignments previously assigned to that employee and falling within the sick-leave window are not automatically reassigned — they remain assigned but gain a conflict flag (`missing_competence` or `incomplete` depending on whether the employee was the only match). The coordinator is notified of the affected assignments via the deviation view and can re-run the algorithm (which will now exclude the sick employee) or manually reassign.

```mermaid
flowchart TD
    A[Coordinator registers sick leave\nfor employee X] --> B[TimeOff record created in DB\nfor sick-leave period]
    B --> C[Employee X marked unavailable\nfor that date range]
    C --> D[Existing assignments for X\ngain violation flag]
    D --> E[Coordinator sees affected\nassignments in deviation view]
    E --> F{How to\nresolve?}
    F -->|Re-run algorithm| G[Algorithm excludes X\nand suggests replacements]
    F -->|Manual override| H[Coordinator manually\nselects replacement employee]
    G --> I[Coordinator reviews\nnew suggestions]
    H --> I
    I --> J[Assignments updated\nviolations cleared]
```

---

## Flow 4: Vehicle Becomes Unavailable

> What happens when a vehicle breaks down or enters maintenance.

```mermaid
flowchart TD
    A[Coordinator sets vehicle status\nto maintenance or out_of_service] --> B[Vehicle excluded from\nfuture algorithm runs]
    B --> C[Existing assignments using\nthis vehicle gain violation flag]
    C --> D[Coordinator sees affected\nassignments in deviation view]
    D --> E[Coordinator manually\nreplaces vehicle or re-runs algorithm]
    E --> F[Assignments updated]
```

---

## Flow 5: Authentication

```mermaid
flowchart TD
    A[User visits app] --> B{Session cookie\nvalid?}
    B -->|Yes| C[tRPC context resolves\ncompanyId from session]
    C --> D[User sees dashboard]
    B -->|No| E[Redirect to /login]
    E --> F[User submits credentials]
    F --> G[Better Auth validates\ncredentials]
    G --> H{Valid?}
    H -->|Yes| I[Session created in DB\ncookie set in browser]
    I --> D
    H -->|No| J[Error shown on login page]
```

---

## Notes for Thesis Writing

- Each diagram above should become a `\begin{figure}` in the LaTeX chapter
- Caption format: "Figure 4.X: [Description of what the flow shows]"
- Label format: `\label{fig:flow-[name]}`
- Reference in text before the figure appears: `\Cref{fig:flow-[name]} illustrates...`
