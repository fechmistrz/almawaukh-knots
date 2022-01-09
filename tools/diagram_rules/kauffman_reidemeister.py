diagram_commands["KauffmanReidemeisterTwoA"] = {
    "lines": [
        "\\strand[thick] (5, -5) .. controls (5, -2) and (-5, -2) .. (-5, 0);",
        "\\strand[thick] (5, 5) .. controls (5, 2) and (-5, 2) .. (-5, 0);",
        "\\strand[thick] (-5, -5) .. controls (-5, -2) and (5, -2) .. (5, 0);",
        "\\strand[thick] (-5, 5) .. controls (-5, 2) and (5, 2) .. (5, 0);",
    ],
    "sizes": ["Medium"],
}
diagram_commands["KauffmanReidemeisterTwoB"] = {
    "lines": [
        "\\strand[thick] (5, -5) .. controls (5, -3) and (-5, -3) .. (-5, -1);",
        "\\strand[thick] (-5, -5) .. controls (-5, -3) and (5, -3) .. (5, -1);",
        "\\strand[thick] (-5, -1) [in=left, out=up] to (0, 1) to [in=up, out=right] (5, -1);",
        "\\strand[thick] (-5, 5) [in=left, out=down] to (0, 3) to [in=down, out=right] (5, 5);",
    ],
    "sizes": [
        "Medium",
    ],
}
diagram_commands["KauffmanReidemeisterTwoC"] = {
    "lines": [
        "\\strand[thick] (5, -5) .. controls (5, -2) and (-5, -2) .. (-5, 0);",
        "\\strand[thick] (5, 5) to (5, 0);",
        "\\strand[thick] (-5, -5) .. controls (-5, -2) and (5, -2) .. (5, 0);",
        "\\strand[thick] (-5, 5) to (-5, 0);",
    ],
    "sizes": [
        "Medium",
    ],
}
diagram_commands["KauffmanReidemeisterThreeA"] = {
    "lines": [
        "\\strand[thick] (-5, -5) -- (5, 5);",
        "\\strand[thick] (-5, 5) -- (5, -5);",
        "\\strand[thick] (-5, 0) .. controls (-3, 0) and (-3, 5) .. (0, 5) .. controls (3, 5) and (3, 0) .. (5, 0);",
    ],
    "sizes": ["Medium"],
    "flip": ["1", "2", "3"],
    "clip": 5,
}
diagram_commands["KauffmanReidemeisterThreeFlippedA"] = {
    "lines": [
        "\\strand[thick] (-5, -5) -- (5, 5);",
        "\\strand[thick] (-5, 5) -- (5, -5);",
        "\\strand[thick] (-5, 0) .. controls (-3, 0) and (-3, -5) .. (0, -5) .. controls (3, -5) and (3, 0) .. (5, 0);",
    ],
    "sizes": ["Medium"],
    "flip": ["1", "2", "3"],
    "clip": 5,
}
diagram_commands["KauffmanReidemeisterThreeB"] = {
    "lines": [
        "\\strand[thick] (-5, 5) [in=-120, out=-60] to (5, 5);",
        "\\strand[thick] (-5, -5) [in=120, out=60] to (5, -5);",
        "\\strand[thick] (-5, 0) .. controls (-3, 0) and (-3, 5) .. (0, 5) .. controls (3, 5) and (3, 0) .. (5, 0);",
    ],
    "sizes": [
        "Medium",
    ],
    "flip": ["1", "2", "3"],
    "clip": 5,
}
diagram_commands["KauffmanReidemeisterThreeFlippedB"] = {
    "lines": [
        "\\strand[thick] (-5, 5) [in=-120, out=-60] to (5, 5);",
        "\\strand[thick] (-5, -5) [in=120, out=60] to (5, -5);",
        "\\strand[thick] (-5, 0) .. controls (-3, 0) and (-3, -5) .. (0, -5) .. controls (3, -5) and (3, 0) .. (5, 0);",
    ],
    "sizes": [
        "Medium",
    ],
    "flip": ["1", "2", "3"],
    "clip": 5,
}
diagram_commands["KauffmanReidemeisterThreeC"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to [out=30, in=-30] (-5, 5);",
        "\\strand[thick] (5, -5) to [out=150, in=-150] (5, 5);",
        "\\strand[thick] (-6, 0) .. controls (-3, 0) and (-3, 5) .. (0, 5) .. controls (3, 5) and (3, 0) .. (6, 0);  ",
    ],
    "sizes": [
        "Medium",
    ],
    "flip": ["1", "2", "3"],
    "clip": 5,
}
diagram_commands["KauffmanReidemeisterThreeFlippedC"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to [out=30, in=-30] (-5, 5);",
        "\\strand[thick] (5, -5) to [out=150, in=-150] (5, 5);",
        "\\strand[thick] (-6, 0) .. controls (-3, 0) and (-3, -5) .. (0, -5) .. controls (3, -5) and (3, 0) .. (6, 0); ",
    ],
    "sizes": [
        "Medium",
    ],
    "flip": ["1", "2", "3"],
    "clip": 5,
}
diagram_commands["KauffmanReidemeisterThreeD"] = {
    "lines": [
        "\\strand[thick] (-5, 5) [in=-120, out=-60] to (5, 5);",
        "\\strand[thick] (-5, -5) [in=120, out=60] to (5, -5);",
        "\\strand[thick] (-5, 0) to (5, 0);",
    ],
    "sizes": [
        "Medium",
    ],
    "flip": ["1", "2", "3"],
    "clip": 5,
}
diagram_commands["KauffmanReidemeisterThreeE"] = {
    "lines": [
        "\\strand[thick] (-5, -5) to [out=30, in=-30] (-5, 5);",
        "\\strand[thick] (5, -5) to [out=150, in=-150] (5, 5);",
        "\\strand[thick] (-6, 0) to (6, 0);",
    ],
    "sizes": [
        "Medium",
    ],
    "flip": ["1", "2", "3"],
    "clip": 5
    # 123
}
