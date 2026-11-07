#!/usr/bin/env python3
"""L-RED 55 R219: DATA on random NOUP genomes (L-NEW box 193 noup193.rgen_noup, read only via env WT193 = worktree of claude/l-new
e3d399cd): own.py run, T, max flips at one gate. Usage: WT193=<dir> noupdata.py COUNT SEED"""
import sys, os, random
W = os.environ["WT193"]
for sub in ("box193", "box191", "box189"): sys.path.insert(0, os.path.join(W, "experiments/new", sub))
import noup193
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import own
rng = random.Random(int(sys.argv[2]))
for i in range(int(sys.argv[1])):
    d = rng.randint(1, 6); G = noup193.rgen_noup(rng, d, rng.randint(1, 4), rng.randint(2, 3))
    out, V, O, ow = own.run(G); N = G["N"]; T = len(out) - 1
    fl = max([sum(out[t][2][V[("g", q)]] != out[t - 1][2][V[("g", q)]] for t in range(1, len(out))) for q in O if G["lev"][q[0]] >= 1] or [0])
    print(i, d, N, T, fl, flush=True)
