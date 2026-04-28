# Academic Writing Guide — Ressursplanlegger

> **Purpose:** Distilled writing rules for AI agents, based on NTNU's academic writing guidance.
> Used by the writer agent when producing thesis text.
> Source: NTNU Universitetsbiblioteket — Akademisk skriving.

---

## Core Principles

An academic text must be:
- **Precise** — concrete language, no filler words, correct terminology
- **Logical** — clear argumentation with visible reasoning chains
- **Structured** — consistent use of headings, topic sentences, and transitions
- **Detailed** — enough specificity that the reader can follow the method and verify claims
- **Transparent** — all sources cited, all weaknesses acknowledged

---

## Writing Action Levels

Different sections require different levels of intellectual engagement. The levels, from least to most demanding:

| Level | Norwegian | What it means | Thesis sections that use it |
|-------|-----------|---------------|----------------------------|
| **Describe** | Beskrive | Restate a situation or topic in your own words | Ch 4.4 (System Description) |
| **Define** | Definere | Explain what a concept or idea means | Ch 2 (Theory — key terms) |
| **Explain** | Gjøre rede for / Forklare | Present and explain material comprehensively — factors, boundaries, significance | Ch 2 (Theory), Ch 3 (Method), Ch 4.1 (Findings) |
| **Analyse** | Analysere | Take material and determine what it means — requires the author's voice | Ch 4 (Findings — interpreting interviews and fit/gap) |
| **Discuss** | Drøfte / Diskutere | Show multiple sides with reasoned argumentation, weigh arguments against criteria, explain why some arguments are stronger | Ch 5 (Discussion — all sections) |

**Key implication for writing:** Chapters 2–3 primarily *explain*. Chapter 4 *analyses*. Chapter 5 *discusses*. The discussion chapter must show the author's critical voice — not just present information but weigh, compare, and evaluate it.

---

## Paragraph Structure

Every paragraph must follow this pattern:

1. **Topic sentence** — the first sentence states what the paragraph is about
2. **Supporting content** — examples, evidence, citations, or explanations that develop the topic sentence
3. **Closing** — connects to the next paragraph or summarises the point

### Topic sentence rules
- Must introduce the paragraph's theme clearly
- Must be specific enough that the reader knows what follows
- Must connect to information already introduced (no orphaned topics)

### What makes a bad paragraph
- Topic sentence promises one thing, body delivers another
- Multiple unrelated points in one paragraph
- No topic sentence at all — starts with a detail instead of a claim

---

## Creating Flow and Coherence

### Big picture (whole thesis)
- Clear connection between research question, results, and conclusion
- All sections are relevant and in logical order
- Consistent language and formatting throughout

### Small picture (paragraphs and sentences)
- Each paragraph has a clearly bounded topic
- Paragraphs are in logical sequence
- Sentences and paragraphs are connected with transition words and cross-references

### Transition words (bindeord)

Use these to signal relationships between sentences and paragraphs:

| Relationship | Norwegian examples | English equivalents |
|-------------|-------------------|---------------------|
| Addition | videre, dessuten, i tillegg | furthermore, moreover, in addition |
| Example | for eksempel, for å illustrere | for example, to illustrate |
| Comparison | til sammenligning, i forhold til | in comparison, relative to |
| Contrast | på den annen side, likevel, men, imidlertid | on the other hand, however, nevertheless |
| Summary | for å oppsummere, kort fortalt, med andre ord | to summarise, in short, in other words |
| Sequence | innledningsvis, videre, avslutningsvis | initially, subsequently, finally |
| Cause/result | derfor, altså, ettersom, slik at | therefore, consequently, since, so that |

### Cross-references
- Use "as described in Section X.Y" to connect across chapters
- Use "the findings presented in Chapter 4 suggest that..." to link findings to discussion
- Avoid repeating information — reference it instead

### The Thread Spool Model (Trådsnellemodellen)

The thesis should follow the thread spool shape (Dysthe et al., 2010):
- **Introduction:** Start broad — the general problem area, then narrow to the specific research question
- **Method:** The narrowest point — precise description of exactly what was done
- **Discussion/Conclusion:** Widen again — connect findings back to the broader context, implications, future work

This shape ensures the thesis begins and ends in the big picture but does its detailed work in the middle.

---

## Headings and Subheadings

### Two types of headings

| Type | What it does | Best for |
|------|-------------|----------|
| **Structural** | Names the function ("Method", "Results", "Discussion") | Main chapter headings; short texts |
| **Thematic** | Names the content ("Tacit Knowledge as a Design Challenge", "Algorithm Performance") | Subheadings within chapters; longer texts |

### Recommendation for this thesis

Use **structural headings for main chapters** (Introduction, Theory, Method, Findings, Discussion, Conclusion) and **thematic subheadings within chapters** (e.g., "5.1 Does Ressursplanlegger Address the Identified Pain Points?" rather than "5.1 First Discussion Point").

This is already reflected in `context/outline.md` — the subheadings there are thematic.

**Rule:** Always verify that the heading still matches the content after revisions. It is common to change the text but forget to update the heading.

---

## Thesis Structure (IMRoD-based, empirical with theory)

The thesis follows this structure, which aligns with NTNU's guidance:

| Part | Chapter | Primary writing action | Key requirement |
|------|---------|----------------------|-----------------|
| Summary | Abstract | Describe | What was investigated, how, what was found — max 1 page |
| Introduction | Ch 1 | Explain | Problem, background, research question, reader guide |
| Theory | Ch 2 | Explain + Define | Theoretical framework — only theories used later in analysis/discussion |
| Method | Ch 3 | Explain + Justify | How data was collected, how it was analysed, strengths and weaknesses |
| Findings | Ch 4 | Analyse + Describe | Present and interpret findings — author's voice required |
| Discussion | Ch 5 | Discuss | Weigh findings against theory, compare with others, evaluate critically |
| Conclusion | Ch 6 | Summarise + Conclude | Answer research question, mirror the introduction, suggest future work |

### Section-specific guidance

**Introduction** — start broad, narrow to the specific research question. End with a reader guide ("This thesis is structured as follows..."). Write early, revise at the end.

**Theory** — only include theory that is actually used in analysis or discussion. If a theory is not referenced again later, it does not belong here. The theory chapter must be "pure" — present only theory, never mix in own empirical data. If own findings appear alongside theory, it becomes implicit analysis before the reader knows how the data was collected. The phenomenon being studied may motivate the choice of theory, but it must not be presented together with the theory.

**Method** — must answer: How did you collect data? How did you analyse it? Why these methods? What are the strengths and weaknesses? Include ethical considerations.

**Findings/Analysis** — present findings objectively first, then interpret. Use figures and tables for quantitative data. Discuss individual findings here; save overarching patterns for the Discussion chapter.

**Discussion** — this is where the thesis earns its grade. Must:
- Answer the research questions explicitly
- Compare findings with existing literature
- Evaluate reliability and validity of the study
- Identify what could have been done differently
- Assess strengths and weaknesses of the methods used

**Conclusion** — mirror the introduction. Summarise what was done, answer the research question, identify contributions, suggest future work. Should not introduce new information.

---

## Four Requirements for Scientific Quality (Malterud, 2003)

These four criteria apply regardless of whether the method is qualitative or quantitative. The thesis must visibly address all four — primarily in Chapters 3 and 5.

| Requirement | What it means | Where it shows in the thesis |
|-------------|---------------|------------------------------|
| **1. Systematic critical reflection** | The researcher's most important tool for reliability is to make the reader an informed companion who understands the conditions under which knowledge was produced | Shown indirectly throughout the entire report — structured method, transparent process |
| **2. Relevance** | What can the knowledge be used for? Originality in the answer, the question, or the research design | Chapter 1 (why this matters), Chapter 6 (contributions) |
| **3. Validity** | What has actually been found out? Internal validity (correctness), external validity (context), consistency (red thread from start to finish) | Chapter 3 (method justification), Chapter 5 (limitations) |
| **4. Reflexivity** | How has the research process shaped findings and conclusions? Awareness of bias and the researcher's own perspective | Chapter 5 (limitations — researcher = developer bias) |

**Reference:** Malterud, K. (2003). *Kvalitative metoder i medisinsk forskning* (2nd ed.). Universitetsforlaget.

> The writer agent should verify that each section implicitly or explicitly addresses these four criteria. The quality agent should check for them during review.

---

## Building Credibility (Troverdighet)

The reader must trust that the authors know what they are writing about. Credibility is built through:

1. **Good structure** — logical flow that the reader can follow without confusion
2. **Correct use of terminology** — using domain terms precisely (see `context/glossary.md`)
3. **Strong topic sentences** — every paragraph opens with a clear statement of what it covers
4. **Well-chosen sources** — arguments backed by relevant, quality-assessed references
5. **Correct referencing** — consistent citation style, no missing or invented sources
6. **Acknowledging limitations** — transparent about what the study cannot claim

Credibility is destroyed by: vague language, unsupported claims, inconsistent terminology, missing citations, or overstating findings.

---

## Language Rules for This Thesis

These rules are specific to the Ressursplanlegger thesis and supplement the general principles above:

1. **Write in formal, academic English** — not Norwegian (the thesis language is English)
2. **Use impersonal constructions** — "the results suggest", "it can be argued", "the interviews indicate" — never "we believe" or "we think"
3. **Use terminology from `context/glossary.md`** consistently — do not introduce synonyms
4. **Avoid filler words** — "jo", "altså", "basically", "obviously", "of course"
5. **Keep sentences short** where possible — prefer clarity over complexity
6. **Start every paragraph with a topic sentence** that states what the paragraph is about
7. **Use transition words** to create flow between paragraphs
8. **Be consistent in tense** — this is critical:
   - **Present tense:** general claims, established theory, definitions ("Constraint programming is a paradigm for solving combinatorial problems")
   - **Past tense:** what was done in this study ("Seven interviews were conducted", "The algorithm generated a plan")
   - **Present perfect:** connecting past actions to current relevance ("Previous research has shown that...")
   - Never mix tenses within the same paragraph without a clear reason
9. **Cite every claim** that is not common knowledge — use `\parencite{key}` or `\textcite{key}`
10. **Do not overload with jargon** — use technical terms where appropriate, but the text should be readable by someone with a CS background who is not a domain expert
11. **Use direct student-level English** — prefer short, clear words over advanced academic phrasing when the meaning is the same. Avoid unnecessary adverbs and vague intensifiers such as "widely", "clearly", "significantly", "particularly", "highly", and "effectively". Do not write phrases such as "widely used" unless the scope is specified, for example by naming the sector, source, country, or user group. The text should sound like precise academic writing by Norwegian bachelor students, not like inflated expert prose.

---

## Citing and Referencing

- **Reference style:** APA 7 / biblatex (author-year format)
- **In-text citations:** `\parencite{key}` for (Author, Year) or `\textcite{key}` for Author (Year)
- **Direct quotes:** Use sparingly. Short quotes (<40 words) in quotation marks inline. Long quotes (40+ words) in a block quote environment. Always include page number.
- **Paraphrasing:** Preferred over direct quotes. Restate in your own words and cite the source.
- **Reference list:** All cited sources in `result/references.bib`. Every source in the text must be in the list, and every source in the list must be cited in the text.
- **Never invent sources** — only cite what exists in `result/references.bib`
- **Self-plagiarism:** Do not reuse text from other submitted coursework without citation

---

## Quality Checklist (per section)

Before outputting any section, verify:

- [ ] Every paragraph has a clear topic sentence
- [ ] Every claim is supported by a citation or by the study's own data
- [ ] No filler words or vague language
- [ ] Consistent terminology (check `context/glossary.md`)
- [ ] Transition words connect paragraphs logically
- [ ] The section serves its chapter's purpose (explain, analyse, or discuss)
- [ ] No information is introduced that does not belong in this section
- [ ] Tense is consistent (past for methods/results, present for theory/discussion)
- [ ] All sources cited are in `result/references.bib`
