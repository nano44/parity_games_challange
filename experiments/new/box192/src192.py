#!/usr/bin/env python3
"""Box 192: SRC-DEC data. At every state and every gate g whose faces share a cycle node w (equal-Lambda) and with sigma-bar(g) = e,
whose MERGE pre-merge segments have a vertex above w, the decisive vertex z (MERGE) is classified: the e-vertex of a SOURCE gate
(faces with different cycle nodes), the e-vertex of another equal-Lambda gate, or other (not an e-vertex). Usage: src192.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192, idealcyc
from mtype192 import play
def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    hh, s0, mv, inv = idealcyc.build(G); st = idealcyc.run(G); gi = {}
    for x in range(G["N"]):
        for v in hh.succ[mv[x]]: gi[(x, inv[v])] = v
    gates = [v for v in range(h.n) if h.owner[v] == 1 and name[v][0] == "g"]
    egate = {V[("e", name[g][1])]: g for g in gates}
    cnt = {"eqD": 0, "srcdec": 0, "eqdec": 0, "other": 0}
    for t in range(len(ev)):
        vs, sb = ev[t]; cur = list(s0)
        for x in range(G["N"]): cur[mv[x]] = gi[(x, st[t][x])]
        src = {g for g in gates if vs[V[("e", name[g][1])]][0] != vs[V[("b", name[g][1])]][0]}
        for g in gates:
            q = name[g][1]; e, b = V[("e", q)], V[("b", q)]
            if g in src or sb[g] != e: continue
            w = vs[e][0]
            PA, PB = play(h, cur, sb, e), play(h, cur, sb, b); sPB = set(PB)
            m = next(v for v in PA if v in sPB)
            seg = PA[:PA.index(m)] + PB[:PB.index(m)]
            up = [v for v in seg if E.rank[v] > E.rank[w]]
            if not up: continue
            z = max(up, key=lambda v: E.rank[v]); cnt["eqD"] += 1
            if z in egate: cnt["srcdec" if egate[z] in src else "eqdec"] += 1
            else: cnt["other"] += 1
    return cnt
tot = {}
for f in sys.argv[1:]:
    c = analyse(json.load(open(f)))
    for k, v in c.items(): tot[k] = tot.get(k, 0) + v
    print(os.path.basename(f), c)
print("TOTAL", tot)
