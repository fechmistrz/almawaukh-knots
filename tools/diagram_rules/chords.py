diagram_commands["ChordDiagramA"] = {
    "lines": [
        "\\draw[thick] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (0:5) to (180:5);",
        "\\draw[thick, first_colour] (60:5) [in=-60,out=-120] to (120:5);",
        "\\draw[thick, first_colour] (-60:5) [in=60,out=120] to (-120:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["ChordDiagramB"] = {
    "lines": [
        "\\draw[thick] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (0:5) [in=-120, out=180] to (60:5);",
        "\\draw[thick, first_colour] (120:5) [in=0, out=-60] to (180:5);",
        "\\draw[thick, first_colour] (240:5) [in=120, out=60] to (300:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["ChordDiagramC"] = {
    "lines": [
        "\\draw[thick] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (0:5) [out=180, in=-60] to (120:5);",
        "\\draw[thick, first_colour] (60:5) [in=0,out=-120] to (180:5);",
        "\\draw[thick, first_colour] (240:5) [in=120, out=60] to (300:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["ChordDiagramD"] = {
    "lines": [
        "\\draw[thick] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (0:5) to (180:5);",
        "\\draw[thick, first_colour] (60:5) [in=120,out=-120] to (300:5);",
        "\\draw[thick, first_colour] (120:5) [in=60, out=-60] to (240:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["ChordDiagramE"] = {
    "lines": [
        "\\draw[thick] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (0:5) to (180:5);",
        "\\draw[thick, first_colour] (60:5) to (240:5);",
        "\\draw[thick, first_colour] (120:5) to (300:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["OneTerm"] = {
    "lines": [
        "\\draw[densely dotted] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (20*17:5) [out=180+17*20, in=down] to (0:2) [in=180+1*20, out=up] to (20*1:5);",
        "\\draw[thick] (20*16:5) arc (20*16:20*20:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["FourTermA"] = {
    "lines": [
        "\\draw[densely dotted] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (20*1:5) [in=180+13*20, out=180+1*20] to (20*13:5);",
        "\\draw[thick, first_colour] (20*6:5) [in=180+12*20, out=180+6*20] to (20*12:5);",
        "\\draw[thick] (20*5 :5) arc (20*5 :20*8 :5);",
        "\\draw[thick] (20*11:5) arc (20*11:20*14:5);",
        "\\draw[thick] (20*17:5) arc (20*17:20*20:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["FourTermB"] = {
    "lines": [
        "\\draw[densely dotted] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (20*0:5) [in=180+12*20, out=180+0*20] to (20*12:5);",
        "\\draw[thick, first_colour] (20*7:5) [in=180+13*20, out=180+7*20] to (20*13:5);",
        "\\draw[thick] (20*5 :5) arc (20*5 :20*8 :5);",
        "\\draw[thick] (20*11:5) arc (20*11:20*14:5);",
        "\\draw[thick] (20*17:5) arc (20*17:20*20:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["FourTermC"] = {
    "lines": [
        "\\draw[densely dotted] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (20*0:5) [in=180+6*20, out=180+0*20] to (20*6:5);",
        "\\draw[thick, first_colour] (20*1:5) [in=180+13*20, out=180+1*20] to (20*13:5);",
        "\\draw[thick] (20*5 :5) arc (20*5 :20*8 :5);",
        "\\draw[thick] (20*11:5) arc (20*11:20*14:5);",
        "\\draw[thick] (20*17:5) arc (20*17:20*20:5);",
    ],
    "sizes": ["Large"],
}
diagram_commands["FourTermD"] = {
    "lines": [
        "\\draw[densely dotted] (-0, 0) circle (5);",
        "\\draw[thick, first_colour] (20*0:5) [in=180+12*20, out=180+0*20] to (20*12:5);",
        "\\draw[thick, first_colour] (20*1:5) [in=180+7*20, out=180+1*20] to (20*7:5);",
        "\\draw[thick] (20*5 :5) arc (20*5 :20*8 :5);",
        "\\draw[thick] (20*11:5) arc (20*11:20*14:5);",
        "\\draw[thick] (20*17:5) arc (20*17:20*20:5);",
    ],
    "sizes": ["Large"],
}
