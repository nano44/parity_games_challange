#!/usr/bin/env python3
"""L-SI box 16: DATA for TC-SWITCH (docs/si/N5-2O-T-box16.md §4.2). At every terminal change of an N5 run (an S4a transition k -> k+1
inside a phase at which some v in R_D at both states changes u(v), the first D-vertex on its (sigma, tau)-play), it records the old
gate u, the new gate u', and the S1 order (Engine.key, Even's view) of Xi_k(u) vs Xi_k(u'), of W_k(u) vs W_k(u'), and whether D_k, R_D,
Xi(D), W(D) are unchanged (same stretch_D). Changes with D_k != D_{k+1} (with ULT=1 also: the set of W-direct gates changes) are counted apart (dchange) and not compared;
changes at a vertex v in D_k itself are counted apart (gatev). Reports how often the change goes to the gate with the larger W, larger Xi, or larger
(W, Xi) pair, and the contradicting cases. Usage: tcdir.py --one GAME START.json | --list FILE [KMIN] | --rand COUNT NLO NHI SEED (random C^kO, k in {2,2,3,4}, multi.py's generator; odd #: S3 start, even #: random start pair)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual, load

def lasso(nx, v):
    seen, out = {}, []
    while v not in seen: seen[v] = len(out); out.append(v); v = nx(v)
    return out, seen[v]

def wval(E, nx, v):
    pl, i = lasso(nx, v); cyc = pl[i:]; c = max(cyc, key=lambda x: E.rank[x])
    j = pl.index(c); P = 0
    for x in pl[:j]:
        if E.rank[x] > E.rank[c]: P |= E.bit[x]
    return (c, P, j)

S = dict(TCCLASS_V=0, gatev=0, D2=0, dchange=0, changes=0, same_stretch=0, toW=0, toX=0, toWX=0, againstW=0, tieW=0)
CASES = []

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        def wdirect(u):
            pl, i = lasso(wn, u)
            return u in pl[i:] or not any(x in D for x in pl[1:])
        dirD = {u for u in D if wdirect(u)}
        uu = {}
        for v in range(g.n):
            pl, _ = lasso(wn, v)
            uu[v] = next((x for x in pl if (x in dirD if ULT else x in D)), None)
        W = {u: wval(E, wn, u) for u in D}
        rows.append(dict(t=tuple(t), lam=tuple(x[0] for x in vs), vs=vs, D=D, dirD=frozenset(dirD), uu=uu, W=W, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    for k in range(len(rows) - 1):
        r0, r1 = rows[k], rows[k + 1]
        if r0["fb"] or (r0["lam"], r0["t"]) != (r1["lam"], r1["t"]): continue
        for v in range(g.n):
            a, b = r0["uu"][v], r1["uu"][v]
            if a is None or b is None or a == b: continue
            S["changes"] += 1
            same = r0["D"] == r1["D"] and {x for x in range(g.n) if r0["uu"][x] is not None} == {x for x in range(g.n) if r1["uu"][x] is not None} \
                and all(r0["vs"][u] == r1["vs"][u] and r0["W"][u] == r1["W"][u] for u in r0["D"])
            S["same_stretch"] += same
            if b not in r0["D"] or r0["D"] != r1["D"] or (ULT and r0["dirD"] != r1["dirD"]): S["dchange"] += 1; continue
            if v in r0["D"]: S["gatev"] += 1; continue
            S["D2"] += len(r0["D"]) == 2
            S["TCCLASS_V"] += r0["vs"][a][0] != r0["vs"][b][0] or r1["vs"][a][0] != r1["vs"][b][0]
            kw = (E.key(r0["W"][b]) > E.key(r0["W"][a])) - (E.key(r0["W"][b]) < E.key(r0["W"][a]))
            kx = (E.key(r0["vs"][b]) > E.key(r0["vs"][a])) - (E.key(r0["vs"][b]) < E.key(r0["vs"][a]))
            S["toW"] += kw > 0; S["againstW"] += kw < 0; S["tieW"] += kw == 0; S["toX"] += kx > 0
            S["toWX"] += (kw, kx) > (0, 0)
            if kw < 0: CASES.append((name, k, v, a, b, kx))

KFIX = int(os.environ.get("K", "0"))
ULT = os.environ.get("ULT") == "1"     # ULT=1: u(v) := the first W-DIRECT D-vertex on v's W-play (ultimate gate), not the first D-vertex   # K=2: only C^2O games in --rand

def main():
    if sys.argv[1] == "--one":                 # --one GAME.pg START.json (start: {"sigma": {v: w}, "tau": {v: w}})
        import json
        g = load(sys.argv[2]); st = json.load(open(sys.argv[3]))
        check(g, sys.argv[2], ({int(a): b for a, b in st["sigma"].items()}, {int(a): b for a, b in st["tau"].items()}))
        print(" ".join(f"{k}={v}" for k, v in S.items()))
        for c in CASES[:10]: print("AGAINST_W", c)
        return
    if sys.argv[1] == "--rand":
        import random
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, sys.argv[2:6]); rng = random.Random(seed); i = 0
        while i < cnt:
            g = rand_ckO(rng, lo, hi, KFIX or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            i += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, f"rand seed {seed} #{i}", None if i % 2 else st)
        print(" ".join(f"{k}={v}" for k, v in S.items()))
        for c in CASES[:10]: print("AGAINST_W", c)
        return
    kmin = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    for line in open(sys.argv[2]):
        f = line.strip()
        if not f: continue
        g = load(os.path.join(ROOT, f))
        if g.n > 48: continue
        if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
        check(g, f)
    print(" ".join(f"{k}={v}" for k, v in S.items()))
    for c in CASES[:10]: print("AGAINST_W", c)

if __name__ == "__main__":
    main()
