## Evidence Marker Taxonomy

All ¶-plans use these markers. The deterministic checker greps for them. Each marker must be on its own indented line under the ¶.

| Marker | Meaning | Used in |
|--------|---------|---------|
| `MUST CITE:` | Academic source TYPE required (foundational textbook, locked theoretical anchor by surname, methodological tradition, etc.). The downstream source-fitting task resolves the type to a specific bib entry plus verified source notes. | Ch 2, 3 |
| `MUST EVIDENCE:` | Empirical / system evidence TYPE required (interview-derived theme, fit/gap item, architecture documentation, benchmark results, etc.). Resolved to specific extracted-content references at write-time. | Ch 4 |
| `MUST ANCHOR:` | Must explicitly connect to the RQ, thesis spine, an earlier chapter section, or a locked anchor concept. For Ch 5 sub-sections the value MUST be one of `Effektivitet`, `Tillit/kontroll`, `Tilpasningsdyktighet` verbatim. Synonyms ("kontroll" alone, "fleksibilitet", "skalerbarhet", "human control", "menneskelig overstyring") fail the readiness gate. | Ch 5 (every sub-section); other chapters where structurally relevant |
| `MUST TRACE:` | Must trace back to a specific section, finding, or limitation. For Ch 6 RQ-answer paragraphs the format is `§5.1.X (<anchor name>)` with the anchor name verbatim. | Ch 6 |
| `MUST GROUND:` | Must be grounded in a context source — TYPE-described — with detailed evidence delivered later. | Ch 1 |

**Source-independence note (locked):** The current state of `result/references.bib`, `context/docs/method/sources/raw/extracted/`, `context/interviews-summary.md` theme labels, and `context/docs/tech/` is draft. This outline is structured around the locked substance (anchors, RQ, SQs, L1–L12, ChatSSB-derived A-grade pattern, five-layer HITL, §12.0.5 origin map). Sources and evidence are fitted to the structure as a downstream task. Locked theoretical authors may be referenced by surname (Bainbridge, Hoff & Bashir, Miller, Parasuraman, Lee, Hevner, Peffers, Wieringa, Orlikowski & Baroudi, Braun & Clarke, Malterud) — surnames are stable even when bib keys change.

---
