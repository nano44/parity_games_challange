#!/usr/bin/env python3
"""L-SI box 73: exact enumeration of the box 70 frame at m = 2 (every acyclic ISO Xi-graph on the 4 upper movers, every improvement
table C satisfying the frame's three constraints: C_z independent of s_z, LOCAL, IM (box 69); key bits c_1(0), c_1(1)).
Movers 0 = A1, 1 = B1 (level 1), 2 = A2, 3 = B2 (level 2). Output: tables.txt = one distinct table per line as 4 x 16-bit hex
(bit s of word z = C_z(s)); same semantics as frame.py (the frame's clause set, enumerated instead of solved)."""
import itertools, sys
U = 4; NS = 16
def chains(xt, z, k, s):
    out = []; t = xt[2 * z + k]
    while t != -1: out.append(t); t = xt[2 * t + ((s >> t) & 1)]
    return out
def acyclic(xt):
    adj = {z: {xt[2 * z], xt[2 * z + 1]} - {-1} for z in range(U)}
    col = {}
    def dfs(z):
        col[z] = 1
        for y in adj[z]:
            if col.get(y) == 1 or (y not in col and not dfs(y)): return False
        col[z] = 2; return True
    return all(z in col or dfs(z) for z in range(U)), adj
def topo(adj):
    order, seen = [], set()
    def go(z):
        if z in seen: return
        seen.add(z); [go(y) for y in adj[z]]; order.append(z)
    [go(z) for z in range(U)]; return order          # descendants first
tables = set(); ng = 0
for xt in itertools.product(*[[-1] + [y for y in range(U) if y != o // 2] for o in range(2 * U)]):
    ok, adj = acyclic(xt)
    if not ok: continue
    ng += 1
    on = {(z, k, s): set(chains(xt, z, k, s)) for z in range(U) for k in (0, 1) for s in range(NS)}
    cands = {}
    order = topo(adj)
    def ok_z(z, f, tab):
        for s in range(NS):
            a = (f >> s) & 1
            if (f >> (s ^ (1 << z))) & 1 != a: return False
            for y in range(U):
                if y == z: continue
                b = (f >> (s ^ (1 << y))) & 1; o0, o1 = y in on[(z, 0, s)], y in on[(z, 1, s)]
                if not o0 and not o1:
                    if a != b: return False
                    continue
                if y not in tab: continue                 # y not a descendant: cannot be on a chain (acyclic) -> handled above
                u = ((tab[y] >> s) & 1) != ((s >> y) & 1)  # y unhappy at s
                if not u: continue
                if o0 and o1 and a != b: return False
                if o1 and not o0 and (b, a) == (0, 1): return False   # only toward 1
                if o0 and not o1 and (b, a) == (1, 0): return False   # only toward 0
        return True
    def rec(i, tab):
        if i == U:
            tables.add(tuple(tab[z] for z in range(U))); return
        z = order[i]
        for f in range(1 << NS):
            pass
    # per-mover candidate generation: C_z is a function of the 3 other states (8 values), lifted to 16
    others = {z: [y for y in range(U) if y != z] for z in range(U)}
    lift = {}
    for z in range(U):
        L = []
        for g in range(256):
            f = 0
            for s in range(NS):
                idx = sum(((s >> y) & 1) << j for j, y in enumerate(others[z]))
                if (g >> idx) & 1: f |= 1 << s
            L.append(f)
        lift[z] = L
    def rec2(i, tab):
        if i == U:
            tables.add(tuple(tab[z] for z in range(U))); return
        z = order[i]
        for f in lift[z]:
            if ok_z(z, f, tab):
                tab[z] = f; rec2(i + 1, tab); del tab[z]
    rec2(0, {})
print("graphs", ng, "tables", len(tables), file=sys.stderr)
with open("tables.txt", "w") as fo:
    for t in sorted(tables): fo.write(" ".join("%04x" % w for w in t) + "\n")
