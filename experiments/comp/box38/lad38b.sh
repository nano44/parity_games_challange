#!/bin/bash
# L-COMP box 38 item 2(b) batch 2: U-ladders on L-SI 85 TC/CL instances (inst/si85_*, copied from claude/l-new 1478886e
# experiments/new/box196/inst_si85, sha1 in inst/SHA1SUMS) and UP ladders from U = 0 endpoints. Resumable per ladder.
cd "$(dirname "$0")"; mkdir -p out/lad
run() { o=out/lad/$1.out; [ -s "$o" ] && grep -q LADEND "$o" && return; rm -f "$o"; python3 ladder38.py "${@:2}" out/lad/g $1 > "$o" && echo LADEND >> "$o"; }
for b in TC2 TC3 CL2_22 CL3_32; do for s in rand1 rand2; do run si85${b}_down_$s inst/si85_$b.json down $s; done; done
run si85TC2_down_greedy inst/si85_TC2.json down greedy
run g37n4_up_rand1 out/lad/g/g37n4_down_greedy_U0.json up rand1
run g37n8_up_rand1 out/lad/g/g37n8_down_greedy_U0.json up rand1
run si85TC3_up_rand1 out/lad/g/si85TC3_down_rand1_U0.json up rand1
echo LADBDONE
