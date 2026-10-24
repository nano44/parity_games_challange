#!/usr/bin/env python3
"""REFEREE §C check for N-U1-3 (R2-N5-U1 §6): at an S4c fallback transition k -> k+1 inside a phase (tau unchanged) from an EQ state
(Xi_k = W_k), W_{k+1} >= W_k pointwise (and W_{k+1}(o) >= W_k(o)). Also records fallbacks at OTHER states for contrast.
Usage: eqfb_check.py rand N nmin nmax seed | eqfb_check.py game.pg ..."""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U

def run(g, cnt):
    o = U.assert_c1o(g); E, Ed, out, it, fb = U.trace(g); rows = U.states(g, E, Ed, out, o)
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if not a["fb"]: continue
        inph = a["ph"] == b["ph"] and a["t"] == b["t"]
        eq = a["Xk"] == a["Wk"]
        tag = ("EQ" if eq else "nonEQ") + ("_inphase" if inph else "_leaves")
        cnt["fb_" + tag] += 1
        if eq and a["t"] == b["t"]:
            if any(b["Wk"][v] < a["Wk"][v] for v in range(g.n)): cnt["EQfb_Wdecrease_FAIL"] += 1
            if b["Wk"][o] != a["Wk"][o]: cnt["EQfb_w_changes"] += 1
            if not (not a["H1"] and not a["H2"]): cnt["EQfb_not_nH1nH2"] += 1

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is not None: run(g, cnt)
    else:
        for p in a: run(U.load(p), cnt)
    print(dict(sorted(cnt.items())))
