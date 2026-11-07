#!/usr/bin/env python3
"""L-LOWER box L3 fast regression (run by experiments/lower/check.sh; < 1 min).
1. Family A (genA.py): T = 2d, moves(2l+1) = 2*floor(2l/3)+1 (l >= 1), every other mover 1, for d = 3..20 (CONJECTURE A-RUN data).
2. Own simulator sim.py == L-NEW box150 Gen (trunk experiments/new/box150/check.py) state for state: family A d 3..8 (every start
   for d <= 4) and inst/dense_d5_l3_H10.json (byte copy of L-RED claude/l-red experiments/red/r214/out/dense_d5_l3_H10.json, 36d340c7;
   every start).
3. tricheck (TRI, TRI-MU, FEEDBACK) on 60 random L^R_d genomes (seed 11, every start for N <= 8) and family A: 0 violations."""
import os, sys, json, itertools, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from sim import run, moves
from genA import genA
for d in range(3, 21):
    A = genA(d); S = run(A, A["start"]); m = moves(S, A["N"])
    assert len(S) - 1 == 2 * d and all(m[2 * l + 1] == 2 * ((2 * l) // 3) + 1 for l in range(1, d)) \
        and all(m[2 * l] == 1 for l in range(d)) and m[1] == 1, d
print("family A: T = 2d and moves(2l+1) = 2*floor(2l/3)+1 for d = 3..20")
P0 = os.path.join(H, "..", "..", "new", "box150", "check.py")
ns = {"__file__": os.path.abspath(P0), "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
runs = 0
gs = [genA(d) for d in range(3, 9)] + [json.load(open(os.path.join(H, "inst", "dense_d5_l3_H10.json")))]
for G in gs:
    N = G["N"]; sts = itertools.product([0, 1], repeat=N) if N <= 10 else [G["start"]]
    for st in sts:
        st = list(st); a = [tuple(s) for s in run(G, st)]; b = [tuple(s) for s in Gen(G).run(st)[0]]
        assert a == b, (N, st); runs += 1
print("sim.py == box150 Gen on", runs, "runs")
fa = []
for d in range(3, 9):
    p = os.path.join(H, "out", f"genA_d{d}.json")
    if not os.path.exists(p): json.dump(genA(d), open(p, "w"))
    fa.append(p)
out = subprocess.run([sys.executable, "-I", os.path.join(H, "tricheck.py"), "11", "60"] + fa, capture_output=True, text=True,
                     env=dict(os.environ, ALLN="8")).stdout
line = [l for l in out.splitlines() if l.startswith("TRICHECK")][-1]; print(line)
V = eval(line.split("violations ")[1].split(" info")[0]); assert all(v == 0 for v in V.values()), V
print("L3 CHECK PASS")
