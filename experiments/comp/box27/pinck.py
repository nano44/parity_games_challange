#!/usr/bin/env python3
"""Audit check of cnf.py's semantics (W=R, no padding): pin a whole genome AND its start by unit clauses, then the CNF must be
SAT for L = T and UNSAT for L = T + 1, where T is sim.py's run length (sim.py = literal R104 rules). Random acyclic R197-wired
genomes, d given in argv[1], count in argv[2]. Any disagreement is printed."""
import sys, random, os
os.environ.pop("SYM", None); os.environ.pop("CUBE", None)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cnf, sim
from pysat.solvers import Solver

def rgen(rng, d):
    N = 2 * d; order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    M = 2 * N; ranks = list(range(M)); rng.shuffle(ranks); gates = list(range(M)); rng.shuffle(gates)
    opts = []
    for x in range(N):
        l = x // 2; later = [y for y in range(N) if pos[y] > pos[x]]
        opts.append([[-1 if l == 0 else 2 * (l - 1) + k, rng.choice(later + [-1] * rng.randrange(1, 3)) if later else -1, 2 * x + k] for k in range(2)])
    return {"N": N, "lev": [x // 2 for x in range(N)], "opts": opts, "gate": [[gates[2 * x], gates[2 * x + 1]] for x in range(N)],
            "br": ranks, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(2) for _ in range(N)]}

def pinned_sat(G, d, L):
    C, I = cnf.build(d, L, None, "R")
    for (x, k) in I["opts"]:
        y = G["opts"][x][k][1]
        C.add([I["Xv"][(x, k)][y]])
        b = G["opts"][x][k][2]; C.add([I["par"][(x, k)] if G["bp"][b] else -I["par"][(x, k)]])
    for o in I["opts"]:
        for o2 in I["opts"]:
            if o != o2: lit = I["rk"][(o, o2)]; C.add([lit if G["br"][G["opts"][o[0]][o[1]][2]] < G["br"][G["opts"][o2[0]][o2[1]][2]] else -lit])
    for l, V in I["gord"].items():
        for (a, b), lit in V.items():
            C.add([lit if G["gate"][a[0]][a[1]] < G["gate"][b[0]][b[1]] else -lit])
    for x in range(G["N"]):
        a = I["S"][0][x]; C.add([a] if G["start"][x] else [-a])
    s = Solver(name="cadical195", bootstrap_with=C.cl); return s.solve()

if sys.argv[1] == "files":   # pinck.py files f.json ... : every start of every (R-wired, 2-wide, degree-2) genome file
    import json, itertools
    bad = runs = 0; hist = {}
    for f in sys.argv[2:]:
        G0 = json.load(open(f)); d = G0["N"] // 2
        assert G0["lev"] == [x // 2 for x in range(G0["N"])] and all(G0["opts"][x][k][0] == (-1 if x < 2 else 2 * (x // 2 - 1) + k) for x in range(G0["N"]) for k in range(2))
        for st in itertools.product((0, 1), repeat=G0["N"]):
            G = dict(G0); G["start"] = list(st); S, why = sim.run(G); T = len(S) - 1; hist[T] = hist.get(T, 0) + 1; runs += 1
            a = pinned_sat(G, d, T) if T >= 1 else True; b = pinned_sat(G, d, T + 1)
            if not a or b: bad += 1; print("DISAGREE", f, st, T, a, b)
    print(f"pinck files: runs {runs}, T histogram {dict(sorted(hist.items()))}, disagreements {bad}"); sys.exit(0)
d, n = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(1000 + d); bad = 0; hist = {}
for i in range(n):
    G = rgen(rng, d); S, why = sim.run(G); T = len(S) - 1; hist[T] = hist.get(T, 0) + 1
    a = pinned_sat(G, d, T) if T >= 1 else True; b = pinned_sat(G, d, T + 1)
    if not a or b: bad += 1; print("DISAGREE", i, T, why, a, b, G)
print(f"pinck d {d}: genomes {n}, T histogram {dict(sorted(hist.items()))}, disagreements {bad}")
