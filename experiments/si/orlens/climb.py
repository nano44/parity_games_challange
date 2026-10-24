#!/usr/bin/env python3
"""Hill climb against (ELIM-n): one-Odd-choice games (o-cyclic allowed), canonical N5 start.
Fitness = (longest run of non-eliminating transitions inside one joint lambda-phase, that phase's length).
Mutations and the random C^1O generator are L-NEW's (experiments/new/box25/common.py, box21 climb_fix.py; read-only).
Usage: climb.py n seed secs outprefix"""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box25")); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from common import rand_c1o
from climb_fix import mutate
sys.path.insert(0, HERE)
import ortrace as OT, elim as EL
pg = OT.pg
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1)
    try:
        _, it, rows = EL.elim_g(pg.Game(*G), None, 'n5', cap=400)
    except Exception: return (-1, -1)
    r = max(rows, key=lambda q: (q["noelimrun"], q["trans"]))
    return (r["noelimrun"], r["trans"])
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    while True:
        g = rand_c1o(rng, n, n, forced=0.0)
        if g is None: continue
        G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
        if f[0] >= 0: break
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
