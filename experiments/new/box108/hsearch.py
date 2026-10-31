#!/usr/bin/env python3
"""L-NEW box 108: random search for an N5 W-run whose frozen-reference W-hierarchy (box 107 hier.py) has depth >= TARGET.
Random games: n vertices, random owner, priorities 0..n-1 (random permutation, so injective), out-degree 1..D (no self-loop
requirement; a self-loop is allowed), every vertex has >= 1 successor. Writes the first hit to out/hit_<seed>.pg.
Usage: hsearch.py SEED0 COUNT NMIN NMAX D TARGET"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
def cs(E, n, v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
def depth(g):
    n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed); S, TAU, FB = [tuple(s)], [tuple(t)], []
    while len(S) < 2000:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    Wc = {}
    def Wv(k, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        return Wc[tau].evaluate(S[k])[0]
    runs = []
    for k in range(len(S) - 1):
        if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
        if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
        else: runs.append([k])
    best = 0
    def block(ks, tau, lev):
        nonlocal best
        if not ks: return
        ref = [cs(E, n, x) for x in Wv(ks[-1] + 1, tau)]
        P = lambda j: sum(lcp(cs(E, n, x), ref[v]) for v, x in enumerate(Wv(j, tau)))
        sub, subs = [], []
        for k in ks:
            if P(k + 1) > P(k):
                best = max(best, lev)
                if sub: subs.append(sub); sub = []
            else: sub.append(k)
        if sub: subs.append(sub)
        for sb in subs: block(sb, tau, lev + 1)
    for run in runs:
        tau = TAU[run[0]]; block([k for k in run if Wv(k, tau) != Wv(k + 1, tau)], tau, 1)
    return best, len(S) - 1
s0, cnt, nmin, nmax, D, target = map(int, sys.argv[1:7]); hist = {}
for seed in range(s0, s0 + cnt):
    R = random.Random(seed); n = R.randint(nmin, nmax); pr = list(range(n)); R.shuffle(pr)
    own = [R.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(R.sample(range(n), R.randint(1, D)))) for _ in range(n)]
    g = pg.Game(pr, own, succ)
    try: h, T = depth(g)
    except Exception as e: print("ERR", seed, e); continue
    hist[h] = hist.get(h, 0) + 1
    if h >= target:
        with open(os.path.join(HERE, "out", f"hit_{seed}.pg"), "w") as f:
            f.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
        print("HIT seed", seed, "n", n, "depth", h, "T", T, flush=True)
print("HIST", s0, cnt, sorted(hist.items()), flush=True)
