#!/usr/bin/env python3
"""L-SI box 7 (fixes file, ENG-1): at every state of every N5 run, the engine's Ξ = Engine.evaluate(σ)[0] equals the VJ00 play value
Θ_{σ σ̄} of the (σ, σ̄)-graph (σ̄ = the engine's counterstrategy), computed independently by walking the lasso. Also counts the Odd
vertices u where σ̄(u) is not a ⊴-minimiser of Ξ over succ(u), split by whether u is a cycle node (λ(u) = u).
Usage: eng1.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mono import *

def playval(E, g, s, sb, v):
    nxt = lambda u: s[u] if g.owner[u] == 0 else sb[u]
    seq = [v]; seen = {v: 0}
    while True:
        u = nxt(seq[-1])
        if u in seen: break
        seen[u] = len(seq); seq.append(u)
    cyc = seq[seen[u]:]; c = max(cyc, key=lambda x: E.rank[x]); pre = seq[:seq.index(c)]
    mask = 0
    for x in pre:
        if E.rank[x] > E.rank[c]: mask |= E.bit[x]
    return (c, mask, len(pre))

if __name__ == "__main__":
    T = dict(states=0, vals=0, mismatch=0, odd=0, nonmin_cn=0, nonmin_other=0)
    for p in sys.argv[1:]:
        g = load(p); E, out = states(g)
        for a in out:
            T["states"] += 1
            for v in range(g.n):
                T["vals"] += 1
                if playval(E, g, a["s"], a["sb"], v) != tuple(a["Xi"][v]): T["mismatch"] += 1
                if g.owner[v] == 1 and len(set(g.succ[v])) > 1:
                    T["odd"] += 1
                    if E.key(a["Xi"][a["sb"][v]]) > min(E.key(a["Xi"][w]) for w in g.succ[v]):
                        T["nonmin_cn" if a["Xi"][v][0] == v else "nonmin_other"] += 1
    print(T)
