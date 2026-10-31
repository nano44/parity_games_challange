#!/usr/bin/env python3
"""L-RED R145 (c): degree-2 version of R120's Odd wave observer. Post-processes mix/obs2.py output (OWNER=1): obs keeps the edges to y_j
with j even, a new Odd sub-observer obs1 (priority 0, appended) takes the y_j with j odd, and a new Odd root (priority 0, appended) has the
two edges {obs, obs1}. The wave's next unflipped reactor alternates parity, so the root's argmin should alternate at every wave step.
Usage: obs3.py IN.pg IN.start OUT.pg OUT.start"""
import sys, re
src, sst, out, ost = sys.argv[1:5]
rows, lab = [], {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if not m: continue
    rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(a) for a in m.group(4).split(",")], m.group(5) or ""])
    lab[m.group(5)] = int(m.group(1))
o = lab["obs"]; ys = rows[o][3]; j = {v: int(rows[v][4][1:]) for v in ys}
ev, od = [v for v in ys if j[v] % 2 == 0], [v for v in ys if j[v] % 2 == 1]
rows[o][3] = ev; n = len(rows)
rows.append([n, 0, 1, od, "obs1"]); rows.append([n + 1, 0, 1, [o, n], "root"])
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n" + "".join(f'{r[0]} {r[1]} {r[2]} {",".join(map(str, r[3]))} "{r[4]}";\n' for r in rows))
lines = open(sst).read().splitlines(); outl = []
for l in lines:
    if l.startswith("TAU0"): l += f" {n}:{od[0]} {n + 1}:{o}"
    outl.append(l)
open(ost, "w").write("\n".join(outl) + "\n")
print(f"obs3: n {len(rows)} even-y {len(ev)} odd-y {len(od)}")
