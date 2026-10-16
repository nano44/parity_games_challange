#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), queue item (3): hill-climb for NESTED deficit runs on A_DTL.
Fitness (lexicographic): F1 = max over phases and child pieces j >= 1 with >= 2 distinct DEF contexts of N_j (total DEF
changes at piece j over its contexts; dtl_nestK's k(j, C)), then total DEF in that phase. Order datum from DTL_ORDER
(oink = exact pinned order). Padding: --pad K adds K source-only vertices (no in-edges) to the seed game.
Usage: DTL_ORDER=oink dtl_nestclimb.py OUTDIR SEED STEPS --seed-game G.pg [--pad K]"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_deficit as X, dtl_nestK as NK
from dtl_mclimb import mutate, TO

def measure(g, limit=20):
    d = X.build(g)
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run()
    except TO:
        return (-1, -1), None
    finally:
        signal.alarm(0)
    best, info = (0, 0), None
    for ph in NK.phases(d):
        k = {}
        for a, b in zip(ph, ph[1:]):
            for j in range(min(len(a["pieces"]), len(b["pieces"]))):
                (Ra, ra, Va, rha, Vha), (Rb, rb, Vb, rhb, Vhb) = a["pieces"][j], b["pieces"][j]
                if Ra == Rb and (rha, Vha) == (rhb, Vhb) and (ra, Va) != (rb, Vb):
                    k[(j, Ra)] = k.get((j, Ra), 0) + 1
        if not k: continue
        J = max(j for j, _ in k) + 1
        K = [max([c for (jj, _), c in k.items() if jj == j] or [0]) for j in range(J)]
        N = [sum(c for (jj, _), c in k.items() if jj == j) for j in range(J)]
        C = [sum(1 for (jj, _) in k if jj == j) for j in range(J)]
        f1 = max([N[j] for j in range(1, J) if C[j] >= 2] or [0])
        f = (f1, sum(N))
        if f > best: best, info = f, (K, N, C, len(ph), d.iterations)
    return best, info

def write(g, path):
    with open(path, "w") as fo:
        fo.write(f"parity {g.n - 1};\n")
        for v in range(g.n):
            fo.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("seed", type=int); ap.add_argument("steps", type=int)
    ap.add_argument("--seed-game", required=True); ap.add_argument("--pad", type=int, default=0)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rnd = random.Random(a.seed); sys.setrecursionlimit(100000)
    g = pg.read(a.seed_game)
    if a.pad:
        n0 = g.n; mp = max(g.prio)
        g = pg.Game(list(g.prio) + [rnd.randrange(mp + 1) for _ in range(a.pad)], list(g.owner) + [rnd.randrange(2) for _ in range(a.pad)],
                    [list(s) for s in g.succ] + [[rnd.randrange(n0)] for _ in range(a.pad)])
    f, info = measure(g); best = f
    print("start", f, info, flush=True); write(g, os.path.join(a.out, f"nest_s{a.seed}.pg"))
    for step in range(a.steps):
        h = mutate(g, rnd, set()); fh, ih = measure(h)
        if fh >= f:
            g, f, info = h, fh, ih
            if f > best:
                best = f; write(g, os.path.join(a.out, f"nest_s{a.seed}.pg"))
                print(f"step {step} n={g.n} fitness {f} K={ih[0]} N={ih[1]} c={ih[2]} searches={ih[3]} iters={ih[4]}", flush=True)
    print("done best", best, flush=True)
