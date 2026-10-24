#!/usr/bin/env python3
"""L-SI box 7: CONJECTURE (JU2) (docs/si/N5-C-box7.md §11). Inside a phase on 𝒞^1O, let k -> k+1 be non-tame with (h) at k and
w_{k+1} = w_k; ℓ := lev(θ_k, θ_{k+1}); r := rank u*_k = lev(θ_k, w_k). Always ℓ <= r (θ_k ◁ θ_{k+1} ⊴ w). (JU2): if ℓ < r then
k+1 -> k+2 is in the phase, non-tame, w unchanged, and lev(θ_{k+1}, θ_{k+2}) = rank u*_{k+1} (= r).
Consequence if true: in-scope non-tame transitions <= 2 (n + 1) per maximal run with w constant and (h) (u* strictly drops at a jump of
level rank u*, or θ reaches w). Prints the counts and every failure. Usage: ju2.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dpot import *

def scan_u(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, f"{name}: not one-Odd-choice"
    Ed = n5.Engine(n5.dual(g)); c = dict(jumps=0, at_u=0, below_u=0, ju2_ok=0, ju2_fail=0, above_u=0); fails = []
    for a in out:
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W
        a["h"] = (not oncycle(g, a["s"], a["sb"], o)) and (not oncycle(g, a["s"], a["t"], o)) and a["Xi"][o][0] == W[o][0]
    def nontame(i):
        a, b = out[i], out[i + 1]; M = a["M"]
        return any(coarse(b["Xi"][v], M) != coarse(a["Xi"][v], M) for v in range(n))
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if a["key"] != b["key"] or not a["h"] or a["W"][o] != b["W"][o] or not nontame(i): continue
        c["jumps"] += 1; l = lev(a["Xi"][o], b["Xi"][o]); r = lev(a["Xi"][o], a["W"][o])
        if l == r: c["at_u"] += 1; continue
        if l > r: c["above_u"] += 1; fails.append((name, i, "above", l, r)); continue
        c["below_u"] += 1
        ok = i + 2 < len(out) and out[i + 2]["key"] == b["key"] and b["W"][o] == out[i + 2]["W"][o] and nontame(i + 1) \
            and lev(b["Xi"][o], out[i + 2]["Xi"][o]) == lev(b["Xi"][o], b["W"][o])
        c["ju2_ok" if ok else "ju2_fail"] += 1
        if not ok: fails.append((name, i, "JU2", l, r))
    return c, fails

if __name__ == "__main__":
    T = {}; F = []
    for p in sys.argv[1:]:
        c, f = scan_u(load(p), os.path.basename(p)); F += f
        for k, v in c.items(): T[k] = T.get(k, 0) + v
    print("TOTAL", T); print("failures", F[:20])
