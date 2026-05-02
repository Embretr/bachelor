# Risk Log — Ressursplanlegger

> Documents identified risks, their likelihood, impact, and mitigation.
> Referenced in Chapter 3 (Methodology) and Chapter 5.5 (Limitations).
> Owner: Both — update as new risks are identified or resolved.

---

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation | Status |
|----|------|:----------:|:------:|------------|--------|
| R-01 | Algorithm produces poor-quality plans for real-world data | Medium | High | Human override always available; coordinator remains in control | ⬜ Open |
| R-02 | Traffic coordinators unwilling to adopt a new system | Low | High | Co-design informed by interviews; system reduces, not replaces, coordinator work | ⬜ Open |
| R-03 | Tacit knowledge cannot be adequately formalised | High | Medium | Explicitly acknowledged as a limitation; human-in-the-loop preserves tacit decision-making | ⬜ Open |
| R-04 | Insufficient interview sample to generalise findings | Medium | Medium | 7 companies across different sizes and regions; limitations discussed in Ch 5.5 | ⬜ Open |
| R-05 | System not deployed in production — no real-world performance data | High | Medium | Identified as a limitation; future work includes production pilot | ⬜ Open |
| R-06 | Scope creep — adding features beyond thesis scope delays writing | Medium | Medium | Scope frozen in scope.md; new features go to "future work" | ⬜ Open |
| R-07 | Time pressure — thesis writing starts late, reducing revision cycles | Medium | High | Context documents prepared in advance; structured workflow with per-section drafting | ⬜ Open |
| R-08 | Optimisation engine performance insufficient for realistic problem sizes | Low | Medium | Three engines available; benchmarking framework identifies limits; limitations documented | ⬜ Open |
| R-09 | Invoicing gap blocks adoption discussion | Medium | Low | Acknowledged as out of scope; discussed as adoption barrier in Ch 5.3 | ⬜ Open |
| R-10 | Researcher bias — developers evaluate their own system | High | Medium | Structured requirements traceability; interview-grounded evaluation criteria; limitations discussed in Ch 5.5 | ⬜ Open |

**Likelihood:** Low / Medium / High
**Impact:** Low / Medium / High
**Status:** ⬜ Open / ✅ Resolved / ⚠️ Materialised

---

## Risk Events (Materialised Risks)

No risk in the register above materialised as a discrete event during the project. The risks remain Open as ongoing considerations addressed structurally (HITL preserves coordinator authority for R-01/R-02/R-03; sample-size, deployment, and bias risks R-04/R-05/R-10 are named explicitly as L1–L11 limitations in §5.4; scope and time risks R-06/R-07 were managed by freezing scope in `scope.md` and following the per-section drafting workflow).

---

## Notes for Thesis Writing

- Risk log entries are referenced in Chapter 3.5 (Validity and Reliability) and Chapter 5.5 (Limitations)
- Do not overstate risks that were mitigated — describe them accurately
- Materialised risks are more credible in the limitations section than hypothetical ones
