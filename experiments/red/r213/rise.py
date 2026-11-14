#!/usr/bin/env python3
"""L-RED R213 RISE query: is there a ladder of L^R_d (r200 xcnf model, all levels free) whose run has a mover z, the Xi-target of some
option, whose current value rises >= r times within the first t steps? Env TMIN=0 (runs of any length <= t). SAT -> genome decoded,
replayed by r187/ideal.py, rises recounted by rises.py. Usage: rise.py d t z r out.json"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..", "r200"); sys.path[:0] = [H, R, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ.setdefault("TMIN", "0")
d, t, z, r, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
os.environ["RISEZ"] = str(z); os.environ["RISEMIN"] = str(r)
import xcnf, rises
t0 = time.time(); C, I = xcnf.build(dict(movers=[], gate=[], states=[[] for _ in range(t + 1)]), d)
t1 = time.time(); ok, model = xcnf.solve(C)
print(f"RISE d {d} t {t} z {z} r {r}: {'SAT' if ok else 'UNSAT'} build {t1 - t0:.1f} s solve {time.time() - t1:.1f} s vars {C.n} clauses {len(C.cl)}", flush=True)
if ok:
    G = xcnf.decode(model, I); json.dump(G, open(out, "w")); T, mr, opt, rz, fall = rises.rises(G)
    print(f"  replay T {T} rises of z {rz[z]} (needs >= {r}: {'OK' if rz[z] >= r else 'MISMATCH'}) maxR {mr} at {opt} FALL {fall} -> {out}", flush=True)
