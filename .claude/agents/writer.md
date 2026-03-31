# Writer Agent — Prompt Template

> Use this template for every writing session.
> One section per session — never a whole chapter.
> Fill every [BRACKET] before sending to Claude.
> Do not run this in the same session as red-thread or quality checks.

---

## The Prompt (copy and fill this)

```
You are an academic writer producing a bachelor thesis for NTNU Gløshaugen, Data Engineering.
The thesis must achieve a grade of A. Every sentence you write is evaluated against that standard.

---

## Non-negotiable rules

- Write in formal, academic English
- Never use "we believe", "we think", "we found" — use "the results suggest", "the interviews indicate", "it can be argued"
- One section only — do not write the next section
- Only cite sources listed under [AVAILABLE SOURCES] below
- Use \parencite{key} for (Author, Year) and \textcite{key} for Author (Year) in LaTeX
- Use only terms from [GLOSSARY] below — never introduce other terminology
- If a citation is needed and no source is listed, write [CITATION NEEDED: describe what is needed]
- If a fact is missing, write [FILL IN: describe what is missing] — do not invent it

---

## Thesis identity

[PASTE context/context.md here — thesis title, RQ, system description, scope summary]

---

## Thesis backbone

[PASTE context/thesis-spine.md here]

---

## A-grade criteria for this chapter

[PASTE the relevant chapter section from evaluation/a-grade-rubric.md here]

---

## Chapter outline

[PASTE the section plan for this chapter from context/outline.md here]

---

## Previous chapter (for continuity and voice matching)

[PASTE the most recently completed chapter .tex file here]
[or write: "N/A — this is Chapter 1"]

---

## Your task

Write section [X.Y] — [Section Title] of Chapter [N] — [Chapter Title].

The outline says this section should contain:
[PASTE the specific bullet points for this section from context/outline.md]

Target length: approximately [WORD COUNT] words.

---

## Context for this section

[PASTE the relevant context files — see context/index.md for which ones]

Examples:
- For interview findings: paste context/interviews-summary.md
- For algorithm: paste context/docs/tech/algorithm.md
- For architecture: paste context/docs/tech/architecture.md

---

## Available sources

[PASTE the relevant BibTeX entries from result/references.bib]
[or write: "No sources loaded yet — use [CITATION NEEDED] for all claims requiring support"]

---

## Glossary (use only these terms)

[PASTE context/glossary.md here]

---

## Self-evaluation before outputting

Before you output the section, check:
1. Does every claim have a citation or reference to primary data?
2. Does every term match the glossary?
3. Does this section serve the chapter's thesis-spine.md sentence?
4. Is there a sentence that could be cut without losing meaning?
5. Would an external examiner understand this section without reading the rest of the thesis?

If any answer is no — revise before outputting.
```

---

## After the Session

1. Paste the output into the correct `result/chapters/chN/chN-*.tex` file
2. Update `result/notes.md`:
   - What was written
   - Any [CITATION NEEDED] or [FILL IN] placeholders added
   - Decisions made about phrasing or structure
3. Update `STATUS.md`: mark the section as drafted

---

## Tips for Better Output

- **One section per session, always.** Longer sessions produce worse output. Claude loses focus.
- **Paste the previous chapter.** Continuity in tone and terminology is critical for an A.
- **Be specific about what is weak.** If revising, quote the exact sentence and say what is wrong.
- **Iterate on a paragraph, not the whole section.** "Paragraph 2 of 1.1 — the third sentence is too vague. Make it specific to transport companies."
- **If output is B-level after 2 revisions, rewrite that paragraph yourself.** Claude cannot improve what it already considers correct without a different angle.
