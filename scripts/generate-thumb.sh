#!/usr/bin/env bash

set -euo pipefail

ISSUE=${1:-"01"}
DENSITY=${2:-"20"}
INPUT_FILE=./public/pdfs/tuttostort-${ISSUE}.pdf
OUTPUT_FILE=./public/img/tuttostort-${ISSUE}.jpg

magick -density ${DENSITY} ${INPUT_FILE}'[0]' ${OUTPUT_FILE}
