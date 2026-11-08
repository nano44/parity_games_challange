#!/bin/bash
# L-COMP 12 box 31: (re)start the LJ = 7 climb lanes + freezer31 (idempotent: a lane whose PID file names a live process is skipped).
# Kill only by PID file (out/.pid_<lane>). Lane state: out/<lane>.unit (local, excluded), resume point = last unit in out/<lane>.log + 1.
cd "$(dirname "$0")"; [ -x bin/rclimb31 ] || { mkdir -p bin; gcc -O2 -o bin/rclimb31 rclimb31.c -lm; }; export RCLIMB=$PWD/bin/rclimb31
upa() { n=$1; shift; f=out/.pid_$n; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "$n running"; return; }
  env $ENVX setsid nohup ./lane31.sh "$@" > out/$n.nohup 2>&1 < /dev/null & echo $! > $f; echo "$n started pid $(cat $f)"; }
upf() { f=out/.pid_freezer31; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "freezer31 running"; return; }
  setsid nohup ./freezer31.sh > out/freezer31.nohup 2>&1 < /dev/null & echo $! > $f; echo "freezer31 started pid $(cat $f)"; }
C="LANEANNEAL=0.15 LJ=7 LJGATE=190 LJGUARD=20:17,34:22 FIX=20,34 NMIN=2 NMAX=4"
# LAUNCHED 02:2xZ 2026-11-08 (Lead 02:20Z: settings + path approved; phase 2 path only if npaths stalls > 0, on notice):
ENVX="$C FROZENBELOW=0"  upa L7a L7a out/seed_HIT7_d32.txt 500000 6 5 7
ENVX="$C FROZENBELOW=0"  upa L7b L7b out/seed_HIT7_d32.txt 510000 6 5 7
# Lead 02:53Z + 03:43Z (LJNPMAX: role-free npaths, ref-checked 112 genomes): from the next (re)start L7c = FROZENBELOW 8 + LJSLACK 8, L7d = FROZENBELOW 12 + LJSLACK 8 (slack j 4,5 at H 8); L7a/L7b baseline
# ENDED 04:57Z (Lead 04:57Z: L7c -> L7cr, ROOM order; L7c best frozen as out/L7_FRZ_PREROOM_L7c.txt sha1 75514342): ENVX="$C FROZENBELOW=8 LJSLACK=8 LJNPMAX=1" upa L7c L7c out/seed_HIT7_d32.txt 520000 6 5 7
ENVX="$C FROZENBELOW=8 LJSLACK=8 LJNPMAX=1 LJORDER=room" upa L7cr L7cr out/L7_FRZ_PREROOM_L7c.txt 540000 6 5 7
ENVX="$C FROZENBELOW=12 LJSLACK=8 LJNPMAX=1" upa L7d L7d out/seed_HIT7_d32.txt 530000 6 5 7
upf
