#!/usr/bin/env python3
"""L-RED R202 XMAX: is there a 2-wide degree-2 ladder genome (R197 model: option k of a level-l >= 1 mover W-points to mover 2(l-1) + k,
level 0 keyed by gates; any Xi-targets (acyclic), ranks, parities, gates, start) with d levels whose IDEAL run has at least t steps?
xcnf.py model with no prescribed movers, E = d free levels, and «step t nonempty». SAT -> genome replayed under r187/ideal.py.
Usage: xmax.py d t out.json   (env SOLVER, LEM)"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ.setdefault("TMIN", "1")
import xcnf, ideal
d, t, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
T = dict(movers=[], gate=[], states=[[] for _ in range(t + 1)])
t0 = time.time(); C, I = xcnf.build(T, d, lem=os.environ.get("LEM", "1") == "1")
print(f"XMAX d {d} t {t} N {I['N']} vars {C.n} clauses {len(C.cl)} build {time.time() - t0:.1f} s", flush=True)
t1 = time.time(); r, model = xcnf.solve(C)
print(f"XMAX d {d} T >= {t}: {'SAT' if r else 'UNSAT'} {time.time() - t1:.1f} s", flush=True)
if r:
    G = xcnf.decode(model, I); json.dump(G, open(out, "w")); S, why = ideal.traj(G)
    print(f"replay L {len(S) - 1} {why} (needs >= {t}): {'OK' if len(S) - 1 >= t or os.environ.get('TMIN') == '0' else 'MISMATCH'} -> {out}", flush=True)
    lev = G["lev"]; Cl = [sum(1 for u in range(1, len(S)) if any(S[u][v] != S[u - 1][v] for v in range(G["N"]) if lev[v] <= l)) for l in range(max(lev) + 1)]
    print(f"replayed C_l (steps moving a mover of level <= l): {Cl}", flush=True)
