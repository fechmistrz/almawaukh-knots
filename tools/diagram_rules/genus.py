diagram_commands["GenusProofA"] = {
    "lines": [
        "\\draw[semithick,-Latex] (-7, -5) to (-5, -5) [in=right, out=right] to (-5, 5) to (-7, 5);",
        "\\draw[semithick,Latex-] ( 7, -5) to ( 5, -5) [in=left, out=left] to ( 5, 5) to ( 7, 5);",
        "\\node at (-5, 0) {$J$};",
        "\\node at (5, 0) {$K$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["GenusProofB"] = {
    "lines": [
        "\\draw[semithick,-Latex] (-7, -5) to (-5, -5) to [out=right, in=left] (-2, -2) -- (2, -2) to [out=right, in=left] (5, -5) to (7, -5);",
        "\\draw[semithick,Latex-] (-7, 5) to (-5,  5) to [out=right, in=left] (-2,  2) -- (2,  2) to [out=right, in=left] (5,  5) to (7, 5);",
        "\\node at (0, -5) {$J \\# K$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["GenusProofC"] = {
    "lines": [
        "\\draw[semithick,fill=diagramfiller] (-7, -5) to (-5, -5) [in=right, out=right] to (-5, 5) to (-7, 5);",
        "\\draw[semithick,fill=diagramfiller] ( 7, -5) to ( 5, -5) [in=left, out=left] to ( 5, 5) to (7, 5);",
        "\\node at (-4.75, 0) {$M_J$};",
        "\\node at (4.75, 0) {$M_K$};",
    ],
    "sizes": ["Large"],
}
diagram_commands["GenusProofD"] = {
    "lines": [
        "\\fill[diagramfiller] (-5, -5) rectangle(5, 5);",
        "\\draw[semithick,fill=white] (-5, -5) to [out=right, in=left] (-2, -2) -- (2, -2) to [out=right, in=left] (5, -5);",
        "\\draw[semithick,fill=white] (-5,  5) to [out=right, in=left] (-2,  2) -- (2,  2) to [out=right, in=left] (5,  5);",
        "\\node at (0, 0) {$M_{J \\# K}$};",
    ],
    "sizes": ["Large"],
}
