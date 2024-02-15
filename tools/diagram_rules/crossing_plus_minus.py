diagram_commands["PlusCrossing"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to (5, 5);",
        "\\strand[thick] (5, -5) to (-5, 5);",
    ],
    "sizes": ["Small", "Medium"],
}
diagram_commands["PlusCrossingColouring"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to (5, 5);",
        "\\strand[thick] (5, -5) to (-5, 5);",
        "\\node[first_colour] at (5, 5)[below right] {$c$};",
        "\\node[first_colour] at (5, -5)[above right] {$b$};",
        "\\node[first_colour] at (-5, 5)[below left] {$a$};",
    ],
    "sizes": ["Huge"],
}
diagram_commands["PlusCrossingLabel"] = {
    "lines": [
        "\\strand[thick,-latex] (-5, -5) to (5, 5);",
        "\\strand[thick,] (5, -5) to (-5, 5);",
        "\\node[first_colour] at (5, 5)[below right] {$g$};",
        "\\node[first_colour] at (5, -5)[above right] {$h$};",
        "\\node[first_colour] at (-5, 5)[below left] {$k$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["PlusCrossingMatrix"] = {
    "lines": [
        "\\strand[thick,] (-5, -5) to (5, 5);",
        "\\strand[thick,] (5, -5) to (-5, 5);",
        "\\node[first_colour] at (5, 5)[below right] {$x_i$};",
        "\\node[first_colour] at (5, -5)[above right] {$x_j$};",
        "\\node[first_colour] at (-5, 5)[below left] {$x_k$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["PlusCrossingArrows"] = {
    "lines": [
        "\\strand[thick,-latex] (-5, -5) to (5, 5);",
        "\\strand[thick,-latex] (5, -5) to (-5, 5);",
    ],
    "sizes": ["Medium", "Large"],
}
diagram_commands["MinusCrossing"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to (5, 5);",
        "\\strand[thick] (-5, 5) to (5, -5);",
    ],
    "sizes": ["Small", "Medium"],
    "flip": ["1"],
}
diagram_commands["MinusCrossingArrows"] = {
    "lines": [
        "\\strand[thick,-latex] (-5, -5) to (5, 5);",
        "\\strand[thick,-latex] (5, -5) to (-5, 5);",
    ],
    "sizes": ["Medium", "Large"],
    "flip": ["1"],
}
diagram_commands["MinusCrossingChessboard"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to (5, 5);",
        "\\strand[thick] (-5, 5) to (5, -5);"
        "\\fill[diagramfiller] (-4, 5) to (0, 1) to (4, 5);",
        "\\fill[diagramfiller] (-4, -5) to (0, -1) to (4, -5);",
        "\\node[first_colour] at (-5, 0) {$-1$};",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
}

diagram_commands["PlusCrossingChessboard"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to (5, 5);",
        "\\strand[thick] (-5, 5) to (5, -5);"
        "\\fill[diagramfiller] (-4, 5) to (0, 1) to (4, 5);",
        "\\fill[diagramfiller] (-4, -5) to (0, -1) to (4, -5);",
        "\\node[first_colour] at (-5, 0) {$+1$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["MinusCrossingQuandle"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to (5, 5);",
        "\\strand[thick,latex-] (5, -5) to (-5, 5);"
        "\\node[first_colour] at (5, 5)[below right] {$x \\triangleright y$};",
        "\\node[first_colour] at (-5, -5)[above left] {$x$};",
        "\\node[first_colour] at (5, -5)[above right] {$y$};",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
}

diagram_commands["CrossingChessboardA"] = {
    "lines": [
        "\\strand[thick] (-5,5) to (5,-5);",
        "\\strand[thick] (-5,-5) to (5,5);",
        "\\fill[diagramfiller] (-4, 5) to (0, 1) to (4, 5);",
        "\\fill[diagramfiller] (-4, -5) to (0, -1) to (4, -5);",
        "\\node[first_colour] at (-5, -5)[left] {$a$};",
        "\\node[first_colour] at (-5, +5)[left] {$b$};",
        "\\node[first_colour] at (+5, -5)[right] {$c$};",
        "\\node[first_colour] at (+5, +5)[right] {$a$};",
    ],
    "sizes": ["Huge"],
    "flip": ["1"],
}
diagram_commands["CrossingChessboardB"] = {
    "lines": [
        "\\strand[thick] (-5,5) to (5,-5);",
        "\\strand[thick] (-5,-5) to (5,5);",
        "\\fill[diagramfiller] (5, -4) to (1, 0) to (5, 4);",
        "\\fill[diagramfiller] (-5, -4) to (-1, 0) to (-5, 4);",
        "\\node[first_colour] at (-5, -5)[left] {$a$};",
        "\\node[first_colour] at (-5, +5)[left] {$b$};",
        "\\node[first_colour] at (+5, -5)[right] {$c$};",
        "\\node[first_colour] at (+5, +5)[right] {$a$};",
    ],
    "sizes": ["Huge"],
    "flip": ["1"],
}

diagram_commands["SingularCrossingArrows"] = {
    "lines": [
        "\\draw[thick,-latex] (-5, -5) to (5, 5);",
        "\\draw[thick,-latex] (5, -5) to (-5, 5);",
        "\\draw[thick,fill=black] (-0, 0) circle (0.5);",
    ],
    "sizes": ["Medium"],
}
