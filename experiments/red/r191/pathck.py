#!/usr/bin/env python3
"""L-RED R191 PATHCK: checks, on the IDEAL run (r187/ideal.traj) of IDEAL-ACYC genomes, (MONO) every face value is non-decreasing
step by step; (V) V(x) := #distinct values of x's current face over the run satisfies V(x) <= sum_k V(xt(x,k)) (V(X) = 1);
(P) moves(x) <= V(x) - 1 <= P(x) - 1, P(x) := number of Xi-paths x -> X counted over options. Prints per genome
L, sum moves, sum (P-1), max moves/(P-1), violations. Usage: pathck.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal, fastcyc
from functools import lru_cache
def check(G):
    S, why = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; bad = []
    seen = [set() for _ in range(N)]; prev = None; mv = [0] * N
    for t, s in enumerate(S):
        val, idx, _, M = fastcyc.values(G, list(s))
        F = {(v, k): val(N + idx[(v, k)]) for v in range(N) for k in range(len(O[v]))}
        if prev is not None:
            for f in F:
                if F[f] < prev[f]: bad.append(("MONO", t, f))
            for v in range(N):
                if s[v] != S[t - 1][v]: mv[v] += 1
        for v in range(N): seen[v].add(F[(v, s[v])])
        prev = F
    V = [len(x) for x in seen]
    @lru_cache(None)
    def P(v): return sum(1 if xt < 0 else P(xt) for (_, xt, _) in O[v])
    for v in range(N):
        if V[v] > sum(1 if xt < 0 else V[xt] for (_, xt, _) in O[v]): bad.append(("V", v))
        if mv[v] > V[v] - 1 or V[v] > P(v): bad.append(("P", v, mv[v], V[v], P(v)))
    return len(S) - 1, why, mv, V, [P(v) for v in range(N)], bad
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); L, why, mv, V, Pv, bad = check(G)
        r = max((mv[v] / (Pv[v] - 1) for v in range(G["N"]) if Pv[v] > 1), default=0)
        print(f"{os.path.basename(f)}: L {L} {why} moves {sum(mv)} sumV-1 {sum(V) - len(V)} sumP-1 {sum(Pv) - len(Pv)} maxP {max(Pv)} max moves/(P-1) {r:.2f} violations {len(bad)} {bad[:3]}")
