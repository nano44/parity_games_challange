#!/usr/bin/env python3
"""Box 108 (L-SI 56): the ABSTRACT latch network of G_k (no chains, no keys): every mover follows Lemma LATCH with its two inputs
computed by the signal formulas of the proof (§2: X0-X7 for pref in the old state, K0-K6 for kmin in the new state, levels in W-order).
Runs it from the start and compares every state with the closed form c_k(t); cheap enough for k beyond the definition-level check.
The formulas themselves are checked against the definition (chains, tuple keys) by check108.py (counter STATIC) for k <= 12.
Usage: abs108.py KLO KHI"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gk108, check108

def step(k, names, S):
    """one step of the abstract network; S: name -> option; returns the new dict"""
    sig = check108.signals(k, S); N = dict(S)
    pf = {n: check108.pref_formula(k, S, n, sig) for n in names}
    def upd(n):
        if pf[n] != S[n]: N[n] = check108.kmin_formula(k, N, n, check108.signals(k, N))
    # W-order: level 0; then level j: u_j, v_j, e_j (they read K_(j-1) of the new state); latches of index j sit two levels higher and
    # read E(j+1) and K_j of the new state, so all block movers and e's first (ascending j), then the latches.
    upd("u0"); upd("v0")
    for j in range(1, k):
        for t in ("u", "v", "e"):
            if f"{t}{j}" in S: upd(f"{t}{j}")
    for j in range(1, k):
        for t in ("y", "yb", "yp", "ypb"):
            if f"{t}{j}" in S: upd(f"{t}{j}")
    return N

if __name__ == "__main__":
    for k in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        G, names = gk108.build(k); S = {n: G["start"][i] for i, n in enumerate(names)}; t = 0; bad = 0; T = 2 ** k - 2
        while t <= T + 2:
            if t <= T and tuple(S[n] for n in names) != check108.closed(k, t, names): bad += 1
            N = step(k, names, S)
            if N == S: break
            S = N; t += 1
        print(f"ABS108 G_{k} N {G['N']} L_abstract {t} want {T} closed_form_mismatches {bad}", flush=True)
