#!/bin/bash
# L-COMP box 47: n5v replay (replay47.py: modes spec, xi, seq) of the seeds = box 212's 5 towers (inst/towers, copied from claude/l-new 5fa64fe6
# experiments/new/box212/inst; SHA1SUMS). One line per (genome, mode) in out/replay47_towers.out; resumable. env LNEW (archive of claude/l-new).
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out; O=out/replay47_towers.out; touch $O
: "${LNEW:?set LNEW}"
for f in inst/towers/DBL4_d20_F30.json inst/towers/RECF4_d20_F60.json inst/towers/H5_d20_F62.json inst/towers/H6_d24_F126.json inst/towers/HIT7_d28_F254.json; do
  for m in spec xi seq; do grep -q "^$(basename $f) .* mode $m " $O || python3 replay47.py $f $m >> $O 2>> $O.err; done
done
echo "run47a done"
