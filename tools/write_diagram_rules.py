def generate_command(command_name, command_details):
    if isinstance(command_details["sizes"], list) and len(command_details["sizes"]) > 0:
        for size in command_details["sizes"]:
            command_copy = {k: v for k, v in command_details.items()}
            command_copy["sizes"] = size
            # print(command_details)
            # print(command_copy)
            generate_command(size + command_name, command_copy)
        return

    command_copy = {k: v for k, v in command_details.items()}
    command_copy["lines"] = [item for item in command_copy["lines"] if "% REMOVE ME" not in item]

    scale = 0.999
    clip = 99
    bound1, bound2, bound3, bound4 = -5, -5, 5, 5
    if "Huge" in command_name:
        scale = 0.25001
        clip = 12
        bound1, bound3 = -7, 7
    elif "Large" in command_name:
        scale = 0.15001
        clip = 6
        bound1, bound3 = -7, 7
    elif "MedLar" in command_name:
        scale = 0.13
        clip = 5
        bound1, bound3 = -7, 7
    elif "Medium" in command_name:
        scale = 0.06001
        clip = 7
        bound1, bound3 = -7, 7
    elif "Small" in command_name:
        scale = 0.03001
        clip = 5

    if "bounding" in command_copy.keys():
        bound1, bound2, bound3, bound4 = command_copy["bounding"]
    if "clip" in command_copy.keys():
        clip = command_copy["clip"]

    command_copy["lines"].insert(
        0, f"\\useasboundingbox ({bound1}, {bound2}) rectangle ({bound3}, {bound4}); % REMOVE ME"
    )

    options = [f"clip width={clip}", "end tolerance=1pt"]
    if "flip" in command_copy.keys():
        options.append("flip crossing/.list={" + ",".join(command_copy["flip"]) + "}")
    if command_details.get("pink", False):
        options.append(f"background color=ocre!15")

    print(f"\\newcommand{{\\{command_name}}} {{\\begin{{tikzpicture}}[baseline=-0.65ex, scale={scale}]")
    print(f"    \\begin{{knot}}[{', '.join(options)}]")
    for line in command_copy["lines"]:
        print("        " + line)
    # print("\\draw[thick,red,fill=red] (-0, 0) circle (3);")
    print("    \\end{knot}")
    print("\\end{tikzpicture}}")
    print()

if "diagram_commands" not in vars():
    diagram_commands = dict()

for k, v in diagram_commands.items():
    generate_command(k, v)
