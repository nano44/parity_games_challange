#!/usr/bin/env python3
"""L-SI succ. 6, box 11: DATA for Lemma RB (docs/si/N5-TEV-box11.md §1). For consecutive fallbacks k0 < k of a scope run S
(reltrace.runs_of) with L := M_k0 >= 0 and r > L at every state of [k0+1, k]:
  (RB)   every Even v in F_k ∩ R_k0 whose k0-successor a := σ_k0(v) lies in R̄_k has COARSE_L(Ξ_k a) = COARSE_L(Ξ_k0 a);
  (BF)   and COARSE_L(b_k v) = COARSE_L(Ξ_k0 a)  (the b-freeze used in the proof);
  (WALK) every v0 in F_k ∩ R_k0 reaches, along its k0-route, a first vertex of R̄_k whose predecessor is Even (the proof's step 4).
Also counts the ENT setting (M_k = L and a COARSE_L(θ) change in (k0, k)) and the M_k <= L premise (CLS2).
Usage: rb.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def scan(g, name):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); C = Counter(); ex = []
    for S in runs:
        fbs = [p for p, e in enumerate(S) if e["k"] == "F"]
        for p, p2 in zip(fbs, fbs[1:]):
            L = S[p]["M"]
            if L < 0 or not all(S[u]["r"] > L for u in range(p + 1, p2 + 1)): continue
            k0, k = S[p]["i"], S[p2]["i"]; A, B = out[k0], out[k]
            C["pairs"] += 1
            if S[p2]["M"] > L: C["cls2_viol"] += 1; ex.append((name, "CLS2", k0, k))
            rise = any(S[u]["lt"] > L for u in range(p + 1, p2))
            if rise: C["rise"] += 1
            if rise and S[p2]["M"] == L: C["ENT"] += 1; ex.append((name, "ENT", k0, k, L))
            Rb_k = B["R"] | {o}
            nxt0 = lambda v: A["s"][v] if g.owner[v] == 0 else A["t"][v]
            for v in range(g.n):
                if v == o or v in Rb_k or v not in A["R"]: continue
                if g.owner[v] == 0:
                    a = A["s"][v]
                    if a in Rb_k:
                        C["rb_chk"] += 1
                        if coarse(B["Xi"][a], L) != coarse(A["Xi"][a], L): C["rb_viol"] += 1; ex.append((name, "RB", k0, k, v, a))
                        if coarse(B["Xi"][B["s"][v]], L) != coarse(A["Xi"][a], L): C["bf_viol"] += 1; ex.append((name, "BF", k0, k, v))
                u, prev, steps = v, None, 0
                while u not in Rb_k:
                    prev, u = u, nxt0(u); steps += 1
                    assert steps <= g.n
                C["walk_chk"] += 1
                if g.owner[prev] != 0: C["walk_viol"] += 1; ex.append((name, "WALK", k0, k, v, prev))
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:30]: print("  ", e)
