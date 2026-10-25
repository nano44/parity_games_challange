#!/usr/bin/env python3
"""REFEREE-2 successor 10 (Opus 5.5, D15): mechanical check of the companion packet P-N5-PFZ-ext (docs/new/P-N5-PFZ-ext-box39.md sha1
b3702b1b @ trunk c61ecc4). A copy of successor 9's pfz_check.py (P-N5-PFZ) with the theta-run replaced by the P-EPOCH (maximal run of one
phase with P(theta) constant; env PFZX_KEY=theta restores theta-runs) and with theta-LEN and BRK-POLY' per HN stretch:
  PFZ/LEN/NCA  P-FREEZE', LEN-TAIL', NO-CROSS-A' (the PFZ / LEN / NCA checks below, run on P-epochs, Mo := wt(P(theta)) of the epoch).
  TLEN    theta-LEN: theta-changes inside a P-epoch <= max(|U| - 2, 0); each is length-only.
  BRKX    BRK-POLY' per HN stretch, rho_S := transitions of S where P(theta) changes: (ii) B_S <= theta_S + (rho_S + 1)(|U| - 1 + |U|(|U| - 1));
          (iii) case A: B_S <= theta_S + (rho_S + 1)(|U| - 1); kind-2 early <= |U| - 1 per P-epoch; (i') theta_S <= rho_S + (rho_S + 1)
          max(|U| - 2, 0) (the proof's count, P-change transitions included).
  Records (statements as written, counted, not violations): (i) theta_S <= (rho_S + 1) max(|U| - 2, 0); (ii)'s middle bound
          (rho_S + 1)(|U|^2 + |U| - 3) and right bound (rho_S + 1)(2n^2 - 1); (iii)'s (rho_S + 1)(2n - 3).
Original docstring of pfz_check.py follows.
REFEREE-2 successor 9 (Opus 5.5, D15): mechanical check of packet P-N5-PFZ (docs/new/P-N5-PFZ-box39.md sha1 3c617e06 @ trunk 283bcb6).
Own code on R2-N5-OUT/out_check.py (traces own | rand | spec). No lane script is imported. Every game asserts exactly one Odd vertex with
out-degree > 1. U := lambda^{-1}(c_theta) per phase; M_t(z) := signed weight of P(Xi_t z); wt(v) := sgn(v) 2^rank(v) if rank v > rank
c_theta else 0. G_U: Even v in U \\ {c} keeps its edges into U, Odd v in U \\ {o, c} its forced edge, o and c sinks.
Checks (packet items):
  FACTS   (A) next_t(z) in U and M_t(z) = wt(z) + M_t(next z) for z in U \\ {c}; (M1') order => M order on U; (M2') M non-decreasing.
  FBR     FB-ROUND at every in-phase Even fallback: M_{k+1}(v) >= wt(v) + M_k(x) for Even v in U \\ {c}, successors x in U.
  PFZ     per theta-run (phase, theta constant): (b) M_t <= Mopt on U; (a) for every j and t > f_j: M_t(z) >= best simple path with <= j
          edges (exact DFS, |U| <= PFZN); (c) after f_{|U|-1}: M_t = Mopt and P constant on U.
  LEN     LEN-TAIL: after f_{|U|-1}, U-rises are length rises, and transitions carrying one <= |U|(|U|-1).
  NCA     NO-CROSS-A: case A, after f_{|U|-1}, H1 at t and t+1: Rbar unchanged; the identity Rbar = {z in U : o in P} at H1 states.
  RISE2   RISE': per break window [a, k] (a = last eviction before the entry k): theta change in [a+1, k], or an Rbar-rise at t -> t+1
          with theta constant on [a, t+1], a <= t < k.
  BRKP    BRK-POLY (i), (ii) per HN stretch, with the kind-1 / kind-2 (j < |U|, j >= |U|) charging.
Records: theta-runs that pass f_{|U|-1} with |U| >= 2 / >= 3 (the post-freeze regime), kind-2 breaks with j >= |U|.
Usage: pfz_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT"))
import out_check as OC
FC, RC = OC.FC, OC.RC
lev = FC.lev
PFZN = int(os.environ.get("PFZN", "12"))
KEYP = os.environ.get("PFZX_KEY", "P") == "P"
def same(x, y): return x[1] == y[1] if KEYP else x == y

def sgnw(g, v): return (1 if g.even[v] else -1) << g.rank[v]

def check_run(g, o, A, fbs, st, name):
    n = g.n; T = len(fbs)
    st.c["runs"] += 1; st.c["states"] += len(A)
    phases, a0 = [], 0
    for k in range(1, len(A) + 1):
        if k == len(A) or OC.key(A[k], o) != OC.key(A[k - 1], o): phases.append((a0, k - 1)); a0 = k
    for (p0, p1) in phases:
        c = A[p0].theta[0]; rc = g.rank[c]
        U = [v for v in range(n) if A[p0].lamX[v] == c]; Us = set(U)
        if o not in Us or c not in Us: st.bad(f"{name} o or c_theta not in U"); continue
        wt = {v: (sgnw(g, v) if g.rank[v] > rc else 0) for v in range(n)}
        def Mv(S, z): return sum(sgnw(g, u) for u in S.Xi[z][1])
        # facts
        for t in range(p0, p1 + 1):
            S = A[t]
            for z in U:
                if z == c: continue
                nx = S.fh[z]
                if nx not in Us or Mv(S, z) != wt[z] + Mv(S, nx): st.bad(f"{name} FACT (A) at {t}, z={z}")
            st.c["FACT_A_states"] += 1
            if t < p1:
                for z in U:
                    if Mv(A[t + 1], z) < Mv(S, z): st.bad(f"{name} FACT (M2') at {t}")
        # G_U
        succU = {}
        for v in U:
            if v in (o, c): succU[v] = []
            elif g.owner[v] == 0: succU[v] = [x for x in g.succ[v] if x in Us]
            else: succU[v] = [x for x in g.succ[v] if x in Us]
        # FB-ROUND
        for k in range(p0, p1):
            if not fbs[k] or A[k].tu != A[k + 1].tu: continue
            st.c["FBR_fallbacks"] += 1
            for v in U:
                if v == c or g.owner[v] != 0: continue
                for x in succU[v]:
                    st.c["FBR_checks"] += 1
                    if Mv(A[k + 1], v) < wt[v] + Mv(A[k], x): st.bad(f"{name} FBR v={v} x={x} at {k}")
        # theta-runs
        t = p0
        while t <= p1:
            e = t
            while e + 1 <= p1 and same(A[e + 1].theta, A[t].theta): e += 1
            theta_run(g, o, A, fbs, t, e, U, Us, succU, wt, Mv, st, name)
            t = e + 1
        # HN stretches: RISE', BRK-POLY
        SS = []; s = None
        for k in range(p0, p1 + 1):
            if A[k].HN and s is None: s = k
            if (not A[k].HN or k == p1) and s is not None: SS.append((s, k if A[k].HN else k - 1)); s = None
        caseA = g.rank[o] > rc
        for (s0, s1) in SS:
            brk(g, o, A, fbs, s0, s1, p0, p1, U, caseA, st, name)

def best_paths(z, j, succU, wt, Mo, o, c):
    """max over simple paths in G_U from z to a terminal with <= j edges of wt(p minus end) + M(end); None if none."""
    best = None
    def dfs(v, used, acc, edges):
        nonlocal best
        if v in (o, c):
            val = acc + Mo[v]
            if best is None or val > best: best = val
            return
        if edges == j: return
        for x in succU[v]:
            if x not in used:
                used.add(x); dfs(x, used, acc + wt[v], edges + 1); used.discard(x)
    dfs(z, {z}, 0, 0)
    return best

def theta_run(g, o, A, fbs, a, b, U, Us, succU, wt, Mv, st, name):
    c = A[a].theta[0]
    Mo = {o: sum(wt[u] for u in A[a].theta[1]), c: 0}
    if o == c: Mo = {o: 0}
    f = [k for k in range(a, b) if fbs[k] and A[k].tu == A[k + 1].tu]
    st.c["theta_runs"] += 1
    nU = len(U)
    tch = [t for t in range(a, b) if A[t].theta != A[t + 1].theta]
    st.c["TLEN_epochs"] += 1; st.c["TLEN_theta_changes"] += len(tch); st.mxu("max_TLEN_theta_changes_in_epoch", len(tch))
    if tch: st.c["TLEN_epochs_with_theta_change"] += 1
    if len(tch) > max(nU - 2, 0): st.bad(f"{name} TLEN {len(tch)} > max(|U| - 2, 0) = {max(nU - 2, 0)}")
    if any(A[t].theta[0] != A[t + 1].theta[0] or A[t].theta[1] != A[t + 1].theta[1] for t in tch): st.bad(f"{name} TLEN not length-only")
    small = nU <= PFZN
    if small:
        Mopt = {z: best_paths(z, nU, succU, wt, Mo, o, c) for z in U}
        for t in range(a, b + 1):
            for z in U:
                if Mopt[z] is None or Mv(A[t], z) > Mopt[z]: st.bad(f"{name} PFZ(b) z={z} at {t}")
        st.c["PFZ_b_runs"] += 1
        for j in range(1, min(len(f), nU - 1) + 1):
            bj = {z: best_paths(z, j, succU, wt, Mo, o, c) for z in U}
            for t in range(f[j - 1] + 1, b + 1):
                for z in U:
                    if bj[z] is not None and Mv(A[t], z) < bj[z]: st.bad(f"{name} PFZ(a) j={j} z={z} t={t}")
                    st.c["PFZ_a_checks"] += 1
    else:
        st.c["PFZ_skipped_large_U"] += 1
    if len(f) >= nU - 1 and nU >= 1:
        t0 = f[nU - 2] + 1 if nU >= 2 else a
        if t0 <= b:
            st.c[f"RECORD_post_freeze_runs_U{'=1' if nU == 1 else '=2' if nU == 2 else '>=3'}"] += 1
            st.c["post_freeze_transitions"] += b - t0
            P0 = {z: A[t0].Xi[z][1] for z in U}
            if small:
                for z in U:
                    if Mv(A[t0], z) != Mopt[z]: st.bad(f"{name} PFZ(c) M != Mopt at {t0}")
            rises = 0
            for t in range(t0, b + 1):
                for z in U:
                    if A[t].Xi[z][1] != P0[z]: st.bad(f"{name} PFZ(c) P changed z={z} t={t}")
                if t < b:
                    rz = [z for z in U if g.cmp(A[t].Xi[z], A[t + 1].Xi[z]) < 0]
                    if rz: rises += 1
                    for z in rz:
                        if A[t].Xi[z][1] != A[t + 1].Xi[z][1]: st.bad(f"{name} LEN rise not length-only")
                    if g.rank[o] > g.rank[c] and A[t].H1 and A[t + 1].H1:
                        st.c["NCA_cases"] += 1
                        if A[t].Rbar != A[t + 1].Rbar: st.bad(f"{name} NCA crossing after the freeze at {t}")
            st.mxu("max_post_freeze_U_rises", rises)
            if rises > nU * (nU - 1): st.bad(f"{name} LEN {rises} > |U|(|U|-1)")
    st.mxu("max_fallbacks_in_theta_run", len(f))
    if nU >= 3: st.mxu("max_fallbacks_minus_U_plus_1_U>=3", len(f) - (nU - 1))
    # identity Rbar = {z in U : o in P} at H1 states, case A
    if g.rank[o] > g.rank[c]:
        for t in range(a, b + 1):
            if A[t].H1:
                st.c["NCA_identity_states"] += 1
                if A[t].Rbar != {z for z in U if o in A[t].Xi[z][1]}: st.bad(f"{name} NCA identity at {t}")

def brk(g, o, A, fbs, s0, s1, p0, p1, U, caseA, st, name):
    nU = len(U); tr = range(s0, s1)
    ent = lambda k: A[k].Rr < A[k + 1].Rr
    evi = lambda k: A[k + 1].Rbar < A[k].Rbar
    th_S = sum(1 for k in tr if A[k].theta != A[k + 1].theta)
    rho = sum(1 for k in tr if A[k].theta[1] != A[k + 1].theta[1])
    st.c["BRKX_stretches"] += 1; st.c["BRKX_rho"] += rho; st.mxu("max_BRKX_rho_S", rho)
    if rho: st.c["BRKX_stretches_rho>=1"] += 1
    mU2 = max(nU - 2, 0)
    if th_S > rho + (rho + 1) * mU2: st.bad(f"{name} BRKX(i') theta_S {th_S} > rho + (rho + 1)(|U| - 2)")
    st.mxu("max_BRKX_(i)_excess_plus_1000", th_S - (rho + 1) * mU2 + 1000)
    if th_S > (rho + 1) * mU2:
        st.c["RECORD_BRKX_(i)_as_stated_fails"] += 1
        if "ex_i" not in st.ex: st.ex["ex_i"] = f"{name} stretch [{s0}, {s1}] theta_S {th_S} rho_S {rho} |U| {nU}"
    B = 0; prev_entry = s0 - 1; seen = False; last_evi = None
    k1 = 0; k2a = {}; k2b = 0
    for k in tr:
        if ent(k):
            if seen:
                B += 1; a = last_evi
                if not fbs[a]: st.bad(f"{name} BRKP eviction not a fallback")
                js = [j for j in range(a + 1, k + 1) if A[j].theta != A[j + 1].theta]
                th_const_from_a = lambda t: all(A[u].theta == A[a].theta for u in range(a, t + 2))   # kind 2 needs theta constant
                rs = [t for t in range(a, k) if th_const_from_a(t) and
                      any(z != o and g.cmp(A[t].Xi[z], A[t + 1].Xi[z]) < 0 for z in A[t].Rbar & A[t + 1].Rbar)]
                if js: k1 += 1
                elif rs:
                    # index j of a -> a+1 among the fallbacks of its theta-run
                    r0 = a
                    while r0 - 1 >= p0 and same(A[r0 - 1].theta, A[a].theta): r0 -= 1
                    j = sum(1 for u in range(r0, a + 1) if fbs[u] and A[u].tu == A[u + 1].tu)
                    if j <= nU - 1: k2a[r0] = k2a.get(r0, 0) + 1
                    else:
                        k2b += 1; st.c["RECORD_kind2_breaks_j>=|U|"] += 1
                        if caseA: st.bad(f"{name} BRKP(ii) case-A kind-2 break with j >= |U|")
                else: st.bad(f"{name} RISE2 break at {k} (window {a}) without theta change or rise")
            seen = False; prev_entry = k
        elif evi(k): seen = True; last_evi = k
    st.c["breaks"] += B; st.c["breaks_kind1"] += k1; st.c["breaks_kind2_early"] += sum(k2a.values()); st.c["breaks_kind2_late"] += k2b
    if any(v > nU - 1 for v in k2a.values()): st.bad(f"{name} BRKP early kind-2 > |U|-1 in one theta-run")
    if B > th_S + (rho + 1) * (nU - 1 + nU * (nU - 1)): st.bad(f"{name} BRKX(ii)")
    if caseA and B > th_S + (rho + 1) * (nU - 1): st.bad(f"{name} BRKX(iii)")
    if B > (rho + 1) * (nU * nU + nU - 3): st.c["RECORD_BRKX_(ii)_middle_fails"] += 1
    if B > (rho + 1) * (2 * g.n * g.n - 1): st.c["RECORD_BRKX_(ii)_right_fails"] += 1
    if caseA and B > (rho + 1) * (2 * g.n - 3): st.c["RECORD_BRKX_(iii)_right_fails"] += 1

def main():
    args = sys.argv[1:]; st = OC.Stats()
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
    for k, v in st.ex.items(): print("EXAMPLE", k, v)

if __name__ == "__main__":
    main()
