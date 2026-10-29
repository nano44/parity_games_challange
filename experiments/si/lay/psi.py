#!/usr/bin/env python3
"""L-SI box 27: candidate potentials on REL segments (lay/wsink.py's sets): PSI1 = |U^W_t| + |U^H_t| + (unready W-sinks at t);
PSI0 = |U^W_t| + |U^H_t|. Counts steps where a potential does not strictly drop (PSI1_V, PSI0_V). Usage: psi.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
src = open(os.path.join(HERE, "wsink.py")).read().replace('''            both = [v for v in WS if v in HS]''', '''            both = [v for v in WS if v in HS]
            P[(name, a, b, t)] = (len(UW) + len(UH), len(UW) + len(UH) + len(WS) - len(rws))''')
ns = {"__name__": "psi", "__file__": os.path.join(HERE, "wsink.py")}; exec(compile(src, "wsink.py", "exec"), ns)
from common import rows, load, readstart
P = {}; ns["P"] = P; C = Counter(); EX = []
def run(g, name, start=None):
    P.clear(); E, R = rows(g, start); ns["_run"](g, R, name)
    for (nm, a, b, t), (p0, p1) in P.items():
        q0, q1 = P.get((nm, a, b, t + 1), (0, 0))
        C["steps"] += 1
        if q0 >= p0: C["PSI0_V"] += 1
        if q1 >= p1: C["PSI1_V"] += 1; EX.append((nm, a, b, t, p1, q1))
def psiscore(g, R):
    """for lay/wclimb.py OBJ=P: (PSI1 failures, steps where PSI1 drops by exactly 1)."""
    P.clear(); ns["_run"](g, R, "x"); f = tight = 0
    for (nm, a, b, t), (p0, p1) in P.items():
        q1 = P.get((nm, a, b, t + 1), (0, 0))[1]; f += q1 >= p1; tight += p1 - q1 == 1
    return f, tight

a = sys.argv[1:]
if __name__ != "__main__": a = ["--none"]
if a[0] == "--none": pass
elif a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
else:
    ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
    for line in open(a[1]):
        p = line.split() if line.strip() and not line.startswith("#") else None
        if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
if __name__ == "__main__": print(" ".join(f"{k}={v}" for k, v in sorted(C.items()))); [print("EXAMPLE", z) for z in EX[:4]]
