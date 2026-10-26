#!/bin/bash
# REFEREE-2 successor 16: all RUND runs (from docs/referee-2/R2-N5-RUND). Logs in logs/.
cd "$(dirname "$0")"
X=../../../experiments; H=../R2-N5-H3/instances
{
for f in frz1_n24 frz2_n24 frz3_n24; do python3 rund_check.py start $X/n5-exhaustive/instances/$f.pg $X/n5-exhaustive/instances/$f.start; done
python3 rund_check.py start $X/red/so/instances/pftheta34_n32.pg $H/pftheta34_n32_S3.start
python3 rund_check.py start $H/pft34_h3u_P32.pg $H/pft34_h3u_P32_t33.start
for f in lcount_n23 lcount2_n23; do python3 rund_check.py start $X/red/h3/instances/$f.pg $X/red/h3/instances/$f.start; done
for f in offret_n23 incdown_n23 offalt_K10 off_s22_n24; do python3 rund_check.py start $X/si/rund/instances/$f.pg $X/si/rund/instances/$f.start; done
for f in lenonly_n8 off_s21_n24 off_s23_n24 off_s24_n40 tw_s1_n10; do python3 rund_check.py start $X/si/rund/instances/$f.pg; done
} > logs/packet_instances.txt 2>&1
# large sets (run in parallel by hand: ./run_all.sh big)
if [ "$1" = big ]; then
python3 rund_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
python3 rund_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1 &
python3 rund_check.py random 3000 5 9 1601 2 2 > logs/rand_k2_n5-9.txt 2>&1 &
python3 rund_check.py random 2000 8 16 1602 3 2 > logs/rand_k3_n8-16.txt 2>&1 &
python3 rund_check.py random 1000 12 24 1603 0 2 > logs/rand_kO_n12-24.txt 2>&1 &
wait
fi
if [ "$1" = extra ]; then
python3 rund_check.py random 2000 10 20 1604 4 3 > logs/rand_k4_n10-20.txt 2>&1 &
python3 climb.py $X/red/so/instances/pftheta34_n32.pg $H/pftheta34_n32_S3.start 1500 11 climb/c_pft > logs/climb_pft.txt 2>&1 &
python3 climb.py $X/n5-exhaustive/instances/frz3_n24.pg $X/n5-exhaustive/instances/frz3_n24.start 1500 12 climb/c_frz3 > logs/climb_frz3.txt 2>&1 &
wait
for c in c_pft c_frz3; do python3 rund_check.py start climb/$c.pg climb/$c.start > logs/climb_$c.check.txt 2>&1; done
for M in shift noforb crrel1 tg4 tgr fz piece unf chu0; do RD_MUT=$M python3 rund_check.py start $X/red/so/instances/pftheta34_n32.pg $H/pftheta34_n32_S3.start > logs/mut_$M.txt 2>&1; done
RD_MUT=crrel1 python3 rund_check.py start $X/n5-exhaustive/instances/frz3_n24.pg $X/n5-exhaustive/instances/frz3_n24.start > logs/mut_crrel1_frz3.txt 2>&1
python3 uf_once.py $X/red/so/instances/so_th_n32.pg - > logs/uf_once_so_th_n32.txt; UF_II=1 python3 uf_once.py $X/red/so/instances/so_th_n32.pg - >> logs/uf_once_so_th_n32.txt
UF_II=1 python3 uf_once.py $X/red/n5inj/instances/phase2_pk48.pg instances/phase2_pk48_s1.start > logs/uf_once_phase2_pk48_s1.txt
python3 uf_scan.py ../R2-N5-STAU/lib41_noref.lst 3 > logs/uf_scan_lib41.txt 2>&1 &
python3 uf_scan.py ../R2-N5-KW/files.lst 2 > logs/uf_scan_c1o.txt 2>&1 &
wait
fi
