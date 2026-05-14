# Ressursplanlegger — Bachelor Thesis · Claude Instructions

## Writing voice — gjelder på alle nivåer: setning, avsnitt, seksjon, kapittel, hele oppgaven

1. **Minst antall ord for mest info, uten at det føles unaturlig kort.** Hvis noe kan kuttes uten å miste informasjon eller bli klippet stakkato, kutt. Gjelder ord i en setning, setninger i et avsnitt, avsnitt i en seksjon.
2. **Definert én gang er nok.** Ingen gjentakelse innen et avsnitt, på tvers av avsnitt, mellom seksjoner, eller mellom kapitler. Bruk kryssreferanser når et faktum allerede er etablert et annet sted.
3. **Enkelt og presist, lett akademisk.** Ingen komplisering for sin egen skyld. Hverdagsord der det funker; faglige termer kun der de bærer last. Alt skal gi mening og være forklart på en måte en leser med begrenset bakgrunn forstår på første gjennomlesning. Ingen "rare" engelske formuleringer som bare høres faglige ut.
4. **Bygg forståelse, ikke forvirring.** Ikke kast nye lister-av-N på leseren (tre konsepter, fem emner, sju iterasjoner) uten å vise hvordan de forholder seg til det leseren allerede har i hodet. Kun spine-lister står som lister; alt annet er prosa.
5. **Ikke påstå mer enn du vet.** Hvis virkeligheten er løsere enn formuleringen, velg den løsere formuleringen. Overkonkret prosa låser tolkningen feil vei og er ofte vanskelig å belegge.

Disse fem er kontrakten. Brudd er en feil, ikke et stilvalg.

### Eksempler og anti-patterns

**Anti-pattern: løse metaforer som ikke betyr noe konkret.**
- Dårlig: "the two threads informed each other"
- Dårlig: "the design space opened up"
- Bra: "the two influenced each other throughout the project"

**Anti-pattern: jargon uten forklaring (forutsetter at leseren kan rammeverket).**
- Dårlig: "the project entered the DSRM cycle through objectives rather than problem identification"
- Bra: "a standard DSRM project starts from a problem, then sets objectives for a solution, then builds. Our project began with the objectives"

**Anti-pattern: implementation- eller optimization-vokabular i koordinator-prosa.**
- Dårlig: "cold-start race over engine pool, fine-grained cells, warm mode"
- Bra: "for a new group, all three solvers run in parallel and the best result returns to the coordinator"

**Anti-pattern: overkonkret påstand der virkeligheten er løsere.**
- Dårlig: "each interview shaped the next design step; each design step shaped the next interview"
- Bra: "the two influenced each other throughout the project"

**Anti-pattern: punktliste der prosa fungerer like godt.**
- Dårlig: punktliste over fem vekter (kontinuitet, balanse, skift, prioritet, preferanser)
- Bra: "the solver balances driver-vehicle continuity, workload spread, transition minimisation, priority handling, and individual driver preferences when scoring candidate plans"

**Anti-pattern: stakkato. Korte setninger på rekke uten flyt.**
- Dårlig: "The thesis uses DSR. The paradigm fits. The artefact and the writing are built together."
- Bra: "The thesis uses Design Science Research. It suits projects where the artefact and the writing about it are built together rather than in sequence."

**Anti-pattern: defensiv "does not"-prosa.** Ikke fortell leseren hva seksjonen IKKE gjør for å forhånds-avgrense påstander leseren ikke har stilt. Si bare hva den gjør; avgrensninger faller naturlig ut av beskrivelsen. Negative avgrensninger reiser spørsmål bare for å svare dem negativt — konfusjon forkledd som presisjon.
- Dårlig: "The benchmark does not measure utilisation outcomes in production, and it does not retest the visibility gap."
- Bra: la setningen falle. "Synthetic instances" og "identical constraints" gjør avgrensningen implisitt; leseren forstår selv at det ikke er produksjonsmåling, og at §4.1.1 allerede har etablert visibility gap.

**Temasetninger.** Hver paragraf åpner med en setning som anker leseren i hva paragrafen handler om, uten å være meta. Ikke "This section sets out X" eller "Three things are described here". Heller en konkret setning som etablerer poenget paragrafen utvikler.
- Dårlig: "This section describes the research paradigm."
- Bra: "Design Science Research suits a project that has to produce a working system and an account of why it was built that way."

## Spør om informasjon — vi skriver sammen

Skriving er samarbeid. Spør brukeren når en setning trenger et faktum som ikke er etablert (et tall, et navn, en hendelse, en intensjon, et valg mellom to leselige tolkninger). Bedre å stille spørsmål enn å gjette eller å skrive svakt for å unngå spørsmålet. Mange små, presise spørsmål er bedre enn ett stort etterpå.

## Audit-linje per underseksjon

Etter hver underseksjon (eller seksjon hvis den ikke har underseksjoner), legg én kort audit-linje som sier hva du sjekket mot. Audit-linjen skal dekke ALLE reglene over: writing voice (1-5), alle anti-patterns, temasetninger, og at hver konkret påstand er verifisert (fra kilde eller bekreftet av brukeren, ikke fylt inn fordi det høres rett ut). Hvis audit-sjekken fanger en ubelagt påstand, fjern eller spør brukeren før du sender. Format: én linje, kursiv. Eksempel: *Sjekket: temasetning, ingen ny liste-av-N, ingen em-dash, ingen metafor, ingen ubelagt påstand, ingen gjentakelse fra ch1.*

Før du begynner på en ny seksjon: re-les "Writing voice" og "Eksempler og anti-patterns" i denne filen.

**Aldri dra med plausible setninger.** Hvis du under drafting skriver noe konkret om prosjektet (timing, motivasjon, hva teamet trodde, hva som overrasket, hvilken vei ting utviklet seg), still spørsmålet "vet jeg dette?" før du sender. Hvis du fyller inn fordi det høres rett ut: bytt til spørsmål til brukeren. Plausibel er ikke sant.

## The Mandate

This thesis must receive an A. Every word Claude produces is evaluated against that standard before it is written. If a change does not move the thesis closer to an A, it is not made.

The full thesis draft already exists in `result/`. The work now is **revision driven by feedback**: applying what supervisor directives, per-paragraph feedback, and distilled review patterns have established as our voice — to every section, until the prose meets the standard everywhere.

---

## The Three-Folder System

The repo holds three things and three things only:

| Folder | Purpose |
|---|---|
| `result/` | The thesis itself — `.tex` files, `references.bib` |
| `sources/` | Source materials — primary literature notes (`raw/extracted/`), interview transcripts (`interviews/`) |
| `context/` | The feedback corpus — what we have decided the thesis should be |

The core `context/` files loaded at session start (plus the live feedback layer at `feedback-app/state.json`):

- `context/thesis-spine.md` — argument backbone, one sentence per chapter
- `context/glossary.md` — locked terms, including anchor concept definitions
- `context/lessons-learned.md` — generalised rules distilled from feedback rounds; the operative voice
- `context/supervisor-log.md` — chronological NTNU supervisor directives, verbatim
- `context/rubric.md` — A-grade criteria the thesis is judged against

Additional files may be added to `context/` when they earn their place (e.g. benchmark theses for comparison, external references that inform writing decisions). Add deliberately, not reflexively: new files should carry information that does not fit one of the existing five.

---

## Loading Context

Load what the task needs. For most revision work, `context/lessons-learned.md` and `context/glossary.md` plus the affected `.tex` file are enough. Pull in `supervisor-log.md`, `thesis-spine.md`, `rubric.md`, source notes, or the A-thesis benchmark when the task actually calls for them. If the work touches the spine or anchors, read the relevant context file first.

---

## The Operating Model — Feedback-Driven Revision

The work is no longer "draft a section, review it, distil the review". The draft exists. The work is now:

1. **Read the feedback** — per-paragraph notes in `feedback-app/state.json` and supervisor directives in `context/supervisor-log.md`.
2. **Locate the rule** — find the `lessons-learned.md` entry the feedback maps to, or add a new one if the pattern is general (one rule, one short reason, one application note, sourced).
3. **Apply across the corpus** — revise the targeted section AND every other section the rule touches. `lessons-learned.md` indexes "When to apply" for every rule; partial application is the most common way drift returns.
4. **Verify against the rubric** — walk `context/rubric.md` for the affected sections.

The goal is convergence: the prose everywhere reflects what the feedback corpus says the prose should be.

### When new per-paragraph feedback arrives

Per-paragraph feedback comes in through the feedback-app web server. When the user says "process the pending feedback":

1. Read `feedback-app/state.json`.
2. For every entry where `feedback` is set and `suggestion` is null/missing:
   - Draft a LaTeX rewrite that applies the feedback while honouring every rule in `context/lessons-learned.md`.
   - Preserve LaTeX commands (`\textcite`, `\parencite`, `\Cref`, `\textit`, math). No new headings or labels. Make only the changes the feedback requests; do not refactor unrelated wording.
   - Write the rewrite into `suggestion`, set `status: "ready"`.
3. For every entry where `summary` is null/missing and `paragraph` exists:
   - Write a one-sentence summary (≤20 words, plain English) of what the paragraph informs the reader of, into `summary`.
4. Save `state.json` back (preserving JSON formatting, UTF-8). Report counts.

The user reviews each suggestion in the web app and clicks Apply or Reject. **Claude does not touch `.tex` files in this loop** — the web app's Apply button does.

To add summaries for paragraphs the user has not yet given feedback on, the user can ask "summarise the paragraphs in `<file>`". Parse the file with the same paragraph splitter the server uses (split on blank lines, skip heading-only / comment-only chunks), compute each paragraph's 16-char hash, and create entries in `state.json` with `summary` filled in. Do not invent feedback or suggestions on paragraphs the user has not commented on.

### When supervisor feedback arrives

1. Append the directive to `context/supervisor-log.md` — chronological, dated, verbatim.
2. If the directive is general: mirror it as a rule in `context/lessons-learned.md` with **Why:** and **When to apply:** lines and a source attribution back to the supervisor-log entry.
3. If the directive is section-specific: apply directly to the target section.
4. Cross-link both directions (the log entry references the lessons-learned rule, the rule cites the log entry's date).

**Never store supervisor directives only in user memory.** Memory is per-machine; the thesis is co-authored. The log is the single source of truth across collaborators and sessions.

---

## Rule 0 — Plain prose is the primary criterion (supervisor 2026-05-04)

Every section, every paragraph, every sentence must be **clear, simple, and direct**. This rule overrides every other stylistic preference. Before any other rule kicks in, the prose has to satisfy four checks:

1. **Open broad, narrow to one clear message.** The section starts with a framing the reader can already grasp, then narrows in stages to the one specific claim it exists to make. Name that one message in a single sentence before drafting; if you cannot, the section is not ready.
2. **Build understanding, not vocabulary.** Our prose is OURS, not the sources'. Where a source uses a heavy academic term ("combinatorial complexity", "stochastic dispatch", "epistemic asymmetry"), paraphrase plainly first; the technical term, if it appears at all, comes second in parentheses or a follow-on. The goal is a reader with limited technical background understanding on first pass.
3. **Open abstract concepts with everyday-life intuition.** When a paragraph introduces an abstract or technical concept, the FIRST sentence anchors the reader in an everyday situation (a head nurse on a paper rota, a passenger waiting for a delayed train, a parent juggling pickups). Only then move to the technical name.
4. **Sequence the argument linearly — no cross-winds.** The section's paragraphs read as one line of thought going in one direction. The reader must never feel the argument is being pulled sideways while they were going forwards.

A section that fails any of the four is not A-grade no matter how strong its source rigour or anchor coverage. Full statements live in `context/lessons-learned.md` (Top-of-stack mandate plus the four named rules).

---

## Anchor Concept Coherence

Three anchor concepts spine the thesis argument. They are **English proper nouns used consistently across the thesis** — never re-translated to Norwegian, never split, never paraphrased.

- **Efficiency** — improved resource utilization (overtime, idle time, load balance)
- **Control** — coordinator's authority to review and override any algorithm-generated assignment, applying the tacit knowledge the algorithm cannot see
- **Adaptability** — capacity to function meaningfully across companies with different operational rules

Where the spine demands them:

- **Ch 1 §1.2** defines all three verbatim
- **Ch 5 §5.1** organises Primary Findings under them (5.1.1 Efficiency, 5.1.2 Control, 5.1.3 Adaptability)
- **Ch 6 §6.2** connects each SQ-answer paragraph to the anchor it serves
- Other chapters reference at least one anchor where structurally relevant

**Don't drift the anchor names silently.** When writing or rewriting, use the current locked terms verbatim: **Efficiency**, **Control**, **Adaptability**. If the user wants to rename or restructure them, they say so explicitly (as with the 2026-05-09 Trust/control → Control rename). Synonyms that are NOT the anchor — "effektivitet", "kontroll" alone, "tilpasningsdyktighet", "fleksibilitet", "skalerbarhet", "tillit/kontroll", "human oversight", "trust calibration" — should be flagged when read; replace on write unless the user has indicated otherwise.

The phrase "accountable to the traffic coordinator" in the research question is operationalised by the coordinator's authority to review and override every algorithm-generated assignment. Use plainer single verbs ("review", "review and override", "approve or change") rather than reciting the four actions inline (see lessons-learned: *Don't list the four Control actions; use a plainer verb instead*).

**Theoretical anchor for HITL**: Bainbridge (1983) *Ironies of Automation* (`bainbridge1983ironies`), layered with Hoff & Bashir 2015 (trust calibration) and Miller 2019 (explanation as interface).

---

## Writing Defaults (override when iteration calls for it)

These are the defaults the thesis was drafted under. Iterate freely; if a rewrite needs to break one of these for a good reason, do.

- Formal academic English.
- Impersonal constructions ("the results suggest", "the interviews indicate") rather than first-person "we believe / we think". Was a strong preference; no longer absolute.
- `\parencite{key}` for (Author, Year); `\textcite{key}` for Author (Year) in-text.
- Glossary terminology where the term is locked (anchor concepts, key defined terms).
- Em dashes (`---`, `—`) are off by default per earlier user preference. Use commas, parentheses, colons, semicolons, or full stops. If the user wants em dashes back, they will say so.

## LaTeX Conventions

- Figures: `figure` environment with `\caption{}` and `\label{fig:name}`.
- Tables: `table` + `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
- Sections: `\section{}`, `\subsection{}`, `\subsubsection{}`.
- Cross-references: `\Cref{label}` (capitalised) or `\cref{label}` (lowercase).
- No hardcoded page breaks — use `\clearpage` sparingly.

## Compiling

```
make        # compile once → main.pdf
make watch  # auto-recompile on save
make clean  # remove build artefacts
```

Run `make` when the edit could plausibly break compilation (new commands, label changes, structural moves, large rewrites). For small prose tweaks, batch and compile at the end of the session.

---

## Hard Rules (factual safety only)

A short list. Everything else is iteration territory.

- **Do not invent references or data.** Cite only what is in `result/references.bib` or extracted in `sources/raw/extracted/`. Real findings only.
- **Do not write Trimtex or Opptur** as Norwegian transport management systems. They are transcription errors for Timpex and Opter respectively. Only Timpex and Opter are real Norwegian TMS named in the interview pool, and neither produces assignment plans automatically (both are order/invoicing tools).
- **Anchor concept names are user-locked.** Current locked terms verbatim: **Efficiency**, **Control**, **Adaptability** (renamed from "Trust/control" 2026-05-09). The user can rename or restructure these, but Claude does not silently drift them. If a rewrite would change an anchor's name, raise it explicitly.
- **Supervisor-log entries are historical record.** Append new directives chronologically; do not retcon old entries to match present terminology.

---

## Repository Structure

```
bachelor/
├── CLAUDE.md                    ← you are here
├── STATUS.md                    ← current revision phase
├── Makefile                     ← run `make` to compile PDF
├── main.tex                     ← root LaTeX file
│
├── context/                     ← feedback corpus (open, add as needed)
│   ├── thesis-spine.md          ← argument backbone (one sentence per chapter)
│   ├── glossary.md              ← locked terms (incl. anchor concept defs)
│   ├── lessons-learned.md       ← generalised rules distilled from feedback
│   ├── supervisor-log.md        ← NTNU supervisor directives (chronological)
│   ├── rubric.md                ← A-grade criteria
│   ├── a-thesis-amundsen-remoy-2025.md  ← benchmark A-thesis: GenAI in programming education (Alsam pool)
│   ├── a-thesis-trana-jorgensen-2025.md ← benchmark A-thesis: ChatSSB (Alsam pool, DSR + 8 iterations + SusAF)
│   └── a-thesis-brand-et-al-2024.md     ← benchmark A-thesis: 5G underperformance prediction (Skundberg, SimulaMet, Hevner DSR, mid-project pivot)
│
├── sources/                     ← source materials
│   ├── raw/                     ← primary materials and stub notes
│   │   └── extracted/           ← deep-read extracted notes per source
│   ├── interviews/              ← interview transcripts (8 files)
│   ├── README.md
│   └── _template.md             ← source-extraction template
│
├── result/                      ← the thesis
│   ├── chapters/
│   │   ├── ch1/ch1-introduction.tex
│   │   ├── ch2/ch2-theory.tex
│   │   ├── ch3/ch3-method.tex
│   │   ├── ch4/ch4-findings.tex
│   │   ├── ch5/ch5-discussion.tex
│   │   └── ch6/ch6-conclusion.tex
│   └── references.bib
│
└── feedback-app/                ← per-paragraph feedback web server (Python)
    ├── server.py
    ├── state.json               ← live feedback layer
    └── ...
```

Build artefacts (`main.aux`, `main.pdf`, `main.log`, etc.) and the project artefact's own code (`ressursplanlegger/` submodule) live alongside but are not part of the thesis-revision corpus.
