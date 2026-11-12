#!/usr/bin/env bash
# L-SI box 101 check (~1 s): must-0 counters of lamgap101 (pathfail, gapfail, optfail, lfail) on the three census files; both controls fire.
set -u
cd "$(dirname "$0")"
fail=0
for f in out/lamgap_s1.out out/lamgap_s2.out out/lamgap_s3_n40.out; do
  grep -q "^TOTAL pathfail 0 .* gapfail 0 optfail 0 lfail 0 " "$f" || { echo "BOX101 FAIL totals $f"; fail=1; }
done
grep -q "^TOTAL .* gapfail [1-9]" out/lamgap_ctrl.out || { echo "BOX101 FAIL CTRL control does not fire"; fail=1; }
grep -q "^TOTAL pathfail [1-9]" out/lamgap_pctrl.out || { echo "BOX101 FAIL PCTRL control does not fire"; fail=1; }
[ $fail = 0 ] && echo "BOX101 checks: PASS"
exit $fail
