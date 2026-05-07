#!/usr/bin/env python3
"""
Paragraph feedback web app for the thesis - file-backed (no API calls).

Workflow:
  1. Run the server, open the page, pick a .tex file.
  2. Type feedback into the box next to any paragraph. Click "Save feedback".
     The feedback is written to feedback-app/state.json.
  3. In a Claude Code CLI session, ask: "process the pending feedback in
     feedback-app/state.json". Claude reads state.json, drafts a suggested
     LaTeX rewrite for every paragraph that has feedback but no suggestion,
     fills in any missing summaries, and writes state.json back.
  4. Click "Refresh" in the web app. Each paragraph with a suggestion now
     shows it with Apply / Reject buttons.
  5. Apply writes the new paragraph back to the .tex file and clears the
     state entry. Reject clears the entry without touching the file.

Run:
  python3 feedback-app/server.py            # default port 8765
  python3 feedback-app/server.py --port 9000

Open http://localhost:8765 in your browser.

State file format:
  feedback-app/state.json
  {
    "result/chapters/ch2/ch2-theory.tex": {
      "<16-char-hash>": {
        "context":    "Theory > Resource Scheduling",
        "paragraph":  "Many everyday jobs come down to scheduling...",
        "summary":    null | "One-sentence description of this paragraph.",
        "feedback":   null | "User's feedback text.",
        "suggestion": null | "Claude-drafted LaTeX rewrite of THIS paragraph."
                          | ["paragraph 1 text", "paragraph 2 text", ...],
        "extra_edits": null | [
          {
            "target_text": "...exact text of another paragraph to replace...",
            "new_text":    "...rewrite (string)..." | ["...part 1...", "...part 2..."],
            "label":       "human-readable hint, e.g. 'SQ1 quote block'"
          },
          ...
        ],

        # Both `suggestion` and `extra_edits[*].new_text` accept a string
        # (single-paragraph rewrite) or a list of strings (split this paragraph
        # into N new ones, joined with two newlines on Apply). The web UI shows
        # each part as its own sub-block so a "split this in two" feedback
        # produces a visibly two-block suggestion.

        "status":     null | "pending" | "ready"
      },
      ...
    }
  }

  The hash is sha256(paragraph_text)[:16]. Hashes can drift when the .tex
  file is edited externally or when a suggestion is Applied; attach_state()
  recovers by matching on the stored `paragraph` field and re-keys the entry
  to the current hash. save_feedback() always recomputes the hash from the
  paragraph text it receives, so state stays consistent across sessions.

  `extra_edits` lets one feedback entry drive edits to OTHER paragraphs in
  the same file. The web UI shows the source entry's primary suggestion plus
  any extras; Apply replaces all of them atomically (validate-all-then-write).
  Target paragraphs get a small "incoming edit" notice on their own block.
"""

import argparse
import hashlib
import http.server
import json
import os
import re
import socketserver
import sys
import threading
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = REPO_ROOT / "result" / "chapters"
STATE_FILE = Path(__file__).resolve().parent / "state.json"

FILE_LOCK = threading.Lock()


# -- LaTeX block parser ------------------------------------------------------

HEADING_RE = re.compile(r"^\\(chapter|section|subsection|subsubsection)\b")
HEADING_NAME_RE = re.compile(r"\\(chapter|section|subsection|subsubsection)\{([^}]*)\}")


def paragraph_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def parse_blocks(tex_text: str):
    blocks = []
    chunks = re.split(r"\n\s*\n", tex_text)
    chapter = section = subsection = ""

    for chunk in chunks:
        stripped = chunk.strip()
        if not stripped:
            continue

        first_line = stripped.splitlines()[0]
        m = HEADING_RE.match(first_line)
        if m:
            level = m.group(1)
            name_match = HEADING_NAME_RE.search(stripped)
            name = name_match.group(2) if name_match else ""
            if level == "chapter":
                chapter, section, subsection = name, "", ""
            elif level == "section":
                section, subsection = name, ""
            elif level == "subsection":
                subsection = name
            blocks.append({
                "kind": "heading",
                "level": level,
                "text": chunk,
                "context": " > ".join(p for p in [chapter, section, subsection] if p) or name,
            })
            continue

        if all(line.lstrip().startswith("%") or not line.strip() for line in stripped.splitlines()):
            blocks.append({"kind": "other", "text": chunk, "context": ""})
            continue

        ctx = " > ".join(p for p in [chapter, section, subsection] if p)
        blocks.append({"kind": "paragraph", "text": chunk, "context": ctx})

    return blocks


# -- State persistence -------------------------------------------------------

def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def file_state(state: dict, rel: str) -> dict:
    return state.setdefault(rel, {})


def attach_state(blocks, file_rel: str):
    """Attach state.json fields to blocks, recovering from hash drift.

    If an entry's stored `paragraph` text matches a current block but the
    entry is keyed under a stale hash (e.g. because the file was edited
    externally or a previous Apply didn't update DOM hashes), the entry is
    re-keyed under the current hash and persisted. This is what makes
    feedback survive paragraph rewrites.

    Also attaches `extra_edits` (drafted by Claude as part of THIS entry's
    feedback, replacing other paragraphs) and `incoming_edits` (extras from
    OTHER entries that target THIS paragraph).
    """
    with FILE_LOCK:
        state = load_state()
        fs = state.get(file_rel, {})

        # Build content -> stale_hash for entries whose stored paragraph
        # matches some current block.
        content_to_stored_hash = {}
        for stored_hash, entry in list(fs.items()):
            stored_para = entry.get("paragraph")
            if stored_para:
                content_to_stored_hash[stored_para] = stored_hash

        # Re-key entries that match a current block by content but not by hash.
        rekeyed = False
        for b in blocks:
            if b["kind"] != "paragraph":
                continue
            current_hash = paragraph_hash(b["text"])
            if current_hash in fs:
                continue
            stale = content_to_stored_hash.get(b["text"])
            if stale and stale in fs and stale != current_hash:
                fs[current_hash] = fs.pop(stale)
                rekeyed = True

        if rekeyed:
            state[file_rel] = fs
            save_state(state)

        # Build incoming-edits map keyed by target paragraph text.
        incoming = {}
        for source_hash, entry in fs.items():
            for edit in entry.get("extra_edits") or []:
                tgt = edit.get("target_text")
                if not tgt:
                    continue
                incoming.setdefault(tgt, []).append({
                    "source_hash": source_hash,
                    "source_context": entry.get("context", ""),
                    "label": edit.get("label", ""),
                    "new_text": edit.get("new_text", ""),
                })

        for b in blocks:
            if b["kind"] != "paragraph":
                continue
            h = paragraph_hash(b["text"])
            entry = fs.get(h, {})
            b["hash"] = h
            b["summary"] = entry.get("summary")
            b["feedback"] = entry.get("feedback")
            b["suggestion"] = entry.get("suggestion")
            b["extra_edits"] = entry.get("extra_edits") or []
            b["incoming_edits"] = incoming.get(b["text"], [])
            b["status"] = entry.get("status")
    return blocks


def aggregate_counts() -> dict:
    state = load_state()
    pending = ready = with_summary = total_entries = 0
    for fs in state.values():
        for entry in fs.values():
            total_entries += 1
            has_suggestion = bool(entry.get("suggestion") or entry.get("extra_edits"))
            if has_suggestion:
                ready += 1
            elif entry.get("feedback"):
                pending += 1
            if entry.get("summary"):
                with_summary += 1
    return {"pending": pending, "ready": ready, "summaries": with_summary, "total": total_entries}


def save_feedback(file_rel: str, client_hash: str, paragraph: str, context: str, feedback: str) -> str:
    """Persist feedback for a paragraph.

    The hash is recomputed from `paragraph` (the canonical hash) so state
    stays consistent even if the client posted a stale hash. If the entry
    already exists under the client's stale hash, it is migrated.

    Returns the canonical hash so the client can update its data-hash.
    """
    correct_hash = paragraph_hash(paragraph)
    with FILE_LOCK:
        state = load_state()
        fs = file_state(state, file_rel)
        if client_hash and client_hash != correct_hash and client_hash in fs and correct_hash not in fs:
            fs[correct_hash] = fs.pop(client_hash)
        entry = fs.setdefault(correct_hash, {})
        entry["context"] = context
        entry["paragraph"] = paragraph
        has_suggestion = bool(entry.get("suggestion") or entry.get("extra_edits"))
        if feedback:
            entry["feedback"] = feedback
            if not has_suggestion:
                entry["status"] = "pending"
        else:
            entry.pop("feedback", None)
            if not has_suggestion and not entry.get("summary"):
                fs.pop(correct_hash, None)
            else:
                entry["status"] = "ready" if has_suggestion else None
        if not fs:
            state.pop(file_rel, None)
        save_state(state)
    return correct_hash


def save_feedback_bulk(file_rel: str, feedback: str, skip_existing: bool):
    """Apply the same feedback prompt to every paragraph in `file_rel`.

    Skips any paragraph that already has a Claude-drafted suggestion, so
    bulk-applying a new prompt never destroys ready-to-apply work. If
    `skip_existing` is true, also skips paragraphs that already carry
    per-paragraph feedback.

    Returns counts: {set, skipped_existing, skipped_has_suggestion, total}.
    Returns None if the file is invalid or outside the repo.
    """
    full_path = (REPO_ROOT / file_rel).resolve()
    if not str(full_path).startswith(str(REPO_ROOT)) or not full_path.exists():
        return None

    text = full_path.read_text(encoding="utf-8")
    blocks = parse_blocks(text)

    set_count = 0
    skipped_existing = 0
    skipped_has_suggestion = 0
    total = 0

    with FILE_LOCK:
        state = load_state()
        fs = file_state(state, file_rel)
        for b in blocks:
            if b["kind"] != "paragraph":
                continue
            total += 1
            h = paragraph_hash(b["text"])
            entry = fs.setdefault(h, {})

            has_suggestion = bool(entry.get("suggestion") or entry.get("extra_edits"))
            if has_suggestion:
                skipped_has_suggestion += 1
                continue
            if skip_existing and entry.get("feedback"):
                skipped_existing += 1
                continue

            entry["context"] = b["context"]
            entry["paragraph"] = b["text"]
            entry["feedback"] = feedback
            entry["status"] = "pending"
            set_count += 1
        save_state(state)

    return {
        "set": set_count,
        "skipped_existing": skipped_existing,
        "skipped_has_suggestion": skipped_has_suggestion,
        "total": total,
    }


def reject_entry(file_rel: str, h: str):
    """Drop feedback, suggestion, and any extra_edits. Keep the summary."""
    with FILE_LOCK:
        state = load_state()
        fs = state.get(file_rel, {})
        entry = fs.get(h)
        if not entry:
            return
        entry.pop("feedback", None)
        entry.pop("suggestion", None)
        entry.pop("extra_edits", None)
        entry["status"] = None
        if not entry.get("summary"):
            fs.pop(h, None)
            if not fs:
                state.pop(file_rel, None)
        save_state(state)


def apply_edits(file_rel: str, source_hash: str, edits: list):
    """Apply a list of {old, new} edits to the file atomically.

    All edits are validated (each `old` appears exactly once) BEFORE any
    write happens. If validation passes, the writes proceed in order; the
    source entry (the one whose feedback drove these edits) is then dropped.
    """
    full_path = (REPO_ROOT / file_rel).resolve()
    if not str(full_path).startswith(str(REPO_ROOT)):
        return False, "Path outside repo root."
    if not full_path.exists():
        return False, "File not found."
    if not edits:
        return False, "No edits supplied."

    with FILE_LOCK:
        content = full_path.read_text(encoding="utf-8")
        for i, e in enumerate(edits, 1):
            old = e.get("old", "")
            if not old:
                return False, f"Edit #{i}: missing `old` text."
            if "new" not in e:
                return False, f"Edit #{i}: missing `new` text."
            count = content.count(old)
            if count == 0:
                return False, f"Edit #{i}: original paragraph not found in file (reload the page)."
            if count > 1:
                return False, f"Edit #{i}: original paragraph appears {count} times - refusing to replace ambiguously."
        for e in edits:
            content = content.replace(e["old"], e["new"], 1)
        full_path.write_text(content, encoding="utf-8")

        state = load_state()
        fs = state.get(file_rel, {})
        if source_hash in fs:
            fs.pop(source_hash)
            if not fs:
                state.pop(file_rel, None)
            save_state(state)
    return True, None


# -- HTML --------------------------------------------------------------------

INDEX_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Thesis paragraph feedback</title>
<style>
  :root { color-scheme: light; }
  body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; max-width: 1500px; margin: 1rem auto; padding: 0 1.25rem; color: #222; }
  header { display: flex; align-items: baseline; gap: 1rem; flex-wrap: wrap; margin-bottom: 0.4rem; }
  header h1 { font-size: 1.1rem; margin: 0; }
  header a { color: #2563eb; text-decoration: none; }
  header a:hover { text-decoration: underline; }
  .meta { color: #6b7280; font-size: 0.82rem; }
  .badge { display: inline-block; padding: 0.1rem 0.45rem; border-radius: 999px; font-size: 0.75rem; margin-right: 0.3rem; }
  .badge.pending { background: #fef3c7; color: #92400e; }
  .badge.ready { background: #dbeafe; color: #1e40af; }
  .protocol { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.6rem 0.9rem; margin-bottom: 1rem; font-size: 0.85rem; color: #334155; }
  .protocol code { background: #e2e8f0; padding: 0 0.25rem; border-radius: 3px; font-family: ui-monospace, monospace; font-size: 0.85em; }
  .bulk-fb { background: #fef9c3; border: 1px solid #fde68a; border-radius: 6px; padding: 0.7rem 0.9rem; margin-bottom: 1rem; }
  .bulk-fb-label { font-weight: 600; font-size: 0.85rem; color: #713f12; margin-bottom: 0.4rem; }
  .bulk-fb-hint { font-size: 0.78rem; color: #92591b; margin-bottom: 0.45rem; line-height: 1.45; }
  .bulk-fb textarea { width: 100%; min-height: 4rem; resize: vertical; font: inherit; padding: 0.4rem 0.5rem; box-sizing: border-box; border: 1px solid #fde68a; border-radius: 4px; }
  .bulk-fb-row { display: flex; align-items: center; flex-wrap: wrap; gap: 0.6rem; margin-top: 0.45rem; }
  .bulk-fb label.skip-toggle { font-size: 0.82rem; color: #713f12; cursor: pointer; }
  .bulk-fb-status { font-size: 0.82rem; color: #6b7280; }
  .bulk-fb button { background: #ca8a04; color: #fff; border: 1px solid #a16207; }
  .bulk-fb button:hover:not(:disabled) { background: #a16207; }
  .files { list-style: none; padding: 0; margin: 0; }
  .files li { margin: 0.35rem 0; }
  .files a { display: inline-block; padding: 0.4rem 0.6rem; border: 1px solid #ddd; border-radius: 4px; color: #1d4ed8; text-decoration: none; font-family: ui-monospace, monospace; font-size: 0.85rem; }
  .files a:hover { background: #f3f4f6; }
  .block { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 0.85rem 0; padding: 0.85rem; border: 1px solid #e5e7eb; border-radius: 6px; background: #fff; }
  .block.heading { display: block; background: #faf7e8; border-color: #e7d99a; padding: 0.55rem 0.85rem; }
  .block.heading pre { margin: 0; font-family: ui-monospace, monospace; font-size: 0.85rem; white-space: pre-wrap; }
  .block.has-feedback { border-color: #fbbf24; }
  .block.has-suggestion { border-color: #3b82f6; box-shadow: 0 0 0 1px #3b82f6 inset; }
  .block.applied { background: #effaf3; border-color: #86c599; }
  .block.other { display: block; opacity: 0.55; background: #f9f9f9; }
  .block.other pre { margin: 0; font-family: ui-monospace, monospace; font-size: 0.78rem; white-space: pre-wrap; }
  .ctx { color: #6b7280; font-size: 0.72rem; margin-bottom: 0.3rem; text-transform: uppercase; letter-spacing: 0.04em; }
  .summary { font-style: italic; color: #475569; font-size: 0.85rem; line-height: 1.4; margin: 0 0 0.5rem 0; padding: 0.4rem 0.6rem; background: #f1f5f9; border-left: 3px solid #94a3b8; border-radius: 2px; }
  .summary.missing { color: #94a3b8; background: #f8fafc; }
  .text-col .rendered { font-family: Georgia, "Times New Roman", serif; font-size: 0.94rem; line-height: 1.55; color: #111827; }
  .text-col .rendered code { font-family: ui-monospace, monospace; font-size: 0.82em; background: #f1f5f9; padding: 0 0.25rem; border-radius: 3px; }
  .text-col .rendered cite { font-style: normal; color: #1d4ed8; }
  .text-col .rendered .xref { color: #6b21a8; font-variant: small-caps; font-size: 0.92em; }
  .row-actions { display: flex; gap: 0.6rem; align-items: center; margin-top: 0.4rem; flex-wrap: wrap; }
  .speak { font-size: 0.72rem; padding: 0.18rem 0.5rem; background: #eef2ff; color: #3730a3; border: 1px solid #c7d2fe; border-radius: 4px; cursor: pointer; font-family: inherit; }
  .speak:hover:not(:disabled) { background: #e0e7ff; }
  .speak.playing { background: #b91c1c; color: #fff; border-color: #b91c1c; }
  .speak.playing:hover { background: #991b1b; }
  .tts-bar { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.5rem 0.85rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.85rem; flex-wrap: wrap; font-size: 0.85rem; color: #334155; }
  .tts-bar label { display: flex; align-items: center; gap: 0.4rem; }
  .tts-bar select, .tts-bar input[type="range"] { font-size: 0.85rem; }
  .tts-bar select { padding: 0.15rem 0.3rem; border: 1px solid #cbd5e1; border-radius: 3px; background: #fff; }
  .tts-bar .stop-all { padding: 0.2rem 0.6rem; background: #fff; border: 1px solid #cbd5e1; border-radius: 4px; cursor: pointer; font-size: 0.78rem; }
  .tts-bar .stop-all:hover { background: #f1f5f9; }
  .text-col .show-source { display: block; margin-top: 0.4rem; font-size: 0.72rem; color: #6b7280; cursor: pointer; user-select: none; }
  .text-col .show-source:hover { color: #2563eb; }
  .text-col pre.source { display: none; white-space: pre-wrap; font-family: ui-monospace, monospace; font-size: 0.78rem; line-height: 1.5; margin: 0.4rem 0 0 0; padding: 0.5rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; color: #475569; }
  .text-col pre.source.shown { display: block; }
  .suggestion .rendered { font-family: Georgia, "Times New Roman", serif; font-size: 0.94rem; line-height: 1.55; color: #111827; }
  .suggestion .rendered code { font-family: ui-monospace, monospace; font-size: 0.82em; background: #fff7d6; padding: 0 0.25rem; border-radius: 3px; }
  .suggestion .rendered cite { font-style: normal; color: #1d4ed8; }
  .suggestion .rendered .xref { color: #6b21a8; font-variant: small-caps; font-size: 0.92em; }
  textarea { width: 100%; box-sizing: border-box; min-height: 80px; font-family: -apple-system, sans-serif; font-size: 0.88rem; padding: 0.5rem; border: 1px solid #d1d5db; border-radius: 4px; resize: vertical; }
  button { margin-top: 0.45rem; margin-right: 0.4rem; padding: 0.35rem 0.75rem; font-size: 0.83rem; cursor: pointer; border: 1px solid #d1d5db; background: #f9fafb; border-radius: 4px; }
  button:hover:not(:disabled) { background: #f3f4f6; }
  button.primary { background: #2563eb; color: #fff; border-color: #2563eb; }
  button.primary:hover:not(:disabled) { background: #1d4ed8; }
  button.apply { background: #16a34a; color: #fff; border-color: #16a34a; }
  button.apply:hover:not(:disabled) { background: #15803d; }
  button.reject { background: #fff; color: #b91c1c; border-color: #fca5a5; }
  button.refresh { background: #fff; }
  button:disabled { opacity: 0.5; cursor: wait; }
  .pending-note { margin-top: 0.5rem; padding: 0.4rem 0.55rem; background: #fef3c7; border: 1px solid #fde68a; color: #92400e; border-radius: 4px; font-size: 0.82rem; }
  .suggestion { margin-top: 0.6rem; padding: 0.6rem; background: #fffbe6; border: 1px solid #f1d97c; border-radius: 4px; }
  .suggestion .label { font-size: 0.72rem; color: #6b5800; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.3rem; }
  .sug-part { margin: 0.45rem 0; padding: 0.45rem 0.55rem; background: #fffefa; border-left: 3px solid #f1d97c; border-radius: 0 3px 3px 0; }
  .sug-part .part-label { font-size: 0.68rem; color: #92400e; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.25rem; }
  .part-label { font-size: 0.7rem; color: #92400e; margin-bottom: 0.4rem; }
  .split-note { color: #92400e; font-style: italic; font-size: 0.78rem; }
  .diff { font-family: Georgia, "Times New Roman", serif; font-size: 0.94rem; line-height: 1.6; white-space: pre-wrap; word-wrap: break-word; padding: 0.45rem 0.55rem; background: #fff; border-radius: 4px; margin-top: 0.3rem; }
  .diff .d-eq { color: #6b7280; }
  .diff .d-add { background: #d1fae5; color: #064e3b; padding: 0.05rem 0.15rem; border-radius: 2px; }
  .diff .d-del { background: #fee2e2; color: #7f1d1d; text-decoration: line-through; padding: 0.05rem 0.15rem; border-radius: 2px; }
  .diff.diff-nochange .d-eq { color: #9ca3af; font-style: italic; }
  .extra-edit { margin-top: 0.5rem; padding: 0.5rem; background: #fff; border: 1px dashed #e7c15a; border-radius: 4px; }
  .extra-edit .head { font-size: 0.72rem; color: #6b5800; margin-bottom: 0.3rem; }
  .extra-edit .head strong { color: #1f2937; }
  .extra-edit .target-prefix { font-family: ui-monospace, monospace; font-size: 0.78rem; color: #6b7280; background: #f9fafb; padding: 0.25rem 0.4rem; border-radius: 3px; margin-bottom: 0.3rem; white-space: pre-wrap; word-break: break-word; }
  .incoming-edit { margin: 0.4rem 0; padding: 0.45rem 0.6rem; background: #ecfeff; border: 1px solid #67e8f9; border-radius: 4px; font-size: 0.82rem; color: #155e75; }
  .incoming-edit strong { color: #0c4a6e; }
  .incoming-edit a { color: #0e7490; text-decoration: underline; cursor: pointer; }
  .block.target-of-extra { border-color: #67e8f9; box-shadow: 0 0 0 1px #67e8f9 inset; }
  .suggestion pre.source { display: none; white-space: pre-wrap; font-family: ui-monospace, monospace; font-size: 0.78rem; line-height: 1.5; margin: 0.4rem 0; padding: 0.5rem; background: #fff7d6; border: 1px solid #f1d97c; border-radius: 4px; color: #6b5800; }
  .suggestion pre.source.shown { display: block; }
  .suggestion .show-source { display: block; margin: 0.4rem 0 0 0; font-size: 0.72rem; color: #92400e; cursor: pointer; user-select: none; }
  .err { color: #b91c1c; margin-top: 0.4rem; font-size: 0.83rem; }
  .ok { color: #15803d; margin-top: 0.4rem; font-size: 0.83rem; }
  .empty { color: #6b7280; padding: 1rem 0; }
</style>
</head>
<body>
<div id="app"></div>

<script>
const $ = (sel, root=document) => root.querySelector(sel);
const $$ = (sel, root=document) => Array.from(root.querySelectorAll(sel));
const params = new URLSearchParams(location.search);
const filePath = params.get("file");

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

const SECTION_LABELS = {
  "chap:theory": "Chapter 2", "chap:findings": "Chapter 4", "chap:discussion": "Chapter 5",
  "sec:scheduling": "Section 2.1", "sec:hitl": "Section 2.2", "sec:tms": "Section 2.3", "sec:dsr": "Section 2.4",
  "sec:iter-multiengine": "Section 4.5", "sec:iter-hitl": "Section 4.5", "sec:iter-deviations": "Section 4.5",
  "sec:iter-tradeoff": "Section 4.5", "sec:iter-weights": "Section 4.5",
  "sec:evaluation-framework": "Section 3.6",
};

function parseCiteKey(key) {
  const m = key.trim().match(/^([A-Za-z]+)(\d{4})/);
  if (!m) return { name: key.trim(), year: "" };
  const name = m[1].charAt(0).toUpperCase() + m[1].slice(1).toLowerCase();
  return { name, year: m[2] };
}

function fmtParenCiteOpts(opts) {
  return opts.replace(/~/g, " ").replace(/--/g, "–").trim();
}

function renderLatex(src) {
  // Input: HTML-escaped LaTeX source. Output: HTML with citations, refs,
  // \textit/\textbf/\texttt rendered as prose. We treat &amp; / &lt; / &gt;
  // / &quot; / &#39; as already-safe text.
  let s = src;

  // Collapse line breaks inside a paragraph - LaTeX sources line-wrap for
  // git readability, but the rendered prose should flow.
  s = s.replace(/\n+/g, " ").replace(/[ \t]+/g, " ").trim();

  // \parencite[opts]{keys}
  s = s.replace(/\\parencite\[([^\]]*)\]\{([^}]+)\}/g, (_, opts, keys) => {
    const parts = keys.split(/,\s*/).map(k => {
      const p = parseCiteKey(k);
      return p.year ? `${p.name}, ${p.year}` : p.name;
    });
    const o = fmtParenCiteOpts(opts);
    return `<cite>(${parts.join("; ")}, ${o})</cite>`;
  });
  // \parencite{keys}
  s = s.replace(/\\parencite\{([^}]+)\}/g, (_, keys) => {
    const parts = keys.split(/,\s*/).map(k => {
      const p = parseCiteKey(k);
      return p.year ? `${p.name}, ${p.year}` : p.name;
    });
    return `<cite>(${parts.join("; ")})</cite>`;
  });
  // \textcite{key}
  s = s.replace(/\\textcite\{([^}]+)\}/g, (_, key) => {
    const p = parseCiteKey(key);
    return p.year ? `<cite>${p.name} (${p.year})</cite>` : `<cite>${p.name}</cite>`;
  });

  // \Cref{labels} - handle multi-label form first
  s = s.replace(/\\Cref\{([^}]+)\}/g, (_, labels) => {
    const parts = labels.split(/,\s*/).map(l => SECTION_LABELS[l] || l.replace(/^[a-z]+:/, ""));
    return `<span class="xref">${parts.join(" / ")}</span>`;
  });
  s = s.replace(/§?\s*\\ref\{([^}]+)\}/g, (_, label) => {
    return `<span class="xref">${SECTION_LABELS[label] || label.replace(/^[a-z]+:/, "")}</span>`;
  });

  // Inline formatting
  s = s.replace(/\\textit\{([^}]+)\}/g, "<em>$1</em>");
  s = s.replace(/\\textbf\{([^}]+)\}/g, "<strong>$1</strong>");
  s = s.replace(/\\texttt\{([^}]+)\}/g, "<code>$1</code>");
  s = s.replace(/\\emph\{([^}]+)\}/g, "<em>$1</em>");

  // Misc
  s = s.replace(/~/g, " ");
  s = s.replace(/(\d)--(\d)/g, "$1–$2");
  s = s.replace(/---/g, "—");
  s = s.replace(/``/g, "“").replace(/''/g, "”");
  s = s.replace(/\\&amp;/g, "&amp;");
  s = s.replace(/\\%/g, "%");
  s = s.replace(/\\\$/g, "$");
  s = s.replace(/\\#/g, "#");

  return s;
}

function renderedBlock(latex, kind /* 'paragraph' | 'suggestion' */) {
  const escaped = escapeHtml(latex);
  const rendered = renderLatex(escaped);
  const dataAttr = kind === "suggestion" ? "data-suggested" : "data-original";
  return `
    <div class="rendered" ${dataAttr}="${escaped}">${rendered}</div>
    <div class="row-actions">
      <button class="speak" data-kind="${kind}">Read aloud</button>
      <span class="show-source" data-toggle="source">show LaTeX source</span>
    </div>
    <pre class="source">${escaped}</pre>
  `;
}

// -- Word-level diff (git style) --------------------------------------------
// Used to render a suggestion as "what changed" rather than as the whole new
// paragraph next to the original. Tokenises so each word carries its trailing
// whitespace (this prevents whitespace tokens from matching as common and
// fragmenting the diff into "del-add-del-add..."), runs LCS, then
// post-processes to put all deletions before all additions inside each
// non-equal run so the reader sees "old old old new new new" not interleaved.

function diffTokenize(s) {
  // Each token = optional leading whitespace + non-whitespace + trailing whitespace.
  // Whitespace stays glued to its adjacent word so it doesn't act as a free
  // anchor that splits the diff.
  if (!s) return [];
  return s.match(/\s*\S+\s*/g) || [];
}

function wordDiff(oldText, newText) {
  const A = diffTokenize(oldText), B = diffTokenize(newText);
  const m = A.length, n = B.length;
  const dp = Array.from({length: m + 1}, () => new Int32Array(n + 1));
  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      dp[i][j] = A[i] === B[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }
  const segs = [];
  let i = 0, j = 0;
  while (i < m && j < n) {
    if (A[i] === B[j]) { segs.push({k: 'eq', t: A[i]}); i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) { segs.push({k: 'del', t: A[i]}); i++; }
    else { segs.push({k: 'add', t: B[j]}); j++; }
  }
  while (i < m) segs.push({k: 'del', t: A[i++]});
  while (j < n) segs.push({k: 'add', t: B[j++]});

  // Post-pass: inside each contiguous non-equal run, gather all dels first,
  // then all adds. This converts "del add del add" into "del del add add" so
  // a multi-word replacement reads as one block of removed text followed by
  // one block of inserted text.
  const grouped = [];
  let k = 0;
  while (k < segs.length) {
    if (segs[k].k === 'eq') { grouped.push(segs[k]); k++; continue; }
    let endK = k;
    let dels = '', adds = '';
    while (endK < segs.length && segs[endK].k !== 'eq') {
      if (segs[endK].k === 'del') dels += segs[endK].t; else adds += segs[endK].t;
      endK++;
    }
    if (dels) grouped.push({k: 'del', t: dels});
    if (adds) grouped.push({k: 'add', t: adds});
    k = endK;
  }
  // Coalesce adjacent eq segments (post-grouping no eq is split, but be safe).
  const out = [];
  for (const s of grouped) {
    if (out.length && out[out.length - 1].k === s.k) out[out.length - 1].t += s.t;
    else out.push({k: s.k, t: s.t});
  }
  return out;
}

function renderDiff(oldText, newText) {
  if (oldText === newText) {
    return `<div class="diff diff-nochange"><span class="d-eq">${escapeHtml(newText)}</span></div>`;
  }
  if (newText === "") {
    return `<div class="diff"><span class="d-del">${escapeHtml(oldText)}</span></div>`;
  }
  if (oldText === "") {
    return `<div class="diff"><span class="d-add">${escapeHtml(newText)}</span></div>`;
  }
  const segs = wordDiff(oldText, newText);
  const html = segs.map(s => {
    const cls = s.k === 'eq' ? 'd-eq' : (s.k === 'add' ? 'd-add' : 'd-del');
    return `<span class="${cls}">${escapeHtml(s.t)}</span>`;
  }).join('');
  return `<div class="diff">${html}</div>`;
}

// -- TTS via browser SpeechSynthesis -----------------------------------------

const TTS = {
  utterance: null,
  button: null,
  voices: [],
};

function loadVoices() {
  TTS.voices = speechSynthesis.getVoices().filter(v => v.lang.startsWith("en"));
  const sel = document.getElementById("tts-voice");
  if (!sel) return;
  const previous = sel.value || localStorage.getItem("tts-voice") || "";
  sel.innerHTML = TTS.voices
    .map(v => `<option value="${escapeHtml(v.name)}">${escapeHtml(v.name)} (${escapeHtml(v.lang)})</option>`)
    .join("");
  if (previous && TTS.voices.some(v => v.name === previous)) {
    sel.value = previous;
  } else {
    // Prefer macOS premium voices if present
    const preferred = TTS.voices.find(v => /Samantha|Karen|Daniel|Moira|Tessa|Serena|Allison/.test(v.name))
      || TTS.voices.find(v => v.localService)
      || TTS.voices[0];
    if (preferred) sel.value = preferred.name;
  }
}

function stopSpeaking() {
  speechSynthesis.cancel();
  if (TTS.button) {
    TTS.button.classList.remove("playing");
    TTS.button.textContent = "Read aloud";
  }
  TTS.utterance = null;
  TTS.button = null;
}

function latexToSpeech(latex) {
  // Reuse the renderer, then strip HTML tags so the TTS engine sees plain prose.
  const escaped = escapeHtml(latex);
  const rendered = renderLatex(escaped);
  const tmp = document.createElement("div");
  tmp.innerHTML = rendered;
  return (tmp.textContent || "").replace(/\s+/g, " ").trim();
}

function speakBlock(block, kind, button) {
  const sel = kind === "suggestion" ? ".rendered[data-suggested]" : ".rendered[data-original]";
  const el = block.querySelector(sel);
  if (!el) return;
  const latex = kind === "suggestion" ? el.dataset.suggested : el.dataset.original;

  // Toggle: if this button is already playing, stop.
  if (TTS.button === button) {
    stopSpeaking();
    return;
  }
  stopSpeaking();

  const text = latexToSpeech(latex);
  if (!text) return;

  const utt = new SpeechSynthesisUtterance(text);
  const voiceSel = document.getElementById("tts-voice");
  const rateInput = document.getElementById("tts-rate");
  if (voiceSel && voiceSel.value) {
    const v = TTS.voices.find(v => v.name === voiceSel.value);
    if (v) utt.voice = v;
  }
  if (rateInput) utt.rate = parseFloat(rateInput.value) || 1.0;
  utt.onend = stopSpeaking;
  utt.onerror = stopSpeaking;

  TTS.utterance = utt;
  TTS.button = button;
  button.classList.add("playing");
  button.textContent = "Stop";
  speechSynthesis.speak(utt);
}

function ttsBar() {
  return `
    <div class="tts-bar">
      <strong>Audio:</strong>
      <label>voice <select id="tts-voice"></select></label>
      <label>rate <input id="tts-rate" type="range" min="0.7" max="1.6" step="0.05" value="1.0" style="width: 110px;">
        <span id="tts-rate-val">1.0×</span></label>
      <button class="stop-all" id="tts-stop">Stop</button>
    </div>
  `;
}

function wireTTS() {
  loadVoices();
  if (typeof speechSynthesis !== "undefined" && "onvoiceschanged" in speechSynthesis) {
    speechSynthesis.onvoiceschanged = loadVoices;
  }
  const voiceSel = document.getElementById("tts-voice");
  if (voiceSel) {
    voiceSel.addEventListener("change", () => {
      localStorage.setItem("tts-voice", voiceSel.value);
    });
  }
  const rate = document.getElementById("tts-rate");
  const rateVal = document.getElementById("tts-rate-val");
  if (rate && rateVal) {
    rate.addEventListener("input", () => {
      rateVal.textContent = `${parseFloat(rate.value).toFixed(2)}×`;
    });
  }
  const stop = document.getElementById("tts-stop");
  if (stop) stop.addEventListener("click", stopSpeaking);
}

async function fetchJSON(url, opts = {}) {
  const resp = await fetch(url, opts);
  const data = await resp.json();
  if (!resp.ok) throw new Error(data.error || `HTTP ${resp.status}`);
  return data;
}

function bulkFeedbackBar() {
  return `
    <div class="bulk-fb">
      <div class="bulk-fb-label">Apply feedback to every paragraph in this chapter</div>
      <div class="bulk-fb-hint">
        One prompt, every paragraph. Useful for chapter-wide passes such as "compare each
        paragraph against its summary, remove unnecessary sentences, and rewrite to be
        concrete to its main message". Paragraphs that already have a Claude-drafted
        suggestion are always skipped so ready-to-apply work is never overwritten.
      </div>
      <textarea id="bulk-fb-text" placeholder="Type a prompt to apply to every paragraph..."></textarea>
      <div class="bulk-fb-row">
        <label class="skip-toggle"><input type="checkbox" id="bulk-fb-skip" checked> Skip paragraphs that already have feedback</label>
        <button id="bulk-fb-apply" class="primary">Apply to all paragraphs</button>
        <span class="bulk-fb-status"></span>
      </div>
    </div>
  `;
}

function protocolBox(counts) {
  const c = counts || { pending: 0, ready: 0, summaries: 0, total: 0 };
  return `
    <div class="protocol">
      <strong>How this loop works:</strong>
      type feedback &rarr; click <em>Save feedback</em> &rarr; in Claude Code, ask
      <code>process the pending feedback in feedback-app/state.json</code> &rarr;
      click <em>Refresh</em> &rarr; <em>Apply</em> or <em>Reject</em>.
      <span class="meta" style="margin-left: 0.5rem;">
        <span class="badge pending">pending: ${c.pending}</span>
        <span class="badge ready">ready: ${c.ready}</span>
        summaries stored: ${c.summaries}
      </span>
    </div>
  `;
}

async function renderIndex() {
  const [files, counts] = await Promise.all([
    fetchJSON("/api/files"),
    fetchJSON("/api/state-counts"),
  ]);
  const list = files.files.map(f => `<li><a href="?file=${encodeURIComponent(f)}">${escapeHtml(f)}</a></li>`).join("");
  $("#app").innerHTML = `
    <header><h1>Thesis paragraph feedback</h1></header>
    ${protocolBox(counts)}
    <p>Pick a chapter file:</p>
    <ul class="files">${list}</ul>
  `;
}

async function renderFile() {
  const [data, counts] = await Promise.all([
    fetchJSON(`/api/file?path=${encodeURIComponent(filePath)}`),
    fetchJSON("/api/state-counts"),
  ]);
  const blocks = data.blocks;
  const totalParagraphs = blocks.filter(b => b.kind === "paragraph").length;

  let html = `
    <header>
      <h1><a href="/">&laquo; files</a></h1>
      <span style="font-family: ui-monospace, monospace; font-size: 0.9rem;">${escapeHtml(filePath)}</span>
      <span class="meta">${totalParagraphs} paragraphs</span>
      <button class="refresh" onclick="location.reload()">Refresh</button>
    </header>
    ${ttsBar()}
    ${protocolBox(counts)}
    ${bulkFeedbackBar()}
  `;

  if (!blocks.length) html += `<p class="empty">No blocks parsed.</p>`;

  blocks.forEach((b, i) => {
    if (b.kind === "heading") {
      html += `<div class="block heading"><div class="ctx">${escapeHtml(b.level)}</div><pre>${escapeHtml(b.text)}</pre></div>`;
    } else if (b.kind === "other") {
      html += `<div class="block other"><pre>${escapeHtml(b.text)}</pre></div>`;
    } else {
      const extras = Array.isArray(b.extra_edits) ? b.extra_edits : [];
      const incoming = Array.isArray(b.incoming_edits) ? b.incoming_edits : [];

      // Helper: normalise a suggestion field (string | string[] | null) to
      // an array of paragraph strings. null/undefined/[] -> []; empty
      // string is a valid suggestion meaning "delete the paragraph".
      const normParts = (val) => {
        if (val === null || val === undefined) return [];
        if (Array.isArray(val)) return val.filter(p => typeof p === "string");
        if (typeof val === "string") return [val];
        return [];
      };

      // Compute hasSuggestion from normalised content, not from raw truthiness
      // (an empty array is truthy in JS).
      const hasPrimary = normParts(b.suggestion).length > 0;
      const hasExtras = extras.some(e => normParts(e.new_text).length > 0);
      const hasSuggestion = hasPrimary || hasExtras;

      const cls = ["block", "paragraph"];
      if (hasSuggestion) cls.push("has-suggestion");
      else if (b.feedback) cls.push("has-feedback");
      if (incoming.length) cls.push("target-of-extra");

      const summaryHTML = b.summary
        ? `<div class="summary">${escapeHtml(b.summary)}</div>`
        : `<div class="summary missing">(no summary yet - ask Claude to populate state.json)</div>`;

      let extrasHTML = "";
      if (extras.length) {
        extrasHTML = extras.map((e, idx) => {
          const tgt = e.target_text || "";
          const newParts = normParts(e.new_text);
          const newJoined = newParts.join("\n\n");
          const labelTxt = e.label
            ? escapeHtml(e.label)
            : (tgt ? escapeHtml(tgt.slice(0, 80) + (tgt.length > 80 ? "..." : "")) : `Extra edit ${idx + 1}`);
          const tgtAttr = encodeURIComponent(tgt);
          const newAttr = encodeURIComponent(newJoined);
          const splitNote = newParts.length > 1
            ? ` <em class="split-note">(splits into ${newParts.length} paragraphs)</em>`
            : (newJoined === "" ? ` <em class="split-note">(deletes paragraph)</em>` : "");
          return `<div class="extra-edit" data-extra-idx="${idx}" data-target="${tgtAttr}" data-new="${newAttr}">
                    <div class="head">Also edits: <strong>${labelTxt}</strong>${splitNote}</div>
                    ${renderDiff(tgt, newJoined)}
                  </div>`;
        }).join("");
      }

      const primaryParts = normParts(b.suggestion);
      const primaryJoined = primaryParts.join("\n\n");
      const primarySplitNote = primaryParts.length > 1
        ? `<em class="split-note">(splits this paragraph into ${primaryParts.length})</em>`
        : (primaryParts.length === 1 && primaryJoined === ""
            ? `<em class="split-note">(deletes this paragraph)</em>`
            : "");
      const primarySugHTML = primaryParts.length
        ? `<div class="primary-suggestion" data-new="${encodeURIComponent(primaryJoined)}">
             ${primarySplitNote ? `<div class="part-label">${primarySplitNote}</div>` : ""}
             ${renderDiff(b.text, primaryJoined)}
           </div>`
        : "";

      const suggestionHTML = hasSuggestion
        ? `<div class="suggestion">
             <div class="label">Suggested revision (drafted by Claude)${extras.length ? ` &middot; replaces ${1 + extras.length} paragraphs` : ""}</div>
             ${primarySugHTML}
             ${extrasHTML}
             <button class="apply">Apply${extras.length ? " all" : ""}</button>
             <button class="reject">Reject</button>
           </div>`
        : (b.feedback
            ? `<div class="pending-note">Feedback saved. Ask Claude to process feedback-app/state.json, then click Refresh.</div>`
            : "");

      const incomingHTML = incoming.length
        ? incoming.map(inc => {
            const ctx = inc.source_context ? escapeHtml(inc.source_context) : "another paragraph";
            const lbl = inc.label ? ` (${escapeHtml(inc.label)})` : "";
            return `<div class="incoming-edit">
                      &#9432; This paragraph will also be rewritten when you Apply the suggestion on
                      <a class="goto-source" data-source-hash="${escapeHtml(inc.source_hash)}"><strong>${ctx}</strong></a>${lbl}.
                    </div>`;
          }).join("")
        : "";
      html += `
        <div class="${cls.join(" ")}" data-idx="${i}" data-hash="${escapeHtml(b.hash)}">
          <div class="text-col">
            <div class="ctx">${escapeHtml(b.context)}</div>
            ${summaryHTML}
            ${incomingHTML}
            ${renderedBlock(b.text, "paragraph")}
          </div>
          <div class="feedback-col">
            <div class="ctx">feedback</div>
            <textarea placeholder="What should change in this paragraph?">${escapeHtml(b.feedback || "")}</textarea>
            <div>
              <button class="primary save">Save feedback</button>
              <button class="clear-fb">Clear</button>
            </div>
            ${suggestionHTML}
            <div class="msg-slot"></div>
          </div>
        </div>
      `;
    }
  });

  $("#app").innerHTML = html;

  const bulkBtn = document.getElementById("bulk-fb-apply");
  if (bulkBtn) bulkBtn.addEventListener("click", submitBulkFeedback);

  $$(".block.paragraph").forEach(block => {
    $(".save", block).addEventListener("click", () => saveFeedback(block));
    $(".clear-fb", block).addEventListener("click", () => clearFeedback(block));
    const applyBtn = $(".apply", block);
    const rejectBtn = $(".reject", block);
    if (applyBtn) applyBtn.addEventListener("click", () => applySuggestion(block));
    if (rejectBtn) rejectBtn.addEventListener("click", () => rejectSuggestion(block));
    $$(".goto-source", block).forEach(link => {
      link.addEventListener("click", () => {
        const target = document.querySelector(`.block.paragraph[data-hash="${link.dataset.sourceHash}"]`);
        if (target) target.scrollIntoView({ behavior: "smooth", block: "center" });
      });
    });
    $$(".show-source", block).forEach(toggle => {
      toggle.addEventListener("click", () => {
        // The source <pre> is the next sibling of the .row-actions wrapper.
        const wrapper = toggle.closest(".row-actions");
        const src = (wrapper || toggle).nextElementSibling;
        if (!src || !src.classList.contains("source")) return;
        const shown = src.classList.toggle("shown");
        toggle.textContent = shown ? "hide LaTeX source" : "show LaTeX source";
      });
    });
    $$(".speak", block).forEach(btn => {
      btn.addEventListener("click", () => speakBlock(block, btn.dataset.kind, btn));
    });
  });

  wireTTS();
  window.addEventListener("beforeunload", stopSpeaking);
}

async function submitBulkFeedback() {
  const ta = document.getElementById("bulk-fb-text");
  const skipBox = document.getElementById("bulk-fb-skip");
  const btn = document.getElementById("bulk-fb-apply");
  const statusEl = document.querySelector(".bulk-fb-status");
  if (!ta || !btn || !statusEl) return;

  const fb = ta.value.trim();
  if (!fb) {
    statusEl.textContent = "Type a prompt first.";
    statusEl.style.color = "#b91c1c";
    return;
  }

  const note = skipBox && skipBox.checked
    ? " on every paragraph that does not already have feedback"
    : " on every paragraph (overwriting any existing feedback)";
  if (!confirm(`Apply this feedback${note}? Paragraphs with a ready Claude suggestion are always skipped.`)) {
    return;
  }

  btn.disabled = true;
  statusEl.textContent = "Applying...";
  statusEl.style.color = "#6b7280";

  try {
    const res = await fetchJSON("/api/feedback-bulk", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        file: filePath,
        feedback: fb,
        skip_existing: skipBox ? skipBox.checked : true,
      }),
    });
    statusEl.textContent =
      `Set on ${res.set} of ${res.total} paragraphs ` +
      `(skipped: ${res.skipped_existing} with existing feedback, ` +
      `${res.skipped_has_suggestion} with a ready suggestion). Reloading...`;
    statusEl.style.color = "#065f46";
    setTimeout(() => location.reload(), 1500);
  } catch (err) {
    statusEl.textContent = err.message;
    statusEl.style.color = "#b91c1c";
  } finally {
    btn.disabled = false;
  }
}

async function saveFeedback(block) {
  const fb = $("textarea", block).value.trim();
  if (!fb) {
    msg(block, "err", "Type feedback first.");
    return;
  }
  const original = $(".rendered[data-original]", block).dataset.original;
  const hash = block.dataset.hash;
  const context = $(".ctx", block).textContent;
  const btn = $(".save", block);
  btn.disabled = true;
  try {
    const res = await fetchJSON("/api/feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ file: filePath, hash, paragraph: original, context, feedback: fb }),
    });
    if (res && res.hash) block.dataset.hash = res.hash;
    msg(block, "ok", "Feedback saved. Ask Claude to process feedback-app/state.json.");
    block.classList.add("has-feedback");
  } catch (err) {
    msg(block, "err", err.message);
  } finally {
    btn.disabled = false;
  }
}

async function clearFeedback(block) {
  const hash = block.dataset.hash;
  try {
    await fetchJSON("/api/reject", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ file: filePath, hash }),
    });
    $("textarea", block).value = "";
    block.classList.remove("has-feedback", "has-suggestion");
    const sug = $(".suggestion", block);
    if (sug) sug.remove();
    const note = $(".pending-note", block);
    if (note) note.remove();
    msg(block, "ok", "Cleared.");
  } catch (err) {
    msg(block, "err", err.message);
  }
}

async function applySuggestion(block) {
  const oldText = $(".rendered[data-original]", block).dataset.original;
  const hash = block.dataset.hash;

  // Build the edit list. The primary suggestion's joined text lives on
  // .primary-suggestion's data-new attribute (the diff view above replaced
  // the per-part DOM nodes). Each extra-edit div carries its own
  // {data-target, data-new} pair.
  const edits = [];
  const primaryEl = $(".primary-suggestion", block);
  if (primaryEl) {
    const newText = decodeURIComponent(primaryEl.dataset.new || "");
    edits.push({ old: oldText, new: newText });
  }
  $$(".extra-edit", block).forEach(el => {
    const tgt = decodeURIComponent(el.dataset.target || "");
    const nw  = decodeURIComponent(el.dataset.new || "");
    if (tgt) edits.push({ old: tgt, new: nw });
  });

  if (!edits.length) {
    msg(block, "err", "Nothing to apply.");
    return;
  }

  const btn = $(".apply", block);
  const originalLabel = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Applying...";
  try {
    await fetchJSON("/api/apply", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ file: filePath, hash, edits }),
    });
    msg(block, "ok", `Applied ${edits.length} edit(s). Reloading...`);
    // A full reload is the simplest way to refresh every affected block's
    // data-hash, drop the source entry's UI, and clear any incoming-edit
    // notices on target paragraphs.
    setTimeout(() => location.reload(), 350);
  } catch (err) {
    btn.disabled = false;
    btn.textContent = originalLabel;
    msg(block, "err", err.message);
  }
}

async function rejectSuggestion(block) {
  const hash = block.dataset.hash;
  try {
    await fetchJSON("/api/reject", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ file: filePath, hash }),
    });
    msg(block, "ok", `Rejected. Reloading...`);
    // Reload so any "incoming edit" notices on other paragraphs disappear.
    setTimeout(() => location.reload(), 250);
  } catch (err) {
    msg(block, "err", err.message);
  }
}

function msg(block, kind, text) {
  const slot = $(".msg-slot", block);
  if (slot) slot.innerHTML = `<div class="${kind}">${escapeHtml(text)}</div>`;
}

(async () => {
  try {
    if (filePath) await renderFile();
    else await renderIndex();
  } catch (err) {
    $("#app").innerHTML = `<div class="err">${escapeHtml(err.message)}</div>`;
  }
})();
</script>
</body>
</html>
"""


# -- HTTP --------------------------------------------------------------------

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("[server] " + fmt % args + "\n")

    def _json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {}

    def _safe_path(self, rel: str):
        full = (REPO_ROOT / rel).resolve()
        if not str(full).startswith(str(REPO_ROOT)) or not full.exists():
            return None
        return full

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/":
            body = INDEX_HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if path == "/api/files":
            files = sorted(
                str(p.relative_to(REPO_ROOT))
                for p in CHAPTERS_DIR.glob("**/*.tex")
            )
            self._json(200, {"files": files})
            return

        if path == "/api/state-counts":
            self._json(200, aggregate_counts())
            return

        if path == "/api/file":
            qs = urllib.parse.parse_qs(parsed.query)
            rel = qs.get("path", [""])[0]
            full = self._safe_path(rel)
            if full is None:
                self._json(400, {"error": "Invalid file path."})
                return
            text = full.read_text(encoding="utf-8")
            blocks = parse_blocks(text)
            attach_state(blocks, rel)
            self._json(200, {"path": rel, "blocks": blocks})
            return

        self._json(404, {"error": "Not found."})

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        data = self._read_json()

        if path == "/api/feedback":
            file_rel = data.get("file", "")
            client_hash = data.get("hash", "")
            paragraph = data.get("paragraph", "")
            context = data.get("context", "")
            feedback = data.get("feedback", "")
            if not file_rel or not paragraph:
                self._json(400, {"error": "Missing file or paragraph."})
                return
            canonical_hash = save_feedback(file_rel, client_hash, paragraph, context, feedback)
            self._json(200, {"ok": True, "hash": canonical_hash})
            return

        if path == "/api/feedback-bulk":
            file_rel = data.get("file", "")
            feedback = data.get("feedback", "")
            skip_existing = bool(data.get("skip_existing", True))
            if not file_rel or not feedback.strip():
                self._json(400, {"error": "Missing file or feedback."})
                return
            result = save_feedback_bulk(file_rel, feedback, skip_existing)
            if result is None:
                self._json(400, {"error": "Invalid file path."})
                return
            self._json(200, {"ok": True, **result})
            return

        if path == "/api/reject":
            file_rel = data.get("file", "")
            h = data.get("hash", "")
            if not file_rel or not h:
                self._json(400, {"error": "Missing file or hash."})
                return
            reject_entry(file_rel, h)
            self._json(200, {"ok": True})
            return

        if path == "/api/apply":
            file_rel = data.get("file", "")
            h = data.get("hash", "")
            edits = data.get("edits")
            if not edits:
                # Backward compat: single-paragraph form
                old_text = data.get("old", "")
                new_text = data.get("new", "")
                if old_text and new_text is not None:
                    edits = [{"old": old_text, "new": new_text}]
            if not file_rel or not h or not edits:
                self._json(400, {"error": "Missing file, hash, or edits."})
                return
            if not isinstance(edits, list):
                self._json(400, {"error": "edits must be a list."})
                return
            ok, err = apply_edits(file_rel, h, edits)
            if not ok:
                self._json(409, {"error": err})
                return
            self._json(200, {"ok": True})
            return

        self._json(404, {"error": "Not found."})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()

    print(f"[server] repo:  {REPO_ROOT}", file=sys.stderr)
    print(f"[server] state: {STATE_FILE}", file=sys.stderr)
    print(f"[server] open:  http://localhost:{args.port}", file=sys.stderr)

    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", args.port), Handler) as srv:
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\n[server] stopped", file=sys.stderr)


if __name__ == "__main__":
    main()
