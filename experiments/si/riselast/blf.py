#!/usr/bin/env python3
"""L-SI succ. 5, box 10: DATA for Lemma BL and Corollary BL-F (docs/si/N5-RL-box10.md §1). At every in-scope THR S4c fallback k
(reltrace.runs_of; τ := τ_k, G_τ = the one-player game with Odd's choices fixed by τ):
  (BL-a)  σ_k is not optimal in G_τ: W_k ≠ W* (W* = play values of an optimal Even strategy of G_τ, computed as in mono.states:
          VJ counterstrategy on the dual arena).
  (BL-F1) on F_k, W_k equals the optimum of G_τ[F_k] (Even's edges from F_k into R̄_k deleted).
  (BL-F2) x0 := σ̄_k(o) is deficient: W_k(x0) ◁ W*(x0).
Usage: blf.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def opt_vals(g, tau, succ_even):
    succ = [list(succ_even[v]) if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]
    Er = n5.Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(g.n)))
    s = [best[v] if g.owner[v] == 0 else -1 for v in range(g.n)]
    return s, wvals(g, s, tau)[1]

def scan(g, name):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); E = n5.Engine(g); C = Counter(); ex = []
    K = lambda v: E.key(v)
    for S in runs:
        for e in S:
            a = out[e["i"]]
            if e["k"] != "F" or e["r"] < -1: continue
            C["thr_fb"] += 1; t = a["t"]; W = a["W"]; Rb = a["R"] | {o}; F = [v for v in range(g.n) if v not in Rb]
            _, Ws = opt_vals(g, t, [sorted(set(g.succ[v])) if g.owner[v] == 0 else [] for v in range(g.n)])
            if all(Ws[v] == W[v] for v in range(g.n)): C["BLa_viol"] += 1; ex.append((name, "BL-a", e["i"]))
            se = [sorted(u for u in set(g.succ[v]) if (v in Rb or u not in Rb)) if g.owner[v] == 0 else [] for v in range(g.n)]
            _, Wf = opt_vals(g, t, se)
            if any(Wf[v] != W[v] for v in F): C["BLF1_viol"] += 1; ex.append((name, "BL-F1", e["i"]))
            x0 = a["sb"][o]
            if not K(W[x0]) < K(Ws[x0]): C["BLF2_viol"] += 1; ex.append((name, "BL-F2", e["i"], x0))
            for v in range(g.n):
                if K(W[v]) > K(Ws[v]): C["dominance_viol"] += 1; ex.append((name, "DOM", e["i"], v)); break
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
