#!/usr/bin/env bash
set -eo pipefail

run_and_log () {
	if [[ "${DRY_RUN}" == "true" ]]; then
        echo "Would run: $*" >&2
    else
        echo "Running: $*" >&2
        "$@"
    fi
}

generate_knot_makefile() {
    knots="3_1 4_1 5_2 6_3 7_7 8_21 9_49 10_165"
    all_knots=($(echo "${knots}" | tr ' _' '\n ' | while read -r cr last; do seq 1 "${last}" | awk -v cr="${cr}" '{printf "%d_%d\n", cr, $1}'; done))
    echo "all: ${all_knots[@]}"

    for knot in "${all_knots[@]}"; do
        echo "${knot}:"
        echo -e "\t${SCRIPT_PATH} knots ${knot}"
        echo
    done
}

generate_link_makefile() {
    links="2^2_1 4^2_1 5^2_1 6^2_3 6^3_3 7^2_8 7^3_1 8^2_16 8^3_10 8^4_3 9^2_61 9^3_21 9^4_1"
    all_links=($(echo "${links}" | tr ' ^_' '\n  ' | while read -r cr co last; do seq 1 "${last}" | awk -v cr="${cr}" -v co="${co}" '{printf "%d_%d_%d\n", cr, co, $1}'; done))
    
    echo "all: ${all_links[@]}"

    for link in "${all_links[@]}"; do
        echo "${link}:"
        echo -e "\t${SCRIPT_PATH} links ${link}"
        echo
    done
}

generate_one() {
    if [[ -f "${SCRIPT_DIR}/../data/${1}/${2}.png" ]]; then
        return 0
    fi
    TMP_PATH="${SCRIPT_DIR}/tmp"
    mkdir -pv "${TMP_PATH}";
    cd "${TMP_PATH}"
    if ! [[ -f "${2}.pdf" ]]; then
        cat << EOF | awk '{$1=$1;print}' > "${2}.kps"
            load ${2/_/.}
            about z 90
            psmode=45
            colour 0 HotPink
            colour 1 SkyBlue
            colour 2 LightGreen
            colour 3 DarkGray
            cyl-rad = 1.5 % thickness
            pserase = 1.7
            psout ${2}
EOF
        knotplot -nog < "${2}.kps" 2>/dev/null 1>/dev/null
        rm "${2}.kps"
        gs -q \
            -dCompatibilityLevel=1.3 \
            -dNOPAUSE \
            -dBATCH \
            -sPAPERSIZE=letter \
            -sDEVICE=pdfwrite \
            "-sOutputFile=${2}.pdf" "${2}.eps"
        rm "${2}.eps"
    fi
    if ! [[ -f "${2}.png" ]]; then
        convert -verbose -density 150 "${2}.pdf" -quality 100 -flatten -sharpen 0x1.0 "${2}.png" 2>/dev/null
    fi
    if ! [[ -f "${2}-trim.png" ]]; then
        run_and_log convert "${2}.png" -trim "${2}-trim.png"
    fi
    if ! [[ -f "${2}-ext.png" ]]; then
        run_and_log convert "${2}-trim.png" -gravity center -background white -extent '1200x1200' "${2}-ext.png"
    fi
    run_and_log convert "${2}-ext.png" -resize '300x300' "${SCRIPT_DIR}/../data/${1}/${2}.png"
}

SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd)"
SCRIPT_PATH="$(cd "$(dirname "$0")"; echo "${PWD}/$(basename "$0")")"

if [[ -n "$1" ]]; then
    generate_one "$1" "$2"
else
    generate_knot_makefile > "${SCRIPT_DIR}/Knots.make"
    make -f "${SCRIPT_DIR}/Knots.make" -j $(nproc) -s
    rm "${SCRIPT_DIR}/Knots.make"

    generate_link_makefile > "${SCRIPT_DIR}/Links.make"
    make -f "${SCRIPT_DIR}/Links.make" -j $(nproc) -s 
    rm "${SCRIPT_DIR}/Links.make"
fi