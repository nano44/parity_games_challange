#!/usr/bin/env python3
"""L-RED R213 MOVE query (MOVES-2D): ladder of L^R_d whose run moves mover z (some option's Xi-target) >= r times within t steps.
Env TMIN=0. SAT -> decode, replay (r187/ideal.py), recount moves. Usage: move.py d t z r out.json"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..", "r200"); sys.path[:0] = [H, R, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ.setdefault("TMIN", "0")
d, t, z, r, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
os.environ["MOVEZ"] = str(z); os.environ["MOVEMIN"] = str(r)
import xcnf, ideal
t0 = time.time(); C, I = xcnf.build(dict(movers=[], gate=[], states=[[] for _ in range(t + 1)]), d)
t1 = time.time(); ok, model = xcnf.solve(C)
print(f"MOVE d {d} t {t} z {z} r {r}: {'SAT' if ok else 'UNSAT'} solve {time.time() - t1:.1f} s", flush=True)
if ok:
    G = xcnf.decode(model, I); json.dump(G, open(out, "w")); S, _ = ideal.traj(G)
    m = sum(1 for u in range(1, len(S)) if S[u][z] != S[u - 1][z]); tg = any(o[1] == z for v in range(G["N"]) for o in G["opts"][v])
    print(f"  replay T {len(S) - 1} moves of z {m} target {tg} ({'OK' if m >= r and (tg or os.environ.get('MOVEANY') or os.environ.get('MOVENT')) and not (tg and os.environ.get('MOVENT')) else 'MISMATCH'}) -> {out}", flush=True)
