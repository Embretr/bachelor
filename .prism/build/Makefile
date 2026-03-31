MAIN    = main
LATEX   = latexmk
FLAGS   = -pdf -bibtex -interaction=nonstopmode -synctex=1

.PHONY: all watch clean open

## Compile once → main.pdf
all:
	$(LATEX) $(FLAGS) $(MAIN)

## Watch for changes and recompile automatically
watch:
	$(LATEX) $(FLAGS) -pvc $(MAIN)

## Open the PDF (macOS)
open: all
	open $(MAIN).pdf

## Remove all build artefacts
clean:
	$(LATEX) -C $(MAIN)
	rm -f *.synctex.gz *.run.xml *.bcf

## Show help
help:
	@echo "Usage:"
	@echo "  make        — compile main.pdf"
	@echo "  make watch  — auto-recompile on file changes"
	@echo "  make open   — compile and open PDF"
	@echo "  make clean  — remove all build artefacts"
