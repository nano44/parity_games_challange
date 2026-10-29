#!/usr/bin/env python3
"""L-NEW box 54 (successor 32): N5-SF, the SINGLE-FRAME variant of N5 (Lead 14:24Z). Identical to SPEC S1-S5 (docs/new/N5-ssi-global.md)
except in S4a / S4b, where the opponent is fixed to its BEST REPLY instead of its current strategy:
  S4a': H: Even v keeps A(v) = {sigma(v)} + {w : (v, w) in Is}; Odd v keeps only sigma-bar(v) (Odd's optimal counterstrategy to sigma, S1),
        sigma_new = Even's optimal strategy of H (S1 procedure on the dual of H, as n5x.step). Arena AND choice are in the Xi frame.
  S4b': mirror: Odd v keeps A(v) = {tau(v)} + It(v); Even v keeps only tau-bar(v) (Even's optimal counter to tau on G^d); tau_new = optimum.
  S4c, S4d, S5 unchanged (S4c is counted; it should never fire, Lemma NOFB in docs/new/N5-SF-box54.md).
MODE=w gives N5-SFW (the W-frame variant: Even's arena = W-improving edges against tau, choice against tau; Odd mirrored against sigma),
kept only to test for cycling. trace(g, start) returns the per-iteration states. Usage: imported, or n5sf.py GAME [START]."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import Engine, dual, load, readstart, start_pair
import pg
MODE = os.environ.get("MODE", "x")

def wimp(E, g, s, t, owner):
    """improving edges of the `owner` player's strategy against the opponent fixed (the (s, t)-play valuation)."""
    sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root")); from common import wplay
    val, _ = wplay(E, g, s, t); out = []
    for v in range(g.n):
        if g.owner[v] != owner: continue
        cur = (s if owner == 0 else t)[v]; kc = E.key(val[cur])
        for w in set(g.succ[v]):
            if w != cur and ((E.key(val[w]) > kc) if owner == 0 else (E.key(val[w]) < kc)): out.append((v, w))
    return out

def step(g, E, Ed, sigma, tau):
    n = g.n
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau)
    oppE = sbar if MODE == "x" else tau          # what Odd plays in Even's arena
    oppO = tbar if MODE == "x" else sigma        # what Even plays in Odd's arena
    IsA = Is if MODE == "x" else wimp(E, g, sigma, tau, 0)
    ItA = It if MODE == "x" else wimp(E, g, sigma, tau, 1)
    if IsA:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in IsA: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [oppE[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(oppE[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
    if ItA:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in ItA: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [oppO[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        _, best = Er.evaluate(tuple(oppO[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == sigma and nt == tau:
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, Is, It, fb, vs, sbar

def trace(g, start=None, cap=200000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); out = []; seen = set()
    while len(out) <= cap:
        key = (tuple(s), tuple(t))
        if key in seen: out.append(dict(s=s, t=t, cycle=True)); break
        seen.add(key)
        r = step(g, E, Ed, s, t)
        vs, sb = E.evaluate(tuple(s))
        out.append(dict(s=list(s), t=list(t), sb=list(sb), lam=tuple(x[0] for x in vs), fb=(r[4] if r else 0)))
        if r is None: break
        s, t = list(r[0]), list(r[1])
    return E, out

if __name__ == "__main__":
    g = load(sys.argv[1]); E, T = trace(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None)
    print("iterations", len(T) - 1, "fallbacks", sum(x.get("fb", 0) for x in T), "cycle", T[-1].get("cycle", False))
