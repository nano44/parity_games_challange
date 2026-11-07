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
# STOPPED 14:3xZ (Lead 14:29Z; resume point in out/D_d28.log): ENVX="FROZENBELOW=12 NMIN=2 NMAX=3" up D_d28 D_d28 out/seed_SL41_d28.txt 350000 6 5 6
# 11:4xZ (Lead 11:42Z): biased D lane on B's core: SL41, GUARD 5, LV 6, FROZENBELOW 12, NMIN 2 / NMAX 3, FUEL BIAS (rclimb30 env BIAS*):
# BIASP 0.5 of proposals carry one fuel edit on a mover of the Xi-closure (both options) of 22 and of 9:1's target 54 in SL41, movers >= 12
# (static set from the seed); 1/4 of fuel edits on mover 19 (L-LOWER's candidate supplier, option 1 rank 95); rank swap above BIASR 87 /
# parity flip / re-target to an owner of a rank > 87 option. Seeds 360000+.
# 12:3xZ (Lead 12:36Z: L-LOWER c7c1419d retall2.py, 144,011 two-edit genomes with mover 19: none > 222): from unit 3 NMAX 4, BIAS19P 0.1
# STOPPED 17:3xZ (Lead 17:27Z; resume point in out/D_d28b.log): ENVX="FROZENBELOW=12 NMIN=2 NMAX=4 BIAS19P=0.1 BIAS=14,15,16,19,20,21,22,24,25,26,29,30,32,34,35,36,39,40,41,43,47,49,50,52,54 BIAS19=19 BIASR=87 BIASP=0.5" up D_d28b D_d28b out/seed_SL41_d28.txt 360000 6 5 6
# 17:3xZ (Lead 17:27Z): D_l6 = L-LOWER 6 noreturn climb (tests CONJECTURE RC-PLATEAU). rclimb30 env L6SCORE: score = port of guard_l6.score
# (claude/l-lower bca48384, guard_l6.py sha1 18e85589, sim6.py sha1 6953306e): (min(caps,6), -npaths(q5, pair 6), F(6)) as
# caps*1e9 - npaths*1e4 + F(6); = guard_l6.score on SL41 + 40 random mutants. Edits: NMIN 2 / NMAX 4 outside pairs 0-5 (FROZENBELOW 12),
# plus with prob 1/4 a re-point of 10:0 (option 20, core) or 55:0 (option 110) (REPT); rank swaps are among the ordinary edits; equal-score
# moves accepted + ANNEAL. TESTOUT out/D_l6_TEST.txt = the FIRST genome with caps 6, q5 found, npaths 0 (never overwritten). Seeds 370000+.
# STOPPED 17:4xZ (Lead 17:42Z; best frozen out/L6_BEST_D_l6_d28.txt): ENVX="L6SCORE=1 FROZENBELOW=12 NMIN=2 NMAX=4 REPT=20,110 TESTOUT=out/D_l6_TEST.txt" up D_l6 D_l6 out/seed_SL41_d28.txt 370000 6 5 6
# 17:3xZ (Lead 17:31Z): D_l6z = the same L6 score and edits as D_l6, from SL41, ANNEAL 0 (only sc >= cur accepted: never gives up F(6));
# lane30a.sh (= lane30.sh with LANEANNEAL); first genome with caps 6, q5 found, npaths 0 -> out/D_l6z_TEST.txt. Seeds 380000+.
upa() { n=$1; shift; f=out/.pid_$n; [ -f $f ] && kill -0 $(cat $f) 2>/dev/null && { echo "$n running"; return; }
       setsid nohup env $ENVX ./lane30a.sh "$@" < /dev/null > /dev/null 2>&1 & echo $! > $f; echo "$n launched $!"; }
ENVX="LANEANNEAL=0 L6SCORE=1 FROZENBELOW=12 NMIN=2 NMAX=4 REPT=20,110 TESTOUT=out/D_l6z_TEST.txt" upa D_l6z D_l6z out/seed_SL41_d28.txt 380000 6 5 6
# 17:4xZ (Lead 17:42Z): D_l6g = GATED L6 score (rclimb30 env L6GATE=222): (caps, [F(6) >= 222], -npaths, F(6)) as caps*1e10 + gate*1e9
# - npaths*1e4 + F(6); same edits as D_l6; ANNEAL 0.15 (cannot cross the gate: a drop below 222 costs 1e9). TESTOUT out/D_l6g_TEST.txt with
# TESTGATE=222: first genome with caps 6, npaths 0 AND F(6) >= 222 (F(6) > 222 kills RC-PLATEAU). Seeds 390000+.
ENVX="LANEANNEAL=0.15 L6SCORE=1 L6GATE=222 FROZENBELOW=12 NMIN=2 NMAX=4 REPT=20,110 TESTOUT=out/D_l6g_TEST.txt TESTGATE=222" upa D_l6g D_l6g out/seed_SL41_d28.txt 390000 6 5 6
