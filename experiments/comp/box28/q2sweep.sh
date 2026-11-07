#!/bin/bash
# L-COMP 11: final sweep of query 2. Waits until all three shard workers (cubes/.pid_q2, .pid_q2b, .pid_q2c) have exited, then runs
# q2shard.sh with SHARD 0 of NSHARD 1 = every piece in the enumeration order, skipping those with a «s VERIFIED» .chk. Needed because
# q2stop2.sh (17:40:43Z) deleted log/q2/*.chk.tmp of ALL workers, so the drup results of c0s1p2 and c0s1p4 (shards 0/1 running) were lost
# (Glucose UNSAT recorded, no .chk, proofs deleted): they are NOT certified until this sweep re-runs them. Runs alone, so no piece twice.
cd "$(dirname "$0")"
for f in cubes/.pid_q2 cubes/.pid_q2b cubes/.pid_q2c; do while [ -f $f ] && kill -0 $(cat $f) 2>/dev/null; do sleep 30; done; done
PDIR=/home/user/pf/q2 SHARD=0 NSHARD=1 exec ./q2shard.sh
