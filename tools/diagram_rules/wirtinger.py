diagram_commands["OldWirtingerPlus"] = {
    "lines": [
        # crossing
        "\\strand[very thick, latex-] (-6,6) to (5,-5);",
        "\\strand[very thick, -latex] (-5,-5) to (6,6);",
        # top left
        # "\\strand[very thick, latex-, first_colour] (-5, 1) to (-1, 5);",
        # bottom left
        # "\\strand[very thick, latex-, first_colour] (-5, -1) to (-1, -5);",
        # bottom right
        # "\\strand[very thick, -latex, first_colour] (5, -1) to (1, -5);",
        # top right
        # "\\strand[very thick, -latex, first_colour] (5, 1) to (1, 5);",
        # nodes
        "\\node[first_colour] at (-6, -6) {$x_k$};",
        "\\node[first_colour] at (-6, 4) {$x_{j+1}$};",
        "\\node[first_colour] at (6, -4) {$x_j$};",
        "\\node[first_colour] at (6, 4) {$x_k$};",
    ],
    "sizes": ["Huge"],
    "flip": ["1"],
    "clip": 4.5
}

diagram_commands["WirtingerPlus"] = {
    "lines": [
        "\\strand[ultra thick, -latex] (-5, -5) to (6, 6);",
        "\\strand[ultra thick, latex-] (-6, 6) to (5, -5);",
        "\\node[first_colour, rotate around={45:(0,0)}] at (-3.25, -2.75) [above left] {$x_k$};",
        "\\node[first_colour, rotate around={315:(0,0)}] at (-2.75, 3.25) [above] {$x_{j+1}$};",
        "\\node[first_colour, rotate around={315:(0,0)}] at (3.25, -2.75) [above right] {$x_j$};",
        "\\node[first_colour, rotate around={45:(0,0)}] at (3.25, 2.75) [below right] {$x_k$};",
    ],
    "sizes": ["Small", "Medium", "Large", "Huge"],
    "clip": 5
}

diagram_commands["WirtingerMinus"] = {
    "lines": [
        "\\strand[ultra thick, -latex] (-5, -5) to (6, 6);",
        "\\strand[ultra thick, latex-] (-6, 6) to (5, -5);",
        "\\node[first_colour, rotate around={45:(0,0)}] at (-3.25, -2.75) [above left] {$x_j$};",
        "\\node[first_colour, rotate around={315:(0,0)}] at (-3.25, 2.75) [below] {$x_{k}$};",
        "\\node[first_colour, rotate around={315:(0,0)}] at (3.25, -2.75) [above right] {$x_k$};",
        "\\node[first_colour, rotate around={45:(0,0)}] at (2.75, 3.25) [above] {$x_{j+1}$};",
    ],
    "sizes": ["Small", "Medium", "Large", "Huge"],
    "clip": 5,
    "flip": ["1"]
}


diagram_commands["OldWirtingerMinus"] = {
    "lines": [
        # crossing
        "\\strand[very thick, latex-] (-6,6) to (5,-5);",
        "\\strand[very thick, latex-] (-6,-6) to (5,5);",
        # top left
        "\\strand[very thick, latex-, first_colour] (-5, 1) to (-1, 5);",
        # bottom left
        "\\strand[very thick, -latex, first_colour] (-5, -1) to (-1, -5);",
        # bottom right
        "\\strand[very thick, -latex, first_colour] (5, -1) to (1, -5);",
        # top right
        "\\strand[very thick, latex-, first_colour] (5, 1) to (1, 5);",
        # nodes
        "\\node[first_colour] at (-7, -2) {$x_k$};",
        "\\node[first_colour] at (-7, 2) {$x_{j+1}$};",
        "\\node[first_colour] at (7, -2) {$x_j$};",
        "\\node[first_colour] at (7, 2) {$x_k$};",
    ],
    "sizes": ["Huge"],
    "flip": ["1"],
    "clip": 4.5
}
diagram_commands["WirtingerRelationA"] = {
    "lines": [
        "\\strand[very thick,-latex] (-5, -5) to (5, 5);",
        "\\strand[very thick,-latex] (5, -5) to (-5, 5);",
        "\\node[first_colour] at (5, -5)  [above right] {$a_k$};",
        "\\node[first_colour] at (-5, 5)  [below left]  {$a_j$};",
        "\\node[first_colour] at (-5, -5) [above left]  {$a_i$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["WirtingerRelationB"] = {
    "lines": [
        "\\strand[very thick,-latex] (-5, -5) to (5, 5);",
        "\\strand[very thick,-latex] (5, -5) to (-5, 5);",
        "\\node[first_colour] at (5, 5)   [below right] {$a_k$};",
        "\\node[first_colour] at (5, -5)  [above right] {$a_i$};",
        "\\node[first_colour] at (-5, -5) [above left]  {$a_j$};",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
}
