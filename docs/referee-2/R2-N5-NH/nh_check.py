#!/usr/bin/env python3
"""REFEREE-2 (Opus 5.5, D15) mechanical check of packet P-N5-NH (docs/new/P-N5-NH-box30.md @ trunk c7981ee).
Definitions and own N5 (random tie-breaks) from ../R2-N5-RE/re_check.py; "spec" mode = n5.py's state sequence.
Phase = lambda_Xi, lambda_U and tau constant across each transition. Crossing-free interval I = maximal run of a phase with R constant.
Checks:
  F1°  : on I, transitions with a Xi-change on F <= max(0, |F| - 1) (OTHER states included).
  TC   : (i) H1 <=> lambda_Xi(o) in F, H2 <=> tau(o) in F, both constant on I; (ii) under H2, (h) constant on I and OTHER all-or-none;
         (iii) H1 & not H2 => all OTHER; (iv) not H1 & not H2: EQ <=> theta = w, and EQ -> OTHER changes w. Consequence: #OTHER blocks.
  P3'  : on (theta, w)-pieces J with both frames in route form and rank(c_theta) > rank(c_w): (R1) Xi = pi + theta, W = pi + w on R;
         (R3) kappa-different routes are ordered alike in both frames; (R4) kappa monotone; step 1 freeze (kappa constant from the
         |R|-th transition of J); the count <= (n + 1)|R|. Gap probe G-NH-1: at S4a steps of J, (a) is sigma_{k+1}|R an optimum of
         R*_w's arena? (b) does W_{k+1}(x) >= (x.pi_z) + w hold for every kappa-strict gate edge (x, z) inside R (the single-switch
         inequality CR's B1 needs)? Counted separately when x lies on o's W-cycle (not H2).
  Cor  : under H2 on I, #pieces <= max(1, |F|).
Usage: nh_check.py random N nmin nmax seed [own|spec] | nh_check.py inst game.pg [start] [own|spec] [runs]"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
import re_check as rc

def cyc(f, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = f[x]
    return path[seen[x]:]

def check_run(g, o, states, fbs, st, name):
    n = g.n; T = len(states) - 1
    A = [rc.analyse(g, o, *s) for s in states]
    st.c["runs"] += 1; st.c["transitions"] += T
    for S in A:
        S.H1 = o not in cyc(S.fh, o); S.H2 = o not in cyc(S.f, o)
        S.typ = "EQ" if S.Xi == S.W else ("THR" if S.h else "OTHER")
        S.cW = cyc(S.f, o) if not S.H2 else []
    inph = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU and states[k][1][o] == states[k + 1][1][o] for k in range(T)]
    k = 0
    while k <= T:
        i0 = k
        while k < T and inph[k] and A[k].R == A[k + 1].R: k += 1
        interval(g, o, A, states, fbs, i0, k, st, name)
        k += 1

def interval(g, o, A, states, fbs, i0, i1, st, name):
    n = g.n
    R = A[i0].R; F = set(range(n)) - R
    st.c["intervals"] += 1
    if i1 > i0: st.c["intervals_multi"] += 1
    # F1°
    nf = sum(1 for j in range(i0, i1) if any(A[j].Xi[v] != A[j + 1].Xi[v] for v in F))
    if nf > max(0, len(F) - 1): st.bad(f"{name} F1° interval {i0}..{i1}: {nf} > max(0,{len(F)}-1)")
    if any(A[j].typ == "OTHER" for j in range(i0, i1 + 1)) and i1 > i0: st.c["F1°_intervals_with_OTHER"] += 1
    # TC
    for j in range(i0, i1 + 1):
        S = A[j]
        if S.H1 != (S.lamX[o] in F): st.bad(f"{name} TC(i) H1 at {j}")
        if S.H2 != (states[j][1][o] in F): st.bad(f"{name} TC(i) H2 at {j}")
        st.c["TC_state_checks"] += 1
    if len({A[j].H1 for j in range(i0, i1 + 1)}) > 1 or len({A[j].H2 for j in range(i0, i1 + 1)}) > 1:
        st.bad(f"{name} TC(i) not constant on {i0}..{i1}")
    H1, H2 = A[i0].H1, A[i0].H2
    types = [A[j].typ for j in range(i0, i1 + 1)]
    st.c[f"TC_case_H1={H1}_H2={H2}"] += 1
    if H2:
        if len({A[j].h for j in range(i0, i1 + 1)}) > 1: st.bad(f"{name} TC(ii) (h) not constant")
        if "OTHER" in types and any(t != "OTHER" for t in types): st.bad(f"{name} TC(ii) OTHER not all-or-none")
    if H1 and not H2 and any(t != "OTHER" for t in types): st.bad(f"{name} TC(iii)")
    if not H1 and not H2:
        for j in range(i0, i1 + 1):
            if (A[j].typ == "EQ") != (A[j].theta == A[j].w): st.bad(f"{name} TC(iv) EQ<=>theta=w at {j}")
        for j in range(i0, i1):
            if A[j].typ == "EQ" and A[j + 1].typ == "OTHER":
                st.c["TC_iv_EQ_OTHER"] += 1
                if A[j].w == A[j + 1].w: st.bad(f"{name} TC(iv) EQ->OTHER without w-change at {j}")
    blocks = sum(1 for j in range(len(types)) if types[j] == "OTHER" and (j == 0 or types[j - 1] != "OTHER"))
    wc = sum(1 for j in range(i0, i1) if A[j].w != A[j + 1].w)
    lim = 1 + wc if (not H1 and not H2) else 1
    if blocks > lim: st.bad(f"{name} TC consequence: {blocks} OTHER blocks > {lim}")
    # pieces
    def rf(S): return (S.H1 or S.lamX[o] == o, S.H2 or S.W[o][0] == o)
    pieces = 0
    j = i0
    while j <= i1:
        if not all(rf(A[j])): j += 1; continue
        p0 = j
        while j < i1 and all(rf(A[j + 1])) and A[j + 1].theta == A[p0].theta and A[j + 1].w == A[p0].w: j += 1
        pieces += 1
        piece(g, o, A, states, fbs, R, p0, j, st, name)
        j += 1
    if H2 and pieces > max(1, len(F)): st.bad(f"{name} Corollary: {pieces} pieces > max(1,{len(F)})")
    if H2: st.mx["Cor_max_pieces"] = max(st.mx["Cor_max_pieces"], pieces)

def piece(g, o, A, states, fbs, R, p0, p1, st, name):
    n = g.n
    th, w = A[p0].theta, A[p0].w
    ct, cw = th[0], w[0]
    st.c["pieces"] += 1
    rel = g.rank[ct] > g.rank[cw]
    st.c["pieces_ct_above_cw" if rel else ("pieces_ct_eq_cw" if ct == cw else "pieces_cw_above_ct(U1)")] += 1
    for j in range(p0, p1 + 1):          # (R1)
        S = A[j]
        for v in R:
            st.c["R1_checks"] += 1
            if S.Xi[v] != rc.prefix(g, S.pi[v], th) or S.W[v] != rc.prefix(g, S.pi[v], w): st.bad(f"{name} P3' (R1) j={j} v={v}")
    if not rel or p1 == p0: return
    st.c["P3_pieces_nontrivial"] += 1; st.c["P3_transitions"] += p1 - p0; st.mx["P3_max_len"] = max(st.mx["P3_max_len"], p1 - p0)
    kap = lambda pi: frozenset(u for u in pi if g.rank[u] > g.rank[ct])
    routes = {tuple(A[j].pi[v]) for j in range(p0, p1 + 1) for v in R}
    for a in routes:                     # (R3)
        for b in routes:
            if kap(a) != kap(b):
                st.c["R3_checks"] += 1
                if g.cmp(rc.prefix(g, list(a), th), rc.prefix(g, list(b), th)) != g.cmp(rc.prefix(g, list(a), w), rc.prefix(g, list(b), w)):
                    st.bad(f"{name} P3' (R3) {a} {b}")
    kc = lambda kk: (0, sum((1 if g.even[u] else -1) << g.rank[u] for u in kk))
    last = None
    for j in range(p0, p1):              # (R4), freeze
        for v in R:
            k0, k1 = kap(A[j].pi[v]), kap(A[j + 1].pi[v])
            if k0 != k1:
                last = j - p0 + 1
                if kc(k1) < kc(k0): st.bad(f"{name} P3' (R4) j={j} v={v}")
    if last is not None:
        st.mx["P3_last_kappa_change"] = max(st.mx["P3_last_kappa_change"], last)
        if last > len(R): st.bad(f"{name} P3' freeze: kappa change at transition {last} > |R|={len(R)}")
    cnt = sum(1 for j in range(p0, p1) if any(A[j].Xi[v] != A[j + 1].Xi[v] for v in R))
    st.mx["P3_max_count"] = max(st.mx["P3_max_count"], cnt)
    if cnt > (n + 1) * len(R): st.bad(f"{name} P3' count {cnt}")
    # G-NH-1 probe at S4a steps
    for j in range(p0, p1):
        if fbs[j]: continue
        S0, S1 = A[j], A[j + 1]
        for x, z in S0.Is:
            if x in R and z in R and kc(kap(S0.pi[z])) > kc(kap(S0.pi[S0.f[x]])) and x not in S0.pi[z] and x != z:
                oncyc = x in S0.cW
                st.c["G-NH-1_single_switch_checks" + ("_x_on_W_cycle" if oncyc else "")] += 1
                target = rc.prefix(g, [x] + S0.pi[z], w)
                if g.cmp(S1.W[x], target) < 0: st.bad(f"{name} G-NH-1 single-switch inequality fails j={j} ({x},{z}) on_cycle={oncyc}")
        # (a) is sigma_{k+1}|R an optimum of R*_w's arena?  R*_w: vertices R plus a sink t with value w (o -> t).
        if not S0.H2:
            st.c["G-NH-1_S4a_steps_notH2"] += 1
            # contracted game: copy G with o's edge redirected to a fresh self-loop sink carrying c_w's rank and parity
            sink = n
            prio = [2 * g.rank[v] + (0 if g.even[v] else 1) for v in range(n)] + [2 * g.rank[cw] + (0 if g.even[cw] else 1)]
            prio[cw] = prio[cw] if cw != o else prio[cw]
            owner = list(g.owner) + [1]
            succ = [list(g.succ[v]) for v in range(n)] + [[sink]]
            succ[o] = [sink]
            if cw == o:   # o itself is the W cycle node: give the sink o's rank, push o just below
                prio[sink] = prio[o]; prio[o] = -1 if prio[o] % 2 == 0 else -2
                prio = [p + 2 for p in prio]
            h = rc.Game(prio, owner, succ)
            f0 = [S0.f[v] if v != o else sink for v in range(n)] + [sink]
            arena = [sorted({S0.f[v]} | {zz for xx, zz in S0.Is if xx == v and zz in R}) if (g.owner[v] == 0 and v in R) else [f0[v]]
                     for v in range(n)] + [[sink]]
            _, opt = rc.even_optimum(h, f0, arena)
            f1 = [S1.f[v] if (v in R and v != o) else f0[v] for v in range(n)] + [sink]
            got = rc.vals_of(h, f1)[0]
            if any(got[v] != opt[v] for v in R): st.c["G-NH-1_R*_arena_not_optimal(notH2)"] += 1

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
