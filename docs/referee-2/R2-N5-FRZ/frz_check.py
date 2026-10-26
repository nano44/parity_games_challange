#!/usr/bin/env python3
"""REFEREE-2 successor 7 (Opus 5.5, D15): mechanical check of packet P-N5-FRZ (docs/new/P-N5-FRZ-box34.md sha1 39df373c @ trunk 25fda0f).
Own code on my lane's R2-N5-RE/re_check.py (self-contained Game, play values, VJ00 order, honest valuation as the pointwise minimum over
Odd's choices at o, Even's one-player optimum by SI, own N5 loop). No lane script and no REFEREE probe is run or imported; lane .pg files
are inputs only. Every game asserts exactly one Odd vertex with out-degree > 1. Phase key: (lambda_Xi, tau) constant (the packet's).
N5 variant: S4a = an arena optimum in G_tau (deterministic switch-all SI, or random-subset SI + random value-preserving re-choices with
--rand); S4b = Odd's pointwise-best option at o; S4c fallback as SPEC. The packet's proofs use only (F1) of the S4a optimum.
Checks (packet items):
  FACT0   at every (h) state: W-cycle node(v) = lambda(v) for all v; lambda(v) = c_theta in F for v in Rbar; honest cycle nodes in F with
          W = Xi = (u, {}, 0).
  NLMF    at in-phase S4a steps with (h) at j and r_j > MF_j: R_j subset Rbar_{j+1}, MF_{j+1} <= MF_j; every leave at an (h) S4a step has
          a gate into F_j of level >= r_j (consequence).
  ARENA   at in-phase S4a steps from (h): every W-improving edge not in the arena has y in F, z in Rbar, is not a gate, level <= r.
  STEP1   at (h) states: COARSE_r(Xi) = COARSE_r(W).
  STEP2   consecutive (h) in-phase states: COARSE_l(W) non-decreasing for every l >= max(r_k, r_{k+1}).
  PC      Lemma P^c_l on every maximal window (deduplicated, at its own max r): exhaustive simple paths for n <= PCN, sampled above.
  FREEZE  per phase, per level l, first F(l): (a) at t >= F with an H2 state t2 >= t; (b) at H2 t >= F. Counts the later states that are
          separated from F by a fallback, a theta-change, a w-change, a not-(h) state.
  RATCHET (a) at H2 t >= F; (b) COARSE_{l-1} theta values / changes over H1 states of T, w changes over T; (c) pair runs, r per run.
  BLOCK   per l >= 0, maximal blocks I (consecutive, >= F, (h), pair constant and different): no re-entry after an S4a leave inside I.
  XRUN    per maximal fallback-free run Q with H1 on its SN prefix P: every sub-count of the proof (pre-F(l_max), per-segment runs, r = l
          blocks <= 2n, agree runs < n states, level -1 re-entries, no crossing after F(bot)), total vs 13(d_o+1)n^3, REL_Q, leaves after
          P (R-STICK), leaves at the transition leaving P.
  SUB     (w, r)-subruns with rho >= -1: (i) Step 1 + monotone; (ii) frozen from k0+n-1; (iii) re-entries strict; count <= n(n-1).
Usage: frz_check.py random N nmin nmax seed [--rand] | inst game.pg [runs] [--rand]"""
import sys, os, random, itertools
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RE"))
import re_check as RC

INF, BOT = 10 ** 9, -2
PCN = 10          # exhaustive Lemma P^c paths up to this n
PCSAMPLE = 40     # sampled paths per vertex per window above PCN
WINF = float(os.environ.get("FRZ_WINF", "1"))   # mutation test only: window length factor

def lev(g, x, y):
    if x == y: return BOT
    if x[0] != y[0]: return INF
    if x[1] != y[1]: return max(g.rank[u] for u in (x[1] ^ y[1]))
    return -1

def coarse(g, x, L):
    if L <= BOT: return x
    return (x[0], frozenset(u for u in x[1] if g.rank[u] > L))

def ck(g, x, L):
    """order key of COARSE_L(x) (L < inf)"""
    if L <= BOT: return g.key(x)
    c = coarse(g, x, L)
    return g.key((c[0], c[1], 0))

def odd_vertex(g):
    o = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    assert len(o) == 1, f"not C^1O: {o}"
    return o[0]

class Stats:
    def __init__(s): s.c = Counter(); s.mx = Counter(); s.viol = []; s.ex = {}
    def bad(s, m):
        s.c["VIOLATIONS"] += 1
        if len(s.viol) < 40: s.viol.append(m)
    def mxu(s, k, v): s.mx[k] = max(s.mx[k], v)

def returns(f, o): return RC._returns(f, o)

def analyse(g, o, sg, tu):
    S = RC.analyse(g, o, sg, tu)
    S.sg, S.tu = list(sg), list(tu)
    S.Rbar = set(S.R); S.Rr = S.Rbar - {o}; S.F = set(range(g.n)) - S.Rbar
    S.H1 = not returns(S.fh, o); S.H2 = not returns(S.f, o); S.H3 = S.Xi[o][0] == S.W[o][0]
    S.hh = S.H1 and S.H2 and S.H3
    S.r = lev(g, S.theta, S.w) if S.H3 else INF
    S.gates = {(y, z): lev(g, S.Xi[sg[y]], S.Xi[z]) for y, z in S.Is}
    S.MF = max([L for (y, z), L in S.gates.items() if z in S.F], default=BOT)
    return S

def run_n5(g, o, s, t, rng, rand, cap=600):
    A = [analyse(g, o, s, t)]; fbs = []
    while len(A) <= cap:
        S = A[-1]; sg, tu = S.sg, S.tu
        if not S.Is and not S.It: break
        ns, nt = list(sg), list(tu); fb = 0
        if S.Is:
            arena = [sorted({sg[v]} | {z for x, z in S.Is if x == v}) if g.owner[v] == 0 else [S.f[v]] for v in range(g.n)]
            fo, _ = RC.even_optimum(g, S.f, arena, rng if rand else None, perturb=rng.randint(0, 6) if rand else 0)
            for v in range(g.n):
                if g.owner[v] == 0: ns[v] = fo[v]
        if S.It:
            mins, table = RC.odd_points(g, S.f, o, [tu[o]] + S.It)
            nt[o] = rng.choice(mins) if rand else min(mins)
        if ns == sg and nt == tu:
            fb = 1
            if S.Is:
                for v in {v for v, _ in S.Is}:
                    ns[v] = max((z for x, z in S.Is if x == v), key=lambda z: (g.key(S.Xi[z]), z))
            else:
                nt[o] = min(S.It, key=lambda z: (g.key(S.U[z]), -z))
        A.append(analyse(g, o, ns, nt)); fbs.append(fb)
    return A, fbs

def path_value(g, rho):
    u = rho[-1]; L = len(rho) - 1
    return (u, frozenset(p for p in rho[:-1] if g.rank[p] > g.rank[u]), L)

def succ_tau(g, o, tau, v):
    return [tau[o]] if v == o else g.succ[v]

# ------------------------------------------------------------------ per-state / per-transition checks
def check_state(g, o, S, st, name):
    if not S.hh: return
    st.c["FACT0_states"] += 1
    lam = S.lamX; cth = S.theta[0]
    for v in range(g.n):
        if S.W[v][0] != lam[v]: st.bad(f"{name} FACT0 W-cycle node of {v} != lambda")
    for v in S.Rbar:
        if lam[v] != cth: st.bad(f"{name} FACT0 lambda({v}) != c_theta")
    if cth not in S.F: st.bad(f"{name} FACT0 c_theta not in F")
    for u in range(g.n):
        if lam[u] == u:
            if u not in S.F or S.W[u] != (u, frozenset(), 0) or S.Xi[u] != S.W[u]: st.bad(f"{name} FACT0 cycle node {u}")
    st.c["STEP1_states"] += 1
    for v in range(g.n):
        if coarse(g, S.Xi[v], S.r) != coarse(g, S.W[v], S.r): st.bad(f"{name} STEP1 v={v} r={S.r}")

def check_transition(g, o, A, B, fb, st, name):
    n = g.n
    if fb == 0 and A.hh:
        # NL-MF
        st.c["NLMF_h_S4a_steps"] += 1
        leaves = A.Rr - B.Rbar
        if leaves:
            st.c["NLMF_h_S4a_steps_with_leave"] += 1
            if not any(L >= A.r for (y, z), L in A.gates.items() if z in A.F): st.bad(f"{name} NLMF consequence: leave without gate into F of level >= r")
        if A.r > A.MF:
            st.c["NLMF_r_gt_MF"] += 1
            if A.MF == BOT: st.c["NLMF_r_gt_MF_with_MF=bot (NL at L=bot)"] += 1
            if leaves: st.bad(f"{name} NLMF leave {sorted(leaves)} with r {A.r} > MF {A.MF}")
            if B.MF > A.MF: st.bad(f"{name} NLMF MF rose {A.MF} -> {B.MF}")
        # ARENA
        st.c["ARENA_steps"] += 1; wh = 0
        for y in range(n):
            if g.owner[y] != 0: continue
            for z in g.succ[y]:
                if z == A.sg[y] or g.cmp(A.W[z], A.W[A.sg[y]]) <= 0: continue
                st.c["ARENA_W_improving_edges"] += 1
                if (y, z) in A.gates: continue
                wh += 1; st.c["ARENA_withheld"] += 1
                if not (y in A.F and z in A.Rbar): st.bad(f"{name} ARENA withheld edge {y}->{z} not F->Rbar")
                if lev(g, A.W[A.sg[y]], A.W[z]) > A.r: st.bad(f"{name} ARENA withheld level > r")
                if A.r == BOT: st.bad(f"{name} ARENA withheld at theta = w")
        if wh: st.c["ARENA_steps_with_withheld"] += 1
    if A.hh and B.hh:
        l0 = max(A.r, B.r)
        for L in [l0] + list(range(max(l0 + 1, -1), n)):
            st.c["STEP2_checks"] += 1
            for v in range(n):
                if ck(g, B.W[v], L) < ck(g, A.W[v], L): st.bad(f"{name} STEP2 W coarse dropped v={v} L={L} fb={fb}"); break

# ------------------------------------------------------------------ Lemma P^c
def best_paths(g, o, tau, lam, x, maxlen, L, rng, exhaustive):
    """best[d] = max COARSE_L key over simple paths from x of length <= d ending at an honest cycle node."""
    best = [None] * (maxlen + 1)
    def upd(rho):
        if lam[rho[-1]] != rho[-1]: return
        k = ck(g, path_value(g, rho), L); d = len(rho) - 1
        if best[d] is None or k > best[d]: best[d] = k
    if exhaustive:
        stack = [[x]]
        while stack:
            rho = stack.pop(); upd(rho)
            if len(rho) - 1 < maxlen:
                for z in succ_tau(g, o, tau, rho[-1]):
                    if z not in rho: stack.append(rho + [z])
    else:
        upd([x])
        for _ in range(PCSAMPLE):
            rho = [x]
            while len(rho) - 1 < maxlen:
                opts = [z for z in succ_tau(g, o, tau, rho[-1]) if z not in rho]
                if not opts: break
                rho.append(rng.choice(opts)); upd(rho)
    for d in range(1, maxlen + 1):
        if best[d - 1] is not None and (best[d] is None or best[d - 1] > best[d]): best[d] = best[d - 1]
    return best

def check_pc(g, o, A, k0, k1, L, rng, st, name):
    tau = A[k0].tu; lam = A[k0].lamX; N = k1 - k0
    st.c["PC_windows"] += 1; st.mxu("PC_max_window_len_over_n_x100", (N + 1) * 100 // g.n)
    for x in range(g.n):
        best = best_paths(g, o, tau, lam, x, min(N, g.n - 1), L, rng, g.n <= PCN)
        for j in range(N + 1):
            b = best[min(j, g.n - 1)]
            if b is None: continue
            st.c["PC_checks_exhaustive" if g.n <= PCN else "PC_checks_sampled"] += 1
            if ck(g, A[k0 + j].W[x], L) < b: st.bad(f"{name} PC fails x={x} j={j} L={L} window [{k0},{k1}]")

# ------------------------------------------------------------------ per phase
def levels(n): return [BOT, -1] + list(range(n))

def first_F(A, a, b, L, n):
    """least end k0+n-1 of a window of n states at L inside states a..b (all (h), r <= L); None if none."""
    n = max(1, int(n * WINF))      # WINF = 1 for the packet's windows; < 1 only in the sensitivity (mutation) test
    cnt = 0
    for k in range(a, b + 1):
        if A[k].hh and A[k].r <= L: cnt += 1
        else: cnt = 0
        if cnt >= n: return k
    return None

def check_phase(g, o, A, fbs, a, b, rng, st, name):
    n = g.n; d_o = len(set(g.succ[o]))
    st.c["phases"] += 1
    # windows for P^c: maximal runs of (h) states with r <= L, dedup, checked at their own max r
    seen = set()
    for L in levels(n):
        k = a
        while k <= b:
            if not (A[k].hh and A[k].r <= L): k += 1; continue
            e = k
            while e + 1 <= b and A[e + 1].hh and A[e + 1].r <= L: e += 1
            if (k, e) not in seen:
                seen.add((k, e)); Lw = max(A[i].r for i in range(k, e + 1))
                if e > k: check_pc(g, o, A, k, e, Lw, rng, st, f"{name}")
            k = e + 1
    # FREEZE / RATCHET / BLOCK per level
    H2later = [False] * (b + 2)
    for k in range(b, a - 1, -1): H2later[k] = A[k].H2 or H2later[k + 1]
    for L in levels(n):
        Fk = first_F(A, a, b, L, n)
        if Fk is None: continue
        st.c[f"FREEZE_levels_with_F"] += 1
        st.c["FREEZE_F_level_" + ("bot" if L == BOT else ("-1" if L == -1 else ">=0"))] += 1
        XF = [coarse(g, x, L) for x in A[Fk].Xi]; WF = [coarse(g, x, L) for x in A[Fk].W]
        if XF != WF: st.bad(f"{name} FREEZE Step 1 at F={Fk} L={L}")
        fbseen = thseen = wseen = nhseen = False
        for t in range(Fk + 1, b + 1):
            if fbs[t - 1]: fbseen = True
            if A[t].theta != A[t - 1].theta: thseen = True
            if A[t].w != A[t - 1].w: wseen = True
            if not A[t].hh: nhseen = True
            Xt = [coarse(g, x, L) for x in A[t].Xi]
            if H2later[t]:
                st.c["FREEZE_a_checks"] += 1
                if fbseen: st.c["FREEZE_a_after_fallback"] += 1
                if thseen: st.c["FREEZE_a_after_theta_change"] += 1
                if wseen: st.c["FREEZE_a_after_w_change"] += 1
                if nhseen: st.c["FREEZE_a_after_not_h_state"] += 1
                if Xt != XF: st.bad(f"{name} FREEZE (a) t={t} F={Fk} L={L}")
            else:
                st.c["FREEZE_no_H2_later_states"] += 1
                if Xt != XF: st.c["FREEZE_a_without_H2_later_differs (no claim)"] += 1
            if A[t].H2:
                st.c["FREEZE_b_checks"] += 1
                if [coarse(g, x, L) for x in A[t].W] != WF: st.bad(f"{name} FREEZE (b) t={t} F={Fk} L={L}")
        # RATCHET
        T = [t for t in range(Fk, b + 1) if A[t].H2]
        for t in T:
            st.c["RATCHET_a_checks"] += 1
            if coarse(g, A[t].theta, L) != coarse(g, A[t].w, L) or not A[t].H3 or A[t].r > L: st.bad(f"{name} RATCHET (a) t={t} L={L}")
            if A[t].H1 and not A[t].hh: st.bad(f"{name} RATCHET (a) H1 but not (h) t={t}")
        if L < 0: continue
        for s in range(Fk, b):
            if fbs[s] == 0 and A[s].hh and (A[s].Rr - A[s + 1].Rbar):
                st.c["LEAVE_S4a_(h)_after_F(l>=0)"] += 1
                if A[s].r == L: st.c["LEAVE_S4a_(h)_after_F_with_r=l"] += 1
        TH = [t for t in T if A[t].H1]
        thv = [coarse(g, A[t].theta, L - 1) for t in TH]
        nth = len(set(thv)); chg = sum(1 for i in range(1, len(thv)) if thv[i] != thv[i - 1])
        st.c["RATCHET_b_checks"] += 1; st.mxu("RATCHET_b_max_theta_values", nth); st.mxu("RATCHET_b_max_theta_changes", chg)
        if nth > 2 * d_o or chg > 2 * d_o - 1: st.bad(f"{name} RATCHET (b) theta {nth} values {chg} changes L={L}")
        wv = [coarse(g, A[t].w, L - 1) for t in T]
        wch = sum(1 for i in range(1, len(wv)) if wv[i] != wv[i - 1]); st.mxu("RATCHET_b_max_w_changes", wch)
        if wch > 1: st.bad(f"{name} RATCHET (b) w changes {wch} L={L}")
        pairs = [(coarse(g, A[t].theta, L - 1), coarse(g, A[t].w, L - 1)) for t in TH]
        runs = 1 + sum(1 for i in range(1, len(pairs)) if pairs[i] != pairs[i - 1]) if pairs else 0
        st.mxu("RATCHET_c_max_runs", runs)
        if runs > 2 * d_o + 1: st.bad(f"{name} RATCHET (c) {runs} runs L={L}")
        for t, (p, q) in zip(TH, pairs):
            if p != q and A[t].r != L: st.bad(f"{name} RATCHET (c) differ but r={A[t].r} != {L}")
            if p == q and A[t].r > L - 1: st.bad(f"{name} RATCHET (c) agree but r={A[t].r} > {L - 1}")
        # BLOCK: maximal consecutive blocks >= F with (h) and pair constant & different
        k = Fk
        while k <= b:
            def pr(t): return (coarse(g, A[t].theta, L - 1), coarse(g, A[t].w, L - 1))
            if not A[k].hh or pr(k)[0] == pr(k)[1]: k += 1; continue
            e = k
            while e + 1 <= b and A[e + 1].hh and pr(e + 1) == pr(k): e += 1
            st.c["BLOCK_blocks"] += 1; st.mxu("BLOCK_max_len", e - k + 1)
            left = {}
            for s in range(k, e):
                if fbs[s] == 0:
                    for v in A[s].Rr - A[s + 1].Rbar: left.setdefault(v, s)
                for v, s0 in left.items():
                    if s0 < s + 1 and v in A[s + 1].Rr:
                        st.bad(f"{name} BLOCK v={v} left at {s0}, back in R at {s + 1} L={L}")
            st.c["BLOCK_S4a_leaves"] += len(left)
            if e < b and fbs[e] == 0 and (A[e].Rr - A[e + 1].Rbar): st.c["BLOCK_S4a_leaves_at_block_exit (no claim)"] += 1
            if all(fbs[s] == 0 for s in range(k, e)):
                xc = sum(1 for s in range(k, e) if A[s].Rr != A[s + 1].Rr)
                st.mxu("BLOCK_max_crossings_in_ff_block", xc)
                if xc > 2 * n: st.bad(f"{name} BLOCK consequence {xc} > 2n crossings")
            k = e + 1

def check_sub(g, o, A, fbs, a, b, st, name):
    n = g.n; k = a
    while k <= b:
        if not A[k].hh: k += 1; continue
        e = k
        while e + 1 <= b and A[e + 1].hh and A[e + 1].w == A[k].w and A[e + 1].r == A[k].r: e += 1
        rho = A[k].r
        if rho >= -1:
            st.c["SUB_subruns_rho>=-1"] += 1
            if e - k + 1 >= n: st.c["SUB_subruns_len>=n"] += 1
            for t in range(k + 1, e + 1):
                for v in range(n):
                    if ck(g, A[t].Xi[v], rho) < ck(g, A[t - 1].Xi[v], rho): st.bad(f"{name} SUB (i) not monotone")
            if e - k + 1 >= n:
                F0 = k + n - 1
                for t in range(F0, e + 1):
                    if [coarse(g, x, rho) for x in A[t].Xi] != [coarse(g, x, rho) for x in A[F0].Xi]: st.bad(f"{name} SUB (ii) t={t}")
            cnt = 0
            for x in range(n):
                s = k
                while s < e:
                    if fbs[s] == 0 and x in A[s].Rr and x not in A[s + 1].Rbar:
                        E = s + 1
                        while E < e and x not in A[E + 1].Rr: E += 1
                        if E < e and x in A[E + 1].Rr:
                            cnt += 1; st.c["SUB_iii_reentries"] += 1
                            if rho >= 0:
                                if ck(g, A[E + 1].Xi[x], rho) <= ck(g, A[s].Xi[x], rho): st.bad(f"{name} SUB (iii) x={x} L={s} E={E}")
                            else:
                                if g.key(A[E + 1].Xi[x]) <= g.key(A[s].Xi[x]): st.bad(f"{name} SUB (iii) rho=-1 x={x}")
                            s = E + 1; continue
                    s += 1
            if rho >= 0 and cnt > n * (n - 1): st.bad(f"{name} SUB count {cnt}")
            st.mxu("SUB_max_reentries", cnt)
        k = e + 1

def check_xrun(g, o, A, fbs, a, b, st, name):
    """maximal fallback-free runs inside phase states a..b"""
    n = g.n; d_o = len(set(g.succ[o])); k = a
    while k < b:
        if fbs[k]: k += 1; continue
        e = k
        while e < b and fbs[e] == 0: e += 1      # states k..e, transitions k..e-1 all non-fallback
        q0, q1 = k, e
        P = []
        for t in range(q0, q1 + 1):
            if A[t].H3: P.append(t)
            else: break
        for t in range(q0 + len(P), q1 + 1):
            if A[t].H3: st.bad(f"{name} SN-PREFIX not a prefix")
        st.c["XRUN_runs"] += 1
        # leaves after P (R-STICK) and at the transition leaving P
        if P:
            pe = P[-1]
            rel_exit = 0
            for s in range(pe + 1, q1):
                if A[s].Rr - A[s + 1].Rbar: st.bad(f"{name} R-STICK leave after the SN prefix at {s}")
            if pe < q1:
                lv = A[pe].Rr - A[pe + 1].Rbar
                if lv:
                    st.c["XRUN_leaves_at_transition_leaving_P"] += 1
                    ex = lv & set(g.succ[o])
                    if ex: st.c["XRUN_exit_leaves_at_transition_leaving_P"] += len(ex)
        if not P or not all(A[t].H1 for t in P):
            if P: st.c["XRUN_runs_P_not_all_H1"] += 1
            k = e; continue
        st.c["XRUN_runs_H1_P"] += 1; st.mxu("XRUN_max_P_len", len(P))
        for t in P:
            if not A[t].hh: st.bad(f"{name} XRUN P state {t} not (h)")
        p0, p1 = P[0], P[-1]
        cross = [s for s in range(p0, p1) if A[s].Rr != A[s + 1].Rr]
        X = len(cross); st.c["XRUN_crossings_in_P"] += X; st.mxu("XRUN_max_crossings_in_P", X)
        if X > 13 * (d_o + 1) * n ** 3: st.bad(f"{name} XRUN total {X}")
        rel = sum(len((A[s].Rr - A[s + 1].Rbar) & set(g.succ[o])) for s in range(q0, q1))
        st.mxu("XRUN_max_REL_Q", rel)
        if rel > 13 * d_o * (d_o + 1) * n ** 3: st.bad(f"{name} XRUN REL_Q")
        # sub-claims
        Fl = {L: first_F(A, p0, p1, L, n) for L in levels(n)}
        lv = levels(n)
        for i in range(1, len(lv)):
            x0, x1 = Fl[lv[i - 1]], Fl[lv[i]]
            if x0 is not None and (x1 is None or x1 > x0): st.bad(f"{name} XRUN F not non-increasing")
        lmax = max(A[t].r for t in P)
        if len(P) >= n and Fl[lmax] != p0 + n - 1: st.bad(f"{name} XRUN F(lmax) != p0+n-1")
        def isx(s): return A[s].Rr != A[s + 1].Rr
        for L in range(n - 1, -1, -1):
            if Fl[L] is None: continue
            s0, s1 = Fl[L], (Fl[L - 1] if Fl[L - 1] is not None else p1 + 1)
            seg = list(range(s0, s1))
            if not seg: continue
            st.c["XRUN_segments_l>=0"] += 1
            pr = [(coarse(g, A[t].theta, L - 1), coarse(g, A[t].w, L - 1)) for t in seg]
            runs = []; i = 0
            while i < len(seg):
                j = i
                while j + 1 < len(seg) and pr[j + 1] == pr[i]: j += 1
                runs.append((seg[i], seg[j], pr[i][0] != pr[i][1])); i = j + 1
            if len(runs) > 2 * d_o + 1: st.bad(f"{name} XRUN segment L={L} {len(runs)} runs")
            for (u0, u1, diff) in runs:
                if diff:
                    xc = sum(1 for s in range(u0, min(u1, p1)) if isx(s))
                    st.mxu("XRUN_max_crossings_r=l_run", xc)
                    if xc > 2 * n: st.bad(f"{name} XRUN r=l run crossings {xc}")
                else:
                    if u1 - u0 + 1 >= n: st.bad(f"{name} XRUN agree run with >= n states in segment L={L}")
            tot = sum(1 for s in seg if s < p1 and isx(s)); st.mxu("XRUN_max_segment_crossings", tot)
            if tot > 6 * (d_o + 1) * n: st.bad(f"{name} XRUN segment L={L} total {tot}")
        if Fl[-1] is not None:
            s0, s1 = Fl[-1], (Fl[BOT] if Fl[BOT] is not None else p1 + 1)
            seg = list(range(s0, s1))
            if seg:
                st.c["XRUN_segments_l=-1"] += 1
                for t in seg:
                    for v in range(n):
                        if coarse(g, A[t].Xi[v], -1) != coarse(g, A[s0].Xi[v], -1): st.bad(f"{name} XRUN -1 segment (c,P) moved")
                pairs = [(A[t].theta, A[t].w) for t in seg]
                runs = 1 + sum(1 for i in range(1, len(pairs)) if pairs[i] != pairs[i - 1])
                if runs > (d_o + 1) * n: st.bad(f"{name} XRUN -1 segment {runs} runs")
                for v in range(n):
                    last_leave = None; reent = 0
                    for s in seg:
                        if s >= p1: break
                        if v in A[s].Rr and v not in A[s + 1].Rbar and A[s].theta != A[s].w: last_leave = s
                        if last_leave is not None and v in A[s + 1].Rr and v not in A[s].Rr:
                            reent += 1
                            if g.key(A[s + 1].Xi[v]) <= g.key(A[last_leave].Xi[v]): st.bad(f"{name} XRUN -1 re-entry not strict v={v}")
                            last_leave = None
                    st.mxu("XRUN_-1_max_reentries_per_vertex", reent)
                    if reent > n - 1: st.bad(f"{name} XRUN -1 re-entries {reent}")
                tot = sum(1 for s in seg if s < p1 and isx(s)); st.mxu("XRUN_max_segment_-1_crossings", tot)
        if Fl[BOT] is not None:
            for s in range(Fl[BOT], p1):
                st.c["XRUN_after_Fbot_transitions"] += 1
                if isx(s): st.bad(f"{name} XRUN crossing after F(bot) at {s}")
        pre = sum(1 for s in range(p0, min(Fl[lmax] if Fl[lmax] is not None else p1, p1)) if isx(s))
        st.mxu("XRUN_max_pre_crossings", pre)
        k = e

def check_run(g, o, A, fbs, rng, st, name):
    T = len(fbs)
    st.c["runs"] += 1; st.c["transitions"] += T; st.c["fallbacks"] += sum(fbs)
    for k, S in enumerate(A): check_state(g, o, S, st, f"{name}@{k}")
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    for k in range(T):
        if inph[k]: check_transition(g, o, A[k], A[k + 1], fbs[k], st, f"{name}@{k}")
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        a, b = k, j                    # states a..b
        st.mxu("max_phase_states", b - a + 1)
        nh = max_h = 0
        for t in range(a, b + 1):
            nh = nh + 1 if A[t].hh else 0; max_h = max(max_h, nh)
        st.mxu("max_consecutive_h_over_n_x100", max_h * 100 // g.n)
        check_phase(g, o, A, fbs, a, b, rng, st, f"{name}[{a},{b}]")
        check_sub(g, o, A, fbs, a, b, st, f"{name}[{a},{b}]")
        check_xrun(g, o, A, fbs, a, b, st, f"{name}[{a},{b}]")
        k = j

def report(st):
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c["VIOLATIONS"] else "OK", f"violations={st.c['VIOLATIONS']}")

def s3_start(g):
    def br(v, dual):
        def rr(w):
            p = g.prio[w] + (1 if dual else 0)
            r_ = p if p % 2 == 0 else -p
            return (r_, w if r_ % 2 == 0 else -w)
        return max(g.succ[v], key=rr)
    return [br(v, False) for v in range(g.n)], [br(v, True) for v in range(g.n)]

def main():
    st = Stats(); args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else s3_start(g)
            A, fbs = run_n5(g, o, s, t, rng, rand)
            check_run(g, o, A, fbs, rng, st, f"seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3
        g = RC.parse(open(path).read()); o = odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = run_n5(g, o, s, t, rng, rand)
            check_run(g, o, A, fbs, rng, st, f"{os.path.basename(path)}#{r}")
    report(st)

if __name__ == "__main__":
    main()
