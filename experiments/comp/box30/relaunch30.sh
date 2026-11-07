#!/bin/bash
# L-COMP box 30: (re)launch the three climb lanes (idempotent: a lane whose pid file names a live process is left alone).
cd "$(dirname "$0")"; [ -x bin/rclimb30 ] || { mkdir -p bin; gcc -O2 -o bin/rclimb30 rclimb30.c -lm; }; export RCLIMB=$PWD/bin/rclimb30
up() { n=$1; shift; f=out/.pid_$n; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "$n running"; return; }
       setsid nohup env $ENVX ./lane30.sh "$@" < /dev/null > /dev/null 2>&1 & echo $! > $f; echo "$n launched $!"; }
# STOPPED 09:3xZ (Lead 09:32Z): up A_d28 A_d28 out/seed_d28.txt 300000 6 5 6      # 7th capped level F(6) = 254 at d 28 (H6 + 4 TOP-ADD)
up B_d32 B_d32 out/seed_d32.txt 310000 6 5 6      # 7th capped level at d 32 (H6 + 8 TOP-ADD; 192-bit values)
# 10:3xZ (Lead 10:23Z): D_d32 re-scored: GUARD 5 + SLACKH 7 (level-5 violations of L-LOWER 5 slack.py, ported) then F(6); seeds 340000+
ENVX="SLACKH=7" up D_d32 D_d32 out/seed_D_d32.txt 340000 6 5 6
# 07:4xZ: top-truncated seed collapsed (F 2 0 0 ...; log out/C_d23_toptrunc.log); restarted from H6 minus level 21 (remlevel.py)
up C_d23 C_d23 out/seed_d23_rm21.txt 320100 5 5 5      # six capped levels at d 23
