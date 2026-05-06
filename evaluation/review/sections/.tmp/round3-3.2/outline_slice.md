# Thesis Outline — Ressursplanlegger

> Claude reads this before writing any chapter.
> Contains section-level outlines with content notes and target lengths.
> Update as structure evolves — but keep thesis-spine.md consistent with changes.

---

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

**3.2 Method Theory — DSR + DSRM Applied** (~2 pages, expanded per §11.5)

- ¶1: Brief DSR reminder + alternative paradigms briefly considered. One to two sentences each on positivist and interpretivist alternatives and why DSR fits the artefact-plus-knowledge structure of this work.
  MUST CITE: Hevner — DSR foundation
  MUST CITE: IS research paradigms (Orlikowski & Baroudi)
- ¶2: Introduce DSRM (Peffers six-step) as the structured framework operationalising DSR for this thesis.
  MUST CITE: Peffers — DSRM
- **DSRM Applied bullets** — each of the six DSRM activities gets one bullet of two to four sentences applied to this specific project (per §11.5, the single most copyable A-grade move):
  - **Problem Identification and Motivation:** the resource-utilization visibility-gap finding from interviews + Admmit's mandate motivated formalising algorithm-assisted planning. The problem is described concretely in §4.1 and discussed in §5.1.1.
  - **Objectives of a Solution:** locked anchor concepts — Efficiency (overtime / idle time / load balance), Trust/control (coordinator authority via inspect / modify / accept / reject), Adaptability (cross-company adaptability via configurable weights and rules).
  - **Design and Development:** algorithm-assisted planning platform with multi-engine solver layer (heuristic / constraint solver / metaheuristic) and drag-and-drop human-in-the-loop timeline. Built across eight named iterations described in §3.5.
  - **Demonstration:** synthetic-dataset multi-engine benchmark (described in §3.6) plus requirements traceability matrix as the coverage check.
  - **Evaluation:** what the artefact tests is *how* solver approaches compare under realistic constraint combinations — a methodologically independent test of how-not-of per §12.0.5. What it does not test (production deployment, real-world utilization gains, user-tested override flow) is forwarded to §5.4 limitations.
  - **Communication:** this thesis itself + recommendations to Admmit on deployment and configurability.

