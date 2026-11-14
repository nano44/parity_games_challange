#!/usr/bin/env python3
"""Box 205 Addendum B (L-NEW successor 69): at each IDEAL-CYC state, the Xi_sigma cycle Z (first found; k = 1: the only one), the parity of
the most relevant beta on its Gamma-cycle, and the exit set (movers x on Z whose gate (x, sigma(x)) is on its e-face). Per run: flips (unit:
gate flips), cycle_changes and exit_changes (unit: steps at which Z, resp. the exit set, changes). Usage: exit205.py G.json ..."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import betaloc205 as B
def cyc(G, s):
    for x0 in range(G["N"]):
        seen = []; x = x0
        while x >= 0 and x not in seen: seen.append(x); x = G["opts"][x][s[x]][1]
        if x >= 0: return tuple(sorted(seen[seen.index(x):]))
    return None
for fn in sys.argv[1:]:
    G = json.load(open(fn)); st = B.idealcyc.run(G, cap=20000); h = B.idealcyc.build(G)[0]
    H, n, E, V, gates = B.gfc203.hist_ideal(G); gv = {q: (v, a, b) for v, (q, a, b) in gates.items()}
    rows = []; flips = 0
    for s in range(len(H)):
        Z = cyc(G, st[s]); par = None; ex = ()
        if Z:
            bs = [gv[(x, st[s][x])][2] for x in Z]; top = max(bs, key=lambda v: h.prio[v]); par = h.prio[top] % 2
            ex = tuple(sorted(x for x in Z if H[s][1][gv[(x, st[s][x])][0]] == gv[(x, st[s][x])][1]))
        rows.append((Z, par, ex))
        if s: flips += sum(H[s-1][1][v] != H[s][1][v] for v in gates)
    zc = sum(rows[s][0] != rows[s-1][0] for s in range(1, len(rows))); ec = sum(rows[s][2] != rows[s-1][2] for s in range(1, len(rows)))
    print(os.path.basename(fn), "T", len(H)-1, "flips", flips, "cycle_changes", zc, "exit_changes", ec, "parities", collections.Counter(r[1] for r in rows), "max_exits", max(len(r[2]) for r in rows))
