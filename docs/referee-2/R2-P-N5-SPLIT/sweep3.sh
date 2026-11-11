#!/bin/bash
# REFEREE-2 successor 36: mutation sweep (own mutate()), one output per base instance so that a stall loses one chunk at most.
# Seeds 11-18 as in sweep2.sh; a chunk whose output already has a TOTAL line is skipped (checkpoint).
D=/home/user/parity_games_challange/docs/referee-2/R2-P-N5-SPLIT; INST=${1:-/tmp/claude-0/-home-user-parity-games-challange/fba5f698-237c-51b2-b7cf-ab72f7aee52a/scratchpad/split/arc_399cda07/experiments/new/box199/inst}
cd $D
s=11
for f in CX4_n21 C2CX4_n23 ROUTELOW_n21 NK6_cl21 GROW7_n34 MW4_2 FW4_2 FW6_4; do
  o=mut_$f.out
  if ! grep -q TOTAL $o 2>/dev/null; then python3 r2split.py --mut 300 $s $INST/$f.json > $o 2>&1; fi
  s=$((s+1))
done
# ninth chunk (added 11-11): 100 mutations of RWX_n95, the only pinned run with S_t = S_t′ couples (RW-SHAPE non-vacuous)
if ! grep -q TOTAL mut_RWX_n95.out 2>/dev/null; then python3 r2split.py --mut 100 19 $INST/RWX_n95.json > mut_RWX_n95.out 2>&1; fi
echo sweep3 done
