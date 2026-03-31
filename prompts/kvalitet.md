# Quality Agent — Prompt Template

> Run this AFTER the red-thread check is done and the chapter is revised.
> Open a new Claude chat.
> Save output to review/kvalitet-kap[N].md

---

## How to Use

1. First complete the red-thread check (`prompts/redtrad.md`) and fix the chapter
2. Open a **new Claude chat**
3. Replace all `[BRACKETS]` with actual content
4. Paste the filled-in prompt as your first message
5. Save the response to `review/kvalitet-kap[N].md`
6. Fix the chapter based on the grade and suggestions

---

## The Prompt

```
You are an external examiner (sensor) at a Norwegian university assessing a
bachelor thesis in Data Engineering (Dataingeniør) at NTNU.

You are honest and critical. You do not give undeserved praise.
A grade of A requires exceptional work. B is solid. C is passing.

## Grading criteria
[PASTE vurdering/sensurveiledning.md here]
[PASTE vurdering/vurderingskriterier.md here]

## Chapter to assess
[PASTE the complete revised chapter .tex file here]

## Context
[PASTE context/context.md here]

## Your task

Assess Chapter [N] against each criterion in the grading guidelines.

For each criterion, provide:
1. **Grade: A / B / C / Cannot assess yet** (with one sentence justification)
2. **What is good** (be specific — quote the passage)
3. **What is weak or missing** (be specific — quote or describe the gap)
4. **One concrete fix** (one sentence — what would move this from B to A)

End with:
- An overall estimated grade for this chapter
- The single most important thing to fix before submission
```

---

## What to Do With the Output

1. Save the full response to `review/kvalitet-kap[N].md`
2. Prioritise fixes: focus on criteria where the grade is C
3. Address "the single most important thing" first
4. Update `STATUS.md` — mark the quality check as done
5. If a criterion is marked "Cannot assess yet" — it probably needs content from another chapter to be written first; note it and come back
