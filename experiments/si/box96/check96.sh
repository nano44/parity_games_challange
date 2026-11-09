#!/usr/bin/env bash
# L-SI box 96 check (~10 s): if the pinned engine commit is present, d96 on the own engine for WC4_2, k1fail_202, MWR4_2 equals the
# recorded rows (out/own96.out), and every must-be-0 column (dpass lamD bonly sfail relD unlD) is 0 in out/own96.out and out/g396.out.
set -u
cd "$(dirname "$0")"
fail=0
for f in out/own96.out out/g396.out; do
  awk 'NR > 1 { if ($8 + $9 + $10 + $11 + $12 + $13 != 0) bad = 1 } END { exit bad }' "$f" || { echo "BOX96 FAIL must-be-0 $f"; fail=1; }
done
[ "$(grep -c '^own ' out/own96.out)" = 19 ] && [ "$(grep -c '^g3 ' out/g396.out)" = 19 ] || { echo "BOX96 FAIL row count"; fail=1; }
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e 4b309716^{commit} 2>/dev/null; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T" || exit 3
  export OWN_DIR="$T/experiments/red/r221"
  a=$(python3 -I d96.py own ../box91/inst/WC4_2.json ../box93/inst/k1fail_202.json ../box93/inst/MWR4_2.json | grep -v '^engine')
  [ "$a" = "$(grep -E '^own (WC4_2|k1fail_202|MWR4_2)\.json' out/own96.out)" ] || { echo "BOX96 FAIL own rows"; fail=1; }
else
  echo "BOX96 NOT RUN engine rows (pinned commit 4b309716 absent)"
fi
python3 -I -B pk/quotesB3.py ../../.. > /dev/null || { echo "BOX96 FAIL packet quotes"; fail=1; }
[ $fail = 0 ] && echo "BOX96 checks: PASS"
exit $fail
