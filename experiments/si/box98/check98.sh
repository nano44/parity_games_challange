#!/usr/bin/env bash
# L-SI box 98 check (~10 s): the frozen climb bests match inst/SHA1SUMS; upfail is 0 on every row of out/asc98_*.out and out/ascC98_*.out;
# the two engines agree on U, T, maxasc, Dmax; if the pinned engine commit is present, asc98 own on C98_2_2_3 equals its recorded row.
set -u
cd "$(dirname "$0")"
fail=0
(cd inst && sha1sum -c --quiet --strict SHA1SUMS) || { echo "BOX98 FAIL inst sha1"; fail=1; }
for f in out/asc98_own.out out/asc98_g3.out out/ascC98_own.out out/ascC98_g3.out; do
  awk 'NR > 1 && $10 != 0 { bad = 1 } END { exit bad }' "$f" || { echo "BOX98 FAIL upfail $f"; fail=1; }
done
for p in asc98 ascC98; do
  cmp -s <(cut -d' ' -f2-8 out/${p}_own.out | tail -n +2) <(cut -d' ' -f2-8 out/${p}_g3.out | tail -n +2) || { echo "BOX98 FAIL engines $p"; fail=1; }
done
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e 4b309716^{commit} 2>/dev/null; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T" || exit 3
  a=$(OWN_DIR="$T/experiments/red/r221" python3 -I asc98.py own inst/C98_2_2_3.json | grep -v '^engine')
  [ "$a" = "$(grep '^own C98_2_2_3' out/ascC98_own.out)" ] || { echo "BOX98 FAIL own row"; fail=1; }
else
  echo "BOX98 NOT RUN engine row (pinned commit 4b309716 absent)"
fi
[ $fail = 0 ] && echo "BOX98 checks: PASS"
exit $fail
