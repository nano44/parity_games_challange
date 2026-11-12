#!/bin/bash
# L-RED-B: the climbs (set H), restart-safe: each climb resumes from work/climb2_<tag>.json and is skipped once its output
# ends with "CLIMB2 ... done". Run from experiments/red-b:  bash run_h.sh [1|2]   (two disjoint halves, for two jobs)
set -u
export PYTHONDONTWRITEBYTECODE=1
N=../new
H1=("stallflips 11 40000 12 26" "minch 12 40000 12 26" "R 13 40000 12 26" "betavals 14 40000 12 26" "plat 15 40000 12 26"
    "loud 16 40000 12 26" "mvals 17 40000 12 26" "Tn 18 40000 12 26" "platrel 19 40000 14 30" "maxgate 20 40000 12 26"
    "RoverQ 21 40000 12 26" "lamvals 22 40000 12 26")
H2=("stallflips 31 6000 52 110 inst/CFI3_n48.json" "stallflips 32 6000 52 110 $N/box203/inst/MWR4_2.json"
    "minch 33 6000 52 110 $N/box206/inst/K1L10_n48.json" "R 34 6000 52 110 $N/box203/inst/K1F21_n48.json"
    "plat 35 6000 52 110 $N/box206/inst/BLKX26_n48.json" "loud 36 6000 120 230 $N/box202/inst/DSALT6_n108.json"
    "betavals 37 6000 52 110 inst/RINT_n48.json" "phi 38 6000 52 110 $N/box206/inst/CW4_n.json"
    "T 39 6000 52 110 $N/box206/inst/K1L7_n48.json" "maxgate 40 6000 52 110 $N/box203/inst/MWR4_2.json"
    "phi 41 30000 24 50" "T 42 30000 24 50" "stallflips 43 30000 24 50" "plat 44 30000 24 50")
run() { set -- $1; local tag="$1_s$2_N$4_M$5"; [ $# -ge 6 ] && tag="${tag}_$(basename $6 .json)"; local out="data/climb2_${tag}.out"
  grep -q "^CLIMB2 .* done" "$out" 2>/dev/null || python3 climb2.py "$@" >> "$out" 2>&1; }
case "${1:-1}" in
1) for s in "${H1[@]}"; do run "$s"; done ;;
2) for s in "${H2[@]}"; do run "$s"; done ;;
esac
echo "run_h ${1:-1} finished"
