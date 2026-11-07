#!/bin/bash
# L-COMP 11 (Lead 17:31Z: query 2 back to two cores for the D_l6z lane): shard 2 of 3 is DEFERRED, not re-indexed. This script waits until
# shard 0 of 3 (pid file cubes/.pid_q2) has exited, then runs shard 2 of 3 (same fixed index i, i % 3 == 2), so every piece keeps exactly
# one owner and none is done twice, across restarts too (relaunch_all.sh starts shards 0, 1 and this chain).
cd "$(dirname "$0")"
while kill -0 $(cat cubes/.pid_q2) 2>/dev/null; do sleep 30; done
PDIR=/home/user/pf/q2 SHARD=2 NSHARD=3 exec ./q2shard.sh
