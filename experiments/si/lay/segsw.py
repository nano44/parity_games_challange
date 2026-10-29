#!/usr/bin/env python3
"""L-SI box 27: per maximal REL segment [a, b] (lwp/seglast.py's cutting): the most switches of one Even vertex inside it (MAXSW), and
(b - a) - (Even vertices switching in it) (EXC; CONJECTURE SEG-COUNT says <= 0). Usage: segsw.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
import seglast
from common import rows, load, readstart
C = Counter(); EX = []
def run(g, name, start=None):
    E, R = rows(g, start); n = g.n
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        sw = Counter(v for t in range(a, b) for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v])
        m = max(sw.values()); exc = (b - a) - len(sw)
        C["segs"] += 1; C["maxsw_%d" % m] += 1; C["exc_max_plus100"] = max(C["exc_max_plus100"], 100 + exc)
        if m >= 3: EX.append(("MAXSW", name, a, b, m))
        if exc > 0: C["SEGCOUNT_V"] += 1; EX.append(("SEGCOUNT", name, a, b, exc))
def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:8]: print("EXAMPLE", z)
    print("SEGCOUNT PASS" if "SEGCOUNT_V" not in C else "SEGCOUNT FAIL")
if __name__ == "__main__":
    main()
