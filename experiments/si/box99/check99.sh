#!/usr/bin/env bash
# L-SI box 99 check (~5 s): TOTAL lines of out/inst99.out and out/rand99.out have locfail 0 and chainfail 0; if the pinned engine commit
# is present, scc99 on WC4_2 equals its recorded row.
set -u
cd "$(dirname "$0")"
fail=0
for f in out/inst99.out out/rand99.out; do
  grep -q "^TOTAL .* locfail 0 chainfail 0 " "$f" || { echo "BOX99 FAIL totals $f"; fail=1; }
done
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e fcba92fc^{commit} 2>/dev/null; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T" || exit 3
  a=$(ROOT="$T" python3 -I scc99.py inst ../box91/inst/WC4_2.json | grep '^WC4_2')
  [ "$a" = "$(grep '^WC4_2' out/inst99.out)" ] || { echo "BOX99 FAIL row WC4_2"; fail=1; }
else
  echo "BOX99 NOT RUN engine row (pinned commit fcba92fc absent)"
fi
[ $fail = 0 ] && echo "BOX99 checks: PASS"
exit $fail
