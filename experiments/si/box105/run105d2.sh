#!/usr/bin/env bash
# L-SI box 105, D2: ladder105.py searches on R110's ladder shape, FREE and E-DOM priorities, d = 2, 3, 4 (seed 11, 40 restarts x 3000
# steps each; predecessor's measured setting). Resumable: a (mode, d) row already in out/ladder105.out is skipped. Best genomes to
# best/ladder_<mode>_d<d>.json; then val105.py runs N5 on each best genome (out/val105.out). About 40 min in all, one core. Engines read-only by git archive as run105.sh.
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out best "$T/red" "$T/new"
TOP=${TOP:-$(git rev-parse --show-toplevel)}; SI=${SI:-$TOP/experiments/si}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
export LNEW="$T/new" LRED="$T/red" BOX104="${BOX104:-$SI/box104}"
touch out/ladder105.out
for d in 2 3 4; do for mode in free edom; do
  grep -q "^LADDER105 mode $mode d $d seed 11 restarts 40 steps 3000: " out/ladder105.out && continue
  python3 -I ladder105.py $mode $d 11 40 3000 best/ladder_${mode}_d$d.json >> out/ladder105.out || exit 1
done; done
python3 -I val105.py best/ladder_free_d2.json best/ladder_edom_d2.json best/ladder_free_d3.json best/ladder_edom_d3.json best/ladder_free_d4.json best/ladder_edom_d4.json > out/val105.out || exit 1
echo DONE
