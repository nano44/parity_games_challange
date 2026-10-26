#!/usr/bin/env python3
"""Box 45 climber (DATA) for CONJECTURE REC (docs/new/N5-NEP-box45.md §2): mutate a 𝒞^kO game (box43 climb.mutate) to maximise,
lexicographically, (max recurrences of one sigma-bar|Q configuration in one phase, max N_ep), from the S3 start (nep.py).
With --d0: recurrences of the configuration tau|Q (D = empty) only. Usage: recclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg] [--d0]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, HERE)
import climb, nep
from multi import rand_ckO, odd_choices
from n5x import load
climb.DEG2 = False
D0 = "--d0" in sys.argv
def score(g):
    for k in list(nep.C): nep.C[k] = 0.0 if isinstance(nep.C[k], float) else 0
    try: nep.check(g, None)
    except RecursionError: return None
    return ((nep.C["MULT_D0MAX"] if D0 else nep.C["MULTMAX"]), nep.C["NEPMAX"])
if __name__ == "__main__":
    K, NMAX, STEPS, SEED = map(int, sys.argv[1:5]); OUT = sys.argv[5]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g); best = score(g)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r; sc = score(h)
        if sc is None: continue
        if sc >= best:
            if sc > best:
                print(t, sc, "n", h.n, flush=True)
                climb.save(os.path.join(OUT, f"best_rec{'0' if D0 else ''}_k{K}_n{NMAX}_s{SEED}.pg"), h, None, {"MULT": sc[0], "NEP": sc[1]})
            g, O, best = h, O2, sc
    print("done", best)
