diagram_commands["AlphaSmoothing"] = {
    "lines": [
        "\\draw[ultra thick] (-5, -5) to [out=45, in=-45] (-5, 5);",
        "\\draw[ultra thick] (5, -5) to [out=135, in=-135] (5, 5);",
    ],
    "sizes": ["Small", "MedLar", "Medium", "Large"],
}
diagram_commands["ThinAlphaSmoothing"] = {
    "lines": [
        "\\draw[ thick] (-5, -5) to [out=45, in=-45] (-5, 5);",
        "\\draw[ thick] (5, -5) to [out=135, in=-135] (5, 5);",
    ],
    "sizes": ["Small", "MedLar", "Medium", "Large"],
}
diagram_commands["BetaSmoothing"] = {
    "lines": [
        "\\draw[ultra thick] (-5, -5) [in=135, out=45] to (5, -5);",
        "\\draw[ultra thick] (-5, 5) [in=-135, out=-45] to (5, 5);",
    ],
    "sizes": ["Small", "MedLar", "Medium", "Large"],
}
diagram_commands["ThinBetaSmoothing"] = {
    "lines": [
        "\\draw[thick] (-5, -5) [in=135, out=45] to (5, -5);",
        "\\draw[thick] (-5, 5) [in=-135, out=-45] to (5, 5);",
    ],
    "sizes": ["Small", "MedLar", "Medium", "Large"],
}
diagram_commands["JustSmoothing"] = {
    "lines": [
        "\\draw[thick,-latex] (-5, -5) to [out=45, in=-45] (-5, 5);",
        "\\draw[thick,-latex] (5, -5) to [out=135, in=-135] (5, 5);",
    ],
    "sizes": ["Medium", "Large"],
}
diagram_commands["ThikkJustSmoothing"] = {
    "lines": [
        "\\draw[ultra thick,-latex] (-5, -5) to [out=45, in=-45] (-5, 5);",
        "\\draw[ultra thick,-latex] (5, -5) to [out=135, in=-135] (5, 5);",
    ],
    "sizes": ["Medium", "Large"],
}
