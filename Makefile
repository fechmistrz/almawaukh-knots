SHELL=/bin/bash

.PHONY: all clean prepare chapter-all release

PDFLATEX_FLAGS = -shell-escape -halt-on-error -output-directory ../build/

define make_pdf
  export max_print_line=$$(tput cols); \
  cd src && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex && cp knot_theory.bib ../build/knot_theory.bib; \
  cd ../build && bibtex knot-theory; \
  cd ../src && ./merridew/fix_bbl_authors.py ../build/knot-theory.bbl && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex && pdflatex $(PDFLATEX_FLAGS) knot-theory.tex; \
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
	./src/merridew/bibliography_sort.py --bib src/knot_theory.bib
	ack -l ' ' | grep -v Makefile | xargs sed -i 's/\xC2\xA0/ /g' || true
	for i in $$(find src -type f -iname '*.tex' | grep -v 'src/90-appendix/dictionary.tex'); do \
		{ echo "" && echo "" && echo "" && cat "$$i" && echo "" && echo "" && echo ""; } | perl -p -e 's/\t/    /g' | cat -s > temporary-file; \
		if ! diff temporary-file "$$i"; then mv -v temporary-file "$$i"; else rm temporary-file; fi; \
	done;
	python3 tools/translate_polish_english.py <(grep -r src --exclude README.md -E -e '% DICTIONARY;.*;.*;.*' -h) > src/90-appendix/dictionary_tmp.tex
	if ! diff src/90-appendix/dictionary{,_tmp}.tex; then mv -v src/90-appendix/dictionary{_tmp,}.tex; else rm src/90-appendix/dictionary_tmp.tex; fi; 
	diff \
		<(grep -Ehor src/ -e '\\label\{.*\}'  | sed -r 's/^\\label//g' | sort -u) \
		<(grep -Ehor src/ -e '\\(page)?ref\{[^}]*\}' | sed -r -e 's/^\\ref//g' -e 's/^\\pageref//g' | sort -u) | sort -k 2 \
		&& echo "No broken/unused references found"

shuffle:
	grep '@' todo-citations.txt | nl | shuf -n 20 | tr -s ' ' | sort -V | awk '{print $$2 " " $$3}'


tools/knotinfo_parsed.json: tools/convert_knotinfo_to_json.py tools/knotinfo_raw.txt
	cd tools && ./convert_knotinfo_to_json.py

