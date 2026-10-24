#!/usr/bin/env python3
"""Box 22: invariant I1 (Lemma P in G_τ for W, restarted at each (θ, w, τ, λ)-stretch) on given C^1O instances (canonical run).
Usage: i1inst.py game.pg [maxk]"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
from stretchP import back_paths, pathval
def main(path, maxk=10 ** 9):
    g = load(path); E = Engine(g); n = g.n
    o = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
    st, _ = trace(g); key = []
    for s, t in st:
        X, _ = E.evaluate(s); key.append((X[o], wvals(g, s, t)[1][o], t, tuple(x[0] for x in X)))
    k0 = 0; checks = viol = 0; longest = 0
    for k in range(1, len(st)):
        if key[k] != key[k0]: k0 = k; continue
        j = k - k0; longest = max(longest, j); s, t = st[k]; s0 = st[k0][0]
        Eg, W = wvals(g, s, t); _, W0 = wvals(g, s0, t)
        succT = [g.succ[v] if g.owner[v] == 0 else [t[v]] for v in range(n)]
        for u in {w[0] for w in W0}:
            for x, verts in back_paths(succT, u, min(j, maxk), set()):
                checks += 1
                if E.key(W[x]) < E.key(pathval(Eg, u, verts, len(verts))):
                    viol += 1
                    if viol <= 3: print("violation: stretch start", k0, "step", j, "x", x, "u", u, "path(before u)", verts)
    print(f"{path.split('/')[-1]}: stretches up to {longest} steps, I1 checks {checks}, violations {viol}")
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9)
