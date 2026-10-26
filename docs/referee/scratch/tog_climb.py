#!/usr/bin/env python3
"""REFEREE climb for P-N5-TOG (own code; mutations from l2_climb.py; one Odd choice vertex asserted on every candidate).
Fitness: max H1-toggles in one phase (ties: total toggles). Every improvement is re-run through tog_probe (all checks).
Usage: tog_climb.py seed minutes nmin nmax [start.pg]"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_probe as L2, l2_climb as C, tog_probe as TP

def fit(g):
    E, o, st, it, fb = L2.states(g); T = len(st) - 1; best = tot = 0; k = 0
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j + 1 < T and inph[j + 1]: j += 1
        t = sum(st[x]["H1"] != st[x + 1]["H1"] for x in range(k, j + 1)); best = max(best, t); tot += t; k = j + 1
    return (best, tot)

seed, mins, lo, hi = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
rng = random.Random(seed); t0 = time.time(); out = os.environ.get("OUT", "."); cnt = Counter(); top = (0, 0); steps = 0
while time.time() - t0 < 60 * mins:
    g = U.load(sys.argv[5]) if len(sys.argv) > 5 else None
    while g is None: g = U.rand_c1o(rng, lo, hi)
    f = fit(g); stall = 0
    while stall < 3000 and time.time() - t0 < 60 * mins:
        h = C.mutate(g, rng); steps += 1
        if h is None: continue
        try: fh = fit(h)
        except AssertionError: continue
        if fh >= f:
            stall = 0 if fh > f else stall + 1
            if fh > f:
                c = Counter(); TP.run(h, c, "climb"); cnt["checked"] += 1
                fails = {k: v for k, v in c.items() if "FAIL" in k}
                if fails or fh > top:
                    top = max(top, fh); p = os.path.join(out, "togc_s%d_%d_%d_n%d.pg" % (seed, fh[0], fh[1], h.n)); C.save(h, p)
                    print("HIT", fh, p, fails, flush=True)
            g, f = h, fh
        else: stall += 1
print("END seed", seed, "top", top, "steps", steps, dict(cnt), flush=True)
