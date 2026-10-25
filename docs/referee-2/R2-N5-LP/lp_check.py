#!/usr/bin/env python3
"""REFEREE-2 successor 5 (Opus 5.5, D15): mechanical check of packet P-N5-LP (docs/new/P-N5-LP-box32.md sha1 d2c8121a @ trunk bc42f2c).
Own code on my R2-N5-FB/fb_check.py (SPEC run asserted = n5.run; Xi_k = Theta_{H_k} code link checked there; levels, COARSE).
PHASE here = a maximal run of transitions with lambda_Xi and tau constant (the packet's definition; coarser than R25's key).
Checks: Lemma U (L_k < inf; COARSE_{L_k} frozen; NU => Xi unchanged); HI (gate edges above L_k unchanged, own-cycle-node switchers
excluded) and its Consequence (M_{k+1} = M_k if M_k > L_k, M_{k+1} <= L_k if M_k = L_k); UL; GR (a), (b); NU (run length <= sum(deg-1)
over Even; every NU switch is at an own cycle node); Theorem LP (both inequalities per phase); on C^1O: DF as stated and DF' (y not its
own cycle node), BAND, WAKE, Corollary LP' (eps <= S_o, rho <= 2f + S_o + 2X + K, J <= S_o, the T bound).
Usage: lp_check.py general N nmin nmax seed | c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FB"))
import fb_check as F
RC, lpg, INF, BOT, lev, coarse = F.RC, F.lpg, F.INF, F.BOT, F.lev, F.coarse

def returns(f, o):
    x, seen = f[o], set()
    while x not in seen:
        if x == o: return True
        seen.add(x); x = f[x]
    return False

def extra(g, E, S, s, t, o):
    n = g.n
    if o is not None:
        S.H1 = not returns(S.H, o)
        fW = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
        S.H2 = not returns(fW, o)
        S.ct, S.cw = S.Xi[o][0], S.W[o][0]
        S.rf = (S.H1 or S.ct == o) and (S.H2 or S.cw == o)

def relevant(g, A, B, s0, s1):
    """List of (vertex, lev) of relevant changes at k -> k+1."""
    out = []
    for v in range(g.n):
        if A.lam[v] == v: continue
        if g.owner[v] == 0 and s0[0][v] != s1[0][v]: out.append((v, lev(A.Xi[s0[0][v]], A.Xi[s1[0][v]]), "E"))
        if g.owner[v] == 1 and A.sbar[v] != B.sbar[v]: out.append((v, lev(A.Xi[A.sbar[v]], A.Xi[B.sbar[v]]), "O"))
    return out

def good(E, x, l, Lv):
    """l-good: (u_l in P(x)) <=> Omega(u_l) even; requires rank c(x) < l."""
    u = Lv[l]
    return (((x[1] >> l) & 1) == 1) == (E.par[u] == 0)

def check_run(g, s, t, st, name, o, rng):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    if (len(fbs), sum(fbs)) != F.n5.run(g, "n5", ({v: s[v] for v in range(g.n) if g.owner[v] == 0},
                                                   {v: t[v] for v in range(g.n) if g.owner[v] == 1}))[:2]:
        st.bad(f"{name} run differs from n5.run")
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k, S in enumerate(A): extra(g, E, S, states[k][0], states[k][1], o)
    n = g.n; T = len(fbs)
    Lv = [None] * n
    for v in range(n): Lv[E.rank[v]] = v
    inph = [A[k].lam == A[k + 1].lam and states[k][1] == states[k + 1][1] for k in range(T)]
    st.c["runs"] += 1; st.c["transitions"] += T
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        phase(g, E, A, states, fbs, k, j, st, f"{name}[{k},{j})", o, Lv)
        k = j

def phase(g, E, A, states, fbs, k0, k1, st, name, o, Lv):
    n = g.n; m = sum(len(E.succ[v]) for v in range(n)); nE = [v for v in range(n) if g.owner[v] == 0]
    Ls = []; rel = []; evonly = []
    st.c["phases"] += 1
    for k in range(k0, k1):
        A0, A1, s0, s1 = A[k], A[k + 1], states[k], states[k + 1]
        R = relevant(g, A0, A1, s0, s1)
        L = max([x[1] for x in R], default=BOT)
        Ls.append(L); rel.append(L != BOT)
        st.c["transitions_in_phase"] += 1
        # ---- Lemma U
        if L >= INF: st.bad(f"{name} U: L_k = inf at {k}")
        if any(coarse(A1.Xi[v], L) != coarse(A0.Xi[v], L) for v in range(n)): st.bad(f"{name} U: COARSE_L moved at {k} L={L}")
        st.c["U_checks"] += 1
        # ---- own-cycle-node switches above L_k (not covered by HI; the Consequence needs them absent)
        for y in nE:
            if s0[0][y] != s1[0][y] and A0.lam[y] == y:
                st.c["own_cycle_node_switches"] += 1
                if lev(A0.Xi[s0[0][y]], A0.Xi[s1[0][y]]) > L: st.c["own_cycle_node_switch_above_L"] += 1
        # ---- HI and its Consequence
        if L != BOT:
            for y in nE:
                switched = s0[0][y] != s1[0][y]
                if switched and A0.lam[y] == y: continue
                g0 = {z: A0.gl[(y, z)] for (yy, z) in A0.Is if yy == y and A0.gl[(y, z)] > L}
                g1 = {z: A1.gl[(y, z)] for (yy, z) in A1.Is if yy == y and A1.gl[(y, z)] > L}
                st.c["HI_checks"] += 1
                if g0 != g1: st.bad(f"{name} HI at {k} y={y}: {g0} vs {g1}")
            if A0.M > L and A0.M < INF + 1:
                st.c["HI_cons_M>L"] += 1
                if A1.M != A0.M:
                    st.c["HI_consequence_fails(M_k>L_k, M_{k+1}!=M_k)"] += 1
                    st.examples.setdefault("HIcons", f"{name} k={k} L={L} M_k={A0.M} M_k+1={A1.M}")
            if A0.M == L:
                st.c["HI_cons_M=L"] += 1
                if A1.M > L: st.c["HI_consequence_fails(M_k=L_k, M_{k+1}>L_k)"] += 1
        # ---- UL, GR
        if L >= 0 and L < INF:
            att = [x for x in R if x[1] == L]
            if any(x[2] == "E" and x[0] == Lv[L] for x in att): st.bad(f"{name} UL at {k}")
            st.c["UL_checks"] += 1
            for y, lv_, kind in att:
                if kind != "E": continue
                c = A0.lam[y]
                st.c["GRb_checks"] += 1
                if not (E.rank[c] < L and not good(E, A0.Xi[y], L, Lv) and good(E, A1.Xi[y], L, Lv)): st.bad(f"{name} GR(b) at {k} y={y}")
            if not any(x[2] == "E" for x in att): evonly.append(k)
        for l in range(n):
            if L == BOT or L <= l:
                for v in range(n):
                    if E.rank[A0.lam[v]] < l and good(E, A0.Xi[v], l, Lv) and not good(E, A1.Xi[v], l, Lv):
                        st.bad(f"{name} GR(a) at {k} l={l} v={v}")
        # ---- NU
        if L == BOT:
            st.c["NU_transitions"] += 1
            if A1.Xi != A0.Xi: st.bad(f"{name} NU: Xi changed at {k}")
            for y in nE:
                if s0[0][y] != s1[0][y] and A0.lam[y] != y: st.bad(f"{name} NU: non-cycle-node switch at {k}")
    # NU runs
    bound_nu = sum(len(E.succ[y]) - 1 for y in nE)
    run = 0
    for r in rel + [True]:
        if not r: run += 1
        else:
            if run > bound_nu: st.bad(f"{name} NU run {run} > {bound_nu}")
            st.mx["max_NU_run"] = max(st.mx["max_NU_run"], run); run = 0
    # Theorem LP
    Tp = k1 - k0; Trel = sum(rel)
    relk = [k0 + i for i in range(Tp) if rel[i]]
    rises = [(relk[i], relk[i + 1]) for i in range(len(relk) - 1) if Ls[relk[i + 1] - k0] > Ls[relk[i] - k0]]
    rho = len(rises); eps = len(evonly)
    if Tp > (m - n + 1) * (Trel + 1): st.bad(f"{name} LP T={Tp} > {(m - n + 1) * (Trel + 1)}")
    if n >= 2 and Trel > (n + 1) * (rho + 1) * n * (n - 1) + eps: st.bad(f"{name} LP T_rel={Trel} rho={rho} eps={eps}")
    st.mx["max_T_phase"] = max(st.mx["max_T_phase"], Tp); st.mx["max_rho"] = max(st.mx["max_rho"], rho)
    st.c["rises"] += rho; st.c["eps"] += eps
    if o is None: return
    # ---- C^1O: DF, BAND, WAKE, Corollary
    f = sum(fbs[k0:k1]); X = sum(1 for k in range(k0, k1) if A[k].Rbar != A[k + 1].Rbar)
    So = sum(1 for k in range(k0, k1) if A[k].lam[o] != o and A[k].sbar[o] != A[k + 1].sbar[o])
    for k in range(k0, k1):
        if fbs[k]: continue
        s0, s1 = states[k][0], states[k + 1][0]
        for y in nE:
            arena = {s0[y]} | {z for (x, z) in A[k].Is if x == y}
            a = s1[y]
            for z in arena:
                if (y, z) not in A[k + 1].gl: continue
                own = A[k + 1].lam[y] == y
                st.c["DF_checks"] += 1
                if a not in A[k + 1].Rbar:
                    st.c[f"DF_as_stated_fails own_cycle_node={own}"] += 1
                    if not own: st.bad(f"{name} DF' (y not own cycle node) fails at {k} y={y}")
                # first step of DF' (no improvement in the arena), for y not its own W-cycle node
                if A[k + 1].W[y][0] != y and E.key(A[k + 1].W[z]) > E.key(A[k + 1].W[a]): st.bad(f"{name} DF' step 1 at {k} y={y}")
    # BAND at every state of the phase
    for k in range(k0, k1 + 1):
        S = A[k]
        if not S.rf or S.ct == S.cw: continue
        for (y, z), lv_ in S.gl.items():
            a = states[k][0][y]
            if lv_ < 0 or lv_ >= INF or a not in S.Rbar or z not in S.Rbar or E.key(S.W[z]) > E.key(S.W[a]): continue
            st.c["BAND_checks"] += 1
            if not (E.rank[S.ct] < lv_ < E.rank[S.cw] and S.W[z][1] == S.W[a][1]): st.bad(f"{name} BAND at {k} y={y} z={z}")
    # WAKE
    K = 0
    relk = [k for k in range(k0, k1) if rel[k - k0]]
    for i in range(len(relk) - 1):
        k, kp = relk[i], relk[i + 1]
        if any(fbs[x] for x in range(k, kp + 1)) or any(A[x].Rbar != A[x + 1].Rbar for x in range(k, kp + 1)): continue
        Lk = Ls[k - k0]; wk = False
        for y, lv_, kind in relevant(g, A[kp], A[kp + 1], states[kp], states[kp + 1]):
            if kind != "E" or lv_ <= Lk: continue
            wk = True; st.c["wakes"] += 1
            a, z = states[kp][0][y], states[kp + 1][0][y]
            if a not in A[kp].Rbar or z not in A[kp].Rbar: st.bad(f"{name} WAKE a/z not in R at {kp}")
            S = A[kp]
            if S.rf and not E.rank[S.cw] > E.rank[S.ct]: st.bad(f"{name} WAKE route form not U1 at {kp}")
        K += wk
    # Corollary
    J = sum(1 for k in range(k0, k1) if any(coarse(A[k + 1].Xi[v], A[k].M) != coarse(A[k].Xi[v], A[k].M) for v in range(g.n)))
    if eps > So: st.bad(f"{name} LP' eps {eps} > S_o {So}")
    if rho > 2 * f + So + 2 * X + K: st.bad(f"{name} LP' rho {rho} > {2 * f + So + 2 * X + K}")
    if J > So: st.bad(f"{name} LP' J {J} > S_o {So}")
    Tb = (m - n + 1) * ((n + 1) * (2 * f + So + 2 * X + K + 1) * n * (n - 1) + So + 1)
    if Tp > Tb: st.bad(f"{name} LP' T bound")
    st.c["C1O_phases"] += 1; st.mx["max_K"] = max(st.mx["max_K"], K); st.mx["max_S_o"] = max(st.mx["max_S_o"], So)

def main():
    st = F.Stats(); st.examples = {}; mode = sys.argv[1]
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
        for r in range(runs):
            s, t = F.start(g, rng, r > 0); check_run(g, s, t, st, f"{os.path.basename(path)}#{r}", o, rng)
    F.report(st)
    for k, v in st.examples.items(): print("example", k, v)

if __name__ == "__main__":
    main()
