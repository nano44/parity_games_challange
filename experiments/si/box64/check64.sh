#!/usr/bin/env bash
# L-SI box 64 self-check (~30 s): flipdp.py on the L-NEW witnesses (XSIM / PATH / MONO_K / CAP all 0, pinned T_k and T_inf),
# bitchain.py (Lemma BIT-CHAIN, BITC 0) on the witnesses and 100 random ISO ladders per m = 1..3.
set -euo pipefail
cd "$(dirname "$0")"
out=$(K=8 python3 -I flipdp.py wit/*.json)
echo "$out" | grep -q "TOTAL bad 0"
echo "$out" | grep -q "^ISO_1_d4_t12.json m 3 T_0..T_8 \[5, 8, 12, 13, 13, 13, 13, 13, 13\] T_inf 13 LP 18"
echo "$out" | grep -q "^kf1_d4_t10.json m 3 T_0..T_8 \[5, 10, 10, 10, 10, 10, 10, 10, 10\] T_inf 10 LP 16"
echo "$out" | grep -q "^kf8_d3_t9.json m 2 T_0..T_8 \[2, 3, 4, 5, 6, 7, 8, 8, 9\] T_inf 9 LP 10"
o2=$(K=8 python3 -I flipdp.py out/inf_m3_s1.json out/inf_m4_s2.json)
echo "$o2" | grep -q "^inf_m3_s1.json m 3 T_0..T_8 \[4, 6, 8, 10, 12, 13, 15, 16, 17\] T_inf 17 LP 23 bad 0 XSIM 0"
echo "$o2" | grep -q "^inf_m4_s2.json m 4 .* T_inf 21 LP 29 bad 0 XSIM 0"
echo "flipdp witnesses + T_inf champions: PASS"
b=$(python3 -I bitchain.py wit/*.json)
echo "$b" | grep -q "TOTAL BITC 0"
echo "$b" | grep -q "^kf1_d4_t10.json {'BITC': 0, 'T0': 5, 'maxR': 5, 'segAtMaxR': 5"
for m in 1 2 3; do python3 -I bitchain.py --random $m 100 $m | grep -q "TOTAL BITC 0"; done
echo "box 64 bitchain: PASS"
# negative control: a wrong carry at level 2 must be caught
if BC_NEG=1 python3 -I bitchain.py --random 3 50 7 >/dev/null; then echo "BC_NEG not caught"; exit 1; fi
echo "box 64 negative control: PASS"
