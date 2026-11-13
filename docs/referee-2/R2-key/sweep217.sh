#!/usr/bin/env bash
# REFEREE-2 41: every output of the box 217 §6-§7 pre-read (R2-key-preread Addendum 3). Usage (from the repository root):
#   python3 docs/referee-2/R2-key/get217.py WORK ; bash docs/referee-2/R2-key/sweep217.sh WORK OUT
# WORK is prepared by get217.py; OUT is a scratch directory that receives the outputs (the unit217_*.out files of record are copies of
# OUT/unit217_*.out; OUT/ctrl_*.out and OUT/chunks/ are intermediate). Resumable: an output that already ends with its FIRED line is kept.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; W="$(cd "$1" && pwd)"; mkdir -p "$2/chunks"; OUT="$(cd "$2" && pwd)"; cd "$W"
U="python3 $HERE/r2unit217.py"
run() { f="$OUT/$1"; shift; if [ -s "$f" ] && grep -q '^FIRED\|^CYC-CTRL' "$f"; then return 0; fi; "$@" > "$f.tmp" 2>&1; mv "$f.tmp" "$f"; }
run unit217_towers.out $U --bridge both --red --supply towers/*.json
run unit217_rec.out $U --bridge both --red --supply rec/*.json red/H5PLUS_L5.json
run unit217_rand.out $U --quiet --gen 3000 41 acyc --lad 1500 42 6 --lad 600 43 10 --xtw 800 44 6
run unit217_randG3.out $U --quiet --bridge both --red --gen 600 45 acyc --lad 120 46 4
run unit217_mut.out $U --quiet --mut 150 51 4 towers/HIT7_d28_F254.json --mut 150 52 4 towers/H6_d24_F126.json --mut 150 53 4 towers/H5_d20_F62.json --mut 150 54 6 towers/RECF4_d20_F60.json --mut 150 55 6 towers/DBL4_d20_F30.json
run unit217_mutG3.out $U --quiet --bridge run --red --mut 12 56 4 towers/H5_d20_F62.json --mut 12 57 6 towers/RECF4_d20_F60.json --mut 12 58 6 towers/DBL4_d20_F30.json
for c in howard aall kmax khalf a3any a4half a7direct a7nop a7path xfhalf l0k l0w; do run "ctrl_$c.out" $U --quiet --ctrl $c towers/*.json --gen 300 61 acyc; done
for c in brpar brstd; do run "ctrl_$c.out" $U --quiet --ctrl $c --bridge both --gen 150 62 acyc; done
run ctrl_kmax_red.out $U --quiet --ctrl kmax --red --gen 150 62 acyc
run ctrl_cyc.out $U --cyc 300 63
run unit217_lift.out $U --bridge run --red --lift 0 towers/H5_d20_F62.json --lift 10 towers/H5_d20_F62.json --lift 40 towers/H5_d20_F62.json --lift 30 towers/DBL4_d20_F30.json
run unit217_e2n7.out $U corp/l-comp/experiments/comp/box38/out/argmax/S_N16M16_U10_elev.json corp/l-red/experiments/red/r207/keep/Tstar_d5_T17.json
run unit217_corpus1p.out $U --quiet --list corpus.list
[ -e "$OUT/chunks/c_000" ] || split -l 25 -d -a 3 corpus.list "$OUT/chunks/c_"
for c in "$OUT"/chunks/c_???; do run "chunks/$(basename "$c").out" $U --quiet --bridge both --red --list "$c"; done
python3 "$HERE/sum217.py" "$OUT"/chunks/c_???.out > "$OUT/unit217_corpus.out"
( for c in howard aall kmax khalf a3any a4half a7direct a7nop a7path xfhalf l0k l0w brpar brstd kmax_red; do echo "ctrl $c: $(grep '^FIRED' "$OUT/ctrl_$c.out")"; done; cat "$OUT/ctrl_cyc.out" ) > "$OUT/unit217_ctrl.out"
echo "sweep217 done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
