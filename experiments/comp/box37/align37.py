#!/usr/bin/env python3
"""L-COMP box 37: align two genomes A -> B (B = A + inserted movers + option edits), by DP over mover order (ADD-mover keeps the
relative order of the old movers). Match cost = differences of (lev, #opts) + 0.1 per differing mapped option field after a
first pass. Prints: inserted movers of B, and per mapped mover the option-level edits (wt, xt mapped; gate rank order and br rank order
compared as relative orders among mapped options). Usage: align37.py A.json B.json [names.json for A]"""
import sys, json
A, B = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
names = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else None
inv = {v: k for k, v in names.items()} if names else {}
def nm(x): return inv.get(x, str(x))
def sig(G, x): return (G["lev"][x], len(G["opts"][x]))
def align(mapf):
    nA, nB = A["N"], B["N"]; INF = 10 ** 9
    D = [[INF] * (nB + 1) for _ in range(nA + 1)]; D[0] = list(range(nB + 1)); P = {}
    for i in range(1, nA + 1):
        for j in range(i, nB + 1):
            c1 = D[i][j - 1] + 1  # B mover j-1 inserted
            c2 = D[i - 1][j - 1] + mapf(i - 1, j - 1)
            D[i][j], P[i, j] = (c2, 0) if c2 <= c1 else (c1, 1)
    m = {}; i, j = nA, nB
    while i > 0:
        if P[i, j] == 0: m[i - 1] = j - 1; i -= 1; j -= 1
        else: j -= 1
    return m
m = align(lambda x, y: 3 * (sig(A, x) != sig(B, y)))
for it in range(3):
    def cost(x, y, m=m):
        c = 3 * (A["lev"][x] != B["lev"][y]) + 2 * (len(A["opts"][x]) != len(B["opts"][y]))
        for oa, ob in zip(A["opts"][x], B["opts"][y]):
            for f in (0, 1):
                c += 0.5 * ((m.get(oa[f], -9) if oa[f] >= 0 else -1) != ob[f])
        return c
    m = align(cost)
ins = sorted(set(range(B["N"])) - set(m.values()))
mi = {v: k for k, v in m.items()}
def bn(y): return nm(mi[y]) if y in mi else (f"NEW{y}" if y >= 0 else "-")
print("A N", A["N"], "B N", B["N"], "inserted:", [(y, B["lev"][y], [[bn(o[0]), bn(o[1])] for o in B["opts"][y]]) for y in ins])
# options: global option list with (owner name, k)
def olist(G, own):
    L = []
    for x in range(G["N"]):
        for k, o in enumerate(G["opts"][x]): L.append((own(x), k, o, G["gate"][x][k], G["br"][o[2]], G["bp"][o[2]], G["start"][x] == k))
    return L
LA = olist(A, nm); LB = olist(B, bn)
for x in range(A["N"]):
    y = m[x]; oa, ob = A["opts"][x], B["opts"][y]
    ea = [[nm(o[0]) if o[0] >= 0 else "-", nm(o[1]) if o[1] >= 0 else "-", A["bp"][o[2]]] for o in oa]
    eb = [[bn(o[0]), bn(o[1]), B["bp"][o[2]]] for o in ob]
    sa, sb = A["start"][x], B["start"][y]
    if ea != eb or (len(oa) > 1 and sa != sb): print("EDIT", nm(x), "->B", y, ea, "start", sa, "=>", eb, "start", sb)
# relative gate order / br order of mapped options
key = lambda t: (t[0], t[1])
ga = sorted([t for t in LA], key=lambda t: t[3]); gb = sorted([t for t in LB], key=lambda t: t[3])
ra = [key(t) for t in ga]; rb = [key(t) for t in gb if key(t) in set(ra)]
print("gate order of common options equal:", [k for k in ra if k in set(rb)] == rb)
if [k for k in ra if k in set(rb)] != rb:
    pa = {k: i for i, k in enumerate(k for k in ra if k in set(rb))}
    print("  gate order moves:", [(k, pa[k], i) for i, k in enumerate(rb) if pa[k] != i][:20])
ba = sorted(LA, key=lambda t: t[4]); bb = sorted(LB, key=lambda t: t[4])
ra = [key(t) for t in ba]; rb = [key(t) for t in bb if key(t) in set(ra)]
cm = [k for k in ra if k in set(rb)]
print("br order of common options equal:", cm == rb)
if cm != rb:
    pa = {k: i for i, k in enumerate(cm)}; print("  br order moves:", [(k, pa[k], i) for i, k in enumerate(rb) if pa[k] != i][:20])
newo = [key(t) for t in LB if (t[0], t[1]) not in set(key(u) for u in LA)]
print("new options (owner, k):", newo, " gate ranks:", [(key(t), t[3]) for t in LB if key(t) in set(newo)])
if len(sys.argv) > 4:
    json.dump({bn(y): y for y in range(B["N"])}, open(sys.argv[4], "w"))
