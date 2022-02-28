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


with open("knotinfo_parsed.json") as f:
    query = '2 + crossing_number == 2 * braid_index'
    all_knots = pd.DataFrame(json.load(f)) 
    filtered_knots = [x for x in all_knots.query(query)["name"]]
    
    print(f"{len(filtered_knots)} results!")
    for x in filtered_knots:
        continue
        print(x)

    # jones_collisions(all_knots)