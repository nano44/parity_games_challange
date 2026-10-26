#!/usr/bin/env bash
# HON-FF climb queues (budget per climb as given). Usage: honclimbs.sh A|B; outputs results/honclimb/<tag>.{pg,start,log}
cd "$(dirname "$0")"
R=../..
q() { tag=$1; shift; python3 honclimb.py "$@" --out results/honclimb/$tag > results/honclimb/$tag.log 2>&1; }
case $1 in
A) q ff_n16 16 3 21 --secs 1200; q ff_seed_j10 24 1 22 --secs 1200 --seed-pg $R/experiments/red/xing/instances/j10_n24.pg;
   q ff_seed_j8 32 1 23 --secs 1200 --seed-pg $R/experiments/red/xing/instances/j8_n32.pg ;;
B) q ff_n24 24 3 24 --secs 1200; q ff_seed_j7 32 1 25 --secs 1200 --seed-pg $R/experiments/red/xing/instances/j7_n32.pg;
   q ff_n32 32 4 26 --secs 1200 ;;
esac
