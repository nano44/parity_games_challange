#!/usr/bin/env bash
# Time Oink's solvers on the ZP killer family T_R (instances/zp_tile8_R*.pg): is T_R hard for any known solver?
O=../../tools/oink/build/oink
for f in instances/zp_tile8_R1_n32.pg instances/zp_tile8_R2_n64.pg instances/zp_tile8_R3_n96.pg instances/zp_tile8_R4_n128.pg instances/zp_tile8_R5_n160.pg; do
  for s in zlk uzlk zlkq tl rtl ortl ptl dtl idtl spptl psi fpi pp dp rr tspm qpt; do
    t0=$(date +%s.%N); out=$(timeout 120 $O --$s -v "$f" 2>&1); rc=$?; t1=$(date +%s.%N)
    it=$(echo "$out" | grep -oE "solved with [0-9]+ [a-z]+|[0-9]+ (iterations|tangles|lifts|recursive calls)" | head -1)
    v=$(echo "$out" | grep -c "solution verified")
    printf "%s %-6s rc=%d verified=%s %5.1fs %s\n" "$(basename $f)" "$s" $rc "$v" "$(echo "$t1 - $t0" | bc)" "$it"
  done
done
