## 7. Transferable A-Markers (for review agents)

When reviewing one of our sections, look for these markers (each present = A-evidence; absent = consider whether intentional):

**Per chapter:**
- Ch 1: Are 3 anchor concepts named in §1.1 and reused later? Are RQs numbered and discrete?
- Ch 2: Does every theory subsection open with a definition? Is depth proportional to argumentative importance? Does each theory point reappear in Ch 4 or Ch 5?
- Ch 3 (our Method): Is there an origin-story paragraph? Is DSRM applied step-by-step? Are iterations named with descriptive titles? Is evaluation a separate sub-section from development?
- Ch 4 (our Findings): Are findings split by category (e.g. interview / artefact / process)? Is there a DSR artifacts mapping table? Are interview findings stated without interpretation?
- Ch 5 (our Discussion): Are findings organised under the anchor concepts from Ch 1? Are limitations named as sub-subsections (not buried)? Are deviations from plan explicit? Are recommendations grounded in implementation experience? Are ethics/societal implications a substantive sub-section, not a disclaimer?
- Ch 6 (our Conclusion): Is each sub-question quoted verbatim and answered discretely in one paragraph? Is Further Work concrete (each item names the limitation it addresses)?

**Cross-chapter:**
- Forward references in Ch 1 actually pay off in their referenced chapters
- Backward references close every loop opened in Ch 1
- The same three anchor concepts appear in Ch 1, Ch 4 evaluation, Ch 5 discussion, and Ch 6 conclusion
- No theoretical concept is introduced that does not reappear in analysis

---

### Chapter 2 (Theory, 8 pages)

**Structure:** flat hierarchy, definitions-first.
- §2.1 Large Language Models (8 sub-subsections — the core concept gets the most space)
- §2.2 REST API's (1.5 paragraphs)
- §2.3 Statistical Definitions (3 sub-subsections, each one paragraph)
- §2.4 Sustainability Awareness Framework (one paragraph defining the framework that returns in Ch 8)
- §2.5 Relevant Literature (5 sub-subsections, each one paragraph summarising a prior work)

**Pattern:** every sub-subsection opens with a definitional first sentence ("A Large Language Model (LLM) is a type of artificial intelligence based on a neural network..."). No throat-clearing.

**Sectional length is asymmetric on purpose.** §2.1 is the bulk because LLM is the central concept. Statistical definitions are short because they are background terms, not load-bearing.

**Relevant Literature done well:** for each prior work, one paragraph that says (a) what it is, (b) what its contribution is, (c) what its relevance to this thesis is. No padding, no exhaustive summarisation. The Original ChatSSB section is honest about overlap and difference.

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

