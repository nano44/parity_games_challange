#!/usr/bin/env python3
"""L-RED R182: hill-climb games for route (C): SCORE = 100 * CRUN(ODIFF <= 2).moves + 10 * CRUN(any ODIFF).moves + lamw bonus.
Mutations as r179/climb179. Usage: climb182.py seed.pg|rand:n iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r179"), os.path.join(HERE, "..", "r181"), os.path.join(HERE, "..", "..", "new", "box21")]
import cscore, climb179, climb181, pg
from n5x import load
def score(g):
    try:
        a = cscore.cruns(g, None, odmax=2); b = cscore.cruns(g, None, odmax=99)
    except Exception: return -1, None
    return 100 * a["moves"] + 10 * b["moves"] + 5 * a["lamw"], (a, b)
if __name__ == "__main__":
    src, iters, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if src.startswith("rand:"):
        n = int(src[5:]); V = climb181.randgame(n, rng); g = pg.Game([x for x, _, _ in V], [y for _, y, _ in V], [z for _, _, z in V])
    else: g = load(src)
    bs, R = score(g); print("START", bs, flush=True)
    for it in range(iters):
        h = climb179.mut(g, rng); hs, HR = score(h)
        if hs >= bs:
            if hs > bs: print("IT", it, "SCORE", hs, HR, flush=True)
            g, bs, R = h, hs, HR; climb179.write(g, out)
    print("BEST", bs, R)
