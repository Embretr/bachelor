#!/bin/bash
# ─── Citation Key Validator ────────────────────────────────────────────────
# Checks that all \parencite{} and \textcite{} keys in a .tex file
# exist in references.bib. macOS/BSD compatible (no grep -P).
#
# Usage: ./scripts/check-citations.sh result/chapters/ch2/ch2-theory.tex
# Exit code: 0 = all keys valid, 1 = missing keys found
# ──────────────────────────────────────────────────────────────────────────

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEX_FILE="${1:-}"
BIB_FILE="$REPO_ROOT/result/references.bib"

if [ -z "$TEX_FILE" ]; then
  echo "Usage: ./scripts/check-citations.sh <tex-file>"
  exit 1
fi

if [ ! -f "$TEX_FILE" ]; then
  echo "Error: File not found: $TEX_FILE"
  exit 1
fi

if [ ! -f "$BIB_FILE" ]; then
  echo "Error: references.bib not found at $BIB_FILE"
  exit 1
fi

# Extract all BibTeX keys from references.bib (portable sed/awk)
BIB_KEYS=$(grep '^@' "$BIB_FILE" | sed 's/^@[a-zA-Z]*{//' | sed 's/,$//' | sed 's/[[:space:]]//g' | sort -u)

# Extract all citation keys from the .tex file
# Strategy: find \parencite or \textcite commands, extract the last {braced} group (the keys)
# Handles: \parencite{key}, \parencite{a,b}, \parencite[see][12]{key}, \textcite{key}, \parencite*{key}
CITE_KEYS=$(
  # Extract lines containing cite commands
  grep -o '\\[a-z]*cite[*]*\([^}]*\)\?{[^}]*}' "$TEX_FILE" 2>/dev/null | \
  # Get just the last {braced} part (the actual keys)
  sed 's/.*{\([^}]*\)}/\1/' | \
  # Split comma-separated keys into individual lines
  tr ',' '\n' | \
  # Trim whitespace
  sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | \
  # Remove empty lines
  grep -v '^$' | \
  sort -u
) || true

if [ -z "$CITE_KEYS" ]; then
  echo "No citations found in $TEX_FILE"
  exit 0
fi

# Check each citation key
MISSING=""
FOUND=0
TOTAL=0

while IFS= read -r key; do
  [ -z "$key" ] && continue
  TOTAL=$((TOTAL + 1))
  if echo "$BIB_KEYS" | grep -qx "$key"; then
    FOUND=$((FOUND + 1))
  else
    MISSING="${MISSING}  - ${key}\n"
  fi
done <<< "$CITE_KEYS"

echo "Citation check: $FOUND/$TOTAL keys valid"

if [ -n "$MISSING" ]; then
  echo ""
  echo "MISSING KEYS (not in references.bib):"
  printf "$MISSING"
  exit 1
else
  echo "All citation keys found in references.bib"
  exit 0
fi
