SHELL=/bin/bash

.PHONY: all clean prepare chapter-all release

PDFLATEX_FLAGS = -shell-escape -halt-on-error -output-directory ../build/

define make_pdf
  export max_print_line=$$(tput cols); \
  cd src && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex && cp knot_theory.bib ../build/knot_theory.bib; \
  cd ../build && bibtex knot-theory && makeindex knot-theory; \
  cd ../src && ./merridew/fix_bbl_authors.py ../build/knot-theory.bbl && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex; \
  cd ..;
endef

all: prepare chapter-all release
draft: prepare chapter-draft release

prepare:
	mkdir -p build

precommit:
	./src/merridew/bibliography_sort.py --bib src/knot_theory.bib
	ack -l ' ' | xargs sed -i 's/ / /g' || true
	for i in $$(find src -type f -iname '*.tex'); do \
	    sed '$$a\' $$i > file && mv file $$i; \
	    perl -p -i -e 's/\t/    /g' "$$i"; \
	done;
	python3 tools/translate_polish_english.py <(grep -r src -E -e '% DICTIONARY;.*;.*;.*' -h) > src/90-appendix/dictionary.tex
	diff \
		<(grep -Ehor src/ -e '\\label\{.*\}'  | sed -r 's/^\\label//g' | sort -u) \
		<(grep -Ehor src/ -e '\\(page)?ref\{[^}]*\}' | sed -r -e 's/^\\ref//g' -e 's/^\\pageref//g'   | sort -u) | sort -k 2 \
		&& echo "No broken/unused references found"

chapter-all: build/knot-theory.pdf

chapter-draft: build/draft-knot-theory.pdf

build/knot-theory.pdf: src/knot-theory.tex src/*/*.tex
	$(call make_pdf)

build/draft-knot-theory.pdf: src/*-*/*.tex
	sed 's@\(\\includecomment\)@% \1@g' src/include/head.tex > src/include/head.tex.bak
	mv src/include/head.tex.bak src/include/head.tex
	$(call make_pdf)
	sed 's@%.*\(\\includecomment.*\)@\1@g' src/include/head.tex > src/include/head.tex.bak
	mv src/include/head.tex.bak src/include/head.tex
	mv build/knot-theory.pdf build/draft-knot-theory.pdf

release:
	cp build/*knot-theory.pdf ./

src/00-meta-latex/new_diagrams.tex: tools/diagram_rules/*.py
	{ echo "#!/usr/bin/env python3"; echo "diagram_commands = dict()"; cat tools/diagram_rules/*.py; cat tools/write_diagram_rules.py; } > tools/write_diagram_rules_2.py
	python tools/write_diagram_rules_2.py > src/00-meta-latex/new_diagrams.tex
	rm tools/write_diagram_rules_2.py


clean:
	rm -rf build *.pdf
