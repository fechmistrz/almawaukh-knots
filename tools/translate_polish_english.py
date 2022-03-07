#!/usr/bin/env python3
# usage: python3 translate_polish_english.py <(grep -r path-to-theory-of-knots/src -E -e '% DICTIONARY;.*;.*;.*' -h)

# converts this:
# % DICTIONARY;braid;warkocz;-
# % DICTIONARY;strand;pasmo ...;warkocz
# % DICTIONARY;pure;czysty;warkocz
# % DICTIONARY;closure of ...;domknięcie ...;warkocz
# % DICTIONARY;braid number;liczba warkoczowa;-
# into this:
# \item \textbf{warkocz}: braid (\emph{czysty}: pure, \emph{domknięcie ...}: closure of ..., \emph{pasmo ...}: strand)

# TODO: implement argparse
import logging
import sys

# TODO: add argparse option to handle logging levels
# logging.basicConfig(level=logging.INFO)

top_level_entries = dict()
second_level_unparsed = list()

with open(sys.argv[1]) as f:
    for line in f:
        logging.info(f"Loading line: '{line}'")
        _, english, polish, parent = line.strip().split(";")
        logging.info(f"English '{english}', Polish '{polish}', parent '{parent}'")

        if parent == "-":
            top_level_entries[polish] = {
                "translation": english,
                "children": dict()
            }
        else:
            second_level_unparsed.append((english, polish, parent))

for line in second_level_unparsed:
    english, polish, parent = line
    logging.info(f"English '{english}', Polish '{polish}', parent '{parent}' (2nd level entry)")
    top_level_entries[parent]["children"][polish] = english

top_level_entries = {k: top_level_entries[k] for k in sorted(top_level_entries)}

for polish_word, details in top_level_entries.items():
    print(f"\\item \\textbf{{{polish_word}}}: {details['translation']}")
    if details["children"]:
        sorted_children = {polish_child: details["children"][polish_child] for polish_child in sorted(details["children"])}
        print("(" + ", ".join([
            f"\\emph{{{polish_subword}}}: {english_subword}" for polish_subword, english_subword in sorted_children.items()
        ]) + ")")