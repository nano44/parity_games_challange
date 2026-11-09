#!/bin/bash
# REFEREE-2 successor 36: controls (after the continue fix) and mutation sweep (own mutate()) around pinned instances
D=/home/user/parity_games_challange/docs/referee-2/R2-P-N5-SPLIT; INST=${1:-/tmp/claude-0/-home-user-parity-games-challange/fba5f698-237c-51b2-b7cf-ab72f7aee52a/scratchpad/split/arc_399cda07/experiments/new/box199/inst}
cd $D
for k in neg U0 how root; do python3 r2split.py --ctrl $k $INST/CX4_n21.json $INST/RWX_n95.json $INST/FW6_4.json > ctrl_$k.out 2>&1; done
python3 r2split.py --ctrl neg --gen 300 5 any > ctrl_neg_gen.out 2>&1
A=""; s=11; for f in CX4_n21 C2CX4_n23 ROUTELOW_n21 NK6_cl21 GROW7_n34 MW4_2 FW4_2 FW6_4; do A="$A --mut 300 $s $INST/$f.json"; s=$((s+1)); done
python3 r2split.py $A > mut.out 2>&1
echo sweep2 done
