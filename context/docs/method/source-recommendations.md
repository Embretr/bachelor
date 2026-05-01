# Source Recommendations per Chapter

> **Purpose:** Independent assessment of which academic sources best fit each section's content, based on Google Scholar / web searches conducted 2026-05-01 against `context/outline.md` only.
> **Method:** Searched for each topic area in the outline. Filtered by citation count, recency, relevance to thesis substance (resource scheduling, HITL automation, DSR, qualitative methods, sustainability). Did **not** consult `result/references.bib`, `context/docs/method/sources/`, or `evaluation/` — this is a content-driven, not repo-driven, audit.
> **Status:** Recommendations only. Downstream source-fitting decides which to adopt and how to cite.

---

## Chapter 1 — Introduction

§1.1 grounds the thesis in Norwegian transport-sector facts. §1.5 narrative; no fresh citations needed beyond what Ch 2–5 supply.

### 1.1 Background and Motivation — empirical grounding

| Source | Why it fits |
|---|---|
| **Statistisk sentralbyrå (SSB) — *Carriage of goods by lorry* (godstransport med lastebil)** | Authoritative Norwegian official statistic on road freight volumes; the only legitimate source for "Norwegian transport-sector fact" anchoring §1.1 ¶1. Updated annually. |
| **SSB — *Cost index for road goods transport*** | Wage / overtime cost component is directly relevant to the overtime utilization claim. |
| **Arbeidstilsynet — *Regulations concerning working time in road transport*** | Regulatory grounding for the overtime / rest-period framing — 48h average / 60h max / 13h daily — directly relevant to §2.1 ¶3 utilization framing and §3.5.6 deviation taxonomy. |
| **Hovi, I. B., Hansen, W., Madslien, A. — TØI reports (most recent: TØI 1918/2022, *Framskrivinger for godstransport i Norge 2018–2050*; older: TØI 1052/2010 on freight market structure)** | Transport Economics Institute (TØI) is the canonical academic source on Norwegian freight transport. Hovi is a chief research economist with multiple highly cited reports. Cite a recent (post-2020) TØI report for current freight-market structure. |
| **Cichosz, Wallenburg & Knemeyer (2020) — *Digital transformation at logistics service providers: barriers, success factors and leading practices*** (Int. J. Logistics Management) | Recent, relevant review on logistics digitalisation that grounds the "why now" framing in §1.1 ¶4. (Note: confirm publication year via Scholar — multiple Cichosz papers exist; the 2020 IJLM article is the most-cited.) |

> §1.2–§1.4 take their substance from §2.2 (anchors), §3 (RQ/SQ are not external citations), and `context/scope.md` (in/out of scope).

---

## Chapter 2 — Theory

This chapter carries the bulk of the citations. Recommendations below are the strongest, most-cited, and most thesis-relevant academic anchors per section.

### 2.1 Resource Scheduling

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶1 Definitional textbook** | **Pinedo, M. L. (2022). *Scheduling: Theory, Algorithms, and Systems* (6th ed.). Springer.** | Foundational textbook, multi-edition, hundreds of citations across editions; standard reference in OR/IE | Single-resource → multi-resource framing in Pinedo's structure mirrors §2.1's adjacency-domain → Ressursplanlegger pedagogical move. Has chapters on machine, job-shop, personnel scheduling — ideal "open with a single-resource example" source. |
| **¶1 (adjacent domain)** | **Van den Bergh, J., Beliën, J., De Bruecker, P., Demeulemeester, E., & De Boeck, L. (2013). Personnel scheduling: A literature review. *European Journal of Operational Research*, 226(3), 367–385.** | Highly cited (~2,000+) review of personnel scheduling | Cleanest entry point for "personnel scheduling" as a tradition; supports the analogous-domains framing without forcing nurse-or-airline specifics. |
| **¶1 (adjacent domain — secondary)** | **Ernst, A. T., Jiang, H., Krishnamoorthy, M., & Sier, D. (2004). Staff scheduling and rostering: A review of applications, methods and models. *European Journal of Operational Research*, 153(1), 3–27.** | Annotated bibliography, very widely cited | Stronger taxonomy of staff scheduling sub-domains; older but still the canonical organising review. Use Pinedo + Ernst + Van den Bergh as a layered set. |
| **¶2 Multi-resource framing** | (Pinedo as above — Chapter on resource-constrained scheduling) | — | Pinedo §13–§16 cover multi-resource extensions. |
| **¶3 Utilization framing** | (Pinedo + Van den Bergh) | — | Both treat utilization metrics (overtime, idle time, balance) explicitly. |
| **¶4 Constraint programming foundations** | **Rossi, F., van Beek, P., & Walsh, T. (Eds.). (2006). *Handbook of Constraint Programming*. Elsevier.** (also: Foundations of AI Vol. 2) | 1,640 citations | Canonical CP reference. Older but still THE foundational handbook. Useful for hard/soft constraint vocabulary (§2.1 ¶4). |
| **¶4 (newer alternative)** | **Apt, K. R. (2003). *Principles of Constraint Programming*. Cambridge University Press.** | Highly cited textbook | Sometimes preferred for pedagogical clarity if Rossi handbook feels too encyclopedic. |
| **¶5 VRP delimit** | **Braekers, K., Ramaekers, K., & Van Nieuwenhuyse, I. (2016). The vehicle routing problem: State of the art classification and review. *Computers & Industrial Engineering*, 99, 300–313.** | Highly cited review (1,500+) | Standard cite for delimiting VRP versus assignment problems. The review itself uses Eksioglu et al. (2009) taxonomy — cite Braekers as the primary, Eksioglu as secondary if needed. |
| **¶6 Tabu search / metaheuristics** | **Talbi, E.-G. (2009). *Metaheuristics: From Design to Implementation*. Wiley.** | 3,261 citations | Comprehensive, modern handbook covering all metaheuristic families. Best single-source for §2.1 ¶6's tri-fold (heuristic / complete / metaheuristic) framing. |
| **¶6 (foundational — tabu specifically)** | **Glover, F., & Laguna, M. (1997). *Tabu Search*. Springer.** | Highly cited canonical book | Cite if the §4.5 metaheuristic family chosen is in fact tabu / its descendants; otherwise Talbi suffices. |

### 2.2 Human-in-the-Loop Automation

The five-layer HITL theory (Parasuraman → Bainbridge → Hoff & Bashir → Miller → Lee) is exceptionally well-anchored by the surnames already locked in the outline. Recommendations confirm and reinforce.

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶1 Parasuraman taxonomy** | **Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics — Part A: Systems and Humans*, 30(3), 286–297.** | **3,839 citations** | THE 10-level scale source. Locks the "level 5–6 (system suggests, human approves)" framing in §2.2 ¶1. Irreplaceable. |
| **¶2 Bainbridge frame** | **Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775–779.** | **1,800+ citations**; resurgent in AI ethics literature | Canonical operator-vs-owner asymmetry source. Cited in modern AI/HCI work as a foundational text on automation paradoxes. Still the right cite despite age. |
| **¶3 Hoff & Bashir** | **Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors*, 57(3), 407–434.** | Highly cited (1,500+) | Three-layer (dispositional / situational / learned) trust antecedent model, exactly the framing §2.2 ¶3 promises. Recent enough to be authoritative. |
| **¶4 Miller** | **Miller, T. (2019). Explanation in artificial intelligence: Insights from the social sciences. *Artificial Intelligence*, 267, 1–38.** | Highly cited (~2,500+) | Most-cited XAI paper from a human-factors angle. Right anchor for "explanation as interface" framing in §2.2 ¶4 and §5.1.2 ¶3. |
| **¶5 Lee & See** | **Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50–80.** | **4,170 citations** | Foundational trust-in-automation paper. Older than Hoff & Bashir but layered under it (as the outline correctly notes). Both should be cited — they are not substitutes. |

**Optional supplements** if §2.2 needs additional depth in specific paragraphs:

- **Endsley, M. R. (2017). From here to autonomy: Lessons learned from human–automation research. *Human Factors*, 59(1), 5–27.** — Out-of-the-loop performance problem; can layer with Bainbridge for §2.2 ¶2 if desired.
- **Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does automation bias decision-making? *International Journal of Human-Computer Studies*, 51(5), 991–1006.** — Automation bias (commission/omission errors). Relevant if §3.5.6 deviation-detection wants to ground "false-positive tuning is itself a coordination problem".

### 2.3 Transport Management Systems

This is the weakest section for academic sources — TMS is primarily defined in industry (Gartner, ARC, Forrester) rather than peer-reviewed literature. The outline trims §2.3 to ~1 page, which fits this reality.

| Recommended source | Citation strength | Why it fits |
|---|---|---|
| **Christopher, M. (2022 / 2016). *Logistics and Supply Chain Management* (5th or 6th ed.). Pearson.** | Standard logistics textbook, widely cited | Best academic-textbook anchor for TMS as a software category situated within SCM. |
| **Min, H. (2009). Application of a decision support system to strategic warehousing decisions. *International Journal of Physical Distribution & Logistics Management*, 39(4), 270–281.** (or similar IJPDLM/IJLM paper) | Field-standard journal | Use a peer-reviewed IJPDLM/IJLM article on TMS / decision support systems for logistics for the definitional ¶1 if Christopher is judged too textbook-heavy. |
| **Gartner. *Magic Quadrant for Transportation Management Systems* (most recent annual edition).** | Industry-standard, not academic | Acceptable as one secondary cite for the *category* definition, alongside an academic anchor. Most theses cite Gartner once for TMS landscape framing. |
| **Norwegian TMS context (§2.3 ¶2):** | — | No academic source — handled via interview-derived evidence per `MUST EVIDENCE`. |

> The outline's `MUST CITE: TMS as software category (definitional)` is realistically satisfied by a textbook + one industry report. There is no high-citation academic paper that defines "TMS" the way Hevner defines "design science".

### 2.4 Design Science Research

Locked surnames (Hevner, Peffers, Wieringa) all confirmed as the right anchors.

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶1 DSR three-cycle (foundational)** | **Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105.** | **~15,000+ citations** | The canonical DSR-in-IS paper. Defines the seven guidelines and the rigor/relevance frame. Irreplaceable. |
| **¶1 (three-cycle specifically)** | **Hevner, A. R. (2007). A three cycle view of design science research. *Scandinavian Journal of Information Systems*, 19(2), 87–92.** | Highly cited follow-up | Direct source for the "relevance / design / rigor" cycles named in §2.4 ¶1. Cite both Hevner 2004 and Hevner 2007 for the "three-cycle" framing — they are complementary, not redundant. |
| **¶2 DSRM six-step** | **Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45–77.** | **7,019 citations** | Defines the six DSRM activities. Mandatory cite for §2.4 ¶1 + §3.2 DSRM-Applied bullets. |
| **¶3 Validation vs evaluation** | **Wieringa, R. J. (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.** | Highly cited textbook | Defines the design-cycle / empirical-cycle distinction and validation-in-context. Right cite for §2.4 ¶3 and §3.6/§3.7. |

---

## Chapter 3 — Methodology

### 3.3 Data Collection

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶1 Semi-structured interviews** | **Kvale, S., & Brinkmann, S. (2015). *InterViews: Learning the Craft of Qualitative Research Interviewing* (3rd ed.). Sage.** | Foundational; multi-edition standard | Most-cited single source on the qualitative interview craft. Norwegian-origin author (Kvale, Aarhus/Aalborg) — fits Nordic academic context naturally. |
| **¶1 (alternative / IS-specific)** | **Oates, B. J., Griffiths, M., & McLean, R. (2022). *Researching Information Systems and Computing* (2nd ed.). Sage.** (or Oates 2006, 1st ed.) | Standard IS methodology textbook | Use *instead of or alongside* Kvale if the thesis wants an IS-specific methodology anchor. Given DSR is the framing, Oates may be the more natural cite. |
| **¶3 Interview-guide framework (optional)** | **Kallio, H., Pietilä, A.-M., Johnson, M., & Kangasniemi, M. (2016). Systematic methodological review: developing a framework for a qualitative semi-structured interview guide. *Journal of Advanced Nursing*, 72(12), 2954–2965.** | Highly cited (1,000+) | Direct cite for "interview-guide development" if §3.3 ¶3 wants to justify guide construction with a procedural source. Optional but strong. |

### 3.4 Data Analysis

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶1 Thematic analysis** | **Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.** | **440,000+ citations** | The single most-cited paper in qualitative methodology. Mandatory cite — six-phase TA process. |
| **¶1 (newer reflexive TA)** | **Braun, V., & Clarke, V. (2022). *Thematic Analysis: A Practical Guide*. Sage.** | Highly cited recent textbook | Cite alongside the 2006 paper if the thesis adopts reflexive TA explicitly. The 2022 textbook clarifies the method's evolution and is increasingly expected in recent qualitative research. |
| **¶1 (alternative — 2019 reflexion)** | **Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589–597.** | Highly cited | Useful intermediate cite if the 2022 book feels too long; clarifies why "reflexive TA" replaces "thematic analysis". |

### 3.7 Validity and Reliability

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶1 Malterud's four criteria** | **Malterud, K. (2001). Qualitative research: standards, challenges, and guidelines. *The Lancet*, 358(9280), 483–488.** | **5,207 citations** | Norwegian author (Malterud, UiB), high-impact journal. Names relevance / validity / reflexivity as standards — exact framing the outline expects. The "four criteria" phrasing in the outline likely refers to systematic reflection + relevance + validity + reflexivity; Malterud 2001 is sufficient. |
| **¶1 (supplement)** | **Malterud, K. (2012). Systematic text condensation: a strategy for qualitative analysis. *Scandinavian Journal of Public Health*, 40(8), 795–805.** | Highly cited | Optional companion if the analysis approach borrows from systematic text condensation rather than pure Braun & Clarke TA. |

> §3.2 (DSR / DSRM) cites the same Hevner / Peffers / Wieringa triplet as §2.4. Do not duplicate.
> §3.5 iteration narrative is empirical and self-grounding — no external citations needed beyond §3.5.4's `MUST ANCHOR: Effektivitet` (which traces, not cites).
> §3.6 Evaluation framework: Wieringa (2014) covers validation-vs-evaluation; do not re-cite if already in §3.2.

---

## Chapter 4 — Findings

§4.1–§4.4 + §4.6 + §4.7 are predominantly empirical (`MUST EVIDENCE`, not `MUST CITE`). §4.5 is the only section with required academic citations.

### 4.5 Optimisation Algorithm

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶3 Solver-engine (CP)** | **Rossi, van Beek, & Walsh (2006).** *Handbook of Constraint Programming*. (As §2.1 ¶4 — do not double-cite if already in Ch 2.) | — | Use as the foundation; cite the relevant chapter for the specific CP variant used. |
| **¶3 Solver-engine (CP-SAT specifically)** | **Perron, L., & Furnon, V. (2023). The CP-SAT-LP Solver (Invited Talk). In *Proc. CP 2023*, LIPIcs Vol. 280, Article 3.** | Recent, official Google CP-SAT reference | The cleanest academic citation for Google OR-Tools CP-SAT. Use this if the §3.5.3 constraint-programming engine is in fact CP-SAT. |
| **¶3 Solver-engine (metaheuristic)** | **Talbi (2009).** *Metaheuristics: From Design to Implementation*. (As §2.1 ¶6.) | — | Foundational metaheuristic textbook. |
| **¶3 (MIP — if used)** | **Wolsey, L. A. (2020). *Integer Programming* (2nd ed.). Wiley.** | Foundational IP textbook | Cite if any integer-programming formulation is used (assignment problems can also be formulated as MIPs). Not necessary if Pinedo + CP handbook + Talbi cover the engines. |
| **¶6 Algorithm limitations** | (No external cite — internal forward to §5.4 L9) | — | — |

---

## Chapter 5 — Discussion

§5.1 (Primary Findings under Anchors) re-cites the same Bainbridge / Hoff & Bashir / Miller triplet introduced in §2.2 — do not duplicate.

§5.2 / §5.4 / §5.5 / §5.6 are interpretive and self-grounding.

### 5.3 Sustainability and Ethical Considerations

| ¶ | Recommended source | Citation strength | Why it fits |
|---|---|---|---|
| **¶1 SusAF foundational** | **Becker, C., Chitchyan, R., Duboc, L., Easterbrook, S., Mahaux, M., Penzenstadler, B., et al. (2015). Sustainability design and software: The Karlskrona manifesto. In *ICSE 2015 — Companion Proceedings*.** | Highly cited; foundational | The manifesto behind SusAF's five-dimension framing. Cite as the conceptual root. |
| **¶1 SusAF main paper** | **Duboc, L., Betz, S., Penzenstadler, B., Akinli Kocak, S., Chitchyan, R., Leifler, O., Porras, J., Seyff, N., & Venters, C. C. (2020). Requirements engineering for sustainability: an awareness framework for designing software systems for a better tomorrow. *Requirements Engineering*, 25(4), 469–492.** | Highly cited, recent | THE canonical SusAF citation. Defines the question-based framework and the five dimensions. Mandatory if §5.3 uses SusAF. |
| **¶4 SDG framework** | **United Nations General Assembly. (2015). *Transforming our world: the 2030 Agenda for Sustainable Development* (Resolution A/RES/70/1).** | Official UN document | The authoritative source for the 17 SDGs. Cite directly to UN; do not cite secondary sources. |
| **¶4 (academic SDG-software bridge)** | **Penzenstadler, B., Betz, S., Venters, C. C., Chitchyan, R., Porras, J., Seyff, N., Duboc, L., & Becker, C. (2018). Everything is INTERRELATED: Teaching software engineering for sustainability. In *Proc. ICSE-SEET 2018*.** | Highly cited | Bridges SDG framework to software engineering practice. Useful if §5.3 ¶4 wants to map artefact effects to SDGs. |

---

## Chapter 6 — Conclusion

No fresh citations. All references trace back to §5.4 limitations, §5.1 anchor sub-sections, and the thesis spine.

---

## Summary — strongest A-grade sources by chapter

The single most defensible "A-grade source set" for this thesis, ranked by within-chapter centrality:

**Mandatory (every section that promises them):**

1. Pinedo (2022) — scheduling foundation
2. Parasuraman, Sheridan & Wickens (2000) — automation taxonomy
3. Bainbridge (1983) — operator-vs-owner asymmetry
4. Hoff & Bashir (2015) — trust calibration
5. Miller (2019) — explanation as interface
6. Lee & See (2004) — trust in automation
7. Hevner et al. (2004) + Hevner (2007) — DSR foundation + three-cycle
8. Peffers et al. (2007) — DSRM six-step
9. Wieringa (2014) — DSR methodology textbook + validation/evaluation
10. Braun & Clarke (2006) [+ 2022 textbook] — thematic analysis
11. Malterud (2001) — qualitative validity
12. Duboc et al. (2020) — SusAF
13. Becker et al. (2015) — Karlskrona Manifesto
14. UN A/RES/70/1 (2015) — SDGs

**Strongly recommended (best-fit support):**

15. Van den Bergh et al. (2013) — personnel scheduling review
16. Ernst et al. (2004) — staff scheduling annotated bibliography
17. Braekers, Ramaekers & Van Nieuwenhuyse (2016) — VRP review
18. Rossi, van Beek & Walsh (2006) — CP handbook
19. Talbi (2009) — metaheuristics
20. Kvale & Brinkmann (2015) [or Oates 2022] — interview methodology
21. Kallio et al. (2016) — interview-guide framework

**Empirical / contextual (Norwegian transport):**

22. SSB statistics (Carriage of goods by lorry; Cost index for road goods transport)
23. TØI report by Hovi et al. (most recent post-2020)
24. Arbeidstilsynet — working time regulations road transport

---

## Notes on completeness

- **Older foundational sources** (Bainbridge 1983, Lee & See 2004, Rossi et al. 2006, Glover & Laguna 1997, Ernst et al. 2004) are kept because they remain canonical. Citation count and continued use in 2020s–2024 publications confirm relevance. Replacing them with newer secondary sources would weaken the thesis.
- **Industry sources** (Gartner) acceptable only for §2.3 TMS-as-category, where no peer-reviewed equivalent exists. Use sparingly and pair with a textbook anchor.
- **Norwegian official statistics** (SSB, Arbeidstilsynet, TØI) are not "academic" but are the only legitimate sources for the empirical claims in §1.1 — academic transport-sector papers exist but rarely contain the specific overtime / load-balance figures the outline anchors require.
- **No source recommended below ~1,000 citations** unless it is recent (post-2020) and uniquely fits a specific paragraph (Perron & Furnon 2023; Duboc et al. 2020).
