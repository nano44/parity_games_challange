#!/usr/bin/env bash
# Fast self-check of box 25 (run by scripts/verify.sh via experiments/*/check.sh): ins.py (INS / KEYCH, n5b) reproduces L-SI's treestab.py
# value on u23sw64_n32 (KEYCH 8 = 1 + INS 7) and the pinned climb witness ins8_n32 (INS 8, |I| 9, W-run 15).
set -e
cd "$(dirname "$0")"
python3 ins.py ../red/xing/instances/u23sw64_n32.pg | grep -q "intervals 1 LTX 0 TSX 0 NOVT 0 KB 0 MAXKEYCH 8 MAXINS 7 " || { echo "n5-box25 check FAILED: u23sw64_n32"; exit 1; }
python3 ins.py instances/ins8_n32.pg instances/ins8_n32.start | grep -q "MAXINS 8 MAXINS2 7 | max-INS interval: INS 8 |I| 9 W-run 15" || { echo "n5-box25 check FAILED: ins8_n32"; exit 1; }
echo "n5-box25 check OK"
