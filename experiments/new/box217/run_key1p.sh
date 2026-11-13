#!/usr/bin/env bash
# Packet P-N5-KEY1P, pinned DATA outputs (not re-run by verify; a few minutes in all). Run from experiments/new/box217: bash run_key1p.sh
# Resumable: a finished output file (last line «DONE») is skipped.
set -uo pipefail
T=../box212/inst; O=out
job() { local f="$O/$1"; shift; if [ -f "$f" ] && [ "$(tail -1 "$f")" = "DONE" ]; then return 0; fi; "$@" > "$f.tmp" 2>&1 && echo DONE >> "$f.tmp" && mv "$f.tmp" "$f"; }
job key1p_towers_n5.out python3 key1p.py --n5 --levels $T/DBL4_d20_F30.json $T/H5_d20_F62.json $T/H6_d24_F126.json $T/HIT7_d28_F254.json $T/RECF4_d20_F60.json
job key1p_rec.out       python3 key1p.py out/rec/*.json
job key1p_mut.out       python3 key1p.py --mut 7703 200 $T/DBL4_d20_F30.json $T/H5_d20_F62.json $T/H6_d24_F126.json $T/HIT7_d28_F254.json $T/RECF4_d20_F60.json
job key1p_mut_n5.out    python3 key1p.py --n5 --mut 7704 12 $T/DBL4_d20_F30.json $T/RECF4_d20_F60.json
job key1p_rand.out      bash -c 'for s in 2154 2155 2156; do python3 key1p.py --rand $s 300; done; for s in 7701 7705 7706; do python3 key1p.py --randlad $s 2000; done; for s in 7702 7707; do python3 key1p.py --n5 --randlad $s 200; done'
job key1p_rec_n5.out    python3 key1p.py --n5 out/rec/*.json
job key1p_lift.out      bash -c 'for d in 0 10 40; do python3 key1p.py --lift $d ../box212/inst/H5_d20_F62.json; done; for d in 10 40; do python3 key1p.py --n5 --lift $d ../box212/inst/H5_d20_F62.json; done'
