#!/usr/bin/env python3
"""L-SI box 103: list every mover Pi-change of e-depth > 1 (whole run) with z, gained / lost e-vertices and the movers that switch at that
step. Engine as mdeep103.py (env RED, LNEW). Usage: wcdeep103.py G.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["RED"], "experiments/red/r232"))
import how3_232 as H
G = json.load(open(sys.argv[1])); G = G.get("genome", G); G.pop("_evals", None)
full = []; seq = H.how3(G, full=full); V = full[0][2]; inv = {v: k for k, v in V.items()}
gm = H.build(G)[0]; rk = H.own.VJ(gm.prio).rk
isE = lambda u: isinstance(inv.get(u), tuple) and inv[u][0] == "e"
cs, comp, succ = H.sccs(G)
print("T3", len(seq) - 1, "N", G["N"], "SCC sizes", sorted(len(c) for c in cs if len(c) > 1))
for y in range(G["N"]):
    X = V[("x", y)]
    for t in range(len(full) - 1):
        va, vb = full[t][0][X], full[t + 1][0][X]
        if va == vb or va[0] != vb[0]: continue
        D = va[1] ^ vb[1]
        if not D: continue
        z = max(D, key=lambda u: rk[u]); d = sum(1 for u in va[1] if isE(u) and rk[u] > rk[z])
        if d > 1:
            print("mover", y, "t", t, "Lam", inv[va[0]], "z", inv[z], "gained" if z in vb[1] else "lost", "e-depth", d,
                  "| movers switching t->t+1:", [x for x in range(G["N"]) if seq[t + 1][x] != seq[t][x]])
            print("   lost e:", sorted(inv[u][1] for u in va[1] - vb[1] if isE(u)), " gained e:", sorted(inv[u][1] for u in vb[1] - va[1] if isE(u)))
