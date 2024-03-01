#!/usr/bin/env bash
set -eo pipefail

knotplot_wrapper() {
    knotplot -nog < "${1}.kps"
    rm "${1}.kps"
	gs -q \
        -dCompatibilityLevel=1.3 \
        -dNOPAUSE \
        -dBATCH \
        -sPAPERSIZE=letter \
        -sDEVICE=pdfwrite \
        "-sOutputFile=${1}.pdf" "${1}.eps"
    rm "${1}.eps"
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

for link in 2^2_1 4^2_1 5^2_1 6^2_1 6^2_2 6^2_3 6^3_1 6^3_2 6^3_3 7^2_1 7^2_2 7^2_3 7^2_4 7^2_5 7^2_6 7^2_7 7^2_8 7^3_1 8^2_1 8^2_2 8^2_3 8^2_4 8^2_5 8^2_6 8^2_7 8^2_8 8^2_9 8^2_10 8^2_11 8^2_12 8^2_13 8^2_14 8^2_15 8^2_16 8^3_1 8^3_2 8^3_3 8^3_4 8^3_5 8^3_6 8^3_7 8^3_8 8^3_9 8^3_10 8^4_1 8^4_2 8^4_3 9^2_1 9^2_2 9^2_3 9^2_4 9^2_5 9^2_6 9^2_7 9^2_8 9^2_9 9^2_10 9^2_11 9^2_12 9^2_13 9^2_14 9^2_15 9^2_16 9^2_17 9^2_18 9^2_19 9^2_20 9^2_21 9^2_22 9^2_23 9^2_24 9^2_25 9^2_26 9^2_27 9^2_28 9^2_29 9^2_30 9^2_31 9^2_32 9^2_33 9^2_34 9^2_35 9^2_36 9^2_37 9^2_38 9^2_39 9^2_40 9^2_41 9^2_42 9^2_43 9^2_44 9^2_45 9^2_46 9^2_47 9^2_48 9^2_49 9^2_50 9^2_51 9^2_52 9^2_53 9^2_54 9^2_55 9^2_56 9^2_57 9^2_58 9^2_59 9^2_60 9^2_61 9^3_1 9^3_2 9^3_3 9^3_4 9^3_5 9^3_6 9^3_7 9^3_8 9^3_9 9^3_10 9^3_11 9^3_12 9^3_13 9^3_14 9^3_15 9^3_16 9^3_17 9^3_18 9^3_19 9^3_20 9^3_21 9^4_1; do
    echo link $link;
    read -r crossing components id <<<"$(echo "$link" | tr '^_' '  ')"
    if ! [[ -f "${crossing}_${components}_${id}.pdf" ]]; then
        echo -en "load ${crossing}.${components}.${id}\nabout z 90\npsmode=45\ncolour 0 HotPink\ncolour 1 SkyBlue\ncolour 2 LightGreen\ncolour 3 DarkGray\ncyl-rad = 1.5 % thickness\npserase = 1.7\npsout ${crossing}_${components}_${id}\n" > "${crossing}_${components}_${id}.kps"
        knotplot_wrapper "${crossing}_${components}_${id}"
    fi
    if ! [[ -f "${crossing}_${components}_${id}-ext.png" ]]; then
        convert -verbose -density 150 "${crossing}_${components}_${id}.pdf" -quality 100 -flatten -sharpen 0x1.0 "${crossing}_${components}_${id}.png"
        convert "${crossing}_${components}_${id}.png" -trim "${crossing}_${components}_${id}-trim.png"
        rm "${crossing}_${components}_${id}.png"
        convert "${crossing}_${components}_${id}-trim.png" -gravity center -background white -extent '1200x1200' "${crossing}_${components}_${id}-ext.png"
        rm "${crossing}_${components}_${id}-trim.png"
    fi
    convert "${crossing}_${components}_${id}-ext.png" -resize '300x300' "../links/${crossing}_${components}_${id}.png"
done