#!/bin/bash
# L-RED-B, report B1 (docs/red-b/B1-box208.md): the DATA runs. Run from experiments/red-b:  bash run_b1.sh A|B|W|X|T|C|D|E|F|G|H
# A: engine validation; B: counters on the 78 frozen genomes; W: WIN / R-HEIGHT counters (win.py); X: the abstract game of par. 10 (abs_rb.py); T: every tie-breaking branch (ties.py); C: controls; D: exhaustive tiny sizes; E: random sweeps;
# F, G, H: longer exhaustive sizes, random sweeps, climbs (minutes to hours; only after the Lead's go).
# A set is skipped when its output exists; F-H are restart-safe. Outputs go to data/ (the repository's root .gitignore
# ignores experiments/*/out/, so the outputs are not kept in a directory called out).
set -u
export PYTHONDONTWRITEBYTECODE=1
. ./frozen.sh
one() { local out="data/$1"; shift; [ -s "$out" ] && return 0; "$@" > "$out.tmp" 2>&1 && mv "$out.tmp" "$out"; }
case "${1:-A}" in
A) one xcheck_s1.out python3 xcheck.py 3000 1 9
   one xcheck_s2.out python3 xcheck.py 400 2 12
   one cmpT_records.out python3 cmpT.py inst/box208_records_T.txt $REC
   one cmpT_corpus.out python3 cmpT.py inst/box208_corpus_T.txt $COR ;;
B) one lev_records_all.out python3 lev.py --all $REC
   one lev_corpus_all.out python3 lev.py --all $COR
   one lev_frozen_high.out python3 lev.py --tie=high $REC $COR
   one lev_frozen_rand.out python3 lev.py --tie=rand $REC $COR ;;
W) one win_records.out python3 win.py $REC
   one win_corpus.out python3 win.py $COR
   one win_rand_s51.out python3 win.py --rand 51 20000 10 20 mix
   one win_rand_k1_s52.out python3 win.py --rand 52 20000 10 20 k1
   RB_WCTRL=1 one win_ctrl1.out python3 win.py inst/CFI3_n48.json inst/RINT_n48.json ../new/box206/inst/K1L10_n48.json ;;
X) one abs_rb.out bash -c 'python3 abs_rb.py 1 30000 8; python3 abs_rb.py 2 20000 30; python3 abs_rb.py 3 5000 100 0 1 2 4 8 16 32; ABS_CTRL=1 python3 abs_rb.py 4 2000 8' ;;
T) one ties_s61.out python3 ties.py 61 3000 7 14 64 mix
   one ties_s62.out python3 ties.py 62 1500 12 26 64 mix ;;
C) RB_CTRL=1 one lev_ctrl1.out python3 lev.py inst/CFI3_n48.json ../new/box203/inst/MWR4_2.json ../new/box202/inst/WC8_2.json
   RB_CTRL=2 one lev_ctrl2.out python3 lev.py inst/CFI3_n48.json ../new/box206/inst/K1D4_n48.json ../new/box202/inst/DSALT6_n108.json ;;
D) for nm in "1 1" "1 2" "2 2" "1 3" "2 3" "3 3" "1 4" "2 4"; do set -- $nm; one exh_N$1_M$2.out python3 sweep.py exh $1 $2; done ;;
E) one rand_s11.out python3 sweep.py rand 11 60000 7 12 all mix
   one rand_s12.out python3 sweep.py rand 12 20000 14 30 all mix
   one rand_s31.out python3 sweep.py rand 31 30000 8 14 all eany
   one mut_s41.out python3 mutsweep.py 41 150 6 T inst/CFI3_n48.json inst/RINT_n48.json ../new/box206/inst/K1L10_n48.json \
       ../new/box206/inst/K1D4_n48.json ../new/box206/inst/BLKX26_n48.json ../new/box203/inst/K1F21_n48.json \
       ../new/box203/inst/MWR4_2.json ../new/box206/inst/CW4_n.json ;;
F) # exhaustive, in residue classes of the outer loop (each chunk a few minutes; restart-safe: finished chunks are skipped)
   one exh_N1_M5.out python3 sweep.py exh 1 5
   for p in $(seq 0 15); do one exh_N3_M4_p${p}of16.out python3 sweep.py exh 3 4 $p 16; done
   for p in $(seq 0 11); do one exh_N1_M6_p${p}of12.out python3 sweep.py exh 1 6 $p 12; done
   ;;  # (N, M) with M = N are not run beyond (3,3): every mover has one option, so T = 0 and LEVEL is vacuous
G) # random sweeps in chunks (seed = chunk), all reference states, random tie rule
   for s in $(seq 400 409); do one rand_s${s}.out python3 sweep.py rand $s 200000 4 7 all mix; done
   for s in $(seq 100 114); do one rand_s${s}.out python3 sweep.py rand $s 200000 8 12 all mix; done
   for s in $(seq 200 209); do one rand_s${s}.out python3 sweep.py rand $s 30000 20 40 all mix; done
   for s in $(seq 300 304); do one rand_s${s}.out python3 sweep.py rand $s 100000 8 14 all eany; done ;;
H) # climbs (resumable; work/climb_*.json), each capped in size; outputs appended
   for spec in "plat 1 60000 12 24" "loud 2 60000 12 24" "mvals 3 60000 12 24" "Tn 4 60000 12 24" "platrel 5 60000 14 30" \
               "phi 6 40000 20 44" "plat 7 40000 24 50" "T 8 40000 24 50" "bothYeq 9 30000 14 30"; do
     set -- $spec; out="data/climb_$1_s$2_N$4_M$5.out"
     grep -q "^CLIMB .* done" "$out" 2>/dev/null || python3 climb.py $1 $2 $3 $4 $5 >> "$out" 2>&1
   done ;;
esac
echo "run_b1 ${1:-A} finished"
