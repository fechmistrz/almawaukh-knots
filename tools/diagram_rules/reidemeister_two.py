diagram_commands["ReidemeisterTwoA"] = {
    "lines": [
        "\\strand[thick] (-2.5, 5) to [in=up, out=down] (2.5, 0);",
        "\\strand[thick] (-2.5, -5) to [in=down, out=up] (2.5, 0);",
        "\\strand[thick] (2.5, 5) to [in=up, out=down] (-2.5, 0);",
        "\\strand[thick] (2.5, -5) to [in=down, out=up] (-2.5, 0);",
    ],
    "sizes": ["Large"],
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
        "\\strand[thick] (-2.5, 5) to [in=up, out=down] (2.5, 0);",
        "\\strand[thick] (-2.5, -5) to [in=down, out=up] (2.5, 0);",
        "\\strand[thick] (2.5, 5) to [in=up, out=down] (-2.5, 0);",
        "\\strand[thick] (2.5, -5) to [in=down, out=up] (-2.5, 0);",
        "\\node[first_colour] at (-4, -2.5)[left] {$d \\equiv b$};",
        "\\node[first_colour] at (4, 2.5)[right] {$a$};",
        "\\node[first_colour] at (4, 0) [right] {$c \\equiv 2a-b$};",
        "\\node[first_colour] at (-4, 2.5) [left] {$b$};",
    ],
    "sizes": ["Large"],
    "bounding": [-3.5, -5, 3.5, 5],
}
diagram_commands["ReidemeisterTwoLinkingA"] = {
    "lines": [
        "\\strand[thick] (-2.5, 5) to [in=up, out=down] (2.5, 0);",
        "\\strand[thick] (-2.5, -5) to [in=down, out=up] (2.5, 0);",
        "\\strand[thick] (2.5, 5) to [in=up, out=down] (-2.5, 0);",
        "\\strand[thick] (2.5, -5) to [in=down, out=up] (-2.5, 0);",
        "\\node[blue] at (-4,2.5)[left] {$a$};",
        "\\node[blue] at (-4,-2.5)[left] {$-a$};",
    ],
    "sizes": ["MedLar"],
}
diagram_commands["ReidemeisterTwoB"] = {
    "lines": [
        "\\strand[thick] (-2.5, 5) to [in=up, out=down] (-1, 0);",
        "\\strand[thick] (-2.5, -5) to [in=down, out=up] (-1, 0);",
        "\\strand[thick] (2.5, 5) to [in=up, out=down] (1, 0);",
        "\\strand[thick] (2.5, -5) to [in=down, out=up] (1, 0);",
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
