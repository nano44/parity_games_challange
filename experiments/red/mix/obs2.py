#!/usr/bin/env python3
"""L-RED successor 30 (R120): wave observer on an mkr game (seg/mkr.py). Adds an Odd observer o (priority 0, no in-edges) with edges
to y_1..y_m, y_j (Odd, single successor) -> r_j (mkr's reactor j, label "r<j>"), y_j priority q_j = Z - 1 + 2j (even, just above z's
priority Z; every original priority > Z is shifted by 2m + 2, which keeps parities and the order). Xi(o) = Odd's minimum over
{q_j} + Xi(r_j): while a wave runs down the chain, the argmin is the next unflipped reactor. o and the y_j reach no other vertex,
so the sigma-run is unchanged. Usage: obs2.py IN.pg IN.start OUT.pg OUT.start"""
import sys, re
src, sst, out, ost = sys.argv[1:5]
rows = []; lab = {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if not m: continue
    v, pr, ow = int(m.group(1)), int(m.group(2)), int(m.group(3)); su = [int(a) for a in m.group(4).split(",")]
    rows.append([v, pr, ow, su, m.group(5) or ""]); lab[m.group(5)] = v
Z = rows[lab["z"]][1]; reac = sorted((int(l[1:]), v) for l, v in lab.items() if l and re.fullmatch(r"r\d+", l)); m = len(reac)
for r in rows:
    if r[1] > Z: r[1] += 2 * m + 2
n = len(rows); o = n
rows.append([o, 0, 1, [n + 1 + k for k in range(m)], "obs"])
for k, (j, rv) in enumerate(reac):
    rows.append([n + 1 + k, Z - 1 + 2 * j, 1, [rv], f"y{j}"])
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, pr, ow, su, l in rows: f.write(f'{v} {pr} {ow} {",".join(map(str, su))} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        l = l.rstrip("\n")
        if l.startswith("TAU0"): l += f" {o}:{n + 1}" + "".join(f" {n + 1 + k}:{rv}" for k, (j, rv) in enumerate(reac))
        f.write(l + "\n")
print(f"obs2: n {len(rows)} m_reactors {m} Z {Z}")
