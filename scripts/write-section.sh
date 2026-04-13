#!/bin/bash
# ─── DEPRECATED ────────────────────────────────────────────────────────────
# This script is superseded by /write-section (slash command).
# Use: /write-section 2.1 instead.
# Kept as manual fallback until /write-section is proven stable.
# ──────────────────────────────────────────────────────────────────────────────
# Original: Write Section — builds a prompt and copies to clipboard.
# ──────────────────────────────────────────────────────────────────────────────

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SECTION="${1:-}"

if [ -z "$SECTION" ]; then
  echo "Usage: ./scripts/write-section.sh <section>"
  echo ""
  echo "Examples:"
  echo "  ./scripts/write-section.sh 2.1    # VRP theory"
  echo "  ./scripts/write-section.sh 2.2    # Resource Scheduling & HITL"
  echo "  ./scripts/write-section.sh 3.1    # Research Design"
  echo "  ./scripts/write-section.sh 4.1    # Interview Findings"
  echo ""
  echo "Writing order (recommended):"
  echo "  2.1 → 2.2 → 2.3 → 2.4 → 3.1 → 3.2 → 3.3 → 3.4 → 3.5"
  echo "  → 4.1 → 4.3 → 4.2 → 4.4 → 4.5 → 5.1 → 5.2 → 5.3"
  echo "  → 5.4 → 5.5 → 5.6 → 1.1 → 1.2 → 1.3 → 1.4 → 6.1 → 6.2 → 6.3"
  exit 1
fi

CHAPTER="${SECTION%%.*}"
PROMPT_FILE="$REPO_ROOT/.claude/prompts/write-${SECTION}.md"
mkdir -p "$REPO_ROOT/.claude/prompts"

# ─── Determine chapter .tex file ─────────────────────────────────────────────
case "$CHAPTER" in
  1) TEX_FILE="result/chapters/ch1/ch1-introduction.tex"; CH_NAME="Introduction" ;;
  2) TEX_FILE="result/chapters/ch2/ch2-theory.tex"; CH_NAME="Theory" ;;
  3) TEX_FILE="result/chapters/ch3/ch3-method.tex"; CH_NAME="Methodology" ;;
  4) TEX_FILE="result/chapters/ch4/ch4-findings.tex"; CH_NAME="Findings" ;;
  5) TEX_FILE="result/chapters/ch5/ch5-discussion.tex"; CH_NAME="Discussion" ;;
  6) TEX_FILE="result/chapters/ch6/ch6-conclusion.tex"; CH_NAME="Conclusion" ;;
  *) echo "Error: Unknown chapter $CHAPTER"; exit 1 ;;
esac

# ─── Determine previous chapter .tex file ────────────────────────────────────
PREV_CHAPTER=$((CHAPTER - 1))
case "$PREV_CHAPTER" in
  0) PREV_TEX="" ;;
  1) PREV_TEX="result/chapters/ch1/ch1-introduction.tex" ;;
  2) PREV_TEX="result/chapters/ch2/ch2-theory.tex" ;;
  3) PREV_TEX="result/chapters/ch3/ch3-method.tex" ;;
  4) PREV_TEX="result/chapters/ch4/ch4-findings.tex" ;;
  5) PREV_TEX="result/chapters/ch5/ch5-discussion.tex" ;;
  *) PREV_TEX="" ;;
esac

# ─── Determine context files per chapter ─────────────────────────────────────
CONTEXT_FILES=()

# Always load
CONTEXT_FILES+=("context/context.md")
CONTEXT_FILES+=("context/thesis-spine.md")
CONTEXT_FILES+=("context/glossary.md")

# Chapter-specific
case "$CHAPTER" in
  1)
    CONTEXT_FILES+=("context/scope.md")
    CONTEXT_FILES+=("context/interviews-summary.md")
    ;;
  2)
    CONTEXT_FILES+=("context/docs/method/theoretical-framework.md")
    CONTEXT_FILES+=("context/docs/tech/algorithm.md")
    ;;
  3)
    CONTEXT_FILES+=("context/docs/method/research-design.md")
    CONTEXT_FILES+=("context/interviews-summary.md")
    ;;
  4)
    CONTEXT_FILES+=("context/interviews-summary.md")
    CONTEXT_FILES+=("context/fitgap-summary.md")
    CONTEXT_FILES+=("context/docs/requirements/functional-requirements.md")
    case "$SECTION" in
      4.1) CONTEXT_FILES+=("context/intervju/summary.md") ;;
      4.4) CONTEXT_FILES+=("context/docs/tech/architecture.md")
           CONTEXT_FILES+=("context/docs/tech/tech-stack.md")
           CONTEXT_FILES+=("context/docs/tech/data-model.md") ;;
      4.5) CONTEXT_FILES+=("context/docs/tech/algorithm.md") ;;
    esac
    ;;
  5)
    CONTEXT_FILES+=("context/docs/method/sustainability-analysis.md")
    CONTEXT_FILES+=("context/docs/method/research-design.md")
    CONTEXT_FILES+=("context/docs/project/risk-log.md")
    ;;
  6)
    CONTEXT_FILES+=("context/scope.md")
    ;;
esac

# ─── Build the prompt ────────────────────────────────────────────────────────
cat > "$PROMPT_FILE" << 'PROMPT_HEADER'
You are writing a section of a bachelor thesis for NTNU (Data Engineering).
The thesis must achieve grade A. Every sentence is evaluated against that standard.

## Rules
- Write in formal, academic English
- Use impersonal constructions — "the results suggest", "it can be argued" — never "we believe"
- One section only — do not write the next section
- Only cite sources from the REFERENCES section below — use \parencite{key} or \textcite{key}
- Use only terms from the GLOSSARY section below
- If a citation is needed but no source is available, write [CITATION NEEDED: describe]
- If a fact is missing, write [FILL IN: describe] — do not invent
- Start each paragraph with a clear topic sentence
- Vary sentence length — mix short and long
- Do not start paragraphs with "Furthermore" or "Moreover" — vary transitions

PROMPT_HEADER

echo "" >> "$PROMPT_FILE"
echo "## Your task" >> "$PROMPT_FILE"
echo "" >> "$PROMPT_FILE"
echo "Write section **${SECTION}** of Chapter ${CHAPTER} — ${CH_NAME}." >> "$PROMPT_FILE"
echo "" >> "$PROMPT_FILE"
echo "## Section plan from outline" >> "$PROMPT_FILE"
echo "" >> "$PROMPT_FILE"
echo '```' >> "$PROMPT_FILE"
# Extract the relevant section from outline.md
python3 -c "
import re, sys
text = open('$REPO_ROOT/context/outline.md').read()
# Find the section header and extract until next section or chapter
pattern = r'(\*\*${SECTION} .*?\*\*.*?)(?=\*\*\d+\.\d+ |\n## Chapter|\n---|\Z)'
match = re.search(pattern, text, re.DOTALL)
if match:
    print(match.group(1).strip())
else:
    print('Section ${SECTION} not found in outline.md — check the section number.')
" >> "$PROMPT_FILE"
echo '```' >> "$PROMPT_FILE"

echo "" >> "$PROMPT_FILE"
echo "## Thesis spine (backbone)" >> "$PROMPT_FILE"
echo "" >> "$PROMPT_FILE"
echo '```' >> "$PROMPT_FILE"
grep -A2 "Chapter ${CHAPTER}" "$REPO_ROOT/context/thesis-spine.md" >> "$PROMPT_FILE" || true
echo '```' >> "$PROMPT_FILE"

echo "" >> "$PROMPT_FILE"
echo "## A-grade criteria for Chapter ${CHAPTER}" >> "$PROMPT_FILE"
echo "" >> "$PROMPT_FILE"
echo '```' >> "$PROMPT_FILE"
python3 -c "
import re
text = open('$REPO_ROOT/evaluation/evaluation.md').read()
pattern = r'(## Chapter ${CHAPTER} .*?)(?=## Chapter \d|## Cross-Chapter|\Z)'
match = re.search(pattern, text, re.DOTALL)
if match:
    print(match.group(1).strip())
else:
    print('No evaluation criteria found for Chapter ${CHAPTER}.')
" >> "$PROMPT_FILE"
echo '```' >> "$PROMPT_FILE"

# Add context files
for ctx in "${CONTEXT_FILES[@]}"; do
  if [ -f "$REPO_ROOT/$ctx" ]; then
    echo "" >> "$PROMPT_FILE"
    echo "## CONTEXT: $ctx" >> "$PROMPT_FILE"
    echo "" >> "$PROMPT_FILE"
    echo '```' >> "$PROMPT_FILE"
    cat "$REPO_ROOT/$ctx" >> "$PROMPT_FILE"
    echo '```' >> "$PROMPT_FILE"
  fi
done

# Add references
echo "" >> "$PROMPT_FILE"
echo "## REFERENCES (available for citation)" >> "$PROMPT_FILE"
echo "" >> "$PROMPT_FILE"
echo '```bibtex' >> "$PROMPT_FILE"
cat "$REPO_ROOT/result/references.bib" >> "$PROMPT_FILE"
echo '```' >> "$PROMPT_FILE"

# Add previous chapter for continuity
if [ -n "$PREV_TEX" ] && [ -f "$REPO_ROOT/$PREV_TEX" ]; then
  PREV_CONTENT=$(cat "$REPO_ROOT/$PREV_TEX")
  # Only include if it has actual content (not just comments/placeholders)
  if echo "$PREV_CONTENT" | grep -q '\\section'; then
    WORD_COUNT=$(echo "$PREV_CONTENT" | wc -w)
    if [ "$WORD_COUNT" -gt 200 ]; then
      echo "" >> "$PROMPT_FILE"
      echo "## PREVIOUS CHAPTER (for voice and continuity matching)" >> "$PROMPT_FILE"
      echo "" >> "$PROMPT_FILE"
      echo '```latex' >> "$PROMPT_FILE"
      cat "$REPO_ROOT/$PREV_TEX" >> "$PROMPT_FILE"
      echo '```' >> "$PROMPT_FILE"
    fi
  fi
fi

# Add current chapter (so writer sees what's already there)
echo "" >> "$PROMPT_FILE"
echo "## CURRENT CHAPTER FILE (write your section into this structure)" >> "$PROMPT_FILE"
echo "" >> "$PROMPT_FILE"
echo '```latex' >> "$PROMPT_FILE"
cat "$REPO_ROOT/$TEX_FILE" >> "$PROMPT_FILE"
echo '```' >> "$PROMPT_FILE"

# Self-evaluation reminder
cat >> "$PROMPT_FILE" << 'PROMPT_FOOTER'

## Before you output

Check:
1. Does every claim have a citation or reference to primary data?
2. Does every term match the glossary?
3. Does this section serve the chapter's thesis-spine sentence?
4. Is there a sentence that could be cut without losing meaning?
5. Does it sound like a knowledgeable student wrote it, not an AI?

If any answer is no — revise before outputting.

## Output format

Output ONLY the LaTeX content for section the requested section.
Do not include \chapter{} or other sections — only the \section{} you are writing.
Start with \section{...} and end when the section content is complete.
PROMPT_FOOTER

# ─── Report ──────────────────────────────────────────────────────────────────
TOTAL_LINES=$(wc -l < "$PROMPT_FILE")
TOTAL_WORDS=$(wc -w < "$PROMPT_FILE")

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  WRITE SECTION ${SECTION} — Chapter ${CHAPTER}: ${CH_NAME}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  Prompt file: $PROMPT_FILE"
echo "  Prompt size: ${TOTAL_LINES} lines, ${TOTAL_WORDS} words"
echo "  Context files loaded: ${#CONTEXT_FILES[@]}"
echo "  Target .tex file: $TEX_FILE"
echo ""
echo "  To run:"
echo ""
echo "    cd $REPO_ROOT"
echo "    claude -p \"\$(cat $PROMPT_FILE)\""
echo ""
echo "  Or open a new Claude Code session and paste:"
echo "    cat $PROMPT_FILE | pbcopy"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Copy to clipboard on macOS
if command -v pbcopy &>/dev/null; then
  cat "$PROMPT_FILE" | pbcopy
  echo "  ✅ Prompt copied to clipboard!"
  echo ""
fi
