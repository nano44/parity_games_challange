#!/usr/bin/env python3
"""REFEREE-2 (Opus 5.5, D15) mechanical check of packet P-N5-XA (docs/new/P-N5-XA-box27.md @ trunk b70aa59).
Uses my own definitions and N5 implementation from ../R2-N5-RE/re_check.py (REFEREE-2 code; no lane code except, in spec mode,
n5.py's functions for the STATE SEQUENCE). Throttled stretch S = maximal run of states, consecutive transitions in one joint
lambda-phase, tau, theta, w constant, theta strictly below w, (h) at every state.
Checks: §1 (W's cycle-node map constant on S and equal to Xi's; u* off every route), Lemma C (coarse Xi = coarse W; coarse
monotone), FBL (classification of switched edges at fallbacks; also the stronger gate form 'no R->R and no F->R gate edges' that
FBF step 1 uses), CR-vacuity (no non-flat W-improving gate edge at a fallback), FBF (after a fallback: R_t subset of R_{L+1}, paths
unchanged since L, no entry), Lemma P^c (every simple path, n <= PMAX), Lemma CR (coarse constant from k0+n-1 on), Theorem XA
(re-entry after an S4a leave: strict coarse increase) and its count n(n-1).
Usage: xa_check.py random N nmin nmax seed [own|spec]  |  xa_check.py inst game.pg [start] [own|spec] [runs]"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
import re_check as rc

PMAX = 10

def coarse(g, val, ustar):
    c, P, l = val
    if ustar is None: return (c, P)
    return (c, frozenset(u for u in P if g.rank[u] > g.rank[ustar]))

def ccmp(g, a, b):
    """coarse order: reward of the cycle node, then signed weight of the (truncated) path set."""
    ka = g.key((a[0], a[1], 0))[:2]; kb = g.key((b[0], b[1], 0))[:2]
    return (ka > kb) - (ka < kb)

def simple_paths_to(g, f, u, maxlen):
    """All simple paths (x = r0, ..., rL = u) in the one-player graph of f restricted to Even's full edge sets (G_tau: Odd keeps f),
    L <= maxlen; yields (x, P(r), L) as value (u, P, L)."""
    pred = [[] for _ in range(g.n)]
    for v in range(g.n):
        succ = g.succ[v] if g.owner[v] == 0 else [f[v]]
        for w in succ: pred[w].append(v)
    out = []
    def rec(path, onpath):
        x = path[-1]
        L = len(path) - 1
        P = frozenset(v for v in path[1:] if g.rank[v] > g.rank[u])
        out.append((x, (u, P, L)))
        if L == maxlen: return
        for p in pred[x]:
            if p not in onpath and p != u:
                onpath.add(p); path.append(p); rec(path, onpath); path.pop(); onpath.discard(p)
    rec([u], {u})
    return out

def check_run(g, o, states, fbs, st, name):
    n = g.n; T = len(states) - 1
    A = [rc.analyse(g, o, *states[k]) for k in range(T + 1)]
    st.c["runs"] += 1; st.c["transitions"] += T
    inph = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU for k in range(T)]
    def same(k):
        return (inph[k] and states[k][1][o] == states[k + 1][1][o] and A[k].theta == A[k + 1].theta and A[k].w == A[k + 1].w)
    def thr(k): return A[k].h and g.cmp(A[k].theta, A[k].w) < 0
    st.c["thr_states"] += sum(1 for k in range(T + 1) if thr(k))
    k = 0
    while k <= T:
        if not thr(k): k += 1; continue
        k0 = k
        while k < T and same(k) and thr(k + 1): k += 1
        k1 = k; k += 1
        if k1 == k0: st.c["S_single_state"] += 1; continue
        stretch(g, o, A, states, fbs, k0, k1, st, name)

def stretch(g, o, A, states, fbs, k0, k1, st, name):
    n = g.n
    th, w = A[k0].theta, A[k0].w
    c = th[0]
    D = th[1] ^ w[1]
    ustar = max(D, key=lambda u: g.rank[u]) if D else None
    st.c["S_stretches"] += 1; st.c["S_transitions"] += k1 - k0
    st.c["S_ustar_none" if ustar is None else "S_ustar_some"] += 1
    st.mx["S_max_len"] = max(st.mx["S_max_len"], k1 - k0)
    if ustar is not None:
        side_w = (ustar in w[1])
        better_w = (g.even[ustar] if side_w else not g.even[ustar])
        if not better_w: st.bad(f"{name} S{k0}: u* not on w's better side")
        if ustar == o: st.bad(f"{name} S{k0}: u* = o")
    C = lambda val: coarse(g, val, ustar)
    lamW0 = tuple(A[k0].W[v][0] for v in range(n))
    for k in range(k0, k1 + 1):
        S = A[k]
        # §1: W's cycle-node map constant on S and equal to Xi's
        if tuple(S.W[v][0] for v in range(n)) != lamW0 or lamW0 != S.lamX: st.bad(f"{name} k={k} §1 lambda map")
        if ustar is not None and any(ustar in S.pi[v] for v in S.R): st.bad(f"{name} k={k} §1 u* on a route")
        # Lemma C
        for v in range(n):
            st.c["C_eq_checks"] += 1
            if C(S.Xi[v]) != C(S.W[v]): st.bad(f"{name} k={k} Lemma C eq v={v}")
            if k < k1:
                st.c["C_mono_checks"] += 1
                if ccmp(g, C(A[k + 1].Xi[v]), C(S.Xi[v])) < 0: st.bad(f"{name} k={k} Lemma C mono v={v}")
    # fallbacks: FBL, gate form, CR-vacuity, FBF
    first_fb = None
    for k in range(k0, k1):
        if not fbs[k]: continue
        S0, S1 = A[k], A[k + 1]
        st.c["FB_in_S"] += 1
        if ustar is None: st.c["FB_in_S_ustar_none"] += 1
        if first_fb is None: first_fb = k
        tag = "none" if ustar is None else "some"
        for x in range(n):
            if g.owner[x] != 0 or S0.f[x] == S1.f[x]: continue
            z = S1.f[x]
            st.c["FBL_switched_edges"] += 1
            if x in S0.R and z not in S0.R: st.c["FBL_leave"] += 1; continue
            if x not in S0.R and z not in S0.R and S0.lamX[x] == x and S0.W[z][0] == x:
                f2 = list(S0.f); f2[x] = z
                if rc.vals_of(g, f2)[0] == S0.W: st.c["FBL_flatFF"] += 1; continue
            st.c[f"FBL_OTHER(u*={tag})"] += 1
            st.ex(f"FBL_other_u*{tag}", f"{name} k={k} edge ({x},{z}) x_in_R={x in S0.R} z_in_R={z in S0.R} z_in_R_next={z in S1.R} c={c}")
            if ustar is not None: st.bad(f"{name} k={k} FBL switched edge ({x},{z}) neither leave nor flat F->F")
        for x, z in S0.Is:
            if x in S0.R and z in S0.R: st.c[f"gate_RR_at_fb(u*={tag})"] += 1; st.bad(f"{name} k={k} gate R->R at fallback")
            if x not in S0.R and z in S0.R:
                st.c[f"gate_FR_at_fb(u*={tag})"] += 1
                st.ex(f"gate_FR_u*{tag}", f"{name} k={k} gate ({x},{z}) c={c}")
                if ustar is not None: st.bad(f"{name} k={k} gate F->R at fallback with u* != none")
            if g.cmp(S0.W[z], S0.W[S0.f[x]]) > 0:
                st.c["fb_W_improving_gate"] += 1
                flat = S0.lamX[x] == x and S0.W[z][0] == x
                if not flat: st.bad(f"{name} k={k} non-flat W-improving gate edge at fallback ({x},{z})")
                if ccmp(g, C(S0.W[z]), C(S0.W[S0.f[x]])) > 0: st.bad(f"{name} k={k} coarse-strict gate edge at fallback ({x},{z})")
    if first_fb is not None:
        L = first_fb
        for t in range(L + 1, k1 + 1):
            st.c["FBF_checks"] += 1
            if not A[t].R <= A[L + 1].R: st.bad(f"{name} t={t} FBF R grew (fb at {L})")
            for v in A[t].R:
                if v not in A[L].R or A[t].pi[v] != A[L].pi[v]: st.bad(f"{name} t={t} FBF path of {v} changed (fb at {L})")
            if t < k1 and A[t + 1].R - A[t].R: st.bad(f"{name} t={t} FBF entry after fallback {L}")
    # Lemma P^c (every simple path) and Lemma CR
    if n <= PMAX:
        f0 = A[k0].f
        cyc_nodes = [u for u in range(n) if lamW0[u] == u]
        paths = []
        for u in cyc_nodes: paths += simple_paths_to(g, f0, u, n - 1)
        # G_tau's edges: Odd keeps tau (tau constant on S), so f0's Odd entries are the right ones
        for j in range(0, k1 - k0 + 1):
            Om = A[k0 + j].W
            for x, val in paths:
                if val[2] <= j:
                    st.c["Pc_checks"] += 1
                    if ccmp(g, C(Om[x]), C(val)) < 0: st.bad(f"{name} k0={k0} j={j} Lemma P^c x={x} r-value={val}")
    last_change = None
    for k in range(k0, k1):
        if any(C(A[k].W[v]) != C(A[k + 1].W[v]) for v in range(n)): last_change = k - k0 + 1
    if last_change is not None:
        st.mx["CR_last_coarse_change"] = max(st.mx["CR_last_coarse_change"], last_change)
        if last_change > n - 1: st.bad(f"{name} S{k0}: coarse change at transition {last_change} > n-1")
    # Theorem XA steps 4-5 as an order fact on real routes: for routes p (any state of S) and q (any state of S),
    # p + theta >= q + w (full order) implies COARSE(p + theta) > COARSE(q + w)   [needs u* != none]
    if ustar is not None:
        routes = {tuple(A[k].pi[v]) for k in range(k0, k1 + 1) for v in A[k].R}
        for p in routes:
            for q in routes:
                a, b = rc.prefix(g, list(p), th), rc.prefix(g, list(q), w)
                if g.cmp(a, b) >= 0:
                    st.c["XA_order_checks"] += 1
                    if ccmp(g, C(a), C(b)) <= 0: st.bad(f"{name} S{k0} XA order p={p} q={q}")
                else:
                    st.c["XA_order_premise_false"] += 1
    # Theorem XA
    nre = 0
    for x in range(n):
        k = k0
        while k < k1:
            if x in A[k].R and x not in A[k + 1].R:
                L = k; E1 = L + 1
                while E1 <= k1 and x not in A[E1].R: E1 += 1
                if E1 > k1: break
                kind = "fb" if fbs[L] else "arena"
                st.c[f"XA_reentry_after_{kind}_leave"] += 1
                if ustar is None: st.c["XA_reentry_ustar_none"] += 1
                elif kind == "arena":
                    nre += 1
                    if ccmp(g, C(A[E1].Xi[x]), C(A[L].Xi[x])) <= 0: st.bad(f"{name} XA x={x} L={L} E+1={E1}")
                k = E1
            else:
                k += 1
    if nre > n * (n - 1): st.bad(f"{name} S{k0}: {nre} XA re-entries > n(n-1)")
    st.mx["XA_max_per_stretch"] = max(st.mx["XA_max_per_stretch"], nre)

def main():
    st = rc.Stats()
    if sys.argv[1] == "random":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); mode = sys.argv[6] if len(sys.argv) > 6 else "own"
        rng = random.Random(seed)
        for i in range(N):
            g, o = rc.rand_game(rng, rng.randint(nmin, nmax)); s, t = rc.rand_start(rng, g)
            states, fbs = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
            check_run(g, o, states, fbs, st, f"seed{seed}#{i}")
    else:
        path = sys.argv[2]; g = rc.parse(open(path).read())
        o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
        mode, start, runs = "own", None, 20
        for a in sys.argv[3:]:
            if a in ("own", "spec"): mode = a
            elif a.isdigit(): runs = int(a)
            else: start = a
        rng = random.Random(1)
        for r in range(1 if mode == "spec" else runs):
            if start:
                s0, t0 = rc.read_start(start)
                s = [s0.get(v, g.succ[v][0]) for v in range(g.n)]; t = [t0.get(v, g.succ[v][0]) for v in range(g.n)]
            elif r == 0:
                def br(v, dual):
                    def rr(w_):
                        p = g.prio[w_] + (1 if dual else 0); r_ = p if p % 2 == 0 else -p
                        return (r_, w_ if r_ % 2 == 0 else -w_)
                    return max(g.succ[v], key=rr)
                s = [br(v, False) for v in range(g.n)]; t = [br(v, True) for v in range(g.n)]
            else:
                s, t = rc.rand_start(rng, g)
            states, fbs = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
            check_run(g, o, states, fbs, st, f"{os.path.basename(path)}#{r}")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for k, v in st.examples.items(): print(f"example {k}: {v}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c["VIOLATIONS"] else "OK", f"violations={st.c['VIOLATIONS']}")

if __name__ == "__main__":
    main()
