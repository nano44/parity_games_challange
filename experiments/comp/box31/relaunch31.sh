#!/bin/bash
# L-COMP 12 box 31: (re)start the LJ = 7 climb lanes + freezer31 (idempotent: a lane whose PID file names a live process is skipped).
# Kill only by PID file (out/.pid_<lane>). Lane state: out/<lane>.unit (local, excluded), resume point = last unit in out/<lane>.log + 1.
cd "$(dirname "$0")"; [ -x bin/rclimb31 ] || { mkdir -p bin; gcc -O2 -o bin/rclimb31 rclimb31.c -lm; }; export RCLIMB=$PWD/bin/rclimb31
upa() { n=$1; shift; f=out/.pid_$n; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "$n running"; return; }
  env $ENVX setsid nohup ./lane31.sh "$@" > out/$n.nohup 2>&1 < /dev/null & echo $! > $f; echo "$n started pid $(cat $f)"; }
upf() { f=out/.pid_freezer31; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "freezer31 running"; return; }
  setsid nohup ./freezer31.sh > out/freezer31.nohup 2>&1 < /dev/null & echo $! > $f; echo "freezer31 started pid $(cat $f)"; }
C="LANEANNEAL=0.15 LJ=7 LJGATE=190 LJGUARD=20:17,34:22 FIX=20,34 NMIN=2 NMAX=4"
# NOT YET LAUNCHED (waiting for the Lead's OK on settings + path, L-COMP 12 02:2xZ):
#ENVX="$C FROZENBELOW=0"  upa L7a L7a out/seed_HIT7_d32.txt 500000 6 5 7
#ENVX="$C FROZENBELOW=0"  upa L7b L7b out/seed_HIT7_d32.txt 510000 6 5 7
#ENVX="$C FROZENBELOW=12" upa L7c L7c out/seed_HIT7_d32.txt 520000 6 5 7
#ENVX="$C FROZENBELOW=12" upa L7d L7d out/seed_HIT7_d32.txt 530000 6 5 7
#upf
