#!/usr/bin/env python3
"""REFEREE-2 successor 10 (Opus 5.5, D15): mechanical check of packet P-N5-LV2 (docs/si/P-N5-LV2-box12.md sha1 3b23a41f @ trunk 283bcb6).
Own code on R2-N5-LV/lv_check.py, R2-N5-ENT/ent_check.py and R2-N5-OUT/out_check.py (traces own | rand | spec). No lane script is
imported. Every game asserts exactly one Odd vertex with out-degree > 1. Scope runs, M_k, r_k, (h), phase key (lambda_Xi, tau(o)) as in
ent_check.py. Fallback = S4c transition k -> k+1 (fbs[k]).
Checks (packet items):
  STALE   §1 every Even-switching S4c fallback k0, every later state k of the run, every gate (y, z) at k: Xi_k(z) != Xi_k0(z).
  EVG     §2 k0 an in-phase THR S4c fallback with (h), k > k0 in the same phase, gate (y, z) at k with z in F_k: z's (sigma_k, tau)-play
          is not contained in F_k0.
  CLASS   §8 every in-scope fallback is in exactly one class: level >= 0 (r >= 0, M >= 0) / block (r >= 0, M = -1) / none (r = -1) / EQ;
          M <= r (FBW-S).
  SAND    §5 after the first state t of S with r = -1, COARSE_{-1}(theta) is constant on the rest of S; every state of [g_1, g_N] has
          r = -1; every fallback of S inside [g_1, g_N] is a g_i; every g_i has M = -1.
  FANONE  §6 every in-scope fallback k with r_k = -1 and (h) at k+1: (i) F_k <= F_k+1, Rbar_k+1 <= Rbar_k with equal routes, every
          switched cycle node (lambda(y) = y) lies in F_k+1; (ii) COARSE_{-1}(theta); (iii) COARSE_{-1}(Xi v) for all v; (iv) M_k+1 <= -1.
  LVNONE  §7 per scope run, g_1 < ... < g_N: (1) COARSE_{-1}(Xi_t v) constant on [g_1, g_{N-1} + 1]; (2) each g_i (i < N) has a level
          -1 tail; at every level -1 tail event (y switched along a level -1 gate) at g_i, i < N: COARSE_{-1}(b_{k+1} y) =
          COARSE_{-1}(b_k y) and b_{k+1}(y) > b_k(y); per Even y at most n events; N <= n n_E + 1.
  LVPL    §4 per scope run, block f_1 < ... < f_N: f_{i+1} has a (beta) gate for i + 1 < N; (f_i, f_{i+1}) clean for i + 1 < N;
          COARSE_{-1}(Xi) constant on [f_1, f_{N-1} + 1]; tail events as in LVNONE; N <= n n_E + 1.
  ENTX1   §3 consecutive block fallbacks k0 < k with a window gate at k (y in R_k, z in F_k): (k0, k) is clean.
  SCOPEFB §8 per scope run: level >= 0 <= 2 n n_E; block <= n n_E + 1; none <= n n_E + 1; EQ <= 1; all <= 4 n n_E + 3.
Records (not checks): per-run maxima of each class, worst ratio to the bound (per mille); runs with N_none >= 2 (where LVNONE (1)-(2)
are not vacuous); at the LAST g_N / f_N: tail events whose b-move breaks the STRETCH step (COARSE change or no strict move), and runs
whose COARSE_{-1}(Xi) changes at g_N -> g_N + 1 (why e := g_{N-1} + 1 and not g_N + 1).
Usage: lv2_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for d in ("R2-N5-ENT", "R2-N5-OUT", "R2-N5-FRZ"): sys.path.insert(0, os.path.join(HERE, "..", d))
import ent_check as EC
OC, FC, RC = EC.OC, EC.FC, EC.RC
INF, BOT, lev, cl = FC.INF, FC.BOT, FC.lev, FC.coarse
M = EC.M
MUT = os.environ.get("LV2_MUT", "")   # mutation controls only: eN (constancy up to g_N + 1), lastN (tail check also at g_N),
# sand0 (SAND from the first THR state, any r), fa0 (FANONE also at fallbacks with r >= 0)

def play(f, x):
    seen, p = set(), []
    while x not in seen: seen.add(x); p.append(x); x = f[x]
    return p

def xi_const(g, A, a, b):
    """COARSE_{-1}(Xi_t v) equal for all t in [a, b] and all v"""
    return all(cl(g, A[t].Xi[v], -1) == cl(g, A[a].Xi[v], -1) for t in range(a + 1, b + 1) for v in range(g.n))

def changes(g, A, a, b):
    """transitions j in (a, b) (a < j < b) at which COARSE_{-1}(Xi) changes"""
    return [j for j in range(a + 1, b) if any(cl(g, A[j + 1].Xi[v], -1) != cl(g, A[j].Xi[v], -1) for v in range(g.n))]

def tails(g, A, k):
    S, B = A[k], A[k + 1]
    return [y for y in range(g.n) if g.owner[y] == 0 and B.sg[y] != S.sg[y] and S.gates.get((y, B.sg[y])) == -1]

def tail_moves(g, A, k, st, tag, name, record=False):
    bad = 0
    for y in tails(g, A, k):
        b0, b1 = A[k].Xi[A[k].sg[y]], A[k + 1].Xi[A[k + 1].sg[y]]
        if not (cl(g, b1, -1) == cl(g, b0, -1) and g.cmp(b1, b0) > 0):
            bad += 1
            if not record: st.bad(f"{name} {tag} STRETCH move at {k} y {y}")
    return bad

def stretch(g, A, ks, st, tag, name):
    n = g.n; cnt = {}
    for k in ks:
        ty = tails(g, A, k)
        if not ty: st.bad(f"{name} {tag} no level -1 tail at {k}")
        tail_moves(g, A, k, st, tag, name)
        for y in ty: cnt[y] = cnt.get(y, 0) + 1
    if cnt:
        st.mxu(f"max_{tag}_tail_events_per_y", max(cnt.values()))
        if max(cnt.values()) > n: st.bad(f"{name} {tag} {max(cnt.values())} tail events > n")

def check_run(g, o, A, fbs, st, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0); T = len(fbs)
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    st.c["runs"] += 1; st.c["states"] += len(A)
    # §1 STALE-GATE (whole run)
    for k0 in range(T):
        if not fbs[k0] or A[k0 + 1].sg == A[k0].sg: continue
        for k in range(k0 + 1, len(A)):
            for (y, z) in A[k].Is:
                st.c["STALE_checks"] += 1
                if A[k].Xi[z] == A[k0].Xi[z]: st.bad(f"{name} STALE k0 {k0} k {k} gate {y}->{z}")
    # §2 EV-G (same phase)
    for k0 in range(T):
        S0 = A[k0]
        if not (fbs[k0] and inph[k0] and S0.hh and g.cmp(S0.theta, S0.w) < 0): continue
        key = OC.key(S0, o); k = k0 + 1
        while k < len(A) and OC.key(A[k], o) == key:
            for (y, z) in A[k].Is:
                if z in A[k].F:
                    st.c["EVG_checks"] += 1
                    if set(play(A[k].f, z)) <= S0.F: st.bad(f"{name} EVG k0 {k0} k {k} z {z}")
            k += 1
    # scope runs
    k = 0
    while k < T:
        if not insc[k]: k += 1; continue
        j = k
        while j + 1 < T and insc[j + 1]: j += 1
        scope(g, o, A, fbs, k, j, n, nE, st, name); k = j + 1

def scope(g, o, A, fbs, s0, s1, n, nE, st, name):
    st.c["scope_runs"] += 1
    fl = [k for k in range(s0, s1 + 1) if fbs[k]]
    cls = {"ge0": [], "blk": [], "none": [], "eq": []}
    for k in fl:
        S = A[k]; Mk = M(S); thr = g.cmp(S.theta, S.w) < 0
        if Mk < -1: st.bad(f"{name} CLASS fallback without gate at {k}")
        if S.r == BOT:
            if thr: st.bad(f"{name} CLASS r = bot but THR at {k}")
            cls["eq"].append(k)
        elif S.r == -1: cls["none"].append(k)
        elif S.r >= 0 and S.r < INF: cls["ge0" if Mk >= 0 else "blk"].append(k)
        else: st.bad(f"{name} CLASS r = {S.r} at {k}")
        if S.r != BOT and Mk > S.r: st.bad(f"{name} CLASS FBW-S M {Mk} > r {S.r} at {k}")
    for c, L in cls.items():
        st.c[f"RECORD_fallbacks_{c}"] += len(L); st.mxu(f"max_per_run_{c}", len(L))
    tot = len(fl); st.mxu("max_per_run_all", tot)
    # §5 SAND
    sts = list(range(s0, s1 + 2))
    t0 = next((t for t in sts if (A[t].r == -1 if MUT != "sand0" else -1 <= A[t].r < INF)), None)
    if t0 is not None:
        st.c["RECORD_runs_with_r=-1"] += 1
        for t in sts:
            if t > t0:
                st.c["SAND_checks"] += 1
                if cl(g, A[t].theta, -1) != cl(g, A[t0].theta, -1): st.bad(f"{name} SAND {t0} -> {t}")
    gs = cls["none"]
    if gs:
        if any(A[t].r != -1 for t in range(gs[0], gs[-1] + 1)): st.bad(f"{name} SAND r != -1 inside [g_1, g_N]")
        if [k for k in fl if gs[0] <= k <= gs[-1]] != gs: st.bad(f"{name} SAND foreign fallback inside [g_1, g_N]")
        if any(M(A[k]) != -1 for k in gs): st.bad(f"{name} SAND g_i with M != -1")
    # §6 FLAT-ALL_{-1}^{none}
    for k in (gs if MUT != "fa0" else gs + cls["ge0"] + cls["blk"]):
        S, B = A[k], A[k + 1]
        if not B.hh: st.c["RECORD_FANONE_skipped_no_h_at_k+1"] += 1; continue
        st.c["FANONE_cases"] += 1
        if any(z in S.Rbar and z != o for (y, z) in S.Is if S.sg[y] in S.F): st.c["FANONE_cases_with_gamma"] += 1
        if not S.F <= B.F: st.bad(f"{name} FANONE(i) F at {k}")
        for v in B.Rbar:
            if v not in S.Rbar or B.pi[v] != S.pi[v]: st.bad(f"{name} FANONE(i) route {v} at {k}"); break
        for y in range(n):
            if g.owner[y] == 0 and B.sg[y] != S.sg[y] and S.lamX[y] == y and y not in B.F: st.bad(f"{name} FANONE(i) cycle node {y} not in F")
        if cl(g, B.theta, -1) != cl(g, S.theta, -1): st.bad(f"{name} FANONE(ii) at {k}")
        if any(cl(g, B.Xi[v], -1) != cl(g, S.Xi[v], -1) for v in range(n)): st.bad(f"{name} FANONE(iii) at {k}")
        if M(B) > -1: st.bad(f"{name} FANONE(iv) at {k}")
    # §7 LV-NONE
    N = len(gs)
    if N > n * nE + 1: st.bad(f"{name} LVNONE N {N} > n n_E + 1")
    if N:
        st.mxu("max_LVNONE_ratio_permille", (1000 * N) // (n * nE + 1))
    if N >= 2:
        st.c["LVNONE_runs_N>=2"] += 1; st.mxu("max_LVNONE_N", N)
        e = gs[-1] + 1 if MUT == "eN" else gs[-2] + 1
        if not xi_const(g, A, gs[0], e): st.bad(f"{name} LVNONE(1) COARSE changes on [g_1, g_N-1 + 1]")
        stretch(g, A, gs[:-1] + ([gs[-1]] if MUT == "lastN" else []), st, "LVNONE", name)
    if N >= 1:
        last = gs[-1]
        if last + 1 < len(A):
            if any(cl(g, A[last + 1].Xi[v], -1) != cl(g, A[last].Xi[v], -1) for v in range(n)): st.c["RECORD_none_COARSE_change_at_g_N"] += 1
            st.c["RECORD_none_last_tail_move_breaks"] += tail_moves(g, A, last, st, "LVNONE", name, record=True)
    # §4 LV-PL' and §3 ENT-X_{-1}
    fs = cls["blk"]; Nb = len(fs)
    if Nb > n * nE + 1: st.bad(f"{name} LVPL N {Nb} > n n_E + 1")
    if Nb >= 2:
        st.c["LVPL_runs_N>=2"] += 1
        for i in range(Nb - 1):
            a, b = fs[i], fs[i + 1]
            win = any(y in A[b].Rr and z in A[b].F for (y, z) in A[b].Is)
            if win:
                st.c["ENTX1_pairs"] += 1
                if changes(g, A, a, b): st.bad(f"{name} ENTX1 dirty ({a}, {b})")
            if i + 1 < Nb - 1:
                if not any(A[b].sg[y] in A[b].Rbar and z in A[b].F for (y, z) in A[b].Is): st.bad(f"{name} LVPL(i) no beta at {b}")
                if changes(g, A, a, b): st.bad(f"{name} LVPL(i) dirty ({a}, {b})")
        if not xi_const(g, A, fs[0], fs[-2] + 1): st.bad(f"{name} LVPL(ii) COARSE changes on [f_1, f_N-1 + 1]")
        stretch(g, A, fs[:-1], st, "LVPL", name)
    # §8 SCOPE-FB
    st.c["SCOPEFB_runs"] += 1
    if len(cls["ge0"]) > 2 * n * nE: st.bad(f"{name} SCOPEFB level >= 0 {len(cls['ge0'])}")
    if len(cls["eq"]) > 1: st.bad(f"{name} SCOPEFB EQ {len(cls['eq'])}")
    if tot > 4 * n * nE + 3: st.bad(f"{name} SCOPEFB {tot} > 4 n n_E + 3")
    if tot: st.mxu("max_SCOPEFB_ratio_permille", (1000 * tot) // (4 * n * nE + 3))

def main():
    args = sys.argv[1:]; st = FC.Stats()
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); mode = args[5] if len(args) > 5 else "own"; rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3; mode = args[3] if len(args) > 3 else "own"
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:{os.path.basename(path)}#{r}")
    FC.report(st)

if __name__ == "__main__":
    main()
