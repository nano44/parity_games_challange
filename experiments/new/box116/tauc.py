#!/usr/bin/env python3
"""L-NEW box 116: tau-stretch statistics of one N5 run. TCH = transitions changing tau (= number of tau-stretches - 1); OSW = Odd
switches (pairs (o, k) with tau_(k+1)(o) != tau_k(o)); ORET = Odd returns (o enters a target it held at an earlier state); MAXOSW =
max Odd switches at one vertex; FB = S4c fallbacks; TFB = tau-changes made by a fallback; ITERS. Usage: tauc.py G.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
held = {o: {t[o]} for o in range(n) if own[o] == 1}; K = TCH = OSW = ORET = FB = TFB = 0; per = {}
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, Is, It, fb, _, _ = r; FB += fb
    if nt != t:
        TCH += 1; TFB += fb
        for o in range(n):
            if own[o] == 1 and nt[o] != t[o]:
                OSW += 1; per[o] = per.get(o, 0) + 1; ORET += nt[o] in held[o]; held[o].add(nt[o])
    s, t = ns, nt; K += 1
print(f"TAUC {os.path.basename(sys.argv[1])} n {n} ITERS {K} TCH {TCH} OSW {OSW} ORET {ORET} MAXOSW {max(per.values() or [0])} FB {FB} TFB {TFB}")
