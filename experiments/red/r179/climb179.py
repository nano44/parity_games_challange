#!/usr/bin/env python3
"""L-RED R179: hill-climb parity games (real N5, default S3 start) for SCORE = 1000*xich + 10*fl + K (odxi.analyse). Mutations: retarget
an edge, add/remove an edge, change a priority, flip an owner. Usage: climb179.py seed.pg iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
import odxi, pg
from n5x import load
def score(g):
    try: R = odxi.analyse(g, None, cap=400)
    except Exception: return -1, None
    return 1000 * R["xich"] + 10 * R["fl"] + R["K"], R
def mut(g, rng):
    n = g.n; pr = list(g.prio); ow = list(g.owner); su = [list(x) for x in g.succ]; r = rng.random(); v = rng.randrange(n)
    if r < 0.35: su[v][rng.randrange(len(su[v]))] = rng.randrange(n)
    elif r < 0.55:
        if len(su[v]) < 5: su[v].append(rng.randrange(n))
    elif r < 0.7:
        if len(su[v]) > 1: su[v].pop(rng.randrange(len(su[v])))
    elif r < 0.92: pr[v] = rng.randrange(0, n + 2)
    else: ow[v] ^= 1
    su = [sorted(set(x)) for x in su]
    return pg.Game(pr, ow, su)
def write(g, p):
    with open(p, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
if __name__ == "__main__":
    g = load(sys.argv[1]); iters, seed, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    bs, R = score(g); print("START", bs, flush=True)
    for it in range(iters):
        h = mut(g, rng); hs, HR = score(h)
        if hs >= bs:
            if hs > bs: print("IT", it, "SCORE", hs, "xich", HR["xich"], "fl", HR["fl"], "K", HR["K"], flush=True)
            g, bs, R = h, hs, HR; write(g, out)
            if HR["xich"] > 0 and os.environ.get("STOP1"): break
    print("BEST", bs)
