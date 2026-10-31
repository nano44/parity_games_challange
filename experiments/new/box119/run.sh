#!/bin/bash
# L-NEW box 119: unblock.py on L-RED's builds + switchbestexp_2..6 (red.txt) and the box 53 corpus (u_sbcg.txt, u_alt.txt).
cd "$(dirname "$0")"
I=../box116/inst
for a in "$I/fbA_K4_m8_m8.pg $I/fbA_K4_m8_m8_fixed.start" "$I/fbA_K8_m8_m8.pg $I/fbA_K8_m8_m8_fixed.start" \
 "$I/fbg_K4_m6_m24.pg $I/fbg_K4_m6_m24_fixed.start" "$I/fbg_K4_m6_m48.pg $I/fbg_K4_m6_m48_fixed.start" \
 "$I/fbg_K8_m6_m24.pg $I/fbg_K8_m6_m24_fixed.start" "$I/fbg_K12_m6_m24.pg $I/fbg_K12_m6_m24_fixed.start" \
 "../../red/seg/instances/s3quad_K8_m30.pg $I/s3quad_K8_m30_default.start" "../box113/inst/cp_K4.pg ../box113/inst/cp_K4.start" \
 "../box113/inst/suf_K8.pg ../box113/inst/suf_K8.start" "../box117/inst/fb3_K4_m6_m12_m12.pg ../box117/inst/fb3_K4_m6_m12_m12.start" \
 "../box115/inst/switchbestexp_4.pg -" "../box115/inst/switchbestexp_6.pg -"; do
  set -- $a; echo "GAME $1 $2 $(timeout 3000 python3 -I unblock.py $1 $2 2>&1 | tail -1)" &
done > red.txt; wait
cd ../..
one() { a="$1"; b="$2"; case "$a" in *comp54_n80.pg) [ -n "$b" ] && b=new/box113/inst/comp54_n80_fixed.start;; *n3cov_lean.pg) [ -n "$b" ] && b=new/box113/inst/n3cov_lean_fixed.start;; esac; echo "GAME $a $b $(timeout 900 python3 -I new/box119/unblock.py $a ${b:--} 2>&1 | tail -1)"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box119/u_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box119/u_alt.txt
