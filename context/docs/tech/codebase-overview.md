# Codebase Overview — Ressursplanlegger

> Summary of the existing codebase for Claude to understand what has been built.
> Used when writing Chapter 4.4 (System Description) and for code-related tasks.
> Owner: Embret — fill this before Chapter 4 is written.
> Do not paste full source code — paste structure, key files, and what they do.

---

## Repository Structure

[FILL IN — paste the output of `tree -L 3` or describe the folder structure]

```
ressursplanlegger/
├── frontend/
│   ├── [FILL IN]
│   └── ...
├── backend/
│   ├── [FILL IN]
│   └── ...
├── algorithm/              ← [separate service or part of backend?]
│   └── ...
└── [other folders]
```

---

## Frontend

**Framework:** [FILL IN — React / Vue / Svelte / other]
**State management:** [FILL IN — Redux / Zustand / Context API / other]
**Key components:**

| Component | What it does |
|-----------|-------------|
| [FILL IN] | |
| [FILL IN] | |

**Main screens:**
- [FILL IN — e.g., "Plan view: shows the day's assignments and routes as a Gantt-style chart"]
- [FILL IN]

---

## Backend

**Framework:** [FILL IN — Express / FastAPI / Django / Spring / other]
**Structure:** [FILL IN — e.g., controllers / services / repositories]
**Key files / modules:**

| File / Module | What it does |
|--------------|-------------|
| [FILL IN] | |
| [FILL IN] | |

**Authentication:** [FILL IN — JWT / session / other]

---

## Database

**Type:** [FILL IN — PostgreSQL / MySQL / MongoDB / other]
**Hosting:** [FILL IN — local / cloud / which provider]
**ORM / query layer:** [FILL IN]

Key tables/collections:
- [FILL IN — e.g., assignments, drivers, vehicles, plans, users]

---

## Algorithm

**Location:** [FILL IN — part of backend? Separate service? External API?]
**Language/runtime:** [FILL IN]
**Key dependencies/libraries:** [FILL IN]

How it is triggered:
- [FILL IN — e.g., "POST /api/plan/generate calls the algorithm service with the day's assignments and available drivers/vehicles"]

---

## External Dependencies

| Library / Service | Why it is used |
|-------------------|---------------|
| [FILL IN] | |
| [FILL IN] | |

---

## What Is Implemented vs. Planned

| Feature | Status |
|---------|--------|
| Plan view / Gantt | [✅ / ⬜] |
| Manual assignment | [✅ / ⬜] |
| Algorithm integration | [✅ / ⬜] |
| Sick leave handling | [✅ / ⬜] |
| Driver profiles | [✅ / ⬜] |
| Vehicle profiles | [✅ / ⬜] |
| Authentication | [✅ / ⬜] |
| [FILL IN] | |
