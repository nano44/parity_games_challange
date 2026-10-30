#!/usr/bin/env python3
"""L-RED R135: classify the WAITS in l-new box 80's lead-follow ladder schedule (the schedule box 82's ogl_k replays).
At each step, a chooser v that is NOT the scheduled switcher but has a W-better successor must be blocked (box 82 section 3).
UPWARD wait: some reader of v (a level-(j+1) vertex or T) currently points to v. LATERAL wait: none does (v waits for a peer).
Usage: upwait.py LADDER.pg LADDER.seq   (l-new box80/inst/ladder_K.*)"""
import sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg
from si import Engine
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
seq = [tuple(map(int, l.split())) for l in open(sys.argv[2]) if l[0] != "%"]
E = Engine(g); n = g.n
sig = [g.succ[v][0] for v in range(n)]
ch = [v for v in range(n) if len(g.succ[v]) > 1]
readers = {v: [r for r in ch if v in g.succ[r]] for v in range(n)}
up = lat = steps = 0; upv = {}
for (v0, t0) in seq:
    W = E.evaluate(tuple(sig))[0]
    for v in ch:
        if v == v0: continue
        if any(E.key(W[w]) > E.key(W[sig[v]]) for w in g.succ[v] if w != sig[v]):
            if any(sig[r] == v for r in readers[v]): up += 1; upv[v] = upv.get(v, 0) + 1
            else: lat += 1
    sig[v0] = t0; steps += 1
print(f"UPWAIT {os.path.basename(sys.argv[1])} steps {steps} upward-blocked {up} lateral-blocked {lat} vertices-with-upward-waits {len(upv)}")
