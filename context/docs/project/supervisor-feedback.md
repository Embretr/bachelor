# Supervisor Feedback Log — Ressursplanlegger

> Chronological log of NTNU supervisor directives. One entry per meeting.
>
> **Workflow:**
> 1. Log every directive here verbatim, dated, with the section or scope it touches.
> 2. Generalisable rules (those that apply beyond the immediate section) are mirrored to `evaluation/review/lessons-learned.md` so the writer + reviewer agents enforce them automatically. Cross-link both directions.
> 3. Section-specific calibration is mirrored to the relevant block in `context/outline.md` so the writer sees it at draft time.
> 4. Never delete entries. Strike through and date the correction if a directive is later revised.
>
> Owner: Mikael. Co-readable by Embret. Read at session start when working on a chapter the supervisor has commented on.

---

## 2026-05-02 — Ch 2 rewrite calibration (after Ch 2.3 / 2.4 first drafts archived)

Context: Ch 2 first draft archived 2026-05-01 under `evaluation/review/sections/archive/2026-05-01-ch2-supervisor-snapshot/`. Supervisor reviewed §2.3 and §2.4 of that snapshot and produced six directives covering Ch 2 broadly.

| # | Directive (verbatim) | Scope | Mirrored to |
|---|----------------------|-------|-------------|
| 1 | "Ikke alle har en TMS, generelt: vær forsiktig med å påstå ting." | Empirical scope of any claim about Norwegian transport / "the industry" | lessons-learned → *Empirical scope* rule |
| 2 | "Skille intervjuene fra teori, teori bør vel være rent teori? Viktig at hvert kapittel er som det skal være." | Ch 2 must stay source-anchored, no interview material | lessons-learned → *Chapter purity* rule (re-confirmed) |
| 3 | "Brå overgang mellom avsnitt: bør være bedre overganger." | Paragraph-to-paragraph flow, all chapters | lessons-learned → *Flow* rule |
| 4 | "Allerede eksisterende løsninger må nevnes." | When framing a problem space, name the live state-of-the-art | lessons-learned → *Coverage* rule + outline.md §2.3 |
| 5 | "Første definisjon av tms er omfattende løsning, andre paragraf virker det som en begrenset definisjon: Definisjoner må konsekvens brukes likt." | Definitional consistency within and across sections | lessons-learned → *Terminology* rule + outline.md §2.3 |
| 6 | "Istedenfor fit gap, som ikke alle vet hva er og kan bli uklart: Feks tabell. Hva finnes det og hva mangler." | Don't expose internal vocabulary in prose; replace fit/gap framing with a "what exists / what is missing" table | lessons-learned → *Reader accessibility* rule + outline.md §2.3 / §4.3 |

**Section-level calibration for the rewrite:**

- **§2.3 (TMS).** Define TMS in ¶1 and use the same scope in ¶2 and ¶3 (do not narrow without flagging the shift). Name actual TMS by vendor — Timpex and Opter are the real Norwegian systems used by interviewed companies; pair with international vendors that appear in the literature so the live market is anchored, not implied. Do not write that all transporters operate a TMS; several interviewed companies do not.
- **§2.4 (DSR).** Same purity and transition rules as §2.3. No interview material in this section.
- **Ch 4.3 (fit/gap).** Replace the in-prose term "fit/gap" with a table or "what exists / what is missing" framing on first use. The internal label can stay in planning files (`fitgap-summary.md`, outline markers) but should not surface unglossed in thesis prose.

---

## 2026-04-28 — Narrative framing for Ch 2 theory

| # | Directive | Scope | Mirrored to |
|---|-----------|-------|-------------|
| 1 | Trafikkoordinator (the human actor) must be introduced early in the narrative of every Ch 2 theory section, not as a reveal at the end. | All Ch 2 sections | lessons-learned → *Narrative framing* rule + writer.md "Actor early" |
| 2 | §2.1 must split into multi-resource / single-resource / valid driver, opening with a single-resource example from an adjacent domain to build intuition before introducing multi-resource complexity. | §2.1 paragraph structure | outline.md §2.1 ¶1–¶2 |