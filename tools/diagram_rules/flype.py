diagram_commands["VirtualFlypeFiveA"] = {
    "lines": [
        "\\strand[ultra thick] (-10, 5) [in=left, out=right] to (0, -5);",
        "\\strand[ultra thick] (-10, -5) [in=left, out=right] to (0, 5);",
        #
        "\\draw[ultra thick] (0, -5) [in=left, out=right] to  (9, 5);",
        "\\draw[ultra thick,-latex] (9, 5) [in=left, out=right] to  (10, 5);",
        "\\draw[ultra thick] (0, 5) [in=left, out=right] to  (9, -5);",
        "\\draw[ultra thick,-latex] (9, -5) [in=left, out=right] to  (10, -5);",
        "\\draw[ultra thick,fill=black] (4.5, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "clip": 5,
    "bounding": [-12, -5, 12, 5],
    "pink": True
}
diagram_commands["VirtualFlypeFiveB"] = {
    "lines": [
        "\\strand[ultra thick] (0, -5) [in=left, out=right] to (9, 5);",
        "\\draw[ultra thick,-latex] (9, 5) [in=left, out=right] to  (10, 5);",
        "\\strand[ultra thick] (0, 5) [in=left, out=right] to (9, -5);",
        "\\draw[ultra thick,-latex] (9, -5) [in=left, out=right] to  (10, -5);",
        #
        "\\draw[ultra thick] (-10, -5) [in=left, out=right] to (0, 5);",
        "\\draw[ultra thick] (-10, 5) [in=left, out=right] to (0, -5);",
        "\\draw[ultra thick,fill=black] (-5, 0) circle (0.5);",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
    "clip": 5,
    "bounding": [-12, -5, 12, 5],
    "pink": True
}
