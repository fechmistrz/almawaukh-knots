#!/usr/bin/env bash
execute() {
    inform "RUNNING: $*"
    "$@"
}

inform() {
    echo "===> $*" 1>&2
}

execute ./src/merridew/bibliography_sort.py --bib src/knot_theory.bib

inform "Removing non-breaking spaces"
ack -l ' ' | grep -v Makefile | if  uname | grep -q Darwin; then :; else xargs -r sed -i 's/\xC2\xA0/ /g' || true; fi

inform "Appending newlines at the end of files"
for i in $(find src -type f -iname '*.tex' | grep -v 'src/90-appendix/dictionary.tex'); do
    {
        echo ""
        echo ""
        echo ""
        cat "$i"
        echo ""
        echo ""
        echo ""
    } | perl -p -e 's/\t/    /g' | cat -s > temporary-file;
    if ! diff temporary-file "$i"; then
        inform "Auto-fixing $i!"
        mv -v temporary-file "$i"
    else
        rm temporary-file
    fi
done;

inform "Refreshing pl-en dictionary!"
python3 tools/translate_polish_english.py \
    <(grep -r src --exclude README.md -E -e '% DICTIONARY;.*;.*;.*' -h) \
    > src/90-appendix/dictionary_tmp.tex
if ! diff src/90-appendix/dictionary{,_tmp}.tex; then
    inform "Refreshing pl-en dictionary - successful!"
    mv -v src/90-appendix/dictionary{_tmp,}.tex
else
    inform "Refreshing pl-en dictionary - skipped!"
    rm src/90-appendix/dictionary_tmp.tex
fi;

inform "Checking whether each \label has matching \ref or \pageref"
if diff \
    <(grep -Ehor src/ -e '\\label\{.*\}'  | sed -r 's/^\\label//g' | sort -u) \
    <(grep -Ehor src/ -e '\\(page)?ref\{[^}]*\}' | sed -r -e 's/^\\ref//g' -e 's/^\\pageref//g' | sort -u) | sort -k 2;
then
    inform "No broken/unused references found"
fi
