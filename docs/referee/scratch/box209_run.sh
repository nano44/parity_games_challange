#!/usr/bin/env bash
# REFEREE s33: sets of box209_replay.py. INST = directory holding experiments/new/box*/inst of claude/l-new 311bbf81 (git archive).
cd "$(dirname "$0")"; mkdir -p box209_logs; I="$1"
python3 -I box209_replay.py files $I/box202/inst/*.json > box209_logs/files_box202.out 2>&1 &
python3 -I box209_replay.py files $I/box191/inst/*.json $I/box203/inst/*.json $I/box204/inst/*.json $I/box205/inst/*.json $I/box206/inst/*.json $I/box207/inst/*.json > box209_logs/files_other.out 2>&1 &
(for fam in rand deep wide selfl acyc; do python3 -I box209_replay.py gen $fam 3309 400 > box209_logs/gen_$fam.out 2>&1; done) &
(python3 -I box209_replay.py gen tiny 3311 20000 > box209_logs/gen_tiny.out 2>&1; python3 -I box209_replay.py gen noX 3312 3000 > box209_logs/gen_noX.out 2>&1; python3 -I box209_replay.py gen big 3313 1500 > box209_logs/gen_big.out 2>&1) &
wait
python3 -I box209_replay.py mut 3310 150 6 $I/box206/inst/K1L10_n48.json $I/box207/inst/CFI3_n48.json $I/box203/inst/MWR4_2.json $I/box207/inst/RINT_n48.json $I/box206/inst/CW4_n.json $I/box206/inst/K1D4_n48.json $I/box203/inst/K1F21_n48.json $I/box206/inst/BLKX26_n48.json > box209_logs/mut.out 2>&1
echo "box209 done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
