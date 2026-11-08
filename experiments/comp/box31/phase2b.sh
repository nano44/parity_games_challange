#!/bin/bash
# L-COMP 12 box 31 (Lead 03:31Z, test (b)): base = L7b's frozen best (sha1 0e71e029) with 24 (12:0) -> 18 and 25 (12:1) -> y. For each y,
# a short constrained climb (rclimb31, nice 15, 2e6 proposals, <= 150 s, seed 600000+i): LJ=7 LJGATE=190 FIX=20,34,24,25
# LJGUARD=20:17,34:22,24:18,25:y FROZENBELOW=0 NMIN=2 NMAX=4 ANNEAL 0.15 LV 6; variant NR adds LJNOREAD=12:0,1,2,3 (movers 0-3 must stop
# reading 12). Outputs phase2b/<y>_<var>.txt/.run; summary by phase2b_sum.py.
cd "$(dirname "$0")"; B=out/L7_FRZ_K7099382600043_L7b.txt; i=0
for y in -1 18 21 26 34 38; do
  python3 -c "import sys; sys.path.insert(0,'l-lower'); from sim6 import rd, wr; D=rd('$B'); D['xt'][24]=18; D['xt'][25]=$y; wr(D,'phase2b/start_$y.txt')"
  for var in base NR; do
    X=""; [ $var = NR ] && X="LJNOREAD=12:0,1,2,3"
    env $X LJ=7 LJGATE=190 FIX=20,34,24,25 LJGUARD=20:17,34:22,24:18,25:$y FROZENBELOW=0 NMIN=2 NMAX=4 ANNEAL=0.15 LV=6 OUT=phase2b/${y}_$var.txt \
      timeout 150 nice -n 15 bin/rclimb31 phase2b/start_$y.txt $((600000+i)) 2000000 > phase2b/${y}_$var.run 2>&1
    echo "$(date -u +%FT%TZ) y $y $var exit $? $(tail -n 1 phase2b/${y}_$var.txt | grep -o 'T [0-9]*\|lj_.*' | tr '\n' ' ')"; i=$((i+1))
  done
done
