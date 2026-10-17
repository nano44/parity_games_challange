#!/usr/bin/env bash
# L-RED box 7 (produced on Opus 5.5): pinned-Oink check of a (MEET) failure at the FIRST search (iteration 0-even, G' = G).
# Prints the tangles A_DTL (oink --dtl --no-single --no-wcwc --no-loops) learns in iteration 0-even, mapped to file ids with
# omap (Oink game.cpp:492-495 std::sort reproduced), whether that iteration finds a dominion, and W_0(G) from Oink --zlk
# (verified). MEET FAILS iff W_0 != {}, no dominion in 0-even, and every tangle is disjoint from W_0. Usage: oinkmeet.sh G.pg
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; O="$here/../../../tools/oink/build/oink"; t="$(mktemp -d)"
g++ -O2 -std=c++17 -o "$t/omap" "$here/omap.cpp"
"$t/omap" "$1" > "$t/map"
"$O" --dtl --no-single --no-wcwc --no-loops -v "$1" > "$t/dtl.log" 2>&1
grep -q "solution verified" "$t/dtl.log" || { echo "DTL run NOT verified"; exit 1; }
"$O" --dtl --no-single --no-wcwc --no-loops -t -t -t "$1" 2>&1 | sed 's/\x1b\[[0-9;]*m//g' | awk '/iteration 0-even/{on=1;next} /iteration /{on=0} on' > "$t/it0"
"$O" --zlk -v "$1" "$t/sol" > "$t/zlk.log" 2>&1
grep -q "solution verified" "$t/zlk.log" || { echo "zlk NOT verified"; exit 1; }
python3 -I - "$t/map" "$t/it0" "$t/sol" "$t/dtl.log" <<'PY'
import sys, re
m = {int(a): int(b) for a, b in (l.split() for l in open(sys.argv[1]))}
it0 = open(sys.argv[2]).read(); W0 = set()
for l in open(sys.argv[3]):
    x = re.match(r"^(\d+)\s+([01])\b", l.strip())
    if x and x.group(2) == "0": W0.add(int(x.group(1)))
T = []
for l in it0.splitlines():
    x = re.search(r"new tangle \d+ \(\d+\) \(depth \d+\) (.*) with \d+ escape", l)
    if x: T.append(sorted(m[int(tok.split("/")[0])] for tok in x.group(1).split()))
dom = "dominion" in it0
print(re.search(r"found .*tangles", open(sys.argv[4]).read()).group(0))
print("W_0(G) =", sorted(W0)); print("iteration 0-even: dominion =", dom, "tangles =", T)
fail = bool(W0) and not dom and T and all(not set(c) & W0 for c in T)
print("MEET FAILS at search 0" if fail else "MEET holds at search 0")
PY
rm -rf "$t"
