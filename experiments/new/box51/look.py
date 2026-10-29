#!/usr/bin/env python3
"""L-NEW box 51: print one phase: per Even vertex with >= 2 distinct successors in the phase, its successor sequence; W-monotonicity check;
the shattered max sets (vcrun.vc) and their traces. Usage: look.py NAME [phase index]"""
import sys, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box50"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "root")); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "runlin"))
D = pickle.load(open(os.path.join(HERE, "..", "out", "box51", sys.argv[1] + ".pkl"), "rb"))
from vcrun import vc
pi = int(sys.argv[2]) if len(sys.argv) > 2 else 0; i, j = D["ph"][pi]; st = D["st"]; n = D["n"]
ev = [v for v in range(n) if D["owner"][v] == 0 and len(D["succ"][v]) >= 2]
osc = [v for v in ev if len({st[k]["s"][v] for k in range(i, j + 1)}) >= 2]
print("phase", i, j, "len", j - i, "oscillating Even", len(osc))
for v in osc: print(" v%-4d" % v, " ".join(str(st[k]["s"][v]) for k in range(i, j + 1)))
bad = [(k, v) for k in range(i, j) for v in range(n) if st[k + 1]["W"][v] < st[k]["W"][v]]
print("W decreases:", len(bad), bad[:5])
weq = sum(1 for k in range(i, j) if st[k + 1]["W"] == st[k]["W"]); print("W-plateau transitions:", weq, "fallbacks:", sum(st[k]["fb"] for k in range(i, j)))
d, m, nf, w = vc([frozenset((v, st[k]["s"][v]) for v in ev) for k in range(i, j + 1)])
print("VC", d, "m", m, "witness", w)
for e in w: print("  ", e, "".join("1" if st[k]["s"][e[0]] == e[1] else "." for k in range(i, j + 1)))
print("fb at", [k for k in range(i, j) if st[k]["fb"]], " W-decrease at", sorted({k for k, v in bad}))
