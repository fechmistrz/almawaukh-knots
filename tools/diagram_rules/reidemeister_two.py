diagram_commands["ReidemeisterTwoA"] = {
    "lines": [
        "\\strand[ultra thick] (-2.5, 5) to [in=up, out=down] (2.5, 0);",
        "\\strand[ultra thick] (-2.5, -5) to [in=down, out=up] (2.5, 0);",
        "\\strand[ultra thick] (2.5, 5) to [in=up, out=down] (-2.5, 0);",
        "\\strand[ultra thick] (2.5, -5) to [in=down, out=up] (-2.5, 0);",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-3.5, -5, 3.5, 5],
}
diagram_commands["ReidemeisterTwoQuandleA"] = {
    "lines": [
        "\\strand[thick] (-2.5, 5) to [in=up, out=down] (2.5, 0);",
        "\\strand[thick] (-2.5, -5) to [in=down, out=up] (2.5, 0);",
        "\\strand[thick] (2.5, 5) to [in=up, out=down] (-2.5, 0);",
        "\\strand[thick] (2.5, -5) to [in=down, out=up] (-2.5, 0);",
        "\\node[first_colour] at (-2.5, -5) [left] {$x$};",
        "\\node[first_colour] at (2.5, -5) [right] {$y$};",
        "\\node[first_colour] at (-2.5, 0) [left] {$y \\triangleright x$};",
        "\\node[first_colour] at (2.5, 5) [right] {$x \\triangleleft (y \\triangleright x)$};",
    ],
    "sizes": ["Large"],
    "bounding": [-3.5, -5, 12.5, 5],
}
diagram_commands["ReidemeisterTwoColouringA"] = {
    "lines": [
        "\\strand[ultra thick] (-2.5, 5) to [in=up, out=down] (2.5, 0);",
        "\\strand[ultra thick] (-2.5, -5) to [in=down, out=up] (2.5, 0);",
        "\\strand[ultra thick] (2.5, 5) to [in=up, out=down] (-2.5, 0);",
        "\\strand[ultra thick] (2.5, -5) to [in=down, out=up] (-2.5, 0);",
        "\\node[first_colour] at (-2.5, 0) [left] {$2b-a$};",
        "\\node[first_colour] at (2.5, 4) [right] {$a$};",
        "\\node[first_colour] at (2.5, -4) [right] {$2b-(2b-a)$};",
        "\\node[first_colour] at (-2.5, 4) [left] {$b$};",
    ],
    "sizes": ["Large"],
    "bounding": [-10, -5, 15.5, 5],
}
diagram_commands["ReidemeisterTwoLinkingA"] = {
    "lines": [
        "\\strand[ultra thick] (-2.5, 5) to [in=up, out=down] (2.5, 0);",
        "\\strand[ultra thick] (-2.5, -5) to [in=down, out=up] (2.5, 0);",
        "\\strand[ultra thick] (2.5, 5) to [in=up, out=down] (-2.5, 0);",
        "\\strand[ultra thick] (2.5, -5) to [in=down, out=up] (-2.5, 0);",
        "\\node[first_colour] at (-4,2.5)[left] {$a$};",
        "\\node[first_colour] at (-4,-2.5)[left] {$-a$};",
    ],
    "sizes": ["MedLar"],
}
diagram_commands["ReidemeisterTwoB"] = {
    "lines": [
        "\\strand[ultra thick] (-2.5, 5) to [in=up, out=down] (-1, 0);",
        "\\strand[ultra thick] (-2.5, -5) to [in=down, out=up] (-1, 0);",
        "\\strand[ultra thick] (2.5, 5) to [in=up, out=down] (1, 0);",
        "\\strand[ultra thick] (2.5, -5) to [in=down, out=up] (1, 0);",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-3.5, -5, 3.5, 5],
}
diagram_commands["ReidemeisterTwoColouringB"] = {
    "lines": [
        "\\strand[ultra thick] (-2.5, 5) to [in=up, out=down] (-1, 0);",
        "\\strand[ultra thick] (-2.5, -5) to [in=down, out=up] (-1, 0);",
        "\\strand[ultra thick] (2.5, 5) to [in=up, out=down] (1, 0);",
        "\\strand[ultra thick] (2.5, -5) to [in=down, out=up] (1, 0);",
        "\\node[first_colour] at (2.5, 4) [right] {$a$};",
        "\\node[first_colour] at (-2.5, 4) [left] {$b$};",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-3.5, -5, 3.5, 5],
}
diagram_commands["ReidemeisterTwoQuandleB"] = {
    "lines": [
        "\\strand[thick] (-2.5, 5) to [in=up, out=down] (-1, 0);",
        "\\strand[thick] (-2.5, -5) to [in=down, out=up] (-1, 0);",
        "\\strand[thick] (2.5, 5) to [in=up, out=down] (1, 0);",
        "\\strand[thick] (2.5, -5) to [in=down, out=up] (1, 0);",
        "\\node[first_colour] at (2, 0) [right] {$y$};",
        "\\node[first_colour] at (-2, 0) [left] {$x$};",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}
