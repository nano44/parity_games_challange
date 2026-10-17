#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §20: hill-climb on C6 (ideal pruning, stable order) for NESTED
reset depth (dtl_nestreset.py). Fitness (lexicographic): max nested-reset depth over transitions, number of transitions at
that depth, number of depth-0 pieces in the longest search. Usage: dtl_resetclimb.py OUTDIR SEED STEPS --seed-game G.pg"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_mirror as M, dtl_nestreset as NR
from dtl_mclimb import mutate, TO
from dtl_nestclimb import write

def measure(g, limit=20):
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    d = M.Tr([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx])
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run(); hist, best = {}, [0, None]; NR.analyse(d, hist, best, "g")
    except TO:
        return (-1,), None
    finally:
        signal.alarm(0)
    mx = max(hist) if hist else 0
    return (mx, hist.get(mx, 0), max((len(t["pieces"]) for t in d.trace), default=0)), (hist, d.iterations)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("seed", type=int); ap.add_argument("steps", type=int); ap.add_argument("--seed-game", required=True)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rnd = random.Random(a.seed); sys.setrecursionlimit(100000)
    g = pg.read(a.seed_game); f, info = measure(g); best = f
    print("start", f, info, flush=True)
    for step in range(a.steps):
        h = mutate(g, rnd, set()); fh, ih = measure(h)
        if fh >= f:
            g, f, info = h, fh, ih
            if f > best:
                best = f; write(g, os.path.join(a.out, f"reset_s{a.seed}.pg"))
                print(f"step {step} n={g.n} fitness {f} {ih}", flush=True)
    print("done best", best, flush=True)
