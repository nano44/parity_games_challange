#!/bin/bash
# L-COMP box 46, successor 22, WORK item 2 (Lead brief + «go» 06:15Z 2026-11-13): L-NEW's box 213 KEY-TAU counters (keymu213.py) and box 215
# KEYSIDE-ALL counters (keyside215.py), run UNCHANGED with python3 -I from their own directory in an archive of claude/l-new cd4f7f4d
# (env LNEW215 = `git archive cd4f7f4d experiments/new experiments/si/si.py experiments/harness experiments/n5-second
# experiments/hard-families | tar -x -C $LNEW215`), on BEST_B3_WU151_NM163_e934d333 first, then the other box 46 climb bests and seeds.
# Modes: spec (the counters), and the controls named in the tools' headers: keymu213 KM_MODE=xi and KM_CTRL=1 (must fire kp);
# keyside215 KM_MODE=xi and KS_CTRL=1 (must fire kflip), KS_CTRL=2 (must fire casc where own flips exist).
# One line per (genome, mode) in out/key46_<tool>_<mode>.out; resumable; 900 s cap per run (a failed or timed-out run is a FAIL line with its exit code). Usage: run46j.sh
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
: "${LNEW215:?set LNEW215}"; N="$LNEW215/experiments/new"; D=$(pwd)
L="out/climb46/BEST_B3_WU151_NM163_e934d333.json $(ls out/climb46/*.json out/climb46e/BEST_E3_*.json inst/seeds46/*.json | grep -v e934d333)"
run() { local tool=$1 tag=$2 f=$3; shift 3; local o="$D/out/key46_${tool}_${tag}.out"; touch "$o"
  grep -q "^$(basename $f) \|^FAIL $(basename $f) " "$o" && return
  (cd "$N/box${tool: -3}" && env "$@" timeout 900 python3 -I $tool.py "$D/$f" >> "$o" 2>> "$o.err"); local rc=$?
  [ $rc -eq 0 ] || echo "FAIL $(basename $f) rc $rc (124 = timeout)" >> "$o"; }
for f in $L; do
  run keymu213 spec $f KM_MODE=spec; run keyside215 spec $f KM_MODE=spec
done
for f in $L; do
  run keymu213 xi $f KM_MODE=xi; run keymu213 ctrl1 $f KM_MODE=spec KM_CTRL=1
  run keyside215 xi $f KM_MODE=xi; run keyside215 ctrl1 $f KM_MODE=spec KS_CTRL=1; run keyside215 ctrl2 $f KM_MODE=spec KS_CTRL=2
done
echo "run46j done"
}
main "$@"
