#!/usr/bin/env python3
"""L-RED successor 38 (R162): add C passive copies of the Even observer "obs" (same successors y_1..y_m, priority 0, no in-edges,
same start choice). The copies reach only the y_j, so the sigma/tau run on the rest is unchanged; each copy is one more vertex.
Usage: mkcopy.py IN.pg IN.start C OUT.pg OUT.start"""
import sys, re
src, sst, C, out, ost = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5]
rows = []
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if m: rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4), m.group(5) or ""])
o = next(r for r in rows if r[4] == "obs"); n = len(rows)
for c in range(C): rows.append([n + c, o[1], o[2], o[3], f"obs_c{c}"])
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, p, w, su, l in rows: f.write(f'{v} {p} {w} {su} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        l = l.rstrip("\n")
        if l.startswith("SIGMA0"):
            ch = dict(t.split(":") for t in l.split()[1:])[str(o[0])]
            l += "".join(f" {n + c}:{ch}" for c in range(C))
        f.write(l + "\n")
print(f"mkcopy: n {len(rows)} copies {C} of obs={o[0]}")
