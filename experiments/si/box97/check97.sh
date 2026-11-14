#!/usr/bin/env bash
# L-SI box 97 check (~10 s): every must-be-0 total (nstd s0 nfb nhow) is 0 in out/inst97.out and out/rand97.out, the control fires in
# out/ctrl97.out, and (if the pinned engine commit is present) std97 on MWR4_2 equals its recorded row.
set -u
cd "$(dirname "$0")"
fail=0
for f in out/inst97.out out/rand97.out; do
  grep -q "^TOTAL .* nstd 0 s0 0 nfb 0 nhow 0 " "$f" || { echo "BOX97 FAIL totals $f"; fail=1; }
done
grep -q "^TOTAL .* nstd [1-9]" out/ctrl97.out || { echo "BOX97 FAIL control"; fail=1; }
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e fcba92fc^{commit} 2>/dev/null; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T" || exit 3
  a=$(ROOT="$T" python3 -I std97.py inst ../box93/inst/MWR4_2.json | grep '^MWR4_2')
  [ "$a" = "$(grep '^MWR4_2' out/inst97.out)" ] || { echo "BOX97 FAIL row MWR4_2"; fail=1; }
else
  echo "BOX97 NOT RUN engine row (pinned commit fcba92fc absent)"
fi
[ $fail = 0 ] && echo "BOX97 checks: PASS"
exit $fail
