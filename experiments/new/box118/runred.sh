#!/bin/bash
# L-NEW box 118: gate.py on L-RED's builds (valid / repaired starts as in box 116b / 117) and switchbestexp_2..6.
cd "$(dirname "$0")"
I=../box116/inst
for a in "$I/fbA_K4_m8_m8.pg $I/fbA_K4_m8_m8_fixed.start" "$I/fbA_K8_m8_m8.pg $I/fbA_K8_m8_m8_fixed.start" \
 "$I/fbg_K4_m6_m24.pg $I/fbg_K4_m6_m24_fixed.start" "$I/fbg_K4_m6_m48.pg $I/fbg_K4_m6_m48_fixed.start" \
 "$I/fbg_K8_m6_m24.pg $I/fbg_K8_m6_m24_fixed.start" "$I/fbg_K12_m6_m24.pg $I/fbg_K12_m6_m24_fixed.start" \
 "../../red/seg/instances/s3quad_K8_m30.pg $I/s3quad_K8_m30_default.start" "../box52/out/topfix_n10.pg $I/topfix_n10_default.start" \
 "../box113/inst/cp_K4.pg ../box113/inst/cp_K4.start" "../box113/inst/suf_K4.pg ../box113/inst/suf_K4.start" \
 "../box113/inst/suf_K8.pg ../box113/inst/suf_K8.start" "../box117/inst/fb3_K4_m6_m12_m12.pg ../box117/inst/fb3_K4_m6_m12_m12.start" \
 "../box115/inst/switchbestexp_2.pg -" "../box115/inst/switchbestexp_3.pg -" "../box115/inst/switchbestexp_4.pg -" \
 "../box115/inst/switchbestexp_5.pg -" "../box115/inst/switchbestexp_6.pg -"; do
  set -- $a; echo "GAME $1 $2 $(timeout 3000 python3 -I gate.py $1 $2 2>&1 | tail -1)"
done
