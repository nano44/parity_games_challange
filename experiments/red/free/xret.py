#!/usr/bin/env python3
"""L-RED R137: second counter (n5b SPEC, independent of l-new retclass.py): switches and returns of the vertex named X, tau-changes, fallbacks,
and the number of distinct W cycle-node maps along the run (1 = the whole run is one W-world). Usage: xret.py GAME.pg START [NAME]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
nm = sys.argv[3] if len(sys.argv) > 3 else "X"
names = {}
for l in open(sys.argv[1]):
    a = l.strip().rstrip(";").split()
    if len(a) >= 5 and a[0].isdigit(): names[a[4].strip('"')] = int(a[0])
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
N.run(s0, t0, trace=tr, fbtrace=fb); X = names[nm]
seq = [s[X] for s, t in tr]; sw = sum(1 for a, b in zip(seq, seq[1:]) if a != b)
held = set([seq[0]]); ret = {}
for a, b in zip(seq, seq[1:]):
    if a != b:
        if b in held: ret[b] = ret.get(b, 0) + 1
        held.add(b)
tch = sum(1 for (a, x), (b, y) in zip(tr, tr[1:]) if x != y)
print(f"XRET {os.path.basename(sys.argv[1])} n {g.n} iterations {len(tr) - 1} fallbacks {sum(fb)} tau-changes {tch} {nm}-switches {sw} "
      f"returns-per-edge {sorted(ret.values(), reverse=True)}")
