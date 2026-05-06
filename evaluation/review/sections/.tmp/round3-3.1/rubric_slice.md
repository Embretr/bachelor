### Chapter 3 — Methodology

**An A methodology chapter:**
- **Origin story (§X.1):** Opens with a paragraph naming how the project began — Admmit's bachelor task, the team's own initiative in contacting coordinators, HITL as Admmit mandate from project start (validated by interviews, not introduced by them). Reads as a story, not a specification.
- **DSRM applied step-by-step:** Method Theory section maps Peffers' six DSRM activities to this specific project, one bullet per activity. Each bullet is 2–4 sentences naming what was actually done. (See `evaluation/reference-thesis-analysis.md` §11.5 for format.)
- **Named iterations (4–6):** Iterative Development Process contains at least four named iterations with descriptive titles (e.g., *Single-engine baseline*, *Constraint generalisation*, *Multi-engine selection*). Each iteration follows tried / why / what happened (positive AND limitations) / learned / next. Honest about failure. Each iteration carries an inline origin label (interview-driven / Admmit mandate / designer-technical) per §12.0.5.
- **Evaluation framework separate from validity:** A dedicated sub-section describes how the artefact is tested (synthetic dataset design, multi-engine "How-not-Of" benchmark) — distinct from Validity and Reliability which addresses the research's epistemic limits.
- Research paradigm is stated and justified in one clear paragraph — not just named
- DSR is connected to Ressursplanlegger explicitly: the artefact, the evaluation, the iteration
- Interview methodology is described precisely enough that it could be replicated
- Participant selection is justified: why these 7 companies, why traffic coordinators specifically
- Validity and reliability section is honest: acknowledges self-selection bias, small sample, and author affiliation with Admmit
- Every methodological choice has a "because" — not just "we chose semi-structured interviews"

**Red flags that signal B or lower:**
- DSR is described generically without connecting it to this specific project
- "7 interviews were conducted" without explaining how companies were selected
- No discussion of validity or limitations of the method
- System development process is absent or described as a sprint diary


---
## Cross-Chapter A Criteria

These apply to the thesis as a whole:

**Argument coherence:**
- The thesis spine (context/thesis-spine.md) is traceable chapter by chapter
- No chapter contradicts another
- The conclusion follows logically from the findings and discussion

**Citation quality:**
- Primary sources preferred over secondary sources
- No citation for a claim that is common knowledge in the domain
- No claim left uncited that requires support
- Every citation in text appears in references.bib

**Language:**
- No hedging that weakens claims that have evidence ("it seems to be", "could possibly")
- No overclaiming that goes beyond evidence ("proves that", "definitively shows")
- No passive voice used to hide agency where agency matters ("mistakes were made")
- Consistent use of glossary.md terminology throughout

**Academic integrity:**
- All quotes are in quotation marks with page number
- Paraphrased content is cited
- The system is not described as solving problems it was not tested against

---


---
## Cross-chapter A-markers (source: ChatSSB 2025)

Structural patterns from a verified A-grade NTNU CS bachelor:
- Three locked anchors threaded from Ch 1 through to Ch 6 — synonyms are flagged
- Origin story in Method §X.1 grounding design choices in stakeholder dialogue
- Named iterations with descriptive titles in the development section
- Limitations as named sub-subsections, each analysed for impact
- Deviations section making plan-vs-reality differences explicit
- Conclusion that quotes each RQ verbatim and answers discretely
- Forward references in Ch 1 that pay off in their target chapter
- Backward references in Ch 5/6 that close loops opened in Ch 1
```

### 8.6 — `evaluation/evaluation.md`

For each chapter checklist, add a verifier item:

```
- [ ] Anchor reference: this chapter references the three anchors (Effektivitet, Tillit/kontroll, Tilpasningsdyktighet) where the spine requires it. Specifically:
  - Ch 1: all three are defined verbatim
  - Ch 5: each Primary Findings sub-section is named after exactly one anchor
  - Ch 6: each RQ answer connects back to the anchor it serves
```

Synonyms or paraphrases of anchor names are checklist failures.

### 8.7 — `.claude/agents/writer.md`

Add a "Required cross-chapter coherence checks" section near the top:

```
Before producing your section, verify:

1. Anchor reference — does this section reference one of the three locked anchors (Effektivitet, Tillit/kontroll, Tilpasningsdyktighet) where the spine requires it? In Ch 1 you are DEFINING them; in Ch 5/Ch 6 you must ORGANISE findings under them. Use the locked names verbatim — no synonyms.
2. Theory→use trace — if introducing a theoretical concept, plan where it reappears in analysis. If it does not reappear, do not introduce it.
3. Forward/backward links — explicit cross-references where the spine demands.
```

### 8.8 — `.claude/agents/red-thread.md`

Add to the existing checklist:

```
- Does each section reference an anchor concept (using the locked name verbatim) where the spine requires it?
- Are forward references made in earlier chapters paid off in later ones?
- Are backward references in Ch 5/6 closing loops opened in Ch 1?
- Are limitations in Ch 5 named as sub-subsections (not buried in paragraphs)?
- Does the Conclusion quote each sub-question verbatim and answer discretely?
```

### 8.9 — `.claude/agents/quality.md`

Add a "Reference-thesis A-markers" section pointing to `evaluation/reference-thesis-analysis.md` §7. Instruct the reviewer to score whether the section under review exhibits the relevant patterns from that list and to flag drift from the locked anchor names as a critical issue.

### 8.10 — `.claude/skills/write-section/SKILL.md`

In Step 1c (the readiness gate), extend the existing `MUST ANCHOR` check so that:
- The marker's anchor tag must match one of the three locked anchor names verbatim. A `MUST ANCHOR` pointing to a synonym, paraphrase, or unknown concept is a hard fail.
- For Ch 5 sections: each sub-section must have a `MUST ANCHOR` marker tied to exactly one of the three anchors.
- For Ch 6 sections: each RQ-answer paragraph must have a `MUST TRACE` marker pointing to the originating Ch 5 sub-section AND naming the anchor.

In Step 5 (review agents), add `evaluation/reference-thesis-analysis.md` §7 to the files-loaded list for Agent 1 (coherence) and Agent 2 (quality).

This change is scoped to existing marker syntax — no new parsers needed.

### 8.11 — `CLAUDE.md`

Add a new entry under "Critical Workflow Rules":

```
### 4. Anchor Concept Coherence

The three anchor concepts (Effektivitet, Tillit/kontroll, Tilpasningsdyktighet) defined in `context/thesis-spine.md` are the spine of the thesis argument.

- Ch 1 MUST define them verbatim
- Ch 5 MUST organise its Primary Findings under them (one sub-section per anchor)
- Ch 6 MUST connect each RQ answer to the anchor it serves
- Other chapters MUST reference at least one where structurally relevant

Drift from the locked names — synonyms ("kontroll" alone, "fleksibilitet", "skalerbarhet") or paraphrases — is a critical issue. Reviewers must flag drift; writers must use the locked names verbatim.
```

### 8.12 — One-time outline audit (after locking anchors)

Do a one-pass review of `context/outline.md` to ensure every section's ¶-plan that needs an anchor has a `MUST ANCHOR` marker pointing to the right one. ~30 minutes. Must happen BEFORE writing Ch 5 or Ch 6 — those chapters depend most on anchor coherence.

---

