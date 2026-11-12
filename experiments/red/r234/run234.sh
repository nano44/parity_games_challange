#!/usr/bin/env bash
# L-RED 66 R234: WINDOW / LAM-GAP / DEPTH-COUNT3 counters on box 99's 26 frozen instances (claude/l-si 23d39400, box91/93/98 inst).
# Engines: this lane's r232 how3_232 + r221q own.py (working tree); Gamma3 graph from L-NEW fcba92fc (env LNEW, extracted here).
# Output: out/w234_inst.out, out/w234_ctrl.out, out/d234_inst.out. Usage: run234.sh [w|d|k|all|exh4]  (exh4: ~10 min CPU, not in all)
set -u
cd "$(dirname "$0")"
TOP=$(git rev-parse --show-toplevel); T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/new" "$T/inst"
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/new" || exit 3
git -C "$TOP" archive 23d39400 experiments/si/box91/inst experiments/si/box93/inst experiments/si/box98/inst | tar -x -C "$T/inst" || exit 3
export LNEW="$T/new"
L=$(ls "$T"/inst/experiments/si/box9*/inst/*.json)
M=${1:-all}
if [ "$M" = w ] || [ "$M" = all ]; then
  python3 w234.py $L > out/w234_inst.out || exit 1
  CTRL=1 python3 w234.py "$T"/inst/experiments/si/box93/inst/MWR4_2.json "$T"/inst/experiments/si/box98/inst/C98_4_5_3.json > out/w234_ctrl.out || exit 1
fi
if [ "$M" = d ] || [ "$M" = all ]; then
  python3 d234.py $L > out/d234_inst.out || exit 1
fi
if [ "$M" = k ] || [ "$M" = all ]; then   # kill side of LAM-GAP / SHARP (independent engine), DEPTH-COUNT3 on random genomes
  git -C "$TOP" archive 59daaef2 experiments/red | tar -x -C "$T" || exit 3
  git -C "$TOP" show 23d39400:experiments/si/box101/lamgap101.py > "$T/lamgap101.py" || exit 3
  python3 lg234.py exh 3 > out/lg_exh3.out || exit 1
  CTRL=1 python3 lg234.py exh 3 > out/lg_exh3_ctrl.out || exit 1
  LSI="$T/lamgap101.py" RED="$T" python3 xlg234.py 1 3000 9 > out/xlg_s1.out || exit 1
  python3 d234.py rand 2341 100 > out/d234_rand.out || exit 1
  for a in "5 5 3000" "7 7 3000" "11 9 4000" "12 9 4000"; do python3 lg234.py climb $a > out/lg_climb_${a// /_}.out || exit 1; done
fi
if [ "$M" = exh4 ]; then python3 lg234.py exh 4 > out/lg_exh4.out || exit 1; fi
echo DONE
