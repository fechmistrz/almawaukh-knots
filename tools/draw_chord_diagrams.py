#!/usr/bin/env python3


def is_minimal(diagram):
    largest = 2 * len(diagram)
    for delta in range(largest):
        new_diagram = sorted([
            sorted([
                (start + delta) % largest,
                (end + delta) % largest
            ]) for start, end in diagram
        ])
        if new_diagram < diagram:
            return False
    return True

def generate_tikz(diagram):
    print(r"\begin{minipage}[b]{.16\linewidth}\[")
    print(r"\begin{tikzpicture}[baseline=-0.65ex, scale=0.15001]")
    print(r"\begin{knot}[clip width=15, end tolerance=1pt]")
    print(r"    \useasboundingbox (-7, -5) rectangle (7, 5); % REMOVE ME")
    for start, end in diagram:
        epsilon = 0
        start_angle = int(start * 180.0 / DIAGRAM_ORDER)
        end_angle   = int(end   * 180.0 / DIAGRAM_ORDER)
        print(f"    \draw[thick, first_colour] ({start_angle}:5) [in={180 + epsilon + end_angle}, out={180 - epsilon + start_angle}] to ({end_angle}:5);")
    print(r"    \draw[very thick] (-0, 0) circle (5);")
    print(r"\end{knot}")
    print(r"\end{tikzpicture}")
    print(r"\]\end{minipage}")


def find_all(size):
    queue = [
        [[], list(range(2*size))]
    ]
    diagrams = list()
    while queue:
        done, not_done = queue.pop(0)
        if not not_done:
            diagrams.append(done)
            continue
        new_done_from = not_done[0]
        for new_done_to in not_done[1:]:
            queue.append(
                [
                    done + [[new_done_from, new_done_to]],
                    [x for x in not_done if x not in [new_done_from, new_done_to]]
                ]
            )   
    return [x for x in diagrams if is_minimal(x)]

for DIAGRAM_ORDER in [1, 2, 3, 4]:
    for diagram in find_all(DIAGRAM_ORDER):
        generate_tikz(diagram)

# https://oeis.org/A007769, https://oeis.org/A054499