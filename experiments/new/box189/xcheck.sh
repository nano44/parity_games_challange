#!/bin/bash
# P-N5-REACH cross-checks (not in check.sh: needs tools/oink/build from scripts/setup_oink.sh; ~10 min). Run from the repo root.
# For each corpus genome: Gamma3 (_g3) and Gamma (_g0) as .pg (box189/writepg.py), sha1; L-COMP's n5b.py --mode spec from its
# default start (S3) -> iterations / fallbacks; experiments/new/check_sol2.py (Oink 8fbf0a7 --zlk, harness/verify.py) on n5b's solution.
t=$(mktemp -d)
for f in experiments/new/box189/corpus/*.json; do python3 experiments/new/box189/writepg.py $f $t/$(basename $f .json); done
for f in $t/*_g3.pg $t/*_g0.pg; do b=${f%.pg}
  printf "%s %s | %s | %s\n" "$(basename $b)" "$(sha1sum < $f | cut -c1-40)" \
    "$(python3 experiments/n5-second/n5b.py $f $b.sol --mode spec 2>&1 | tail -1)" "$(python3 experiments/new/check_sol2.py $f $b.sol 300 2>&1 | tail -1)"
done
rm -rf "$t"
