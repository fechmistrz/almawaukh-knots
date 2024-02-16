SHELL=/bin/bash

.PHONY: all clean prepare chapter-all release

PDFLATEX_FLAGS = -shell-escape -halt-on-error -output-directory ../build/

define make_pdf
	export max_print_line=$$(tput cols); \
	cd src && cat knot_theory.bib | sed -r -e 's/ FJOURNAL/ XJOURNAL/g' -e 's/ JOURNAL/ FJOURNAL/g' | sed -r 's/XJOURNAL/JOURNAL/g' > tmp.txt && mv tmp.txt knot_theory.bib; \
	cd src && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex && cp knot_theory.bib ../build/knot_theory.bib; \
	cd ../build && bibtex knot-theory; \
	cd ../src && ./merridew/fix_bbl_authors.py ../build/knot-theory.bbl && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex; \
	cd src && cat knot_theory.bib | sed -r -e 's/ FJOURNAL/ XJOURNAL/g' -e 's/ JOURNAL/ FJOURNAL/g' | sed -r 's/XJOURNAL/JOURNAL/g' > tmp.txt && mv tmp.txt knot_theory.bib; \
	cd ..;
endef

all: prepare chapter-all release
draft: prepare chapter-draft release

test:
	python3 tools/verify_bib_authors.py --bib src/knot_theory.bib

prepare:
	mkdir -p build

chapter-all: build/knot-theory.pdf

chapter-draft: build/draft-knot-theory.pdf

build/knot-theory.pdf: src/knot-theory.tex src/knot_theory.bib src/*/*.tex src/90-appendix/table_invariants_summary.tex src/90-appendix/table_invariants.tex
	$(call make_pdf)

build/draft-knot-theory.pdf: src/*-*/*.tex
	sed 's@\(\\includecomment\)@% \1@g' src/include/head.tex > src/include/head.tex.bak
	mv src/include/head.tex.bak src/include/head.tex
	$(call make_pdf)
	sed 's@%.*\(\\includecomment.*\)@\1@g' src/include/head.tex > src/include/head.tex.bak
	mv src/include/head.tex.bak src/include/head.tex
	mv build/knot-theory.pdf build/draft-knot-theory.pdf

src/00-meta-latex/new_diagrams.tex: tools/diagram_rules/*.py tools/write_diagram_rules.py
	{ echo "#!/usr/bin/env python3"; echo "diagram_commands = dict()"; cat tools/diagram_rules/*.py; cat tools/write_diagram_rules.py; } > tools/write_diagram_rules_2.py
	python3 tools/write_diagram_rules_2.py > src/00-meta-latex/new_diagrams.tex
	rm tools/write_diagram_rules_2.py

src/90-appendix/table_invariants_summary.tex: tools/convert_knotinfo_json_to_table.py tools/knotinfo_parsed.json
	python3 tools/convert_knotinfo_json_to_table.py summary tools/knotinfo_parsed.json > src/90-appendix/table_invariants_summary.tex

src/90-appendix/table_invariants.tex: tools/convert_knotinfo_json_to_table.py tools/knotinfo_parsed.json
	python3 tools/convert_knotinfo_json_to_table.py all tools/knotinfo_parsed.json > src/90-appendix/table_invariants.tex

release:
	for i in build/*knot-theory.pdf; do \
		if [[ "$$i" -nt "$$(basename "$$i")" ]]; then \
			cp "$$i" .; \
		fi; \
	done

clean:
	rm -rf build *.pdf

lint:
	./tools/make_lint.sh

shuffle:
	grep '@' todo-citations.txt | nl | shuf -n 20 | tr -s ' ' | sort -V | awk '{print $$2 " " $$3}'


tools/knotinfo_parsed.json: tools/convert_knotinfo_to_json.py tools/knotinfo_raw.txt
	cd tools && ./convert_knotinfo_to_json.py

