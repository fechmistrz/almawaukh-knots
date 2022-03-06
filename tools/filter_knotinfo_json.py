#!/usr/bin/env python3

import json
import pandas as pd

def jones_collisions(knots):
    jones = dict()
    for knot in knots.itertuples():
        if knot.category not in [3, 4, 5, 6, 7, 8, 9, 10]:
            break

        key_1 = eval(knot.jones_polynomial_vector)
        key_2 = [-key_1[1], -key_1[0]] + key_1[-1:1:-1]
        key = min(str(key_1), str(key_2))
        # 5_1    [2, 7, 1, 0, 1, -1, 1, -1]
        # 10_132 [-7, -2, -1, 1, -1, 1, 0, 1]
        # due to orientation issues

        value = knot.name
        if key not in jones:
            jones[key] = list()
        jones[key].append(value)

    print("Jones does not distinguish:")
    for v in jones.values():
        if len(v) > 1:
            print("/".join(v))
    return


def trivial_alexander(knots):
    print("Knots with trivial Alexander polynomial:")
    for knot in knots.itertuples():
        # print(knot)
        alexander = eval(knot.alexander_polynomial_vector)
        alexander_span = alexander[1] - alexander[0]
        if alexander_span == 0:
            print(knot.name)
    return


def unknotting_sigma(knots):
    print("Knots that satisfy 2u >= sigma?")

    all_knots = 0
    unknown_knots = 0
    double_sigma = 0

    for knot in knots.itertuples():
        if knot.crossing_number >= 12:
            continue

        all_knots = all_knots + 1
        if ".." in str(knot.unknotting_number):
            unknown_knots = unknown_knots + 1
        elif 2 * int(knot.unknotting_number) == abs(knot.signature):
            double_sigma = double_sigma + 1

    print(f"{all_knots} (all knots)")
    print(f"{unknown_knots} (unknown crossing number)")
    print(f"{double_sigma} (2u = |sigma|)")
    return


def invisible_knots(knots):
    print("Invisible knots (with det = 1):")
    for knot in knots.itertuples():
        if knot.determinant == 1:
            print(knot.name)
    return


def bankwitz_application(knots):
    examples = dict()
    crowell = dict()
    torus_knots = ["3_1", "5_1", "7_1", "8_19", "9_1", "10_124", "11a_367"]
    for knot in knots.itertuples():
        cr = knot.crossing_number
        det = knot.determinant
        if det < cr:
            if cr not in examples:
                examples[cr] = list()
            examples[cr].append(knot.name)
        elif not knot.alternating and knot.name not in torus_knots and knot.determinant + 3 < 2 * knot.crossing_number:
            if cr not in crowell:
                crowell[cr] = list()
            crowell[cr].append(knot.name)
            
    print("Nonalternating knots because det < cr:")
    for k, v in examples.items():
        print(f"{len(v)} knot(s) with cr = {k}: {', '.join(v)}")

    print("Nonalternating knots because det + 3 < 2cr:")
    for k, v in crowell.items():
        print(f"{len(v)} knot(s) with cr = {k}: {', '.join(v)}")

    return


def alexander_genus(knots):
    examples = dict()
    print("Knots for which span Delta/2 < g without equality:")
    for knot in knots.itertuples():
        alexander = eval(knot.alexander_polynomial_vector)
        span = abs(alexander[1] - alexander[0])
        g = knot.three_genus
        if 2*g - span <= 1:
            continue
        if g not in examples:
            examples[g] = list()
        examples[g].append(knot.name)
    for k, v in examples.items():
        print(f"g = {k}, knots: {', '.join(v)}")
    return


def genus_prime(knots):
    genus_one = list()
    genus_more = list()
    print("Does genus often detect primality?")
    for knot in knots.itertuples():
        g = knot.three_genus
        if g == 1:
            genus_one.append(knot.name)
        else:
            genus_more.append(knot.name)

    print(f"{len(genus_one)} knots with g = 1: {', '.join(genus_one)}")
    print(f"{len(genus_more)} knots with g > 1")
    return


def symmetric_not_acheiral(knots):
    signature_zero = []
    signature_nonzero = []
    for knot in knots.itertuples():
        if knot.symmetry_type not in ["reversible", "chiral"]:
            continue

        poly = eval(knot.jones_polynomial_vector)
        if sum(poly[:2]) != 0:
            continue

        poly = poly[2:]
        if poly != poly[::-1]:
            continue

        if knot.signature == 0:
            signature_zero.append(knot.name)
        else:
            signature_nonzero.append(knot.name)

    print ("Symmetric Jones polynomial, chiral")
    print (f"{len(signature_zero)} knots with signature zero: {', '.join(signature_zero)}")
    print (f"{len(signature_nonzero)} knots with signature zero: {', '.join(signature_nonzero)}")
    return



with open("knotinfo_parsed.json") as f:
    all_knots = pd.DataFrame(json.load(f)) 

    # query = '2 + crossing_number == 2 * braid_index'
    # filtered_knots = [x for x in all_knots.query(query)["name"]]

    # jones_collisions(all_knots)
    # trivial_alexander(all_knots)
    # unknotting_sigma(all_knots)
    # invisible_knots(all_knots)
    # bankwitz_application(all_knots)
    # alexander_genus(all_knots)
    # genus_prime(all_knots)
    # symmetric_not_acheiral(all_knots)

    # print("Koniec psot.")