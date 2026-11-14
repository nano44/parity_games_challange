#!/usr/bin/env python3
"""L-RED R183 structured climb over iterated odxi gadgets: core = odxi_n37 vertices 0..32 (32 = Even sink, self-loop, priority 8);
k gadgets (mover x_i Even priority px_i -> {A_i, B_i}; Odd gates A_i, B_i with two targets each from core 0..32 or any mover x_j, and
priorities). Genome mutation: one target or one priority. SCORE = 1000*L(best FL run) + 100*FVCH(that run) + 20*CROSS + total FL.
Usage: climbs.py k iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "..", "new", "box21")]
import fvch, chain, pg
from n5x import load
core = load(chain.CORE)
def build(G):
    k = len(G); P, O, S = list(core.prio[:33]), list(core.owner[:33]), [list(x) for x in core.succ[:33]]
    X = [33 + 3 * i for i in range(k)]; ref = lambda t: t if t < 33 else X[t - 33]
    for i, (px, (a1, a2, pa), (b1, b2, pb)) in enumerate(G):
        x = X[i]; P += [px, pa, pb]; O += [0, 1, 1]
        S += [[x + 1, x + 2], sorted({ref(a1), ref(a2)}), sorted({ref(b1), ref(b2)})]
    return pg.Game(P, O, S)
def score(G):
    try: R = fvch.analyse(build(G), None, cap=400)
    except Exception: return -1, None
    rs = R["runs"]
    if not rs: return 0, dict(L=0)
    b = max(rs, key=lambda r: (r["L"], r["FVCH"]))
    return 1000 * b["L"] + 100 * b["FVCH"] + 20 * sum(r["CROSS"] for r in rs) + sum(r["L"] for r in rs), dict(L=b["L"], FVCH=b["FVCH"], CROSS=sum(r["CROSS"] for r in rs), K=R["K"])
if __name__ == "__main__":
    k, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    T = lambda: rng.randrange(33 + k)
    G = [[0, [32, rng.randrange(32), 0], [32, rng.randrange(32), 0]] for _ in range(k)]
    bs, R = score(G); print("START k", k, bs, R, flush=True)
    for it in range(iters):
        H = [[x[0], list(x[1]), list(x[2])] for x in G]; i = rng.randrange(k); f = rng.randrange(7)
        if f == 0: H[i][0] = rng.randrange(13)
        elif f in (1, 2): H[i][1 + f - 1][2] = rng.randrange(13)
        else: H[i][1 + (f - 3) // 2][(f - 3) % 2] = T()
        hs, HR = score(H)
        if hs >= bs:
            if hs > bs: print("IT", it, HR, flush=True)
            G, bs, R = H, hs, HR; chain.write(build(G), out)
    print("BEST k", k, R, flush=True)
