#!/usr/bin/env bash
set -xeo pipefail

knotplot_wrapper() {
    knotplot -nog < "${1}.kps"
	gs -q \
        -dCompatibilityLevel=1.3 \
        -dNOPAUSE \
        -dBATCH \
        -sPAPERSIZE=letter \
        -sDEVICE=pdfwrite \
        "-sOutputFile=${1}.pdf" "${1}.eps"
}

cd "$(readlink -f "$(dirname "$0")")"

for knot in 3_1 4_1 5_2 6_3 7_7 8_21 9_49 10_165; do
    read -r crossing count <<<"$(echo "$knot" | tr '_' ' ')"
    for id in $(seq 1 $count); do
        if ! [[ -f "${crossing}_${id}.pdf" ]]; then
            echo -en "load ${crossing}.${id}\nabout z 90\npsmode=45\ncolour 0 HotPink\ncyl-rad = 1.5 % thickness\npserase = 1.7\npsout ${crossing}_${id}\n" > "${crossing}_${id}.kps"
            knotplot_wrapper "${crossing}_${id}"
        fi
        if ! [[ -f "${crossing}_${id}.png" ]]; then
            convert -verbose -density 150 "${crossing}_${id}.pdf" -quality 100 -flatten -sharpen 0x1.0 "${crossing}_${id}.png"
        fi
        if ! [[ -f "${crossing}_${id}-trim.png" ]]; then
            convert "${crossing}_${id}.png" -trim "${crossing}_${id}-trim.png"
        fi
        if ! [[ -f "${crossing}_${id}-ext.png" ]]; then
            convert "${crossing}_${id}-trim.png" -gravity center -background white -extent '1200x1200' "${crossing}_${id}-ext.png"
        fi
        convert "${crossing}_${id}-ext.png" -resize '300x300' "../knots/${crossing}_${id}.png"
    done;
done
