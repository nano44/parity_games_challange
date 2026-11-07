#!/bin/bash
# L-COMP box 30: (re)launch the three climb lanes (idempotent: a lane whose pid file names a live process is left alone).
cd "$(dirname "$0")"; [ -x bin/rclimb30 ] || { mkdir -p bin; gcc -O2 -o bin/rclimb30 rclimb30.c -lm; }; export RCLIMB=$PWD/bin/rclimb30
up() { n=$1; shift; f=out/.pid_$n; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "$n running"; return; }
       setsid nohup env $ENVX ./lane30.sh "$@" < /dev/null > /dev/null 2>&1 & echo $! > $f; echo "$n launched $!"; }
# STOPPED 09:3xZ (Lead 09:32Z): up A_d28 A_d28 out/seed_d28.txt 300000 6 5 6      # 7th capped level F(6) = 254 at d 28 (H6 + 4 TOP-ADD)
# STOPPED 11:4xZ (Lead 11:42Z; resume point in out/B_d32.log): up B_d32 B_d32 out/seed_d32.txt 310000 6 5 6      # 7th capped level at d 32 (H6 + 8 TOP-ADD; 192-bit values)
# 10:3xZ (Lead 10:23Z): D_d32 re-scored: GUARD 5 + SLACKH 7 (level-5 violations of L-LOWER 5 slack.py, ported) then F(6); seeds 340000+
# REPLACED 11:0xZ (Lead 11:02Z: lane D from L-LOWER SL41, score F(6), core-fixed mutations): ENVX="SLACKH=7" up D_d32 D_d32 out/seed_D_d32.txt 340000 6 5 6
# 07:4xZ: top-truncated seed collapsed (F 2 0 0 ...; log out/C_d23_toptrunc.log); restarted from H6 minus level 21 (remlevel.py)
# STOPPED 10:2xZ at park (Lead 09:32Z / 10:27Z): up C_d23 C_d23 out/seed_d23_rm21.txt 320100 5 5 5      # six capped levels at d 23
# 11:1xZ (Lead 11:02Z): lane D_d28 = L-LOWER 5 rec/SL41_d28.txt (eeb25f6e, sha1 c1b46c31; 0 level-1..5 slack violations, F(6) 222, T 290);
# GUARD 5, score F(6) (LV 6), mutations only on movers >= 12 (FROZENBELOW=12: pairs 0-5 untouched); seeds 350000+. d 32 variant
# (out/seed_SL41_d32.txt, 4 TOP-ADD) NOT run: no free core (B_d32, D_d28, query 2, xval_d3 on 4 cores).
# 11:4xZ (Lead 11:38Z, L-LOWER aac4ebcc: SL41 plateau >= 2 edits deep): from unit 1 every proposal = NMIN..NMAX = 2-3 simultaneous edits
# (rclimb30 env NMIN/NMAX; defaults 1-3 = original, regression byte-identical); equal-score moves were already accepted (sc >= cur) + ANNEAL.
ENVX="FROZENBELOW=12 NMIN=2 NMAX=3" up D_d28 D_d28 out/seed_SL41_d28.txt 350000 6 5 6
# 11:4xZ (Lead 11:42Z): biased D lane on B's core: SL41, GUARD 5, LV 6, FROZENBELOW 12, NMIN 2 / NMAX 3, FUEL BIAS (rclimb30 env BIAS*):
# BIASP 0.5 of proposals carry one fuel edit on a mover of the Xi-closure (both options) of 22 and of 9:1's target 54 in SL41, movers >= 12
# (static set from the seed); 1/4 of fuel edits on mover 19 (L-LOWER's candidate supplier, option 1 rank 95); rank swap above BIASR 87 /
# parity flip / re-target to an owner of a rank > 87 option. Seeds 360000+.
# 12:3xZ (Lead 12:36Z: L-LOWER c7c1419d retall2.py, 144,011 two-edit genomes with mover 19: none > 222): from unit 3 NMAX 4, BIAS19P 0.1
ENVX="FROZENBELOW=12 NMIN=2 NMAX=4 BIAS19P=0.1 BIAS=14,15,16,19,20,21,22,24,25,26,29,30,32,34,35,36,39,40,41,43,47,49,50,52,54 BIAS19=19 BIASR=87 BIASP=0.5" up D_d28b D_d28b out/seed_SL41_d28.txt 360000 6 5 6
