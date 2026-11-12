#!/usr/bin/env bash
# L-SI box 104, Addendum B probe: the gate-face scan of gscan104.py on H_n, n = 1..4, ten variants. Output out/gscan104.out.
# Engines read-only by git archive (as rung104.sh). About 8 min, one core.
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
: > out/gscan104.out
for c in "e e d1 1" "e h d1 1" "h e d1 1" "h h d1 1" "e e h 1" "e d1 h 1" "h d1 d1 1" "e d1 d1 0" "h d1 d1 0" "e h h 1"; do
  python3 -I gscan104.py $c 1 2 3 4 >> out/gscan104.out || exit 1
done
echo DONE
