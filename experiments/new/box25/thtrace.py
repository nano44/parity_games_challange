#!/usr/bin/env python3
"""Box 25: per-state trace on a C^1O game: θ = Ξ(o) (rank-free), σ̄(o), τ(o), w = W(o), R (σ-path reaches o), exits' Ξ, trust set
T = {z in R, Even: some successor y ∉ R with Ξ(y) ▷ Ξ(σ(z))} (honest-improving edge leaving R, refused by the selection).
Usage: thtrace.py game.pg [start]"""
from common import *
def Rset(g, s, t, o):
    n = g.n; nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]; R = set()
    for v in range(n):
        x, seen = v, set()
        while x not in seen and x != o: seen.add(x); x = nxt[x]
        if x == o: R.add(v)
    return R
if __name__ == "__main__":
    g = load(sys.argv[1]); s0 = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; st, _ = trace(g, s0)
    o = odd_choice(g); E = Engine(g)
    for k, (s, t) in enumerate(st):
        Xi, sb = E.evaluate(s); _, W = wvals(g, s, t); R = Rset(g, s, t, o)
        Is = E.improving(s, Xi); T = sorted({v for v, w in Is if v in R and w not in R})
        th = vset(E, Xi[o]); w = vset(E, W[o])
        print(f"{k:2d} τ(o)={t[o]} σ̄(o)={sb[o]} θ=({th[0]},{sorted(th[1])},{th[2]}) w=({w[0]},{sorted(w[1])},{w[2]}) R={sorted(R)} T={T} σ={list(s)}")
