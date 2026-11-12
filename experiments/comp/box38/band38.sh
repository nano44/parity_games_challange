#!/bin/bash
# L-COMP box 38 item 1 (Lead 02:43Z: ONE band [580, 620], 2 seed streams x 1 restart x 200 steps, resumable): D_mov climb (climb38.py SCORE
# Dmov, no U constraint, KONE 1 = BOX 36/37's k = 1), seed gen37(19) (N + M 580). Stream s uses RNG seed 3800 + s. Every new best is re-run
# on ideal37 inside climb38 (agreement logged). Resumable: climb38 OUT.state; a log with DONE is skipped. Usage: band38.sh STREAM
cd "$(dirname "$0")"; s=$1; T=B600s$s
grep -q DONE out/climb38_$T.log 2>/dev/null && exit 0
python3 climb38.py $T 580 620 1 200 $((3800 + s)) out/climb38_$T.log Dmov -1 1 ../box37/inst/gen37_n19.json
