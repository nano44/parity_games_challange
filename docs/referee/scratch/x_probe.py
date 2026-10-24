#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-X (docs/new/P-N5-X-box28.md, pin afc88b0). n5x.step read-only. Phase = (λ_Ξ, λ_U, τ) constant.
State types: EQ (Ξ = W), THR ((h), Ξ != W), OTHER (not (h), Ξ != W). Checks, per phase:
 XW     Ξ ⊴ W at every vertex of every state
 NF     every value-changing S4c fallback with no OTHER endpoint is a crossing
 F1     per F-interval (no crossing / OTHER-touching transition inside): #transitions changing Ξ on F <= |F| - 1
 F2     EQ -> THR inside an F-interval: τ(o) in F and Ξ(τ(o)) changes; THR -> THR with a w-change: Ξ(τ(o)) changes
 EQB    per maximal EQ block inside an F-interval: value-changing transitions inside <= n - 1
 SUB    per sub-block (THR block cut at w-changes, inside an F-interval): value-changing (Ξ or W) transitions <= n - 2;
        THF: every θ-change inside a sub-block is a transition at which W changes on F (the referee's θ-free step for R19 (f))
 TX     per phase: transitions <= (3n²(1+X+O)+X+O+1)(4n(n-1)+1), and value-changing <= 3n²(1+X+O)+X+O
Usage: x_probe.py game.pg [start] | x_probe.py N nmin nmax seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter

def rows_of(g, start):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        Xk = tuple(E.key(x) for x in Xi); Wk = tuple(E.key(x) for x in W)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        typ = "EQ" if Xk == Wk else ("THR" if h else "OTHER")
        rows.append(dict(s=tuple(s), t=tuple(t), Xk=Xk, Wk=Wk, typ=typ, R=frozenset(Rset(g, s, t, o)), fb=0,
                         ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), tuple(t))))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = list(r[0]), list(r[1])
    return E, o, rows

def run(g, start, cnt):
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1, "not in C^1O: exactly one Odd choice vertex required"
    E, o, rows = rows_of(g, start); n = g.n
    for r in rows:
        cnt["XW_checks"] += n; cnt["XW_FAIL"] += sum(r["Xk"][v] > r["Wk"][v] for v in range(n))
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[a]["ph"]:
            phase(g, o, rows[a:i], cnt); a = i

def phase(g, o, P, cnt):
    n = g.n; T = len(P) - 1
    if T < 1: return
    cnt["phases"] += 1
    vc = lambda a, b: a["Xk"] != b["Xk"] or a["Wk"] != b["Wk"]
    cross = [P[k]["R"] != P[k + 1]["R"] for k in range(T)]
    oth = [P[k]["typ"] == "OTHER" or P[k + 1]["typ"] == "OTHER" for k in range(T)]
    X, O = sum(cross), sum(c or d for c, d in zip(cross, oth)) - sum(cross)  # O counted apart from X (each cut once)
    Oraw = sum(oth)
    VC = sum(vc(P[k], P[k + 1]) for k in range(T))
    cnt["TX_checks"] += 1; cnt["max_phase_len"] = max(cnt["max_phase_len"], T); cnt["max_X"] = max(cnt["max_X"], X); cnt["max_O"] = max(cnt["max_O"], Oraw)
    if VC > 3 * n * n * (1 + X + Oraw) + X + Oraw: cnt["TX_VC_FAIL"] += 1
    if T > (3 * n * n * (1 + X + Oraw) + X + Oraw + 1) * (4 * n * (n - 1) + 1): cnt["TX_FAIL"] += 1
    for k in range(T):
        a, b = P[k], P[k + 1]
        if a["fb"] and not oth[k] and vc(a, b):
            cnt["NF_checks"] += 1
            if not cross[k]: cnt["NF_FAIL"] += 1
    # F-intervals
    k = 0
    while k <= T:
        j = k
        while j < T and not cross[j] and not oth[j]: j += 1
        interval(g, o, P[k:j + 1], cnt); k = j + 1

def interval(g, o, I, cnt):
    n = g.n; L = len(I) - 1
    if L < 1: return
    F = [v for v in range(n) if v not in I[0]["R"]]; tau_o = I[0]["t"][o]
    cnt["intervals"] += 1
    fch = sum(any(I[k]["Xk"][v] != I[k + 1]["Xk"][v] for v in F) for k in range(L))
    if not F: cnt["intervals_F_empty"] += 1
    cnt["F1_max_slack_min"] = min(cnt.get("F1_max_slack_min", 99), max(0, len(F) - 1) - fch)
    if fch > max(0, len(F) - 1): cnt["F1_FAIL"] += 1
    vc = lambda a, b: a["Xk"] != b["Xk"] or a["Wk"] != b["Wk"]
    for k in range(L):
        a, b = I[k], I[k + 1]
        if a["typ"] == "EQ" and b["typ"] == "THR":
            cnt["F2a_checks"] += 1
            if tau_o not in F or a["Xk"][tau_o] == b["Xk"][tau_o]: cnt["F2a_FAIL"] += 1
        if a["typ"] == "THR" and b["typ"] == "THR" and a["Wk"][o] != b["Wk"][o]:
            cnt["F2b_checks"] += 1
            if a["Xk"][tau_o] == b["Xk"][tau_o]: cnt["F2b_FAIL"] += 1
    # blocks
    k = 0
    while k <= L:
        j = k
        while j < L and I[j + 1]["typ"] == I[k]["typ"]: j += 1
        B = I[k:j + 1]
        if I[k]["typ"] == "EQ":
            c = sum(vc(B[i], B[i + 1]) for i in range(len(B) - 1)); cnt["EQB_blocks"] += 1
            cnt["EQB_max"] = max(cnt["EQB_max"], c)
            if c > n - 1: cnt["EQB_FAIL"] += 1
        else:
            i = 0
            while i < len(B):
                m = i
                while m + 1 < len(B) and B[m + 1]["Wk"][o] == B[i]["Wk"][o]: m += 1
                S = B[i:m + 1]
                if len(S) > 1:
                    cnt["SUB_blocks"] += 1
                    c = sum(vc(S[q], S[q + 1]) for q in range(len(S) - 1)); cnt["SUB_max"] = max(cnt["SUB_max"], c)
                    if c > n - 2: cnt["SUB_FAIL"] += 1
                    for q in range(len(S) - 1):
                        if S[q]["Xk"][o] != S[q + 1]["Xk"][o]:
                            cnt["THF_checks"] += 1
                            if all(S[q]["Wk"][v] == S[q + 1]["Wk"][v] for v in F): cnt["THF_FAIL"] += 1
                        if S[q]["fb"]: cnt["SUB_flat_fallbacks"] += 1
                i = m + 1
        k = j + 1

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
