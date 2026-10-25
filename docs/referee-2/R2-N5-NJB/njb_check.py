#!/usr/bin/env python3
"""REFEREE-2 successor 7 (Opus 5.5, D15): mechanical check of packet P-N5-NJB (docs/si/P-N5-NJB-box9.md sha1 f43a8823 @ trunk a7d85b3).
Own code on my lane's R2-N5-FRZ/frz_check.py (own N5, any S4a arena optimum; R2-N5-RE/re_check.py primitives). No lane script
(reltrace.py, minset.py, norf.py, ffprobe.py, jclimb.py) and no REFEREE probe. Every game asserts exactly one Odd vertex with out-degree > 1.
Phase key (lambda_Xi, tau). SCOPE RUN: maximal run of in-phase transitions k -> k+1 with (h) at k, H2 at k+1, w_{k+1} = w_k.
Fallback level M_k = max gate level at k. BLOCK (level M >= 0): the fallbacks of S with M_k = M.
Checks:
  RDROP   first COARSE_M(Xi) change j of a dirty interval: S4a, r_j > M.
  PLC     PL (c'): D_M <= (d_o - 1) + REL_M, N <= n_E (d_o + REL_M) for EVERY block; PL-S' per scope run.
  MINSET  on intervals with r > M on [f_i+1, f_{i+1}]: (a) COARSE_M(theta_t) = min over free exits of COARSE_M(o + Xi_t x), attained at
          sigma-bar_t(o); (b) free exits keep COARSE_M(o + Xi x), members leave only by absorption; (c) SURVIVOR form: COARSE_M(theta)
          changes at t -> t+1 iff Mn_t ∩ F_{t+1} = {}; LITERAL form (Mn_{t+1} w.r.t. theta_{t+1} empty) counted; (d) Mn_{f_i} ⊆ Mn_{f_i+1}.
  NORF    NO-RF-OLD for every fallback k0 of S (L = M_{k0}), every t* <= next fallback with r > L on [k0+1, t*], every S4a j in (k0, t*)
          with a COARSE_L(theta) change: no gate (y, z) at t in [j+1, t*] with y in R_j ∩ R_t, z in F_t. Corollary + ENT-SHAPE (1)-(4) at
          the next fallback k when M_k = L >= 0.
Usage: njb_check.py random N nmin nmax seed [--rand] | inst game.pg [runs] [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC; INF, BOT = FC.INF, FC.BOT; lev, coarse, ck = FC.lev, FC.coarse, FC.ck

def M_of(S): return max(S.gates.values(), default=BOT)
def b(S, y): return S.Xi[S.sg[y]]

def oplus_o(g, o, x):
    c, P, l = x
    return (c, P | ({o} if g.rank[o] > g.rank[c] else frozenset()), l + 1)

def beta_good(g, x, L):
    """rank-L vertex v_L in P(x) and even, or not in P(x) and odd -> good"""
    vL = [v for v in range(g.n) if g.rank[v] == L][0]
    ev = g.prio[vL] % 2 == 0
    return (vL in x[1]) == ev

def scope_runs(A, fbs, o):
    T = len(fbs); out = []; k = 0
    def ins(k): return (A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] and A[k].hh and A[k + 1].H2 and A[k + 1].w == A[k].w)
    while k < T:
        if not ins(k): k += 1; continue
        j = k
        while j < T and ins(j): j += 1
        out.append((k, j)); k = j            # transitions k..j-1, states k..j
    return out

def check_scope(g, o, A, fbs, s0, s1, st, name):
    n = g.n; d_o = len(set(g.succ[o])); nE = sum(1 for v in range(n) if g.owner[v] == 0); exits = set(g.succ[o])
    fb = [k for k in range(s0, s1) if fbs[k]]
    st.c["scope_runs"] += 1; st.c["scope_fallbacks"] += len(fb)
    levs = [M_of(A[k]) for k in fb]
    tot_ge0 = 0; relS = sum(len((A[k].Rr - A[k + 1].Rbar) & exits) for k in fb)
    for M in sorted(set(L for L in levs if L >= 0)):
        F = [k for k, L in zip(fb, levs) if L == M]; N = len(F); tot_ge0 += N
        st.c["blocks"] += 1; st.mxu("max_block_N", N)
        D = 0; rel = sum(len((A[f].Rr - A[f + 1].Rbar) & exits) for f in F[:-1])
        for i in range(N - 1):
            fi, fj = F[i], F[i + 1]
            ch = [t for t in range(fi + 1, fj) if any(coarse(g, A[t].Xi[v], M) != coarse(g, A[t + 1].Xi[v], M) for v in range(n))]
            if ch:
                D += 1; j = ch[0]; st.c["dirty_intervals"] += 1
                if fbs[j]: st.bad(f"{name} RDROP first change {j} is a fallback")
                if not A[j].r > M: st.bad(f"{name} RDROP r_j={A[j].r} <= M={M}")
            # MINSET on intervals with r > M on [fi+1, fj]
            if all(A[t].r > M for t in range(fi + 1, fj + 1)):
                st.c["MINSET_intervals"] += 1
                def Mn(t, ref):
                    return {x for x in exits if x in A[t].F and coarse(g, oplus_o(g, o, A[t].Xi[x]), M) == ref}
                for t in range(fi + 1, fj + 1):
                    S = A[t]
                    if S.lamX[o] == o: continue
                    free = [x for x in exits if x in S.F]
                    mn = min(ck(g, oplus_o(g, o, S.Xi[x]), M) for x in free)
                    if ck(g, S.theta, M) != mn: st.bad(f"{name} MINSET (a) at {t}")
                    if S.sbar not in S.F or coarse(g, oplus_o(g, o, S.Xi[S.sbar]), M) != coarse(g, S.theta, M): st.bad(f"{name} MINSET (a) attained at sbar")
                    st.c["MINSET_a_states"] += 1; st.mxu("MINSET_max_|Mn|", len(Mn(t, coarse(g, S.theta, M))))
                for t in range(fi + 1, fj):
                    a_, b_ = A[t], A[t + 1]
                    for x in exits:
                        if x in b_.F:
                            if x not in a_.F: st.bad(f"{name} MINSET (b) exit {x} became free inside interval")
                            elif coarse(g, oplus_o(g, o, a_.Xi[x]), M) != coarse(g, oplus_o(g, o, b_.Xi[x]), M): st.bad(f"{name} MINSET (b) free exit {x} moved")
                    mt = Mn(t, coarse(g, a_.theta, M)); surv = mt & b_.F
                    changed = coarse(g, a_.theta, M) != coarse(g, b_.theta, M)
                    absorbed = mt - b_.F
                    if absorbed: st.c["MINSET_members_absorbed"] += len(absorbed)
                    if changed != (not surv): st.bad(f"{name} MINSET (c) survivor form at {t}")
                    if changed: st.c["MINSET_theta_coarse_changes_inside (literal (c) / NJB would forbid)"] += 1
                    if not Mn(t + 1, coarse(g, b_.theta, M)): st.bad(f"{name} MINSET (a) Mn empty at {t+1}")
            # (d) at block fallbacks f_i (i < N-1 handled; f_i with (h) at f_i+1)
            if A[fi + 1].hh and A[fi].lamX[o] != o:
                m0 = {x for x in exits if x in A[fi].F and coarse(g, oplus_o(g, o, A[fi].Xi[x]), M) == coarse(g, A[fi].theta, M)}
                m1 = {x for x in exits if x in A[fi + 1].F and coarse(g, oplus_o(g, o, A[fi + 1].Xi[x]), M) == coarse(g, A[fi + 1].theta, M)}
                st.c["MINSET_d_fallbacks"] += 1
                if not m0 <= m1: st.bad(f"{name} MINSET (d) at fallback {fi}")
        st.mxu("max_D_M", D)
        if D > (d_o - 1) + rel: st.bad(f"{name} PL(c') D={D} > {(d_o - 1) + rel}")
        if N > nE * (d_o + rel): st.bad(f"{name} PL(c') N={N}")
        rdrop_block = any(A[t].r <= M for t in range(F[0], F[-1] + 1))
        if rdrop_block: st.c["blocks_with_r<=M_somewhere (PL (c) hypothesis fails; PL (c') covers)"] += 1
    if tot_ge0 > nE * (n * d_o + relS): st.bad(f"{name} PL-S' {tot_ge0}")
    # NO-RF-OLD, Corollary, ENT-SHAPE
    for i, k0 in enumerate(fb):
        L = M_of(A[k0]); nxt = fb[i + 1] if i + 1 < len(fb) else s1
        tstar = k0
        while tstar + 1 <= nxt and A[tstar + 1].r > L: tstar += 1
        if tstar <= k0 + 1: continue
        for j in range(k0 + 1, tstar):
            if fbs[j]: continue
            if L < INF and coarse(g, A[j].theta, L) != coarse(g, A[j + 1].theta, L):
                st.c["NORF_rises_above_L_after_fallback"] += 1
                for t in range(j + 1, tstar + 1):
                    st.c["NORF_post_rise_states"] += 1
                    for (y, z) in A[t].gates:
                        if y in A[j].Rr and y in A[t].Rr and z in A[t].F: st.bad(f"{name} NORF gate ({y},{z}) at {t}, j={j}, k0={k0}")
                if tstar == nxt and nxt < s1 and fbs[nxt]:
                    st.c["NORF_fallback_after_rise"] += 1
                    k = nxt
                    for (y, z), lv in A[k].gates.items():
                        if lv == L and L >= 0 and y in A[k].Rr and z in A[k].F:
                            st.c["ENT_SHAPE_gates"] += 1
                            if y in A[j].Rr: st.bad(f"{name} ENT (1) y not an entrant")
                            zeta = coarse(g, A[k].Xi[z], L)
                            for t in range(k0, k + 1):
                                if coarse(g, b(A[t], y), L) != zeta: st.bad(f"{name} ENT (1) COARSE_L(b y) at {t}")
                                if beta_good(g, b(A[t], y), L): st.bad(f"{name} ENT (2) b good at {t}")
                                if coarse(g, A[t].Xi[z], L) != zeta: st.bad(f"{name} ENT (4) COARSE_L(Xi z) at {t}")
                            if beta_good(g, A[k0].Xi[z], L) or not beta_good(g, A[k].Xi[z], L): st.bad(f"{name} ENT (4) beta of z")
                            ups = [t for t in range(k0, k) if beta_good(g, A[t + 1].Xi[z], L) != beta_good(g, A[t].Xi[z], L)]
                            if any(fbs[t] for t in ups): st.bad(f"{name} ENT (5) rise at a fallback")
                break

def check_run(g, o, A, fbs, rng, st, name):
    st.c["runs"] += 1; st.c["transitions"] += len(fbs); st.c["fallbacks"] += sum(fbs)
    for s0, s1 in scope_runs(A, fbs, o): check_scope(g, o, A, fbs, s0, s1, st, f"{name}[{s0},{s1}]")

def main():
    st = FC.Stats(); args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, rng, st, f"seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, rng, st, f"{os.path.basename(path)}#{r}")
    FC.report(st)

if __name__ == "__main__":
    main()
