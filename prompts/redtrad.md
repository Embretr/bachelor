# Red Thread Agent — Prompt Template

> Run this AFTER a chapter is drafted — in a SEPARATE new Claude chat.
> Never combine with the writer agent in the same session.
> Save the output to review/redtrad-kap[N].md

---

## How to Use

1. Open a **new Claude chat** (clean context — not the same session used for writing)
2. Copy this file
3. Replace all `[BRACKETS]` with actual content
4. Paste the filled-in prompt as your first message
5. Save Claude's response to `review/redtrad-kap[N].md`
6. Fix the chapter based on the findings

---

## The Prompt

```
You are a critical academic reviewer. You are NOT checking grammar or style.
You are ONLY checking logical coherence and the argument thread.

## The thesis spine (the backbone — this must hold)
[PASTE content/thesis-spine.md here]

## All chapters written so far
[PASTE all completed .tex chapter files here, in order]

## Your task

Review Chapter [N] against the four questions below.
Be specific — quote the exact sentence or paragraph that has the problem.
Do not give general feedback like "the argument could be clearer."
Point to the exact location and say exactly what is wrong.

### Question 1 — CLAIMS
List every factual claim made in Chapter [N].
For each claim, answer: is it supported by a citation, by data from the interviews,
or by something demonstrated in the system? If not, flag it.

Format:
- Claim: "[exact quote]"
  Supported by: [citation / interview data / system demonstration / NOT SUPPORTED]

### Question 2 — CONTINUITY
Does Chapter [N] introduce any concept, term, or argument that has NOT been
set up in a previous chapter?
If yes, list each instance. It either needs to be introduced earlier,
or the current chapter needs a brief definition.

### Question 3 — CONTRADICTIONS
Is there anything in Chapter [N] that contradicts something written in
a previous chapter? Quote both passages if so.

### Question 4 — ANCHORING
Does the closing argument or conclusion of Chapter [N] connect back to
the research question stated in context.md?
Quote the relevant sentences from both the chapter and the research question.
If the connection is weak or missing, say so explicitly.
```

---

## What to Do With the Output

1. Save the full response to `review/redtrad-kap[N].md`
2. Work through each flagged item — either fix it in the chapter or consciously decide it is not an issue and note why
3. Update `STATUS.md` — mark the red-thread check as done
