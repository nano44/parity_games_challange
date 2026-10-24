#!/bin/bash
# REFEREE-2 R2-N5-U1 batch (final checker version). Run from this directory. Every log ends with RESULT.
mkdir -p logs
python3 u1_check.py random 3000 6 14 511 > logs/rand_511.txt 2>&1 &
python3 u1_check.py random 1500 12 20 512 > logs/rand_512.txt 2>&1 &
python3 u1_check.py random 3000 6 14 551 > logs/rand_551.txt 2>&1 &
python3 tb_general.py 3000 5 16 531 > logs/tbgen_531.txt 2>&1 &
python3 tb_general.py 1000 16 30 532 > logs/tbgen_532.txt 2>&1 &
python3 tb_arena.py 20000 4 14 541 > logs/tbarena_541.txt 2>&1 &
for f in ../../../experiments/new/box31/instances/*.pg ../../../experiments/new/box29/instances/*.pg ../../../experiments/red/xing/instances/*.pg ../../../experiments/n5-exhaustive/instances/b5_os_n*.pg ../../../experiments/n5-exhaustive/instances/b6_xw_n32.pg; do
  [ -f "$f" ] || continue
  b=$(basename $f .pg); python3 u1_check.py inst $f 10 > logs/inst_$b.txt 2>&1
done
wait
