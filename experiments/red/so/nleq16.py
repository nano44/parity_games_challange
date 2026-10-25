#!/usr/bin/env python3
"""Box 40 (L-RED successor 16): own checker of L-SI succ. 6's CONJECTURE NL= (docs/si/N5-STR-box11.md §3, sha1 c7b9c671; target shape in
docs/si/N5-STR2-box11.md, sha1 b6ed9476): R29 / P-N5-CLS §5 Lemma NL (i)-(iii) with "r_j > L" weakened to "r_j >= L". Written from the
text. Trace = sox.trace (asserted = n5.run). Setting checked: every in-phase S4a step j -> j+1 inside a scope run S (sox3 / rx16), after
an in-scope fallback k0 of S (the last one before j), L := M_k0 >= 0 (not ∞), (h) at j, (A_j): every gate (y, z) at j with z in F_j has
level <= L. Claims, split by r_j > L (Lemma NL, PROVED: a sanity check) and r_j = L (NL=):
  (i)   COARSE_L(Ξ_{j+1} v) = COARSE_L(Ξ_j v) for every v not in R̄_{j+1}
  (ii)  R_j ⊆ R̄_{j+1}                       (iii) (A_{j+1})
Also: LEAVE_SHAPE = an (ii) failure at r_j = L where a leaving Even p switches to e* = τ(o) (N5-STR2 §2's shape).
Usage: nleq16.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, pg, n5
from si import Engine
from sox import BOT, INF, lev, coarse

def analyse(g, cap=5000, trace=None):
    oc = sox.oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n
    if trace is None:
        S, FB, E = sox.trace(g, cap)
        it, fb, *_ = n5.run(g, cap=cap); assert (it, fb) == (len(FB), sum(FB)), "trace differs from n5.run"
    else: S, FB, E = trace
    N = len(S); ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]; Wv = []
    for s, t in S:
        succ = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
        Wv.append(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(s)[0])
    def play(k, v, odd):
        x, seen = v, set()
        while x not in seen:
            seen.add(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if odd else sb[k][x])
        return seen
    Rb = [frozenset({o} | {v for v in range(n) if o in play(k, v, True)}) for k in range(N)]
    H1 = [o not in play(k, sb[k][o], False) for k in range(N)]; H2 = [o not in play(k, S[k][1][o], True) for k in range(N)]
    h = [H1[k] and H2[k] and Wv[k][o][0] == lam[k][o] for k in range(N)]
    r = [lev(Xi[k][o], Wv[k][o]) for k in range(N)]
    gates = [None] * N
    def G(k):
        if gates[k] is None: gates[k] = [(y, z, lev(Xi[k][S[k][0][y]], Xi[k][z])) for y, z in E.improving(S[k][0], Xi[k])]
        return gates[k]
    def M(k): return max((l for _, _, l in G(k)), default=BOT)
    def A(k, L): return all(l <= L for y, z, l in G(k) if z not in Rb[k])
    scope = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] and h[k] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    C, ex = {}, {}
    def bad(nm, x): C[nm] = C.get(nm, 0) + 1; ex.setdefault(nm, x)
    st = dict(n=n, it=len(FB), fb=sum(FB), gt=0, eq=0, eq_noA=0, lt=0)
    k = 0
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        L = None
        for j in range(k, e + 1):
            if FB[j]:
                L = M(j); L = None if (L == INF or L < 0) else L; continue
            if L is None or not h[j]: continue
            if r[j] < L: st["lt"] += 1; continue
            if not A(j, L):
                if r[j] == L: st["eq_noA"] += 1
                continue
            tag = "GT" if r[j] > L else "EQ"; st["gt" if r[j] > L else "eq"] += 1
            for v in set(range(n)) - Rb[j + 1]:
                if coarse(Xi[j + 1][v], L) != coarse(Xi[j][v], L): bad(tag + "_i", (j, L, v)); break
            lv = (Rb[j] - {o}) - Rb[j + 1]
            if lv:
                bad(tag + "_ii", (j, L, sorted(lv)))
                if tag == "EQ" and any(g.owner[p] == 0 and S[j + 1][0][p] == S[j][1][o] for p in lv): bad("LEAVE_SHAPE", (j, L, sorted(lv)))
            if not A(j + 1, L): bad(tag + "_iii", (j, L))
        k = e + 1
    return dict(C=C, ex=ex, **st)

if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        try: r = analyse(g)
        except AssertionError as er: print(os.path.basename(f), "ASSERT", er, flush=True); continue
        print(os.path.basename(f), {k: r[k] for k in ("n", "it", "fb", "gt", "eq", "eq_noA", "lt")}, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for kk in ("gt", "eq", "eq_noA", "lt"): tot[kk] = tot.get(kk, 0) + r[kk]
        for kk, v in r["C"].items(): tot[kk] = tot.get(kk, 0) + v
        tot["files"] = tot.get("files", 0) + 1
    print("TOTAL", tot)
