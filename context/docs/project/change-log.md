# Change Log — Ressursplanlegger

> Source-of-truth for §5.5 (Deviations from Plan). Two confirmed deviations from the original plan, both due to time constraints in the bachelor timeframe.

---

## D11 — Real-time sick-leave replanning dropped

- **Before:** Original scope included real-time replanning when a driver calls in sick — the system would partially resolve the affected day's plan, keeping unaffected assignments and redoing only the disturbed sub-plan.
- **After:** Sick-leave handling is supported as a hard-constraint update (a driver flagged unavailable becomes unschedulable in subsequent solver runs) but real-time partial replanning is not implemented. The coordinator must trigger a full re-solve manually.
- **Reason:** Time constraints. Partial-resolve semantics — what to keep, what to redo, how to bound the disturbance — turned out to require its own iteration that the project schedule could not absorb after iterations 1–8.
- **Impact:** Anchors §6.3 (Future Work) item on real-time replanning. Listed in §5.5 (Deviations from Plan) as one of two confirmed deviations. Does not affect the locked anchors directly — Effektivitet, Tillit/kontroll, and Tilpasningsdyktighet are tested under the implemented scope.

---

## D12 — User testing with traffic coordinators dropped

- **Before:** Original plan included a user-testing phase with three traffic coordinators walking through the override flow on a populated planning day, with think-aloud feedback recorded for the design.
- **After:** No formal user testing was conducted. Override-flow validity rests on requirements traceability + designer judgement informed by the seven brief stakeholder consultations (~15 min each).
- **Reason:** Time constraints + coordinator availability. Recruiting three coordinators for a walkthrough session within the project timeline did not materialise.
- **Impact:** Anchors §5.4 L8 (no user testing with coordinators) — the most consequential limitation for the Tillit/kontroll anchor. Listed in §5.5 (Deviations from Plan). Forwarded to §6.3 (Future Work) as a near-term post-thesis activity. The thesis's claims about HITL design are bounded by this gap and must be qualified accordingly throughout §5.1.2.