#!/usr/bin/env python3
"""Hill climb against (ELIM-n): one-Odd-choice games (o-cyclic allowed), canonical N5 start.
Fitness = (longest run of non-eliminating transitions inside one joint lambda-phase, that phase's length).
Mutations and the random C^1O generator are L-NEW's (experiments/new/box25/common.py, box21 climb_fix.py; read-only).
Usage: climb.py n seed secs outprefix [--seedgame file.pg] [--anyodd]"""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box25")); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from common import rand_c1o
from climb_fix import mutate
sys.path.insert(0, HERE)
import ortrace as OT, elim as EL, thetaelim as TE
pg = OT.pg
ONEODD = "--anyodd" not in sys.argv
THETA = "--theta" in sys.argv   # fitness = (max theta-changes in a non-eliminating window, theta-changes in that phase)
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if (ONEODD and len(odd) != 1) or any(not s for s in G[2]): return (-1, -1)
    try:
        if THETA:
            _, _, b = TE.run_g(pg.Game(*G), None, cap=400); return (b[0], b[1])
        _, it, rows = EL.elim_g(pg.Game(*G), None, 'n5', cap=400)
    except Exception: return (-1, -1)
    r = max(rows, key=lambda q: (q["noelimrun_st"], q["trans"]))
    return (r["noelimrun_st"], r["trans"])
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if "--seedgame" in sys.argv:
        g0, _ = OT.load(sys.argv[sys.argv.index("--seedgame") + 1]); n = g0.n
        G = [list(g0.prio), list(g0.owner), [list(x) for x in g0.succ]]; f = fit(G); print("seed fit", f, flush=True)
    while "--seedgame" not in sys.argv:
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
