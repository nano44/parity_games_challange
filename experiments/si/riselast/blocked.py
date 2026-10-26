#!/usr/bin/env python3
"""L-SI succ. 5, box 10: BLOCKED edges (DATA). At a state, an Even edge (v, u) is BLOCKED if it is W-improving (W(u) ▷ W(σ v)) but not
a gate (Ξ(u) ⊴ Ξ(σ v)). Checks: (BL-FORM) every blocked edge at an in-scope state has v ∈ F, u ∈ R̄; (BL-FB) every in-scope THR
fallback has a blocked edge; (BL-X, data question) some blocked tail lies on the σ_k-play of x0 = σ̄_k(o). Prints per in-scope state: fb flag, r, #gates, #RF, #blocked and the levels lev(Ξ σv, Ξ u) of blocked edges.
Usage: blocked.py [-v] game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def scan(g, name, verbose):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); E = n5.Engine(g); C = Counter(); ex = []
    for S in runs:
        L = None
        for e in S:
            i = e["i"]; a = out[i]; R = a["R"]; Rb = R | {o}; X = a["Xi"]; W = a["W"]; s = a["s"]
            gs = set(a["Is"]); bl = []
            for v in range(g.n):
                if g.owner[v] != 0: continue
                for u in set(g.succ[v]):
                    if u == s[v] or (v, u) in gs: continue
                    if E.key(W[u]) > E.key(W[s[v]]): bl.append((v, u, lev(X[s[v]], X[u])))
            C["states"] += 1; C["blocked"] += len(bl)
            for v, u, l in bl:
                if not (v not in Rb and u in Rb): C["BLFORM_viol"] += 1; ex.append((name, "BL-FORM", i, v, u))
            r = lev(X[o], W[o])
            if e["k"] == "F":
                C["fb"] += 1
                if r >= -1:
                    C["thr_fb"] += 1
                    if not bl: C["BLFB_viol"] += 1; ex.append((name, "BL-FB", i, r))
                    play = []; q = a["sb"][o]                      # (BL-X) a blocked tail on x0's σ_k-play
                    while q not in play and q != o:
                        play.append(q); q = s[q] if g.owner[q] == 0 else g.succ[q][0]
                    onp = [(v, u, l) for v, u, l in bl if v in play]
                    if onp: C["BLX_ok"] += 1
                    else: C["BLX_fail"] += 1; ex.append((name, "BL-X", i, r, e["M"]))
                L = e["M"]
            if verbose:
                print(name, i, e["k"], "r", r, "L", L, "lt", e["lt"], "gates", len(gs), "blocked", len(bl), sorted(l for *_, l in bl))
    return C, ex

if __name__ == "__main__":
    v = "-v" in sys.argv; T = Counter(); X = []
    for p in [a for a in sys.argv[1:] if a != "-v"]:
        c, e = scan(load(p), os.path.basename(p), v); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
