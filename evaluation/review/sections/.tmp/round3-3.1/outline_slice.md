## Evidence Marker Taxonomy

All ¶-plans use these markers. The deterministic checker greps for them. Each marker must be on its own indented line under the ¶.

| Marker | Meaning | Used in |
|--------|---------|---------|
| `MUST CITE:` | Academic source TYPE required (foundational textbook, locked theoretical anchor by surname, methodological tradition, etc.). The downstream source-fitting task resolves the type to a specific bib entry plus verified source notes. | Ch 2, 3 |
| `MUST EVIDENCE:` | Empirical / system evidence TYPE required (interview-derived theme, fit/gap item, architecture documentation, benchmark results, etc.). Resolved to specific extracted-content references at write-time. | Ch 4 |
| `MUST ANCHOR:` | Must explicitly connect to the RQ, thesis spine, an earlier chapter section, or a locked anchor concept. For Ch 5 sub-sections the value MUST be one of `Efficiency`, `Trust/control`, `Adaptability` verbatim. Synonyms ("kontroll" alone, "fleksibilitet", "skalerbarhet", "human control", "menneskelig overstyring") fail the readiness gate. | Ch 5 (every sub-section); other chapters where structurally relevant |
| `MUST TRACE:` | Must trace back to a specific section, finding, or limitation. For Ch 6 RQ-answer paragraphs the format is `§5.1.X (<anchor name>)` with the anchor name verbatim. | Ch 6 |
| `MUST GROUND:` | Must be grounded in a context source — TYPE-described — with detailed evidence delivered later. | Ch 1 |

**Source-independence note (locked):** The current state of `result/references.bib`, `context/docs/method/sources/raw/extracted/`, `context/interviews-summary.md` theme labels, and `context/docs/tech/` is draft. This outline is structured around the locked substance (anchors, RQ, SQs, L1–L12, ChatSSB-derived A-grade pattern, five-layer HITL, §12.0.5 origin map). Sources and evidence are fitted to the structure as a downstream task. Locked theoretical authors may be referenced by surname (Bainbridge, Hoff & Bashir, Miller, Parasuraman, Lee, Hevner, Peffers, Wieringa, Orlikowski & Baroudi, Braun & Clarke, Malterud) — surnames are stable even when bib keys change.

**3.1 Defining the Task** (~1.5 pages, NEW per §8.4 + §12.1)

Origin story — how the project began. Reads as a story, not a specification.

> **Supervisor calibration 2026-05-04** (full log: `context/docs/project/supervisor-feedback.md`):
> - The task description belongs at the top of the section. Open with what the project was — Admmit's task — before any framing about students, interviews, or process.
> - Do not call them "design choices" in this section. Frame the section as research that informs design; the design choices are made later, with the research as the input.
> - The word "brief" is unclear. Use concrete phrasing — "Admmit's bachelor task description", "the task offered by Admmit", or similar.
> - Grammar: when referring to the team in a possessive form, use "their", not "its".
> - Use "the companies interviewed" or "the seven companies" when referring to the interview sample, not the disembodied "interviews".
> - Do not present seven interviews as happening on a single day. The honest reconstruction: one interview at a time, with the team adjusting questions and reflecting between calls; vendor names like Timpex and Opter surfaced gradually through "what tools do you use" questions, with several companies describing mixes of tools rather than single-vendor adoption.
> - Strengthen the motivation for the choice to interview seven coordinators. The current draft reads as a decision presented without a reason. Name what the team needed the interviews to answer.
> - Do not jump from "seven interviews" straight to "two design choices were locked". The two are not in the same chain of causation; the connecting reasoning has to be visible.
> - Reframe the HITL and multi-tenant origin honestly: "after the interviews, the team agreed with what Admmit had set as requirements; Admmit had the requirements, and the interviews validated them" — not "regardless of what coordinators said, HITL was chosen". Admmit had the mandate; the interviews validated it.
> - Do not write "not in the interviews". The phrasing reads as dismissive or boss-like. State positively where the requirement actually came from.
> - Explain multi-tenant in plain language. One short sentence — one deployed system serving several customer companies, each company's data and configuration isolated from the others.
> - Drop the phrase "they validated but did not introduce". The framing is wrong; rewrite around the corrected origin story above.
> - Drop the meta-phrase "so the reader can tell apart". Awkward and unnecessary if the prose itself is clear.
> - Drop "every design choice traced through" if it has already been said earlier in the section. The text up to the HITL paragraph in the previous draft was largely repetition; cut.
> - When the section names the four Trust/control operationalisations, write the four actions in the prose — "inspect, modify, accept, or reject" — rather than "the four actions defined under Trust/control" or "the four operationalisations of Trust/control".
> - Simplify the Efficiency sentence. Whatever the precise wording becomes, it must be a sentence a reader with no prior exposure to the anchor concepts could read once and understand.
> - Drop "interview-driven analysis" as a compound. Use plain phrasing.
> - Read the whole section after drafting and ask: does the argument move forward in one direction? The previous draft read as cross-winds (a sailboat with wind from every direction). Sequence: task -> why interviews were needed -> how the interviews actually unfolded -> what they validated against Admmit's existing requirements -> bridge to method.

- ¶1: How the project began — Admmit's bachelor task offer to NTNU. The decision to accept the task and build Ressursplanlegger.
- ¶2: Stakeholder access — seven traffic coordinators contacted directly by the team on its own initiative (Admmit did not broker introductions). Phone interviews on a single day.
- ¶3: HITL as Admmit mandate from project start — explicitly stated by Admmit at the outset, validated by interviews but not introduced by them. The multi-tenant architecture follows from Admmit's customer structure, also Admmit-mandated.
  MUST GROUND: Admmit-mandate origin (HITL, multi-tenant) per §12.0.5 origin map
- ¶4: Bridge to method — story-driven framing. Every later design choice is traceable to this origin or to the seven-interview dialogue, with the §12.0.5 origin map distinguishing interview-validated from designer / Admmit-mandated / domain-knowledge-driven decisions.

