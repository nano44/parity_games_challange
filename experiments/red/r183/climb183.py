#!/usr/bin/env python3
"""L-RED R183: hill-climb real parity games (N5, default S3 start) for growing FVCH (fvch.analyse). SCORE = 1000*FVCH(best run) +
200*CROSS(total) + 10*L(best run) + total L. Mutations as r179/climb179.mut. UNION=k adds a random k-vertex part to a seed.
Usage: climb183.py seed.pg|rand:n iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r179"), os.path.join(HERE, "..", "r181"), os.path.join(HERE, "..", "..", "new", "box21")]
import fvch, climb179, climb181, pg
from n5x import load
def score(g):
    try: R = fvch.analyse(g, None, cap=600)
    except Exception: return -1, None
    rs = R["runs"]
    if not rs: return 0, dict(FVCH=0, L=0, CROSS=0, K=R["K"])
    b = max(rs, key=lambda r: (r["FVCH"], r["L"]))
    cr = sum(r["CROSS"] for r in rs); tl = sum(r["L"] for r in rs)
    return 1000 * b["FVCH"] + 200 * cr + 10 * b["L"] + tl, dict(FVCH=b["FVCH"], L=b["L"], CROSS=cr, K=R["K"], FVMAX=b["FVMAX"])
if __name__ == "__main__":
    src, iters, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if src.startswith("rand:"):
        n = int(src[5:]); V = climb181.randgame(n, rng); g = pg.Game([a for a, _, _ in V], [b for _, b, _ in V], [c for _, _, c in V])
    else:
        g = load(src); k = int(os.environ.get("UNION", "0"))
        if k:
            V = climb181.randgame(k, rng, g.n)
            g = pg.Game(list(g.prio) + [a for a, _, _ in V], list(g.owner) + [b for _, b, _ in V], [list(x) for x in g.succ] + [c for _, _, c in V])
    bs, R = score(g); print("START n", g.n, bs, R, flush=True)
    for it in range(iters):
        h = climb179.mut(g, rng); hs, HR = score(h)
        if hs >= bs:
            if hs > bs: print("IT", it, HR, flush=True)
            g, bs, R = h, hs, HR; climb179.write(g, out)
    print("BEST n", g.n, R, flush=True)
