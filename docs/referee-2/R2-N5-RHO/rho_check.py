#!/usr/bin/env python3
"""REFEREE-2 successor 10 (Opus 5.5, D15): mechanical check of packet P-N5-RHO (docs/new/P-N5-RHO-box40.md sha1 cd5df65c @ trunk c814455).
Own code on R2-N5-OUT/out_check.py (traces own | rand | spec) and the phase / U / M conventions of R2-N5-PFZ/pfz_check.py. No lane script
(rhodata.py, rhoclimb.py, box39/rho.py) is run or imported. Every game asserts exactly one Odd vertex with out-degree > 1.
U := lambda^{-1}(c_theta) per phase, Uh := U \\ {o}; M_t(z) := signed weight of P(Xi_t z); g_1 < g_2 < ... the in-phase S4c fallback
transitions of the phase. Exact simple-path optima by DFS when |U| <= RHON (default 12; larger phases skip those checks, counted).
Checks (packet items):
  YFORM   §1 every state: H1 => sbar(o) in Y_t = succ(o) & U & F_t and M(o) = wt(o) + min_Y M; not H1 => P(theta) empty.
  HAT     §2 (a) t > g_j: M_t(z) >= best path of G_Uh with <= j edges (z in Uh); (b) z in F_t & U: Mopt_Uh(z) defined, M_t(z) <= it;
          (c) |U| >= 2, t > g_{|U|-2}, y in F_t & U: M_t(y) = Mopt_Uh(y).
  TAIL    §3 transitions t -> t+1 with t > g_{|U|-2} changing P(theta) <= deg(o).
  BFF     §4 S4a k -> k+1 with HN at k and k+1, Even v in U & F_{k+1}, v != c, x in succ(v) & U: M_{k+1}(v) >= wt(v) + M_k(x).
  FRZF    §5 per maximal fallback-free run [s, e] of HN states: (a) M_t(z) >= best path of G[F_t & U] with <= t - s edges; (b) M constant
          on F_{t'} & U for t, t' in [s + |U| - 2, e]; (c) P(theta)-changes in the run <= max(|U| - 2, 0) + deg(o) - 1.
  RHOHN   §6 per phase (|U| >= 2): rho_HN <= (N_HN + |U| - 2)(|U| + deg(o) - 3) + deg(o).
  HNPOLY  §6 per phase: sum_S theta_S <= rho_HN + (rho_HN + N_HN) max(|U| - 2, 0); sum_S B_S <= (rho_HN + N_HN)(2 n^2 - 1).
Records: phases past g_{|U|-2} with |U| >= 3 and an H1 state after it (HAT (c) / TAIL non-trivial); FRZF (b) states; maxima.
Usage: rho_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT"))
import out_check as OC
FC, RC = OC.FC, OC.RC
RHON = int(os.environ.get("RHON", "12"))
MUT = os.environ.get("RHO_MUT", "")   # mutation controls only: hatall (HAT (c) at every state of the phase), frzb0 (FRZF (b) from s)

def sgnw(g, v): return (1 if g.even[v] else -1) << g.rank[v]

def best_by_edges(g, z, A, c, wt):
    """b[e] = max wt(p \\ {c}) over simple paths p from z to c with exactly e edges in G[A] (Even: edges into A; Odd: forced edge if in A;
    c a sink); None if none."""
    n = len(A); b = [None] * (n + 1)
    def dfs(v, used, acc, e):
        if v == c:
            if b[e] is None or acc > b[e]: b[e] = acc
            return
        nxt = [x for x in set(g.succ[v]) if x in A] if g.owner[v] == 0 else ([g.succ[v][0]] if g.succ[v][0] in A else [])
        for x in nxt:
            if x not in used: used.add(x); dfs(x, used, acc + wt[v], e + 1); used.discard(x)
    dfs(z, {z}, 0, 0)
    return b

def upto(b, j):
    v = [x for x in b[:j + 1] if x is not None]
    return max(v) if v else None

def check_run(g, o, A, fbs, st, name):
    n = g.n; st.c["runs"] += 1; st.c["states"] += len(A); dego = len(set(g.succ[o]))
    phases, a0 = [], 0
    for k in range(1, len(A) + 1):
        if k == len(A) or OC.key(A[k], o) != OC.key(A[k - 1], o): phases.append((a0, k - 1)); a0 = k
    for (p0, p1) in phases:
        st.c["phases"] += 1
        c = A[p0].theta[0]; rc = g.rank[c]
        U = [v for v in range(n) if A[p0].lamX[v] == c]; Us = set(U); Uh = Us - {o}; nU = len(U)
        wt = {v: (sgnw(g, v) if g.rank[v] > rc else 0) for v in range(n)}
        M = lambda S, z: sum(sgnw(g, u) for u in S.Xi[z][1])
        gs = [k for k in range(p0, p1) if fbs[k]]
        small = nU <= RHON
        if not small: st.c["RECORD_phases_skipped_large_U"] += 1
        BB = {z: best_by_edges(g, z, Uh, c, wt) for z in Uh} if small and c != o else {}
        Mopt = {z: upto(b, nU) for z, b in BB.items()}
        Pch = lambda t: A[t].theta[1] != A[t + 1].theta[1]
        # §1 Y-FORM
        for t in range(p0, p1 + 1):
            S = A[t]
            if S.H1:
                Y = [y for y in set(g.succ[o]) if y in Us and y in S.F]; st.c["YFORM_a"] += 1
                if S.sbar not in Y or M(S, o) != wt[o] + min(M(S, y) for y in Y): st.bad(f"{name} YFORM(a) at {t}")
            else:
                st.c["YFORM_b"] += 1
                if S.theta[1]: st.bad(f"{name} YFORM(b) at {t}")
        # §2 HAT-FREEZE
        if c != o and small:
            for t in range(p0, p1 + 1):
                S = A[t]
                for z in Us & S.F:
                    st.c["HAT_b"] += 1
                    if z == c: continue
                    if Mopt.get(z) is None or M(S, z) > Mopt[z]: st.bad(f"{name} HAT(b) z {z} at {t}")
            for j in range(1, min(nU - 2, len(gs)) + 1):
                for t in range(gs[j - 1] + 1, p1 + 1):
                    for z in Uh - {c}:
                        bj = upto(BB[z], j)
                        if bj is not None:
                            st.c["HAT_a"] += 1
                            if M(A[t], z) < bj: st.bad(f"{name} HAT(a) j {j} z {z} t {t}")
        frz = None
        if nU >= 2 and (len(gs) >= nU - 2 or MUT == "hatall"):
            frz = gs[nU - 3] + 1 if nU >= 3 and MUT != "hatall" else p0          # first state t > g_{|U|-2}
            if nU >= 3 and any(A[t].H1 for t in range(frz, p1 + 1)): st.c["RECORD_phases_past_hat_freeze_U>=3_with_H1"] += 1; st.mxu("max_U_past_hat_freeze", nU)
            if small and c != o:
                for t in range(frz, p1 + 1):
                    for y in Us & A[t].F:
                        if y == c: continue
                        st.c["HAT_c"] += 1
                        if M(A[t], y) != Mopt[y]: st.bad(f"{name} HAT(c) y {y} t {t}")
            ch = sum(1 for t in range(frz, p1) if Pch(t))
            st.c["TAIL_phases"] += 1; st.mxu("max_TAIL_changes", ch)
            if ch > dego and MUT != "hatall": st.bad(f"{name} TAIL {ch} > deg(o) {dego}")
        # §4 BF-F
        for k in range(p0, p1):
            if fbs[k] or not (A[k].HN and A[k + 1].HN): continue
            S, B = A[k], A[k + 1]
            for v in Us & B.F:
                if v == c or g.owner[v] != 0: continue
                for x in set(g.succ[v]):
                    if x not in Us: continue
                    st.c["BFF_checks"] += 1
                    if M(S, x) > M(S, S.sg[v]): st.c["BFF_case2"] += 1
                    if M(B, v) < wt[v] + M(S, x): st.bad(f"{name} BFF v {v} x {x} at {k}")
        # §5 FREEZE-F and HN stretches
        runs, s = [], None
        for t in range(p0, p1 + 1):
            if A[t].HN and s is None: s = t
            if s is not None and (t == p1 or not A[t + 1].HN or fbs[t]): runs.append((s, t)); s = None
        for (s, e) in runs:
            st.c["FRZF_runs"] += 1
            ch = sum(1 for t in range(s, e) if Pch(t)); st.mxu("max_FRZF_changes", ch)
            if ch > max(nU - 2, 0) + dego - 1: st.bad(f"{name} FRZF(c) {ch} at run [{s}, {e}]")
            for t in range(s, e + 1):
                Ft = Us & A[t].F
                if small:
                    for z in Ft - {c}:
                        bj = upto(best_by_edges(g, z, Ft, c, wt), t - s)
                        if bj is not None:
                            st.c["FRZF_a"] += 1
                            if M(A[t], z) < bj: st.bad(f"{name} FRZF(a) z {z} t {t}")
                if t >= s + (nU - 2 if MUT != "frzb0" else 0) and t < e:
                    st.c["FRZF_b_states"] += 1
                    if any(M(A[t + 1], z) != M(A[t], z) for z in Us & A[t + 1].F): st.bad(f"{name} FRZF(b) at {t}")
        SS, s = [], None
        for t in range(p0, p1 + 1):
            if A[t].HN and s is None: s = t
            if s is not None and (t == p1 or not A[t + 1].HN): SS.append((s, t)); s = None
        NHN = len(SS)
        if not NHN: continue
        st.c["phases_with_HN"] += 1
        rho = sum(1 for (s, e) in SS for t in range(s, e) if Pch(t)); st.mxu("max_rho_HN", rho); st.c["rho_HN_total"] += rho
        if nU >= 2 and rho > (NHN + nU - 2) * (nU + dego - 3) + dego: st.bad(f"{name} RHOHN {rho}")
        th = sum(1 for (s, e) in SS for t in range(s, e) if A[t].theta != A[t + 1].theta)
        Bs = 0
        for (s, e) in SS:
            seen = False
            for k in range(s, e):
                if A[k].Rr < A[k + 1].Rr:
                    if seen: Bs += 1
                    seen = False
                elif A[k + 1].Rbar < A[k].Rbar: seen = True
        st.mxu("max_sum_B_S", Bs); st.mxu("max_sum_theta_S", th)
        if th > rho + (rho + NHN) * max(nU - 2, 0): st.bad(f"{name} HNPOLY theta {th}")
        if Bs > (rho + NHN) * (2 * n * n - 1): st.bad(f"{name} HNPOLY B {Bs}")

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
