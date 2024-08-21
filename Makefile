SHELL = /bin/bash
LUALALATEX_FLAGS = -shell-escape -halt-on-error
MY_TMP_DIR = $(shell echo "$${PWD}/tmp/")
.PHONY: all 

define make_pdf
	rsync -aR --delete src/./ src-build/
	sed -r -e 's/ FJOURNAL/ XJOURNAL/g' -e 's/ JOURNAL/ FJOURNAL/g' "src/knot_theory.bib" | sed -r 's/XJOURNAL/JOURNAL/g' > "${MY_TMP_DIR}/${$@_precision}/build/knot_theory.bib";
	cd "${MY_TMP_DIR}/${$@_precision}/src/" && max_print_line=10000 lualatex $(LUALALATEX_FLAGS) knot-theory.tex;
endef

define make_bib
	$(eval $@_precision = $(1))
	cd "${MY_TMP_DIR}/${$@_precision}/build/" && bibtex knot-theory;
	./src/merridew/fix_bbl_authors.py "${MY_TMP_DIR}/${$@_precision}/build/knot-theory.bbl";
	cd "${MY_TMP_DIR}/${$@_precision}/src/" && max_print_line=10000 lualatex $(LUALALATEX_FLAGS) knot-theory.tex;
	cd "${MY_TMP_DIR}/${$@_precision}/src/" && max_print_line=10000 lualatex $(LUALALATEX_FLAGS) knot-theory.tex;
endef

all: knot-theory.pdf

all-fallback: src/00-meta-latex/new_diagrams.tex src/90-appendix/table_invariants_summary.tex src/90-appendix/table_invariants.tex tools/knotinfo_parsed.json
	mkdir -pv build
	cd src && max_print_line=10000 lualatex -shell-escape -halt-on-error knot-theory.tex;
	cd src && python3 merridew/fix_bbl_authors.py knot-theory.bbl && bibtex knot-theory && python3 merridew/fix_bbl_authors.py knot-theory.bbl ;
	cd src && max_print_line=10000 lualatex -shell-escape -halt-on-error knot-theory.tex;
	cd src && python3 merridew/fix_bbl_authors.py knot-theory.bbl && bibtex knot-theory && python3 merridew/fix_bbl_authors.py knot-theory.bbl ;
	cd src && max_print_line=10000 lualatex -shell-escape -halt-on-error knot-theory.tex;
	cp src/*pdf .

test:
	python3 tools/verify_bib_authors.py --bib src/knot_theory.bib

clean:
	rm -rf tmp *.pdf || true

lint:
	./tools/make_lint.sh

knot-theory.pdf: src/knot-theory.tex src/knot_theory.bib src/*/*.tex
	rsync -avR --delete src/./ src-build/
	cd src-build && sed -r -e 's/ FJOURNAL/ XJOURNAL/g' -e 's/ JOURNAL/ FJOURNAL/g' "knot_theory.bib" | sed -r 's/XJOURNAL/JOURNAL/g' > "tmp-knot_theory.bib" && mv tmp-knot_theory.bib knot_theory.bib
	cd src-build && lualatex -shell-escape -halt-on-error knot-theory.tex && bibtex knot-theory && python3 merridew/fix_bbl_authors.py knot-theory.bbl ;
	cd src-build && lualatex -shell-escape -halt-on-error knot-theory.tex && bibtex knot-theory && python3 merridew/fix_bbl_authors.py knot-theory.bbl ;
	cd src-build && lualatex -shell-escape -halt-on-error knot-theory.tex && bibtex knot-theory && python3 merridew/fix_bbl_authors.py knot-theory.bbl ;
	cp src-build/*pdf .

draft-knot-theory.pdf: src/knot-theory.tex src/knot_theory.bib src/*/*.tex
	$(call make_pdf,draft)
	$(call make_bib,draft)
	cp ${MY_TMP_DIR}/${$@_precision}/build/knot-theory.pdf draft-knot-theory.pdf

### Python

src/00-meta-latex/new_diagrams.tex: tools/diagram_rules/*.py tools/write_diagram_rules.py
	{ echo "#!/usr/bin/env python3"; echo "diagram_commands = dict()"; cat tools/diagram_rules/*.py; cat tools/write_diagram_rules.py; } > tools/write_diagram_rules_2.py
	{ echo; python3 tools/write_diagram_rules_2.py; } > src/00-meta-latex/new_diagrams.tex
	rm tools/write_diagram_rules_2.py

src/90-appendix/table_invariants_summary.tex: tools/convert_knotinfo_json_to_table.py tools/knotinfo_parsed.json
	{ echo; python3 tools/convert_knotinfo_json_to_table.py summary tools/knotinfo_parsed.json; } > src/90-appendix/table_invariants_summary.tex

src/90-appendix/table_invariants.tex: tools/convert_knotinfo_json_to_table.py tools/knotinfo_parsed.json
	{ echo; python3 tools/convert_knotinfo_json_to_table.py all tools/knotinfo_parsed.json; } > src/90-appendix/table_invariants.tex

tools/knotinfo_parsed.json: tools/convert_knotinfo_to_json.py tools/knotinfo_raw.txt
	cd tools && ./convert_knotinfo_to_json.py
