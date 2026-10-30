#!/usr/bin/env python3
"""L-RED R143 (b): state-by-state trace of a mkrel2 game on n5b SPEC: sigma(y), sigma-bar(oz), tau(oz), and Xi / W of A, B, h, oz.
Usage: trace.py GAME.pg START"""
import sys, os
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
names = {}
for l in open(sys.argv[1]):
    a = l.strip().rstrip(";").split()
    if len(a) >= 5 and a[0].isdigit(): names[int(a[0])] = a[4].strip('"')
ix = {v: k for k, v in names.items()}
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
N.run(s0, t0, trace=tr, fbtrace=fb)
SG = n5b.SpecSI(g)
def top(val): return max(val[1], key=lambda x: (g.prio[x], x)) if val[1] else None
y, oz = ix["y"], ix["oz"]; A, B = g.succ[oz]; H = [w for w in g.succ[y] if w != oz][0]
for k, (s, t) in enumerate(tr):
    xi, sb = SG.evaluate_choice(list(s))
    h = n5b.pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])
    W = n5b.SpecSI(h).evaluate(list(s))
    f = lambda v, val: names[top(val[v])] if top(val[v]) is not None else "-"
    print(k, "y->", names[s[y]], "| sbar(oz)", names[sb[oz]], "tau(oz)", names[t[oz]], "| Xi A", f(A, xi), "B", f(B, xi), "h", f(H, xi),
          "oz", f(oz, xi), "| W oz", f(oz, W), "h", f(H, W), "| fb", fb[k] if k < len(fb) else "-")
