#!/usr/bin/env python3
"""Box 40 (L-RED successor 16): own checker of L-SI succ. 6's docs/si/N5-LV-box11.md (sha1 407c5520), written from the text. Trace =
sox.trace (asserted = n5.run) unless given. Setting (LV): k an in-scope S4c fallback (k -> k+1 a transition of a scope run S, Even's
fallback), THR at k (θ ◁ w), M_k = -1. Counted: in-scope THR fallbacks (thr), those with M = -1 (lv), EQ fallbacks (eq) and their M.
At every (LV) fallback, each gate (y, z), s := σ_k(y), is classified (Proposition LV-SHAPE):
  (α) s, z in F_k, λ(y) = y and y is its own W-cycle node;
  (γ) s in F_k, z in R̄_k, r_k = -1, λ(y) = y = W-cycle node of y, P(W_k z) = ∅;
  (β) y in R_k, z in F_k, rank o < rank c, π_s^k has no vertex of rank > rank c, P(Ξ_k z) = P(θ_k), and W_k(s) ▷ W_k(z) at level r_k
      when r_k >= 0.
  LVX = a gate of none of the kinds (or s, z both in R̄_k); LVCN = an (LV) fallback with no (β) gate where Ξ_{k+1} != Ξ_k or k+1 is
  not the last state of its phase (CN-LAST, as stated in §1). beta_fb = (LV) fallbacks with a (β) gate; maxbeta = most per scope run.
  P-N5-LV2 (docs/si/P-N5-LV2-box12.md, sha1 3b23a41f): LVNONE = a scope run with more than n·n_E + 1 THR fallbacks with r = -1 (u* = none);
  SCOPEFB = more than 4·n·n_E + 3 S4c fallbacks in one scope run (n_E = number of Even vertices). maxnone / maxs4c = the per-run maxima.
Usage: lv16.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, pg, n5
from si import Engine
from sox import BOT, INF, lev

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
    def tplay(k, v):
        x, seen, out = v, set(), []
        while x not in seen: seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else S[k][1][x]
        return out
    def hplay(k, v):
        x, seen = v, set()
        while x not in seen: seen.add(x); x = S[k][0][x] if g.owner[x] == 0 else sb[k][x]
        return seen
    Rb = [frozenset({o} | {v for v in range(n) if o in tplay(k, v)}) for k in range(N)]
    H1 = [o not in hplay(k, sb[k][o]) for k in range(N)]; H2 = [o not in tplay(k, S[k][1][o]) for k in range(N)]
    h = [H1[k] and H2[k] and Wv[k][o][0] == lam[k][o] for k in range(N)]
    r = [lev(Xi[k][o], Wv[k][o]) for k in range(N)]
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    scope = [inph[k] and h[k] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    rk = E.rank
    C, ex = {}, {}
    def bad(nm, x): C[nm] = C.get(nm, 0) + 1; ex.setdefault(nm, x)
    nE = sum(1 for v in range(n) if g.owner[v] == 0)
    st = dict(n=n, it=len(FB), fb=sum(FB), thr=0, lv=0, eq=0, eqM={}, beta_fb=0, maxbeta=0, kinds={}, nE=nE, maxnone=0, maxs4c=0,
              none_bound=n * nE + 1, s4c_bound=4 * n * nE + 3)
    k = 0
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        nb = 0; nnone = 0; ns4c = 0
        for t in range(k, e + 1):
            if not FB[t] or S[t][0] == S[t + 1][0]: continue          # Even (S4c) fallbacks only
            ns4c += 1
            gs = [(y, z, lev(Xi[t][S[t][0][y]], Xi[t][z])) for y, z in E.improving(S[t][0], Xi[t])]
            Mt = max((l for *_, l in gs), default=BOT)
            if r[t] == BOT: st["eq"] += 1; st["eqM"][Mt] = st["eqM"].get(Mt, 0) + 1; continue
            if not E.key(Xi[t][o]) < E.key(Wv[t][o]): bad("NOTTHR", t); continue
            st["thr"] += 1; nnone += r[t] == -1
            if Mt != -1: continue
            st["lv"] += 1; c = Xi[t][o][0]; F = set(range(n)) - Rb[t]; anyb = False
            for y, z, l in gs:
                s = S[t][0][y]; kind = None
                if s in F and z in F and lam[t][y] == y and Wv[t][y][0] == y: kind = "a"
                elif s in F and z in Rb[t] and r[t] == -1 and lam[t][y] == y and Wv[t][y][0] == y and Wv[t][z][1] == 0: kind = "g"
                elif y in Rb[t] and y != o and z in F and rk[o] < rk[c] and Xi[t][z][1] == Xi[t][o][1] \
                        and all(rk[x] <= rk[c] for x in tplay(t, s)[:tplay(t, s).index(o)] if o in tplay(t, s)) \
                        and (r[t] < 0 or (E.key(Wv[t][s]) > E.key(Wv[t][z]) and lev(Wv[t][s], Wv[t][z]) == r[t])): kind = "b"
                st["kinds"][kind] = st["kinds"].get(kind, 0) + 1
                if kind is None: bad("LVX", (t, y, z))
                anyb |= kind == "b"
            if anyb: st["beta_fb"] += 1; nb += 1
            elif Xi[t + 1] != Xi[t] or (t + 1 < N - 1 and inph[t + 1]): bad("LVCN", t)
        st["maxbeta"] = max(st["maxbeta"], nb); st["maxnone"] = max(st["maxnone"], nnone); st["maxs4c"] = max(st["maxs4c"], ns4c)
        if nnone > st["none_bound"]: bad("LVNONE", (k, nnone))
        if ns4c > st["s4c_bound"]: bad("SCOPEFB", (k, ns4c))
        k = e + 1
    return dict(C=C, ex=ex, **st)

if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        try: r = analyse(g)
        except AssertionError as er: print(os.path.basename(f), "ASSERT", er, flush=True); continue
        print(os.path.basename(f), {k: r[k] for k in ("n", "it", "fb", "thr", "lv", "eq", "eqM", "beta_fb", "maxbeta", "kinds", "nE", "maxnone", "maxs4c")}, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for kk in ("thr", "lv", "eq", "beta_fb"): tot[kk] = tot.get(kk, 0) + r[kk]
        tot["maxbeta"] = max(tot.get("maxbeta", 0), r["maxbeta"])
        for kk, v in r["C"].items(): tot[kk] = tot.get(kk, 0) + v
        tot["files"] = tot.get("files", 0) + 1
    print("TOTAL", tot)
