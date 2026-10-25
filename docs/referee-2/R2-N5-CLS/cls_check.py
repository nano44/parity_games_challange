#!/usr/bin/env python3
"""REFEREE-2 successor 6 (Opus 5.5, D15): mechanical check of packet P-N5-CLS (docs/si/P-N5-CLS-box8.md sha1 5bbfd872 @ trunk 486107a).
Own code on my lane's R2-N5-LP/lp_check.py and R2-N5-FB/fb_check.py (SPEC run asserted = n5.run; Xi_k from si.py's Engine; W, R-bar,
levels, COARSE, gate levels, M_k, (h), scope runs computed from the definitions). No lane script (cls2.py, rfinv.py, clscope.py) and no
REFEREE probe is run or imported. C^1O inputs assert exactly one Odd vertex with out-degree > 1.
PHASE: (lambda_Xi, tau) constant (default; coarser than R21's key, so a stronger test), or PHKEY=fine for (lambda_Xi, lambda_U, tau).
Checks:
  C567  (C5), (C6), (C7) on random triples of valuations drawn from the run (C7 with a random disjoint prefix).
  TRANS TRANSFER at every in-phase transition, every L in {BOT, -1, .., n-1}, every z with COARSE_L frozen (any game).
  CN    every in-phase switch at an own cycle node has gate level -1 at k (any game).
  OFFG  OFFGATE: gates at k+1 into V minus R-bar_{k+1} have level <= M_k (C^1O).
  FACTR r non-increasing along every scope run.
  CLU   at in-phase fallbacks with (h), theta < w: switched R -> F edges have level <= r.
  FBL   at in-scope fallbacks with r >= 0: no F->R, no R->R gate edge; switched edges are R->F or at own cycle nodes.
  NL    at every in-phase S4a transition with (h) at j, for EVERY L < inf with r_j > L and (A_j): (i), (ii), (iii).
        Also: leaves at such transitions when (A_j) fails for all L < r_j (shows the hypothesis has bite).
  CLS1  every in-scope fallback k1 with r >= 0: M_k1 <= min of earlier in-scope fallback levels; case split r <= L / r > L counted;
        in case r > L, (A_j) asserted at every j in [k0+1, k1]. Corollary: the THR u*!=none fallback levels are non-increasing.
Usage: cls_check.py general N nmin nmax seed | c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LP"))
import lp_check as LP
F = LP.F; RC = F.RC; lpg = F.lpg; INF, BOT, lev, coarse = F.INF, F.BOT, F.lev, F.coarse
FINE = os.environ.get("PHKEY") == "fine"

def ckey(E, x, L):
    """A total-order key for COARSE_L values consistent with E.key on full values (C1)."""
    return E.key(coarse(x, L) if L > BOT else x) if L < INF else 0

def cle(E, x, y, L):
    """COARSE_L(x) <=_L COARSE_L(y), computed from the definition: equal, or the full values ordered with lev > L."""
    if lev(x, y) <= L: return True
    return E.key(x) < E.key(y)

def prefix(E, pi, x):
    """pi (+) x for a vertex list pi (applied right to left), si.py representation (c, mask, len)."""
    c, mask, l = x
    for u in reversed(pi):
        if E.rank[u] > E.rank[c]: mask |= E.bit[u]
        l += 1
    return (c, mask, l)

def check_C567(E, vals, n, rng, st):
    for _ in range(30):
        a, b, c = rng.choice(vals), rng.choice(vals), rng.choice(vals)
        ka, kb, kc = E.key(a), E.key(b), E.key(c)
        st.c["C567_checks"] += 1
        if ka < kb <= kc and not lev(a, b) <= lev(a, c): st.bad(f"C5 {a} {b} {c}")
        if not lev(a, c) <= max(lev(a, b), lev(b, c)): st.bad(f"C6 {a} {b} {c}")
        used = set()
        for x in (a, b):
            used.add(x[0]); used |= {u for u in range(n) if (x[1] >> E.rank[u]) & 1}
        free = [u for u in range(n) if u not in used]
        pi = rng.sample(free, rng.randint(0, min(3, len(free))))
        pa, pb = prefix(E, pi, a), prefix(E, pi, b)
        if lev(pa, pb) != lev(a, b) or (E.key(pa) < E.key(pb)) != (ka < kb) or (pa == pb) != (a == b): st.bad(f"C7 {a} {b} {pi}")

def check_run(g, s, t, st, name, o, rng):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    if (len(fbs), sum(fbs)) != F.n5.run(g, "n5", ({v: s[v] for v in range(g.n) if g.owner[v] == 0},
                                                   {v: t[v] for v in range(g.n) if g.owner[v] == 1}))[:2]:
        st.bad(f"{name} run differs from n5.run")
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k, S in enumerate(A): LP.extra(g, E, S, states[k][0], states[k][1], o)
    n = g.n; T = len(fbs); nE = [v for v in range(n) if g.owner[v] == 0]
    st.c["runs"] += 1; st.c["transitions"] += T
    inph = [A[k].lam == A[k + 1].lam and states[k][1] == states[k + 1][1] and (not FINE or A[k].lamU == A[k + 1].lamU) for k in range(T)]
    vals = [x for S in A for x in S.Xi]
    check_C567(E, vals, n, rng, st)
    for k in range(T):
        if not inph[k]: continue
        A0, A1, s0, s1 = A[k], A[k + 1], states[k][0], states[k + 1][0]
        st.c["transitions_in_phase"] += 1
        # ---- TRANSFER (any game)
        for L in range(BOT, n):
            frozen = {z for z in range(n) if coarse(A1.Xi[z], L) == coarse(A0.Xi[z], L)}
            for (y, z), lv1 in A1.gl.items():
                if lv1 > L and z in frozen:
                    st.c["TRANS_checks"] += 1
                    lv0 = A0.gl.get((y, z))
                    if lv0 is None or not lv0 > L: st.bad(f"{name} TRANSFER at {k} L={L} ({y},{z}) lev1={lv1} lev0={lv0}")
        # ---- CN (any game)
        for y in nE:
            if s0[y] != s1[y] and A0.lam[y] == y:
                st.c["CN_checks"] += 1
                if A0.gl.get((y, s1[y])) != -1: st.bad(f"{name} CN at {k} y={y} level={A0.gl.get((y, s1[y]))}")
        if o is None: continue
        # ---- OFFGATE
        for (y, z), lv1 in A1.gl.items():
            if z not in A1.Rbar:
                st.c["OFFG_checks"] += 1
                if lv1 > A0.M: st.bad(f"{name} OFFGATE at {k} ({y},{z}) {lv1} > M_k {A0.M}")
    if o is None: return
    h = [S.H1 and S.H2 and S.ct == S.cw for S in A]
    th = [S.Xi[o] for S in A]; w = [S.W[o] for S in A]
    r = [lev(th[k], w[k]) for k in range(len(A))]
    F_ = [set(range(n)) - S.Rbar for S in A]
    R_ = [S.Rbar - {o} for S in A]
    def Aj(j, L): return all(lv_ <= L for (y, z), lv_ in A[j].gl.items() if z in F_[j])
    # ---- NL at every in-phase S4a transition with (h) at j, every admissible L
    for j in range(T):
        if not inph[j] or fbs[j] or not h[j]: continue
        LA = max([lv_ for (y, z), lv_ in A[j].gl.items() if z in F_[j]], default=BOT)   # smallest L with (A_j)
        leave = bool(R_[j] - A[j + 1].Rbar)
        if r[j] > LA:
            st.c["NL_transitions_with_admissible_L"] += 1
            if R_[j]: st.c["NL_admissible_with_R_nonempty"] += 1
            for L in range(max(LA, BOT), min(r[j], n)):
                if L >= r[j]: break
                st.c["NL_(j,L)_checks"] += 1
                for v in range(n):
                    if v not in A[j + 1].Rbar and coarse(A[j + 1].Xi[v], L) != coarse(A[j].Xi[v], L):
                        st.bad(f"{name} NL(i) at {j} L={L} v={v}")
                if leave: st.bad(f"{name} NL(ii) leave at {j} L={L}")
                if not Aj(j + 1, L): st.bad(f"{name} NL(iii) at {j} L={L}")
        else:
            st.c["NL_no_admissible_L(S4a,(h))"] += 1
            if leave: st.c["NL_no_admissible_L_with_leave"] += 1
    # ---- scope runs
    insc = [inph[k] and h[k] and A[k + 1].H2 and w[k + 1] == w[k] for k in range(T)]
    k = 0
    while k < T:
        if not insc[k]: k += 1; continue
        j0 = k
        while k < T and insc[k]: k += 1
        scope(g, E, A, states, fbs, j0, k, st, name, o, r, h, F_, R_, Aj)

def scope(g, E, A, states, fbs, k0s, k1s, st, name, o, r, h, F_, R_, Aj):
    n = g.n
    st.c["scope_runs"] += 1
    for k in range(k0s, k1s):
        st.c["scope_transitions"] += 1
        if r[k + 1] > r[k]: st.bad(f"{name} FACT R at {k}: {r[k]} -> {r[k+1]}")
    fl = [k for k in range(k0s, k1s) if fbs[k]]
    st.mx["max_fallbacks_per_scope_run"] = max(st.mx["max_fallbacks_per_scope_run"], len(fl))
    seq = []
    for i, k1 in enumerate(fl):
        S = A[k1]; s0, s1 = states[k1][0], states[k1 + 1][0]
        st.c["scope_fallbacks"] += 1
        thr = E.key(S.Xi[o]) < E.key(S.W[o])
        if r[k1] >= 0: st.c["scope_fallbacks_THR_u*!=none"] += 1
        elif r[k1] == -1: st.c["scope_fallbacks_u*=none"] += 1
        else:
            st.c["scope_fallbacks_theta=w"] += 1
            if any(S.Xi[v] != S.W[v] for v in range(n)): st.bad(f"{name} theta=w under (h) but not EQ at {k1}")
        sw = [(y, s1[y]) for y in range(n) if g.owner[y] == 0 and s0[y] != s1[y]]
        # FB step (2): M attained by a switched edge
        if S.M != max(S.gl[e] for e in sw): st.bad(f"{name} FB(2): M not attained by switched edge at {k1}")
        # CLU
        if thr:
            for y, z in sw:
                if y in R_[k1] and z in F_[k1]:
                    st.c["CLU_checks"] += 1
                    if S.gl[(y, z)] > r[k1]: st.bad(f"{name} CLU at {k1} ({y},{z}) {S.gl[(y,z)]} > r {r[k1]}")
        if r[k1] < 0: continue
        # FBL strong form (R20 (b), u* != none)
        for (y, z) in S.gl:
            if z in S.Rbar: st.bad(f"{name} FBL: gate into R-bar at {k1} ({y},{z})")
        for y, z in sw:
            if not (y in R_[k1] and z in F_[k1]) and S.lam[y] != y: st.bad(f"{name} FBL: switched ({y},{z}) at {k1}")
        # CLS1
        prev = fl[:i]
        seq.append(S.M)
        if not prev: st.c["CLS1_first_fallback(vacuous)"] += 1; continue
        k0 = prev[-1]; L = A[k0].M
        st.c["CLS1_checks"] += 1
        if any(r[x] < 0 for x in prev): st.bad(f"{name} CLS1 (beta) earlier fallback with r<0 before {k1}")
        if S.M > min(A[x].M for x in prev): st.bad(f"{name} CLS1 at {k1}: M={S.M} > min {min(A[x].M for x in prev)}")
        if r[k1] <= L: st.c["CLS1_case_r<=L"] += 1
        else:
            st.c["CLS1_case_r>L"] += 1
            st.mx["max_CLS1_case_r>L_gap(k1-k0)"] = max(st.mx["max_CLS1_case_r>L_gap(k1-k0)"], k1 - k0)
            for j in range(k0 + 1, k1 + 1):
                st.c["CLS1_A_chain_checks"] += 1
                if not Aj(j, L): st.bad(f"{name} CLS1 (A_j) fails at {j} L={L} (k0={k0}, k1={k1})")
        if S.M < L: st.c["CLS1_strict_drop"] += 1
    if any(seq[i + 1] > seq[i] for i in range(len(seq) - 1)): st.bad(f"{name} CLS1 Corollary: levels {seq}")

def main():
    st = F.Stats(); st.ex = {}; mode = sys.argv[1]
    if mode in ("general", "c1o"):
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            if mode == "general": g = F.rand_general(rng, rng.randint(nmin, nmax)); o = None
            else:
                rg, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7); g = F.to_lpg(rg); assert F.one_odd(g) == o
            s, t = F.start(g, rng, rng.random() < 0.6)
            check_run(g, s, t, st, f"{mode}{seed}#{i}", o, rng)
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); o = F.one_odd(g); rng = random.Random(7)
        for r_ in range(runs):
            s, t = F.start(g, rng, r_ > 0); check_run(g, s, t, st, f"{os.path.basename(path)}#{r_}", o, rng)
    F.report(st)

if __name__ == "__main__":
    main()
