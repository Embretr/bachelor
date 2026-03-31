# Datamodell — Cephalo

> **Owner: Embret** — fill in all sections.
> Used when writing Chapter 4.4 (System Description).

---

## Entities

### Assignment (Oppdrag)
| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Primary key |
| [FILL IN] | | |

### Driver (Sjåfør)
| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Primary key |
| [FILL IN] | | |

### Vehicle (Kjøretøy)
| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Primary key |
| [FILL IN] | | |

### Plan
| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Primary key |
| [FILL IN] | | |

---

## Relationships

```
[Add Mermaid ER diagram here]

erDiagram
    ASSIGNMENT ||--o| DRIVER : "assigned to"
    ASSIGNMENT ||--o| VEHICLE : "uses"
    PLAN ||--|{ ASSIGNMENT : "contains"
    DRIVER }|--|{ COMPETENCE : "has"
```

---

## Notes
[Any constraints, indexes, or design decisions worth documenting]
