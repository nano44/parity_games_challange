#!/usr/bin/env bash
# Fast self-check of box 26 (run by scripts/verify.sh via experiments/*/check.sh): xich.py (XICH_F(v), n5b) reproduces its pins
# xich12_n16 (max XICH 12, |F| 13) and xich14_n32 (14, |F| 18, longest W-constant interval 8); both equal L-NEW xirise.py's 'xich'.
set -e
cd "$(dirname "$0")"
python3 xich.py instances/xich12_n16.pg instances/xich12_n16.start | grep -q "runs 1 maxXICH 12 (v 6) F 13 sum 39 I 0 " || { echo "n5-box26 check FAILED: xich12_n16"; exit 1; }
python3 xich.py instances/xich14_n32.pg instances/xich14_n32.start | grep -q "runs 1 maxXICH 14 (v 6) F 18 sum 209 I 8 " || { echo "n5-box26 check FAILED: xich14_n32"; exit 1; }
echo "n5-box26 check OK"
