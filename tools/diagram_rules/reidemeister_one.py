diagram_commands["ReidemeisterOneLeft"] = {
    # verified
    "lines": [
        "\\strand[ultra thick] (-5, 5)  [in=left, out=-60] to (3, -5) [in=down, out=right] to (5, 0);",
        "\\strand[ultra thick] (-5, -5) [in=left, out=60]  to (3, 5)  [in=up, out=right]   to (5, 0);",
    ],
    "sizes": ["Medium", "Large", "MedLar"],
    "bounding": [-6, -5, 6, 5],
}
diagram_commands["ReidemeisterOneLeftProof"] = {
    "lines": [
        "\\strand[ultra thick] (-5, 5)  [in=left, out=-60] to (3, -5) [in=down, out=right] to (5, 0);",
        "\\strand[ultra thick] (-5, -5) [in=left, out=60]  to (3, 5)  [in=up, out=right]   to (5, 0);"
        "\\node[first_colour] at (-5, -5)[below] {$b \\equiv a$};",
        "\\node[first_colour] at (-5,  5)[above] {$a$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["ReidemeisterOneLeftRightQuandleProof"] = {
    "lines": [
        "\\strand[thick] (0, 2) [in=up, out=left] to (-10, -3) [in=left, out=down] to (-5, -5);",
        "\\strand[thick] (-10, 5) [in=up, out=right]  to (-4, -3)  [in=right, out=down]   to (-5, -5);"
        "\\strand[thick,latex-] (10, 5) [in=up, out=left]  to (4, -3)  [in=left, out=down]   to (5, -5);"
        "\\strand[thick] (0, 2) [in=up, out=right] to (10, -3) [in=right, out=down] to (5, -5);",
        "\\node[first_colour] at (-10, 5) [left]  {$x$};",
        "\\node[first_colour] at (10, 5)  [right] {$x$};",
        "\\node[first_colour] at (0, 2)   [above] {$x \\triangleright x$};",
    ],
    "bounding": [-12, -5, 12, 5],
    "sizes": ["Large"],
    "flip": ["1"],
}
diagram_commands["ReidemeisterOneRight"] = {
    "lines": [
        "\\strand[thick] (-5, -5) [in=left, out=60] to  (3, 5)  [in=up, out=right]   to (5, 0);",
        "\\strand[thick] (-5, 5)  [in=left, out=-60] to (3, -5) [in=down, out=right] to (5, 0);",
    ],
    "sizes": ["Medium"],
}
diagram_commands["ReidemeisterOneRightQuandleProof"] = {
    "lines": [
        "\\strand[thick] (-5, -5) [in=left, out=60] to  (3, 5)  [in=up, out=right]   to (5, 0);",
        "\\strand[thick,latex-] (-5, 5)  [in=left, out=-60] to (3, -5) [in=down, out=right] to (5, 0);",
        "\\node[first_colour] at (-5, -4)[left] {$x$};",
        "\\node[first_colour] at (-5,  4)[left] {$x \\triangleright x$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["ReidemeisterOneStraight"] = {
    # verified
    "lines": [
        "\\strand[ultra thick] (0, -5) to (0, 5);",
    ],
    "sizes": ["Large", "MedLar", "Medium"],
    "bounding": [-1, -5, 1, 5],
}
diagram_commands["ReidemeisterOneStraightProof"] = {
    "lines": [
        "\\strand[thick] (0, -5) to (0, 5);",
        "\\node[first_colour] at (0,  0)[left] {$a$};",
    ],
    "sizes": ["Large"],
    "bounding": [-2, -5, 2, 5],
}
diagram_commands["ReidemeisterOneStraightQuandleProof"] = {
    "lines": [
        "\\strand[thick] (0, -6.65) to (0, 6);",
        "\\node[first_colour] at (0,  0)[left] {$x$};",
    ],
    "sizes": ["Large"],
    "bounding": [-2, -5, 2, 5],
}
diagram_commands["ReidemeisterOneStraightQuandleProofRotated"] = {
    "lines": [
        "\\strand[thick, -latex] (-5, 0) to (5, 0);",
        "\\node[first_colour] at (0,  0)[above] {$x$};",
    ],
    "sizes": ["Large"],
    "bounding": [-7, -2, 7, 2],
}
diagram_commands["ReidemeisterOneSmoothA"] = {
    "lines": [
        "\\strand[thick] (-5, 5)  [in=left, out=-60] to (-2, 1.5)  [in=left, out=right] to (3, 5)  [in=up]   to (5, 0);",
        "\\strand[thick] (-5, -5) [in=left, out=60] to  (-2, -1.5) [in=left, out=right] to (3, -5) [in=down] to (5, 0);",
    ],
    "sizes": ["Medium"],
}
diagram_commands["ReidemeisterOneSmoothB"] = {
    "lines": [
        "\\strand[thick] (-5, -5) [in=down, out=up] to (-3.5, 0) to (-5, 5);",
        "\\strand[thick] (-1, 0) [in=left, out=up] to (3, 5) [in=up, out=right] to (5, 0);",
        "\\strand[thick] (-1, 0) [in=left, out=down] to (3, -5) [in=down, out=right] to (5, 0);",
    ],
    "sizes": ["Medium"],
}
