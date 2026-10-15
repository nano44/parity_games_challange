#!/usr/bin/env bash
# L-SI self-test (< 2 min), run by scripts/verify.sh: engine valuations equal the REFEREE-checked PGSolver port on random
# games and switch-all counts equal the port's (incl. switchallexp N=1,2: 10 and 30 iterations); every rule returns py-zlk's
# regions with strategies that pass harness/verify.py; pinned killer instances in instances/ reproduce their counts.
set -euo pipefail
cd "$(dirname "$0")"
python3 -I xcheck.py --tiny | tail -1 | grep -q "XCHECK PASS"
echo "xcheck --tiny: PASS"
if [ -f instances/pinned.txt ]; then
  while read -r rule file iters startflag; do
    [ -z "$rule" ] && continue
    start=best
    [ "$startflag" = "start" ] && start="spec:$(cat "instances/${file%.pg}.start")"
    got=$(python3 -I si.py "$rule" "instances/$file" /dev/null --start "$start" 2>&1 | grep -o "with [0-9]* iterations" | grep -o "[0-9]*")
    [ "$got" = "$iters" ] || { echo "pinned $rule $file: expected $iters got $got"; exit 1; }
  done < instances/pinned.txt
  echo "pinned instances: PASS"
fi
