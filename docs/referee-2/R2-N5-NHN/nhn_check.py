#!/usr/bin/env python3
"""REFEREE-2 successor 11 (Opus 5.5, D15): mechanical check of packet P-N5-NHN (docs/new/P-N5-NHN-box40.md sha1 da7d09ec @ trunk 0bb175d).
Own code on R2-N5-OUT/out_check.py (traces own | rand | spec) and the phase / U / M conventions of R2-N5-RHO/rho_check.py. No lane script
(experiments/new/box40/nhn.py, nhnclimb.py, qsurvey.py) is run or imported. Every game asserts exactly one Odd vertex with out-degree > 1.
t0 := tau(o) (a phase constant). EV2 end: in-phase k -> k+1 with HN at k and H1 & H2 at k+1. DROP: in-phase H1 -> not H1.
T := |U|(n + 1) + n - 1 (R34 (e)). HN stretch: maximal run of HN states of one phase.
Checks (packet items):
  T0U     t0 != o: (a) every state: not H2 <=> t0 in R; (b) phase with an HN state: t0 in U \\ {o, c_theta} (so |U| >= 3).
  EV2     every EV2 end is an in-phase Even fallback with t0 in R_k \\ R_{k+1}.
  SGEV    every in-phase k -> k+1 with H1 at k, t0 in R_k, t0 not in R_{k+1}: Xi_k(t0) strictly below Xi_{k+1}(t0).
  PIN     EV2 end at g_j with j >= |U| - 1: M_k(t0) = M_{k+1}(t0) = Mopt_Uh(t0) (exact DFS, |U| <= NHNN).
  NHNB    (a) EV2 ends <= 2 max(|U| - 2, 0); (b) N_HN <= 1 + drops + EV2 ends, drops <= ceil(T/2), N_HN <= 1 + ceil(T/2) + 2 max(|U| - 2, 0).
  H3      t0 != o and an HN state: every H2 state has H3.
  TOO     tau(o) = o phases (RHO-N2 / N-NHN-1 citation): not H2 at every state, N_HN <= floor(T_ph/2) + 1 (T_ph := H1-toggles of the
          phase), case A and case B counted separately.
Records: EV2 ends (all / with j >= |U| - 1), SG-EV transitions that are not EV2 ends, max N_HN, phases by kind.
MUT (mutation controls only): pin1 (PIN at j >= |U| - 2), nhn (NHNB (b) without the 1 +).
Usage: nhn_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RHO"))
import out_check as OC
import rho_check as RH
FC, RC = OC.FC, OC.RC
NHNN = int(os.environ.get("NHNN", "12"))
MUT = os.environ.get("NHN_MUT", "")

def check_run(g, o, A, fbs, st, name):
    n = g.n; st.c["runs"] += 1
    phases, a0 = [], 0
    for k in range(1, len(A) + 1):
        if k == len(A) or OC.key(A[k], o) != OC.key(A[k - 1], o): phases.append((a0, k - 1)); a0 = k
    for (p0, p1) in phases:
        st.c["phases"] += 1
        c = A[p0].theta[0]; rc = g.rank[c]; t0 = A[p0].tu[o]
        U = [v for v in range(n) if A[p0].lamX[v] == c]; Us = set(U); Uh = Us - {o}; nU = len(U)
        T = nU * (n + 1) + n - 1
        wt = {v: (RH.sgnw(g, v) if g.rank[v] > rc else 0) for v in range(n)}
        M = lambda S, z: sum(RH.sgnw(g, u) for u in S.Xi[z][1])
        gs = [k for k in range(p0, p1) if fbs[k]]
        hn = [A[t].HN for t in range(p0, p1 + 1)]
        SS, s = [], None
        for t in range(p0, p1 + 1):
            if A[t].HN and s is None: s = t
            if s is not None and (t == p1 or not A[t + 1].HN): SS.append((s, t)); s = None
        NHN = len(SS)
        if t0 == o:
            st.c["phases_tau(o)=o"] += 1
            for t in range(p0, p1 + 1):
                if A[t].H2: st.bad(f"{name} TOO H2 at {t} with tau(o) = o")
            if NHN:
                Tph = sum(1 for t in range(p0, p1) if A[t].H1 != A[t + 1].H1)
                case = "A" if g.rank[o] > rc else "B"; st.c[f"TOO_phases_with_HN_case{case}"] += 1
                if NHN > Tph // 2 + 1: st.bad(f"{name} TOO N_HN {NHN} > floor(T_ph/2) + 1, case {case}")
            continue
        st.c["phases_tau(o)!=o"] += 1
        for t in range(p0, p1 + 1):
            st.c["T0U_a_states"] += 1
            if (not A[t].H2) != (t0 in A[t].R): st.bad(f"{name} T0U(a) at {t}")
        if not NHN: continue
        st.c["phases_tau(o)!=o_with_HN"] += 1
        if t0 not in Us or t0 in (o, c): st.bad(f"{name} T0U(b) t0 {t0}")
        for t in range(p0, p1 + 1):
            if A[t].H2:
                st.c["H3_states"] += 1
                if not A[t].H3: st.bad(f"{name} H3 at {t}")
        small = nU <= NHNN
        mopt = None
        if small and t0 in Uh and c != o:
            mopt = RH.upto(RH.best_by_edges(g, t0, Uh, c, wt), nU)
        ev2 = drops = 0
        for k in range(p0, p1):
            S, B = A[k], A[k + 1]
            if S.H1 and not B.H1: drops += 1
            if S.H1 and t0 in S.R and t0 not in B.R:
                st.c["SGEV_transitions"] += 1
                if g.cmp(S.Xi[t0], B.Xi[t0]) >= 0: st.bad(f"{name} SGEV at {k}")
                if not (S.HN and B.H1 and B.H2): st.c["RECORD_SGEV_not_EV2"] += 1
            if S.HN and B.H1 and B.H2:
                ev2 += 1; st.c["EV2_ends"] += 1
                if not fbs[k] or not (t0 in S.R and t0 not in B.R): st.bad(f"{name} EV2 at {k}")
                if fbs[k]:
                    j = gs.index(k) + 1
                    if j >= nU - (2 if MUT == "pin1" else 1):
                        st.c["RECORD_EV2_ends_j>=|U|-1"] += 1
                        if small:
                            st.c["PIN_checks"] += 1
                            if mopt is None or not (M(S, t0) == M(B, t0) == mopt): st.bad(f"{name} PIN at {k}")
        st.mxu("max_EV2_ends_per_phase", ev2); st.mxu("max_N_HN", NHN); st.c["N_HN_total"] += NHN; st.c["drops"] += drops
        if ev2 > 2 * max(nU - 2, 0): st.bad(f"{name} NHNB(a) {ev2}")
        if NHN > (0 if MUT == "nhn" else 1) + drops + ev2: st.bad(f"{name} NHNB(b) N_HN {NHN} > 1 + drops {drops} + ev2 {ev2}")
        if drops > -(-T // 2): st.bad(f"{name} NHNB drops {drops}")
        if NHN > 1 + -(-T // 2) + 2 * max(nU - 2, 0): st.bad(f"{name} NHNB(b) bound")

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
