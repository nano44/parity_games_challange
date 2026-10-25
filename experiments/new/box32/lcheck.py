#!/usr/bin/env python3
"""Box 32 consolidated checker for docs/new/N5-L-box32.md (N5 SPEC run, C^1O asserted). Inside every phase (λ_Ξ, λ_U, τ(o) constant):
  RELEVANT changes at k -> k+1: Even y with σ_{k+1}(y) != σ_k(y) and λ_k(y) != y; Odd u with σ̄_{k+1}(u) != σ̄_k(u) and λ_k(u) != u.
  L_k = max lev(Ξ_k(old), Ξ_k(new)) over relevant changes (⊥ = none: a NU transition).
  Lemma U:   COARSE_{L_k}(Ξ_{k+1}) = COARSE_{L_k}(Ξ_k); NU transitions have Ξ_{k+1} = Ξ_k.
  Lemma HI:  gate edges of level > L_k (with level and direction) are the same at k and k+1.
  Lemma UL:  L_k is never attained by an Even switch at the rank-L_k vertex.
  Lemma GR:  at an Even-attained L_k = l >= 0, the attaining y goes from l-bad to l-good; G_l never loses a vertex at a transition with L_k <= l.
  Theorem LP: per phase T <= (m - n + 1)(T_rel + 1), T_rel <= (n + 1)(rho + 1) n (n - 1) + eps, rho = rises in the relevant subsequence,
             eps = relevant transitions whose level is attained only by Odd changes.
  CONJECTURE NO-WAKE: consecutive relevant transitions k < k' (only NU between), no fallback in [k, k'], R constant on [k, k'+1]:
             every relevant Even switch at k' has level <= L_k.
  Census per phase: T, NU, f, S_o (σ̄(o) changes), S_o_rel (those with λ(o) != o), X (R changes), rho, eps, and rises split by cause (fallback / σ̄(o) / crossing / other).
Usage: lcheck.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mblock import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d

def good(x, l, pr): return ((x[1] >> l) & 1) == (1 if pr % 2 == 0 else 0)

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); n = g.n; m = sum(len(s) for s in g.succ); byrank = {E.rank[v]: v for v in range(n)}
    ev = [E.evaluate(tuple(r["s"])) for r in rows]; Is = [E.improving(tuple(r["s"]), ev[i][0]) for i, r in enumerate(rows)]
    info = []
    for k in range(len(rows) - 1):
        a, c = rows[k], rows[k + 1]
        if a["ph"] != c["ph"]: info.append(None); continue
        Xi, Xi2, sb, sb2 = ev[k][0], ev[k + 1][0], ev[k][1], ev[k + 1][1]
        L, src = -2, []
        for y in range(n):
            if g.owner[y] == 0 and a["s"][y] != c["s"][y] and Xi[y][0] != y:
                l = lev(Xi[a["s"][y]], Xi[c["s"][y]])
                if l > L: L, src = l, []
                if l == L: src.append(("E", y))
        for u in range(n):
            if g.owner[u] == 1 and sb[u] != sb2[u] and Xi[u][0] != u:
                l = lev(Xi[sb[u]], Xi[sb2[u]])
                if l > L: L, src = l, []
                if l == L: src.append(("O", u))
        bump(acc, "tr")
        if L == -2:
            bump(acc, "NU")
            if Xi2 != Xi: bump(acc, "U_FAIL_nu")
        else:
            if L >= 99: bump(acc, "L_INF_FAIL")
            elif not all(coarse(Xi2[v], L) == coarse(Xi[v], L) for v in range(n)): bump(acc, "U_FAIL"); acc.setdefault("ex_U", (name, k))
            hi = lambda s, X, I: {(y, z): (lev(X[s[y]], X[z])) for y, z in I if lev(X[s[y]], X[z]) > L}
            if L < 99 and hi(a["s"], Xi, Is[k]) != hi(c["s"], Xi2, Is[k + 1]): bump(acc, "HI_FAIL"); acc.setdefault("ex_HI", (name, k))
            if L >= 0:
                u = byrank[L]
                if any(t == "E" and y == u for t, y in src): bump(acc, "UL_FAIL")
                for t, y in src:
                    if t == "E" and not (not good(Xi[y], L, g.prio[u]) and good(Xi2[y], L, g.prio[u])): bump(acc, "GR_FAIL"); acc.setdefault("ex_GR", (name, k, y))
        if L != -2 and L < 99:
            for l in range(max(L, 0), n):
                pu = g.prio[byrank[l]]
                if any(E.rank[Xi[v][0]] < l and good(Xi[v], l, pu) and not good(Xi2[v], l, pu) for v in range(n)): bump(acc, "GR_LOSS_FAIL"); break
        info.append(dict(L=L, src=src, fb=bool(a["fb"]), x=a["R"] != c["R"], so=sb[o] != sb2[o], sor=sb[o] != sb2[o] and Xi[o][0] != o))
    k = 0
    while k < len(info):
        if info[k] is None: k += 1; continue
        j = k
        while j + 1 < len(info) and info[j + 1] is not None: j += 1
        ph = info[k:j + 1]; T = len(ph); rel = [i for i, x in enumerate(ph) if x["L"] != -2]
        rho = eps = 0; cause = {}
        for t in range(len(rel)):
            x = ph[rel[t]]
            if all(s[0] == "O" for s in x["src"]): eps += 1
            if t == 0: continue
            p = ph[rel[t - 1]]; seg = ph[rel[t - 1]:rel[t] + 1]
            Ev = max([lev(ev[k + rel[t]][0][rows[k + rel[t]]["s"][y]], ev[k + rel[t]][0][rows[k + rel[t] + 1]["s"][y]]) for s, y in x["src"] if s == "E"] +
                     [lev(ev[k + rel[t]][0][rows[k + rel[t]]["s"][y]], ev[k + rel[t]][0][rows[k + rel[t] + 1]["s"][y]]) for y in range(n)
                      if g.owner[y] == 0 and rows[k + rel[t]]["s"][y] != rows[k + rel[t] + 1]["s"][y] and ev[k + rel[t]][0][y][0] != y] + [-2])
            nofb = not any(s["fb"] for s in seg); nox = not any(s["x"] for s in seg)
            if nofb and nox:
                bump(acc, "NW_checked")
                if Ev > p["L"]: bump(acc, "NOWAKE_FAIL"); acc.setdefault("ex_NW", (name, k + rel[t]))
            if x["L"] > p["L"]:
                rho += 1
                c_ = "fb" if not nofb else ("so" if Ev <= p["L"] else ("x" if not nox else "OTHER"))
                cause[c_] = cause.get(c_, 0) + 1; bump(acc, "rise_" + c_)
        Trel = len(rel); nu = T - Trel; f = sum(s["fb"] for s in ph); So = sum(s["so"] for s in ph); Sor = sum(s["sor"] for s in ph); X = sum(s["x"] for s in ph)
        if Trel > (n + 1) * (rho + 1) * n * (n - 1) + eps: bump(acc, "LP_FAIL_rel")
        if T > (m - n + 1) * (Trel + 1): bump(acc, "LP_FAIL_nu")
        if eps > Sor: bump(acc, "EPS_GT_SOrel")
        if rho > 2 * f + Sor + 2 * X: bump(acc, "RHO_GT_2f_SOrel_2X")
        for key, val in (("max_T", T), ("max_rho", rho), ("max_So", So), ("max_So_rel", Sor), ("max_nu", nu), ("max_X", X)):
            if val > acc.get(key, (0,))[0]: acc[key] = (val, dict(n=n, T=T, nu=nu, f=f, So=So, So_rel=Sor, X=X, rho=rho, eps=eps), name)
        k = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            assert len([v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]) == 1, f
            check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
