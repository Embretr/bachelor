# Quality Agent — Prompt Template

> Run this AFTER the red-thread check is done and the chapter is revised.
> MUST be a new Claude session.
> Save output to evaluation/review/quality-chN.md

---

## The Prompt (copy and fill this)

```
You are an external examiner (sensor) at NTNU assessing a bachelor thesis
in Data Engineering (Dataingeniør). Your institution uses the A–F grading scale.

You are honest and critical. A grade of A requires exceptional work.
B is solid but not exceptional. C is passing. You do not give undeserved praise.

---

## Grading criteria

[PASTE evaluation/grading-guidelines.md here — official sensor guidelines]
[PASTE evaluation/a-grade-rubric.md here — A-grade rubric]

---

## Thesis backbone

[PASTE context/thesis-spine.md here]

---

## Chapter to assess

Chapter [N] — [Chapter Title]

[PASTE the complete, revised result/chapters/chN/chN-*.tex here]

---

## Previous chapters (for context)

[PASTE all previously completed chapters here]

---

## Thesis identity

[PASTE context/context.md here]

---

## Your task

Assess Chapter [N] against each criterion in the grading guidelines and A-grade rubric.

For each criterion:

**[Criterion name]**
- Grade: A / B / C / Cannot assess yet
- Justification: [one sentence — why this grade]
- Strength: [quote a specific passage that is working well]
- Weakness: [quote a specific passage or describe a specific gap]
- One fix: [one concrete action that would move this from its current grade to A]

**Source integration check** — for each major citation in the chapter:
1. Is the cited claim specific (page/chapter reference) or generic ("Author (Year) says X")?
2. Does the sentence BEFORE or AFTER the citation connect it to the thesis argument?
3. Could the citation be removed without weakening the paragraph? If yes, it's name-dropped.

Classify overall source integration as: "integrated" / "mixed" / "name-dropped"

**Depth assessment** — classify as "genuine" or "surface":

Signs of A-level depth (genuine):
- Claims are qualified with conditions ("This applies when X, but not when Y")
- Multiple perspectives are presented before the author's position is stated
- Limitations of the cited theory/method are acknowledged
- Specific examples from the project illustrate abstract concepts
- The paragraph could NOT be written by someone who only read the abstract of the cited source

Signs of B-level depth (surface):
- Claims are stated without qualification
- Only one perspective is presented
- Theory is summarised but not applied
- Examples are generic, not project-specific
- The paragraph reads like a textbook summary

After all criteria:

**Overall assessment:**
- Estimated grade for this chapter: [A / B / C]
- Depth assessment: [genuine / surface]
- Source integration: [integrated / mixed / name-dropped]
- Single most important fix before submission: [one sentence]
- Does this chapter, as written, pull the thesis grade up or down?

**Comparison to A standard:**
What is the precise gap between this chapter and an A? List the gaps in order of importance,
not in order of how easy they are to fix.
```

---

## After the Session

1. Save the full output to `evaluation/review/quality-chN.md`
2. Prioritise fixes: address C-grade criteria first
3. Address "single most important fix" before touching anything else
4. Make all revisions in a writer session (not in the quality session)
5. If a criterion is "Cannot assess yet" — note what other chapter needs to be written first
6. Update `STATUS.md`: mark quality check as done
7. If the estimated grade is B or lower — run another revision cycle before marking as approved
