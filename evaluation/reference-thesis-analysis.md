# Reference Thesis Analysis — ChatSSB (NTNU 2025, A-grade)

> Read by: writer agents, review agents, and system maintainers (when updating spine, outline, rubric, agent prompts).
> Source: `context/docs/method/sources/raw/a-opg.pdf` — NTNU bachelor, computer science, May 2025, advisor Ali Alsam, graded A.
> Domain: LLM-based natural-language retrieval from SSB Statbank. Different problem domain from ours, **but** same study programme, same examination committee tradition, same DSR-based methodology, same NTNU formatting/expectations.

---

## How to Use This File

| If you are... | Read... |
|---|---|
| A writer agent for any chapter | §12 (project facts) + §3 (pattern for that chapter type) + §5 (argumentation moves) + §11 (prose/format conventions) |
| The red-thread reviewer | §12 + §4 (the five spine moves) + §6 (anti-patterns to flag) |
| The quality reviewer | §12 + §4 + §7 (transferable A-markers) + §11 |
| Updating spine, outline, rubric, agent prompts, SKILL.md, CLAUDE.md | §8 (12 sub-sections, one per file) |
| Sceptical that this generalises | §9 (what does not transfer automatically) |
| Just read this file for the first time | §12 first (so you know whose thesis this is) |

**Always-essential**: §12 (our project's locked anchors and domain context). Without it, all other guidance can be applied to the wrong project.

Token-efficient reading order: §12 → §4 → §8 are the highest-leverage. §3 is reference material — skip unless you're the agent for that specific chapter type.

---

## 1. Why This Source Is Worth Studying

| Property | ChatSSB | Ressursplanlegger | Match? |
|---|---|---|---|
| Programme | NTNU BSc Computer Engineering | NTNU BSc Data Engineering | ≈ same |
| Methodology | DSR + DSRM (Hevner; Peffers et al.) | DSR + DSRM | identical |
| Stakeholder | One organisation (SSB) shaping requirements | Multiple companies via interviews shaping requirements | similar shape |
| Artifact type | Web application + benchmarking framework | Web application + scheduling algorithm | similar shape |
| Validation | Quantitative benchmarks + qualitative user tests | Quantitative benchmarks + interviews + requirements traceability | similar shape |
| Length | 120 pages incl. front matter and appendix | Target ~80–100 pages | comparable |
| Outcome | A-grade | TBD | — |

**What that means:** structural and rhetorical patterns transfer with high confidence. Domain-specific content (LLM theory, Statbank specifics) does NOT.

---

## 2. Top-Level Structural Anatomy

```
Front matter      Abstract / Sammendrag / Preface / Task Description / TOC / Figures / Tables
Ch 1 Introduction and Relevance       (~3 p)
Ch 2 Theory and Relevant Literature   (~8 p)   — generic concepts + 5 prior-work paragraphs
Ch 3 Background                        (~6 p)   — CASE-SPECIFIC tech, APIs, existing solution
Ch 4 Method                            (~22 p)  — 4.1 Defining Task, 4.2 Method Theory, 4.3 Tech, 4.4 Iterative Dev, 4.5 Evaluation
Ch 5 Results                           (~16 p)  — 5.1 Scientific, 5.2 Engineering, 5.3 Administrative
Ch 6 Discussion                        (~10 p)  — 6.1 Findings, 6.2 Precautions, 6.3 Deviations, 6.4 Methodology, 6.5 Teamwork, 6.6 API Improvements, 6.7 Implementation
Ch 7 Conclusion and Further Work       (~3 p)
Ch 8 Societal Impact                   (~3 p)   — uses SusAF, 5 dimensions
Bibliography
Appendix (≈22 p)                        — search examples, code, raw test data, app screenshots, sprint milestones, time accounting, SusAD diagram
```

**Page-budget pattern:** Method dominates (~28 % of body). Theory is short and tight (~10 %). Discussion and Results combined ~32 %. Conclusion is short (3 p).

**Notable structural choices:**
- Theory and Background are **separate chapters**. Ch 2 = generic concepts (LLM, RAG, REST, statistical definitions, SusAF). Ch 3 = the specific case's surrounding tech (SSB org context, PxWebApi protocol, LangChain library). This separation lets theory stay portable and prevents the method chapter from drowning in tool descriptions.
- "Relevant Literature" is **inside Ch 2 (§2.5)** as five one-paragraph summaries of prior systems/papers — explicit positioning against existing work, not a separate "related work" chapter.
- Conclusion is **deliberately short**: it answers each RQ in one paragraph, then 1 page of Further Work. No padding.
- Societal Impact is its **own chapter**, anchored to the SusAF framework introduced in §2.4. Five sustainability dimensions (Social/Individual/Environmental/Economic/Technical), each ≈ half a page.

---

## 3. Per-Chapter Patterns

> **Notation in this section:** unqualified chapter numbers (e.g. "Ch 4 (Method)") refer to **ChatSSB's** structure (8 chapters). Prefixed names (e.g. "our Method", "our Findings") refer to **our thesis** (6 chapters). Specific names mentioned ("All at Once", "Stability/Efficiency/Security", "/navigation endpoint") are ChatSSB's vocabulary, used only as illustration.

### Chapter 1 (Introduction, 3 pages — ChatSSB)

**Move sequence:**
1. Domain hook — first sentence is concrete: "Statistics Norway (SSB), established in 1876, is a professionally autonomous institution responsible for...". No abstract preamble, no "in today's digital world".
2. Problem narrowing — paragraph 2 explains the specific friction (manual hierarchical navigation, 7000 tables, multi-step process).
3. Technology framing — paragraph 3 introduces LLMs as the candidate solution.
4. Project introduction — names the artefact (ChatSSB), states what it does in one sentence.
5. Forward-looking foreshadow — closes intro with "future improvements" (this telegraphs Ch 6.6's API recommendations).
6. **§1.1 Requirements** — three named anchors: **Stability, Efficiency, Security**. Each gets a 3-sentence definition. **These three names are referenced in every later chapter.**
7. **§1.2 Research Questions** — three numbered RQs explicitly linked to the requirements.
8. **§1.3 Acronyms** — bullet list.

**Strengths to imitate:**
- The first sentence is a concrete fact, not a generic statement.
- Three anchor concepts defined here, threaded throughout — a coherence engine.
- Multiple RQs are numbered and discrete; each is verifiably answered later.

**Anti-patterns we must avoid:**
- "The purpose of this thesis is to explore..." (their intro never says this).
- Burying the artefact name. They name ChatSSB on page 1.

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

### Chapter 3 (Background, 6 pages)

**Why this chapter exists:** to keep Ch 2 (theory) generic and re-usable, while still providing enough case-specific detail that Ch 4 can refer to "the /navigation endpoint" without re-introducing it.

**Content type:**
- §3.1 The organisation and its data (SSB; what APIs they have; the PxWebApi protocol; folder structure; existing UI)
- §3.2 The library/tool used to build (LangChain; specific components: BaseChatModel, Callbacks, Structured Output)

**Tone:** descriptive and technical. Heavy on figure references (folder diagram, API specifications, screenshots in appendix). Almost no citations because this is concrete fact-of-the-platform, not literature.

**Effect:** when Ch 4 says "we used the /tables/<id>/metadata endpoint with structured output via LangChain's withStructuredOutput()", the reader has the vocabulary and does not need it re-explained.

### Chapter 4 (Method, 22 pages — the largest chapter)

**Sub-structure:**
- §4.1 Defining the Task (origin story — 1.5 pages)
- §4.2 Method Theory (DSR/DSRM applied — 3 pages)
- §4.3 Choice of Technologies (4 short sub-subsections — 2 pages)
- §4.4 Iterative Development Process (NINE NAMED ITERATIONS — 12 pages, the bulk)
- §4.5 Evaluation (test setup — 3 pages)

**§4.1 Defining the Task — the origin-story move.** Tells how the idea emerged ("the authors' own experience navigating the SSB website"), how the stakeholder was approached ("initiated contact through the organization's general inquiry webpage. After seven days, a response was received"), and how requirements crystallised through that dialogue. **Reads like a story, not a specification.** This is rare and powerful — it makes every later design choice traceable to a real conversation, not an arbitrary decision.

**§4.2 Method Theory.** Defines DSR (citing Hevner, Gregor & Hevner). Names the three foundational cycles (relevance, design, rigor). Briefly contrasts DSR against positivist and interpretivist alternatives — shows they considered alternatives. Then DSRM (Peffers et al.) is given as a structured framework, and **each of the six DSRM steps gets one bullet that applies it to this project specifically**:
> - Problem Identification and Motivation: The problem was identified through observations that...
> - Objectives of a Solution: In consultation with SSB architects requirements for efficiency, stability, and security were defined.
> - Design and Development: A web application supporting user interaction was developed...

**This applied-bullet pattern is the single most copyable A-grade move.** It converts methodology theory into a verifiable mapping to the actual work. (See §8.4 for how to import this.)

**§4.3 Choice of Technologies.** One sub-subsection per major technology, each 1–4 sentences. Format: name → what it is → why it was chosen for THIS project. No deep dives; the deep dives live in Ch 3.

**§4.4 Iterative Development Process — nine named iterations.**

The names tell the story: 4.4.1 *All at Once* → 4.4.2 *From Query to Data* → 4.4.3 *Enhance Functionality While Maintaining Simplicity* → 4.4.4 *Absolute Constraints* → 4.4.5 *Tentatively Comparing LLMs* → 4.4.6 *Coming to Terms with LLM's Volatility* → 4.4.7 *Leveraging Language and Creating New Context* → 4.4.8 *A New Approach to Navigation* → 4.4.9 *Retry on Failure*.

Each iteration follows the same micro-structure:
1. What was tried (concrete: a specific approach with code listing or schema)
2. Why it was tried (the hypothesis)
3. What happened (positive results AND limitations)
4. What was learned and what came next (the bridge to the next iteration)

**The narrative is honest about failure.** §4.4.1 explicitly says: "This approach had several major flaws. Mainly, the sheer volume of unprocessed data overwhelmed the capabilities of the 4o-mini model, often resulting in hallucinated outputs." Failure is described, attributed to a cause, and used to motivate the next iteration.

**§4.5 Evaluation.** Distinct from §4.4. Sets up the **evaluation framework**: techniques vs. configurations (a key conceptual distinction); benchmark question design; controlled test environment. This is *how* the artefact is evaluated, separate from *how* it was built. Includes the user-test design (participant recruitment, environment, question selection, expected favourabilities per question).

### Chapter 5 (Results, 16 pages)

**Three explicit categories:**
- §5.1 Scientific Results — the empirical data (test results, accuracy, speed, cost; user-test response times; product artifacts table mapping to DSR Construct/Model/Method/Instantiation)
- §5.2 Engineering Results — the artefact itself (Final Application walkthrough, Fullscreen Mode, Dev Mode; qualitative user-test observations)
- §5.3 Administrative Results — process documentation (Scheduled Progress, Time Tracking, Process Documentation: GitHub Milestones, Sprints, Issues, Issue Branching, Meetings)

**Why this split is strong:** each category answers a different reader question. *Scientific* answers "did it work?" *Engineering* answers "what did you build?" *Administrative* answers "how did you run the project?" — which is required by NTNU bachelor expectations. Most B-grade theses bundle all three under "Results" and lose the structural clarity.

**Style:** quantitative-heavy. Many "Top 5 by X" tables. Short narration around each table (1–2 paragraphs, no padding). Figures are referenced explicitly ("see Figure A.6"). Findings are stated without interpretation — that is reserved for Ch 6.

**The DSR Artifacts table (Table 5.9)** is a one-page mapping of every project artifact to its DSR category (Construct, Model, Method, Instantiation). This makes the abstract methodology theory in Ch 4.2 concrete and verifiable. Strong evidence of methodological discipline.

### Chapter 6 (Discussion, 10 pages)

**Sub-structure (the cleanest part of the thesis):**
- §6.1 Primary Findings — organised by the three named requirements (Stability / Efficiency / Security), each with a one-paragraph synthesis answering "did the artefact meet this requirement?"
- §6.2 Evaluation Precautions — four named limitations: Benchmark Question Scope, Selection Accuracy Metric, User Test Skewed Averages, Lack of Data
- §6.3 Deviations — what changed from the original plan and why: Lessened Security Focus, Shift of Research Question Scope
- §6.4 Development Methodology and Technology Choices — reflective: what went well with DSR + agile, where the iterative process lacked rigor
- §6.5 Teamwork and Collaboration — short, personal, reflective on two-person team dynamics
- §6.6 Possible Statbank API Improvements — directly answers RQ3, three named recommendations
- §6.7 Considering an Official Implementation — implications and open issues: Privacy Concerns, Ethics Around Bias and Unfairness, Societal Shift, Immediate Applicability

**Strongest moves:**
- §6.1 organises findings by the three anchor concepts from §1.1 — creates a near-perfect closed loop with the introduction.
- §6.2 names four specific limitations and analyses each. Honest about: small sample size (only 2 attempts per question), skewed averages (4-minute timeout), unrealistic test conditions (questions designed to match Statbank content). This is what "Limitations analysed honestly with impact on conclusions" looks like in practice.
- §6.3 *Deviations* — explicit acknowledgement that the project deviated from the original plan, with reasons. Most theses hide this; A-grade work surfaces it.
- §6.4 critiques their own methodology: "While the iterative development process was crucial for achieving a usable outcome, it lacked an empirical foundation to guide successive iterations. Many decisions were made without quantitative backing..." — willing to flag the weakness in their own approach.
- §6.5 — short, personal, on collaboration. Sensors at NTNU value process reflection.
- §6.6 directly answers RQ3 with named recommendations grounded in implementation experience — not vague suggestions.
- §6.7 raises ethics, privacy, and the question of whether the artefact *should* be deployed at all (not just whether it *can*) — handles dual-use concerns explicitly.

### Chapter 7 (Conclusion + Further Work, 3 pages)

**Move sequence:**
1. One-sentence opener: "The project has successfully explored the domain of every research question and the learnings has contributed to SSB's knowledge base."
2. Each RQ is **quoted verbatim**, then answered in one paragraph. Three RQs → three paragraphs. The answer references findings from Ch 5 and discussion from Ch 6, but introduces no new material.
3. §7.2 Further Work — three concrete sub-projects (Programmatically Handling Codelists; Improved Frontend; Increased Testing). Each is a paragraph, names a specific limitation it would address.

**Key discipline:** the conclusion is tight. No padding, no "in summary" preamble, no general reflections about the field. **It mirrors the RQs.**

### Chapter 8 (Societal Impact, 3 pages)

- §8.1 Holistic System Perspective — names the project as a socio-technical system, identifies actors (SSB, ChatSSB, users, journalists, citizens) and their interactions.
- §8.2 Sustainability Awareness Framework — uses SusAF (introduced in §2.4) as the structuring frame. Five dimensions, half a page each. Each names both benefits and harms.

**Pattern:** sustainability is not a tacked-on chapter; it is anchored to a framework that was introduced in theory and explicitly applied here. Each dimension cites at least one source.

---

## 4. The Five Highest-Leverage Moves

Ranked by transferability and grade-impact:

### Move 1 — Three Named Anchor Concepts Threaded Through Every Chapter

ChatSSB defined **Stability, Efficiency, Security** in their §1.1 and used them as a coherence backbone:
- §1.1 introduces them as named requirements
- §4.5 evaluates against them (accuracy = stability proxy; time + cost = efficiency proxy; threat model = security)
- §6.1 organises Primary Findings under them
- §7 Conclusion answers RQ1 by re-stating what was proven about each

**For our thesis (locked):** the three anchor concepts are
1. **Effektivitet** — planning time and quality vs. manual process
2. **Tillit / kontroll** — HITL: traffic coordinator must be able to override the algorithm
3. **Tilpasningsdyktighet** — solution must work across diverse Norwegian transport companies

These names are authoritative. Synonyms ("kontroll alone", "fleksibilitet", "skalerbarhet", "overstyring") drift the spine and must be flagged by reviewers. This is the single biggest coherence engine available to the thesis.

### Move 2 — Origin Story in Method §4.1

Rather than starting Method with research paradigm theory, ChatSSB §4.1 tells the actual story of how the project began (authors' frustration → cold-emailing SSB → seven-day wait → dialogue → name agreed). This makes every later design choice traceable to a stakeholder conversation. For us: the seven interviews already give us this raw material — the origin story is "we noticed X in adjacent work / had access to Y companies / interviewed N coordinators and found..."

### Move 3 — Named Iterations as a Narrative

§4.4 names nine iterations with descriptive titles ("All at Once", "From Query to Data", "Coming to Terms with LLM's Volatility"). Each iteration is a 1–2 page mini-story: tried, failed, learned, pivoted. This reads like a developer diary in academic prose. For us: Ressursplanlegger's algorithm has natural iteration phases (e.g. "Single-engine baseline" → "Constraint generalisation" → "Conflict detection layer" → "HITL controls" → "Multi-engine selection"). Naming them is what turns a sprint log into a research narrative.

### Move 4 — Limitations + Deviations Sections That Are Honest

§6.2 names four limitations as sub-subsections, each analysed for impact ("the averages underrepresent the actual time required"). §6.3 admits two outright deviations from the plan ("Initially, security was a central design concern... however... such concerns quickly subsided"). For us: the rubric already requires honest limitations, but the **structural move** — making them named sub-subsections, not buried paragraphs — increases legibility and signals discipline.

### Move 5 — Conclusion That Quotes RQs and Answers Each Discretely

§7.1 reproduces each RQ verbatim as a block quote, then answers it in one paragraph with no new claims. This is structurally trivial to copy and produces an exceptionally tight closing. For us: rewrite Ch 6 conclusion to quote each sub-question explicitly.

---

## 5. Argumentation Flow Patterns

### Theory→Background separation
Generic concepts (resource scheduling, HITL, DSR) live in Ch 2. Case-specific tech (TMS systems used in Norwegian transport, regulatory framework, existing software the coordinators use) belongs in a Background section that we currently fold into Ch 2 awkwardly. **Verdict for us:** consider a §2.X "Background" subsection or accept that our Ch 4 (Findings) will absorb this — but do not let Ch 2 turn into vendor descriptions.

### Definition-first paragraphs
Every theoretical sub-section opens with a noun-phrase definition: "A Large Language Model (LLM) is a type of artificial intelligence...". No throat-clearing. This pattern is already in our writing-style examples; the reference shows how relentlessly to apply it.

### Comparison-as-justification
When choosing DSR over alternatives, ChatSSB doesn't just claim DSR is right — it briefly contrasts against positivist and interpretivist paradigms (1 paragraph each). The reader sees that alternatives were considered. For us: when justifying any design choice (algorithm family, interview method, evaluation approach), include 1–2 sentences on the alternative that was considered and rejected.

### Asymmetric depth
Ch 2.1 (LLMs) is many sub-subsections; Ch 2.2 (REST API) is 1.5 paragraphs. Depth tracks importance to the argument. For us: the scheduling theory section in Ch 2 should dominate; HITL and tacit knowledge should get serious depth; vehicle routing theory is a one-paragraph delimit — and that should remain.

### Forward references that earn payoff
The §1 closing line about "future improvements" foreshadows §6.6 API recommendations. The §2.4 SusAF paragraph foreshadows Ch 8. Forward references must pay off in the chapter they point to. For us: any forward reference must be checked against the eventual chapter content — otherwise the spine cracks.

### Backward references for closure
§6.1 organises Primary Findings under the §1.1 requirements. §7.1 quotes the §1.2 RQs. These backward references close the loops that were opened in Ch 1. **Without these the thesis has no closure.**

---

## 6. Anti-Patterns the Reference Avoids

| Anti-pattern | Reference's actual practice |
|---|---|
| "The purpose of this thesis is to explore..." | First sentence is a concrete domain fact about SSB. |
| Theory chapter as detached literature review | Every concept in Ch 2 reappears in Ch 4 or 6. |
| Method chapter as project timeline | Method has DSR mapping, named iterations, evaluation framework. |
| Results bundled under one heading | Three explicit categories: Scientific, Engineering, Administrative. |
| Discussion that re-describes findings | §6.1 synthesises by anchor concept; never restates a number from §5. |
| Limitations as one paragraph at the end | §6.2 has four named sub-subsections, each analysed. |
| Conclusion that introduces new material | §7.1 quotes RQs verbatim and answers in 1 paragraph each, no new content. |
| Sustainability as paragraph in Ch 5 | Ch 8 is dedicated, anchored to a framework introduced in Ch 2. |
| Ethics as throwaway disclaimer | §6.7 raises bias, privacy, deployment-or-not as substantive design issues. |

---

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

## 8. Concrete Changes to Apply to the Writing System

> **Conventions used below:**
> - "Reference" = pattern observed in ChatSSB (the A-grade thesis)
> - "Apply" = specific change in our repo
> - **Locked anchors** for our thesis: **Effektivitet, Tillit/kontroll, Tilpasningsdyktighet**
> - **Pipeline mechanism note**: `.claude/skills/write-section/SKILL.md` already parses `MUST CITE`, `MUST EVIDENCE`, `MUST GROUND`, `MUST ANCHOR`, `MUST TRACE`. Use these existing markers — do **not** invent new `Anchor:`-syntax.
> - Section numbers below for our outline are **illustrative**. Adapt to whatever IDs `context/outline.md` actually uses.

### 8.1 — `context/thesis-spine.md`

Add an "Anchor Concepts" section above "The Argument — One Sentence Per Chapter":

```
## Anchor Concepts

The thesis argument turns on three named concepts. Every chapter must reference at least one. Discussion and Conclusion MUST organise findings under them. Synonyms drift the spine and must be flagged by reviewers.

1. **Effektivitet** — planning time and quality vs. manual process
2. **Tillit / kontroll** — HITL: traffic coordinator must be able to override the algorithm
3. **Tilpasningsdyktighet** — solution must work across diverse Norwegian transport companies
```

Then revise the per-chapter spine sentences. At minimum, Ch 1, Ch 5, and Ch 6 must explicitly name at least one anchor.

### 8.2 — `context/glossary.md`

Define each anchor as an official glossary term. Without this, writers will use synonyms and break terminology consistency.

```
**Effektivitet**: Reduction in coordinator's planning time and increase in plan quality (feasibility + coverage), relative to current manual practice. Used when discussing the artefact's primary value claim.

**Tillit / kontroll**: The coordinator's ability to inspect, modify, accept, or reject any algorithm-generated assignment. Trust and control are inseparable in this thesis: trust is built through demonstrable control. Use the compound term verbatim — do NOT split into "tillit" or "kontroll" alone, and do NOT substitute "menneskelig overstyring".

**Tilpasningsdyktighet**: Capacity of the system to function meaningfully across companies with materially different operational rules, fleet composition, and assignment criteria. Distinct from "skalerbarhet" (which concerns volume).
```

### 8.3 — `context/context.md`

Verify that the system description and research question align with the three anchors. Concretely:
- The RQ's "more efficiently" maps to **Effektivitet** — keep it
- The system description must explicitly mention HITL / override capability — maps to **Tillit/kontroll**
- The system description must explicitly mention multi-company applicability — maps to **Tilpasningsdyktighet**

If any anchor lacks a corresponding claim in `context.md`, the spine is unsupported. Either add the claim or revise the anchor.

### 8.4 — `context/outline.md` (structural guidance)

Restructure each chapter's outline to contain the following content slots, in this order. Use whatever numbering your outline already uses — the *content sequence* is what matters, not the IDs.

**Method chapter** must contain (in order):
1. *Defining the Task* — opens with origin-story paragraph (how the project began, how stakeholders were engaged, how requirements emerged)
2. *Method Theory* — DSR + DSRM applied as a step-by-step bullet list, one bullet per DSRM step applied to our specific work
3. *Choice of Technologies / Data Collection* — short justification per choice
4. *Iterative Development Process* — **named iterations** (4–9 with descriptive titles, each: tried / failed / learned / next)
5. *Evaluation* — separate from Iterative Development; describes the testing/validation framework

**Findings chapter** must split into:
- *Empirical Findings* — interview synthesis, no interpretation
- *The Artefact* — Ressursplanlegger system; **must include a DSR Artifacts mapping table** (Construct / Model / Method / Instantiation)
- *Process Documentation* — sprint log, decisions, time tracking (decide with user whether body or appendix)

**Discussion chapter** must contain (in order):
- *Primary Findings under the anchors* — one named sub-section per anchor (Effektivitet, Tillit/kontroll, Tilpasningsdyktighet)
- *Limitations / Evaluation Precautions* — named sub-subsections, each analysed for impact (NOT buried paragraphs)
- *Deviations from Plan* — explicit acknowledgements of what changed and why
- *Methodology Reflection* — what worked / what did not with DSR + iterative process
- *Recommendations* — grounded in implementation experience, not generic suggestions
- *Implications* — deployment, ethics, sustainability (anchor to a framework like SusAF where appropriate)

**Conclusion chapter** must contain:
- One paragraph per sub-question, each opening with the sub-question quoted verbatim as a block quote, then answered with no new material
- *Further Work* — concrete items, each citing a specific Limitation from Discussion
- A closing claim about the domain (one sentence beyond "we built X")

**Marker convention for outline ¶-plans:**
- Where a paragraph must serve an anchor, write `MUST ANCHOR: \textcite{anchor-concept-name} → §X.Y` using existing pipeline syntax. Tag the anchor by name (Effektivitet / Tillit/kontroll / Tilpasningsdyktighet).
- Where a paragraph in Conclusion must trace back to a Discussion sub-section, use `MUST TRACE: §X.Y → anchor-name`.
- Do **not** introduce new `Anchor:` lines — those bypass the existing readiness gate.

### 8.5 — `evaluation/a-grade-rubric.md`

Add per-chapter rubric criterion (append to the existing "An A [chapter] does..." sections):

Criteria are tied to **chapter types** (Introduction, Theory, Method, Findings, Discussion, Conclusion) — chapter numbering may differ depending on final structure choice.

| Chapter type | Add this criterion |
|---|---|
| **Introduction** | Names the three anchor concepts (Effektivitet, Tillit/kontroll, Tilpasningsdyktighet) with brief definitions; they are referenced verbatim in the Discussion and Conclusion chapters. |
| **Theory** | Asymmetric depth: the most argument-load-bearing theory gets the most space; secondary concepts <1 page; each theoretical concept introduced reappears in Findings or Discussion. |
| **Method / Methodology** | Opens with an origin-story paragraph naming how the project began. DSRM is applied step-by-step with one bullet per step. Iterative Development contains at least 4 named iterations (tried / failed / learned / next). |
| **Findings / Results** | Findings split by category (empirical / artefact / process). A DSR artifact mapping table is present. No interpretation — that lives in Discussion. |
| **Discussion** | Primary findings synthesised under the three locked anchors (one sub-section per anchor). Limitations are named sub-subsections, not buried. Deviations from original plan are explicit. Recommendations grounded in implementation experience. |
| **Conclusion** | Each sub-question quoted verbatim as a block quote and answered in one discrete paragraph with no new material. Further Work items each cite a specific Discussion limitation. |

Add a new section at the end of the rubric:

```
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

## 9. What Does NOT Transfer Automatically

Be careful — not every reference move applies to our project. Our chapter structure is **open** (could be 6, 7, or 8 chapters). The principles below apply regardless of count; the *layout choices* are decisions to make consciously, not defaults to copy.

- **Chapter count is a design choice, not a default.** ChatSSB chose 8 because their platform-specific tech (PxWebApi, LangChain) was too heavy for either Theory or Method. Decide based on actual content load: if platform/case-specific material is light, fold it into a Theory subsection or Method §X.1; if heavy, give it its own Background chapter. Either is valid.
- **Separate Societal Impact / Sustainability chapter:** ChatSSB Ch 8 is its own chapter, anchored to SusAF. We can either keep sustainability as a sub-section of Discussion (anchored to SusAF), or split into its own chapter if it grows past ~3 pages. Make this call after drafting the substance, not before.
- **Administrative Results in body vs appendix:** ChatSSB §5.3 puts Gantt, time tracking, sprint mechanics in body. NTNU often expects this somewhere — body or appendix is acceptable. Put in appendix unless your examiner explicitly expects it in body.
- **Two-author teamwork section:** Optional. Include only if it adds to methodology critique (e.g. how role split affected design decisions). Skip if it would be filler.
- **Heavy benchmark tables:** ChatSSB tested 54 LLM configurations and Top-5 tables made sense. Our evaluation is different (interview validation + requirements traceability + algorithm correctness on synthetic datasets). The *form* of compact comparison tables transfers; the *content* doesn't.
- **Code listings in body text:** ChatSSB shows JSON/TypeScript inline with numbered captions. NTNU CS sensors generally expect: pseudocode allowed in body for algorithm sections, but actual implementation code belongs in appendix. Default to that.
- **DSRM as Peffers et al. exclusively:** ChatSSB cites both Hevner (2004) three-cycle and Peffers et al. (2007) DSRM process model. Use both, applied step-by-step (see §8.4 and §11.5). Citing only one is a missed depth signal.

---

## 10. Verification — How a Reviewer Spot-Checks This Analysis

Each claim in this file maps to a specific page or section of `a-opg.pdf`:
- Three named requirements: pp. 2–3, §1.1
- Three numbered RQs: p. 3, §1.2
- Theory→Background separation: pp. 5–18, Ch 2 vs Ch 3
- DSR + DSRM application as bulleted list: pp. 20–22, §4.2.1
- Nine named iterations: pp. 24–34, §4.4.1–4.4.9
- Three results categories: pp. 41, 53, 54, §5.1, §5.2, §5.3
- DSR Artifacts table: p. 52, Table 5.9
- Discussion sub-structure: pp. 57–65, §6.1–6.7
- Four named limitations: pp. 58–60, §6.2.1–6.2.4
- Two named deviations: pp. 60, §6.3.1–6.3.2
- Conclusion quoting RQs: pp. 67–68, §7.1
- SusAF five-dimension treatment: pp. 71–73, §8.2.1–8.2.5

If any claim above seems wrong or surprising, jump to the cited page in the PDF.

---

## 11. Other Transferable A-Grade Conventions

Patterns observed in ChatSSB that are not load-bearing for the thesis argument but consistently appear in A-grade work. These are conventions, not principles — apply where they fit.

### 11.1 Front matter and chapter-opening conventions

ChatSSB's front matter includes:
- **Abstract** (English, ~1 page)
- **Sammendrag** (Norwegian summary, ~1 page) — required at NTNU
- **Preface** (acknowledgments — supervisor, stakeholders, collaborators)
- **Task Description** (the original assignment text, ~½ page)
- **Contents / Figures / Tables** (auto-generated)

**Chapter-opening epigraph** (optional but elegant): ChatSSB Ch 1 opens with a quoted epigraph (`"Official statistics are the nation's common factual basis... — SSB, 2025"`) before the first paragraph. Establishes domain authority and tone in one move. Use sparingly (Ch 1 only, or Ch 1 + a major chapter).

**"Why this chapter exists" opener**: ChatSSB Ch 3 (Background) opens with a meta-paragraph explaining why the chapter is there (to keep Theory generic and tools-specific detail bounded). Worth doing for any chapter whose role might be unclear (Background, Process Documentation, Societal Impact).

**Acronyms**: dedicated subsection at end of Introduction (ChatSSB §1.3). Bullet list, alphabetical. Required when the thesis has 5+ acronyms used multiple times.

### 11.2 Paragraph and prose conventions

- **Paragraph length**: 3–7 sentences. Longer paragraphs are split into ones with single topics. ChatSSB's longest paragraphs in body chapters are ~7 sentences; most are 4–5.
- **Definition-first openings** for theoretical concepts: "A Large Language Model (LLM) is a type of artificial intelligence based on a neural network…". No throat-clearing.
- **Transitions between paragraphs**: explicit content bridges, not "Furthermore"-spam. Each paragraph boundary should let the reader re-orient without scrolling back.
- **Voice**: predominantly impersonal ("the application", "the system", "the data shows"). First-person plural ("the authors", "we") is rare — used deliberately in Method §4.1 origin story to signal personal initiative, then dropped.
- **No hedging that weakens evidence-backed claims** ("might possibly", "perhaps could indicate"). Either the data supports the claim or it doesn't.
- **No overclaiming beyond evidence** ("proves definitively"). Use "demonstrates", "indicates", "suggests" with calibration.
- **First-use definitions of acronyms/specialised terms**: "structured output" defined at first occurrence; "LLM" expanded once; thereafter used unqualified.

### 11.3 Tables, figures, and code-listing conventions

- **Tables**: numbered as `Table N.M`, captioned below, booktabs style (`\toprule`, `\midrule`, `\bottomrule`). ChatSSB's "Top 5 by X" tables are dense and short — 5 rows, 4 columns max. Caption explains what the table compares.
- **Figures**: numbered as `Figure N.M` (body) or `Figure A.M` (appendix). Captioned below. ChatSSB references figures explicitly inline ("see Figure A.6").
- **Code listings**: numbered as `Code listing N.M` with descriptive caption. Short (5–20 lines). ChatSSB inlines JSON schemas and TypeScript snippets in Method to make iteration choices concrete. Default in our case: pseudocode in body, real code in appendix.
- **Cross-references**: `\Cref{}` for capitalised, `\cref{}` for lowercase. Never hardcode "Section 4.5" — use the macro so renumbering doesn't break references.

### 11.4 Sub-heading hierarchy

ChatSSB uses three levels: `\section{}`, `\subsection{}`, `\subsubsection{}` — all numbered. Inside a numbered subsection, ChatSSB sometimes adds **unnumbered bold sub-headers** (e.g. "Vector Databases and Embeddings" inside §2.1.7). Useful for breaking a long subsection into logical chunks without bloating the TOC.

### 11.5 DSRM Applied Process Model — exact format

This is the single most copyable A-move in Method. Format (from ChatSSB §4.2.1):

```
DSRM Applied Process Model

- Problem Identification and Motivation: <how we identified the problem in our case>
- Objectives of a Solution: <what we set out to achieve, with concrete criteria>
- Design and Development: <what we actually built, in one sentence>
- Demonstration: <how the artefact was shown to work>
- Evaluation: <how we measured success>
- Communication: <recommendations and contributions>
```

Each bullet 2–4 sentences. Anchors the abstract DSRM theory to verifiable project specifics. **Do this even if it feels mechanical** — it converts methodology theory into a checkable mapping.

### 11.6 Self-critical methodology paragraph

In Discussion, ChatSSB §6.4 contains a deliberately self-critical paragraph: *"While the iterative development process was crucial for achieving a usable outcome, it lacked an empirical foundation to guide successive iterations. Many decisions were made without quantitative backing…"*

This signals methodological maturity. Sensors notice. Don't fake it — find the actual weak spot in your method and name it. Possible candidates for our thesis: small interview sample (7 companies), validation against synthetic benchmarks rather than production data, single domain expert (Admmit) shaping requirements.

### 11.7 Comparison-as-justification

When choosing among methodological alternatives, ChatSSB names what was rejected and why. DSR is justified by 1 paragraph each contrasting positivist and interpretivist alternatives. Apply this to:
- Research paradigm (DSR vs alternatives)
- Interview method (semi-structured vs structured/unstructured)
- Algorithm family (CP-SAT vs MILP vs heuristics-only)
- Evaluation approach (benchmarks vs user studies vs requirements traceability)

1–2 sentences per alternative is enough. Shows that alternatives were considered, not that DSR was the only thing the authors knew.

---

## 12. Project Context for Writer / Reviewer Sessions

Self-contained facts about our thesis. A Claude session that reads only this file should have everything it needs to apply §8 correctly.

### 12.0 Thesis Statement (the message to the reader) — LOCKED

The position the thesis takes:

> Norske transportselskaper opererer i dag uten systematisk oversikt over ressursutnyttelse: overtid håndteres reaktivt, og lastbalansering mellom sjåfører avhenger av koordinatorers hukommelse og intuisjon. Etterspørselen etter algoritme-støttet planlegging kommer derfor primært fra bedriftseiere og forretningssiden, ikke fra koordinatorene som faktisk planlegger — en konfigurasjon som speiler Bainbridges (1983) klassiske *ironi* at automatiseringsbehov sjelden artikuleres av dem som må operere systemet. Ressursplanlegger demonstrerer at slik støtte kan gi målbar reduksjon i overtid, tid mellom oppdrag, og ujevn sjåfør-belastning (**Effektivitet**) når koordinatoren beholder reell overstyrings-kontroll over hvert forslag (**Tillit/kontroll**) og når systemet tilpasses bedriftens egne fordelings-regler (**Tilpasningsdyktighet**). Argumentet gjelder ikke flåter med høy rute-stabilitet eller koordinatorer som ikke ser verdi i systemstøtte i utgangspunktet.

**Empirical grounding** (NOT aspirational):
- Manglende systematisk oversikt over ressursutnyttelse: bekreftet på tvers av 7 intervjuer.
- Etterspørselen er fra bedriftseiere/Admmit, ikke fra koordinatorer i seg selv: bekreftet via flere intervjuer + Admmits opprinnelige mandat.
- Boundary cases (lav-variasjon flåter, manuelt-preferende koordinatorer): observert i intervjuene, ikke spekulert.

**Theoretical anchor**: Bainbridge (1983) *Ironies of Automation* — the operator-vs-owner asymmetry is the framing concept this thesis empirically extends to Norwegian transport's resource-planning domain. Already in `references.bib` as `bainbridge1983ironies`.

**Sharpened research question** (replaces current phrasing in `context.md` and `thesis-spine.md`):

> *How can an algorithm-assisted resource planning platform improve resource utilization in Norwegian transport companies (reducing overtime, idle time between assignments, and uneven driver load) while remaining accountable to the traffic coordinator who operates it?*

Note for downstream sessions: the existing RQ in `context.md` and `thesis-spine.md` says "support traffic coordinators... more efficiently than current manual processes". That framing is **outdated** as of 2026-04-29. Replace with the sharpened version above. Sub-questions in `thesis-spine.md` may also need adjustment to reflect the multi-stakeholder structure (operator vs. owner).

**Implications for downstream chapters**:
- *Introduction*: open with the visibility-gap finding, NOT "manual planning is slow".
- *Theory*: HITL section must engage Bainbridge directly, not just cite the source.
- *Findings*: the primary surprising finding is "manglende oversikt over ressursutnyttelse"; secondary is the operator-vs-owner stakeholder asymmetry.
- *Discussion*: the Effektivitet sub-section uses utilization metrics (overtime, idle time, load balance); not planning-time metrics primarily.
- *Conclusion*: the argument's qualifier (low-variation fleets, manual-preferring coordinators) must be stated explicitly, not hidden.

### 12.0.5 Findings Stance (artefact-evidence relationship) — LOCKED

The relationship between artefact and empirical findings is asymmetric. Must be communicated honestly throughout Method, Findings, and Discussion.

**Position (locked formulation):**
> Artefakten embodier behov surfaset i intervjuene; den tester ikke om disse behovene er reelle. Det multi-engine-arkitekturen gjør, er å generere empirisk evidens om hvilke solver-tilnærminger som best møter Effektivitet-kravet under realistiske constraint-kombinasjoner — en metodologisk uavhengig test av *hvordan*, ikke *om*.

**Origin map of major design decisions:**

| Design choice | Origin | Empirically validated? |
|---|---|---|
| HITL with full override | Admmit mandate | Confirmed by interviews (not introduced by them) |
| Resource-utilization focus | Admmit mandate | Confirmed by interviews (visibility gap) |
| Multi-tenant architecture | Admmit (customer structure) | Not interview-validated |
| Three solver engines (greedy / OR-Tools / Timefold) | Technical exploration | Not interview-validated |
| Drag-and-drop timeline UI | Interview-driven | Validated by interviews |
| Multi-engine selection | Technical exploration | Not interview-validated |
| Web-app (not mobile) | Admmit / technical | Not interview-validated |
| Real-time deviation detection (overtime, certificate expiry) | Designer / domain knowledge | Not interview-validated |
| Real-time streaming of planning to UI | Designer choice | Not interview-validated |
| Specific deviation categories | Domain knowledge | Not interview-validated |
| Database model and data-input flow | Technical | Not interview-validated |

**Empirical scope boundary:**
The interview guide (`context/intervju/`) defines what was empirically asked. Design decisions outside that scope are NOT interview-derived findings — they must be presented as design choices grounded in technical or stakeholder rationale, not as needs the interviews surfaced. Discussion's Limitations sub-section names this gap explicitly.

**What the artefact tests (vs. embodies):**
- *Tests:* which solver approach best meets Effektivitet under realistic constraint combinations (multi-engine benchmark = how-question).
- *Embodies, does not test:* whether the visibility gap is real (interviews surface this); whether HITL is necessary (Admmit mandate, not interview-tested); whether utilization improvement is the right primary metric (Admmit mandate).

### 12.0.7 Known Limitations — LOCKED

What the thesis cannot claim. Names below must reappear as named sub-subsections in Discussion's Limitations section. Knowing these in advance prevents overclaiming during writing.

**Empirical foundation:**

- **L1 — Sample size (7 interviews).** Prevents quantitative generalisation; prevents statistical-significance claims about cross-company patterns.
- **L2 — Self-selection bias in interview sample.** All interviewees are Admmit's customers — they have already chosen a structured-software solution. Findings cannot be claimed to reflect the Norwegian transport sector at large; only companies in this self-selected segment.
- **L3 — Author affiliation with Admmit.** We write for Admmit. Risk of "leading the witness" toward Admmit's hypotheses during interviews; reduced independence in interpretation. Cannot claim full investigator independence.
- **L4 — Interview-guide coverage gap.** Significant portions of the artefact (multi-tenant architecture, three solver engines, real-time deviation detection, real-time UI streaming, specific deviation categories, web-vs-mobile, database model) were not asked about in interviews. These design decisions cannot be claimed as interview-validated. See §12.0.5 for the full origin map.

**Validation / artefact:**

- **L5 — Synthetic benchmarks, not production data.** Solver results cannot be claimed to generalise to real Norwegian-transport operational data without further validation.
- **L6 — No real-world deployment.** Cannot claim that Effektivitet gains are actually realised in production use; cannot claim HITL controls function under operational time pressure.
- **L7 — No empirical comparison against existing TMS.** Cannot claim Ressursplanlegger is better than alternative systems in the same market segment.
- **L8 — No user testing with coordinators.** Cannot claim UI/HITL controls are comprehensible; cannot claim coordinators will actually use the override function as designed.
- **L9 — Algorithm evaluation against own benchmarks only.** Solutions are not compared against known optima or external standards; cannot claim absolute solution-quality.

**Conceptual / methodological:**

- **L10 — HITL as mandate, not validated level.** Admmit-mandated; cannot claim the chosen HITL level is optimal or that full automation would not work better in sub-cases.
- **L11 — Single-domain (Norwegian transport).** Cannot generalise to adjacent planning domains (shift planning, production scheduling, etc.) without further work.
- **L12 — Boundary cases described, not quantified.** Low-variation fleets and manually-preferring coordinators are observed as outside the argument's validity, but the proportion of the sector they represent is not measured. Argument's scope can be described qualitatively, not bounded quantitatively.

**Cross-reference to outline:**
Each L# must map to a named sub-subsection in Discussion's Limitations chapter. Use these L-numbers in the outline's MUST EVIDENCE markers so writers and reviewers can verify coverage.

### 12.1 Origin story raw material (for Method §X.1)

- **Source of project**: NTNU bachelor task offered by **Admmit** (the firm we write for). The task description PDF (`OPG29.pdf`) is part of the project documentation.
- **Stakeholder access**: the seven traffic coordinators interviewed are **Admmit's customers**. Contact was initiated by us on our own initiative — we phoned them directly. Admmit did not broker introductions.
- **HITL as mandate**: Human-in-the-loop was an **explicit requirement from Admmit from the start** of the project, not a finding from interviews. Interviews validated the necessity but did not introduce it.
- **Idea genesis**: the gap between current manual planning and algorithmic support is observable in the Norwegian transport sector at large; Admmit's product roadmap motivated investing in this specifically.

### 12.2 Locked anchor concepts (defined verbatim)

1. **Effektivitet** — improved resource utilization in three concrete dimensions: (a) reduced overtime, (b) reduced idle time between assignments, (c) reduced uneven load between drivers (load balancing). Secondary: reduced time spent on the planning activity itself. Note: visibility into utilization is the precondition for optimization — the system's primary value is making invisible utilization patterns visible to the coordinator and the company.
2. **Tillit / kontroll** — the coordinator's ability to inspect, modify, accept, or reject any algorithm-generated assignment. Trust and control are inseparable: trust is built through demonstrable control. Use the compound term verbatim.
3. **Tilpasningsdyktighet** — capacity to function meaningfully across companies with materially different operational rules, fleet composition, and assignment criteria. Distinct from "skalerbarhet" (which concerns volume).

### 12.3 Domain and stakeholders

- **Domain**: Norwegian transport sector (godstransport + persontransport). Multi-resource scheduling problem: assigning **drivers + vehicles** to **assignments**. Constraints include certifications, availability, regulatory rest rules, vehicle compatibility.
- **Stakeholder structure (asymmetric — see §12.0)**:
  - **Primary demand-side stakeholder**: Admmit AS (the firm we write for) and the transport-company owners that are Admmit's customers. They demand resource-utilization optimization.
  - **Primary operator** (the system's user, but NOT its primary demander): **trafikkoordinator** (traffic coordinator). Must remain in authority over individual assignment decisions.
  - **Other personas**: transport manager, driver — secondary.
- **Stakeholder firm**: Admmit AS. Customer firms: 7 Norwegian transport companies (small to medium-sized) that participated in interviews.
- **Methodology**: Design Science Research (DSR — Hevner et al. 2004 three-cycle) + DSRM Process Model (Peffers et al. 2007). Semi-structured interviews (Kvale & Brinkmann tradition) with 7 traffic coordinators. Iterative artefact development. Validation through requirements traceability + algorithm benchmarks on synthetic datasets.

### 12.4 Artefact summary (for Findings)

- **Ressursplanlegger**: web application (Next.js + tRPC + PostgreSQL) for managing employees, vehicles, and assignments within a transport company.
- **Multi-engine solver layer**:
  - Greedy baseline (Python, first-fit heuristic)
  - OR-Tools CP-SAT (Python, constraint programming)
  - Timefold Solver (Java, constraint programming)
- **HITL surface**: drag-and-drop timeline, real-time deviation detection (overbooking, missing certifications, certificate expiry), explicit accept/modify/reject on every algorithm suggestion.
- **Multi-tenant**: one application instance per Admmit customer, isolated via company scoping.

### 12.5 Validation approach

- **Empirical**: 7 interviews of traffic coordinators (data → pain points + requirements)
- **Algorithmic**: benchmarks on synthetic datasets (small/medium/large) comparing solver engines on solution quality + runtime
- **Coverage**: requirements traceability matrix (which functional/non-functional requirements are implemented and tested)
- **Not done**: production user testing with real-world fleets (acknowledge in Limitations)

### 12.6 Out of scope (delimits — keep explicit)

- **Vehicle Routing Problem** (VRP, Braekers et al. 2016) — referenced *only* to delimit. Our problem is assignment, not sequencing/routing. Do not let Theory drift into VRP depth.
- **Full automation without HITL** — explicitly out of scope per Admmit mandate. Discussion may note this as a deliberate constraint, not a limitation.
- **Cross-border / international transport regulations** — out of scope. Norwegian regulatory context only.
- **Real-time GPS / dispatch tracking** — out of scope. Planning artefact, not execution-monitoring artefact.

### 12.7 Sources baseline (for citation work)

- `result/references.bib` is the authoritative bibliography. Currently ~42 entries; 4 keys cited in `outline.md` are missing from the bib (`kvale2015interview`, `oates2022researching`, `braun2006thematic`, `malterud2017kvalitative`) — must be added before Method writing.
- Source notes in `context/docs/method/sources/raw/extracted/` (28 done, ~18 remaining). Source-extractor pipeline requires raw PDF/MD before extraction can run.
- `evaluation/reference-thesis-analysis.md` (this file) is a reference document, not a citable source.

---

## Status

Generated: 2026-04-28 from `context/docs/method/sources/raw/a-opg.pdf` (120 pages, NTNU BSc CS, May 2025, A-grade).
Revised: 2026-04-29 — anchors locked; §8 expanded to cover all 11 system files; ChatSSB-vs-our-thesis notation clarified; chapter-count assumption removed from §9 and §8.5; new §11 (additional A-grade conventions) and §12 (project context for sessions) added so the file is self-contained for handover.
Coverage: chapter-level structural analysis, argumentation moves, applicability assessment, full system-update specification, prose/format conventions, our project's domain context.
Not covered (out of scope): line-level prose-style edits to existing drafted text (none exist yet); literal LaTeX template; sensor-specific feedback from prior NTNU theses other than ChatSSB.