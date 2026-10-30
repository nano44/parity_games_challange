#!/usr/bin/env python3
"""L-RED successor 33 (R137): TWO interleaved Even wave observers + a chooser X (FREE returns at one edge). Derived from mix/obs2.py (R120):
O1 reads the odd reactors, O2 the even ones (y_j as in R120); X (Even, prio 0) -> {O1, O2}. Original R120 docstring follows.
R120: wave observer on an mkr game (seg/mkr.py). Adds an Odd observer o (priority 0, no in-edges) with edges
to y_1..y_m, y_j (Odd, single successor) -> r_j (mkr's reactor j, label "r<j>"), y_j priority q_j = Z - 1 + 2j (even, just above z's
priority Z; every original priority > Z is shifted by 2m + 2, which keeps parities and the order). Xi(o) = Odd's minimum over
{q_j} + Xi(r_j): while a wave runs down the chain, the argmin is the next unflipped reactor. o and the y_j reach no other vertex,
so the sigma-run is unchanged. Env: OWNER=0 makes o Even; ABOVE=a puts the q_j just above the reactor a-markers
(instead of just above z); TARGET=1 adds an Even e -> {o, d} that switches to o once. Usage: obs2.py IN.pg IN.start OUT.pg OUT.start"""
import sys, re
src, sst, out, ost = sys.argv[1:5]
rows = []; lab = {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if not m: continue
    v, pr, ow = int(m.group(1)), int(m.group(2)), int(m.group(3)); su = [int(a) for a in m.group(4).split(",")]
    rows.append([v, pr, ow, su, m.group(5) or ""]); lab[m.group(5)] = v
Z = rows[lab["z"]][1]
import os
BLK = int(os.environ.get("BLK", "1"))                         # R137: O1 reads reactor blocks 1..BLK, 2BLK+1.., O2 the others
OWN = int(os.environ.get("OWNER", "1"))                       # OWNER=0: Even observer (R120 §3)
if os.environ.get("ABOVE") == "a": Z = max(r[1] for r in rows if re.fullmatch(r"a\d+", r[4]))   # q_j just above the a-markers
reac = sorted((int(l[1:]), v) for l, v in lab.items() if l and re.fullmatch(r"r\d+", l)); m = len(reac)
for r in rows:
    if r[1] > Z: r[1] += 2 * m + 2
n = len(rows); o = n; o2 = n + 1 + m; X = o2 + 1
rows.append([o, 0, OWN, [n + 1 + k for k, (j, rv) in enumerate(reac) if ((j - 1) // BLK) % 2 == 0], "obs"])
for k, (j, rv) in enumerate(reac):
    rows.append([n + 1 + k, Z - 1 + 2 * j, 1, [rv], f"y{j}"])
rows.append([o2, 0, OWN, [n + 1 + k for k, (j, rv) in enumerate(reac) if ((j - 1) // BLK) % 2 == 1], "obs2"])
rows.append([X, 0, 0, [o, o2], "X"])
TGT = os.environ.get("TARGET") == "1"                          # TARGET=1: Even e -> {o, d}, d -> z with a low odd marker: e switches to o
if TGT:                                                        # at the first transition, so o is a target of a switching edge (R121)
    e, d = len(rows), len(rows) + 1
    rows.append([e, 0, 0, [o, d], "e"]); rows.append([d, Z, 1, [lab["z"]], "d"])
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, pr, ow, su, l in rows: f.write(f'{v} {pr} {ow} {",".join(map(str, su))} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        l = l.rstrip("\n")
        if l.startswith("TAU0"): l += (f" {o}:{n + 1}" if OWN == 1 else "") + "".join(f" {n + 1 + k}:{rv}" for k, (j, rv) in enumerate(reac))
        if l.startswith("SIGMA0") and OWN == 0: l += f" {o}:{rows[o][3][0]} {o2}:{rows[o2][3][0]}"
        if l.startswith("SIGMA0"): l += f" {X}:{o}"
        if l.startswith("SIGMA0") and TGT: l += f" {e}:{d}"
        if l.startswith("TAU0") and TGT: l += f" {d}:{lab['z']}"
        f.write(l + "\n")
print(f"obs2: n {len(rows)} m_reactors {m} Z {Z}")
