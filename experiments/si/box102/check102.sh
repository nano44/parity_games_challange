#!/usr/bin/env bash
# L-SI box 102 check (~1 s): must-0 counters of deep102 (abovefail, propfail) on the 26 instances and 400 random genomes; the PCTRL control
# fires; the recorded MWR rows (no internal flip of e-depth > 1) and the DHIB26_2804 row (D1 24, D2 11).
set -u
cd "$(dirname "$0")"
fail=0
for f in out/deep102_inst.out out/deep102_rand.out; do
  grep -q "^TOTAL .* abovefail 0 lam [0-9]* propfail 0 " "$f" || { echo "BOX102 FAIL totals $f"; fail=1; }
done
grep -q "^TOTAL .* propfail [1-9]" out/deep102_ctrl.out || { echo "BOX102 FAIL control does not fire"; fail=1; }
for m in MWR4_2 MWR8_2 MWR16_2; do
  grep -q "^$m.json T3 [0-9]* {'nflip': [0-9]*, 'D1': 0, 'D2': 0," out/deep102_inst.out || { echo "BOX102 FAIL row $m"; fail=1; }
done
grep -q "^DHIB26_2804.json T3 28 {'nflip': 129, 'D1': 24, 'D2': 11," out/deep102_inst.out || { echo "BOX102 FAIL row DHIB26"; fail=1; }
[ $fail = 0 ] && echo "BOX102 checks: PASS"
exit $fail
