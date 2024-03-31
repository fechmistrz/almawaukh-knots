diagram_commands["ReidemeisterThreeB"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5) -- (5, 5);",
        "\\strand[ultra thick] (-5, 5) -- (5, -5);",
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, -5);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, -5);",
    ],
    "sizes": ["Large", "MedLar"],
    "flip": ["1", "2", "3"],
    "bounding": [-6, -5, 6, 5],
}
diagram_commands["ReidemeisterThreeLinkingA"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5) -- (5, 5);",
        "\\strand[ultra thick] (-5, 5) -- (5, -5);",
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, 5);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, 5);",
        "\\node[first_colour] at (-4,2.5)[left] {$a$};",
        "\\node[first_colour] at (4,2.5)[right] {$b$};",
        "\\node[first_colour] at (0,-2)[below] {$c$};",
    ],
    "sizes": ["MedLar"],
    "flip": ["1", "2", "3"],
}
diagram_commands["ReidemeisterThreeLinkingB"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5) -- (5, 5);",
        "\\strand[ultra thick] (-5, 5) -- (5, -5);",
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, -5);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, -5);",
        "\\node[first_colour] at (-4,-2.5)[left] {$a$};",
        "\\node[first_colour] at (4,-2.5)[right] {$b$};",
        "\\node[first_colour] at (0,2)[above] {$c$};",
    ],
    "sizes": ["MedLar"],
    "flip": ["1", "2", "3"],
}
diagram_commands["ReidemeisterThreeColouringA"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5) -- (5, 5);",
        "\\strand[ultra thick] (-5, 5) -- (5, -5);",
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, 5);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, 5);",
        "\\node[first_colour] at (-5, 4) [left] {$b$};",
        "\\node[first_colour] at (5, 4) [right] {$c$};",
        "\\node[first_colour] at (-5, 0) [left] {$a$};",
        "\\node[first_colour] at (-5, -5) [below] {$2a-2b+c$};",
        "\\node[first_colour] at (5, -5) [below] {$2a-b$};",
    ],
    "sizes": ["Large"],
    "flip": ["1", "2", "3"],
    "bounding": [-10, -8, 10, 8],
    "clip": 5,
}
diagram_commands["ReidemeisterThreeQuandleA"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5)  -- (4, 4);",
        "\\strand[ultra thick,-latex] (4, 4) to (5, 5);"
        # split to improve clip area
        "\\strand[ultra thick] (-5, 5) -- (4, -4);",
        "\\strand[ultra thick,-latex] (-4, 4) to (5, -5);",
        # split to improve area
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, 4);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, 4);",
        "\\strand[ultra thick,-latex] (5, 0) to (6, 0);"
        "\\node[first_colour] at (-5, 4) [ left] {$z$};",
        "\\node[first_colour] at (-5, 0) [left] {$y$};",
        "\\node[first_colour] at (-5, -4) [ left] {$x$};",
        "\\node[first_colour] at (0, 4) [above] {$y \\triangleright z$};",
        "\\node[first_colour] at (5, 4) [right] {$(x \\triangleright z) \\triangleright (y \\triangleright z)$};",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
    "bounding": [-7, -5, 20, 7],
    "clip": 7,
}
diagram_commands["ReidemeisterThreeQuandleB"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5)  -- (4, 4);",
        "\\strand[ultra thick,-latex] (4, 4) to (5, 5);"
        # split to improve clip area
        "\\strand[ultra thick] (-5, 5) -- (4, -4);",
        "\\strand[ultra thick,-latex] (-4, 4) to (5, -5);",
        # split to improve area
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, -4);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, -4);",
        "\\strand[ultra thick,-latex] (5, 0) to (6, 0);"
        "\\node[first_colour] at (-5, 4) [ left] {$z$};",
        "\\node[first_colour] at (-5, 0) [left] {$y$};",
        "\\node[first_colour] at (-5, -4) [ left] {$x$};",
        "\\node[first_colour] at (5, 4) [right] {$(x \\triangleright y) \\triangleright z$};",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
    "bounding": [-7, -5, 15, 7],
    "clip": 7,
}
diagram_commands["ReidemeisterThreeColouringB"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5) -- (5, 5);",
        "\\strand[ultra thick] (-5, 5) -- (5, -5);",
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, -5);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, -5);",
        "\\node[first_colour] at (-5, 4) [left] {$b$};",
        "\\node[first_colour] at (5, 4) [right] {$c$};",
        "\\node[first_colour] at (5, 0) [right] {$a$};",
        "\\node[first_colour] at (-5, -5) [below] {$2a-2b+c$};",
        "\\node[first_colour] at (5, -5) [below] {$2a-b$};",
    ],
    "sizes": ["Large"],
    "flip": ["1", "2", "3"],
    "bounding": [-10, -8, 10, 6],
    "clip": 5,
}

diagram_commands["ReidemeisterThreeA"] = {
    "lines": [
        "\\strand[ultra thick] (-5, -5) -- (5, 5);",
        "\\strand[ultra thick] (-5, 5) -- (5, -5);",
        "\\strand[ultra thick] (-5, 0) to [in=left, out=right] (0, 5);",
        "\\strand[ultra thick] (5, 0) to [in=right, out=left] (0, 5);",
    ],
    "sizes": ["Large", "MedLar"],
    "flip": ["1", "2", "3"],
    "bounding": [-6, -5, 6, 5],
}
diagram_commands["VirtualReidemeisterThreeA"] = {
    "lines": [
        # down arrow
        "\\strand[ultra thick,latex-] (-5, -5) to (-4, -4);",
        "\\strand[ultra thick] (-4, -4) to (-0.25, -0.25);",
        "\\strand[ultra thick] (0.25, 0.25) to (5, 5);",
        # up arrow
        "\\strand[ultra thick,-latex] (-4, 4) to (-5, 5);",
        "\\strand[ultra thick] (5, -5) to (0.25, -0.25);",
        "\\strand[ultra thick] (-0.25, 0.25) to (-4, 4);",
        # background arrow
        "\\strand[ultra thick,-latex] (5, 0) to (4, 0);",
        "\\strand[ultra thick] (-5, 0) [in=left, out=right] to (-4, 0) to (0, 5) to (4, 0);",
        # singular crossing
        "\\draw[ultra thick,fill=black] (0, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "clip": 7,
    "flip": ["1", "2"],
}
diagram_commands["VirtualReidemeisterThreeB"] = {
    "lines": [
        # down arrow
        "\\strand[ultra thick,latex-] (-5, -5) to (-4, -4);",
        "\\strand[ultra thick] (-4, -4) to (-0.25, -0.25);",
        "\\strand[ultra thick] (0.25, 0.25) to (5, 5);",
        # up arrow
        "\\strand[ultra thick,-latex] (-4, 4) to (-5, 5);",
        "\\strand[ultra thick] (5, -5) to (0.25, -0.25);",
        "\\strand[ultra thick] (-0.25, 0.25) to (-4, 4);",
        # background arrow
        "\\strand[ultra thick,-latex] (5, 0) to (4, 0);",
        "\\strand[ultra thick] (-5, 0) [in=left, out=right] to (-4, 0) to (0, -5) to (4, 0);",
        # singular crossing
        "\\draw[ultra thick,fill=black] (0, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "clip": 7,
    "flip": ["1", "2"],
}
diagram_commands["VirtualReidemeisterThreeC"] = {
    "lines": [
        # down arrow
        "\\strand[ultra thick,latex-] (-5, -5) to (-4, -4);",
        "\\strand[ultra thick] (-4, -4) to (-0.25, -0.25);",
        "\\strand[ultra thick] (0.25, 0.25) to (5, 5);",
        # up arrow
        "\\strand[ultra thick,-latex] (-4, 4) to (-5, 5);",
        "\\strand[ultra thick] (5, -5) to (0.25, -0.25);",
        "\\strand[ultra thick] (-0.25, 0.25) to (-4, 4);",
        # background arrow
        "\\strand[ultra thick,-latex] (5, 0) to (4, 0);"
        "\\strand[ultra thick] (-5, 0) [in=left, out=right] to (-4, 0) to (0, 5) to (4, 0);",
        # singular crossing
        "\\draw[ultra thick,fill=black] (0, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "clip": 7,
}
diagram_commands["VirtualReidemeisterThreeD"] = {
    "lines": [
        # down arrow
        "\\strand[ultra thick,latex-] (-5, -5) to (-4, -4);",
        "\\strand[ultra thick] (-4, -4) to (-0.25, -0.25);",
        "\\strand[ultra thick] (0.25, 0.25) to (5, 5);",
        # up arrow
        "\\strand[ultra thick,-latex] (-4, 4) to (-5, 5);",
        "\\strand[ultra thick] (5, -5) to (0.25, -0.25);",
        "\\strand[ultra thick] (-0.25, 0.25) to (-4, 4);",
        # background arrow
        "\\strand[ultra thick,-latex] (5, 0) to (4, 0);"
        "\\strand[ultra thick] (-5, 0) [in=left, out=right] to (-4, 0) to (0, -5) to (4, 0);",
        # singular crossing
        "\\draw[ultra thick,fill=black] (0, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "clip": 7,
}
