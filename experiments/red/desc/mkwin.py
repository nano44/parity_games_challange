#!/usr/bin/env python3
"""L-RED successor 38 (R162): windowed passive observers on an obs2 game. For s = 1 .. m - W + 1 adds an Even vertex o_s (priority 0,
no in-edges) with successors y_s .. y_(s+W-1) (obs2's y_j -> r_j), start choice y_s. A window observer meets the h-wave only at its own
reactors, so (READING) its round has: a change at a ladder digit when its first reactor flips, then an ASCENT per later reactor; the
DESCENT falls at the flip of r_(s+1), a different transition for each s. The o_s reach only the y_j: the run on the rest is unchanged.
W = 0 gives SUFFIX observers o_s -> y_s .. y_m, s = 1 .. m - 1 (an observer jumps back to y_s at the ladder change and descends at the
next flip). Usage: mkwin.py IN.pg IN.start W OUT.pg OUT.start"""
import sys, re
src, sst, W, out, ost = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5]
rows = []; lab = {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if m: rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4), m.group(5) or ""]); lab[m.group(5)] = int(m.group(1))
y = sorted((int(l[1:]), v) for l, v in lab.items() if l and re.fullmatch(r"y\d+", l)); m = len(y); n = len(rows); add = []
for s in range(m - W + 1 if W else m - 1):
    w = W if W else m - s
    add.append((n + len(add), ",".join(str(y[s + i][1]) for i in range(w)), f"ow{y[s][0]}", y[s][1]))
with open(out, "w") as f:
    f.write(f"parity {n + len(add) - 1};\n")
    for v, p, w, su, l in rows: f.write(f'{v} {p} {w} {su} "{l}";\n')
    for v, su, l, _ in add: f.write(f'{v} 0 0 {su} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        l = l.rstrip("\n")
        if l.startswith("SIGMA0"): l += "".join(f" {v}:{c}" for v, _, _, c in add)
        f.write(l + "\n")
print(f"mkwin: n {n + len(add)} windows {len(add)} width {W}")
