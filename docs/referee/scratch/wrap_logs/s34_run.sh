#!/usr/bin/env bash
# REFEREE s34: re-run of my lane's wrap_replay.py (s33; own engine rl_engine.py, no lane code) on NEW seeds, for the first review of
# P-N5-WRAP (claude/l-si e01447e7). Five families x two modes, 2,000 games each, n <= 10; PERM=1 (another index order) on rand, xi.
cd "$(dirname "$0")/.."
for mode in xi spec; do for fam in rand dup even odd twin; do
  python3 -I wrap_replay.py $mode $fam 3440 2000 10 > wrap_logs/s34_${mode}_${fam}_3440.out 2>&1; echo "$mode $fam exit $?"
done; done
PERM=1 python3 -I wrap_replay.py xi rand 3441 2000 10 > wrap_logs/s34_xi_rand_3441_perm.out 2>&1; echo "perm exit $?"
python3 -I wrap_f11.py 1 2 3 4 5 6 7 8 9 10 > wrap_logs/s34_f11_H_fig4.out 2>&1; echo "f11 H exit $?"
