#!/bin/bash
# Box 195 (L-NEW successor 63): DATA behind Lemmas E0-E4 / Theorems ENDGAME-3 and ENDGAME-3-N5 (eg195.py). Run from experiments/new/box195.
# Families: L-RED R221 §11 (spost221.py gen(), transcribed; claude/l-red 86a7a7a8) + rand + acyc; all pinned genomes of box189-194.
# Lines tagged «ctrl» are negative controls: their fail counters MUST be positive (check.sh tests both).
set -e
cd "$(dirname "$0")"
for mode in xi spec; do
  for fam in rand esc noesc deep dense late lvl0 acyc; do EG195_MODE=$mode python3 eg195.py $fam 1953 300; done
  EG195_MODE=$mode python3 eg195.py --files ../box194/inst/*.json ../box193/inst/*.json ../box192/inst/*.json ../box191/inst/*.json \
    ../box189/inst/*.json ../box189/corpus/*.json
done
EG195_TAG="ctrl1 " EG195_CTRL=1 python3 eg195.py rand 195 100
EG195_TAG="ctrl2 " EG195_CTRL=2 python3 eg195.py rand 195 100
