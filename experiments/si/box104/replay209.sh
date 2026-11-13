#!/usr/bin/env bash
# L-SI box 104, duty (b): box 209's must-0 counters replayed on this lane's 26 frozen instances (box 91's 11, box 93's 8, box 98's 7;
# the set of box 99-103) under HOW3 by L-RED 65's own engine. Tools read-only, by git archive into a temporary directory:
#   L-NEW at claude/l-new 3f8960998 (box 209: experiments/new/box208/level208.py --hist, box209/plat209.py --hist, box209/own3hist209.py;
#     experiments/si/si.py, experiments/harness);
#   L-RED at claude/l-red 707c0e82 (experiments/red/r232/how3_232.py with r230, r221q: values, Odd's reply and tie rule of its own).
# Per instance: own3hist209.py writes the HOW3 run as a history; level208.py --hist and plat209.py --hist count on it.
# Controls: LV_CTRL=2 (front := the highest lagging class) on MWR4_2, C6G8_n54, WC16_2; PL_CTRL=1 (Y := the front alone) on the same
#   three (no plateau there: it cannot fire) and on four instances with plateaus (DWT20_2803, C98_2_2_3, C98_3_3_3, C98_5_5_3).
# Output: out/replay209_level.out, out/replay209_plat.out, out/replay209_ctrl.out, out/replay209_engine.sha1. About 15 min, one core.
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/new" "$T/red" "$T/h"
TOP=${TOP:-$(git rev-parse --show-toplevel)}; SI=${SI:-$TOP/experiments/si}
git -C "$TOP" archive 3f8960998 experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/new" || exit 3
git -C "$TOP" archive 707c0e82bd514e8f76b7ba8a6d67b1e0ccca045c experiments/red/r230 experiments/red/r221q experiments/red/r232 | tar -x -C "$T/red" || exit 3
R="$T/red/experiments/red"; B="$T/new/experiments/new"
( cd "$R" && sha1sum r232/how3_232.py r230/elev230.py r230/bonly3_230.py r221q/own.py ) | sed 's/$/ (claude\/l-red 707c0e82)/' > out/replay209_engine.sha1
( cd "$B" && sha1sum box208/level208.py box209/plat209.py box209/own3hist209.py ) | sed 's/$/ (claude\/l-new 3f8960998)/' >> out/replay209_engine.sha1
export LNEW="$T/new"
I=$SI/box91/inst; J=$SI/box93/inst
L="$I/WC4_2.json $I/WC16_2.json $I/FW8_2.json $I/FW16_2.json $I/MW8_2.json $I/MW32_2.json $I/C6G8_n54.json $I/RWX_n95.json $I/DWT20_2803.json $I/DHIB26_2804.json $I/DHIB18_2805.json $J/k1fail_202.json $J/Ku_4.json $J/Ku_8.json $J/Ku_16.json $J/Kprev_8.json $J/MWR4_2.json $J/MWR8_2.json $J/MWR16_2.json $(ls $SI/box98/inst/C98_*.json)"
: > out/replay209_level.out; : > out/replay209_plat.out; : > out/replay209_ctrl.out
for f in $L; do
  b=$(basename "$f" .json)
  ( cd "$B/box209" && python3 own3hist209.py "$R" "$f" "$T/h/$b.json" ) > /dev/null 2>&1 || { echo "$b.json ENGINE FAILED" >> out/replay209_level.out; continue; }
  ( cd "$B/box209" && python3 ../box208/level208.py --hist "$T/h/$b.json" ) >> out/replay209_level.out 2>&1
  ( cd "$B/box209" && python3 plat209.py --hist "$T/h/$b.json" ) >> out/replay209_plat.out 2>&1
  case $b in MWR4_2|C6G8_n54|WC16_2)
    ( cd "$B/box209" && LV_CTRL=2 python3 ../box208/level208.py --hist "$T/h/$b.json" ) 2>&1 | sed 's/^/LV_CTRL=2 /' >> out/replay209_ctrl.out ;;
  esac
  case $b in MWR4_2|C6G8_n54|WC16_2|DWT20_2803|C98_2_2_3|C98_3_3_3|C98_5_5_3)
    ( cd "$B/box209" && PL_CTRL=1 python3 plat209.py --hist "$T/h/$b.json" ) 2>&1 | sed 's/^/PL_CTRL=1 /' >> out/replay209_ctrl.out ;;
  esac
  rm -f "$T/h/$b.json"
done
echo DONE
