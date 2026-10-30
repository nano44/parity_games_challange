#!/usr/bin/env python3
"""L-RED R148: add N passive clones of Even vertex X: same priority (ties broken by index, SPEC A1), same successors, no in-edges, start
sigma0 = X's. A clone changes no other vertex's play, so the (sigma, tau)-run on the original vertices is unchanged (checked by the caller
against the original trace). START "-" = no start file (default start; a clone's default equals X's, same successors and priority class).
X may be a comma list x1,x2,...: N clones of each, appended in that order (the start file then only for a single X).
Usage: clone.py IN.pg IN.start|- X[,X2,...] N OUT.pg OUT.start|-"""
import sys, re
src, sst, XS, N, out, ost = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")], int(sys.argv[4]), sys.argv[5], sys.argv[6]
X = XS[0]
rows = []
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if m: rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4), m.group(5)])
rows.sort(); n = len(rows)
for X in XS:
    assert rows[X][2] == 0, "X must be Even"
    for i in range(N): rows.append([len(rows), rows[X][1], 0, rows[X][3], f"clone{i}" if len(XS) == 1 else f"clone{X}_{i}"])
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, p, o, s, lab in rows: f.write(f"{v} {p} {o} {s}" + (f' "{lab}"' if lab else "") + ";\n")
if sst == "-": sys.exit(0)
lines = open(sst).read().splitlines(); sx = None
for l in lines:
    if l.startswith("SIGMA0"):
        for p in l.split()[1:]:
            a, b = p.split(":")
            if int(a) == X: sx = b
with open(ost, "w") as f:
    for l in lines:
        if l.startswith("SIGMA0"): l = l + "".join(f" {n + i}:{sx}" for i in range(N))
        f.write(l + "\n")
