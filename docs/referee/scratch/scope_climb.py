#!/usr/bin/env python3
"""REFEREE climb for P-N5-SCOPE (own code; mutations from l2_climb.py; one Odd choice vertex asserted on every candidate).
Fitness: (max scope runs in one phase, max NH1 fallbacks in one phase, max WCH in one phase). Every improvement re-run through scope_probe.
Usage: scope_climb.py seed minutes nmin nmax [start.pg]"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_climb as C, scope_probe as SP

def run(g):
    c = Counter(); SP.general(g, c, "c"); SP.c1o(g, c, "c"); return c

seed, mins, lo, hi = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
rng = random.Random(seed); t0 = time.time(); out = os.environ.get("OUT", "."); top = None; steps = 0; checked = 0
while time.time() - t0 < 60 * mins:
    g = U.load(sys.argv[5]) if len(sys.argv) > 5 else None
    while g is None: g = U.rand_c1o(rng, lo, hi)
    c = run(g); f = (c["max_scope_runs"], c["max_NH1_fb"], c["max_WCH"]); stall = 0
    while stall < 3000 and time.time() - t0 < 60 * mins:
        h = C.mutate(g, rng); steps += 1
        if h is None: continue
        try: ch = run(h)
        except AssertionError: continue
        checked += 1; fails = {k: v for k, v in ch.items() if "FAIL" in k}
        fh = (ch["max_scope_runs"], ch["max_NH1_fb"], ch["max_WCH"])
        if fails: p = os.path.join(out, "scfail_s%d_n%d.pg" % (seed, h.n)); C.save(h, p); print("FAIL", fails, p, flush=True)
        if fh >= f:
            stall = 0 if fh > f else stall + 1
            if top is None or fh > top: top = fh; p = os.path.join(out, "scc_s%d_%d_%d_%d_n%d.pg" % ((seed,) + fh + (h.n,))); C.save(h, p); print("HIT", fh, p, flush=True)
            g, f = h, fh
        else: stall += 1
print("END seed", seed, "top", top, "steps", steps, "checked", checked, flush=True)
