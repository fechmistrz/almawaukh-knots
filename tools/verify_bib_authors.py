#!/usr/bin/env python3

import argparse
import logging
import re

def extract_authors(bib_file):
    authors = list()
    with open(bib_file) as f:
        for raw_line in f:
            if "AUTHOR" not in raw_line:
                continue
            authors_with_and = re.sub("^ *AUTHOR *= *\{(.*)\},$", r"\1", raw_line.strip())
            authors.extend(authors_with_and.split(" and "))
    return authors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib", help="Path to the bibliography file", required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    surnames_to_firstnames = dict()
    for author in extract_authors(args.bib):
        surname, firstname = author.split(", ")
        if surname not in surnames_to_firstnames:
            surnames_to_firstnames[surname] = set()
        surnames_to_firstnames[surname].add(firstname)

    for surname, firstnames in surnames_to_firstnames.items():
        if len(firstnames) == 1:
            continue
        print(f"Surname {surname} doesn't match exactly one firstname: {firstnames}")
