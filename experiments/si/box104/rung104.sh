#!/usr/bin/env bash
# L-SI box 104, Addendum A probe: N5 (SPEC) and N5'-xi on the guided wrappers of Friedmann's games (guide104.py). DATA only.
# Engines read-only by git archive: claude/l-new fcba92fc (experiments/new, si.py, harness, hard-families, n5-second, friedmann-hn),
# claude/l-red 8c01d40e (r217), claude/l-lit 5c53efbd (T66-depth-check.py). Output out/guide104.out. About 5 min, one core.
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
python3 -I guide104.py hn opt 1 2 3 4 5 6 > out/guide104.out || exit 1
python3 -I guide104.py lmcs opt 1 2 3 4 5 >> out/guide104.out || exit 1
python3 -I guide104.py fried opt 2 3 4 5 >> out/guide104.out || exit 1
ALG=xi python3 -I guide104.py hn opt 1 2 3 >> out/guide104.out || exit 1
ALG=xi python3 -I guide104.py lmcs opt 1 2 3 >> out/guide104.out || exit 1
CORE=low python3 -I guide104.py hn opt 1 2 3 >> out/guide104.out || exit 1
echo DONE
