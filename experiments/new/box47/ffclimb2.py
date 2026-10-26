#!/usr/bin/env python3
"""Box 47 climber (DATA) against CONJECTURE XI-EARLY and HON-FF (docs/new/N5-XDIR-box47.md §8): mutate a game (box43 climb.mutate) to
maximise, lexicographically, (HONFF_V, DEEP, XI-EARLY failures, non-honest fallbacks after an honest state) of ffdeep.py on the S3 start.
XI-EARLY failure = a non-honest in-phase fallback t after a W-honest state h (h -> h+1 non-fallback) with LEV(t) < min(LEV(h)+1, n-1).
Usage: ffclimb2.py NMAX STEPS SEED OUTDIR --seed FILE.pg [--budget B]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21", "../box46"): sys.path.insert(0, os.path.join(HERE, p))
import climb, ffdeep
from multi import odd_choices
from n5x import load
climb.DEG2 = False
def score(g, budget):
    ffdeep.C = {}
    ffdeep.run(g, None, budget, "c")
    c = ffdeep.C
    return (c.get("HONFF_V", 0), c.get("DEEP", 0), c.get("nonhon_fb_after_honest", 0) - c.get("XI_AT", 0) - c.get("UNK", 0) * 0,
            c.get("nonhon_fb_after_honest", 0))
if __name__ == "__main__":
    a = sys.argv[1:]; budget = 300000
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    NMAX, STEPS, SEED = map(int, a[:3]); OUT = a[3]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(a[a.index("--seed") + 1]); NMAX = max(NMAX, g.n); O = odd_choices(g)
    best = score(g, budget); print("start", best, "n", g.n, flush=True)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r
        try: sc = score(h, budget)
        except (RecursionError, ffdeep.Unknown): continue
        if ffdeep.C.get("UNK"): continue
        if sc >= best:
            if sc > best:
                print(t, sc, "n", h.n, flush=True)
                climb.save(os.path.join(OUT, f"best_ff_n{NMAX}_s{SEED}.pg"), h, None, {"DEEP": sc[1], "XIE": sc[2]})
            g, O, best = h, O2, sc
    print("done", best, flush=True)
