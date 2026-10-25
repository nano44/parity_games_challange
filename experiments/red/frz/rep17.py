#!/usr/bin/env python3
"""Box 41: per phase, the vertices switched by in-phase Even fallbacks; counts vertices switched by ≥ 2 fallbacks of one phase, and
fallbacks that switch no vertex of U ∖ {o, c_θ} (e.g. cycle-node switches outside U). Trace only. Usage: rep17.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox
acc = {}
def bump(k, v=1): acc[k] = acc.get(k, 0) + v
for f in sys.argv[1:]:
    try:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        S, FB, E = sox.trace(g, cap=3000)
    except Exception: continue
    o = sox.oddchoice(g)[0]; X = [E.evaluate(tuple(s))[0] for s, t in S]; N = len(S); a = 0
    while a < N:
        b = a
        while b + 1 < N and [x[0] for x in X[b + 1]] == [x[0] for x in X[a]] and S[b + 1][1] == S[a][1]: b += 1
        ct = X[a][o][0]; U = {z for z in range(g.n) if X[a][z][0] == ct}; cnt = {}
        for k in range(a, b):
            if not FB[k]: continue
            bump("fallbacks"); sw = [v for v in range(g.n) if g.owner[v] == 0 and S[k][0][v] != S[k + 1][0][v]]
            inner = [v for v in sw if v in U - {o, ct}]
            if not inner: bump("fb_no_inner_U_switch"); print("NOINNER", f, k, len(U), [(v, v in U, X[k][v][0] == v) for v in sw], flush=True)
            for v in inner: cnt[v] = cnt.get(v, 0) + 1
        rep = {v: c for v, c in cnt.items() if c >= 2}
        if rep: bump("phases_with_repeat"); print("REPEAT", f, a, len(U), sum(FB[a:b]), rep, flush=True)
        a = b + 1
print(acc)
