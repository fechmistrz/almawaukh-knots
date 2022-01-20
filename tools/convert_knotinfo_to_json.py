#!/usr/bin/env python3
import json
import re
import collections

# TODO: change '"[2,infty]"'} into 2..infinity
# TODO: check adequate - always True?

def guesser(value):
    """
    Converts cells into one unified format
    """
    if value == "" or not isinstance(value, str):
        return value
    
    translator = {
        "Y": True, "N": False,
        "Large": True, "Small": False,
        "Yes": True, "No": False,
        " ": ""
    }
    if value in translator:
        return translator[value]

    integer_regex = re.compile(r"^-?[0-9]+$")
    if integer_regex.match(value):
        return int(value)

    pair_regex = re.compile(r'"\[(\d+), ?(\d+)\]"')
    pair_match = pair_regex.match(value)
    if pair_match:
        return "..".join(pair_match.groups())

    pretzel_regex = re.compile(r'^"P\([0123456789,-]+\)"$')
    if pretzel_regex.match(value):
        return list(map(int, value.replace('"P(', "").replace(')"', "").split(",")))

    wrong_bracket_regex = re.compile(r'^"\{[0-9,/()-]+\} *"$')
    if wrong_bracket_regex.match(value):
        return eval(value.replace("{", "[").replace("}", "]").replace('"', ''))
    return value

underscore_names = "name	name_anon	diagram	diagram_anon	category	category_anon	knot_atlas	knot_atlas_anon	knotilus_page	knotilus_page_anon	alternating	alternating_anon	name_rank	name_rank_anon	dt_name	dt_name_anon	dt_rank	dt_rank_anon	dt_notation	dt_notation_anon	classical_conway_name	classical_conway_name_anon	conway_notation	conway_notation_anon	two_bridge_notation	two_bridge_notation_anon	fibered	fibered_anon	gauss_notation	gauss_notation_anon	enhanced_gauss_notation	enhanced_gauss_notation_anon	pd_notation	pd_notation_anon	crossing_number	crossing_number_anon	tetrahedral_census_name	tetrahedral_census_name_anon	unknotting_number	unknotting_number_anon	three_genus	three_genus_anon	crosscap_number	crosscap_number_anon	bridge_index	bridge_index_anon	braid_index	braid_index_anon	braid_length	braid_length_anon	braid_notation	braid_notation_anon	signature	signature_anon	nakanishi_index	nakanishi_index_anon	super_bridge_index	super_bridge_index_anon	thurston_bennequin_number	thurston_bennequin_number_anon	arc_index	arc_index_anon	polygon_index	polygon_index_anon	tunnel_number	tunnel_number_anon	morse_novikov_number	morse_novikov_number_anon	alexander_polynomial	alexander_polynomial_anon	alexander_polynomial_vector	alexander_polynomial_vector_anon	jones_polynomial	jones_polynomial_anon	jones_polynomial_vector	jones_polynomial_vector_anon	conway_polynomial	conway_polynomial_anon	conway_polynomial_vector	conway_polynomial_vector_anon	homfly_polynomial	homfly_polynomial_anon	homfly_polynomial_vector	homfly_polynomial_vector_anon	kauffman_polynomial	kauffman_polynomial_anon	kauffman_polynomial_vector	kauffman_polynomial_vector_anon	a_polynomial	a_polynomial_anon	khovanov_polynomial	khovanov_polynomial_anon	khovanov_polynomial_vector	khovanov_polynomial_vector_anon	khovanov_torsion_polynomial	khovanov_torsion_polynomial_anon	khovanov_torsion_polynomial_vector	khovanov_torsion_polynomial_vector_anon	smooth_four_genus	smooth_four_genus_anon	topological_four_genus	topological_four_genus_anon	smooth_4d_crosscap_number	smooth_4d_crosscap_number_anon	topological_4d_crosscap_number	topological_4d_crosscap_number_anon	smooth_concordance_genus	smooth_concordance_genus_anon	topological_concordance_genus	topological_concordance_genus_anon	smooth_concordance_crosscap_number	smooth_concordance_crosscap_number_anon	topological_concordance_crosscap_number	topological_concordance_crosscap_number_anon	algebraic_concordance_order	algebraic_concordance_order_anon	smooth_concordance_order	smooth_concordance_order_anon	topological_concordance_order	topological_concordance_order_anon	ribbon	ribbon_anon	determinant	determinant_anon	seifert_matrix	seifert_matrix_anon	rasmussen_invariant	rasmussen_invariant_anon	ozsvath_szabo_tau_invariant	ozsvath_szabo_tau_invariant_anon	volume	volume_anon	maximum_cusp_volume	maximum_cusp_volume_anon	longitude_translation	longitude_translation_anon	meridian_translation	meridian_translation_anon	longitude_length	longitude_length_anon	meridian_length	meridian_length_anon	other_short_geodesics	other_short_geodesics_anon	symmetry_type	symmetry_type_anon	full_symmetry_group	full_symmetry_group_anon	chern_simons_invariant	chern_simons_invariant_anon	volume_imaginary_part	volume_imaginary_part_anon	arf_invariant	arf_invariant_anon	turaev_genus	turaev_genus_anon	signature_function	signature_function_anon	monodromy	monodromy_anon	small_large	small_large_anon	positive_braid	positive_braid_anon	positive	positive_anon	strongly_quasipositive	strongly_quasipositive_anon	quasipositive	quasipositive_anon	positive_braid_notation	positive_braid_notation_anon	positive_pd_notation	positive_pd_notation_anon	strongly_quasipositive_braid_notation	strongly_quasipositive_braid_notation_anon	quasipositive_braid_notation	quasipositive_braid_notation_anon	fd_clasp_number	fd_clasp_number_anon	width	width_anon	torsion_numbers	torsion_numbers_anon	td_clasp_number	td_clasp_number_anon	l_space	l_space_anon	nu	nu_anon	epsilon	epsilon_anon	quasi_alternating	quasi_alternating_anon	almost_alternating	almost_alternating_anon	adequate	adequate_anon	montesinos_notation	montesinos_notation_anon	boundary_slopes	boundary_slopes_anon	pretzel_notation	pretzel_notation_anon	double_slice_genus	double_slice_genus_anon".split("\t")
english_names = "Name		Diagram		Category		Knot Atlas Page		Knotilus Page		Alternating		Name Rank		DT Name		DT Rank		DT Notation		Conway Name		Conway Notation		Two-Bridge Notation		Fibered		Gauss Notation		Enhanced Gauss Notation		PD Notation		Crossing Number		Tetrahedral Census Name		Unknotting Number		Genus-3D		Crosscap Number		Bridge Index		Braid Index		Braid Length		Braid Notation		Signature		Nakanishi Index		Super Bridge Index		Thurston-Bennequin Number		Arc Index		Stick Number		Tunnel Number		Morse-Novikov Number		Alexander		Alexander (vector)		Jones		Jones (vector)		Conway		Conway (vector)		HOMFLY		HOMFLY (vector)		Kauffman		Kauffman (vector)		A-Polynomial		Khovanov		Khovanov (vector)		Khovanov Torsion		Khovanov Torsion (vector)		Genus-4D		Genus-4D (Top.)		Crosscap Number-4D		Crosscap Number-4D (Top.)		Concordance Genus		Concordance Genus (Top.)		Crosscap Number (Con.)		Crosscap Number (Top. Con.)		Concordance Order (Alg.)		Concordance Order		Concordance Order (Top.)		Ribbon		Determinant		Seifert Matrix		Rasmussen <i>s</i>		Ozsvath-Szabo <i>tau</i>		Volume		Max. Cusp Volume		Longitude Translation		Meridinal Translation		Longitude Length		Meridian Length		Other Short Geodesics		Symmetry Type		Full Symmetry Group		Chern-Simons Invariant		Volume (Imaginary Part)		Arf Invariant		Turaev Genus		Signature function		Monodromy		Small or Large		Positive Braid		Positive		SQ-Positive		Q-Positive		Pos. Braid Notation		Pos. PD Notation		SQ-Postive Braid		Q-Positive Braid		Clasp Number-4D		Width		Torsion Numbers		Clasp Number		L-space		Nu		Epsilon		Quasialternating	Quasialternating Citation	Almost Alternating	Almost Alternating Citation	Adequate	Adequate Citation	Montesinos Notation		Boundary Slopes		Pretzel Notation		Double Slice Genus	".split("\t")

# columns that contain no data (like ribbon) or which we don't need (like diagram)
not_needed_columns = [
    "a_polynomial",
    "diagram",
    "enhanced_gauss_notation",
    "knot_atlas", 
    "knotilus_page",
    "name_rank",
    "ribbon",
    "smooth_concordance_crosscap_number",
    "topological_concordance_crosscap_number",
    "topological_concordance_genus",
]

knowledge = dict()
for underscore_name in underscore_names:
    if underscore_name == "\t":
        continue
    knowledge[underscore_name] = list()

# Pandas requires data in column-oriented format, we have rows :(
with open("knotinfo_raw.txt") as f:
    for line in f:
        words = line.strip().split("\t")
        if "age" not in line and "_" in line:
            for j in range(205):
                knowledge[underscore_names[j]].append(words[j])
# now the date is grouped by columns, not rows

for underscore_name in underscore_names:
    if underscore_name.endswith("_anon") or underscore_name in not_needed_columns or underscore_name not in knowledge:
        throw_away_variable = knowledge.pop(underscore_name)
        continue

    # we don't want to convert this '1' into 1 (integer)
    if underscore_name not in ["full_symmetry_group"]:
        knowledge[underscore_name] = list(map(guesser, knowledge[underscore_name]))

with open("knotinfo_parsed.json", "w") as f:
    f.write(json.dumps(knowledge,sort_keys=False))

print(len(knowledge["other_short_geodesics"]))