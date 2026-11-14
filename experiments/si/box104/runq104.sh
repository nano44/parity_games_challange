#!/usr/bin/env bash
# L-SI box 104, Addendum B probe: glo104.py (N5 on a guided wrapper against the globally optimal improvement step). Output out/glo104.out.
# Engines read-only by git archive (as rung104.sh). About 10 min, one core.
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out "$T/red" "$T/new" "$T/lit"
TOP=${TOP:-$(git rev-parse --show-toplevel)}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second experiments/friedmann-hn | tar -x -C "$T/new" || exit 3
git -C "$TOP" archive 5c53efbd2d8401dc056e575fa42e49b50a265a0c docs/lit/T66-depth-check.py | tar -x -C "$T/lit" || exit 3
export LNEW="$T/new" LRED="$T/red" LLIT="$T/lit" HN="$T/new/experiments/friedmann-hn"
python3 -I glo104.py lmcs emul 1 2 3 4 5 6 > out/glo104.out || exit 1
python3 -I glo104.py lmcs plain 1 2 3 4 >> out/glo104.out || exit 1
python3 -I glo104.py rand1p 1045 300 12 >> out/glo104.out || exit 1
python3 -I glo104.py rand1p 1046 100 24 >> out/glo104.out || exit 1
python3 -I glo104.py hn e e d1 1 1 2 3 >> out/glo104.out || exit 1
python3 -I glo104.py hn e h d1 1 1 2 3 >> out/glo104.out || exit 1
echo DONE
