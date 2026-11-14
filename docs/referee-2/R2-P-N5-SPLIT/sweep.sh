#!/bin/bash
# REFEREE-2 successor 36: P-N5-SPLIT replay driver (absolute paths; INST = box199/inst of a git archive of claude/l-new 399cda07)
D=/home/user/parity_games_challange/docs/referee-2/R2-P-N5-SPLIT; INST=${1:-/tmp/claude-0/-home-user-parity-games-challange/fba5f698-237c-51b2-b7cf-ab72f7aee52a/scratchpad/split/arc_399cda07/experiments/new/box199/inst}
cd $D
python3 r2split.py --gen 3000 2 any --gen 2000 3 self --gen 2000 4 acyc > gen.out 2>&1
for k in neg U0 how root; do python3 r2split.py --ctrl $k $INST/CX4_n21.json $INST/RWX_n95.json $INST/FW6_4.json > ctrl_$k.out 2>&1; done
python3 r2split.py --ctrl neg --gen 300 5 any > ctrl_neg_gen.out 2>&1
echo sweep done
