SHELL = /bin/bash
LUALALATEX_FLAGS = -shell-escape -halt-on-error
.PHONY: all all-fallback test clean lint

all: knot-theory.pdf

define lualatex_pass
	cd $(1) && max_print_line=10000 lualatex $(LUALALATEX_FLAGS) knot-theory.tex;
endef

define bibtex_pass
	cd $(1) && bibtex knot-theory && python3 merridew/fix_bbl_authors.py knot-theory.bbl ;
endef

knot-theory.pdf: src/knot-theory.tex src/knot_theory.bib src/00-meta-latex/new_diagrams.tex src/90-appendix/table_invariants_summary.tex src/90-appendix/table_invariants.tex src/*/*.tex | src/merridew/createspace.cls
	cd src && rsync -av --delete . ../src-build/
	cd src-build && sed -r -e 's/ FJOURNAL/ XJOURNAL/g' -e 's/ JOURNAL/ FJOURNAL/g' "knot_theory.bib" | sed -r 's/XJOURNAL/JOURNAL/g' > "tmp-knot_theory.bib" && mv tmp-knot_theory.bib knot_theory.bib
	$(call lualatex_pass,src-build)
	$(call bibtex_pass,src-build)
	$(call lualatex_pass,src-build)
	$(call bibtex_pass,src-build)
	$(call lualatex_pass,src-build)
	$(call bibtex_pass,src-build)
	cp src-build/*pdf .

# if you forgot --recurse-submodules when cloning...
src/merridew/createspace.cls:
	git submodule update --init

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

all-fallback: src/00-meta-latex/new_diagrams.tex src/90-appendix/table_invariants_summary.tex src/90-appendix/table_invariants.tex tools/knotinfo_parsed.json | src/merridew/createspace.cls
	$(call lualatex_pass,src)
	$(call bibtex_pass,src)
	$(call lualatex_pass,src)
	$(call bibtex_pass,src)
	$(call lualatex_pass,src)
	cp src/*pdf .

test:
	python3 tools/verify_bib_authors.py --bib src/knot_theory.bib

clean:
	rm -rf tmp src-build *.pdf || true

lint: | src/merridew/createspace.cls
	./tools/make_lint.sh