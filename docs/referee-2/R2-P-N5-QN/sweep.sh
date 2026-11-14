#!/bin/bash
# REFEREE-2 successor 35: P-N5-QN own replay. Usage: sweep.sh ARCHIVE_DIR(experiments/new of e252182d, with k1fail_202.json) OUTDIR
X=$1; O=$2; T=$(dirname "$(readlink -f "$0")")/r2qn.py
python3 $T $X/k1fail_202.json $X/box202/inst/*.json $X/box203/inst/*.json > $O/pinned.out 2>&1
python3 $T --gen 3000 2 > $O/gen2.out
python3 $T --gen 3000 3 > $O/gen3.out
python3 $T --ctrl --gen 300 4 > $O/ctrl_gen.out
python3 $T --ctrl $X/k1fail_202.json $X/box203/inst/MWR4_2.json $X/box203/inst/MWR8_2.json > $O/ctrl_pinned.out
grep -h TOTAL $O/*.out
