#!/usr/bin/env python3
"""Box 5 lower bounds: hill climb on o-cyclic C^1O games of fixed n, canonical N5 start, fitness = (max X per phase, its phase
length) or (max O, ...) from box4.measure (same definitions as the tables; mutation = box21 climb_fix.mutate, accept >=).
Usage: climb5.py X|O n seed secs OUTPREFIX [SEED.pg]  (SEED.pg: start from that game, padded to n with Even self-loop vertices of
priority 0; writes OUTPREFIX.pg at every strict improvement; last line FINAL fit)"""
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
import box4  # noqa: E402
from exh import pg, trace, split, rand_c1o  # noqa: E402
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box21"))
from climb_fix import mutate  # noqa: E402


def fit(G, f):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]):
        return (-1, 0)
    o = odd[0]; g = pg.Game(*G)
    if not any(w in split(g, o) for w in G[2][o]):
        return (-1, 0)
    try:
        st, _ = trace(g, None, check=False)
        if len(st) < 2:
            return (0, 0)
        m = box4.measure(g, st)
    except Exception:
        return (-1, 0)
    return (m[f], -m[f + "plen"])  # more X first, then a SHORTER phase attaining it (cleaner witness)


def main():
    f, n, seed, secs, outp = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed)
    if len(sys.argv) > 6:
        g = pg.read(sys.argv[6]); k = n - g.n
        G = [list(g.prio) + [0] * k, list(g.owner) + [0] * k, [list(x) for x in g.succ] + [[g.n + i] for i in range(k)]]
        fg = fit(G, f); assert fg[0] >= 0, "seed game not in the class"
    while len(sys.argv) <= 6:
        g = rand_c1o(rng, n, n, forced=0.0)
        if g is not None:
            G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; fg = fit(G, f)
            if fg[0] >= 0:
                break
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H, f)
        if fh >= fg:
            if fh > fg:
                print(f"{time.time() - t0:7.0f}s it {it} fit {fh}", flush=True)
                pg.write(pg.Game(*H), outp + ".pg")
            G, fg = H, fh
    print("FINAL", f, n, fg, it, flush=True)


if __name__ == "__main__":
    main()
