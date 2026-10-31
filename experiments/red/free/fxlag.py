#!/usr/bin/env python3
"""L-RED R142b: fx with LAGGED observer clones, aimed at many STRICT releases of ONE Even edge in ONE frozen-sigma-bar stretch (L-NEW
box 89 CONJECTURE BIP-REL-1). From mkrw K m (span/mkrw.py) as in free/obsx.py (R137), reactor blocks of size BLK (default 2):
  y_j (Odd, even prio q_j just above the a-markers, -> r_j) as in R120 / obs2.py; the y_j are shared.
  O_i (Even, prio 0) -> pa_ij -> pb_ij -> y_j            (observer i reads its blocks, 3 steps to y_j)
  O'_i (Even, prio 0) -> h_ij; h_ij (Odd) -> {qa -> qb -> qc -> y_j (tau), O_i}   (dg-style follower: lags O_i by one iteration)
  g_i (Odd) -> {c1_i -> c2_i -> O_i (tau), O'_i}         (equal lengths 6 to y)
  X (Even, prio 0) -> {g_1, g_2}.
Every padding vertex has priority 0 and one successor. Usage: fxlag.py IN.pg IN.start OUT.pg OUT.start"""
import sys, re, os
src, sst, out, ost = sys.argv[1:5]; BLK = int(os.environ.get("BLK", "2"))
rows = []; lab = {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if not m: continue
    rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(a) for a in m.group(4).split(",")], m.group(5) or ""]); lab[m.group(5)] = int(m.group(1))
Z = max(r[1] for r in rows if re.fullmatch(r"a\d+", r[4]))
reac = sorted((int(l[1:]), v) for l, v in lab.items() if l and re.fullmatch(r"r\d+", l)); m = len(reac)
for r in rows:
    if r[1] > Z: r[1] += 2 * m + 2
sig, tau = {}, {}
def add(name, pr, ow, su):
    v = len(rows); rows.append([v, pr, ow, su, name]); return v
def pad(name, target): return add(name, 0, 1, [target])
y = {j: add(f"y{j}", Z - 1 + 2 * j, 1, [rv]) for j, rv in reac}
for j in y: tau[y[j]] = rows[y[j]][3][0]
blocks = {1: [j for j, _ in reac if ((j - 1) // BLK) % 2 == 0], 2: [j for j, _ in reac if ((j - 1) // BLK) % 2 == 1]}
O, Op, G = {}, {}, {}
for i in (1, 2):
    O[i] = add(f"O{i}", 0, 0, []); Op[i] = add(f"Op{i}", 0, 0, [])
    for j in blocks[i]:
        pb = pad(f"pb{i}_{j}", y[j]); pa = pad(f"pa{i}_{j}", pb); rows[O[i]][3].append(pa)
        qc = pad(f"qc{i}_{j}", y[j]); qb = pad(f"qb{i}_{j}", qc); qa = pad(f"qa{i}_{j}", qb)
        h = add(f"h{i}_{j}", 0, 1, [qa, O[i]]); tau[h] = qa; rows[Op[i]][3].append(h)
        for p in (pa, pb, qa, qb, qc): tau[p] = rows[p][3][0]
    sig[O[i]] = rows[O[i]][3][0]; sig[Op[i]] = rows[Op[i]][3][0]
    c2 = pad(f"c2_{i}", O[i]); c1 = pad(f"c1_{i}", c2); tau[c1] = c2; tau[c2] = O[i]
    G[i] = add(f"g{i}", 0, 1, [c1, Op[i]]); tau[G[i]] = c1
X = add("X", 0, 0, [G[1], G[2]]); sig[X] = G[1]
with open(out, "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, pr, ow, su, l in rows: f.write(f'{v} {pr} {ow} {",".join(map(str, su))} "{l}";\n')
with open(ost, "w") as f:
    for l in open(sst):
        l = l.rstrip("\n")
        if l.startswith("SIGMA0"): l += "".join(f" {v}:{w}" for v, w in sig.items())
        if l.startswith("TAU0"): l += "".join(f" {v}:{w}" for v, w in tau.items())
        f.write(l + "\n")
print(f"fxlag: n {len(rows)} reactors {m} blocks {blocks}")
