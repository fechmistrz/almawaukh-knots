diagram_commands["TemperleyA"] = {
    "lines": [
        "\\draw[ultra thick] (-7, -5) to (7, -5);",
        "\\draw[ultra thick] (-7, -0) to (7, +0);",
        "\\draw[ultra thick] (-7, +5) to (7, +5);",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-7, -5, 7, 5],
}

diagram_commands["TemperleyB"] = {
    "lines": [
        "\\draw[ultra thick] (-7, -5) [in=down, out=right] to (-3.5, -2.5) [in=right, out=up] to (-7, -0);",
        "\\draw[ultra thick] (7, -5) [in=down, out=left] to (3.5, -2.5) [in=left, out=up] to (7, -0);",
        "\\draw[ultra thick] (-7, +5) to (7, +5);",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-7, -5, 7, 5],
}

diagram_commands["TemperleyC"] = {
    "lines": [
        "\\draw[ultra thick] (-7, -5) to (7, -5);",
        "\\draw[ultra thick] (-7, 0) [in=down, out=right] to (-3.5, 2.5) [in=right, out=up] to (-7, 5);",
        "\\draw[ultra thick] (7, 0) [in=down, out=left] to (3.5, 2.5) [in=left, out=up] to (7, 5);",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-7, -5, 7, 5],
}

diagram_commands["TemperleyD"] = {
    "lines": [
        "\\draw[ultra thick] (-7, -5) [in=left, out=right] to (7, 5);",
        "\\draw[ultra thick] (-7, 0) [in=down, out=right] to (-3.5, 2.5) [in=right, out=up] to (-5, 5);",
        "\\draw[ultra thick] (7, -5) [in=down, out=left] to (3.5, -2.5) [in=left, out=up] to (5, 0);",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-7, -5, 7, 5],
}

diagram_commands["TemperleyE"] = {
    "lines": [
        "\\draw[ultra thick] (-7, 5) [in=left, out=right] to (7, -5);",
        "\\draw[ultra thick] (-7, 0) [in=up, out=right] to (-3.5, -2.5) [in=right, out=down] to (-7, -5);",
        "\\draw[ultra thick] (7, 5) [in=up, out=left] to (3.5, 2.5) [in=left, out=down] to (7, 0);",
    ],
    "sizes": ["Large", "MedLar"],
    "bounding": [-7, -5, 7, 5],
}
