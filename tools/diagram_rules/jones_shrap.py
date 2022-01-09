diagram_commands["JonesShrapA"] = {
    "lines": [
        "\\strand[thick] (-22, -10) rectangle (-12, 10);",
        "\\strand[thick] (22, -10) rectangle (12, 10);",
        "\\strand[thick,-latex] (12, -6) [in=right, out=left] to (6, -6) to (-6, 6) to (-12, 6);",
        "\\strand[thick,-latex] (-12, -6) [in=left, out=right] to (-6, -6) to (6, 6) to (12, 6);",
        "\\node at (-17, 0) {$K_1$};",
        "\\node at (17, 0) {$K_2$};",
    ],
    "sizes": ["Medium"],
    "bounding": [-23, -10, 23, 10],
    "flip": ["1"],
}
diagram_commands["JonesShrapB"] = {
    "lines": [
        "\\strand[thick] (-22, -10) rectangle (-12, 10);",
        "\\strand[thick] (22, -10) rectangle (12, 10);",
        "\\strand[thick,-latex] (12, -6) [in=right, out=left] to (6, -6) to (-6, 6) to (-12, 6);",
        "\\strand[thick,-latex] (-12, -6) [in=left, out=right] to (-6, -6) to (6, 6) to (12, 6);",
        "\\node at (-17, 0) {$K_1$};",
        "\\node at (17, 0) {$K_2$};",
    ],
    "sizes": ["Medium"],
    "bounding": [-23, -10, 23, 10],
}
diagram_commands["JonesShrapAB"] = {
    "lines": [
        "\\strand[thick] (-22, -10) rectangle (-12, 10);",
        "\\strand[thick] (-12, -6) [in=down, out=right] to (-2, 0);",
        "\\strand[thick,Latex-] (-12, 6) [in=up, out=right] to (-2, 0);",
        "\\strand[thick] (22, -10) rectangle (12, 10);",
        "\\strand[thick] (12, -6) [in=down, out=left] to (2, 0);",
        "\\strand[thick,Latex-] (12, 6) [in=up, out=left] to (2, 0);",
        "\\node at (-17, 0) {$K_1$};",
        "\\node at (17, 0) {$K_2$};",
    ],
    "sizes": ["Medium"],
    "bounding": [-23, -10, 23, 10],
}
