#!/usr/bin/env python3
"""REFEREE successor 22: own control for packet P-N5-REALIZE (L-RED 45, l-red e609c5d2, sha1 067f06b6). Own engine rl_engine (SPEC
only); no lane code (no stab.py, ideal.py, lemck.py). Layout from packet §3.1 only: M := #Odd - 1, N := n - 3M - 6; movers 0..N-1,
gates N..N+M-1, beta N+M..N+2M-1, e N+2M..N+3M-1, c_X, c_W, K0, K1, K2, K3 = N+3M .. N+3M+5. Per state j of the N5 run from the pin start:
  STD   sigma_j = sigma_0 off the movers (standard state), tau_j = tau_0               (Theorem REALIZE induction)
  SBAR  sigma-bar_j(g) = the beta-successor of g at every gate, sigma-bar_j(K2) = K1     (Lemma SBAR)
  TAU   I_tau_j = {}                                                                    (Lemma TAU)
  ESC   (K0, K1) in I_sigma_j                                                           (Lemma ESC / K (b))
  W     W_j = W_0                                                                        (Lemma W (i))
  KEYK  I_sigma_j restricted to K is exactly {(K0, K1)}                                  (Lemma K (b))
  FL    transitions 1..L are FL, transition L+1 is a fallback (L := last standard state with a successor change)
Usage: realize_probe.py FILE.pg FILE.start"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
import s4b_probe as SB
from collections import Counter


def main(a):
    g = RE.parse(a[0]); n = g.n
    odd = [v for v in range(n) if g.owner[v] == 1]; M = len(odd) - 1; N = n - 3 * M - 6
    K0, K1, K2, K3 = N + 3 * M + 2, N + 3 * M + 3, N + 3 * M + 4, N + 3 * M + 5
    gates = range(N, N + M); beta = set(range(N + M, N + 2 * M)); movers = range(N)
    assert set(odd) == set(gates) | {K2}, "layout"
    st = RE.run(g, SB.partial_start(g, a[1])); K = len(st) - 1; cnt = Counter()
    s0, t0 = st[0]["s"], st[0]["t"]
    W = lambda k: [RE.play_value(g, [st[k]["s"][v] if g.owner[v] == 0 else st[k]["t"][v] for v in range(n)], v) for v in range(n)]
    W0 = W(0); L = None
    for j in range(K + 1):
        S = st[j]
        std = S["t"] == t0 and all(S["s"][v] == s0[v] for v in range(N, n) if g.owner[v] == 0)
        if not std: break
        cnt["std_states"] += 1
        for gt in gates:
            if S["sb"][gt] not in beta: cnt["SBAR_V"] += 1
        if S["sb"][K2] != K1: cnt["SBAR_V"] += 1
        if S["It"]: cnt["TAU_V"] += 1
        if (K0, K1) not in S["Is"]: cnt["ESC_V"] += 1
        if sorted(e for e in S["Is"] if e[0] >= N + 3 * M) != [(K0, K1)]: cnt["KEYK_V"] += 1
        if W(j) != W0: cnt["W_V"] += 1
        if j < K:
            T = st[j + 1]
            stdn = T["t"] == t0 and all(T["s"][v] == s0[v] for v in range(N, n) if g.owner[v] == 0)
            if not S["fb"] and stdn and T["s"] != S["s"]: cnt["FL_trans"] += 1; L = j + 1
            elif S["fb"]: cnt["fallback_at"] = j + 1; break
            else: cnt["OTHER_V"] += 1; break
    first_nonFL = cnt.get("fallback_at")
    print("FILE", os.path.basename(a[0]), "n", n, "N", N, "M", M, "K", K, "L_FL", L, "fallback at transition", first_nonFL)
    if L is not None and first_nonFL != L + 1: cnt["FB_V"] += 1
    if L is not None and cnt["FL_trans"] != L: cnt["FLCONSEC_V"] += 1
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))


if __name__ == "__main__":
    main(sys.argv[1:])
