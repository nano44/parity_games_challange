#!/usr/bin/env bash
# Packet P-N5-KEY1P, verify-time check (about 40 s): must-0 counters of key1p.py on the 5 towers (with N5 itself on the two smallest),
# on random sets, and the seven controls. Output is compared with the pinned check_key1p.out by experiments/new/check.sh.
# Run from experiments/new/box217:  bash check_key1p.sh
set -uo pipefail
T=../box212/inst
python3 key1p.py $T/DBL4_d20_F30.json $T/H5_d20_F62.json $T/H6_d24_F126.json $T/HIT7_d28_F254.json $T/RECF4_d20_F60.json
python3 key1p.py --n5 $T/DBL4_d20_F30.json $T/RECF4_d20_F60.json | sed 's/^/n5 /'
python3 key1p.py --rand 2154 300
python3 key1p.py --randlad 7701 2000
python3 key1p.py --n5 --randlad 7702 200 | sed 's/^/n5 /'
python3 key1p.py out/rec/rec_w2_d32_D2_s2001_enum.json out/rec/rec_w2_d28_D2_s2002_enum.json out/rec/rec_w2_d30_D2_s2003_enum.json
python3 key1p.py --lift 10 $T/H5_d20_F62.json
for c in perm howard down a2half a3all a4any w0; do
  KEY1P_CTRL=$c python3 key1p.py $T/HIT7_d28_F254.json $T/DBL4_d20_F30.json | sed "s/^/ctrl$c /"
done
KEY1P_CTRL=perm python3 key1p.py --n5 $T/DBL4_d20_F30.json | sed 's/^/ctrlpermn5 /'
KEY1P_CTRL=perm python3 key1p.py --n5 --randlad 7702 200 | sed 's/^/ctrlpermn5 /'
KEY1P_CTRL=fbearly python3 key1p.py --n5 $T/DBL4_d20_F30.json | sed 's/^/ctrlfbearly /'
