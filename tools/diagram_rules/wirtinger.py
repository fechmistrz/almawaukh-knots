diagram_commands["WirtingerPlus"] = {
    "lines": [
        # crossing
        "\\strand[thick, latex-] (-5,5) to (5,-5);",
        "\\strand[thick, -latex] (-5,-5) to (5,5);",
        # top left
        "\\strand[thick, latex-, first_colour] (-5, 1) to (-1, 5);",
        # bottom left
        "\\strand[thick, latex-, first_colour] (-5, -1) to (-1, -5);",
        # bottom right
        "\\strand[thick, -latex, first_colour] (5, -1) to (1, -5);",
        # top right
        "\\strand[thick, -latex, first_colour] (5, 1) to (1, 5);",
        # nodes
        "\\node[first_colour] at (-7, -2) {$x_k$};",
        "\\node[first_colour] at (-7, 2) {$x_{j+1}$};",
        "\\node[first_colour] at (7, -2) {$x_j$};",
        "\\node[first_colour] at (7, 2) {$x_k$};",
    ],
    "sizes": ["Huge"],
    "flip": ["1"],
}
diagram_commands["WirtingerMinus"] = {
    "lines": [
        # crossing
        "\\strand[thick, latex-] (-5,5) to (5,-5);",
        "\\strand[thick, latex-] (-5,-5) to (5,5);",
        # top left
        "\\strand[thick, latex-, first_colour] (-5, 1) to (-1, 5);",
        # bottom left
        "\\strand[thick, -latex, first_colour] (-5, -1) to (-1, -5);",
        # bottom right
        "\\strand[thick, -latex, first_colour] (5, -1) to (1, -5);",
        # top right
        "\\strand[thick, latex-, first_colour] (5, 1) to (1, 5);",
        # nodes
        "\\node[first_colour] at (-7, -2) {$x_k$};",
        "\\node[first_colour] at (-7, 2) {$x_{j+1}$};",
        "\\node[first_colour] at (7, -2) {$x_j$};",
        "\\node[first_colour] at (7, 2) {$x_k$};",
    ],
    "sizes": ["Huge"],
    "flip": ["1"],
}
diagram_commands["WirtingerRelationA"] = {
    "lines": [
        "\\strand[thick,-latex] (-5, -5) to (5, 5);",
        "\\strand[thick,-latex] (5, -5) to (-5, 5);",
        "\\node[first_colour] at (5, -5)  [above right] {$a_k$};",
        "\\node[first_colour] at (-5, 5)  [below left]  {$a_j$};",
        "\\node[first_colour] at (-5, -5) [above left]  {$a_i$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["WirtingerRelationB"] = {
    "lines": [
        "\\strand[thick,-latex] (-5, -5) to (5, 5);",
        "\\strand[thick,-latex] (5, -5) to (-5, 5);",
        "\\node[first_colour] at (5, 5)   [below right] {$a_k$};",
        "\\node[first_colour] at (5, -5)  [above right] {$a_i$};",
        "\\node[first_colour] at (-5, -5) [above left]  {$a_j$};",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
}
