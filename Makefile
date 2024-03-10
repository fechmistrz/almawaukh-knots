SHELL = /bin/bash
LUALALATEX_FLAGS = -shell-escape -halt-on-error -output-directory ../build/
MY_TMP_DIR = $(shell echo "$${PWD}/tmp/")
.PHONY: all 

define make_pdf
	$(eval $@_precision = $(1))
	mkdir -p "${MY_TMP_DIR}/${$@_precision}/build/"
	rsync -aR --delete --exclude tmp --exclude .git "$${PWD}/./" "${MY_TMP_DIR}/${$@_precision}/"; 
	mkdir -p "${MY_TMP_DIR}/${$@_precision}/build/"
	sed -r -e 's/ FJOURNAL/ XJOURNAL/g' -e 's/ JOURNAL/ FJOURNAL/g' "src/knot_theory.bib" | sed -r 's/XJOURNAL/JOURNAL/g' > "${MY_TMP_DIR}/${$@_precision}/build/knot_theory.bib";
	if [ "${$@_precision}" != "slow" ]; then sed 's@\(\\includecomment\)@% \1@g' src/include/head.tex > "${MY_TMP_DIR}/${$@_precision}/src/include/head.tex"; fi
	cd "${MY_TMP_DIR}/${$@_precision}/src/" && max_print_line=10000 lualatex $(LUALALATEX_FLAGS) knot-theory.tex;
	cd "${MY_TMP_DIR}/${$@_precision}/build/" && bibtex knot-theory;
	./src/merridew/fix_bbl_authors.py "${MY_TMP_DIR}/${$@_precision}/build/knot-theory.bbl";
	cd "${MY_TMP_DIR}/${$@_precision}/src/" && max_print_line=10000 lualatex $(LUALALATEX_FLAGS) knot-theory.tex;
	cd "${MY_TMP_DIR}/${$@_precision}/src/" && max_print_line=10000 lualatex $(LUALALATEX_FLAGS) knot-theory.tex;
	if [ "${$@_precision}" == "fast" ]; then mv ${MY_TMP_DIR}/${$@_precision}/build/knot-theory.pdf ${MY_TMP_DIR}/${$@_precision}/build/draft-knot-theory.pdf; fi
	cp ${MY_TMP_DIR}/${$@_precision}/build/*.pdf .; 
endef

all: knot-theory.pdf

test:
	python3 tools/verify_bib_authors.py --bib src/knot_theory.bib

clean:
	rm -rf tmp *.pdf || true

lint:
	./tools/make_lint.sh

knot-theory.pdf: src/knot-theory.tex src/knot_theory.bib src/*/*.tex
	$(call make_pdf,slow)

draft-knot-theory.pdf: src/knot-theory.tex src/knot_theory.bib src/*/*.tex
	$(call make_pdf,fast)

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
