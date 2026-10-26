#!/usr/bin/env bash
# Fast self-check of the box-12 epoch census (run by scripts/verify.sh via experiments/*/check.sh):
# N_ep of three pinned lane instances from S3 (lap_n6 3, so_th_n32 31, lev_l_x 50; reported by L-NEW / RESULTS R60) and 0 violations.
set -e
cd "$(dirname "$0")"
R=../..
for spec in "$R/experiments/new/box25/laps/lap_n6_s1_110421.pg 3" "$R/experiments/red/so/instances/so_th_n32.pg 31" "$R/experiments/si/orlens/instances/lev_l_x.pg 50"; do
  set -- $spec
  out="$(python3 census.py 0 0 "$1")"
  echo "$out" | grep -q "^max_N_ep: $2\$" || { echo "census check FAILED on $1 (expected max_N_ep $2)"; exit 1; }
  echo "$out" | grep -q "^RESULT OK violations=0\$" || { echo "census check FAILED on $1 (violations)"; exit 1; }
done
echo "n5-epoch census check OK"
