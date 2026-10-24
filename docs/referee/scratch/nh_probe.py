#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-NH (docs/new/P-N5-NH-box30.md, pin c7981ee). n5x.step read-only. Phase = (λ_Ξ, λ_U, τ) constant;
crossing-free interval I = maximal run of a phase with R constant. Checks:
 F1o   per I: transitions changing Ξ on F <= max(0, |F| - 1)
 TC    (i) H1 <=> λ_Ξ(o) in F, H2 <=> τ(o) in F, both constant on I; (ii) under H2, (h) constant on I and OTHER all-or-none;
       (iii) H1 and not H2 => all OTHER; (iv) not H1, not H2: EQ <=> θ = w, and EQ -> OTHER changes w
 PC    under H2 on I: #(θ, w)-pieces <= max(1, |F|)
 P3    route-form pieces J (honest: H1 or λ_Ξ(o) = o; W: H2 or λ_W(o) = o; θ, w constant) with c_θ more relevant than c_w:
       last κ change at index <= |R|; transitions with a Ξ-change on R <= (n + 1)|R|; split by whether the W frame is in route form by
       H2 or by λ_W(o) = o (the referee's case P3-1)
 CW    in pieces with λ_W(o) = o (not H2): κ-strict gate edges (x, z) with x on o's W-cycle at a state k with k+1 in J (P3-1 says none)
 SG    every switched Even y in R with λ_Ξ(y) != y gains strictly in Ξ (used for ROI: an R-only W-change needs a switch on R)
Usage: nh_probe.py game.pg [start] | nh_probe.py N nmin nmax seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter

def route(nxt, v, o):
    p = []
    while v != o and v not in p: p.append(v); v = nxt[v]
    return p

def wcycle(nxt, o):
    x, seen = nxt[o], [o]
    while x != o and x not in seen: seen.append(x); x = nxt[x]
    return set(seen) if x == o else set()

def rows_of(g, start):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Xk = tuple(E.key(x) for x in Xi); Wk = tuple(E.key(x) for x in W)
        H1 = not oncycle(g, s, sb, o); H2 = not oncycle(g, s, t, o); H3 = Xi[o][0] == W[o][0]
        h = H1 and H2 and H3
        nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]
        rows.append(dict(s=tuple(s), t=tuple(t), Xi=Xi, W=W, Xk=Xk, Wk=Wk, H1=H1, H2=H2, h=h, nxt=nxt,
                         typ="EQ" if Xk == Wk else ("THR" if h else "OTHER"), R=frozenset(Rset(g, s, t, o)),
                         Is=E.improving(tuple(s), Xi), fb=0, ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), tuple(t))))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = list(r[0]), list(r[1])
    return E, o, rows

def run(g, start, cnt):
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1, "not in C^1O: exactly one Odd choice vertex required"
    E, o, rows = rows_of(g, start); n = g.n
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        for y in range(n):
            if g.owner[y] == 0 and y in a["R"] and a["s"][y] != b["s"][y] and a["Xi"][y][0] != y and b["Xi"][y][0] != y:
                cnt["SG_checks"] += 1
                if not a["Xk"][y] < b["Xk"][y]: cnt["SG_FAIL"] += 1
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[a]["ph"] or rows[i]["R"] != rows[a]["R"]:
            if i - a >= 1: interval(g, E, o, rows[a:i], cnt)
            a = i

def interval(g, E, o, I, cnt):
    n = g.n; R = I[0]["R"]; F = [v for v in range(n) if v not in R]; L = len(I) - 1; Fs = set(F)
    cnt["intervals"] += 1
    fch = sum(any(I[k]["Xk"][v] != I[k + 1]["Xk"][v] for v in F) for k in range(L))
    if fch > max(0, len(F) - 1): cnt["F1o_FAIL"] += 1
    # TC
    for r in I:
        lx = r["Xi"][o][0]
        if r["H1"] != (lx in Fs): cnt["TCi_H1_FAIL"] += 1
        if r["H2"] != (r["t"][o] in Fs): cnt["TCi_H2_FAIL"] += 1
    if len({r["H1"] for r in I}) > 1 or len({r["H2"] for r in I}) > 1: cnt["TCi_const_FAIL"] += 1
    H1, H2 = I[0]["H1"], I[0]["H2"]; cnt["iv_%d%d" % (H1, H2)] += 1
    if H2:
        if len({r["h"] for r in I}) > 1: cnt["TCii_h_FAIL"] += 1
        if len({r["typ"] == "OTHER" for r in I}) > 1: cnt["TCii_other_FAIL"] += 1
        ch = sum(I[k]["Xk"][o] != I[k + 1]["Xk"][o] or I[k]["Wk"][o] != I[k + 1]["Wk"][o] for k in range(L))
        cnt["PC_checks"] += 1
        if ch + 1 > max(1, len(F)): cnt["PC_FAIL"] += 1
    if H1 and not H2 and any(r["typ"] != "OTHER" for r in I): cnt["TCiii_FAIL"] += 1
    if not H1 and not H2:
        for r in I:
            if (r["typ"] == "EQ") != (r["Xk"][o] == r["Wk"][o]): cnt["TCiv_eq_FAIL"] += 1
        for k in range(L):
            if I[k]["typ"] == "EQ" and I[k + 1]["typ"] == "OTHER":
                cnt["TCiv_trans"] += 1
                if I[k]["Wk"][o] == I[k + 1]["Wk"][o]: cnt["TCiv_w_FAIL"] += 1
    # route-form pieces
    def rform(r):
        return (r["H1"] or r["Xi"][o][0] == o) and (r["H2"] or r["W"][o][0] == o)
    k = 0
    while k <= L:
        if not rform(I[k]): k += 1; continue
        j = k
        while j < L and rform(I[j + 1]) and I[j + 1]["Xk"][o] == I[k]["Xk"][o] and I[j + 1]["Wk"][o] == I[k]["Wk"][o]: j += 1
        piece(g, E, o, I[k:j + 1], R, cnt)
        k = j + 1

def piece(g, E, o, J, R, cnt):
    n = g.n; ct, cw = J[0]["Xi"][o][0], J[0]["W"][o][0]
    if not E.rank[ct] > E.rank[cw]: cnt["pieces_other_order"] += 1; return
    tag = "H2" if J[0]["H2"] else "Wself"
    cnt["P3_pieces_" + tag] += 1; cnt["P3_maxlen"] = max(cnt["P3_maxlen"], len(J) - 1)
    top = E.rank[ct]
    kap = lambda r, v: frozenset(u for u in route(r["nxt"], v, o) if E.rank[u] > top)
    K = [{v: kap(r, v) for v in R if v != o} for r in J]
    last = 0
    for i in range(1, len(J)):
        if K[i] != K[i - 1]: last = i
    if last > len(R): cnt["P3_freeze_FAIL"] += 1
    cnt["P3_max_last"] = max(cnt["P3_max_last"], last)
    xr = sum(any(J[i]["Xk"][v] != J[i + 1]["Xk"][v] for v in R) for i in range(len(J) - 1))
    cnt["P3_max_Xi_R"] = max(cnt["P3_max_Xi_R"], xr)
    if xr > (n + 1) * len(R): cnt["P3_count_FAIL"] += 1
    if tag == "Wself":
        for i in range(len(J) - 1):
            r = J[i]; C = wcycle(r["nxt"], o)
            for x, z in r["Is"]:
                if x in C and x != o and z in R:
                    cnt["CW_gate_edges"] += 1
                    kx, kz = K[i].get(r["nxt"][x], frozenset()) if r["nxt"][x] != o else frozenset(), K[i].get(z, frozenset()) if z != o else frozenset()
                    if kx != kz: cnt["CW_kappa_strict_FAIL"] += 1

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0].endswith(".pg"):
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 and not a[1].startswith("-") else None, cnt)
        print(a[0], "n", g.n, dict(sorted(cnt.items()))); sys.exit()
    N, lo, hi, seed = map(int, a[0:4]); RS = "--randstart" in a; rng = random.Random(seed)
    for _ in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.1)
        if g is None: continue
        st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
              {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        cnt["runs"] += 1; run(g, st, cnt)
    print(dict(sorted(cnt.items())))
