#!/bin/bash
# L-COMP box 28: relaunch everything after a container restart (idempotent; per-cube state survives on disk).
cd "$(dirname "$0")"
[ -x frup ] || gcc -O2 -o frup frup.c; [ -x ../box27/drup ] || (cd ../box27 && gcc -O2 -o drup drup.c)
up() { name=$1; shift; f=cubes/.pid_$name; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "$name running"; return; }
       "$@" & echo $! > $f; echo "$name launched $!"; }
mkdir -p cubes
up diskguard setsid nohup ./diskguard.sh < /dev/null > /dev/null 2>&1
up ISO_L13 setsid nohup env ENC=cnf2 ISO=1 TLIM=1500 PAR=3 ROOTS=40,0,42,2,8,10,32,34 python3 acube28.py ISO_L13 4 13 >> log/acube_ISO_L13.out 2>&1 < /dev/null
# PAUSED Lead 05:32Z: up R4_L14 setsid nohup env ENC=cnf2 TLIM=1500 PAR=1 ROOTS=40,0,42,2,8,10,32,34 python3 acube28.py R4_L14 4 14 >> log/acube_R4_L14.out 2>&1 < /dev/null
up xval env PDIR=/home/user/pf/x setsid nohup nice -n 15 ./xval_d3.sh < /dev/null > log/xval_d3.run 2>&1
up q2 env PDIR=/home/user/pf/q2 setsid nohup ./q2pieces.sh < /dev/null > log/q2pieces.run 2>&1
up commit setsid nohup ./commit_loop.sh < /dev/null > /dev/null 2>&1
