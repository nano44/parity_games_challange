#!/usr/bin/env bash
# L-SI self-test (< 2 min), run by scripts/verify.sh: engine valuations equal the REFEREE-checked PGSolver port on random
# games and switch-all counts equal the port's (incl. switchallexp N=1,2: 10 and 30 iterations); every rule returns py-zlk's
# regions with strategies that pass harness/verify.py; pinned killer instances in instances/ reproduce their counts.
set -euo pipefail
cd "$(dirname "$0")"
python3 -I xcheck.py --tiny | tail -1 | grep -q "XCHECK PASS"
echo "xcheck --tiny: PASS"
python3 -I coarse/levcheck.py | grep -q "LEVCHECK PASS"
echo "coarse levcheck (level ∞ sentinel): PASS"
if command -v g++ >/dev/null; then
  # compile to a separate name: the lane's long runs use ./vjfast and must not see it replaced mid-run
  g++ -O2 -std=c++17 -o vjfast_check vjfast.cpp && FAST_BIN=./vjfast_check python3 -I xcheck_fast.py --games 40 --nmax 10 | tail -1 | grep -q "XCHECK-FAST PASS" && echo "vjfast vs si.py (40 games): PASS"
else
  echo "g++ not found: vjfast cross-check skipped"
fi
if [ -f instances/pinned.txt ]; then
  while read -r rule file iters startflag; do
    [ -z "$rule" ] && continue
    start=best
    [ "$startflag" = "start" ] && start="spec:$(cat "instances/${file%.pg}.start")"
    if [ "$rule" = "most-improved" ]; then
      [ -x ./vjfast_check ] || { echo "pinned $rule $file: needs vjfast_check (g++), skipped"; continue; }
      got=$(./vjfast_check "$rule" "instances/$file" /dev/null --start "$start" 2>&1 | grep -o "with [0-9]* iterations" | grep -o "[0-9]*")
    else
      got=$(python3 -I si.py "$rule" "instances/$file" /dev/null --start "$start" 2>&1 | grep -o "with [0-9]* iterations" | grep -o "[0-9]*")
    fi
    [ "$got" = "$iters" ] || { echo "pinned $rule $file: expected $iters got $got"; exit 1; }
  done < instances/pinned.txt
  echo "pinned instances: PASS"
fi
# box 17 (RUN_D): OFFSET / TWIN-GAP checks on lib2o, and the DEAD strict-raise instance reproduces its length-only twin change
python3 -I rund/gap.py --list fb2o/lib2o.txt 2 | grep -q "GAP PASS"
python3 -I rund/rund.py --one rund/instances/lenonly_n8.pg | grep -q "LENONLY ('rund/instances/lenonly_n8.pg', 1, 2, 6, 4"
echo "rund (gap lib2o, lenonly_n8): PASS"
python3 -I rund/gap.py --one rund/instances/offret_n23.pg rund/instances/offret_n23.start | grep -q "RETURN ('rund/instances/offret_n23.pg', 0, 3, 22, \[131204, 264200, 264200, 131204\])"
echo "rund (OFFSET-ONCE counterexample offret_n23): PASS"
python3 -I rund/piece.py --list fb2o/lib2o.txt 2 | grep -q "PIECE PASS"
echo "rund (PIECE_D / SPLIT-RED on lib2o): PASS"
python3 -I rund/lvl.py --one rund/instances/incdown_n23.pg rund/instances/incdown_n23.start | grep -q "('INC', 'rund/instances/incdown_n23.pg', 0, 3, 22, \[20, 19\])"
echo "rund (INC counterexample incdown_n23): PASS"
