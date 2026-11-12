#!/usr/bin/env bash
# L-SI box 95 check: P-N5-GATE fix rounds (fix1: G1-G6 + line L-1).
set -u
cd "$(dirname "$0")"
bash fix1/check_fix1.sh || { echo "BOX95 FAIL fix1"; exit 1; }
bash fix2/check_fix2.sh || { echo "BOX95 FAIL fix2"; exit 1; }
bash fix3/check_fix3.sh || { echo "BOX95 FAIL fix3"; exit 1; }
