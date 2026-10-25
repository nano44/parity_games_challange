#!/usr/bin/env python3
"""Box 33: wakes (P-N5-LP §3 definition) per phase, with a per-wake description used by Lemma WK (docs/new/N5-K-box33.md):
for each wake y: a -> z at k': state type, parity of λ_W(y), whether W changes at a or z at k' (W_{k'+1} vs W_{k'}), whether W changes
anywhere on R, whether the switch is a W-tie (W_{k'+1}(z) = W_{k'+1}(a)), and whether it is an event (U3/U23: kind change or c_w switch).
Phase key and rows as box32 (rows_w; key (λ_Ξ, λ_U, τ(o))). Usage: wakes.py game.pg ... ; as a module: wakes(g) -> (list, rows, o)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

def wakes(g):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n; out = []
    Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
    prev = None; ph = 0
    for k in range(len(Ls)):
        if Ls[k] is None: prev = None; ph += 1; continue
        if Ls[k] == -2: continue
        if prev is not None:
            seg = range(prev, k + 1)
            if not any(rows[j]["fb"] for j in seg) and all(rows[j]["R"] == rows[j + 1]["R"] for j in seg):
                a_, c_ = rows[k], rows[k + 1]; R = set(a_["R"]) | {o}; cw = a_["W"][o][0]
                for y in range(n):
                    if g.owner[y] != 0 or a_["s"][y] == c_["s"][y] or ev[k][0][y][0] == y: continue
                    a, z = a_["s"][y], c_["s"][y]; l = lev(ev[k][0][a], ev[k][0][z])
                    if l <= Ls[prev]: continue
                    st = "rf" if a_["rfX"] and a_["rfW"] else ("U2" if a_["rfW"] else ("U3" if a_["rfX"] else "U23"))
                    kind = lambda nx, v: cw in route(nx, v, o)
                    evt = st in ("U3", "U23") and any(g.owner[v] == 0 and a_["s"][v] != c_["s"][v] and
                              (v == cw or kind(a_["nxt"], v) != kind(c_["nxt"], v)) for v in R if v != o)
                    out.append(dict(ph=ph, k=k, y=y, a=a, z=z, lev=l, Lprev=Ls[prev], st=st, cw=cw, cwodd=g.prio[a_["W"][y][0]] % 2,
                                    wAZ=a_["W"][a] != c_["W"][a] or a_["W"][z] != c_["W"][z],
                                    wR=any(a_["W"][v] != c_["W"][v] for v in R), tie=c_["W"][a] == c_["W"][z], event=evt,
                                    lenonly=all(E.rank[cw] > E.rank[v] for v in R if v != cw)))
        prev = k
    return out, rows, o

if __name__ == "__main__":
    for f in sys.argv[1:]:
        g = load(f)
        for w in wakes(g)[0]: print(os.path.basename(f), w)
