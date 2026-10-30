#!/usr/bin/env python3
"""L-RED successor 30: add one observer vertex x (no in-edges, priority 0 renumbered below everything: all priorities + 1... no:
x gets priority 0 and every original priority is shifted by +2, which keeps parities and the relative order) with edges to a vertex set Y.
OWNER = 0 (Even observer) or 1 (Odd observer); Y = 'all' | 'even' | 'odd' | comma list. Writes GAME and START (START = original start,
plus x -> its first successor). Usage: observe.py IN.pg IN.start OWNER Y OUT.pg OUT.start"""
import sys
src, sst, own, Y, out, ost = sys.argv[1:7]; own = int(own)
rows = []
for line in open(src):
    line = line.strip().rstrip(";")
    if not line or line.startswith("parity"): continue
    p = line.split(); v, pr, ow = int(p[0]), int(p[1]), int(p[2]); su = [int(a) for a in p[3].split(",")]
    rows.append((v, pr + 2, ow, su))
n = len(rows)
if Y == "all": ys = list(range(n))
elif Y == "even": ys = [v for v, _, ow, _ in rows if ow == 0]
elif Y == "odd": ys = [v for v, _, ow, _ in rows if ow == 1]
else: ys = [int(a) for a in Y.split(",")]
rows.append((n, 0, own, ys))
with open(out, "w") as f:
    f.write(f"parity {n};\n")
    for v, pr, ow, su in rows: f.write(f"{v} {pr} {ow} {','.join(map(str, su))};\n")
lines = [l.rstrip("\n") for l in open(sst)]
with open(ost, "w") as f:
    for l in lines:
        if own == 0 and l.startswith("SIGMA0"): l += f" {n}:{ys[0]}"
        if own == 1 and l.startswith("TAU0"): l += f" {n}:{ys[0]}"
        f.write(l + "\n")
