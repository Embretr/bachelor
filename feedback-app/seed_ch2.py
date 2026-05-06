#!/usr/bin/env python3
"""One-shot script to populate feedback-app/state.json with summaries for
every paragraph in result/chapters/ch2/ch2-theory.tex.

Hashes are computed by the same parser the server uses, so the entries
match what the web app will look up at request time.
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from server import parse_blocks, paragraph_hash  # noqa: E402

REPO_ROOT = HERE.parent
FILE_REL = "result/chapters/ch2/ch2-theory.tex"
FULL_PATH = REPO_ROOT / FILE_REL
STATE_PATH = HERE / "state.json"

SUMMARIES = [
    # Chapter intro
    "Maps the chapter's four theoretical foundations to the three anchor concepts and explains why section lengths differ.",
    # 2.1 Resource Scheduling (6 paragraphs)
    "Defines scheduling generally and frames RP's daily driver-and-vehicle assignment as one instance of it.",
    "Explains why pairing a driver and a vehicle makes RP's scheduling problem harder than the single-resource case.",
    "Distinguishes feasible from good plans and positions visibility of utilization measures as RP's first contribution.",
    "Defines hard versus soft constraints and how RP handles each.",
    "States the problem's NP-hardness and bounds RP against the adjacent Vehicle Routing Problem literature.",
    "Names three solver families used for the problem and explains why each occupies a different operating regime.",
    # 2.2 HITL (6 paragraphs)
    "Places RP at level 5 of Parasuraman's automation taxonomy and motivates partial human authority.",
    "Grounds the human-in-the-loop choice in Bainbridge's owner-versus-operator asymmetry argument.",
    "Introduces Hoff and Bashir's three-layer trust model and what it means for deploying RP.",
    "Argues from Miller that explanations must be contrastive, selective, and social to keep trust calibrated.",
    "Adopts Lee and See's definition of trust and the goal of appropriate, not maximal, trust calibration.",
    "Translates the four HITL theories into concrete RP interface mechanisms.",
    # 2.3 TMS (3 paragraphs)
    "Defines a Transport Management System as the software category transport companies operate within.",
    "Shows that TMS coverage and adoption vary across vendors and across the sector.",
    "Names the upstream driver-and-vehicle planning gap that no TMS covers and that RP fills.",
    # 2.4 DSR (3 paragraphs)
    "Defines Design Science Research as artefact-plus-knowledge construction via Hevner's cycles and Peffers' six activities.",
    "Compares positivist and interpretive paradigms to justify why DSR fits this project.",
    "Distinguishes validation from evaluation per Wieringa and explains why this thesis validates rather than evaluates RP.",
]


def main():
    text = FULL_PATH.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    paragraphs = [b for b in blocks if b["kind"] == "paragraph"]

    if len(paragraphs) != len(SUMMARIES):
        print(
            f"MISMATCH: parser found {len(paragraphs)} paragraphs, "
            f"script has {len(SUMMARIES)} summaries.",
            file=sys.stderr,
        )
        for i, b in enumerate(paragraphs):
            print(f"  [{i}] ({b['context']})  {b['text'][:90]}...", file=sys.stderr)
        sys.exit(1)

    # Preserve any existing state for other files; replace this file's entries.
    if STATE_PATH.exists():
        try:
            state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
            if not isinstance(state, dict):
                state = {}
        except json.JSONDecodeError:
            state = {}
    else:
        state = {}

    file_state = {}
    for block, summary in zip(paragraphs, SUMMARIES):
        h = paragraph_hash(block["text"])
        file_state[h] = {
            "context": block["context"],
            "paragraph": block["text"],
            "summary": summary,
            "feedback": None,
            "suggestion": None,
            "status": None,
        }
    state[FILE_REL] = file_state

    STATE_PATH.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {STATE_PATH} with {len(paragraphs)} entries for {FILE_REL}")


if __name__ == "__main__":
    main()
