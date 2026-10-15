#!/usr/bin/env python3
"""L-ALG (2026-10-15, DTL step 4, GAP-A data): per-top tangle counts from a DEBUG Oink trace (-t -t prints every new
tangle with its vertices and strategy). The top of a tangle learned by sptl is its maximum-priority vertex (ties: any).
Usage: dtl_pertop.py DEBUG_OINK GAME.pg  -> prints #tangles, #iterations, max tangles at one top, histogram of per-top counts,
and the number of distinct (vertex set) tangles per top sharing the same vertex set size."""
import sys, re, subprocess, collections
oink, game = sys.argv[1], sys.argv[2]
r = subprocess.run([oink, "--dtl", "-t", "-t", "--no-single", "--no-wcwc", game], capture_output=True, text=True, timeout=600)
out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
pr = {}
for line in open(game):
    if line.startswith("parity"): continue
    f = line.split()
    if len(f) >= 3 and f[0].isdigit(): pr[f[0]] = int(f[1])
per_top = collections.Counter(); tangles = 0; its = 0; doms = 0
for line in out.splitlines():
    if "iteration" in line and "-even" in line or "-odd" in line: its += 1
    m = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
    if m:
        tangles += 1
        verts = [tok.split("->")[0] for tok in m.group(4).split()]
        # vertex labels are indices after Oink's reindexing; the trace priority (group 1) is the region's top priority
        per_top[(m.group(1), max(verts, key=lambda v: int(v) if v.isdigit() else 0))] += 1
    if "dominion" in line and "depth" in line: doms += 1
hist = collections.Counter(per_top.values())
print(f"{game}: tangles {tangles}, dominions {doms}, iterations {its}, tops {len(per_top)}, max per top {max(per_top.values()) if per_top else 0}, hist {dict(sorted(hist.items()))}")
