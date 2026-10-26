#!/usr/bin/env python3
"""Box 34: re-releases. Per phase and per vertex (exits and all vertices): how many times it leaves R at an S4a step (releases) and how
often it re-joins R in between. Reports max releases of one exit per phase / per fallback-free run, max leaves of one vertex per phase /
per run, and absorb-then-release events (exit absorbed at an ε-transition, released later in the same run). Usage: rerel.py game.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from exittrace import *

def check(g, acc, name):
    tr, o = trace(g); ex = set(g.succ[o]) - {o}
    perph = {}; perrun = {}; run = 0; vph = {}; vrun = {}; absd = set()
    for t in tr:
        if not t["same"] or t["fb"]: run += 1; absd = set()
        if not t["same"]: continue
        if t["eps"] and t["sb"][0] in t["join"]: absd.add(t["sb"][0])
        if t["fb"]: continue
        for x in t["leave"]:
            perph[(t["ph"], x)] = perph.get((t["ph"], x), 0) + 1; perrun[(run, x)] = perrun.get((run, x), 0) + 1
            if x in absd: acc["absorb_then_release"] = acc.get("absorb_then_release", 0) + 1
    for d, key in ((perph, "max_exit_rel_per_phase"), (perrun, "max_exit_rel_per_run")):
        m = max(d.values(), default=0)
        if m > acc.get(key, (0,))[0]: acc[key] = (m, name)
        acc[key + "_ge2"] = acc.get(key + "_ge2", 0) + sum(1 for v in d.values() if v >= 2)

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
