#!/usr/bin/env bash
# Box 12 (c) climb queues (budget per climb in seconds as given). Usage: climbs.sh QUEUE (1..4); outputs results/climb/<tag>.{pg,start,log}
cd "$(dirname "$0")"
R=../..
q() { tag=$1; shift; python3 climb.py "$@" --out results/climb/$tag > results/climb/$tag.log 2>&1; }
case $1 in
1) q nep_n8  nep 8 2 1 --secs 600;  q nep_n12 nep 12 3 2 --secs 600; q nep_n16 nep 16 3 3 --secs 600; q nep_n24 nep 24 3 4 --secs 600 ;;
2) q nep_n32 nep 32 3 5 --secs 900; q nep_seed_levlx nep 32 1 6 --secs 1200 --seed-pg $R/experiments/si/orlens/instances/lev_l_x.pg;
   q nep_seed_rise51 nep 40 1 7 --secs 1200 --seed-pg $R/experiments/red/so/instances/rise_thin51_n40.pg ;;
3) q lend2_n8 lend2 8 3 11 --secs 600; q lend2_n12 lend2 12 3 12 --secs 600; q lend2_n16 lend2 16 3 13 --secs 600; q lend2_n24 lend2 24 3 14 --secs 600 ;;
4) q lend2_n32 lend2 32 3 15 --secs 900; q lend2_n48 lend2 48 4 16 --secs 900;
   q lend2_seed_pk32 lend2 32 2 17 --secs 1200 --seed-pg $R/experiments/red/n5inj/instances/phase2_pk32.pg;
   q lend2_seed_fb17 lend2 32 2 18 --secs 1200 --seed-pg $R/experiments/new/box44/instances/fb17_n32.pg ;;
esac
