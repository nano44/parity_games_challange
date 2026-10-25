#!/usr/bin/env python3
"""Box 32: CONJECTURE NO-WAKE (docs/new/N5-L-box32.md §4) and the per-phase census for the reduction T <= poly(n)(1 + f + S_o + X).
NO-WAKE: if transitions k = i-1 and i are both S4a steps (no fallback) of one phase, and R_{i-1} = R_i = R_{i+1} (no crossing), then every
Even switch at i has level <= L_{i-1}. Per phase: T transitions, f fallbacks, S_o = #transitions changing σ̄(o), X = #crossings (R changes),
rho = #used-level rises, eps = #exceptional (used level only from σ̄(o)). Usage: nowake.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rises import *

def census(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
    Ls = []; tops = []
    for i in range(len(rows) - 1):
        if rows[i]["ph"] != rows[i + 1]["ph"]: Ls.append(None); tops.append(None); continue
        L, top = usedL(g, rows, ev, i); Ls.append(L); tops.append(top)
    for i in range(1, len(Ls)):
        if Ls[i] is None or Ls[i - 1] is None: continue
        if rows[i - 1]["fb"] or rows[i]["fb"]: continue
        if not (rows[i - 1]["R"] == rows[i]["R"] == rows[i + 1]["R"]): continue
        acc["nw_checked"] = acc.get("nw_checked", 0) + 1
        a, c = rows[i], rows[i + 1]
        for y in range(n):
            if g.owner[y] == 0 and a["s"][y] != c["s"][y] and lev(ev[i][0][a["s"][y]], ev[i][0][c["s"][y]]) > Ls[i - 1]:
                acc["NOWAKE_FAIL"] = acc.get("NOWAKE_FAIL", 0) + 1; acc.setdefault("ex_nw", (name, i, y)); break
    i = 0
    while i < len(Ls):
        if Ls[i] is None: i += 1; continue
        j = i
        while j + 1 < len(Ls) and Ls[j + 1] is not None: j += 1
        T = j - i + 1; f = sum(rows[k]["fb"] > 0 for k in range(i, j + 1))
        So = sum(ev[k][1][o] != ev[k + 1][1][o] for k in range(i, j + 1)); X = sum(rows[k]["R"] != rows[k + 1]["R"] for k in range(i, j + 1))
        rho = sum(Ls[k] > Ls[k - 1] for k in range(i + 1, j + 1)); eps = sum(1 for k in range(i, j + 1) if tops[k] and all(t[0] == "O" for t in tops[k]))
        r = T / (1 + f + So + X)
        if r > acc.get("max_T_over_1fSoX", (0,))[0]: acc["max_T_over_1fSoX"] = (round(r, 2), n, T, f, So, X, rho, eps, name)
        for key, val in (("max_So", So), ("max_X", X), ("max_T", T)):
            if val > acc.get(key, (0,))[0]: acc[key] = (val, n, T, f, So, X, rho, eps, name)
        i = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            census(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if len([v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]) != 1: continue
            census(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
