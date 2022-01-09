diagram_commands["TemperleyA"] = {
    "lines": [
        "\\draw[thick] (-5, -5) to (5, -5);",
        "\\draw[thick] (-5, -0) to (5, +0);",
        "\\draw[thick] (-5, +5) to (5, +5);",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}

diagram_commands["TemperleyB"] = {
    "lines": [
        "\\draw[thick] (-5, -5) [in=down, out=right] to (-1, -2.5) [in=right, out=up] to (-5, -0);",
        "\\draw[thick] (5, -5) [in=down, out=left] to (1, -2.5) [in=left, out=up] to (5, -0);",
        "\\draw[thick] (-5, +5) to (5, +5);",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}

diagram_commands["TemperleyC"] = {
    "lines": [
        "\\draw[thick] (-5, -5) to (5, -5);",
        "\\draw[thick] (-5, 0) [in=down, out=right] to (-1, 2.5) [in=right, out=up] to (-5, 5);",
        "\\draw[thick] (5, 0) [in=down, out=left] to (1, 2.5) [in=left, out=up] to (5, 5);",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}

diagram_commands["TemperleyD"] = {
    "lines": [
        "\\draw[thick] (-5, -5) [in=left, out=right] to (5, 5);",
        "\\draw[thick] (-5, 0) [in=down, out=right] to (-1, 2.5) [in=right, out=up] to (-5, 5);",
        "\\draw[thick] (5, -5) [in=down, out=left] to (1, -2.5) [in=left, out=up] to (5, 0);",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}

diagram_commands["TemperleyE"] = {
    "lines": [
        "\\draw[thick] (-5, 5) [in=left, out=right] to (5, -5);",
        "\\draw[thick] (-5, 0) [in=up, out=right] to (-1, -2.5) [in=right, out=down] to (-5, -5);",
        "\\draw[thick] (5, 5) [in=up, out=left] to (1, 2.5) [in=left, out=down] to (5, 0);",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}
