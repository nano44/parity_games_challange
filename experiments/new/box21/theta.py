#!/usr/bin/env python3
"""Box 21, games with one Odd choice vertex o: along the canonical N5 run print the throttle θ = Ξ(o), w = W(o) (vs the current tau),
Odd moves, the number of θ-changes, w-changes and the longest stretch with (θ, w, tau) constant. Usage: theta.py game.pg [-v]"""
import sys
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # box21 -I: find sibling modules
from n5x import *
from h1 import wvals
def main(path, verbose=False):
    g = load(path); E = Engine(g); n = g.n
    o = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
    st, fb = trace(g); th, ww = [], []; Ed = Engine(dual(g))
    for s, t in st:
        X, sb = E.evaluate(s); Eg, W = wvals(g, s, t); th.append(X[o]); ww.append((W[o], tuple(x[0] for x in X), tuple(y[0] for y in Ed.evaluate(t)[0])))
        if verbose: print("θ", X[o], "σ̄(o)", sb[o], "w", W[o], "τ(o)", t[o])
    tc = sum(th[k] != th[k - 1] for k in range(1, len(st))); wc = sum(ww[k] != ww[k - 1] for k in range(1, len(st)))
    oc = sum(st[k][1] != st[k - 1][1] for k in range(1, len(st)))
    best = cur = 0
    for k in range(1, len(st)):
        cur = cur + 1 if (th[k - 1], ww[k - 1], st[k - 1][1]) == (th[k - 2], ww[k - 2], st[k - 2][1]) and k > 1 else 1
        best = max(best, cur)
    print(f"{path.split('/')[-1]} n={n} iterations={len(st)-1} fb={fb} Odd moves={oc} θ-changes={tc} (w or joint-λ)-changes={wc} longest (θ,w,τ,λ)-constant stretch={best}")
if __name__ == "__main__": main(sys.argv[1], "-v" in sys.argv)
