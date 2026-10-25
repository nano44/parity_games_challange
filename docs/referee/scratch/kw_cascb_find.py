#!/usr/bin/env python3
"""REFEREE succ. 11: re-run kw_climb seed 12's lineage until a game with CASCB_switches > 0 appears; save it and print each such
switch with its full state context, for a hand check of the CASCB counter (L-RED R73 reports 0 such switches)."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, kw_probe as KP, kw_climb as KC
from collections import Counter
starts = [RE.parse(l.split()[0]) for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kw_logs/u3_starts.txt"))]
rng = random.Random(12); t0 = time.time()
g = rng.choice(starts); best, c = KC.score(g)
while time.time() - t0 < 600:
    h = rng.choice(starts) if rng.random() < 0.02 else None
    if h is None:
        try: h = KC.mutate(g, rng)
        except AssertionError: continue
    s, c = KC.score(h)
    if c["CASCB_switches"]:
        p = KC.save(h, "cascb_witness"); print("saved", p, dict((k, c[k]) for k in ("CASCB_switches", "u3_runs"))); break
    if s >= best: g, best = h, s
