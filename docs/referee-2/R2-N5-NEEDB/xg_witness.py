#!/usr/bin/env python3
"""REFEREE-2 succ. 12: rng-free check of the XG witness (N-NEEDB-4). Usage: xg_witness.py climb/witness_xg_12004.pg climb/witness_xg_12004.json
The json holds the start pair, the trace (own: deterministic), the state k, an optimal G_tau strategy sigma* (full successor map, Odd
entries = tau) and the edge (y, z = sigma*(y)). Checks XG's setting and hypothesis at k, then its conclusions (i), (ii) and the gate level."""
import sys, json, random, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import needb_check as EC
OC, FC, RC = EC.OC, EC.FC, EC.RC
g = RC.parse(open(sys.argv[1]).read()); o = FC.odd_vertex(g); d = json.load(open(sys.argv[2]))
s, t, k, fo, y, z = d["sigma0"], d["tau0"], d["state"], d["sigma_star"], d["y"], d["z"]
assert all(s[v] in g.succ[v] and t[v] in g.succ[v] for v in range(g.n)), "start pair is not a strategy pair of this game"
A, fbs = OC.run_trace(g, o, s, t, random.Random(0), d["trace"])
S = A[k]
ok = {}
ok["in-phase S4c fallback"] = fbs[k] == 1 and OC.key(S, o) == OC.key(A[k + 1], o)
ok["(h) and THR"] = S.hh and g.cmp(S.theta, S.w) < 0
ok["sigma* is a G_tau strategy"] = all((fo[v] in g.succ[v]) if g.owner[v] == 0 else (fo[v] == S.f[v]) for v in range(g.n))
ok["sigma* is optimal (valuation = U)"] = RC.vals_of(g, fo)[0] == S.U
ok["y Even in R_k"] = g.owner[y] == 0 and y in S.Rr and fo[y] == z
ok["z in F_k, z's sigma*-play inside F_k"] = z in S.F and all(x in S.F for x in EC.play(fo, z)[0])
sv = S.sg[y]
ok["XG (i) U(z) = W(z) = Xi(z)"] = S.U[z] == S.W[z] == S.Xi[z]
ok["XG (ii) U(z) >= W(s)"] = g.cmp(S.U[z], S.W[sv]) >= 0
ok["XG (y, z) is a gate of level >= r_k"] = (y, z) in S.gates and S.gates[(y, z)] >= S.r
for kk, v in ok.items(): print(f"{kk}: {v}")
print(f"state {k}: r = {S.r}, gate level = {S.gates.get((y, z))}, s = sigma_k(y) = {sv}")
print("RESULT", "OK" if all(ok.values()) else "FAIL")
