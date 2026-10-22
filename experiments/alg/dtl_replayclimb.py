#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §20: hill-climb on C6 (ideal pruning, stable order) for §6's
REPLAYS (a level-j transition after a lower level changed in between; depth = nesting of replays, dtl_pieces.replays2).
Fitness (lexicographic): replay depth, replays, searches of the longest phase. Usage: dtl_replayclimb.py OUTDIR SEED STEPS
--seed-game G.pg [--pad K]"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_pieces as P
from dtl_c6proto import C6
from dtl_mclimb import mutate, TO
from dtl_nestclimb import write

def measure(g, limit=20):
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    d = P.mk(C6)([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx])
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run(); rep, dep = P.replays2(d)
    except TO:
        return (-1,), None
    finally:
        signal.alarm(0)
    phases = P.level_seqs(d)
    return (dep, rep, max((len(ph) for ph in phases), default=0)), (d.iterations, [ph for ph in phases if ph][:2])

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("seed", type=int); ap.add_argument("steps", type=int); ap.add_argument("--seed-game", required=True)
    ap.add_argument("--pad", type=int, default=0)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rnd = random.Random(a.seed); sys.setrecursionlimit(100000)
    g = pg.read(a.seed_game)
    if a.pad:
        n0 = g.n
        g = pg.Game(list(g.prio) + [0] * a.pad, list(g.owner) + [rnd.randrange(2) for _ in range(a.pad)],
                    [list(s) for s in g.succ] + [[rnd.randrange(n0)] for _ in range(a.pad)])
    f, info = measure(g); best = f
    print("start", g.n, f, info, flush=True)
    for step in range(a.steps):
        h = mutate(g, rnd, set()); fh, ih = measure(h)
        if fh >= f:
            g, f, info = h, fh, ih
            if f > best:
                best = f; write(g, os.path.join(a.out, f"replay_s{a.seed}.pg"))
                print(f"step {step} n={g.n} fitness {f} {ih}", flush=True)
    print("done best", best, flush=True)
