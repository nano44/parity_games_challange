#!/usr/bin/env python3
"""L-RED successor 24: survey of f, RF and R1 (fbphase.reuse modes) over .pg files (own .start if present, else S3).
Usage: r1survey.py FILE.pg ...   prints one line per game and a summary."""
import sys, os, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
import trace as T, fbphase as F
class TO(Exception): pass
def h(*a): raise TO()
signal.signal(signal.SIGALRM, h)
best = {"f": (0, ""), "rf": (0, ""), "r1": (0, "")}; ok = 0
for p in sys.argv[1:]:
    try:
        g = T.pg.parse("".join(l for l in open(p) if not l.lstrip().startswith("%")))
        if g.n > 200: continue
        sp = p[:-3] + ".start"; st = T.readstart(sp) if os.path.exists(sp) else ({}, {})
        st = tuple({v: w for v, w in d.items() if v < g.n and w in g.succ[v] and g.owner[v] == o} for d, o in zip(st, (0, 1)))
        signal.alarm(20)
        F.MODE_RF = 1; f, rf = F.reuse(g, st, cap=5000)
        F.MODE_RF = 2; f2, r1 = F.reuse(g, st, cap=5000)
        signal.alarm(0); ok += 1
        for k, v in (("f", f), ("rf", rf), ("r1", r1)):
            if v > best[k][0]: best[k] = (v, "%s n=%d f=%d" % (p, g.n, f))
        if r1 > 0: print("R1>0", p, g.n, f, rf, r1, flush=True)
    except Exception as e:
        signal.alarm(0)
print("games", ok, "max f", best["f"], "max RF", best["rf"], "max R1", best["r1"])
