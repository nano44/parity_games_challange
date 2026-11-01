#!/usr/bin/env python3
"""L-RED R181: hill-climb real parity games (N5, default S3 start) for SCORE = 1000*LFL + gate (flrun.analyse: longest FL run and
its gating changes). Mutations as r179/climb179.mut. UNION=k: start from the seed plus a random k-vertex part (disjoint).
Usage: climb181.py seed.pg|rand:n iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r179"), os.path.join(HERE, "..", "..", "new", "box21")]
import flrun, climb179, pg
from n5x import load
def randgame(n, rng, base=0):
    return [(rng.randint(0, n), rng.randint(0, 1), sorted(set(base + rng.randrange(n) for _ in range(rng.randint(1, 3))))) for _ in range(n)]
def score(g):
    try: R = flrun.analyse(g, None, cap=600)
    except Exception: return -1, None
    return 1000 * R["LFL"] + R["gate"], R
if __name__ == "__main__":
    src, iters, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if src.startswith("rand:"):
        n = int(src[5:]); V = randgame(n, rng); g = pg.Game([a for a, _, _ in V], [b for _, b, _ in V], [c for _, _, c in V])
    else:
        g = load(src); k = int(os.environ.get("UNION", "0"))
        if k:
            V = randgame(k, rng, g.n)
            g = pg.Game(list(g.prio) + [a for a, _, _ in V], list(g.owner) + [b for _, b, _ in V], [list(x) for x in g.succ] + [c for _, _, c in V])
    bs, R = score(g); print("START n", g.n, bs, flush=True)
    for it in range(iters):
        h = climb179.mut(g, rng); hs, HR = score(h)
        if hs >= bs:
            if hs > bs: print("IT", it, "LFL", HR["LFL"], "gate", HR["gate"], "K", HR["K"], flush=True)
            g, bs, R = h, hs, HR; climb179.write(g, out)
    print("BEST n", g.n, "LFL", R["LFL"], "gate", R["gate"])
