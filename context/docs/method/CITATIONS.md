# Citations Map — Ressursplanlegger

> **Status: empty (2026-04-28).**
>
> This file will be assembled from the source notes in `sources/raw/extracted/` after all 48 sources have been extracted. Until then, it does not exist as a meaningful mapping.
>
> **The previous content was hypothesis-driven** — claims mapped to bibkeys based on titles and guesses, not on what the sources actually say. That induced confirmation bias in the source-extractor agent (it would jump to "the source supports claim X" because the file said so, instead of reading the source freshly).
>
> The pre-extraction backup is preserved at `CITATIONS-pre-extraction-backup.md` for reference but should not be used as input.
>
> **What replaces it during extraction:**
> - The agent reads each source guided by `context/outline.md` and `context/thesis-spine.md` — these define areas of interest (e.g. Ch 2.1 = scheduling theory) without prescribing specific claim-to-source mappings.
> - The agent extracts what the source actually contributes and suggests fit (`Suggested for: Ch X.Y ¶Z`) in the source notes.
> - Once all 48 source notes exist, this file will be rebuilt from those empirically grounded suggestions.

---

## Format (when populated)

```
Ch X.Y ¶Z: "claim text" → bibkey1, bibkey2 (page reference)
```

Mapping is empirical: each line traces to a verified passage in `sources/raw/extracted/{bibkey}.md`.