#!/bin/bash
# REFEREE-2 successor 18: all OFFMONO-unit runs (from docs/referee-2/R2-N5-OFFMONO). Logs in logs/ (logs_v1/: first pass, before the
# CMP counters were added; same checks otherwise).
cd "$(dirname "$0")"
X=../../../experiments
{
python3 offmono_check.py start $X/red/rec0/instances/nep90_n40.pg $X/si/rund/instances/nep90_n40.start
python3 offmono_check.py start $X/n5-epoch/instances/nep76_n40.pg $X/n5-epoch/instances/nep76_n40.start
python3 offmono_check.py start $X/new/box48/instances/long121_n40.pg $X/new/box48/instances/long121_n40.start
python3 offmono_check.py start $X/red/n5inj/instances/frz40.pg $X/red/n5inj/instances/frz40.start
for f in $X/new/box48/out/qpcclimb/best_qpc_nep90_n40_s51 $X/new/box48/out/qpcclimb/best_qpc_nep76_n40_s52 $X/new/box48/out/qpcclimb/best_qpc_long121_n40_s53 \
         $X/new/box48/out/qpcclimb/scale/snap_n80_s62 $X/new/box48/out/qpcclimb/scale/best_qpc_nep76_n40_s63 $X/new/box48/out/qpcclimb/scale/best_qpc_nep90_n40_s61 \
         $X/new/box48/out/qpcclimb/scale/best_qpc_nep90_n40_s62 $X/new/box48/out/tieclimb/best_oddc_u3ev_n16_s1 $X/new/box48/out/tieclimb/best_oddc_u3ev_n16_s2 \
         $X/new/box48/out/tieclimb/best_tie_klcount_n16_s3 $X/new/box48/out/tieclimb/best_tie_klcount_n16_s4 $X/new/box48/instances/du/nep90x2 \
         $X/new/box48/instances/du/nep90x3 $X/new/box48/instances/du/nep90x4; do
  python3 offmono_check.py start $f.pg $f.start
done
} > logs/named.txt 2>&1 &
python3 offmono_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
{
python3 offmono_check.py files ../R2-N5-ROOT/lib2o_noref.lst 5 > logs/lib2o_x5.txt 2>&1
python3 offmono_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1
python3 offmono_check.py random 600 20 40 1805 5 2 > logs/rand_k5_n20-40.txt 2>&1
} &
{
python3 offmono_check.py random 3000 6 14 1801 2 3 > logs/rand_k2_n6-14.txt 2>&1
python3 offmono_check.py random 2000 8 18 1802 4 3 > logs/rand_k4_n8-18.txt 2>&1
python3 offmono_check.py random 1500 8 20 1803 0 3 > logs/rand_kO_n8-20.txt 2>&1
python3 offmono_check.py random 400 20 30 1804 3 2 > logs/rand_k3_n20-30.txt 2>&1
} &
wait
