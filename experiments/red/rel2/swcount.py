#!/usr/bin/env python3
"""L-RED R144: time accounting of an N5 run (n5b SPEC). Prints |F| (iterations), n, total Even switches SW, the switch-count histogram
(vertices switching 1, 2, 3+ times), max per-vertex switches, frozen stretches (sigma-bar constant; tau and fallback breaks too) and their
max / mean length. Usage: swcount.py GAME.pg START"""
import sys, os
from collections import Counter
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
N.run(s0, t0, trace=tr, fbtrace=fb); SG = n5b.SpecSI(g)
sw = Counter()
for (s, t), (s2, t2) in zip(tr, tr[1:]):
    for v in range(g.n):
        if g.owner[v] == 0 and s[v] != s2[v]: sw[v] += 1
sb = [tuple(SG.evaluate_choice(list(s))[1][v] for v in range(g.n) if g.owner[v] == 1) for s, t in tr]
lens, cur = [], 0
for k in range(len(tr) - 1):
    if sb[k] == sb[k + 1] and tr[k][1] == tr[k + 1][1] and not fb[k]: cur += 1
    else: lens.append(cur); cur = 0
lens.append(cur)
h = Counter(min(c, 3) for c in sw.values())
print(f"SWCOUNT {os.path.basename(sys.argv[1])} n {g.n} F {len(tr) - 1} SW {sum(sw.values())} sw1 {h[1]} sw2 {h[2]} sw3+ {h[3]} maxSW {max(sw.values(), default=0)} "
      f"stretches {len(lens)} maxlen {max(lens)} meanlen {sum(lens) / len(lens):.2f}")
