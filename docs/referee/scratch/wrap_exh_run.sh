#!/usr/bin/env bash
# REFEREE s33: every game H on 1, 2, 3 vertices with priorities 0..2, every s0. Logs wrap_logs/exh_*.out
cd "$(dirname "$0")"; mkdir -p wrap_logs
for mode in xi spec; do
  python3 -I wrap_replay.py $mode exh 1 2 > wrap_logs/exh_${mode}_n1.out 2>&1
  python3 -I wrap_replay.py $mode exh 2 2 > wrap_logs/exh_${mode}_n2.out 2>&1
  for k in 0 1 2 3; do python3 -I wrap_replay.py $mode exh 3 2 $k 4 > wrap_logs/exh_${mode}_n3_part$k.out 2>&1 & done
  wait
done
PERM=1 python3 -I wrap_replay.py xi exh 2 2 > wrap_logs/exh_xi_n2_perm.out 2>&1
echo "exh done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
