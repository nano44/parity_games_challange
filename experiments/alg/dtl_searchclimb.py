#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4): hill-climb on ACTUAL A_DTL runs for SEARCHES PER PHASE (the headline
measure, Lead 19:08Z): fitness = (max searches in one phase, total iterations). Order datum from DTL_ORDER. Starts from a
random game of size --n (gen.random_game) or --seed-game. Usage: DTL_ORDER=oink dtl_searchclimb.py OUTDIR SEED STEPS --n N"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, dtl_deficit as X, dtl_nestK as NK
from dtl_mclimb import mutate, TO
from dtl_nestclimb import write

def measure(g, limit=30):
    d = X.build(g)
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run()
    except TO:
        return (-1, -1)
    finally:
        signal.alarm(0)
    return (max((len(ph) for ph in NK.phases(d)), default=0), d.iterations)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("seed", type=int); ap.add_argument("steps", type=int)
    ap.add_argument("--n", type=int, default=0); ap.add_argument("--seed-game")
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rnd = random.Random(a.seed); sys.setrecursionlimit(100000)
    g = pg.read(a.seed_game) if a.seed_game else gen.random_game(a.n, a.n, 1, 3, a.seed)
    f = measure(g); best = f
    print("start", g.n, f, flush=True)
    for step in range(a.steps):
        h = mutate(g, rnd, set()); fh = measure(h)
        if fh >= f:
            g, f = h, fh
            if f > best:
                best = f; write(g, os.path.join(a.out, f"search_s{a.seed}.pg"))
                print(f"step {step} n={g.n} fitness {f}", flush=True)
    print("done best", best, flush=True)
