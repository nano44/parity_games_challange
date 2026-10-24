#!/usr/bin/env python3
"""L-SI box 6: gate-edge levels after carries. For each state k after a carry of level L (w constant), list the gate edges
(Ξ_k-improving Even edges) with lev(Ξ_k(σ_k y), Ξ_k(z)) > L, classified: CYC (z's honest play passes y: cycle-closing), CN (y = λ_Ξ(y)),
RF/FR/RR/FF (membership of y, z). Usage: gatelev.py game.pg ..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carries import *

def hplay(g, s, sb, z):
    nxt = lambda v: s[v] if g.owner[v] == 0 else sb[v]
    p = [z]; seen = {z}
    while True:
        u = nxt(p[-1])
        if u in seen: return set(p)
        p.append(u); seen.add(u)

def scan5(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    x, y = max(ph, key=lambda p: p[1] - p[0]); L = None; w0 = None; cnt = Counter(); states = 0; bad_states = 0
    for k in range(x, y + 1):
        r = rows[k]; Xi, sb = E.evaluate(tuple(r["s"])); r["Xi"] = Xi
        if r["w"] != w0: L, w0 = None, r["w"]
        if L is not None:
            states += 1; bad = False
            for v in range(g.n):
                if g.owner[v] != 0: continue
                for z in g.succ[v]:
                    if z == r["s"][v] or E.key(Xi[z]) <= E.key(Xi[r["s"][v]]): continue
                    l = lev(E, Xi[r["s"][v]], Xi[z])
                    if l > L:
                        bad = True
                        cyc = v in hplay(g, r["s"], sb, z); cn = Xi[v][0] == v
                        m = ("R" if v in r["R"] else "F") + ("R" if (z in r["R"] or z == o) else "F")
                        cnt[("CYC" if cyc else "nocyc") + ("/CN" if cn else "") + "/" + m] += 1
            bad_states += bad
        if k < y and any(rows[k + 1]["Wk"][v] < r["Wk"][v] for v in range(g.n)):
            Xi1, _ = E.evaluate(tuple(rows[k + 1]["s"]))
            S, act, pas = classify(g, rows, k, o)
            L = max([lev(E, Xi[v], Xi1[v]) for v, kd in act if kd.startswith("L")] or [-3])
    return states, bad_states, cnt

if __name__ == "__main__":
    T = Counter(); S = B = 0
    for p in sys.argv[1:]:
        s, b, c = scan5(p); S += s; B += b; T.update(c)
    print("states after a carry:", S, "states with a gate edge above L:", B); print(dict(T))
