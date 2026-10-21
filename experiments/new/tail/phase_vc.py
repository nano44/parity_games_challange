#!/usr/bin/env python3
"""Box 10: for one-player switch-best runs (phase_trace.sbstep), per λ-phase count ALL steps and VALUE-CHANGING steps (some Ω changes); Theorem PH
says value-changing steps per phase ≤ n − 1. Prints the max per instance and flags violations. Usage: phase_vc.py game.pg [...] (uses .start)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
from phase_trace import sbstep
for p in sys.argv[1:]:
    g = pg.read(p); s = [g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n)]
    if os.path.exists(p + ".start"):
        for tok in open(p + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); s[a] = b
    E = Engine(g); ph = []; cur = [0, 0]; prev = None; k = 0
    while True:
        ns, lam, vs = sbstep(g, E, s)
        if prev is not None and lam != prev: ph.append(tuple(cur)); cur = [0, 0]
        prev = lam
        if ns is None: break
        vs2, _ = E.evaluate(tuple(ns)); changed = any(E.key(vs2[v]) != E.key(vs[v]) for v in range(g.n))
        cur[0] += 1; cur[1] += changed; s = ns; k += 1
    ph.append(tuple(cur))
    mx = max(ph); mxvc = max(c for _, c in ph)
    flag = "VIOLATION of Theorem PH" if mxvc > g.n - 1 else "ok"
    print(f"{os.path.basename(p)} n={g.n} steps={k} phases={len(ph)} max phase (steps, value-changing)={mx} max value-changing per phase={mxvc} (n-1={g.n-1}) {flag}")
