#!/usr/bin/env python3
"""Box 44 climber (DATA): mutate a C^kO game (box43 climb.mutate) to maximise, lexicographically, (max in-phase fallbacks in one
phase, TA violations, max rho) from fbf.py; stops and saves on any fbf.py violation of a PROVED statement (CNO_V, EXS_V, FEX_V,
RED_V). With --obj rho: (max rho per phase, FMAX, NLATE). With --obj ta: (TA violations, max rho, FMAX) (an instance against per-terminal THETA-AFTER).
Usage: fbclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg] [--obj ta]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
import climb, fbf
from multi import rand_ckO, odd_choices
from n5x import load
climb.DEG2 = False
OBJ = sys.argv[sys.argv.index("--obj") + 1] if "--obj" in sys.argv else "f"

def score(g):
    for k in fbf.C: fbf.C[k] = 0
    try: fbf.check(g, cap=4000)
    except RecursionError: return None, None
    c = dict(fbf.C)
    if OBJ == "rho": return (c["RHOMAX"], c["FMAX"], c["NLATE"]), c
    if OBJ == "ta": return (c["TA_V"], c["RHOMAX"], c["FMAX"]), c
    return (c["FMAX"], c["TA_V"], c["RHOMAX"]), c

if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OUT = sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g); best, _ = score(g)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r; sc, c = score(h)
        if sc is None: continue
        if any(c[v] for v in ("CNO_V", "EXS_V", "FEX_V", "RED_V", "REDL_V")):
            climb.save(os.path.join(OUT, f"viol_k{K}_s{SEED}.pg"), h, None, c); print("VIOLATION", t, c, flush=True); break
        if sc >= best:
            if sc > best: print(t, sc, "n", h.n, flush=True); climb.save(os.path.join(OUT, f"best_{OBJ}_k{K}_n{NMAX}_s{SEED}.pg"), h, None, c)
            g, O, best = h, O2, sc
    print("done", best)
