#!/usr/bin/env python3

import json
import pandas as pd

with open("knotinfo_parsed.json") as f:
    query = '2 + crossing_number == 2 * braid_index'
    all_knots = pd.DataFrame(json.load(f)) 
    filtered_knots = [x for x in all_knots.query(query)["name"]]
    
    print(f"{len(filtered_knots)} results!")
    for x in filtered_knots:
        print(x)