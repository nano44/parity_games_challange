#!/usr/bin/env python3
"""L-COMP box 30: remove ONE level j of a text genome (rclimb format; option m = 2x+k): movers 2j, 2j+1 deleted, movers above renumbered
down by 2 (their W-wiring is by level and option index, so level j+1 now W-points into level j-1); Xi-targets at the removed movers ->
X (-1), others renumbered; ranks renumbered in the old order; gates, parities, start kept. Usage: remlevel.py in.txt j out.txt"""
import sys
D = {}
for ln in open(sys.argv[1]):
    w = ln.split()
    if w and w[0] in ("d", "xt", "br", "bp", "gate", "start"): D[w[0]] = list(map(int, w[1:]))
d = D["d"][0]; j = int(sys.argv[2]); gone = {2 * j, 2 * j + 1}
keepx = [x for x in range(2 * d) if x not in gone]; nx = {x: i for i, x in enumerate(keepx)}
keepm = [m for m in range(4 * d) if m // 2 not in gone]
xt = [(-1 if D["xt"][m] < 0 or D["xt"][m] in gone else nx[D["xt"][m]]) for m in keepm]
br = [D["br"][m] for m in keepm]; srt = sorted(br); br = [srt.index(b) for b in br]
with open(sys.argv[3], "w") as f:
    f.write(f"d {d - 1}\n"); f.write("xt " + " ".join(map(str, xt)) + "\n"); f.write("br " + " ".join(map(str, br)) + "\n")
    for k in ("bp", "gate"): f.write(k + " " + " ".join(str(D[k][m]) for m in keepm) + "\n")
    f.write("start " + " ".join(str(D["start"][x]) for x in keepx) + "\n")
