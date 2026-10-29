#!/bin/bash
# REFEREE-2 successor 21: P-N5-FRAME runs as actually made (from docs/referee-2/R2-N5-FRAME). Logs in logs/. 4 CPUs.
# Pinned: experiments/new/check.sh run whole in a detached worktree at l-new 938d8796 -> logs/pinned_check.txt.
cd "$(dirname "$0")"; T=${TMPDIR:-/tmp}
python3 fquote.py > logs/quotes.txt 2>&1; SHIFT=1 python3 fquote.py > logs/quotes_shift1.txt 2>&1
BF=8 python3 frame_check.py random 1500 3 8 21 3 > logs/rand_bf_3_8.txt 2>&1
python3 frame_check.py random 300 6 14 3 2 > logs/rand_6_14_s3.txt 2>&1
python3 frame_check.py random 2000 6 14 22 3 > logs/rand_6_14.txt 2>&1
python3 frame_check.py random 300 15 30 23 2 > logs/rand_15_30.txt 2>&1
BF=7 python3 frame_check.py alltau 1500 3 7 32 > logs/alltau_3_7.txt 2>&1
python3 frame_check.py alltau 150 8 11 33 > logs/alltau_8_11.txt 2>&1
python3 frame_check.py files dual.lst 2 experiments/ > logs/dual.txt 2>&1
grep -v mk_16_100 mkr.lst > $T/mkr_small.lst; grep mk_16_100 mkr.lst > $T/mkr_big.lst
DUMP=1 PROGRESS=1 python3 frame_check.py files $T/mkr_small.lst 2 experiments/ > logs/mkr_small.txt 2>&1
OFNODE=2000 GPMAX=20 DORDMAX=1000 DUMP=1 PROGRESS=1 python3 frame_check.py files $T/mkr_big.lst 1 experiments/ > logs/mkr_big.txt 2>&1
echo new/box59/out/dw_3.pg > $T/dw3.lst; DUMP=1 python3 frame_check.py files $T/dw3.lst 1 experiments/ > logs/dw3_dump.txt 2>&1
# sbcg: games with n <= 100 at default caps, n > 100 with OFNODE=3000 GPMAX=20 DORDMAX=2000 (the as-run split is described in the report §4.2)
: > $T/sb_small; : > $T/sb_big
while read g r; do n=$(head -1 ../../../experiments/$g | tr -d ';' | awk '{print $2}'); if [ $n -le 100 ]; then echo $g >> $T/sb_small; else echo $g >> $T/sb_big; fi; done < ../../../experiments/new/box59/sbcg.lst
PROGRESS=1 python3 frame_check.py files $T/sb_small 1 experiments/ > logs/sbcg_small_all.txt 2>&1
OFNODE=3000 GPMAX=20 DORDMAX=2000 PROGRESS=1 python3 frame_check.py files $T/sb_big 1 experiments/ > logs/sbcg_big_all.txt 2>&1
