#!/usr/bin/env bash
# L-SI box 100 check (~10 s): must-0 TOTAL counters of cross100 (TWO-CROSS: unm, sumf, minf, tie) on the 26 instances and 400 random genomes;
# the CTRL=1 control fires (unm > 0); iv100 rows for MWR4/8/16_2 as recorded in docs/si/box100-scclin.md §1; if the pinned engine commits
# are present, trace100 on MWR4_2 equals out/trace_MWR4_2.out.
set -u
cd "$(dirname "$0")"
fail=0
for f in out/cross100_inst.out out/cross100_rand.out; do
  grep -q "^TOTAL .* unm 0 sumf 0 minf 0 tie 0 " "$f" || { echo "BOX100 FAIL totals $f"; fail=1; }
done
grep -q "^TOTAL .* unm [1-9]" out/cross100_ctrl.out || { echo "BOX100 FAIL control does not fire"; fail=1; }
grep -q "^MWR4_2.json T3 30 t0 0 N_C 44 M_C 91 E 89 I 2 Phi_int 9 Phi_ext 4 intervals 14 maxlen 8 " out/iv100.out || { echo "BOX100 FAIL iv MWR4_2"; fail=1; }
grep -q "^MWR8_2.json T3 54 t0 0 N_C 80 M_C 171 E 169 I 2 Phi_int 17 Phi_ext 8 intervals 26 maxlen 8 " out/iv100.out || { echo "BOX100 FAIL iv MWR8_2"; fail=1; }
grep -q "^MWR16_2.json T3 102 t0 0 N_C 152 M_C 331 E 329 I 2 Phi_int 33 Phi_ext 16 intervals 50 maxlen 8 " out/iv100.out || { echo "BOX100 FAIL iv MWR16_2"; fail=1; }
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e 59daaef2^{commit} 2>/dev/null && git cat-file -e fcba92fc^{commit} 2>/dev/null; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT; mkdir -p "$T/red" "$T/new"
  git -C "$TOP" archive 59daaef2 experiments/red | tar -x -C "$T/red" || exit 3
  git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/new" || exit 3
  RED="$T/red" LNEW="$T/new" python3 -I trace100.py ../box93/inst/MWR4_2.json > "$T/tr.out" 2>/dev/null
  cmp -s "$T/tr.out" out/trace_MWR4_2.out || { echo "BOX100 FAIL trace MWR4_2"; fail=1; }
else
  echo "BOX100 NOT RUN trace re-run (pinned commit 59daaef2 or fcba92fc absent)"
fi
[ $fail = 0 ] && echo "BOX100 checks: PASS"
exit $fail
