#!/usr/bin/env python3
"""REFEREE-2 successor 6 (Opus 5.5, D15): mechanical check of packet P-N5-FBW (docs/si/P-N5-FBW-box9.md sha1 88337bd6 @ trunk e69772b).
Own code on my lane's R2-N5-LP / R2-N5-FB / R2-N5-SN tools. No lane script (fbw.py, reltrace.py, cls*.py, jclimb.py) and no REFEREE probe is
run or imported. C^1O inputs assert exactly one Odd vertex with out-degree > 1. Phase = (lambda_Xi, tau) constant.
Checks:
  POPT    at every Even S4c fallback (any game): for every gate (y, z) and also every edge (y, z) of the arena, the single switch
          sigma[y -> z] does not raise W(y) (V' <= W at y); and the full arena optimum = sigma_k (re-run of S4a's arena on the state).
  FBW     (a) l <= max(delta, -1); (b) l = -1 > delta => y own W- and Xi-cycle node; Step 1 (l > delta => W-improving at level l).
  FBWS    in-phase fallbacks with (h): every gate level <= max(r, -1); EQ => every gate at an own cycle node with level -1.
  CLS2    along every scope run: fallback levels non-increasing (all kinds); M_k <= max(r_k, -1).
  FLAT    FLAT-ALL (i)-(iv) at in-scope fallbacks with M >= 0 and (h) at k+1.
  STRETCH per scope run, per M >= 0, per maximal stretch of constant COARSE_M(Xi): each Even y is a level-M tail at most once among the
          stretch's fallbacks k with s <= k <= e (the statement's k < e, plus k = e).
  PL      blocks per scope run: (a) N <= n_E (1 + D_M); (b) first COARSE_M change of a dirty interval is an S4a eps-absorption with
          lev(theta) = O_j > M >= E_j; (c) if r > M on [f_1, f_N]: D_M <= (d_o - 1) + REL_M. PL-S per scope run.
Usage: fbw_check.py general N nmin nmax seed | c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-SN"))
import sn_check as SC
LP = SC.LP; F = SC.F; RC = F.RC; lpg = F.lpg; INF, BOT, lev, coarse = F.INF, F.BOT, F.lev, F.coarse
from si import Engine
import n5

def W_of(E, g, s, t):
    f = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]
    return [F.play_val(E, f, v)[0] for v in range(g.n)]

def arena_opt(g, s, t, Is):
    """S4a's computation re-run on the state: optimum of the arena {s(v)} u Is(v) against t (n5's dual engine call)."""
    n = g.n
    opt = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
    Er = Engine(n5.dual(lpg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(t[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else s[v] for v in range(n)]

def check_run(g, s, t, st, name, o):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    if (len(fbs), sum(fbs)) != F.n5.run(g, "n5", ({v: s[v] for v in range(g.n) if g.owner[v] == 0},
                                                   {v: t[v] for v in range(g.n) if g.owner[v] == 1}))[:2]:
        st.bad(f"{name} run differs from n5.run")
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k, S in enumerate(A): LP.extra(g, E, S, states[k][0], states[k][1], o)
    n = g.n; T = len(fbs); nE = [v for v in range(n) if g.owner[v] == 0]
    st.c["runs"] += 1; st.c["transitions"] += T
    # ---- POPT and FBW at every Even fallback (any game)
    for k in range(T):
        if not fbs[k]: continue
        S = A[k]; s0, t0 = states[k]
        if not S.Is: st.c["odd_fallbacks"] += 1; continue
        st.c["even_fallbacks"] += 1
        W = S.W
        if arena_opt(g, s0, t0, S.Is) != list(s0):
            st.c["POPT_arena_opt_differs_from_sigma_k"] += 1
            # value-level check is what P-OPT needs: compare valuations
            Wopt = W_of(E, g, arena_opt(g, s0, t0, S.Is), t0)
            if Wopt != W: st.bad(f"{name} POPT: arena optimum valuation != W_k at fallback {k}")
        arena = {y: {s0[y]} | {z for (x, z) in S.Is if x == y} for y in nE}
        for y in nE:
            for z in arena[y]:
                s1 = list(s0); s1[y] = z
                Vp = W_of(E, g, s1, t0)
                st.c["POPT_single_switch_checks"] += 1
                if E.key(Vp[y]) > E.key(W[y]): st.bad(f"{name} POPT: single switch {y}->{z} raises W(y) at {k}")
        for (y, z), l in S.gl.items():
            u = s0[y]
            d = max(lev(S.Xi[u], W[u]), lev(S.Xi[z], W[z]))
            st.c["FBW_gates"] += 1
            if not l <= max(d, -1): st.bad(f"{name} FBW(a) at {k} ({y},{z}) l={l} delta={d}")
            if l > d:
                if not (E.key(W[z]) > E.key(W[u]) and lev(W[u], W[z]) == l): st.bad(f"{name} FBW step 1 at {k} ({y},{z})")
            if l == -1 and d < -1:
                st.c["FBW_case_b"] += 1
                if not (W[y][0] == y and S.lam[y] == y): st.bad(f"{name} FBW(b) at {k} y={y}")
            if l > d: st.c["FBW_l>delta"] += 1
            if l >= 0 and l == d: st.c["FBW_tight_l>=0"] += 1
    if o is None: return
    inph = [A[k].lam == A[k + 1].lam and states[k][1] == states[k + 1][1] for k in range(T)]
    h = [S.H1 and S.H2 and S.ct == S.cw for S in A]
    r = [lev(S.Xi[o], S.W[o]) for S in A]
    so = set(g.succ[o]); d_o = len(so)
    insc = [inph[k] and h[k] and A[k + 1].H2 and A[k + 1].W[o] == A[k].W[o] for k in range(T)]
    for k in range(T):
        if not (fbs[k] and inph[k] and h[k]): continue
        S = A[k]
        st.c["FBWS_fallbacks"] += 1
        for (y, z), l in S.gl.items():
            if l > max(r[k], -1): st.bad(f"{name} FBW-S at {k} ({y},{z}) l={l} r={r[k]}")
            if r[k] == BOT and not (l == -1 and S.lam[y] == y): st.bad(f"{name} FBW-S EQ at {k} ({y},{z})")
    k = 0
    while k < T:
        if not insc[k]: k += 1; continue
        a = k
        while k < T and insc[k]: k += 1
        scope(g, E, A, states, fbs, a, k, st, name, o, r, h, nE, so, d_o)

def info(g, A, states, j, o):
    R = LP.relevant(g, A[j], A[j + 1], states[j], states[j + 1])
    Ek = max([x[1] for x in R if x[2] == "E"], default=BOT)
    Oc = [x for x in R if x[2] == "O"]
    return Ek, (Oc[0][1] if Oc else BOT)

def scope(g, E, A, states, fbs, a, b, st, name, o, r, h, nE, so, d_o):
    n = g.n
    st.c["scope_runs"] += 1
    fl = [k for k in range(a, b) if fbs[k]]
    lv = [A[k].M for k in fl]
    for i, k in enumerate(fl):
        st.c["CLS2_fallbacks"] += 1
        if r[k] >= 0: st.c["CLS2_THR_u*!=none"] += 1
        elif r[k] == -1: st.c["CLS2_u*=none"] += 1
        else: st.c["CLS2_EQ"] += 1
        if A[k].M > max(r[k], -1): st.bad(f"{name} CLS2 bound at {k}")
        if i and lv[i] > lv[i - 1]: st.bad(f"{name} CLS2 order at {k}: {lv}")
        # FLAT-ALL
        M = A[k].M
        if M >= 0 and h[k + 1]:
            st.c["FLAT_checks"] += 1
            S0, S1 = A[k], A[k + 1]
            F0 = set(range(n)) - S0.Rbar; F1 = set(range(n)) - S1.Rbar
            if not F0 <= F1: st.bad(f"{name} FLAT(i) F at {k}")
            f0 = [states[k][0][v] if g.owner[v] == 0 else states[k][1][v] for v in range(n)]
            f1 = [states[k + 1][0][v] if g.owner[v] == 0 else states[k + 1][1][v] for v in range(n)]
            for v in S1.Rbar - {o}:
                if v not in S0.Rbar: st.bad(f"{name} FLAT(i) R at {k} v={v}"); continue
                x0, x1 = v, v
                while x0 != o:
                    if f0[x0] != f1[x0]: st.bad(f"{name} FLAT(i) route at {k} v={v}"); break
                    x0 = f0[x0]
            if coarse(S0.Xi[o], M) != coarse(S1.Xi[o], M): st.bad(f"{name} FLAT(ii) at {k}")
            if any(coarse(S0.Xi[v], M) != coarse(S1.Xi[v], M) for v in range(n)): st.bad(f"{name} FLAT(iii) at {k}")
            if S1.M > M: st.bad(f"{name} FLAT(iv) at {k}")
    # ---- STRETCH and PL per level
    blocks_ok = True
    for M in sorted({m for m in lv if 0 <= m < INF}):
        # STRETCH on maximal constant-COARSE_M stretches
        t = a
        while t <= b:
            s_ = t
            while t < b and all(coarse(A[t].Xi[v], M) == coarse(A[t + 1].Xi[v], M) for v in range(n)): t += 1
            e = t
            seen = set()
            for k in fl:
                if s_ <= k <= e and A[k].M == M:
                    tails = {y for (y, z), l in A[k].gl.items() if l == M}
                    st.c["STRETCH_tail_checks"] += len(tails)
                    if tails & seen: st.bad(f"{name} STRETCH at {k} M={M}: repeated tails {tails & seen}")
                    seen |= tails
            t += 1
        # PL
        blk = [k for k in fl if A[k].M == M]
        N = len(blk)
        st.c["PL_blocks"] += 1; st.mx["max_block_size"] = max(st.mx["max_block_size"], N)
        D = 0; first = []
        for i in range(N - 1):
            fi, fj = blk[i], blk[i + 1]
            ch = [j for j in range(fi + 1, fj) if any(coarse(A[j].Xi[v], M) != coarse(A[j + 1].Xi[v], M) for v in range(n))]
            if ch: D += 1; first.append(ch[0])
        nEc = len(nE)
        if N > nEc * (1 + D): st.bad(f"{name} PL(a) M={M} N={N} D={D}")
        st.c["PL_dirty_intervals"] += D
        for j in first:
            Ek, Ok = info(g, A, states, j, o)
            x0 = A[j].sbar[o]
            if fbs[j] or not (Ok > M >= Ek) or lev(A[j].Xi[o], A[j + 1].Xi[o]) != Ok or x0 in A[j].Rbar or x0 not in A[j + 1].Rbar:
                st.bad(f"{name} PL(b) at {j} M={M}")
        if N and not all(r[x] > M for x in range(blk[0], blk[-1] + 1)): blocks_ok = False
        if N and all(r[x] > M for x in range(blk[0], blk[-1] + 1)):
            st.c["PL_c_blocks"] += 1
            rel = sum(len(((A[x].Rbar - A[x + 1].Rbar) & so) - {o}) for x in blk[:-1])
            if D > (d_o - 1) + rel: st.bad(f"{name} PL(c) M={M} D={D} rel={rel}")
    pos = [k for k in fl if A[k].M >= 0]
    if pos and blocks_ok:
        relS = sum(len(((A[x].Rbar - A[x + 1].Rbar) & so) - {o}) for x in fl)
        st.c["PLS_checks"] += 1
        if len(pos) > len(nE) * (n * d_o + relS): st.bad(f"{name} PL-S")

def main():
    st = F.Stats(); st.ex = {}; mode = sys.argv[1]
    if mode in ("general", "c1o"):
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            if mode == "general": g = F.rand_general(rng, rng.randint(nmin, nmax)); o = None
            else:
                rg, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7); g = F.to_lpg(rg); assert F.one_odd(g) == o
            s, t = F.start(g, rng, rng.random() < 0.6); check_run(g, s, t, st, f"{mode}{seed}#{i}", o)
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); o = F.one_odd(g); rng = random.Random(7)
        for r_ in range(runs):
            s, t = F.start(g, rng, r_ > 0); check_run(g, s, t, st, f"{os.path.basename(path)}#{r_}", o)
    F.report(st)

if __name__ == "__main__":
    main()
