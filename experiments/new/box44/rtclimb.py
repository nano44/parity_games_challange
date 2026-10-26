#!/usr/bin/env python3
"""Box 44 climber (DATA): mutate a C^kO game (box43 climb.mutate) to maximise, lexicographically, crd.py's (DIFF, RTDIS, ST2):
cross-terminal gate edges at fallbacks (a hit refutes CONJECTURE Delta-RT-F), cross-terminal disagreements, states with |D| >= 2
and (hD), (h3D). Also stops on any crd.py violation (LAMD, CRD, CMON, FBLD, FRD) and saves the game.
Usage: rtclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
import climb, crd
from multi import rand_ckO, odd_choices
from n5x import load
climb.DEG2 = False
VIOL = ("LAMD", "CRD", "CMON", "FBLD", "FRD")

def score(g):
    for k in crd.C: crd.C[k] = 0 if k != "CRD_maxj" else -1
    try: crd.check(g, cap=4000)
    except RecursionError: return None, None
    c = dict(crd.C); return (c["DIFF"], c["RTDIS"], c["ST2"]), c

if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OUT = sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g); best, bc = score(g)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r; sc, c = score(h)
        if sc is None: continue
        if any(c[v] for v in VIOL):
            climb.save(os.path.join(OUT, f"viol_k{K}_s{SEED}.pg"), h, None, c); print("VIOLATION", t, c, flush=True); break
        if sc >= best:
            if sc > best:
                print(t, sc, "n", h.n, flush=True); climb.save(os.path.join(OUT, f"best_k{K}_s{SEED}.pg"), h, None, c)
            g, O, best = h, O2, sc
    print("done", best)
