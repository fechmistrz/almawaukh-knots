#!/usr/bin/env python3
import json

FIELDS = [
	("name", "nazwa", lambda x: "_{".join(x.split("_")) + "}"),
	# ("crossing_number", "$\\crossing$", None),
	("unknotting_number", "u", None),
	("braid_index", "$\\braid$", None),
	("bridge_index", "$\\bridge$", None),
	("determinant", "det", None),
	("signature", "$\\sigma$", None),
	# ("arf_invariant", "Arf", None),
	("conway_polynomial_vector", "$\\conway$", lambda x: "+".join(x.replace("{", "").replace("}", "").replace(" ", "").replace('"', "").split(",")[2:]).replace("+-", "-")),
	("symmetry_type", "symetria", lambda x: {"reversible": "odwracalny", "chiral": "chiralny", "fully amphicheiral": "caLkowicie", "positive amphicheiral": "+zwierciadlany", "negative amphicheiral": "-zwierciadlany"}.get(x, x + "???")),
	("alternating", "alt.", lambda x: {True: "tak", False: "nie"}.get(x, "???")),
]

with open("knotinfo_parsed.json") as f:
	d = json.load(f)

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

