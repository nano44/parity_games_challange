#!/usr/bin/env bash
# L-RED 66 R235: box 208 attack. Extracts box 208 (claude/l-new 8db300fe) and trunk RESULTS (471aba45), then: q235 (29 quotes),
# lv235 on box202's 53 corpus genomes + control, plc235 climbs (CPU-heavy, mode c). Output: out/. Usage: run235.sh [q|lv|c]
set -u
cd "$(dirname "$0")"
TOP=$(git rev-parse --show-toplevel); T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out
git -C "$TOP" show 8db300fe:docs/new/N5-LEVEL-box208.md > "$T/box208.md" || exit 3
git -C "$TOP" show 471aba45:docs/RESULTS.md > "$T/RESULTS.md" || exit 3
git -C "$TOP" archive 8db300fe experiments/new/box202/inst experiments/new/box203/inst experiments/new/box206/inst | tar -x -C "$T" || exit 3
M=${1:-q}
[ "$M" = q ] && { python3 q235.py "$T/box208.md" "$T/RESULTS.md" > out/q235.out || exit 1; }
if [ "$M" = lv ]; then
  python3 lv235.py "$T"/experiments/new/box202/inst/*.json > out/lv235_corpus.out || exit 1
  CTRL=1 python3 lv235.py "$T"/experiments/new/box202/inst/C6G8_n54.json "$T"/experiments/new/box202/inst/C2CX4_n23.json > out/lv235_ctrl.out || exit 1
fi
if [ "$M" = c ]; then
  OUT=out/plc SCORE=ratio NMAX=56 DMAX=3 RESUME=1 python3 plc235.py ratK1F 2351 3000 "$T"/experiments/new/box203/inst/K1F21_n48.json || exit 1
  OUT=out/plc SCORE=plat NMAX=56 DMAX=3 RESUME=1 python3 plc235.py platMWR 2352 3000 "$T"/experiments/new/box203/inst/MWR4_2.json || exit 1
fi
echo DONE
