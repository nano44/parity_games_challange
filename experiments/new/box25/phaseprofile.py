#!/usr/bin/env python3
"""Box 27: per joint λ-phase (τ fixed): iterations, θ-changes, w-changes, non-(h) transitions, throttled transitions, number of
(θ, w)-stretches, longest throttled stretch. Usage: phaseprofile.py game.pg [start]"""
from common import *
from wdrop_h import oncycle
g = load(sys.argv[1]); st0 = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; st, _ = trace(g, st0)
E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); rows = []
for s, t in st:
    Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t); _, W = wvals(g, s, t)
    h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
    rows.append(((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o]), h))
ph = []; a = 0
for i in range(1, len(rows) + 1):
    if i == len(rows) or rows[i][0] != rows[i - 1][0]: ph.append((a, i - 1)); a = i
for a, b in ph:
    if b - a < 4: continue
    thc = sum(rows[k][1] != rows[k - 1][1] for k in range(a + 1, b + 1)); wc = sum(rows[k][2] != rows[k - 1][2] for k in range(a + 1, b + 1))
    noh = sum(not (rows[k][3] and rows[k + 1][3]) for k in range(a, b)); thr = sum(rows[k][3] and rows[k][1] < rows[k][2] for k in range(a, b))
    st_ = 1 + sum((rows[k][1], rows[k][2]) != (rows[k - 1][1], rows[k - 1][2]) for k in range(a + 1, b + 1))
    print(f"{os.path.basename(sys.argv[1])} n {g.n} phase {a}..{b} ({b-a} it): θ-changes {thc}, w-changes {wc}, (θ,w)-stretches {st_}, non-(h) transitions {noh}, throttled transitions {thr}")
