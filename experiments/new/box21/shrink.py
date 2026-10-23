#!/usr/bin/env python3
"""Box 21: greedy shrink of a game while the frozen-tau* phase excess stays: keep a change iff
(max N5 iterations in one joint λ-phase from (sigma_0, tau*)) - (n - 1) does not drop below TARGET.
Moves: drop an edge (out-degree > 1); delete a vertex (redirect its in-edges to its first successor; renumber).
Usage: shrink.py in.pg out.pg TARGET"""
import sys
from n5x import *
from climb_fix import fit_tstarph
def tolist(g): return [list(g.prio), list(g.owner), [list(s) for s in g.succ]]
def excess(G):
    try: return fit_tstarph(G) - (len(G[0]) - 1)
    except Exception: return -10 ** 9
def delvert(G, v):
    prio, owner, succ = G; n = len(prio); tgt = next((w for w in succ[v] if w != v), None)
    if tgt is None: return None
    m = lambda w: w if w < v else w - 1
    ns = []
    for u in range(n):
        if u == v: continue
        s = sorted({m(tgt if w == v else w) for w in succ[u]}); ns.append(s)
    return [prio[:v] + prio[v + 1:], owner[:v] + owner[v + 1:], ns]
def write(G, path):
    n = len(G[0])
    with open(path, "w") as f:
        f.write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))
if __name__ == "__main__":
    G = tolist(load(sys.argv[1])); T = int(sys.argv[3]); print("start excess", excess(G), "n", len(G[0]), flush=True)
    changed = True
    while changed:
        changed = False
        for v in range(len(G[0])):
            H = delvert(G, v)
            if H and excess(H) >= T: G = H; changed = True; print("del vertex ->", len(G[0]), excess(G), flush=True); break
        if changed: continue
        for v in range(len(G[0])):
            for w in list(G[2][v]):
                if len(G[2][v]) > 1:
                    H = [G[0], G[1], [list(s) for s in G[2]]]; H[2][v].remove(w)
                    if excess(H) >= T: G = H; changed = True; break
            if changed: break
    write(G, sys.argv[2]); print("final n", len(G[0]), "edges", sum(map(len, G[2])), "excess", excess(G))
