Log supervisor feedback into the three-file system: $ARGUMENTS

Follow the orchestration instructions in `.claude/skills/log-supervisor-feedback/SKILL.md` exactly.
Do not improvise file targets — supervisor directives never go in user memory.
The pipeline classifies each directive (generalisable / section-specific / project-context),
drafts entries for `supervisor-feedback.md`, `lessons-learned.md`, and `outline.md`,
and waits for explicit approval before writing.

Argument is the raw notes from the meeting (Norwegian or English, paraphrase or verbatim).
If no argument is given, the skill will ask the user to paste the notes.
