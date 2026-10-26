#!/usr/bin/env python3
"""L-SI box 9: DATA for Lemma FBW (docs/si/N5-C-box9.md §2). At every Even S4c fallback k of N5 (any game, any state), for every
gate (y, z) at k (Ξ-improving Even edge), with δ := max(lev(Ξ_k σ_k y, W_k σ_k y), lev(Ξ_k z, W_k z)) (W_k = (σ_k, τ_k) play valuation):
  (FBW-a) lev(Ξ_k σ_k y, Ξ_k z) <= max(δ, -1);
  (FBW-b) if that level is -1 and δ < -1, then y is its own W_k-cycle node (and its own Ξ_k-cycle node).
Also (FBW-W): every gate of level > δ is W_k-improving at the same level (the step the proof uses), and the arena-optimality premise:
S4a's arena optimum equals σ_k at the fallback (re-computed here). On 𝒞^1O games (one Odd choice vertex o; --c1o, or files that are),
the in-scope consequences: at in-scope (h) fallbacks with θ = w (EQ) or θ ◁ w at level -1 (u* = none), M_k <= -1.
Runs are asserted equal to experiments/new/n5.py run() (mono.states).
Usage: fbw.py game.pg ...  |  fbw.py --random SEED COUNT NMIN NMAX"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rfinv import *
from collections import Counter

def scan_w(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); C = Counter(); ex = []
    Ed = n5.Engine(n5.dual(g))
    for i, a in enumerate(out[:-1]):
        if not a["fb"] or not a["Is"]: continue          # Even fallbacks only (Odd fallbacks are the dual statement)
        b = out[i + 1]; C["fbE"] += 1
        Eg, W = wvals(g, a["s"], a["t"]); X = a["Xi"]
        # premise: S4a's arena optimum against τ_k is σ_k (re-computed as in mono.states)
        opt = {v: {a["s"][v]} for v in range(n) if g.owner[v] == 0}
        for v, w in a["Is"]: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [a["t"][v]] for v in range(n)]
        Er = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(a["t"][v] if g.owner[v] == 1 else -1 for v in range(n)))
        if any(best[v] != a["s"][v] for v in range(n) if g.owner[v] == 0): C["premise_fail"] += 1; ex.append((name, "premise", i))
        Mk = -3
        for y, z in a["Is"]:
            u = a["s"][y]; l = lev(X[u], X[z]); Mk = max(Mk, l); C["gates"] += 1
            d = max(lev(X[u], W[u]), lev(X[z], W[z]))
            if l > max(d, -1): C["a_viol"] += 1; ex.append((name, "FBW-a", i, y, z, l, d))
            if l == -1 and d < -1:
                C["b_chk"] += 1
                if not (W[y][0] == y and X[y][0] == y): C["b_viol"] += 1; ex.append((name, "FBW-b", i, y, z))
            if l > d and d < INF:
                C["W_chk"] += 1
                if not (Eg.key(W[z]) > Eg.key(W[u]) and lev(W[u], W[z]) == l): C["W_viol"] += 1; ex.append((name, "FBW-W", i, y, z))
            if d < l: C["above_gap"] += 1
        if o is not None:                                   # in-scope consequence on 𝒞^1O
            ka = (tuple(x[0] for x in X), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
            _, Wb = wvals(g, b["s"], b["t"])
            kb = (tuple(x[0] for x in b["Xi"]), b["t"], tuple(x[0] for x in Ed.evaluate(tuple(b["t"]))[0]))
            h = (not oncycle(g, a["s"], a["sb"], o)) and (not oncycle(g, a["s"], a["t"], o)) and X[o][0] == W[o][0]
            if ka == kb and h and not oncycle(g, b["s"], b["t"], o) and Wb[o] == W[o]:
                r = lev(X[o], W[o]); kind = "THRu" if r >= 0 else ("THR0" if r == -1 else "EQ")
                C["scope_" + kind] += 1
                if kind != "THRu" and Mk > -1: C["scope_viol"] += 1; ex.append((name, "scope", kind, i, Mk))
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    if sys.argv[1] == "--random":
        seed, cnt, a, b = map(int, sys.argv[2:6]); rnd = random.Random(seed)
        for i in range(cnt):
            n = rnd.randint(a, b)
            prio = [rnd.randrange(n) for _ in range(n)]; own = [rnd.randrange(2) for _ in range(n)]
            succ = [sorted(set(rnd.sample(range(n), rnd.randint(1, min(3, n))))) for _ in range(n)]
            c, e = scan_w(pg.Game(prio, own, succ), f"rand{seed}_{i}"); T.update(c); X += e
    else:
        for p in sys.argv[1:]:
            c, e = scan_w(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
