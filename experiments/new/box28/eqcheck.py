#!/usr/bin/env python3
"""Box 28: mechanical checks of Lemma XW (Ξ ⊴ W pointwise at every state), Lemma EQ (a maximal run of states with Ξ = W inside one
phase has ≤ n − 1 Ξ-changing transitions) and Lemma FBL-N (at an Even fallback with τ unchanged: every gate edge from F is flat,
i.e. λ_W(x) = x and λ_W(z) = x; under ¬H2 no gate edge F → R). Phases: (λ_Ξ, λ_U, τ(o)) constant (phaseprofile convention).
Usage: eqcheck.py N lo hi seed [--randstart]   |   eqcheck.py game.pg [start]"""
import sys, random
from fbre import *

def check(g, start, tot):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        tot["XW_checks"] += g.n; tot["XW_fail"] += sum(Xk[v] > Wk[v] for v in range(g.n))
        r = step(g, E, Ed, s, t)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), eq=Xk == Wk, Xk=Xk))
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r
        if fb and tuple(nt) == tuple(t):
            R = reach_o(g, s, t, o); h2 = not oncycle(g, s, t, o); tot["FB"] += 1
            for (x, z) in Is:
                if x in R: continue
                tot["FBL_F_edges"] += 1
                if not (W[x][0] == x and W[z][0] == x): tot["FBL_flat_fail"] += 1
                if z in R and not h2: tot["FBL_noH2_FR_fail"] += 1
        s, t = ns, nt
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]:
            k = a
            while k < i:
                if not rows[k]["eq"]: k += 1; continue
                j = k
                while j + 1 < i and rows[j + 1]["eq"]: j += 1
                vc = sum(rows[q]["Xk"] != rows[q + 1]["Xk"] for q in range(k, j))
                tot["EQ_runs"] += 1; tot["EQ_max_vc"] = max(tot["EQ_max_vc"], vc - (g.n - 1))
                if vc > g.n - 1: tot["EQ_fail"] += 1
                k = j + 1
            a = i

if __name__ == "__main__":
    a = sys.argv[1:]
    tot = dict(runs=0, XW_checks=0, XW_fail=0, FB=0, FBL_F_edges=0, FBL_flat_fail=0, FBL_noH2_FR_fail=0, EQ_runs=0, EQ_fail=0,
               EQ_max_vc=-10 ** 9)
    if a[0].endswith(".pg"):
        g = load(a[0]); check(g, readstart(a[1]) if len(a) > 1 else None, tot); tot["runs"] = 1
    else:
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[:4]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            check(g, start, tot); tot["runs"] += 1
    tot["EQ_max_excess_over_n-1"] = tot.pop("EQ_max_vc"); print(tot)
