#!/usr/bin/env python3
"""L-RED R184 climbs (Lead retarget 18:37Z of R183, after L-NEW 46 box 135 CASC-M). MODE=cyc: SCORE = 1000*LCYC (longest D'-cyclic
stretch) + 50*SELFL-capped + LFL; MODE=cn: SCORE = 1000*CNMAX (W-cycle-node moves in one FL run) + 10*CNMOV + LFL. Default S3 start.
Mutations r179/climb179.mut; UNION=k adds k random vertices to the seed. Usage: [MODE=cyc|cn] climb184.py seed.pg|rand:n iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r179"), os.path.join(HERE, "..", "r181"), os.path.join(HERE, "..", "..", "new", "box21")]
import dcyc, climb179, climb181, pg
from n5x import load
MODE = os.environ.get("MODE", "cyc")
def score(g):
    try: R = dcyc.summary(dcyc.analyse(g, None, cap=600))
    except Exception: return -1, None
    if MODE == "cyc": return 1000 * R["LCYC"] + 50 * min(R["SELFL"], 10) + R["LFL"], R
    return 1000 * R["CNMAX"] + 10 * R["CNMOV"] + R["LFL"], R
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
        g, bs, R = h, hs, HR; climb179.write(g, out + ".tmp"); os.replace(out + ".tmp", out)
print("BEST n", g.n, R, flush=True)
