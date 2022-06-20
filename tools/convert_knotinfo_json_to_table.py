#!/usr/bin/env python3
import json
import sys

FIELDS = [
	("name", "nazwa", lambda x: "_{".join(x.split("_")) + "}"),
	# ("crossing_number", "$\\crossing$", None),
	("unknotting_number", "u", None),
	("braid_index", "$\\braid$", None),
	("bridge_index", "$\\bridge$", None),
	("determinant", "det", None),
	("signature", "$\\sigma$", None),
	# ("arf_invariant", "Arf", None),
	("conway_polynomial_vector", "$\\conway$", lambda x: "+".join(x.replace("{", "").replace("}", "").replace(" ", "").replace('"', "").split(",")[2:]).replace("+-", "-").replace("]", "")),
	("symmetry_type", "symetria", lambda x: {"reversible": "odwracalny", "chiral": "chiralny", "fully amphicheiral": "całkowicie", "positive amphicheiral": "+zwierciadlany", "negative amphicheiral": "-zwierciadlany"}.get(x, x + "???")),
	("alternating", "alt.", lambda x: {True: "tak", False: "nie"}.get(x, "???")),
]

def list_values(d):
	print("\\renewcommand*{\\arraystretch}{1.4}")
	print("\\footnotesize")
	print("\\begin{longtable}{" + "c" * len(FIELDS) + "}")
	print("\\hline")
	print(" & ".join([x[1] for x in FIELDS]), "\\\\ \\hline")
	print("\\endhead % all the lines above this will be repeated on every page")

	i = 0
	while True:
		row = list()
		for field in FIELDS:
			key, nice_name, function = field
			value = d[key][i]
			if function is not None:
				value = function(value)
			if key == "bridge_index" and value in [2, "2"]:
				p, q = d["two_bridge_notation"][i].split("/")
				value = f"{{}}^{{{p}}}{{\\mskip -5mu/\\mskip -3mu}}_{{{q}}}"
			value = str(value)
			if key not in ("symmetry_type", "alternating"):
				value = f"${value}$"
			row.append(value)
		print(" & ".join(row), "\\\\")

		# TODO: consider adding "two_bridge_notation"

		i = i + 1
		if i == len(d["crossing_number"]):
			break

		if d["crossing_number"][i] > 12:
			break

	print("\\hline")
	print("\\end{longtable}")
	print("\\normalsize")

def print_summary(d):
	print("\\renewcommand*{\\arraystretch}{1.4}")
	print("\\footnotesize")
	print("\\begin{longtable}{" + "c" * (len(FIELDS) + 1) + "}")
	print("\\hline")
	print(" & ".join([x[1] for x in FIELDS]) + " & all", "\\\\ \\hline")
	print("\\endhead % all the lines above this will be repeated on every page")

	knowledge = dict()

	i = 0
	while True:
		crossings = d["crossing_number"][i]
		for field in FIELDS:
			key, nice_name, function = field
			value = str(d[key][i])
			meta_key = f"{key}-{crossings}"
			if meta_key not in knowledge:
				knowledge[meta_key] = set()
			knowledge[meta_key].add(value)

		i = i + 1
		if i == len(d["crossing_number"]):
			break

		if d["crossing_number"][i] > 12:
			break

	for crossing in range(3, 12 + 1):
		row = [str(crossing)]
		for field in FIELDS[1:]:
			meta_key = f"{field[0]}-{crossing}"
			value = knowledge.get(meta_key, "")
			if value:
				value = len(value)
			row.append(str(value))
		row.append(str(len( knowledge.get(f"name-{crossing}") ) ))
		print(" & ".join(row), "\\\\")

	print("\\hline")
	print("\\end{longtable}")
	print("\\normalsize")

with open(sys.argv[2]) as f:
	data = json.load(f)
	if sys.argv[1] == "all":
		list_values(data)
	elif sys.argv[1] == "summary":
		print_summary(data)