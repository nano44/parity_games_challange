#!/usr/bin/env bash
# L-SI box 105 check (~1 s, no engine, no git): (1) the [Q] strings of docs/si/box105-key.md were found at their sources (frozen
# out/quotes105.out: 0 FAIL) and stand in the file; (2) D1, when its outputs are present: key105.py against N5, all must-0 counters 0
# on the three random sets and on 25 of the lane's 26 frozen E-DOM instances (Kprev_8 is not an R104 genome: skipped), the control fires.
set -u
cd "$(dirname "$0")"
fail=0
bad() { echo "BOX105 FAIL $1"; fail=1; }
grep -q "^QUOTES105 total [0-9]* fail 0$" out/quotes105.out || bad "quotes at source"
python3 -I quotes105.py doc ../../../docs/si/box105-key.md > /dev/null || bad "quotes in the doc"
Z="s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0"
if [ -f out/key_rand.out ]; then
  [ "$(grep -c "^KEY105 rand .*: $Z | " out/key_rand.out)" = 3 ] && [ "$(wc -l < out/key_rand.out)" = 3 ] || bad "key random"
  grep -q "CTRL 1: s3fail 0 keyfail [1-9]" out/key_ctrl.out || bad "key control"
  [ "$(grep -c "^KEY105 json .*: $Z | " out/key_json.out)" = 25 ] && [ "$(grep -c "^KEY105 json Kprev_8.json: SKIPPED" out/key_json.out)" = 1 ] && [ "$(wc -l < out/key_json.out)" = 26 ] || bad "key frozen instances"
fi
[ $fail = 0 ] && echo "BOX105 checks: PASS"
exit $fail
