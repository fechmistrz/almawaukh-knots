# basic tangles

diagram_commands["TangleBasicZero"] = {
    "lines": [
        "\\draw[semithick] (225:5) [in=135, out=45] to (-45:5);",
        "\\draw[semithick] (135:5) [in=-135, out=-45] to (45:5);",
        "\\draw[semithick, densely dotted] (-0, 0) circle (5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["TangleBasicInfinity"] = {
    "lines": [
        "\\draw[semithick] (225:5) [in=-45, out=45] to (135:5);",
        "\\draw[semithick] (-45:5) [in=-135, out=135]  to (45:5);",
        "\\draw[semithick, densely dotted] (-0, 0) circle (5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["TangleBasicPlus"] = {
    "lines": [
        "\\strand[semithick] (225:5) to (45:5);",
        "\\strand[semithick] (-45:5) to (135:5);",
        "\\draw[semithick, densely dotted] (-0, 0) circle (5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["TangleBasicMinus"] = {
    "lines": [
        "\\strand[semithick] (225:5) to (45:5);",
        "\\strand[semithick] (135:5) to (-45:5);",
        "\\draw[semithick, densely dotted] (-0, 0) circle (5);",
    ],
    "sizes": ["Large"],
}

# alternating?

diagram_commands["TangleAlternatingYes"] = {
    "lines": [
        "\\node [left] at (-5, -5) {SW};",
        "\\draw[semithick,latex-] (-1, -1) to (-5,-5);",
        #
        "\\node [right] at (5, 5) {NE};",
        "\\draw[semithick,latex-] (1, 1) to (5,5);",
        #
        "\\node [right] at (5, -5) {SE};",
        "\\draw[semithick,-latex] (1, -1) to (5,-5);",
        #
        "\\node [left] at (-5, 5) {NW};",
        "\\draw[semithick,-latex] (-1, 1) to (-5,5);",
        #
        "\\draw[semithick, densely dotted] (-0, 0) circle (4);",
    ],
    "sizes": ["Large"],
}
diagram_commands["TangleAlternatingNo"] = {
    "lines": [
        "\\node [left] at (-5, -5) {SW};",
        "\\draw[semithick,latex-] (-1, -1) to (-5,-5);",
        #
        "\\node [right] at (5, 5) {NE};",
        "\\draw[semithick,-latex] (1, 1) to (5,5);",
        #
        "\\node [right] at (5, -5) {SE};",
        "\\draw[semithick,latex-] (1, -1) to (5,-5);",
        #
        "\\node [left] at (-5, 5) {NW};",
        "\\draw[semithick,-latex] (-1, 1) to (-5,5);",
        #
        "\\draw[semithick, densely dotted] (-0, 0) circle (4);",
    ],
    "sizes": ["Large"],
}

# a + b = ...

diagram_commands["TangleSummandA"] = {
    "lines": [
        "\\foreach \\x in {0,1,2,3} {\\draw[semithick] (45+90*\\x:2) to (45+90*\\x:6);}",
        "\\node at (0, 0) {$T_1$};",
        "\\draw[semithick, densely dotted] (-0, 0) circle (4);",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}
diagram_commands["TangleSummandB"] = {
    "lines": [
        "\\foreach \\x in {0,1,2,3} {\\draw[semithick] (45+90*\\x:2) to (45+90*\\x:6);}",
        "\\node at (0, 0) {$T_2$};",
        "\\draw[semithick, densely dotted] (-0, 0) circle (4);",
    ],
    "sizes": ["Large"],
    "bounding": [-5, -5, 5, 5],
}
diagram_commands["TangleSumAB"] = {
    "lines": [
        # T1 straight arcs
        "\\foreach \\x in {-1} {\\foreach \\y in {-1,1} {\\draw[semithick] (-10 + 2*\\x/1.41421356237, 0 + 2*\\y/1.41421356237) to (-10 + 6*\\x/1.41421356237, 0 + 6*\\y/1.41421356237) ;}}",
        "\\draw[semithick, densely dotted] (-10, 0) circle (4);",
        "\\node at (-10, 0) {$T_1$};",
        # T2 straight arcs
        "\\foreach \\x in {1} {\\foreach \\y in {-1,1} {\\draw[semithick] (10 + 2*\\x/1.41421356237, 0 + 2*\\y/1.41421356237) to (10 + 6*\\x/1.41421356237, 0 + 6*\\y/1.41421356237) ;}}",
        "\\draw[semithick, densely dotted] (10, 0) circle (4);",
        "\\node at (10, 0) {$T_2$};",
        # upper connecting arc
        "\\draw[thick] (-10 + 2/1.41421356237, 0 + 2/1.41421356237) [in=135, out=45] to (10 - 2/1.41421356237, 0 + 2/1.41421356237);",
        # lower connecting arc
        "\\draw[thick] (-10 + 2/1.41421356237, 0 - 2/1.41421356237) [in=-135, out=-45] to (10 - 2/1.41421356237, 0 - 2/1.41421356237);",
        "\\node at (-10, 0) {$T_1$};",
        "\\node at (10, 0) {$T_2$};",
    ],
    "sizes": ["Large"],
    "bounding": [-12, -5, 12, 5],
}

# fraction

diagram_commands["TangleFraction"] = {
    "lines": [
        "\\foreach \\x in {0,1,2,3} {\\draw[semithick] (45+90*\\x:2) to (45+90*\\x:6);}",
        "\\draw[semithick, densely dotted] (-0, 0) circle (4);",
    ],
    "sizes": ["Large"],
    "bounding": [-6, -6, 6, 6],
}
diagram_commands["TangleFractionNumerator"] = {
    "lines": [
        "\\foreach \\x in {0,1,2,3} {\\draw[semithick] (45+90*\\x:2) to (45+90*\\x:6);}",
        "\\draw[semithick, densely dotted] (-0, 0) circle (4);",
        "\\draw[thick] (45+90*1:6) [in=45,out=135] to (45+90*0:6);",
        "\\draw[thick] (45+90*2:6) [in=-45,out=-135] to (45+90*3:6);",
    ],
    "sizes": ["Large"],
    "bounding": [-6, -6, 6, 6],
}
diagram_commands["TangleFractionDenominator"] = {
    "lines": [
        "\\foreach \\x in {0,1,2,3} {\\draw[semithick] (45+90*\\x:2) to (45+90*\\x:6);}",
        "\\draw[semithick, densely dotted] (-0, 0) circle (4);",
        "\\draw[thick] (45+90*1:6) [in=-135,out=135] to (45+90*2:6);",
        "\\draw[thick] (45+90*3:6) [in=45,out=-45] to (45+90*0:6);",
    ],
    "sizes": ["Large"],
    "bounding": [-6, -6, 6, 6],
}

# twists

diagram_commands["TwistsRight"] = {
    "lines": [
        "\\strand[semithick] (-10, -5) [out=right, in=left] to (0, 5) to (10, -5);",
        "\\strand[semithick] (-10, 5) [out=right, in=left] to (0, -5);",
        "\\strand[semithick] (0, -5) [out=right, in=left] to (10, 5);",
    ],
    "sizes": ["Large"],
    "flip": ["2"],
    "bounding": [-12, -5, 12, 5],
}
diagram_commands["TwistsLeft"] = {
    "lines": [
        "\\strand[semithick] (-10, -5) [out=right, in=left] to (0, 5) to (10, -5);",
        "\\strand[semithick] (-10, 5) [out=right, in=left] to (0, -5);",
        "\\strand[semithick] (0, -5) [out=right, in=left] to (10, 5);",
    ],
    "sizes": ["Large"],
    "flip": ["1"],
    "bounding": [-12, -5, 12, 5],
}
