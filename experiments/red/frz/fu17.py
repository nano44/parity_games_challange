#!/usr/bin/env python3
"""Box 41: per θ-run (f, |U|) and per phase (g, |U|) over files (trace only). Prints, per file, the θ-runs and phases with the largest
f − (|U| − 2) and g − (|U| − 2); then the global top. Usage: fu17.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, shrink17 as S
TOP = []
for f in sys.argv[1:]:
    try:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        X, FB, o = S.runs(g)
    except Exception: continue
    N = len(X); a = 0
    while a < N:
        b = a
        while b + 1 < N and X[b + 1][0] == X[a][0] and X[b + 1][2] == X[a][2]: b += 1
        ct = X[a][1][0]; u = sum(1 for z in X[a][0] if z == ct); gph = sum(FB[k] for k in range(a, b))
        TOP.append((gph - (u - 2), "phase", gph, u, f, a))
        s0 = a
        while s0 <= b:
            e0 = s0
            while e0 + 1 <= b and X[e0 + 1][1] == X[s0][1]: e0 += 1
            fr = sum(FB[k] for k in range(s0, e0)); TOP.append((fr - (u - 2), "theta", fr, u, f, s0)); s0 = e0 + 1
        a = b + 1
for kind in ("theta", "phase"):
    L = sorted([t for t in TOP if t[1] == kind and t[3] >= 3], reverse=True)[:8]
    print(kind, "top f-(u-2) at |U|>=3:", *L, sep="\n  ")
    print(kind, "max f:", max(TOP, key=lambda t: (t[1] == kind, t[2]))[:5])
