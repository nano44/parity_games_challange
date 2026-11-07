#!/usr/bin/env python3
"""random gadget ranks/parities (Xi-graph fixed) x exact csp.py search; reports the largest NEED solved. Usage:
cspdrive.py clock.json gadget.json TP TQ NEED tries maxnodes seed"""
import os, sys, json, random, subprocess
H = os.path.dirname(os.path.abspath(__file__))
cf, vf, TP, TQ, NEED, tries, maxn, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6]), sys.argv[7], int(sys.argv[8])
rng = random.Random(seed); V = json.load(open(vf)); M = 2 * V["N"]
for i in range(tries):
    W = json.loads(json.dumps(V)); br = list(range(M)); rng.shuffle(br); W["br"] = br; W["bp"] = [rng.randint(0, 1) for _ in range(M)]
    fn = os.path.join(H, "out", "gadget_s%d_i%d.json" % (seed, i)); json.dump(W, open(fn, "w"))
    out = subprocess.run([sys.executable, os.path.join(H, "csp.py"), cf, fn, TP, TQ, str(NEED), maxn], capture_output=True, text=True).stdout
    line = out.strip().split("\n")
    print(i, line[0][-40:], *(l for l in line[1:2]), flush=True)
    if "BUILT" in out: print(out, flush=True); break
    os.remove(fn)
