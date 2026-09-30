#!/usr/bin/env bash
set -eo pipefail

cd "$(dirname "$0")/.."

# Prose chapters only (matches the "real content" glob already documented in
# src/README.md for finding recently-edited files) - skips the generated
# appendix tables and the pl-en dictionary, which would just be noise for a
# Polish spellchecker.
misspelled=$(cat src/[12345]*/*.tex | aspell --lang=pl --mode=tex --personal="$(pwd)/tools/aspell-pl.pws" list | sort -u | tr '\n' ' ')

if [ -n "${misspelled}" ]; then
    echo "aspell flagged the following words as misspelled (or missing from tools/aspell-pl.pws):" >&2
    echo "${misspelled}" >&2
    echo "If any of these are real Polish words, technical terms, or names, add them to tools/aspell-pl.pws (one per line, keep the count on the header line in sync) and rerun." >&2
    exit 1
fi

echo "aspell: no issues found."
