#!/usr/bin/env bash
# Fast self-check of box 24 (run by scripts/verify.sh via experiments/*/check.sh): n5-box23/rstar.py reproduces the pinned W-run lengths
# C4_F3 (|F| 3 = n - 1, exhaustive max at n 4) and F8_n8 (|F| 8 > n - 1, least n found with |F| > n - 1; R*_F 4).
set -e
cd "$(dirname "$0")"
python3 ../n5-box23/rstar.py instances/C4_F3.pg instances/C4_F3.start | grep -q "'runs': 1, 'viol_freered': 0, 'incl_ne_strict': 0, 'rs': 0, 'ri': 0, 'fl': 0, 'F': 3," \
  || { echo "n5-box24 check FAILED: C4_F3"; exit 1; }
python3 ../n5-box23/rstar.py instances/F8_n8.pg instances/F8_n8.start | grep -q "'runs': 1, 'viol_freered': 0, 'incl_ne_strict': 0, 'rs': 4, 'ri': 4, 'fl': 0, 'F': 8," \
  || { echo "n5-box24 check FAILED: F8_n8"; exit 1; }
echo "n5-box24 check OK"
