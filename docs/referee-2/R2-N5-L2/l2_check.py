#!/usr/bin/env python3
"""REFEREE-2 successor 7 (Opus 5.5, D15): mechanical check of packet P-N5-L2 (docs/new/P-N5-L2-box34.md sha1 cbea0739 @ trunk 04b3f48).
Own code: my lane's R2-N5-FRZ/frz_check.py (own N5 with any S4a arena optimum, on R2-N5-RE/re_check.py). No lane script, no REFEREE
probe. Every game asserts exactly one Odd vertex with out-degree > 1. Phase key (lambda_Xi, tau).
Checks:
  H3C    H3-CONST: at H2 states c_w = lambda(tau(o)); H3 uniform over the phase's H2 states; with an (h) state, (h) <=> H1 and H2.
  H2S    H2-STICK: in-phase S4a step with H1 and not-H2 at s => not-H2 at s+1; Corollary: in fallback-free runs with H1 throughout, the
         H2 states and the (h) states form prefixes.
  GP     Lemma G' at H3 and not-H1 states: (a) not-H2, c in Rbar; (b) c-first => Xi = W; o-first => Xi = pi + theta, W = pi + w, pi
         disjoint from P(theta), P(w), c; (c) lev(Xi, W) <= r everywhere.
  FRZ'   FREEZE' on H3 windows (n states, H3, r <= l): (a) at t >= F with an H2-or-H3 state at or after t; (b) at H2-or-H3 t.
         Also Lemma P^c_l (frz_check.check_pc) on maximal H3 windows, Step 1 at H3 states, Step 2 at consecutive H3 states.
  RC     R-CONST: at not-H1 states Rbar = U = lambda^-1(c_theta); no crossing between consecutive not-H1 states.
  HI     H1-INT: P(theta) = {} states form one interval; not-H1 states and pre-drop states lie in it; theta = (c, {}, len) monotone there,
         <= n-1 changes.
  XR'    X-RUN': per maximal fallback-free run: crossings with both ends in P <= 13(d_o+1)n^3 (t_Q+1) + t_Q; per H1 run of P
         <= 13(d_o+1)n^3; no crossing inside not-H1 runs; REL_Q <= d_o (C+1); R-STICK after P.
Usage: l2_check.py random N nmin nmax seed [--rand] | inst game.pg [runs] [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC; INF, BOT = FC.INF, FC.BOT; lev, coarse, ck = FC.lev, FC.coarse, FC.ck

def first_on_route(f, v, o, c):
    """walk the (sigma, tau)-play from v: 'c' if c is met before o, 'o' otherwise (v in Rbar)"""
    x, seen = v, set()
    while x not in seen:
        if x == o: return "o"
        if x == c: return "c"
        seen.add(x); x = f[x]
    return None

def route(f, v, o):
    p, x = [], v
    while x != o: p.append(x); x = f[x]
    return p

def path_set(f, v, c):
    """vertices of v's play before its first visit of c"""
    p, x = [], v
    while x != c: p.append(x); x = f[x]
    return p

def check_state(g, o, S, st, name):
    lam = S.lamX
    if S.H2:
        st.c["H3C_H2_states"] += 1
        if S.W[o][0] != lam[S.tu[o]]: st.bad(f"{name} H3C c_w != lambda(tau(o))")
    if S.H3 and not S.H1:
        st.c["GP_H3_notH1_states"] += 1
        c = S.theta[0]
        if S.H2: st.bad(f"{name} GP (a) H2 holds")
        if c not in S.Rbar: st.bad(f"{name} GP (a) c not in Rbar")
        if c == o:
            st.c["GP_c=o"] += 1
            if S.theta != (o, frozenset(), 0) or S.w != S.theta: st.bad(f"{name} GP remark c = o")
        Pth = set(path_set(S.fh, o, c)) if c != o else set()
        Pw = set(path_set(S.f, o, c)) if c != o else set()
        for v in S.Rbar:
            kind = "o" if v == o else first_on_route(S.f, v, o, c)
            if kind == "c":
                st.c["GP_c_first"] += 1
                if S.Xi[v] != S.W[v]: st.bad(f"{name} GP (b) c-first v={v} Xi != W")
            else:
                st.c["GP_o_first"] += 1
                pi = route(S.f, v, o)
                if (set(pi) & (Pth | Pw)) or c in pi: st.bad(f"{name} GP (b) route of {v} meets a path / c")
                if S.Xi[v] != RC.prefix(g, pi, S.theta) or S.W[v] != RC.prefix(g, pi, S.w): st.bad(f"{name} GP (b) o-first frames v={v}")
        for v in range(g.n):
            if lev(g, S.Xi[v], S.W[v]) > S.r: st.bad(f"{name} GP (c) v={v}")
    if not S.H1:
        st.c["RC_notH1_states"] += 1
        U = {v for v in range(g.n) if lam[v] == S.theta[0]}
        if S.Rbar != U: st.bad(f"{name} RC Rbar != U")

def h3(S): return S.H3

def check_phase(g, o, A, fbs, a, b, rng, st, name):
    n = g.n; d_o = len(set(g.succ[o]))
    # H3-CONST uniformity
    H2s = [t for t in range(a, b + 1) if A[t].H2]
    if H2s and len({A[t].H3 for t in H2s}) > 1: st.bad(f"{name} H3C H3 not uniform over H2 states")
    if any(A[t].hh for t in range(a, b + 1)):
        st.c["H3C_phases_with_h"] += 1
        for t in range(a, b + 1):
            if A[t].hh != (A[t].H1 and A[t].H2): st.bad(f"{name} H3C (h) != H1 and H2 at {t}")
        runs = 0; prev = False
        for t in range(a, b + 1):
            if A[t].hh and not prev: runs += 1
            prev = A[t].hh
        st.mxu("ONE-H_max_h_runs_per_phase (sec.8, no claim)", runs)
    # H2-STICK
    for s in range(a, b):
        if fbs[s] == 0 and A[s].H1 and not A[s].H2:
            st.c["H2S_steps"] += 1
            if A[s + 1].H2: st.bad(f"{name} H2S H2 restored at S4a step {s}")
        if fbs[s] == 1 and A[s].H1 and not A[s].H2 and A[s + 1].H2: st.c["H2S_restart_by_fallback (sec.8 open (2), no claim)"] += 1
    # R-CONST no crossing
    for s in range(a, b):
        if not A[s].H1 and not A[s + 1].H1:
            st.c["RC_notH1_pairs"] += 1
            if A[s].Rr != A[s + 1].Rr: st.bad(f"{name} RC crossing between not-H1 states {s}")
    # H1-INT
    E = [t for t in range(a, b + 1) if not A[t].theta[1]]
    if E:
        if E != list(range(E[0], E[-1] + 1)): st.bad(f"{name} HI (a) P(theta) = {{}} not an interval")
        I = set(E)
        for t in range(a, b + 1):
            if not A[t].H1 and t not in I: st.bad(f"{name} HI (b) not-H1 state {t} outside I")
        for t in range(a, b):
            if A[t].H1 and not A[t + 1].H1:
                st.c["HI_drops"] += 1
                if t not in I: st.bad(f"{name} HI (b) pre-drop state {t} outside I")
        ch = 0
        for t in range(E[0] + 1, E[-1] + 1):
            if A[t].theta != A[t - 1].theta:
                ch += 1
                if g.key(A[t].theta) < g.key(A[t - 1].theta): st.bad(f"{name} HI (c) theta dropped")
        if ch > n - 1: st.bad(f"{name} HI (c) {ch} changes")
        st.mxu("HI_max_theta_changes_on_I", ch)
    drops = sum(1 for t in range(a, b) if A[t].H1 and not A[t + 1].H1)
    st.mxu("ONE-DROP_max_drops_per_phase (sec.8, no claim)", drops)
    # FREEZE' on H3 windows; P^c on maximal H3 windows; Step 1 / Step 2
    for t in range(a, b + 1):
        if A[t].H3:
            st.c["STEP1'_H3_states"] += 1
            for v in range(n):
                if coarse(g, A[t].Xi[v], A[t].r) != coarse(g, A[t].W[v], A[t].r): st.bad(f"{name} STEP1' at {t}")
    for t in range(a, b):
        if A[t].H3 and A[t + 1].H3:
            l0 = max(A[t].r, A[t + 1].r)
            for L in [l0] + list(range(max(l0 + 1, -1), n)):
                st.c["STEP2'_checks"] += 1
                if any(ck(g, A[t + 1].W[v], L) < ck(g, A[t].W[v], L) for v in range(n)): st.bad(f"{name} STEP2' at {t} L={L}"); break
    seen = set()
    for L in FC.levels(n):
        k = a
        while k <= b:
            if not (A[k].H3 and A[k].r <= L): k += 1; continue
            e = k
            while e + 1 <= b and A[e + 1].H3 and A[e + 1].r <= L: e += 1
            if (k, e) not in seen:
                seen.add((k, e)); Lw = max(A[i].r for i in range(k, e + 1))
                nh1 = sum(1 for i in range(k, e + 1) if not A[i].H1)
                if e > k and nh1:
                    st.c["PC'_windows_with_notH1"] += 1
                    FC.check_pc(g, o, A, k, e, Lw, rng, st, name + "'")
            k = e + 1
    H23later = [False] * (b + 2)
    for k in range(b, a - 1, -1): H23later[k] = A[k].H2 or A[k].H3 or H23later[k + 1]
    for L in FC.levels(n):
        cnt = 0; Fk = None
        for k in range(a, b + 1):
            cnt = cnt + 1 if (A[k].H3 and A[k].r <= L) else 0
            if cnt >= n: Fk = k; break
        if Fk is None: continue
        win_nh1 = any(not A[i].H1 for i in range(Fk - n + 1, Fk + 1))
        st.c["FRZ'_freezes"] += 1
        if win_nh1: st.c["FRZ'_freezes_window_with_notH1"] += 1
        XF = [coarse(g, x, L) for x in A[Fk].Xi]; WF = [coarse(g, x, L) for x in A[Fk].W]
        if XF != WF: st.bad(f"{name} FRZ' Step 1 at F")
        for t in range(Fk + 1, b + 1):
            if H23later[t]:
                st.c["FRZ'_a_checks"] += 1
                if not A[t].H1: st.c["FRZ'_a_checks_at_notH1_t"] += 1
                if [coarse(g, x, L) for x in A[t].Xi] != XF: st.bad(f"{name} FRZ' (a) t={t} L={L}")
            if A[t].H2 or A[t].H3:
                st.c["FRZ'_b_checks"] += 1
                if [coarse(g, x, L) for x in A[t].W] != WF: st.bad(f"{name} FRZ' (b) t={t} L={L}")
    # X-RUN' per maximal fallback-free run
    k = a
    while k < b:
        if fbs[k]: k += 1; continue
        e = k
        while e < b and fbs[e] == 0: e += 1
        P = []
        for t in range(k, e + 1):
            if A[t].H3: P.append(t)
            else: break
        if A[k].H1 and all(A[t].H1 for t in range(k, e + 1)):
            h2 = [A[t].H2 for t in range(k, e + 1)]
            if any(h2[i] and not h2[i - 1] for i in range(1, len(h2))): st.bad(f"{name} H2S corollary: H2 states not a prefix")
        if P:
            p0, p1 = P[0], P[-1]
            for s in range(p1 + 1, e):
                if A[s].Rr - A[s + 1].Rbar: st.bad(f"{name} XR' R-STICK leave after P at {s}")
            tq = sum(1 for s in range(p0, p1) if A[s].H1 != A[s + 1].H1)
            C = sum(1 for s in range(p0, p1) if A[s].Rr != A[s + 1].Rr)
            st.c["XR'_runs"] += 1; st.mxu("XR'_max_toggles_t_Q", tq); st.mxu("XR'_max_C", C)
            if tq: st.c["XR'_runs_with_toggle"] += 1
            if any(not A[t].H1 for t in P): st.c["XR'_runs_with_notH1_in_P"] += 1
            B = 13 * (d_o + 1) * n ** 3
            if C > B * (tq + 1) + tq: st.bad(f"{name} XR' (a) {C}")
            i = 0
            while i < len(P):
                j = i
                while j + 1 < len(P) and A[P[j + 1]].H1 == A[P[i]].H1: j += 1
                cr = sum(1 for s in range(P[i], P[j]) if A[s].Rr != A[s + 1].Rr)
                if A[P[i]].H1:
                    if cr > B: st.bad(f"{name} XR' H1 run crossings {cr}")
                else:
                    st.c["XR'_notH1_runs"] += 1
                    if cr: st.bad(f"{name} XR' crossing inside a not-H1 run")
                i = j + 1
            rel = sum(len((A[s].Rr - A[s + 1].Rbar) & set(g.succ[o])) for s in range(k, e))
            if rel > d_o * (C + 1): st.bad(f"{name} XR' (b) REL {rel} > d_o (C+1)")
            st.mxu("XR'_max_REL_Q", rel)
        k = e

def check_run(g, o, A, fbs, rng, st, name):
    T = len(fbs); st.c["runs"] += 1; st.c["transitions"] += T; st.c["fallbacks"] += sum(fbs)
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        st.c["phases"] += 1
        for t in range(k, j + 1): check_state(g, o, A[t], st, f"{name}@{t}")
        check_phase(g, o, A, fbs, k, j, rng, st, f"{name}[{k},{j}]")
        k = j

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
