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


with open("knotinfo_parsed.json") as f:
    all_knots = pd.DataFrame(json.load(f)) 

    # query = '2 + crossing_number == 2 * braid_index'
    # filtered_knots = [x for x in all_knots.query(query)["name"]]

    # jones_collisions(all_knots)
    # trivial_alexander(all_knots)
    # unknotting_sigma(all_knots)
    # invisible_knots(all_knots)

    # print("Koniec psot.")