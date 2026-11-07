#!/bin/bash
# L-COMP 11 (20:5xZ): shards 0/3 and 1/3 have finished; re-run their lists once (skips VERIFIED), which redoes c0s1p2 and c0s1p4 (drup
# results lost by q2stop2.sh 17:40Z). Disjoint from the running shard 2/3 (i % 3 == 2), so no piece twice. Uses pid file cubes/.pid_q2,
# so q2sweep.sh still waits for it.
cd "$(dirname "$0")"
PDIR=/home/user/pf/q2 SHARD=0 NSHARD=3 ./q2shard.sh
PDIR=/home/user/pf/q2 SHARD=1 NSHARD=3 ./q2shard.sh
