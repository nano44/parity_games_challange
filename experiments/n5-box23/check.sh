#!/usr/bin/env bash
# Fast self-check of box 23 (run by scripts/verify.sh via experiments/*/check.sh): rstar.py (R*_F / FL_F per W-run, n5b SPEC) reproduces
# its pinned values: rs8_n10 (one W-run, |F| 10, R*_F 8, FL_F 1) and n5-epoch's ffin4_n24 with its start (R*_F 2, |F| 8, = L-NEW xirise_alt).
set -e
cd "$(dirname "$0")"
python3 rstar.py instances/rs8_n10.pg instances/rs8_n10.start | grep -q "'runs': 1, 'viol_freered': 0, 'incl_ne_strict': 0, 'rs': 8, 'ri': 8, 'fl': 1, 'F': 10," \
  || { echo "n5-box23 check FAILED: rs8_n10"; exit 1; }
python3 rstar.py ../n5-epoch/instances/ffin4_n24.pg ../n5-epoch/instances/ffin4_n24.start | grep -q "'runs': 3, 'viol_freered': 0, 'incl_ne_strict': 0, 'rs': 2, 'ri': 2, 'fl': 0, 'F': 8," \
  || { echo "n5-box23 check FAILED: ffin4_n24"; exit 1; }
echo "n5-box23 check OK"
