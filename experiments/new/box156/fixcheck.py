#!/usr/bin/env python3
"""box 156: cross-check the z3 step encoding of zmax.py against the box 150 simulator on random deg <= 2 genomes with xorder = identity
(relabelled), M = 2N ranks/gates. Prints the number of mismatching runs (must be 0)."""
import sys, json, random, subprocess, os
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from val import ns
import tempfile; FX = tempfile.mktemp(suffix=".json")
rng = random.Random(int(sys.argv[1])); cnt = int(sys.argv[2]); bad = 0
for i in range(cnt):
    N = rng.randint(2, 6); lev = sorted(rng.randint(0, 2) for _ in range(N)); 
    lev = [l - min(lev) for l in lev]; ls = sorted(set(lev)); lev = [ls.index(l) for l in lev]; rng.shuffle(lev)
    opts, idx = [], 0
    for x in range(N):
        D = 1 if rng.random() < 0.15 else 2; o = []
        for k in range(D):
            low = [v for v in range(N) if lev[v] == lev[x] - 1]; w = rng.choice(low) if lev[x] > 0 else -1
            later = list(range(x + 1, N)); t_ = rng.choice(later) if later and rng.random() < 0.8 else -1
            o.append([w, t_, idx]); idx += 1
        opts.append(o)
    gates = rng.sample(range(2 * N), idx); it = iter(gates); gate = [[next(it) for _ in o] for o in opts]
    br = rng.sample(range(2 * N), idx); bp = [rng.randint(0, 1) for _ in range(idx)]
    start = [rng.randrange(len(o)) for o in opts]
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": start, "xorder": list(range(N))}
    g = ns["Gen"](G); S, _ = g.run(start); L = len(S) + 1
    json.dump(G, open(FX, "w"))
    z = json.loads(subprocess.run(["python3", "zmax.py", str(N), "T", str(L)], env=dict(os.environ, FIX=FX, NOSYM="1"), capture_output=True, text=True).stdout)
    want = [list(s) for s in S] + [list(S[-1])] * (L + 1 - len(S))
    if z != want: bad += 1; print("MISMATCH", G, z, want)
print("fixcheck runs", cnt, "mismatches", bad)
