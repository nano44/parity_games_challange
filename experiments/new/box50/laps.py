#!/usr/bin/env python3
"""L-NEW box 50: LAPS inside one fallback-free run. For each run, the switch set of a transition t -> t+1 is {(v, s_t(v), s_{t+1}(v))}
over switching Even vertices. REP := the most transitions of one run with the SAME switch set (a lap repeated REP times makes REP >= its
count); EREP := the most transitions of one run containing one same single switch (v, a, b). Usage: laps.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("root", "runlin"): sys.path.insert(0, os.path.join(ROOT, "experiments", "si", p))
from common import rows, load, readstart
from trace import runs
C = Counter(); TOP = []

def one(g, name, start=None):
    E, R = rows(g, start); ev = [v for v in range(g.n) if g.owner[v] == 0]
    for a, b, i, j in runs(R):
        if b <= a: continue
        sets = Counter(); single = Counter()
        for t in range(a, b):
            sw = frozenset((v, R[t]["s"][v], R[t + 1]["s"][v]) for v in ev if R[t]["s"][v] != R[t + 1]["s"][v])
            sets[sw] += 1
            for x in sw: single[x] += 1
        rep = max(sets.values()); erep = max(single.values()); C["runs"] += 1
        C["REP_max"] = max(C["REP_max"], rep); C["EREP_max"] = max(C["EREP_max"], erep)
        TOP.append((rep, erep, b - a, g.n, name, a, b))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": one(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                X = lambda q: os.path.join(ROOT, "experiments", q)
                try: one(load(X(p[0])), p[0], readstart(X(p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
                except Exception as ex: C["ERR"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(TOP, key=lambda x: (-x[0], -x[1]))[:6]: print("TOP REP %d EREP %d run %d n %d %s [%d,%d]" % x)
    for x in sorted(TOP, key=lambda x: (-x[1], -x[0]))[:4]: print("TOPE REP %d EREP %d run %d n %d %s [%d,%d]" % x)

if __name__ == "__main__":
    main()
