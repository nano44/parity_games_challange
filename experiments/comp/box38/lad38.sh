#!/bin/bash
# L-COMP box 38 item 2(b): U-ladder batch on gen37(n) (box37/inst). Resumable: a ladder whose .out has a U0 row (down) or ends is skipped.
cd "$(dirname "$0")"; mkdir -p out/lad
run() { o=out/lad/$1.out; [ -s "$o" ] && grep -q '"U": 0,' "$o" && return; rm -f "$o"; python3 ladder38.py "${@:2}" out/lad/g $1 > "$o"; }
for n in 2 3 4 5 6 8 10 12; do run g37n${n}_down_greedy ../box37/inst/gen37_n$n.json down greedy; done
for n in 2 4 8 12; do run g37n${n}_down_rand1 ../box37/inst/gen37_n$n.json down rand1; run g37n${n}_down_rand2 ../box37/inst/gen37_n$n.json down rand2; done
for n in 2 4 8; do run g37n${n}_down_greedy_noelev ../box37/inst/gen37_n$n.json down greedy --noelev; done
echo LADDONE
