#!/usr/bin/env bash
# L-SI box 106: the kill search for CONJECTURE KEY2-5 with the audited abstract evaluator (mg106.py climb): 40 chunks (seeds 1..40) of
# 10 restarts x 5,000 hill-climb steps on the free depth-2 ladder; one line per chunk in out/climb106.out (resumable: a seed already
# there is skipped); each chunk's best genome to best/climb106_<seed>.json. Then every best genome is replayed on N5 (box 105 val105.py:
# s3fail, keyfail, endfail, wrong, keymono, valmono) into out/climbval106.out. About 1 h 40 min, one core.
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out best "$T/red" "$T/new"
TOP=${TOP:-$(git rev-parse --show-toplevel)}; SI=${SI:-$TOP/experiments/si}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
export LNEW="$T/new" LRED="$T/red" BOX104="${BOX104:-$SI/box104}"
touch out/climb106.out
for seed in $(seq 1 40); do
  grep -q "^MG106 climb seed $seed restarts 10 steps 5000: " out/climb106.out && continue
  python3 -I mg106.py climb $seed 10 5000 best/climb106_$seed.json >> out/climb106.out || exit 1
done
python3 -I ../box105/val105.py best/climb106_*.json > out/climbval106.out || exit 1
echo DONE
