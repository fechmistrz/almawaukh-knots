diagram_commands["Isthmus"] = {
    "lines": [
        "\\strand[semithick] (-5,-5) rectangle (5,5);",
        "\\strand[semithick] (-5, -3) [in=right, out=left] to (-15, 3);",
        "\\strand[semithick] (-5, 3) [in=right, out=left] to (-15, -3);",
        "\\node at (-20, -3) {$\\ldots$};",
        "\\node at (-20,  3) {$\\ldots$};",
    ],
    "sizes": ["Large"],
    "bounding": [-25, -5, 5, 5],
}
