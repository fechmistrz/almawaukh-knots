diagram_commands["VirtualFlypeFiveA"] = {
    "lines": [
        "\\strand[thick] (-10, 5) [in=left, out=right] to (0, -5);",
        "\\strand[thick] (-10, -5) [in=left, out=right] to (0, 5);",
        #
        "\\draw[thick] (0, -5) [in=left, out=right] to  (9, 5);",
        "\\draw[thick,-latex] (9, 5) [in=left, out=right] to  (10, 5);",
        "\\draw[thick] (0, 5) [in=left, out=right] to  (9, -5);",
        "\\draw[thick,-latex] (9, -5) [in=left, out=right] to  (10, -5);",
        "\\draw[thick,fill=black] (4.5, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "clip": 7,
    "bounding": [-12, -5, 12, 5],
}
diagram_commands["VirtualFlypeFiveB"] = {
    "lines": [
        "\\strand[thick] (0, -5) [in=left, out=right] to (9, 5);",
        "\\draw[thick,-latex] (9, 5) [in=left, out=right] to  (10, 5);",
        "\\strand[thick] (0, 5) [in=left, out=right] to (9, -5);",
        "\\draw[thick,-latex] (9, -5) [in=left, out=right] to  (10, -5);",
        #
        "\\draw[thick] (-10, -5) [in=left, out=right] to (0, 5);",
        "\\draw[thick] (-10, 5) [in=left, out=right] to (0, -5);",
        "\\draw[thick,fill=black] (-5, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
    "clip": 7,
    "bounding": [-12, -5, 12, 5],
}
