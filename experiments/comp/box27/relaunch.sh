#!/bin/bash
# L-COMP box 27: idempotent relaunch of every open acube.py search (run after a container restart). Finished/split cubes are kept.
cd "$(dirname "$0")"
run() { D=$1; L=$2; tag=$3; shift 3; pgrep -f "acube.py $tag " >/dev/null && { echo "$tag already running"; return; }
        env "$@" setsid nohup python3 acube.py $tag $D $L >> log/acube_$tag.out 2>&1 < /dev/null & echo "$tag launched"; }
# priority (Lead 14:13Z): T_1(3) first; low-priority lines below are commented while it runs
run 4 11 T1_m3_L11 TLIM=3600 PAR=2 FREE0=1 KF=1   # NEW #2 (Lead 04:09Z): own-encoding T_1(3) <= 10
# run 4 10 T1_m3_L10 TLIM=1200 PAR=1 FREE0=1 KF=1
# STOPPED Lead 04:09Z: run 4 13 R_d4_L13 TLIM=1200 PAR=1
# STOPPED Lead 04:09Z: run 4 14 R_d4_L14 TLIM=1200 PAR=1
# STOPPED Lead 04:09Z: run 4 18 INF_m3_L18 TLIM=1200 PAR=1 FREE0=1 KF=99
# run 3 9 F_d3_L9  TLIM=1200 PAR=1 W=free
# run 2 5 P22_d2_L5 TLIM=1200 PAR=1 W=free P=2,2
