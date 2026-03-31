# UI Flow — Ressursplanlegger

> Describes the main screens and user flows as they are implemented.
> Used in Chapter 4.4 (System Description) when describing the interface.
> Owner: Embret (implementation) + Mikael (user perspective).
> Ground every screen in what is actually built, not what is planned.

---

## Main Screens

### 1. Plan View (Main Screen)

**What the traffic coordinator sees:**
[FILL IN — e.g., "A Gantt-style view showing all drivers on the vertical axis and time on the horizontal axis. Each assignment appears as a coloured block. Unassigned assignments appear in a sidebar."]

**Key actions available:**
- [FILL IN — e.g., "Drag an assignment to a different driver row"]
- [FILL IN — e.g., "Click an assignment to see details and manually reassign"]
- [FILL IN — e.g., "Generate algorithm plan button"]
- [FILL IN — e.g., "Approve plan button"]

**Date selection:** [FILL IN — how does the coordinator select which day to view?]

---

### 2. Assignment Detail / Manual Assignment

**What the coordinator sees:**
[FILL IN]

**Key actions:**
- [FILL IN — e.g., "Select a driver from a dropdown filtered by availability and licence class"]
- [FILL IN — e.g., "Select a vehicle from available vehicles of the required type"]
- [FILL IN — e.g., "Save or cancel"]

**Validation:**
[FILL IN — what happens if an invalid assignment is attempted? Is the coordinator warned or blocked?]

---

### 3. Driver / Vehicle Management

[FILL IN — is there a screen for managing driver profiles? What can be edited?]

---

### 4. Algorithm Result Review

[FILL IN — how does the algorithm output appear? Is it different from the manual plan view?]

---

### 5. Sick Leave Registration

[FILL IN — how does the coordinator mark a driver as sick? What happens to their assignments?]

---

## Navigation Structure

[FILL IN — how are the screens connected? Top navigation, sidebar, tabs?]

```
[Main Plan View]
    ├── [Click assignment] → Assignment Detail
    ├── [Driver list] → Driver Profile
    ├── [Generate plan] → Algorithm runs → Plan View updates
    └── [Settings] → [FILL IN]
```

---

## Screens Not Yet Implemented

[FILL IN — list screens that are planned but not built, so Claude does not describe them as implemented]

| Screen | Status | Notes |
|--------|--------|-------|
| [FILL IN] | ⬜ Planned | |
