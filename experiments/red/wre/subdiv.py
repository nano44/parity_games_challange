#!/usr/bin/env python3
"""L-RED successor 38 (R166, W-REOPEN, L-SI box 58 §10): subdivide edge (a, b) by a new FORCED Even vertex e (single successor b).
All priorities are shifted by +2 (order and parity kept) and e gets priority 0, the unique lowest, so e is never the cycle node or in a
path set above one; it only adds 1 to the length of plays through it. Start: e -> b; if sigma/tau(a) = b it becomes e.
Env CHOICE=1: e gets a second successor d, a new Odd vertex with a self-loop at the TOP odd priority (Even never wants it), so e is an
Even vertex WITH a choice that it never takes. Usage: subdiv.py IN.pg IN.start a b OUT.pg OUT.start"""
import sys, re
src, sst, a, b, out, ost = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
rows = []
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if m: rows.append([int(m.group(1)), int(m.group(2)) + 2, int(m.group(3)), [int(x) for x in m.group(4).split(",")], m.group(5) or ""])
e = len(rows); assert b in rows[a][3]
rows[a][3] = [e if x == b else x for x in rows[a][3]]; rows.append([e, 0, 0, [b], f"e{a}_{b}"])
import os
if os.environ.get("CHOICE") == "1":
    top = max(r[1] for r in rows); top += 1 if top % 2 == 0 else 2; d = len(rows)
    rows[e][3] = sorted([b, d]); rows.append([d, top, 1, [d], "dsink"])
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, p, o, su, l in rows: f.write(f'{v} {p} {o} {",".join(map(str, su))} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        t = l.split()
        if not t: continue
        t = [t[0]] + [f"{v}:{e if (int(v) == a and int(w) == b) else w}" for v, w in (x.split(":") for x in t[1:])]
        if t[0] == "SIGMA0": t.append(f"{e}:{b}")
        if t[0] == "TAU0" and os.environ.get("CHOICE") == "1": t.append(f"{len(rows) - 1}:{len(rows) - 1}")
        f.write(" ".join(t) + "\n")
print(f"subdiv: n {len(rows)} e {e} on ({a}, {b})")
