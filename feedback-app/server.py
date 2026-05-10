#!/usr/bin/env python3
"""
Thesis editor web app - Overleaf-style three-pane UI backed by Claude Code.

Layout:
  +-------------------+--------------------+----------------+
  | file tree         |                    | chat header    |
  | + LaTeX editor    |   PDF viewer       +----------------+
  | (raw .tex)        |   (PDF.js)         | messages       |
  | [Save][Compile]   |   [<- ->] [+/-]    | input + send   |
  +-------------------+--------------------+----------------+

Workflow:
  1. Pick a .tex file from the tree on the left and edit it directly.
  2. Save (Cmd/Ctrl+S or button) writes the file and runs `make`. The PDF
     reloads and scroll position is preserved.
  3. The chat panel persists to feedback-app/chat.json. Type prompts there;
     reference files with @path/to/file.tex; attach editor selections.
  4. In a Claude Code CLI session, ask: "process my chat in
     feedback-app/chat.json". Claude reads chat.json, edits files, and may
     reply by appending an assistant message to chat.json.
  5. Click Refresh in the chat panel to see Claude's reply.

Run:
  python3 feedback-app/server.py            # default port 8765
  python3 feedback-app/server.py --port 9000

State files:
  feedback-app/chat.json  - {"messages": [{"role","ts","text"}, ...]}
  feedback-app/state.json - per-paragraph feedback (legacy; still readable
                            by Claude when it wants to record paragraph-level
                            suggestions, but no longer surfaced in the UI).

The legacy per-paragraph feedback functions (parse_blocks, save_feedback,
apply_edits, attach_state, etc.) and their /api/file, /api/feedback,
/api/apply, /api/reject, /api/edit-paragraph endpoints are kept intact so
existing Claude tooling that touches state.json still works. They are not
exposed in the new UI.
"""

import argparse
import datetime
import hashlib
import http.server
import json
import os
import re
import socketserver
import subprocess
import sys
import threading
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = REPO_ROOT / "result" / "chapters"
STATE_FILE = Path(__file__).resolve().parent / "state.json"
CHAT_FILE = Path(__file__).resolve().parent / "chat.json"

FILE_LOCK = threading.Lock()


# -- LaTeX block parser (legacy, kept for state.json tooling) ---------------

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


# -- state.json (legacy paragraph-feedback persistence) ---------------------

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
    with FILE_LOCK:
        state = load_state()
        fs = state.get(file_rel, {})

        content_to_stored_hash = {}
        for stored_hash, entry in list(fs.items()):
            stored_para = entry.get("paragraph")
            if stored_para:
                content_to_stored_hash[stored_para] = stored_hash

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
            b["explanation"] = entry.get("explanation")
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


def reject_entry(file_rel: str, h: str):
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


def edit_paragraph(file_rel: str, old_text: str, new_text: str):
    full_path = (REPO_ROOT / file_rel).resolve()
    if not str(full_path).startswith(str(REPO_ROOT)):
        return False, "Path outside repo root."
    if not full_path.exists():
        return False, "File not found."
    if not old_text:
        return False, "Missing original text."
    if new_text is None:
        return False, "Missing new text."

    with FILE_LOCK:
        content = full_path.read_text(encoding="utf-8")
        count = content.count(old_text)
        if count == 0:
            return False, "Original paragraph not found in file (reload the page)."
        if count > 1:
            return False, f"Original paragraph appears {count} times - refusing to replace ambiguously."
        new_content = content.replace(old_text, new_text, 1)
        full_path.write_text(new_content, encoding="utf-8")

        old_hash = paragraph_hash(old_text)
        new_hash = paragraph_hash(new_text)
        if old_hash != new_hash:
            state = load_state()
            fs = state.get(file_rel, {})
            if old_hash in fs:
                entry = fs.pop(old_hash)
                entry["paragraph"] = new_text
                fs[new_hash] = entry
                state[file_rel] = fs
                save_state(state)
    return True, None


# -- File tree, file IO, compile --------------------------------------------

ALLOWED_TEX_DIRS = ("result",)
ALLOWED_TEX_ROOT_FILES = {"main.tex"}


def _is_allowed_tex_path(rel: str) -> bool:
    """Whitelist of editable .tex paths: main.tex + everything under result/."""
    if rel == "main.tex":
        return True
    parts = Path(rel).parts
    if parts and parts[0] in ALLOWED_TEX_DIRS and rel.endswith(".tex"):
        return True
    return False


def list_tex_files() -> list:
    out = []
    main = REPO_ROOT / "main.tex"
    if main.exists():
        out.append("main.tex")
    result_dir = REPO_ROOT / "result"
    if result_dir.exists():
        for p in sorted(result_dir.rglob("*.tex")):
            try:
                rel = str(p.relative_to(REPO_ROOT))
            except ValueError:
                continue
            out.append(rel)
    return out


def read_file_text(rel: str):
    if not _is_allowed_tex_path(rel):
        return None, "Path not allowed."
    full = (REPO_ROOT / rel).resolve()
    if not str(full).startswith(str(REPO_ROOT)) or not full.exists():
        return None, "File not found."
    try:
        return full.read_text(encoding="utf-8"), None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def write_file_text(rel: str, content: str):
    if not _is_allowed_tex_path(rel):
        return False, "Path not allowed."
    full = (REPO_ROOT / rel).resolve()
    if not str(full).startswith(str(REPO_ROOT)):
        return False, "Path outside repo root."
    if not full.parent.exists():
        return False, f"Parent directory does not exist: {full.parent}"
    with FILE_LOCK:
        try:
            full.write_text(content, encoding="utf-8")
        except Exception as e:
            return False, f"{type(e).__name__}: {e}"
    return True, None


def run_make() -> dict:
    """Run `make` in REPO_ROOT, return result dict."""
    try:
        proc = subprocess.run(
            ["make"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=240,
        )
        return {
            "ok": proc.returncode == 0,
            "code": proc.returncode,
            "stdout": proc.stdout or "",
            "stderr": proc.stderr or "",
        }
    except FileNotFoundError:
        return {"ok": False, "code": -1, "stdout": "", "stderr": "`make` not found on PATH."}
    except subprocess.TimeoutExpired:
        return {"ok": False, "code": -1, "stdout": "", "stderr": "Compile timed out (>240s)."}
    except Exception as e:
        return {"ok": False, "code": -1, "stdout": "", "stderr": f"{type(e).__name__}: {e}"}


# -- chat.json --------------------------------------------------------------

def load_chat() -> dict:
    if not CHAT_FILE.exists():
        return {"messages": []}
    try:
        data = json.loads(CHAT_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("messages"), list):
            return data
    except json.JSONDecodeError:
        pass
    return {"messages": []}


def save_chat(chat: dict) -> None:
    CHAT_FILE.parent.mkdir(parents=True, exist_ok=True)
    CHAT_FILE.write_text(
        json.dumps(chat, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def append_chat_message(role: str, text: str) -> dict:
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    msg = {"role": role, "ts": ts, "text": text}
    with FILE_LOCK:
        chat = load_chat()
        chat["messages"].append(msg)
        save_chat(chat)
    return msg


def clear_chat() -> None:
    with FILE_LOCK:
        save_chat({"messages": []})


def chat_unanswered() -> list:
    """User messages with no assistant message after them, in order.

    A polling Claude (e.g. via /loop) hits this to cheaply check whether
    there is anything to do before reading the full chat or any files.
    """
    chat = load_chat()
    msgs = chat.get("messages", [])
    out = []
    for i, m in enumerate(msgs):
        if m.get("role") != "user":
            continue
        responded = False
        for j in range(i + 1, len(msgs)):
            if msgs[j].get("role") == "assistant":
                responded = True
                break
        if not responded:
            out.append({**m, "index": i})
    return out


# Prompt the launcher hands the user to paste into Claude Code so chat.json
# is polled and answered automatically. Kept here so the launcher and the
# UI's "Copy auto prompt" button stay in sync.
AUTO_LOOP_PROMPT = (
    "Watch feedback-app/chat.json. Whenever you see user messages without an "
    "assistant message after them, process them: read the referenced files "
    "(@-mentions are paths, optionally with :line or :start-end ranges), "
    "apply the requested revisions to .tex files honouring "
    "context/lessons-learned.md and the rest of CLAUDE.md, run make if a "
    ".tex file changed, then append an assistant message to chat.json "
    "summarising what you changed."
)


# -- HTML --------------------------------------------------------------------

INDEX_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Thesis editor</title>
<style>
  :root { color-scheme: light; }
  html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #1f2937; }
  * { box-sizing: border-box; }

  #app { display: grid; grid-template-columns: 320px 6px 1fr 6px 380px; height: 100vh; min-height: 0; }

  /* ---- Splitters ---- */
  .splitter { background: #e5e7eb; cursor: col-resize; user-select: none; transition: background 0.15s; }
  .splitter:hover, .splitter.dragging { background: #93c5fd; }
  body.resizing { cursor: col-resize; user-select: none; }
  body.resizing * { user-select: none !important; }

  /* ---- Left pane: files + editor ---- */
  .pane.left { display: flex; flex-direction: column; min-width: 0; min-height: 0; background: #fafafa; }
  .files-section { border-bottom: 1px solid #e5e7eb; padding: 0.5rem 0.6rem; max-height: 32vh; overflow-y: auto; flex: 0 0 auto; background: #fff; }
  .files-section h2 { margin: 0 0 0.4rem 0; font-size: 0.7rem; text-transform: uppercase; color: #6b7280; letter-spacing: 0.06em; font-weight: 600; }
  .file-tree { list-style: none; padding: 0; margin: 0; font-family: ui-monospace, Menlo, monospace; font-size: 0.78rem; }
  .file-tree li { margin: 0; }
  .file-tree a { display: block; padding: 0.18rem 0.4rem; border-radius: 3px; color: #1d4ed8; text-decoration: none; cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .file-tree a:hover { background: #eef2ff; }
  .file-tree a.active { background: #2563eb; color: #fff; }
  .file-tree .dirty-mark { color: #b91c1c; margin-left: 0.3rem; }

  .editor-section { display: flex; flex-direction: column; flex: 1 1 auto; min-height: 0; }
  .editor-toolbar { display: flex; gap: 0.4rem; align-items: center; padding: 0.45rem 0.55rem; border-bottom: 1px solid #e5e7eb; background: #f9fafb; font-size: 0.82rem; flex-wrap: wrap; }
  .editor-toolbar button { padding: 0.3rem 0.7rem; font-size: 0.8rem; cursor: pointer; border: 1px solid #d1d5db; background: #fff; border-radius: 4px; font: inherit; }
  .editor-toolbar button:hover:not(:disabled) { background: #f3f4f6; }
  .editor-toolbar button.primary { background: #2563eb; color: #fff; border-color: #2563eb; }
  .editor-toolbar button.primary:hover:not(:disabled) { background: #1d4ed8; }
  .editor-toolbar button:disabled { opacity: 0.5; cursor: progress; }
  .file-label { font-family: ui-monospace, Menlo, monospace; color: #374151; flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 0.78rem; }
  .save-status { font-size: 0.74rem; color: #6b7280; flex-basis: 100%; }
  .save-status.dirty { color: #b91c1c; }
  .save-status.saved { color: #15803d; }
  .save-status.busy { color: #1d4ed8; }

  textarea.editor { flex: 1 1 auto; width: 100%; min-height: 0; resize: none; border: 0; outline: 0; padding: 0.7rem 0.9rem; font-family: ui-monospace, Menlo, "Courier New", monospace; font-size: 0.85rem; line-height: 1.55; tab-size: 2; background: #fff; color: #111827; }
  textarea.editor:disabled { background: #f9fafb; color: #9ca3af; }

  /* ---- Center pane: PDF ---- */
  .pane.center { display: flex; flex-direction: column; min-width: 0; min-height: 0; background: #525659; }
  .pdf-toolbar { display: flex; gap: 0.45rem; align-items: center; padding: 0.4rem 0.7rem; background: #2d3033; color: #d1d5db; font-size: 0.78rem; flex: 0 0 auto; }
  .pdf-toolbar button { background: #3a3e42; color: #e5e7eb; border: 1px solid #4b5258; padding: 0.18rem 0.55rem; border-radius: 3px; cursor: pointer; font-size: 0.78rem; font: inherit; line-height: 1.3; }
  .pdf-toolbar button:hover:not(:disabled) { background: #4b5258; color: #fff; }
  .pdf-toolbar button:disabled { opacity: 0.5; cursor: not-allowed; }
  .pdf-toolbar .compile-status { margin-left: auto; }
  .pdf-toolbar .compile-status.ok { color: #6ee7b7; }
  .pdf-toolbar .compile-status.busy { color: #fde68a; }
  .pdf-toolbar .compile-status.err { color: #fca5a5; cursor: pointer; text-decoration: underline; }
  .pdf-container { flex: 1 1 auto; overflow: auto; position: relative; padding: 6px 0; min-height: 0; }
  .pdf-container canvas { display: block; margin: 8px auto; box-shadow: 0 1px 4px rgba(0,0,0,0.5); background: #fff; }
  .pdf-loading, .pdf-error { color: #fff; text-align: center; padding: 2rem 1rem; font-size: 0.9rem; }
  .pdf-error { color: #fca5a5; }

  /* ---- Right pane: chat ---- */
  .pane.right { display: flex; flex-direction: column; min-width: 0; min-height: 0; background: #fff; }
  .chat-header { padding: 0.5rem 0.7rem; border-bottom: 1px solid #e5e7eb; background: #f9fafb; display: flex; gap: 0.45rem; align-items: center; flex-wrap: wrap; flex: 0 0 auto; }
  .chat-header h2 { margin: 0; font-size: 0.85rem; flex: 0 0 auto; }
  .chat-header .help { font-size: 0.68rem; color: #6b7280; flex-basis: 100%; line-height: 1.4; }
  .chat-header button { font-size: 0.7rem; padding: 0.2rem 0.45rem; background: #fff; border: 1px solid #d1d5db; border-radius: 3px; cursor: pointer; font: inherit; }
  .chat-header button:hover:not(:disabled) { background: #f3f4f6; }
  .chat-messages { flex: 1 1 auto; overflow-y: auto; padding: 0.5rem 0.6rem; min-height: 0; }
  .chat-msg { margin-bottom: 0.55rem; padding: 0.45rem 0.55rem; border-radius: 6px; font-size: 0.84rem; line-height: 1.5; word-wrap: break-word; }
  .chat-msg.user { background: #eef2ff; border: 1px solid #e0e7ff; color: #1e293b; }
  .chat-msg.assistant { background: #ecfdf5; border: 1px solid #a7f3d0; color: #064e3b; }
  .chat-msg .meta { font-size: 0.66rem; color: #6b7280; margin-bottom: 0.25rem; text-transform: uppercase; letter-spacing: 0.04em; }
  .chat-msg .body { white-space: pre-wrap; }
  .chat-msg .body .mention { background: rgba(37, 99, 235, 0.12); color: #1d4ed8; padding: 0 0.2rem; border-radius: 3px; font-family: ui-monospace, Menlo, monospace; font-size: 0.92em; cursor: pointer; }
  .chat-msg .body .mention:hover { background: rgba(37, 99, 235, 0.22); }
  .chat-empty { color: #6b7280; text-align: center; padding: 2rem 1rem; font-size: 0.84rem; line-height: 1.5; }

  .chat-input-row { border-top: 1px solid #e5e7eb; padding: 0.45rem 0.55rem; flex: 0 0 auto; background: #fafafa; position: relative; }
  .chat-input-tools { display: flex; gap: 0.35rem; align-items: center; margin-bottom: 0.35rem; flex-wrap: wrap; }
  .chat-input-tools button { font-size: 0.72rem; padding: 0.2rem 0.5rem; border: 1px solid #d1d5db; background: #fff; border-radius: 3px; cursor: pointer; font: inherit; color: #374151; }
  .chat-input-tools button:hover:not(:disabled) { background: #f3f4f6; }
  .chat-input-tools .selection-info { font-size: 0.7rem; color: #6b7280; }
  .chat-input { width: 100%; min-height: 80px; padding: 0.45rem 0.55rem; font: inherit; font-size: 0.85rem; border: 1px solid #d1d5db; border-radius: 4px; resize: vertical; line-height: 1.45; }
  .chat-input:focus { outline: 0; border-color: #2563eb; box-shadow: 0 0 0 2px rgba(37,99,235,0.15); }
  .chat-actions { display: flex; gap: 0.35rem; margin-top: 0.35rem; align-items: center; }
  .chat-actions button { padding: 0.32rem 0.75rem; font-size: 0.82rem; cursor: pointer; border: 1px solid #d1d5db; border-radius: 4px; background: #fff; font: inherit; }
  .chat-actions button.primary { background: #2563eb; color: #fff; border-color: #2563eb; }
  .chat-actions button.primary:hover:not(:disabled) { background: #1d4ed8; }
  .chat-actions button:disabled { opacity: 0.5; cursor: progress; }
  .chat-actions .hint { font-size: 0.68rem; color: #6b7280; margin-left: auto; }

  /* @-mention dropdown */
  .mention-dropdown { position: absolute; bottom: calc(100% + 4px); left: 0.55rem; right: 0.55rem; max-height: 220px; overflow-y: auto; background: #fff; border: 1px solid #d1d5db; border-radius: 5px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); z-index: 50; font-family: ui-monospace, Menlo, monospace; font-size: 0.78rem; }
  .mention-dropdown[hidden] { display: none; }
  .mention-item { padding: 0.3rem 0.55rem; cursor: pointer; color: #1f2937; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; border-bottom: 1px solid #f3f4f6; }
  .mention-item:last-child { border-bottom: 0; }
  .mention-item.active, .mention-item:hover { background: #2563eb; color: #fff; }
  .mention-empty { padding: 0.5rem 0.55rem; color: #9ca3af; font-style: italic; font-family: -apple-system, sans-serif; font-size: 0.78rem; }

  /* ---- Compile log overlay ---- */
  #compile-output { position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 80vw; max-width: 1100px; max-height: 80vh; background: #1f2937; color: #f3f4f6; padding: 1rem 1.1rem; border-radius: 8px; box-shadow: 0 12px 40px rgba(0,0,0,0.5); display: none; z-index: 200; flex-direction: column; }
  #compile-output.shown { display: flex; }
  #compile-output .head { display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem; flex: 0 0 auto; }
  #compile-output .head h3 { margin: 0; font-size: 0.9rem; flex: 1; color: #fff; }
  #compile-output .head button { background: #374151; border: 0; color: #fff; padding: 0.25rem 0.6rem; cursor: pointer; border-radius: 3px; font-size: 0.78rem; font: inherit; }
  #compile-output .head button:hover { background: #4b5563; }
  #compile-output pre { flex: 1 1 auto; overflow: auto; margin: 0; font-family: ui-monospace, Menlo, monospace; font-size: 0.76rem; line-height: 1.45; white-space: pre-wrap; word-wrap: break-word; background: #0f172a; padding: 0.7rem 0.85rem; border-radius: 5px; color: #e2e8f0; }
  #overlay-bg { position: fixed; inset: 0; background: rgba(0,0,0,0.4); z-index: 199; display: none; }
  #overlay-bg.shown { display: block; }
</style>
</head>
<body>
<div id="app">
  <div class="pane left">
    <div class="files-section">
      <h2>Files</h2>
      <ul class="file-tree" id="file-tree"><li><span style="color:#9ca3af;font-style:italic;">Loading...</span></li></ul>
    </div>
    <div class="editor-section">
      <div class="editor-toolbar">
        <button id="save-btn" class="primary" disabled title="Save and compile (Cmd/Ctrl+S)">Save</button>
        <button id="compile-btn" disabled title="Run make">Compile</button>
        <span class="file-label" id="current-file">No file open</span>
        <span class="save-status" id="save-status"></span>
      </div>
      <textarea class="editor" id="editor" spellcheck="false" placeholder="Pick a file from the tree on the left." disabled></textarea>
    </div>
  </div>

  <div class="splitter" id="splitter-left" title="Drag to resize"></div>

  <div class="pane center">
    <div class="pdf-toolbar">
      <button id="pdf-prev" title="Previous page (k)">&larr;</button>
      <button id="pdf-next" title="Next page (j)">&rarr;</button>
      <span id="pdf-page-info">- / -</span>
      <button id="pdf-zoom-out" title="Zoom out">&minus;</button>
      <button id="pdf-zoom-in" title="Zoom in">+</button>
      <span id="pdf-zoom-info">100%</span>
      <span class="compile-status" id="compile-status">PDF</span>
    </div>
    <div class="pdf-container" id="pdf-container">
      <div class="pdf-loading" id="pdf-loading">Loading PDF...</div>
    </div>
  </div>

  <div class="splitter" id="splitter-right" title="Drag to resize"></div>

  <div class="pane right">
    <div class="chat-header">
      <h2>Chat</h2>
      <button id="chat-refresh" title="Reload chat from chat.json">Refresh</button>
      <button id="chat-clear" title="Clear all messages">Clear</button>
      <button id="copy-auto-prompt" title="Copy a /loop prompt to paste into Claude Code so chat.json is answered automatically">Copy auto prompt</button>
      <span class="help">
        Saved to <code>feedback-app/chat.json</code>.<br>
        <strong>Manual:</strong> in Claude Code ask <em>process my chat in feedback-app/chat.json</em>.<br>
        <strong>Auto:</strong> click <em>Copy auto prompt</em>, paste into Claude Code as <code>/loop &lt;prompt&gt;</code>; chat.json is then polled and answered hands-off.
      </span>
    </div>
    <div class="chat-messages" id="chat-messages"></div>
    <div class="chat-input-row">
      <div class="chat-input-tools">
        <button id="chat-mention-btn" type="button" title="Insert a file reference (or type @)">@ file</button>
        <button id="chat-attach-selection" type="button" title="Insert a reference to the currently selected text in the editor">Attach selection</button>
        <span class="selection-info" id="selection-info"></span>
      </div>
      <textarea class="chat-input" id="chat-input" placeholder="Ask Claude to revise sections, fix references, apply lessons-learned rules. Type @ to mention a file."></textarea>
      <div class="chat-actions">
        <button id="chat-send" class="primary">Send</button>
        <span class="hint">Cmd+Enter to send</span>
      </div>
      <div class="mention-dropdown" id="mention-dropdown" hidden></div>
    </div>
  </div>
</div>

<div id="overlay-bg"></div>
<div id="compile-output">
  <div class="head">
    <h3 id="compile-output-title">Compile log</h3>
    <button id="compile-close">Close</button>
  </div>
  <pre id="compile-output-body"></pre>
</div>

<script type="module">
import * as pdfjsLib from "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.7.76/build/pdf.mjs";
pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.7.76/build/pdf.worker.mjs";

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

const State = {
  files: [],
  currentFile: null,
  loadedContent: "",
  dirty: false,
  pdfDoc: null,
  pdfZoom: 1.2,
  pdfPageCount: 0,
  rendering: false,
  pendingRender: null,
  lastCompile: null,
  chatSig: "",
  chatPollTimer: null,
};

const LS = {
  lastFile: "editor:last-file",
  pdfScroll: "editor:pdf-scroll",
  pdfZoom: "editor:pdf-zoom",
};

function escapeHtml(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

async function api(url, opts = {}) {
  const resp = await fetch(url, opts);
  let data;
  try { data = await resp.json(); }
  catch { data = {}; }
  if (!resp.ok) throw new Error(data.error || ("HTTP " + resp.status));
  return data;
}

// ============ File tree ============

async function loadFileTree() {
  const data = await api("/api/files-tree");
  State.files = data.files || [];
  renderFileTree();
  const last = localStorage.getItem(LS.lastFile);
  let target = (last && State.files.includes(last)) ? last : null;
  if (!target) target = State.files.includes("main.tex") ? "main.tex" : State.files[0];
  if (target) await openFile(target, true);
}

function renderFileTree() {
  const ul = $("#file-tree");
  if (!State.files.length) {
    ul.innerHTML = `<li><span style="color:#9ca3af;font-style:italic;">No .tex files found.</span></li>`;
    return;
  }
  ul.innerHTML = State.files.map(f =>
    `<li><a data-file="${escapeHtml(f)}" title="${escapeHtml(f)}">${escapeHtml(f)}</a></li>`
  ).join("");
  $$("#file-tree a").forEach(a => {
    a.addEventListener("click", () => openFile(a.dataset.file, false));
  });
  highlightActive();
}

function highlightActive() {
  $$("#file-tree a").forEach(a => {
    const active = a.dataset.file === State.currentFile;
    a.classList.toggle("active", active);
    const mark = a.querySelector(".dirty-mark");
    if (active && State.dirty) {
      if (!mark) {
        const span = document.createElement("span");
        span.className = "dirty-mark";
        span.textContent = "*";
        a.appendChild(span);
      }
    } else if (mark) {
      mark.remove();
    }
  });
}

// ============ Editor ============

async function openFile(path, initial) {
  if (!initial && State.dirty) {
    if (!confirm("You have unsaved changes in " + State.currentFile + ". Discard them and switch?")) return;
  }
  let data;
  try {
    data = await api("/api/file-content?path=" + encodeURIComponent(path));
  } catch (err) {
    setSaveStatus("dirty", "Open failed: " + err.message);
    return;
  }
  State.currentFile = path;
  State.loadedContent = data.content || "";
  $("#editor").value = State.loadedContent;
  $("#editor").disabled = false;
  $("#current-file").textContent = path;
  $("#save-btn").disabled = true;
  $("#compile-btn").disabled = false;
  State.dirty = false;
  setSaveStatus("saved", "Loaded " + path + ".");
  localStorage.setItem(LS.lastFile, path);
  highlightActive();
  updateSelectionInfo();
}

function setSaveStatus(kind, text) {
  const el = $("#save-status");
  el.className = "save-status " + (kind || "");
  el.textContent = text || "";
}

function onEditorInput() {
  const cur = $("#editor").value;
  const dirty = cur !== State.loadedContent;
  if (dirty !== State.dirty) {
    State.dirty = dirty;
    highlightActive();
  }
  $("#save-btn").disabled = !dirty;
  setSaveStatus(dirty ? "dirty" : "saved", dirty ? "Unsaved changes." : "Saved.");
}

async function saveAndCompile() {
  if (!State.currentFile) return;
  if (!State.dirty) { compile(); return; }
  const content = $("#editor").value;
  $("#save-btn").disabled = true;
  setSaveStatus("busy", "Saving...");
  try {
    await api("/api/file-write", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ file: State.currentFile, content }),
    });
    State.loadedContent = content;
    State.dirty = false;
    highlightActive();
    setSaveStatus("busy", "Saved. Compiling...");
    await compile();
  } catch (err) {
    setSaveStatus("dirty", "Save failed: " + err.message);
    $("#save-btn").disabled = false;
  }
}

async function compile() {
  const status = $("#compile-status");
  status.className = "compile-status busy";
  status.textContent = "Compiling...";
  status.onclick = null;
  $("#compile-btn").disabled = true;
  try {
    const res = await api("/api/compile", { method: "POST" });
    State.lastCompile = res;
    if (res.ok) {
      status.className = "compile-status ok";
      status.textContent = "Compiled OK";
      status.onclick = () => showCompileLog(res, true);
      await loadPDF(true);
      if (State.dirty) setSaveStatus("dirty", "Unsaved changes.");
      else setSaveStatus("saved", "Saved + compiled.");
    } else {
      status.className = "compile-status err";
      status.textContent = "Compile failed (click for log)";
      status.onclick = () => showCompileLog(res, false);
      setSaveStatus("dirty", "Compile failed.");
    }
  } catch (err) {
    status.className = "compile-status err";
    status.textContent = "Compile error";
    State.lastCompile = { ok: false, code: -1, stdout: "", stderr: err.message };
    status.onclick = () => showCompileLog(State.lastCompile, false);
    setSaveStatus("dirty", "Compile failed.");
  } finally {
    $("#compile-btn").disabled = false;
  }
}

function showCompileLog(res, ok) {
  $("#compile-output-title").textContent = ok ? "Compile log (success)" : "Compile log (failed, exit " + res.code + ")";
  $("#compile-output-body").textContent =
    "=== STDOUT ===\n" + (res.stdout || "(empty)") +
    "\n\n=== STDERR ===\n" + (res.stderr || "(empty)") +
    "\n\nExit: " + res.code;
  $("#compile-output").classList.add("shown");
  $("#overlay-bg").classList.add("shown");
}

function hideCompileLog() {
  $("#compile-output").classList.remove("shown");
  $("#overlay-bg").classList.remove("shown");
}

// ============ PDF ============

async function loadPDF(preserveScroll) {
  if (State.rendering) {
    State.pendingRender = preserveScroll;
    return;
  }
  State.rendering = true;
  const container = $("#pdf-container");
  const savedScroll = preserveScroll
    ? container.scrollTop
    : (parseInt(localStorage.getItem(LS.pdfScroll) || "0", 10) || 0);

  const url = "/api/pdf?t=" + Date.now();
  let pdf;
  try {
    pdf = await pdfjsLib.getDocument({ url, disableAutoFetch: false, disableStream: false }).promise;
  } catch (err) {
    container.innerHTML = `<div class="pdf-error">PDF load failed: ${escapeHtml(err.message)}<br><br>Click <em>Compile</em> to build it.</div>`;
    State.pdfDoc = null;
    State.rendering = false;
    if (State.pendingRender !== null) { const p = State.pendingRender; State.pendingRender = null; loadPDF(p); }
    return;
  }
  State.pdfDoc = pdf;
  State.pdfPageCount = pdf.numPages;

  container.innerHTML = "";
  const dpr = window.devicePixelRatio || 1;
  for (let i = 1; i <= pdf.numPages; i++) {
    const page = await pdf.getPage(i);
    const viewport = page.getViewport({ scale: State.pdfZoom * dpr });
    const cssViewport = page.getViewport({ scale: State.pdfZoom });
    const canvas = document.createElement("canvas");
    canvas.dataset.page = String(i);
    canvas.width = Math.floor(viewport.width);
    canvas.height = Math.floor(viewport.height);
    canvas.style.width = Math.floor(cssViewport.width) + "px";
    canvas.style.height = Math.floor(cssViewport.height) + "px";
    container.appendChild(canvas);
    const ctx = canvas.getContext("2d", { alpha: false });
    await page.render({ canvasContext: ctx, viewport }).promise;
  }
  container.scrollTop = savedScroll;
  updatePageInfo();
  State.rendering = false;
  if (State.pendingRender !== null) {
    const p = State.pendingRender; State.pendingRender = null; loadPDF(p);
  }
}

function bindPDFScroll() {
  const container = $("#pdf-container");
  let saveTimer;
  container.addEventListener("scroll", () => {
    updatePageInfo();
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      localStorage.setItem(LS.pdfScroll, String(container.scrollTop));
    }, 250);
  });
}

function updatePageInfo() {
  if (!State.pdfDoc) {
    $("#pdf-page-info").textContent = "- / -";
    return;
  }
  const container = $("#pdf-container");
  const canvases = $$("#pdf-container canvas");
  let current = 1;
  const probe = container.scrollTop + container.clientHeight / 3;
  for (const c of canvases) {
    if (c.offsetTop <= probe) current = parseInt(c.dataset.page, 10);
    else break;
  }
  $("#pdf-page-info").textContent = current + " / " + State.pdfPageCount;
}

function changeZoom(delta) {
  const newZoom = Math.max(0.5, Math.min(3.0, State.pdfZoom + delta));
  if (newZoom === State.pdfZoom) return;
  State.pdfZoom = newZoom;
  $("#pdf-zoom-info").textContent = Math.round(State.pdfZoom * 100) + "%";
  localStorage.setItem(LS.pdfZoom, String(State.pdfZoom));
  loadPDF(true);
}

function pageNav(delta) {
  const canvases = $$("#pdf-container canvas");
  if (!canvases.length) return;
  const container = $("#pdf-container");
  const top = container.scrollTop;
  let currentIdx = 0;
  for (let i = 0; i < canvases.length; i++) {
    if (canvases[i].offsetTop <= top + 5) currentIdx = i;
    else break;
  }
  const target = Math.max(0, Math.min(canvases.length - 1, currentIdx + delta));
  container.scrollTop = canvases[target].offsetTop - 6;
}

// ============ Chat ============

function chatSignature(messages) {
  if (!messages.length) return "0:";
  const last = messages[messages.length - 1];
  return messages.length + ":" + (last.ts || "") + ":" + (last.role || "");
}

async function loadChat() {
  let data;
  try { data = await api("/api/chat"); }
  catch (err) {
    $("#chat-messages").innerHTML = `<div class="chat-empty">Chat load failed: ${escapeHtml(err.message)}</div>`;
    return;
  }
  const messages = data.messages || [];
  renderChat(messages, "bottom");
  State.chatSig = chatSignature(messages);
}

async function pollChat() {
  let data;
  try { data = await api("/api/chat"); }
  catch { return; }
  const messages = data.messages || [];
  const sig = chatSignature(messages);
  if (sig === State.chatSig) return;
  renderChat(messages, "auto");
  State.chatSig = sig;
}

function startChatPolling(intervalMs) {
  if (State.chatPollTimer) clearInterval(State.chatPollTimer);
  State.chatPollTimer = setInterval(pollChat, intervalMs);
}

function renderChat(messages, scrollMode) {
  const root = $("#chat-messages");
  const wasAtBottom = root.scrollHeight - root.scrollTop - root.clientHeight < 24;
  const prevScroll = root.scrollTop;
  if (!messages.length) {
    root.innerHTML = `<div class="chat-empty">No messages yet.<br><br>Type a prompt below. Use <strong>@</strong> to mention files, <strong>Attach selection</strong> to quote editor text. Then in Claude Code: <em>process my chat in feedback-app/chat.json</em>.</div>`;
    return;
  }
  root.innerHTML = messages.map(m => {
    const role = m.role === "assistant" ? "assistant" : "user";
    const tsTxt = formatTs(m.ts);
    return `<div class="chat-msg ${role}">
      <div class="meta">${escapeHtml(role)} - ${escapeHtml(tsTxt)}</div>
      <div class="body">${renderChatBody(m.text || "")}</div>
    </div>`;
  }).join("");
  if (scrollMode === "bottom" || (scrollMode === "auto" && wasAtBottom)) {
    root.scrollTop = root.scrollHeight;
  } else {
    root.scrollTop = prevScroll;
  }
  $$(".chat-msg .mention").forEach(el => {
    el.addEventListener("click", () => {
      const f = el.dataset.file;
      if (f && State.files.includes(f)) openFile(f, false);
    });
  });
}

function renderChatBody(text) {
  // Highlight @path/to/file.tex mentions; everything else is plain text.
  const escaped = escapeHtml(text);
  return escaped.replace(/@([\w./\-]+\.tex)(?::(\d+(?:-\d+)?))?/g, (m, path, lines) => {
    const linesAttr = lines ? ` title="lines ${escapeHtml(lines)}"` : "";
    const display = lines ? `@${path}:${lines}` : `@${path}`;
    return `<span class="mention" data-file="${escapeHtml(path)}"${linesAttr}>${display}</span>`;
  });
}

function formatTs(ts) {
  if (!ts) return "";
  try {
    const d = new Date(ts);
    if (isNaN(d.getTime())) return ts;
    return d.toLocaleString();
  } catch { return ts; }
}

async function sendChat() {
  const ta = $("#chat-input");
  const text = ta.value.trim();
  if (!text) return;
  $("#chat-send").disabled = true;
  try {
    await api("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ role: "user", text }),
    });
    ta.value = "";
    await loadChat();
  } catch (err) {
    alert("Send failed: " + err.message);
  } finally {
    $("#chat-send").disabled = false;
  }
}

async function clearChatHistory() {
  if (!confirm("Clear all chat messages? This cannot be undone.")) return;
  await api("/api/chat", { method: "DELETE" });
  await loadChat();
}

async function copyAutoPrompt() {
  const btn = $("#copy-auto-prompt");
  const original = btn.textContent;
  let text;
  try {
    const data = await api("/api/auto-prompt");
    text = data.prompt || "";
  } catch (err) {
    btn.textContent = "Failed";
    setTimeout(() => { btn.textContent = original; }, 1500);
    return;
  }
  const cmd = "/loop " + text;
  try {
    await navigator.clipboard.writeText(cmd);
    btn.textContent = "Copied!";
  } catch {
    // Fallback: select textarea content and prompt the user
    window.prompt("Copy this into Claude Code:", cmd);
    btn.textContent = "Copied";
  }
  setTimeout(() => { btn.textContent = original; }, 1500);
}

// ============ @-mention picker ============

const Mention = {
  open: false,
  items: [],
  active: 0,
  triggerStart: -1, // index in textarea where the `@` was typed
  query: "",
};

function openMentionPicker(triggerStart, query) {
  Mention.open = true;
  Mention.triggerStart = triggerStart;
  Mention.query = query;
  filterMention(query);
  renderMention();
}

function closeMentionPicker() {
  if (!Mention.open) return;
  Mention.open = false;
  $("#mention-dropdown").hidden = true;
}

function filterMention(query) {
  const q = (query || "").toLowerCase();
  const matches = State.files.filter(f => f.toLowerCase().includes(q));
  // Bring exact prefix matches first, then substring matches.
  matches.sort((a, b) => {
    const ap = a.toLowerCase().startsWith(q) ? 0 : 1;
    const bp = b.toLowerCase().startsWith(q) ? 0 : 1;
    if (ap !== bp) return ap - bp;
    return a.localeCompare(b);
  });
  Mention.items = matches.slice(0, 12);
  Mention.active = 0;
}

function renderMention() {
  const dd = $("#mention-dropdown");
  if (!Mention.open) { dd.hidden = true; return; }
  if (!Mention.items.length) {
    dd.innerHTML = `<div class="mention-empty">No matching files.</div>`;
    dd.hidden = false;
    return;
  }
  dd.innerHTML = Mention.items.map((f, i) =>
    `<div class="mention-item${i === Mention.active ? " active" : ""}" data-idx="${i}">${escapeHtml(f)}</div>`
  ).join("");
  dd.hidden = false;
  $$(".mention-item", dd).forEach(el => {
    el.addEventListener("mousedown", (e) => {
      e.preventDefault(); // keep textarea focused
      pickMention(parseInt(el.dataset.idx, 10));
    });
  });
}

function pickMention(idx) {
  const item = Mention.items[idx];
  if (!item) { closeMentionPicker(); return; }
  const ta = $("#chat-input");
  const v = ta.value;
  const before = v.slice(0, Mention.triggerStart);
  const after = v.slice(ta.selectionEnd);
  const insert = "@" + item + " ";
  ta.value = before + insert + after;
  const caret = before.length + insert.length;
  ta.setSelectionRange(caret, caret);
  ta.focus();
  closeMentionPicker();
}

function onChatInput(e) {
  const ta = $("#chat-input");
  const caret = ta.selectionStart;
  const v = ta.value;
  // Find the most recent `@` before caret that starts a token.
  let i = caret - 1;
  while (i >= 0) {
    const ch = v[i];
    if (ch === "@") {
      const prev = i > 0 ? v[i - 1] : " ";
      // Only treat as trigger if @ is at start, after whitespace, or after newline.
      if (i === 0 || /\s/.test(prev)) {
        const query = v.slice(i + 1, caret);
        // If the query contains whitespace, the mention has ended; close.
        if (/\s/.test(query)) break;
        openMentionPicker(i, query);
        return;
      }
      break;
    }
    if (/\s/.test(ch)) break;
    i--;
  }
  closeMentionPicker();
}

function onChatKeydown(e) {
  if (Mention.open) {
    if (e.key === "ArrowDown") { e.preventDefault(); Mention.active = Math.min(Mention.items.length - 1, Mention.active + 1); renderMention(); return; }
    if (e.key === "ArrowUp") { e.preventDefault(); Mention.active = Math.max(0, Mention.active - 1); renderMention(); return; }
    if (e.key === "Enter" && !e.shiftKey && !e.metaKey && !e.ctrlKey) {
      e.preventDefault();
      pickMention(Mention.active);
      return;
    }
    if (e.key === "Tab") { e.preventDefault(); pickMention(Mention.active); return; }
    if (e.key === "Escape") { e.preventDefault(); closeMentionPicker(); return; }
  }
  // Cmd/Ctrl+Enter: send
  if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
    e.preventDefault();
    sendChat();
  }
}

// ============ Editor selection -> chat ============

function getEditorSelection() {
  const ta = $("#editor");
  if (!ta || ta.disabled) return null;
  const start = ta.selectionStart;
  const end = ta.selectionEnd;
  if (start === end) return null;
  const text = ta.value.slice(start, end);
  const before = ta.value.slice(0, start);
  const startLine = (before.match(/\n/g) || []).length + 1;
  const span = ta.value.slice(start, end);
  const endLine = startLine + (span.match(/\n/g) || []).length;
  return { start, end, text, startLine, endLine };
}

function updateSelectionInfo() {
  const sel = getEditorSelection();
  const info = $("#selection-info");
  const btn = $("#chat-attach-selection");
  if (!sel) {
    info.textContent = "";
    btn.disabled = false; // still allow click; we'll just warn
    return;
  }
  const lines = sel.startLine === sel.endLine ? `line ${sel.startLine}` : `lines ${sel.startLine}-${sel.endLine}`;
  info.textContent = `${State.currentFile || "(file)"} - ${lines}`;
  btn.disabled = false;
}

function attachEditorSelection() {
  const sel = getEditorSelection();
  if (!sel) {
    alert("Select text in the editor first, then click 'Attach selection'.");
    return;
  }
  const file = State.currentFile || "(unknown.tex)";
  const lineRange = sel.startLine === sel.endLine ? String(sel.startLine) : sel.startLine + "-" + sel.endLine;
  const quoted = sel.text.split("\n").map(l => "> " + l).join("\n");
  const ref = "@" + file + ":" + lineRange + "\n" + quoted + "\n\n";

  const ta = $("#chat-input");
  const caret = ta.selectionStart;
  const v = ta.value;
  const before = v.slice(0, caret);
  const after = v.slice(ta.selectionEnd);
  // Insert a leading newline if previous char isn't one and we're not at the start.
  const lead = (before && !before.endsWith("\n")) ? "\n" : "";
  const insert = lead + ref;
  ta.value = before + insert + after;
  const newCaret = before.length + insert.length;
  ta.setSelectionRange(newCaret, newCaret);
  ta.focus();
}

// ============ Wire-up ============

function bindKeys() {
  document.addEventListener("keydown", (e) => {
    const isMac = /Mac/i.test(navigator.platform);
    const mod = isMac ? e.metaKey : e.ctrlKey;
    if (mod && e.key.toLowerCase() === "s") {
      e.preventDefault();
      saveAndCompile();
      return;
    }
    if (e.key === "Escape" && $("#compile-output").classList.contains("shown")) {
      hideCompileLog();
    }
  });
}

// ============ Splitters (resizable panes) ============

const SPLITTER_BAR = 6; // keep in sync with .splitter width in CSS
const MIN_LEFT = 220;
const MIN_CENTER = 240;
const MIN_RIGHT = 260;
const LS_LEFT_W = "editor:left-width";
const LS_RIGHT_W = "editor:right-width";

function applyPaneWidths(leftPx, rightPx) {
  const app = $("#app");
  const total = app.clientWidth;
  const avail = total - 2 * SPLITTER_BAR;
  leftPx = Math.max(MIN_LEFT, Math.min(leftPx, avail - MIN_CENTER - MIN_RIGHT));
  rightPx = Math.max(MIN_RIGHT, Math.min(rightPx, avail - MIN_CENTER - leftPx));
  app.style.gridTemplateColumns = `${leftPx}px ${SPLITTER_BAR}px 1fr ${SPLITTER_BAR}px ${rightPx}px`;
  return { leftPx, rightPx };
}

function getCurrentPaneWidths() {
  const left = $(".pane.left").getBoundingClientRect().width;
  const right = $(".pane.right").getBoundingClientRect().width;
  return { leftPx: left, rightPx: right };
}

function bindSplitters() {
  const splitterLeft = $("#splitter-left");
  const splitterRight = $("#splitter-right");

  function startDrag(side, splitterEl, ev) {
    ev.preventDefault();
    const startX = ev.clientX;
    const { leftPx: startLeft, rightPx: startRight } = getCurrentPaneWidths();
    splitterEl.classList.add("dragging");
    document.body.classList.add("resizing");

    function onMove(e) {
      const dx = e.clientX - startX;
      if (side === "left") applyPaneWidths(startLeft + dx, startRight);
      else applyPaneWidths(startLeft, startRight - dx);
    }
    function onUp() {
      document.removeEventListener("mousemove", onMove);
      document.removeEventListener("mouseup", onUp);
      splitterEl.classList.remove("dragging");
      document.body.classList.remove("resizing");
      const { leftPx, rightPx } = getCurrentPaneWidths();
      localStorage.setItem(LS_LEFT_W, String(Math.round(leftPx)));
      localStorage.setItem(LS_RIGHT_W, String(Math.round(rightPx)));
    }
    document.addEventListener("mousemove", onMove);
    document.addEventListener("mouseup", onUp);
  }

  splitterLeft.addEventListener("mousedown", (e) => startDrag("left", splitterLeft, e));
  splitterRight.addEventListener("mousedown", (e) => startDrag("right", splitterRight, e));

  // Double-click to reset that splitter to default.
  splitterLeft.addEventListener("dblclick", () => {
    const { rightPx } = getCurrentPaneWidths();
    applyPaneWidths(320, rightPx);
    localStorage.removeItem(LS_LEFT_W);
  });
  splitterRight.addEventListener("dblclick", () => {
    const { leftPx } = getCurrentPaneWidths();
    applyPaneWidths(leftPx, 380);
    localStorage.removeItem(LS_RIGHT_W);
  });

  // Re-clamp on window resize so panes never crowd out the center.
  window.addEventListener("resize", () => {
    const { leftPx, rightPx } = getCurrentPaneWidths();
    applyPaneWidths(leftPx, rightPx);
  });

  // Restore persisted widths.
  const savedLeft = parseInt(localStorage.getItem(LS_LEFT_W) || "0", 10);
  const savedRight = parseInt(localStorage.getItem(LS_RIGHT_W) || "0", 10);
  if (savedLeft > 0 || savedRight > 0) {
    applyPaneWidths(savedLeft || 320, savedRight || 380);
  }
}

function init() {
  // Restore zoom
  const savedZoom = parseFloat(localStorage.getItem(LS.pdfZoom) || "1.2");
  State.pdfZoom = isFinite(savedZoom) && savedZoom > 0 ? savedZoom : 1.2;
  $("#pdf-zoom-info").textContent = Math.round(State.pdfZoom * 100) + "%";

  $("#editor").addEventListener("input", () => { onEditorInput(); updateSelectionInfo(); });
  $("#editor").addEventListener("keyup", updateSelectionInfo);
  $("#editor").addEventListener("mouseup", updateSelectionInfo);
  $("#editor").addEventListener("blur", updateSelectionInfo);

  $("#save-btn").addEventListener("click", saveAndCompile);
  $("#compile-btn").addEventListener("click", compile);

  $("#pdf-prev").addEventListener("click", () => pageNav(-1));
  $("#pdf-next").addEventListener("click", () => pageNav(1));
  $("#pdf-zoom-in").addEventListener("click", () => changeZoom(0.1));
  $("#pdf-zoom-out").addEventListener("click", () => changeZoom(-0.1));

  $("#chat-send").addEventListener("click", sendChat);
  $("#chat-refresh").addEventListener("click", loadChat);
  $("#chat-clear").addEventListener("click", clearChatHistory);
  $("#copy-auto-prompt").addEventListener("click", copyAutoPrompt);
  $("#chat-input").addEventListener("input", onChatInput);
  $("#chat-input").addEventListener("keydown", onChatKeydown);
  $("#chat-input").addEventListener("blur", () => setTimeout(closeMentionPicker, 120));

  $("#chat-mention-btn").addEventListener("click", () => {
    const ta = $("#chat-input");
    ta.focus();
    const caret = ta.selectionStart;
    const v = ta.value;
    const lead = (caret > 0 && !/\s/.test(v[caret - 1])) ? " @" : "@";
    ta.value = v.slice(0, caret) + lead + v.slice(ta.selectionEnd);
    const newCaret = caret + lead.length;
    ta.setSelectionRange(newCaret, newCaret);
    onChatInput();
  });
  $("#chat-attach-selection").addEventListener("click", attachEditorSelection);

  $("#compile-close").addEventListener("click", hideCompileLog);
  $("#overlay-bg").addEventListener("click", hideCompileLog);

  bindPDFScroll();
  bindKeys();
  bindSplitters();

  Promise.all([
    loadFileTree(),
    loadChat(),
    loadPDF(false),
  ]).catch(err => console.error(err));

  startChatPolling(2000);
}

init();
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
        self.send_header("Cache-Control", "no-store")
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

    def _serve_pdf(self):
        pdf = REPO_ROOT / "main.pdf"
        if not pdf.exists():
            self._json(404, {"error": "main.pdf not found - click Compile."})
            return
        try:
            data = pdf.read_bytes()
        except Exception as e:
            self._json(500, {"error": f"PDF read failed: {e}"})
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/pdf")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/":
            body = INDEX_HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return

        # ---- New editor endpoints ----

        if path == "/api/files-tree":
            self._json(200, {"files": list_tex_files()})
            return

        if path == "/api/file-content":
            qs = urllib.parse.parse_qs(parsed.query)
            rel = qs.get("path", [""])[0]
            content, err = read_file_text(rel)
            if err:
                self._json(400, {"error": err})
                return
            self._json(200, {"path": rel, "content": content})
            return

        if path == "/api/pdf":
            self._serve_pdf()
            return

        if path == "/api/chat":
            self._json(200, load_chat())
            return

        if path == "/api/chat/unanswered":
            self._json(200, {"messages": chat_unanswered()})
            return

        if path == "/api/auto-prompt":
            self._json(200, {"prompt": AUTO_LOOP_PROMPT})
            return

        # ---- Legacy state.json endpoints (kept for Claude tooling) ----

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

    def do_DELETE(self):
        path = urllib.parse.urlparse(self.path).path
        if path == "/api/chat":
            clear_chat()
            self._json(200, {"ok": True})
            return
        self._json(404, {"error": "Not found."})

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        data = self._read_json()

        # ---- New editor endpoints ----

        if path == "/api/file-write":
            file_rel = data.get("file", "")
            content = data.get("content", "")
            if not file_rel:
                self._json(400, {"error": "Missing file."})
                return
            if not isinstance(content, str):
                self._json(400, {"error": "Content must be a string."})
                return
            ok, err = write_file_text(file_rel, content)
            if not ok:
                self._json(400, {"error": err})
                return
            self._json(200, {"ok": True})
            return

        if path == "/api/compile":
            res = run_make()
            self._json(200, res)
            return

        if path == "/api/chat":
            role = (data.get("role") or "user").strip() or "user"
            if role not in ("user", "assistant", "system"):
                role = "user"
            text = data.get("text", "")
            if not isinstance(text, str) or not text.strip():
                self._json(400, {"error": "text is required."})
                return
            msg = append_chat_message(role, text)
            self._json(200, {"ok": True, "message": msg})
            return

        # ---- Legacy state.json endpoints ----

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

        if path == "/api/reject":
            file_rel = data.get("file", "")
            h = data.get("hash", "")
            if not file_rel or not h:
                self._json(400, {"error": "Missing file or hash."})
                return
            reject_entry(file_rel, h)
            self._json(200, {"ok": True})
            return

        if path == "/api/edit-paragraph":
            file_rel = data.get("file", "")
            old_text = data.get("old", "")
            new_text = data.get("new", "")
            if not file_rel or old_text is None or new_text is None:
                self._json(400, {"error": "Missing file/old/new."})
                return
            ok, err = edit_paragraph(file_rel, old_text, new_text)
            if not ok:
                self._json(409, {"error": err})
                return
            self._json(200, {"ok": True, "new_hash": paragraph_hash(new_text)})
            return

        if path == "/api/apply":
            file_rel = data.get("file", "")
            h = data.get("hash", "")
            edits = data.get("edits")
            if not edits:
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
    print(f"[server] chat:  {CHAT_FILE}", file=sys.stderr)
    print(f"[server] open:  http://localhost:{args.port}", file=sys.stderr)

    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", args.port), Handler) as srv:
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\n[server] stopped", file=sys.stderr)


if __name__ == "__main__":
    main()
