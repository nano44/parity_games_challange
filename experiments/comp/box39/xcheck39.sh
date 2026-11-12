#!/bin/bash
# box 39 item 1 cross-check run (scope all; then movers on the records). Resumable: rerun regenerates the outputs.
cd "$(dirname "$0")"
I=inst
python3 depth39.py $I/MWR4_2.json $I/MWR8_2.json $I/MWR16_2.json $I/K1F21_n48.json $I/K1F34_n84.json $I/K1C16_n400.json $I/B400_r32_a13d9661.json \
  $I/K1D4_n48.json $I/K1L7_n48.json $I/K1L10_n48.json $I/BLKX23_n48.json $I/BLKX26_n48.json $I/CLA25_n64.json \
  $I/CWRR4_n.json $I/CWRR8_n.json $I/CWRR16_n.json $I/CWRQ4_n.json $I/CWRQ8_n.json $I/CWRQ16_n.json \
  $I/ring3A_k8_m12.json $I/ring3B_k8_m12.json $I/ring3C_k8_m12.json $I/ring3D_k8_m12.json \
  $I/CW4_n.json $I/CW8_n.json $I/CW16_n.json $I/CW32_own.json > out/xcheck39_all.out 2>&1
echo "all exit $?"
DEP_CTRL=1 python3 depth39.py $I/MWR4_2.json $I/K1L7_n48.json > out/xcheck39_ctrl.out 2>&1
echo "ctrl exit $?"
