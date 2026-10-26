#!/usr/bin/env python3
"""Box 47 DATA: in-phase S4c fallbacks per phase (f) against n, and how many of them are at states with D = empty / D != empty, and the
longest run of consecutive fallbacks with no W-honest state between them. Usage: fbph.py STARTS SEED (--list FILE | files) [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box46", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
import hon
from levels import load, step, start_pair, Engine, dual
C = {"fmax": 0, "f_over_n": 0.0}; TOP = []
def run(g, start, nm, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append((tuple(x[0] for x in vs), tuple(t), r[4] if r else 0, any(sb[q] != t[q] for q in Q)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        f = sum(rows[k][2] for k in range(i, j)); fD = sum(rows[k][2] for k in range(i, j) if rows[k][3])
        if f > C["fmax"]: C["fmax"] = f; C["fmax_n"] = g.n; C["fmax_nm"] = nm; C["fmax_D"] = fD
        if f / g.n > C["f_over_n"]: C["f_over_n"] = round(f / g.n, 3); C["fon_nm"] = nm; C["fon_f"] = f; C["fon_n"] = g.n
        i = j + 1
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 64
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: run(g, st, nm)
            except RecursionError: pass
    print(C)
