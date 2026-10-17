#!/usr/bin/env python3
"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): hill-climb against (SPP) "searches in one phase <= |G'|".
Fitness = max over phases with |G'| >= SPPC_MING (default 2) of (S - |G'|), then S of that phase, then iterations (dtl_spp.py phase convention). Order datum from
DTL_ORDER. Mutations: dtl_mclimb.mutate. Start: random game of size --n or --seed-game.
Usage: DTL_ORDER=oink dtl_sppclimb.py OUTDIR SEED STEPS --n N"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, dtl_spp as P
from dtl_mclimb import mutate, TO
from dtl_nestclimb import write

def measure(g, limit=30):
    d = P.build(g)
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run()
    except TO:
        return (-99, -1, -1)
    finally:
        signal.alarm(0)
    ph = P.phases(d)
    return max(((r["S"] - r["G"], r["S"], d.iterations) for r in ph if r["G"] >= int(os.environ.get("SPPC_MING", "2"))), default=(-99, 0, 0))

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
                best = f; write(g, os.path.join(a.out, f"sppc_s{a.seed}.pg"))
                print(f"step {step} n={g.n} fitness {f}", flush=True)
    print("done best", best, flush=True)
