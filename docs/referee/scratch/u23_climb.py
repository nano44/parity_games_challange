#!/usr/bin/env python3
"""REFEREE climb for P-N5-U23 (ii)'s L_B = 0 corner: fitness = (#kind-A switches in event-free sub-runs with NO kind-B vertex,
max packet-(ii) excess s - (L_B + lambda - 3), #U3/U23 sub-run switches). Every candidate fully checked by u23_probe (FAIL counters saved).
Usage: u23_climb.py seed.pg steps rngseed outdir"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u23_probe as P, u1_probe as U, pg
from casc_climb import mutate

def fitness(g):
    c = Counter(); ex = [-99]; nb = [0]; orig = P.sub
    def sub(g_, o, cw, S, a, b, Rl, kind, sw, cnt, nR):
        KB = [v for v in Rl if kind(S[a], v) == "B"]; LB = max((len(U.play_to(S[a]["nx"], v, o)) for v in KB), default=0)
        for st in range(a, b):
            for v in Rl:
                if sw(st, v) and kind(S[a], v) == "A":
                    lam = len(U.play_to(S[st]["nx"], v, cw)); ex[0] = max(ex[0], (st - a) - (LB + lam - 3)); nb[0] += not KB
        orig(g_, o, cw, S, a, b, Rl, kind, sw, cnt, nR)
    P.sub = sub
    try: P.run(g, c)
    finally: P.sub = orig
    return (nb[0], ex[0], c["U3_switches"] + c["U2_switches"]), c

if __name__ == "__main__":
    seedf, steps, rs, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    os.makedirs(out, exist_ok=True); rng = random.Random(rs); g = U.load(seedf); best, c = fitness(g); tot = Counter()
    print("seed", best, flush=True)
    for it in range(steps):
        h = mutate(g, rng)
        if h is None: continue
        try: f, c = fitness(h)
        except AssertionError: continue
        tot["cands"] += 1; tot.update({k: v for k, v in c.items() if "FAIL" in k})
        if any("FAIL" in k for k in c): pg.write(h, os.path.join(out, "fail_%d.pg" % it)); print("FAIL", it, f, {k: v for k, v in c.items() if "FAIL" in k}, flush=True)
        if f >= best:
            if f > best: print(it, f, flush=True)
            best, g = f, h
    pg.write(g, os.path.join(out, "best.pg")); print("final", best, dict(tot), flush=True)
