#!/bin/bash
# L-COMP box 28: relaunch everything after a container restart (idempotent; per-cube state survives on disk).
cd "$(dirname "$0")"
[ -x frup ] || gcc -O2 -o frup frup.c; [ -x ../box27/drup ] || (cd ../box27 && gcc -O2 -o drup drup.c)
up() { name=$1; shift; f=cubes/.pid_$name; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "$name running"; return; }
       "$@" & echo $! > $f; echo "$name launched $!"; }
mkdir -p cubes
up diskguard setsid nohup ./diskguard.sh < /dev/null > /dev/null 2>&1
# STOPPED 07:0xZ (Lead 05:32Z rule): up ISO_L13 setsid nohup env ENC=cnf2 ISO=1 TLIM=1500 PAR=3 ROOTS=40,0,42,2,8,10,32,34 python3 acube28.py ISO_L13 4 13 >> log/acube_ISO_L13.out 2>&1 < /dev/null
# PAUSED Lead 05:32Z: up R4_L14 setsid nohup env ENC=cnf2 TLIM=1500 PAR=1 ROOTS=40,0,42,2,8,10,32,34 python3 acube28.py R4_L14 4 14 >> log/acube_R4_L14.out 2>&1 < /dev/null
# DONE 16/16 (log/xval_d3.txt): up xval env PDIR=/home/user/pf/x setsid nohup nice -n 15 ./xval_d3.sh 4 7 8 11 12 < /dev/null > log/xval_d3.run 2>&1
# REPLACED 14:3xZ (Lead 14:29Z: two query-2 workers, q2shard.sh = q2pieces.sh + fixed piece index i, worker k takes i % 2 == k):
# up q2 env PDIR=/home/user/pf/q2 setsid nohup ./q2pieces.sh < /dev/null > log/q2pieces.run 2>&1
# 17:xxZ: xval_d3 finished (16/16) -> its core to query 2: THREE shards (i % 3), switched at a piece boundary (after c0s1p0) by q2reshard3.sh
# 20:5xZ: shards 0/3, 1/3 finished; one worker re-runs both lists (q2redo01.sh)
# up q2 env PDIR=/home/user/pf/q2 SHARD=0 NSHARD=3 setsid nohup ./q2shard.sh < /dev/null > log/q2shard0.run 2>&1
# up q2b env PDIR=/home/user/pf/q2 SHARD=1 NSHARD=3 setsid nohup ./q2shard.sh < /dev/null > log/q2shard1.run 2>&1
# DONE: up q2 setsid nohup ./q2redo01.sh < /dev/null > log/q2redo01.run 2>&1
# 17:3xZ (Lead 17:31Z: two query-2 cores): shard 2/3 DEFERRED, runs after shard 0/3 exits (q2chain2.sh); same index, nothing twice
# up q2c env PDIR=/home/user/pf/q2 SHARD=2 NSHARD=3 setsid nohup ./q2shard.sh < /dev/null > log/q2shard2.run 2>&1
# DONE: up q2c setsid nohup ./q2chain2.sh < /dev/null > log/q2shard2.run 2>&1
# 19:2xZ: final sweep (re-runs every non-VERIFIED piece, incl. c0s1p2/c0s1p4 lost by q2stop2.sh) after all three shards exit
# DONE 23:33Z (query 2 complete, log/lsi_q2_cert.txt): up q2s setsid nohup ./q2sweep.sh < /dev/null > log/q2sweep.run 2>&1
up commit setsid nohup ./commit_loop.sh < /dev/null > /dev/null 2>&1
../box30/relaunch30.sh   # BOX 30 climb lanes (Lead 07:12Z; all STOPPED at L-COMP 11's park)
../box31/relaunch31.sh   # BOX 31 level-7 climb lanes L7a-d + freezer31 (L-COMP 12, Lead 02:20Z)
