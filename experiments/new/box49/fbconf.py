#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA for docs/new/N5-READER-box49.md §7: per phase P of N5, f(P) := the in-phase S4c fallbacks (transitions
t -> t+1 inside P with fallback flag 1) and |C_f(P)| := the number of distinct configurations σ̄_t|Q at their sources t (RESULTS R71's 𝒞_f(P);
Q = Odd vertices of out-degree >= 2). Also: RECUR := fallback sources whose configuration already occurred at an earlier fallback source of the
same phase; and the largest gap (in fallbacks) between two sources with the same configuration.
Usage: fbconf.py STARTS SEED (--list FILE | files) [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from collections import Counter
C = Counter(); MAX = {}
def mx(k, v, tag):
    if v > MAX.get(k, (-1,))[0]: MAX[k] = (v, tag)

def run(g, st, nm):
    E, R = rows(g, st); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    for i, j in phases(R):
        src = [t for t in range(i, j) if R[t]["fb"]]
        cf = [tuple(R[t]["sb"][q] for q in Q) for t in src]
        f, k = len(cf), len(set(cf)); C["phases"] += 1; C["f"] += f; C["Cf"] += k; C["RECUR"] += f - k
        tag = (nm, (i, j), g.n, len(Q))
        mx("Cf", k, tag + (f,)); mx("Cf_over_n", k / g.n, tag + (k, f)); mx("f", f, tag + (k,)); mx("f_over_Cf", f / k if k else 0, tag + (f, k))
        if f: C["phases_with_fb"] += 1

if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    files = [os.path.join(ROOT, l.split()[0]) for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else a
    for f in files:
        g = load(f)
        if g.n > nmax: continue
        sf = f[:-3] + ".start"
        sts = [readstart(sf) if os.path.exists(sf) else None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                                  {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, os.path.relpath(f, ROOT)); C["runs"] += 1
            except RecursionError: C["RECERR"] += 1
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for k, v in sorted(MAX.items()): print("max", k, v)
