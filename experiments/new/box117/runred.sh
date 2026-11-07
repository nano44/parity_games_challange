#!/bin/bash
# L-NEW box 117: squeeze.py on L-RED's builds (valid / repaired starts as in box 116b) and the switchbestexp family, N5 and ARSB.
cd "$(dirname "$0")"
I=../box116/inst
for a in "$I/fbA_K4_m8_m8.pg $I/fbA_K4_m8_m8_fixed.start" "$I/fbA_K8_m8_m8.pg $I/fbA_K8_m8_m8_fixed.start" \
 "$I/fbg_K4_m6_m24.pg $I/fbg_K4_m6_m24_fixed.start" "$I/fbg_K4_m6_m48.pg $I/fbg_K4_m6_m48_fixed.start" \
 "$I/fbg_K8_m6_m24.pg $I/fbg_K8_m6_m24_fixed.start" "$I/fbg_K12_m6_m24.pg $I/fbg_K12_m6_m24_fixed.start" \
 "../../red/seg/instances/s3quad_K8_m30.pg $I/s3quad_K8_m30_default.start" "../box52/out/topfix_n10.pg $I/topfix_n10_default.start" \
 "../box113/inst/cp_K4.pg ../box113/inst/cp_K4.start" "../box113/inst/suf_K4.pg ../box113/inst/suf_K4.start" \
 "../box113/inst/suf_K8.pg ../box113/inst/suf_K8.start" "inst/fb3_K4_m6_m12_m12.pg inst/fb3_K4_m6_m12_m12.start"; do
  set -- $a; for V in N5 ARSB; do echo "GAME $1 $2 $(timeout 3000 python3 -I squeeze.py $1 $V $2 2>&1 | tail -1)"; done &
done; wait
