#!/usr/bin/env python3
"""L-RED R182: climb games for long C-STATIC runs (score = 100*maxlen + 1000*viol + routeC). Usage: climbcs.py rand:n iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r179"), os.path.join(HERE, "..", "r181"), os.path.join(HERE, "..", "..", "new", "box21")]
import cstatic, climb179, climb181, pg
src, iters, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
n = int(src[5:]); V = climb181.randgame(n, rng); g = pg.Game([x for x, _, _ in V], [y for _, y, _ in V], [z for _, _, z in V])
def sc(g):
    try: R = cstatic.check(g, None, cap=300)
    except Exception: return -1, None
    return 100 * R["maxlen"] + 1000 * R["viol"] + R["routeC"], R
bs, R = sc(g)
for it in range(iters):
    h = climb179.mut(g, rng); hs, HR = sc(h)
    if hs >= bs:
        if hs > bs: print("IT", it, hs, HR, flush=True)
        g, bs, R = h, hs, HR; climb179.write(g, out)
print("BEST", bs, R)
