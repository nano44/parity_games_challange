#!/usr/bin/env bash
# L-SI box 104: Lemma WRAP's DATA (wrap104.py): the W-flat wrapper W(H, s0) on random games, on PGSolver's switchallexp_n and on
# Friedmann's G_n of arXiv 1106.0778v2 (Figure 4's injective priorities, and Table 4 as printed) with its initial strategy.
# Engines read-only as in run104.sh (env LRED: claude/l-red 8c01d40e r217/fried.py; env LNEW: claude/l-new fcba92fc; env LLIT:
# claude/l-lit 5c53efbd docs/lit/T66-depth-check.py). Output: out/wrap_*.out, inst/W_*.pg, inst/WL_*.pg, inst/rand300.json.
# Default: the runs up to n = 6 (about 8 min, one core). LONG=1: only the long rows n = 7, 8 and the two-engine check at n = 5
# (about 60 min), written to out/wrap_long.out.
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out inst "$T/red" "$T/new" "$T/lit"
TOP=${TOP:-$(git rev-parse --show-toplevel)}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
git -C "$TOP" archive 5c53efbd2d8401dc056e575fa42e49b50a265a0c docs/lit/T66-depth-check.py | tar -x -C "$T/lit" || exit 3
export LRED="$T/red" LNEW="$T/new" LLIT="$T/lit"
if [ "${LONG:-0}" = 1 ]; then
  python3 -I wrap104.py lmcs fig4 7 8 > out/wrap_long.out || exit 1
  python3 -I wrap104.py fried 7 8 >> out/wrap_long.out || exit 1
  python3 -I wrap104.py xcklmcs fig4 5 >> out/wrap_long.out || exit 1
  python3 -I wrap104.py xck 5 >> out/wrap_long.out || exit 1
  echo DONE; exit 0
fi
python3 -I wrap104.py rand 1043 3000 12 > out/wrap_rand.out || exit 1
python3 -I wrap104.py rand 1044 1000 24 >> out/wrap_rand.out || exit 1
ALG=spec python3 -I wrap104.py rand 1043 3000 12 >> out/wrap_rand.out || exit 1
CTRL=1 python3 -I wrap104.py rand 1043 100 12 > out/wrap_ctrl.out || exit 1
CTRL=2 python3 -I wrap104.py rand 1043 100 12 >> out/wrap_ctrl.out || exit 1
python3 -I wrap104.py dumprand 1043 300 12 inst/rand300.json > /dev/null || exit 1
python3 -I wrap104.py json inst/rand300.json > out/wrap_json.out || exit 1
python3 -I wrap104.py ties 2 3 4 5 6 7 8 > out/wrap_ties.out || exit 1
python3 -I wrap104.py lmcs fig4 1 2 3 4 5 6 > out/wrap_lmcs_xi.out || exit 1
python3 -I wrap104.py lmcs table4 1 2 3 4 5 6 >> out/wrap_lmcs_xi.out || exit 1
ALG=spec python3 -I wrap104.py lmcs fig4 1 2 3 4 5 6 > out/wrap_lmcs_spec.out || exit 1
python3 -I wrap104.py fried 2 3 4 5 6 > out/wrap_fried_xi.out || exit 1
ALG=spec python3 -I wrap104.py fried 2 3 4 5 6 > out/wrap_fried_spec.out || exit 1
python3 -I wrap104.py xcklmcs fig4 1 2 3 4 > out/wrap_xck.out || exit 1
python3 -I wrap104.py xck 2 3 4 >> out/wrap_xck.out || exit 1
for n in 2 3 4 5 6 7 8; do python3 -I wrap104.py pg "$n" "inst/W_$n.pg" || exit 1; done
for n in 1 2 3 4; do python3 -I wrap104.py pglmcs fig4 "$n" "inst/WL_$n.pg" || exit 1; done
(cd inst && sha1sum F_*.pg W_*.pg WL_*.pg rand300.json > SHA1SUMS)
echo DONE
