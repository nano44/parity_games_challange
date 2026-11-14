#!/bin/bash
# Box 212 RF-D DATA on the tower genomes (inst/, from claude/l-comp 2fa72fb5 box 29; see inst/SOURCE.txt): rfd212.py, N5 itself (spec)
# and the variants seq, idx, xi of box190 n5v, from S3 on Gamma3(G) up to the first fallback. Resumable. Run from experiments/new/box212.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {
mkdir -p out
for r in spec seq idx xi; do
  o=out/rfd212_tower_$r.out
  [ -s $o ] || { RFD_MODE=$r timeout 5400 python3 -I rfd212.py inst/DBL4_d20_F30.json inst/RECF4_d20_F60.json inst/H5_d20_F62.json inst/H6_d24_F126.json inst/HIT7_d28_F254.json > $o.tmp 2>&1 && mv $o.tmp $o; }
done
echo "run212h finished"
}
main "$@"; exit $?
