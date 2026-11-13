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
# Addendum F: REFEREE 32's replacement for RESTRICT-C (iv) (claude/referee ff9b16f6 docs/referee/R-restrictC-preread.md l. 126-128):
# the byte copy has the recorded sha1 and stands unchanged in docs/si/box101-lamgap.md.
[ "$(sha1sum < restrictC_iv_ff9b16f6.txt | cut -c1-40)" = a76a8eab7afcf25458ae849737056af3a9f14229 ] || { echo "BOX101 FAIL Addendum F sha1"; fail=1; }
python3 -I -c 'import sys; t = open("restrictC_iv_ff9b16f6.txt", encoding="utf-8").read().rstrip("\n"); d = open("../../../docs/si/box101-lamgap.md", encoding="utf-8").read(); sys.exit(0 if d.count(t) == 1 else 1)' || { echo "BOX101 FAIL Addendum F string not in the doc"; fail=1; }
[ $fail = 0 ] && echo "BOX101 checks: PASS"
exit $fail
