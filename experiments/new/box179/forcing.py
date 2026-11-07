#!/usr/bin/env python3
"""L-NEW box 179: forcing transitions for Theorem OPT-K. For d and every level l <= d - 2 and both movers p of level l, a genome of
L^R_d with every Xi-target the exit X (all parities even; the option s(x) of the state has the larger rank at every mover except p)
and a state s such that step(s) moves p only, k(p) goes 1 -> 0, both level-(l+1) movers go k 0 -> 1, and no other k bit changes;
for l = d - 1 a state where only p moves and only k(p) changes (1 -> 0). Exact check with the box150 simulator. Writes out/force_d<d>.json.
Usage: forcing.py dmax seed"""
import os, sys, json, random
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def kbits(g, s):
    K = g.keys(s); return [int(s[x] != min((0, 1), key=lambda j: g.optkey(K, x, j))) for x in range(g.N)]
def build(d, p, s, gates):
    N = 2 * d; lev = [x // 2 for x in range(N)]; opts = []; br = [0] * (2 * N); bp = [0] * (2 * N); gate = []
    for x in range(N):
        best = (1 - s[x]) if x == p else s[x]; o = []
        for k in (0, 1):
            m = 2 * x + k; o.append([2 * (lev[x] - 1) + k if lev[x] else -1, -1, m]); br[m] = 2 * x + (1 if k == best else 0)
        opts.append(o); gate.append([gates[2 * x], gates[2 * x + 1]])
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": list(s)}
def want(d, l, p, k0, k1, mv):
    if mv != [p]: return False
    for x in range(2 * d):
        if x == p: ok = k0[x] == 1 and k1[x] == 0
        elif l + 1 < d and x // 2 == l + 1: ok = k0[x] == 0 and k1[x] == 1
        else: ok = k0[x] == k1[x]
        if not ok: return False
    return True
rng = random.Random(int(sys.argv[2])); out = {}
for d in range(1, int(sys.argv[1]) + 1):
    res = []
    for l in range(d):
        for p in (2 * l, 2 * l + 1):
            for tries in range(200000):
                s = [rng.randint(0, 1) for _ in range(2 * d)]; gates = list(range(4 * d)); rng.shuffle(gates)
                G = build(d, p, s, gates); g = Gen(G); n, _ = g.step(tuple(s))
                if n is None: continue
                mv = [x for x in range(2 * d) if n[x] != s[x]]
                if want(d, l, p, kbits(g, s), kbits(g, n), mv): res.append({"l": l, "p": p, "genome": G, "s": s, "next": list(n)}); break
            else: print("NOT FOUND d %d l %d p %d" % (d, l, p))
    out[d] = res; print("d %d: %d of %d forcing transitions found and checked" % (d, len(res), 2 * d))
    json.dump(res, open(os.path.join(H, "out", "force_d%d.json" % d), "w"))
