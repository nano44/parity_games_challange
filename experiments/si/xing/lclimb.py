#!/usr/bin/env python3
"""L-SI box 4: climb for reversals of R. o-cyclic C^1O, canonical N5 start. Fitness = max over joint λ-phases of
(Z = reversals of R (zcount.py), X, phase length). Mutation: experiments/new/box21 climb_fix.mutate (read-only import).
Every improvement is written to OUT.pg; re-verify bests with leaves.py (asserts n5.run equality), n5.py, Oink zlk, check_sol2.py.
Usage: lclimb.py seed secs OUT seed.pg"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from leaves import *
from zcount import zsigns
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box28")); sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from climb_fix import mutate
from pureY import split

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1)
    o = odd[0]; g = pg.Game(*G)
    if not any(w in split(g, o) for w in G[2][o]): return (-1, -1, -1)
    try:
        rows, ph = profile(g); oo = annotate(g, rows); best = (0, 0, 0)
        for (x, y) in ph:
            Z, sg = zsigns(rows, x, y)
            best = max(best, (Z, len(sg), y - x))
        return best
    except Exception: return (-1, -1, -1)

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
