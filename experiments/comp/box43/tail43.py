#!/usr/bin/env python3
"""L-COMP box 43 item 3: the TAIL transformation. TAIL_h(G): every option of G whose Ξ-target is X (the sink) is retargeted to a new
mover A_top; the tail is a chain of new movers A_top, …, A_1, A_0 at levels Lmax + h, …, 1, 0 (Lmax = G's largest level), each with ONE
option: A_j (j ≥ 1) has W-target A_(j−1) and Ξ-target A_j ITSELF with an even β (so the β-face closes an Even-won cycle and Odd must
take the escape e(A_j)); A_0 (level 0) has W-target c_W and Ξ-target X. So every play that ended at the sink now ends
… → A_top → e → A_(top−1) → e → … → A_0 → β → K0, and its Π gains the same e-vertices; the h e-vertices of the tail movers above level
Lmax are more relevant than every e-vertex of G ([E-LEV]: e-priorities ordered by (level, gate index)). The tail's gate and β ranks are
the lowest. Purpose: each value change of a sink-ending play keeps its most relevant difference z and gains h more elements above z, so
its depth (L-SI box 100 §3) rises by at least h.
Usage: tail43.py G.json H OUT.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box39")]
from mut39 import flat, unflat, canon


def tail(G, h):
    G = canon(G); N, lev = G["N"], list(G["lev"]); O = flat(G); Lmax = max(lev); top = Lmax + h
    ids = {j: N + j for j in range(top + 1)}; lev = lev + list(range(top + 1)); N += top + 1      # movers need not be ordered by level
    lo_g = min(o["gate"] for o in O); lo_b = min(o["br"] for o in O)
    for o in O:
        if o["xt"] == -1: o["xt"] = ids[top]
    for j in range(top + 1):
        O.append(dict(x=ids[j], wt=ids[j - 1] if j else -1, xt=ids[j] if j else -1, gate=lo_g - 1 - j, br=lo_b - 1 - j, bp=0, st=True))
    return unflat(N, lev, O)


if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); G = G.get("genome", G); T = tail(G, int(sys.argv[2])); json.dump(T, open(sys.argv[3], "w"), sort_keys=True)
    print(sys.argv[3], "N", T["N"], "N+M", T["N"] + sum(map(len, T["opts"])), "levels", max(T["lev"]) + 1)
