#!/usr/bin/env python3
"""REFEREE-2 successor 11 (Opus 5.5, D15): mechanical check of packet P-N5-PHI (docs/si/P-N5-PHI-box14.md sha1 35e79ec1 @ trunk af3a3b5a).
Own code on R2-N5-OUT/out_check.py (traces own | rand | spec), C^1O only (the tracer's Odd side has one choice vertex); no lane script
(experiments/si/phi14/phicheck.py) is run or imported. reward(c) = p'(c) if Omega(c) even, -p'(c) if odd, p' = 2 rank + parity.
Checks: PHIA reward(lambda_{k+1}(v)) >= reward(lambda_k(v)) at every transition, equal iff lambda equal; PHIB reward(lambda^U_{k+1}(v)) <=
reward(lambda^U_k(v)) (lambda^U from Odd's valuation U_tau, Even's best response read in G's order), equal iff equal; PHIC per vertex
lambda changes <= n - 1 and lambda^U changes <= n - 1; transitions changing lambda <= n(n-1), lambda^U <= n(n-1); joint lambda-runs
<= 2n(n-1) + 1; PHI1O (a) tau changes <= d - 1 and no tau repeats; (b) phases <= n(n-1) + d. Maxima are recorded as ratios (per mille).
Usage: phi_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT"))
import out_check as OC
FC, RC = OC.FC, OC.RC
MUT = os.environ.get("PHI_MUT", "")   # mutation control only: ub (PHIB with the direction flipped: lambda^U reward non-decreasing)

def reward(g, c):
    p = 2 * g.rank[c] + (0 if g.even[c] else 1)
    return p if g.even[c] else -p

def check_run(g, o, A, fbs, st, name):
    n = g.n; d = len(set(g.succ[o])); st.c["runs"] += 1; st.c["transitions"] += len(A) - 1
    chl = [0] * n; chu = [0] * n; tl = tu_ = joint = 0; taus = [A[0].tu[o]]; tch = 0; phases = 1
    for k in range(len(A) - 1):
        S, B = A[k], A[k + 1]
        for v in range(n):
            a, b = reward(g, S.lamX[v]), reward(g, B.lamX[v]); st.c["PHIA_checks"] += 1
            if b < a or (a == b) != (S.lamX[v] == B.lamX[v]): st.bad(f"{name} PHIA v {v} at {k}")
            a, b = reward(g, S.lamU[v]), reward(g, B.lamU[v]); st.c["PHIB_checks"] += 1
            if (b < a if MUT == "ub" else b > a) or (a == b) != (S.lamU[v] == B.lamU[v]): st.bad(f"{name} PHIB v {v} at {k}")
            chl[v] += S.lamX[v] != B.lamX[v]; chu[v] += S.lamU[v] != B.lamU[v]
        L = S.lamX != B.lamX; Uc = S.lamU != B.lamU; T = S.tu[o] != B.tu[o]
        tl += L; tu_ += Uc; joint += (L or Uc); phases += (L or T)
        if T:
            tch += 1
            if B.tu[o] in taus: st.bad(f"{name} PHI1O tau repeats at {k}")
            taus.append(B.tu[o])
    if max(chl) > n - 1 or max(chu) > n - 1: st.bad(f"{name} PHIC per-vertex changes")
    if tl > n * (n - 1) or tu_ > n * (n - 1) or joint + 1 > 2 * n * (n - 1) + 1: st.bad(f"{name} PHIC counts")
    if tch > d - 1: st.bad(f"{name} PHI1O(a) tau changes {tch} > d - 1")
    if phases > n * (n - 1) + d: st.bad(f"{name} PHI1O(b) phases {phases}")
    st.c["lambda_changes"] += tl; st.c["lambdaU_changes"] += tu_; st.c["tau_changes"] += tch; st.c["phases"] += phases
    st.mxu("max_lambda_changes_per_vertex", max(chl)); st.mxu("max_lambdaU_changes_per_vertex", max(chu))
    st.mxu("max_tau_changes", tch); st.mxu("max_phases", phases)
    if n > 1:
        st.mxu("max_permille_vertex_changes_of_n-1", 1000 * max(max(chl), max(chu)) // (n - 1))
        st.mxu("max_permille_joint_runs_of_bound", 1000 * (joint + 1) // (2 * n * (n - 1) + 1))
        st.mxu("max_permille_phases_of_bound", 1000 * phases // (n * (n - 1) + d))
    if d > 1: st.mxu("max_permille_tau_changes_of_d-1", 1000 * tch // (d - 1))

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
