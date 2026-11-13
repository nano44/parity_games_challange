#!/bin/bash
# L-COMP box 47: search lanes (search47 + one47.h = the 1P(G) port, checked by run47b.sh). Lead 09:08Z / 09:15Z: objective T_key, and the
# ENUMERATION DEPTH k(G) (SCORE=K; target k = 8; min d per k). d is fixed per lane by its seed (gen47 mutations keep levels and N).
# Seeds: inst/towers (HIT7 etc.) and lifts by lift47.py (TOP-ADD). Each launch runs ~6,600 s, then exits; re-launch resumes (OUT.state).
# Output out/lanes/<LANE>.log, <LANE>.state, <LANE>_BEST_k*_T*_d*_N*_NM*_<hash>.txt (gen47 text; gen47.py t2j for JSON).
# Usage: run47c.sh LANE   (LANE = K28 | K32 | K36 | T<N>)
set -u; cd "$(dirname "$0")"; mkdir -p out/lanes inst/seeds bin
gcc -O2 -Wno-unused-function -Wno-misleading-indentation -I. -DMODEL='"one47.h"' -o bin/search47 search47.c -lm || exit 1
seed() { local base=$1 k=$2 out=inst/seeds/$3; [ -f $out.txt ] && return; python3 -B lift47.py inst/towers/$base.json $k $out.json >/dev/null && python3 -B gen47.py j2t $out.json $out.txt; }
case "$1" in
K28) seed HIT7_d28_F254 0 HIT7_d28; S=inst/seeds/HIT7_d28.txt; CAP=260; SC=K; SD=4728 ;;
K32) seed HIT7_d28_F254 4 HIT7_d32; S=inst/seeds/HIT7_d32.txt; CAP=300; SC=K; SD=4732 ;;
K36) seed HIT7_d28_F254 8 HIT7_d36; S=inst/seeds/HIT7_d36.txt; CAP=340; SC=K; SD=4736 ;;
K24) seed H6_d24_F126 0 H6_d24; S=inst/seeds/H6_d24.txt; CAP=220; SC=K; SD=4724 ;;
T*) n=${1#T}; k=$(( (n - 56) / 2 )); seed HIT7_d28_F254 $k HIT7_N$n; S=inst/seeds/HIT7_N$n.txt; CAP=$(( 3 * n + 40 )); SC=T; SD=$((4700 + n)) ;;
*) echo usage; exit 2 ;;
esac
SCORE=$SC timeout 6600 ./bin/search47 $S out/lanes/$1 $CAP 4000000000 $SD ${TEMP0:-2.0} ${UNIT:-200000}
echo "run47c $1 exit $?"
