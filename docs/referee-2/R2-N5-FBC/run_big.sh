#!/bin/bash
# REFEREE-2 successor 17: the named instances that were UNK at budget 3e6, at 3e7 (FBC). Logs in logs/big_*.txt.
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=30000000
for f in red/xing/instances/j7_n32 red/xing/instances/j8_n32 red/so/instances/rise_thin51_n40 si/xing/instances/zcl_rx_n32 si/orlens/instances/lev_l_x; do
  python3 fbc_check.py start $X/$f.pg > logs/big_$(basename $f).txt 2>&1; done
python3 fbc_check.py start $X/n5-epoch/instances/ffin12_n32.pg $X/n5-epoch/instances/ffin12_n32.start > logs/big_ffin12_n32.txt 2>&1
