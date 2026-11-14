#!/usr/bin/env python3
"""L-RED R213 T^N query (L-NEW box 183, real-run form): a ladder of L^R_d (xcnf, all free) whose IDEAL run has >= u steps changing levels
>= 1 (U) and <= k steps moving 0 or 1, within horizon t (TMIN=0). SAT -> decode, replay (ideal.py), recount U and level-0 steps.
Usage: tn.py d t u k out.json   (k = -1: no level-0 limit)"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..", "r200"); sys.path[:0] = [H, R, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ.setdefault("TMIN", "0")
d, t, u, k, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
os.environ["UMIN"] = str(u)
if k >= 0: os.environ["Z0MAX"] = str(k)
import xcnf, ideal
C, I = xcnf.build(dict(movers=[], gate=[], states=[[] for _ in range(t + 1)]), d)
t1 = time.time(); ok, model = xcnf.solve(C)
print(f"TN d {d} t {t} U >= {u} k {k}: {'SAT' if ok else 'UNSAT'} solve {time.time() - t1:.1f} s", flush=True)
if ok:
    G = xcnf.decode(model, I); json.dump(G, open(out, "w")); S, _ = ideal.traj(G); lev = G["lev"]
    U = sum(1 for s in range(1, len(S)) if any(S[s][v] != S[s - 1][v] for v in range(G["N"]) if lev[v] >= 1))
    Z = sum(1 for s in range(1, len(S)) if any(S[s][v] != S[s - 1][v] for v in range(G["N"]) if lev[v] == 0))
    print(f"  replay T {len(S) - 1} U {U} level-0 steps {Z} ({'OK' if U >= u and (k < 0 or Z <= k) else 'MISMATCH'}) -> {out}", flush=True)
