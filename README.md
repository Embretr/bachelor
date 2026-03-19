# Bachelor Thesis — NTNU Gløshaugen

## Setup

### 1. Install LaTeX (if not already installed)

Check if LaTeX is installed:
```bash
which latexmk
```

If not found, install MacTeX (macOS):
```bash
brew install --cask mactex
```
Or download from: https://www.tug.org/mactex/

After installing, restart your terminal and verify:
```bash
latexmk --version
```

### 2. Clone the repo

```bash
git clone <your-github-url>
cd bachelor
```

### 3. Compile the thesis

```bash
make        # compile once → main.pdf
make watch  # auto-recompile on save
make open   # compile and open PDF
make clean  # remove build artefacts
```

---

## Workflow

1. Fill in `context/context.md` with your thesis title, research question, and scope
2. Update `context/disposisjon.md` with your planned chapter structure
3. Open a Claude Code session — it reads `CLAUDE.md` automatically
4. Write chapters in `kapitler/` and references in `bibtex/referanser.bib`
5. Commit and push — your partner pulls and continues

---

## Structure

```
bachelor/
├── CLAUDE.md                  ← Claude Code reads this automatically
├── Makefile                   ← run `make` to compile
├── main.tex                   ← root LaTeX file
├── context/                   ← paste context.md into new Claude chats
├── kapitler/                  ← one .tex file per chapter
├── bibtex/referanser.bib      ← all references (APA 7 / biblatex)
└── kilder/                    ← raw source files (not tracked by git if PDF)
```
