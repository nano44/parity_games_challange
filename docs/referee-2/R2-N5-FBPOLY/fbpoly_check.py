#!/usr/bin/env python3
"""REFEREE-2 successor 11 (Opus 5.5, D15): mechanical check of packet P-N5-FBPOLY (docs/new/P-N5-FBPOLY-box41.md sha1 de244dcd @ trunk
42d8c3a9). Own code on R2-N5-OUT/out_check.py (traces own | rand | spec) and the phase / U conventions of R2-N5-RHO/rho_check.py. No lane
script (experiments/new/box41/fbpoly.py) is run or imported. Every game asserts exactly one Odd vertex with out-degree > 1.
kappa_t(z) := (M_t(z), s_theta * l(Xi_t z)), lexicographic; kwt(v) := (wt(v), s_theta); s_theta = +1 iff Omega(c_theta) odd.
U := lambda^{-1}(c_theta) per phase, Uh := U \\ {o}, T := {o, c_theta}, deg_U(o) := |succ(o) & U|; g_1 < g_2 < ... in-phase Even S4c
fallbacks; S_k := Even vertices switched at k -> k+1; S_U := S_k & (U \\ T); x*_v := sigma_{k+1}(v).
Checks (packet items):
  AK      (A-kappa) every state, z in U \\ {c}: fh(z) in U and kappa(z) = kwt(z) + kappa(fh z); (A0) kappa(c) = (0, 0).
  YB      not-H1 states: P(theta) empty and, o != c, 1 <= l(theta) <= |U| - 1.
  KY      kappa-Y-FORM at H1 states: sbar(o) in Y_t = succ(o) & U & F_t and kappa(o) = kwt(o) + min_Y kappa.
  KH      kappa-HAT-FREEZE (a) t > g_j: kappa_t(z) >= best kappa-path of G_Uh to c with <= j edges; (b) z in F_t & U: kappa <= kopt;
          (c) t > g_{|U|-2}, y in F_t & U: kappa = kopt (exact DFS for |U| <= FBN).
  KP      kappa-PFZ (o != c): t in theta-run Theta, t > f^Theta_j: kappa_t(z) >= best kappa-path of G_U^o to o with <= j edges + kappa_t(o).
  SW      switched set = gate sources (S4c), switched vertices Even.
  EXIT    EXIT-SWITCH: S_U != {} => some u in S_U whose k-honest play from x*_u meets T before u (kind ct / o; else kind loop);
          for each such u: p_u simple, in G_Uh (e = c) or G_U^o (e = o), kappa_k(x*_u) = kwt(p_u \\ {u, e}) + kappa_k(e).
  FX      FREEZE-EXIT per switched u of kind ct: j <= |U| - 2; of kind o: i <= |U| - 2 (i = index of k among its theta-run's fallbacks);
          so j >= |U| - 1 and i >= |U| - 1 => S_U = {} (o != c). For o = c (packet (c)): kind o only at i <= |U| - 1.
  CN      CN-ONLY: S_U = {} => every gate (y, z) has lambda(y) = y and lev = -1, and k + 1 is the phase's last state; <= 1 per phase.
  TA      THETA-AFTER (o != c, f >= |U| - 2): theta-changes at t -> t+1 with t > g_{|U|-2} <= deg_U(o) + |U| - 2.
  FB      FB-POLY (a) o != c: f <= 1 + (|U| - 2)(deg_U(o) + |U|); (b) |U| = 2: f <= 1; (c) o = c: f <= |U|; (d) as CN.
Records: fallbacks g_j with j >= |U| - 1 at |U| >= 3 (FREEZE-EXIT / THETA-AFTER hypotheses), FB-CAP excess f - max(1, |U| - 2), phases
  with o = c and |U| = 2 and their f, maxima.
MUT (mutation controls only): fx (FX with |U| - 3 for |U| - 2), ta (TA bound - 1), fb (FB (a) with deg_U + |U| - 1 for deg_U + |U|).
Usage: fbpoly_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT"))
import out_check as OC
FC, RC = OC.FC, OC.RC
lev = FC.lev
FBN = int(os.environ.get("FBN", "12"))
MUT = os.environ.get("FBP_MUT", "")

def sgnw(g, v): return (1 if g.even[v] else -1) << g.rank[v]
def add(a, b): return (a[0] + b[0], a[1] + b[1])

def best_kpaths(g, z, Vs, sink, kw, skip_odd):
    """b[e] = max kwt(p \\ {sink}) over simple paths p from z to sink with exactly e edges, in the graph on Vs where Even v keeps its
    edges into Vs, Odd v (not in skip_odd) its forced edge if it lies in Vs, and sink is a sink. None if no such path."""
    b = [None] * (len(Vs) + 1)
    def dfs(v, used, acc, e):
        if v == sink:
            if b[e] is None or acc > b[e]: b[e] = acc
            return
        if g.owner[v] == 0: nxt = [x for x in set(g.succ[v]) if x in Vs]
        elif v in skip_odd: nxt = []
        else: nxt = [g.succ[v][0]] if g.succ[v][0] in Vs else []
        for x in nxt:
            if x not in used: used.add(x); dfs(x, used, add(acc, kw[v]), e + 1); used.discard(x)
    dfs(z, {z}, (0, 0), 0)
    return b

def upto(b, j):
    v = [x for x in b[:j + 1] if x is not None]
    return max(v) if v else None

def check_run(g, o, A, fbs, st, name):
    n = g.n; st.c["runs"] += 1; st.c["states"] += len(A)
    phases, a0 = [], 0
    for k in range(1, len(A) + 1):
        if k == len(A) or OC.key(A[k], o) != OC.key(A[k - 1], o): phases.append((a0, k - 1)); a0 = k
    for (p0, p1) in phases:
        st.c["phases"] += 1
        c = A[p0].theta[0]; rc = g.rank[c]
        U = [v for v in range(n) if A[p0].lamX[v] == c]; Us = set(U); Uh = Us - {o}; nU = len(U); T = {o, c}
        degU = len(set(g.succ[o]) & Us)
        sth = -1 if g.even[c] else 1
        wt = {v: (sgnw(g, v) if g.rank[v] > rc else 0) for v in range(n)}
        kw = {v: (wt[v], sth) for v in range(n)}
        def kap(S, z): x = S.Xi[z]; return (sum(sgnw(g, u) for u in x[1]), sth * x[2])
        gs = [k for k in range(p0, p1) if fbs[k]]
        f = len(gs); st.c["fallbacks"] += f
        small = nU <= FBN
        if not small: st.c["RECORD_phases_skipped_large_U"] += 1
        # theta-runs of the phase: run index of each state, and the index i of each fallback inside its run
        run_of, r = [], 0
        for t in range(p0, p1 + 1):
            if t > p0 and A[t].theta != A[t - 1].theta: r += 1
            run_of.append(r)
        idx_in_run, cnt = {}, {}
        for k in gs:
            rr = run_of[k - p0]; cnt[rr] = cnt.get(rr, 0) + 1; idx_in_run[k] = cnt[rr]
        # (A-kappa), (A0), (YB), kappa-Y-FORM
        for t in range(p0, p1 + 1):
            S = A[t]
            if kap(S, c) != (0, 0): st.bad(f"{name} A0 kappa(c) at {t}")
            for z in Us - {c}:
                st.c["AK_checks"] += 1
                if S.fh[z] not in Us or kap(S, z) != add(kw[z], kap(S, S.fh[z])): st.bad(f"{name} AK z {z} at {t}")
            if not S.H1:
                st.c["YB_states"] += 1
                if S.theta[1] or (o != c and not 1 <= S.theta[2] <= nU - 1): st.bad(f"{name} YB at {t}")
            else:
                Y = [y for y in set(g.succ[o]) if y in Us and y in S.F]; st.c["KY_states"] += 1
                if S.sbar not in Y or kap(S, o) != add(kw[o], min(kap(S, y) for y in Y)): st.bad(f"{name} KY at {t}")
        # exact optima
        if small:
            BH = {z: best_kpaths(g, z, Uh, c, kw, {o}) for z in Uh} if c != o else {}
            kopt = {z: upto(b, nU) for z, b in BH.items()}
            Vo = Us - {c}
            BO = {z: best_kpaths(g, z, Vo, o, kw, set()) for z in Vo} if c != o else {}
        # kappa-HAT-FREEZE
        if small and c != o:
            for t in range(p0, p1 + 1):
                for z in (Us & A[t].F) - {c}:
                    st.c["KH_b"] += 1
                    if kopt.get(z) is None or kap(A[t], z) > kopt[z]: st.bad(f"{name} KH(b) z {z} t {t}")
            for j in range(1, min(nU - 2, f) + 1):
                for t in range(gs[j - 1] + 1, p1 + 1):
                    for z in Uh - {c}:
                        bj = upto(BH[z], j)
                        if bj is not None:
                            st.c["KH_a"] += 1
                            if kap(A[t], z) < bj: st.bad(f"{name} KH(a) j {j} z {z} t {t}")
            if nU >= 2 and f >= nU - 2:
                frz = gs[nU - 3] + 1 if nU >= 3 else p0
                for t in range(frz, p1 + 1):
                    for y in (Us & A[t].F) - {c}:
                        st.c["KH_c"] += 1
                        if kap(A[t], y) != kopt[y]: st.bad(f"{name} KH(c) y {y} t {t}")
        # kappa-PFZ
        if small and c != o:
            for t in range(p0, p1 + 1):
                rr = run_of[t - p0]
                fr = [k for k in gs if run_of[k - p0] == rr and k < t]       # f^Theta_1 < ... < t, all in Theta
                for j in range(0, min(len(fr), nU - 2) + 1):
                    for z in Us - {c}:
                        bj = upto(BO[z], j)
                        if bj is not None:
                            st.c["KP_checks"] += 1
                            if kap(A[t], z) < add(bj, kap(A[t], o)): st.bad(f"{name} KP j {j} z {z} t {t}")
        # fallbacks: SW, EXIT, FX, CN
        ncn = 0
        for jj, k in enumerate(gs, 1):
            S, B = A[k], A[k + 1]
            Sk = {v for v in range(n) if B.sg[v] != S.sg[v]}
            src = {y for y, _ in S.Is}
            st.c["SW_fallbacks"] += 1
            if Sk != src or any(g.owner[v] != 0 for v in Sk): st.bad(f"{name} SW at {k}")
            if B.tu != S.tu: st.bad(f"{name} in-phase fallback changes tau at {k}")
            SU = Sk & (Us - T); i = idx_in_run[k]
            if nU >= 3 and jj >= nU - 1: st.c["RECORD_fallbacks_j>=|U|-1_U>=3"] += 1
            if nU >= 3 and jj >= nU - 1 and i >= nU - 1: st.c["RECORD_fallbacks_j,i>=|U|-1_U>=3"] += 1
            if not SU:
                ncn += 1; st.c["CN_fallbacks"] += 1
                for (y, z) in S.Is:
                    if S.lamX[y] != y or lev(g, S.Xi[S.sg[y]], S.Xi[z]) != -1: st.bad(f"{name} CN gate ({y}, {z}) at {k}")
                if k + 1 != p1: st.bad(f"{name} CN k + 1 not the phase's last state at {k}")
                continue
            st.c["EXIT_fallbacks"] += 1
            good = 0
            for u in SU:
                x = B.sg[u]; play, v = [], x
                while v not in T and v != u and v not in play: play.append(v); v = S.fh[v]
                if v == u or (v not in T):
                    st.c["EXIT_kind_loop"] += 1; continue
                e = v; good += 1; st.c[f"EXIT_kind_{'o' if e == o else 'ct'}"] += 1
                pu = [u] + play + [e]
                if len(set(pu)) != len(pu): st.bad(f"{name} EXIT p_u not simple at {k}")
                Vs = Us if c == o else (Uh if e == c else Us - {c})      # o = c_theta: G_U (packet (c)); fixed by succ. 11 after climb 4101
                if any(w not in Vs for w in pu): st.bad(f"{name} EXIT p_u leaves its graph at {k}")
                acc = (0, 0)
                for w in play: acc = add(acc, kw[w])
                if kap(S, x) != add(acc, kap(S, e)): st.bad(f"{name} EXIT kappa identity at {k}")
                lim = nU - (3 if MUT == "fx" else 2)
                st.mxu("max_FX_ct_j_minus_lim_plus_1000" if e == c else "max_FX_o_i_minus_lim_plus_1000", (jj if e == c else i) - (nU - 2) + 1000)
                if c != o:
                    if e == c and jj > lim: st.bad(f"{name} FX kind ct at j {jj} > |U| - 2 (|U| {nU}) at {k}")
                    if e == o and i > lim: st.bad(f"{name} FX kind o at i {i} > |U| - 2 (|U| {nU}) at {k}")
                elif i > nU - 1: st.bad(f"{name} FX(c) kind o at i {i} > |U| - 1 at {k}")
            if not good: st.bad(f"{name} EXIT no switched u of kind ct / o at {k}")
        if ncn > 1: st.bad(f"{name} CN {ncn} > 1 in a phase")
        # THETA-AFTER
        if c != o and f >= nU - 2 and nU >= 2:
            frz = gs[nU - 3] + 1 if nU >= 3 else p0
            ch = sum(1 for t in range(frz, p1) if A[t].theta != A[t + 1].theta)
            st.c["TA_phases"] += 1; st.mxu("max_TA_changes", ch)
            if nU >= 3: st.c["RECORD_TA_phases_U>=3"] += 1; st.mxu("max_TA_changes_U>=3", ch)
            if ch > degU + nU - 2 - (1 if MUT == "ta" else 0): st.bad(f"{name} TA {ch} > deg_U(o) + |U| - 2 = {degU + nU - 2}")
        # FB-POLY
        st.mxu("max_f_per_phase", f); st.mxu("max_FBCAP_excess_plus_1000", f - max(1, nU - 2) + 1000)
        if f > max(1, nU - 2): st.c["RECORD_FBCAP_fails"] += 1
        if nU >= 3: st.mxu("max_f_minus_U_plus_2_U>=3_plus_1000", f - (nU - 2) + 1000)
        if c != o:
            bd = 1 + (nU - 2) * (degU + nU - (1 if MUT == "fb" else 0))
            st.mxu("max_FB_a_slack_minus_1000", f - bd + 1000)
            if f > bd: st.bad(f"{name} FB(a) f {f} > {bd}")
        else:
            st.c["phases_o=c"] += 1
            if nU == 2: st.c["RECORD_phases_o=c_U=2"] += 1; st.mxu("max_f_o=c_U=2", f)
            if f > nU: st.bad(f"{name} FB(c) f {f} > |U| {nU}")
        if nU == 2 and f > 1: st.bad(f"{name} FB(b) f {f} > 1")

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

if __name__ == "__main__":
    main()
