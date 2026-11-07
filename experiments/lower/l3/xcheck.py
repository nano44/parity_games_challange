#!/usr/bin/env python3
"""Cross-check: own simulator (sim.py) vs L-NEW's box150 Gen, and L-NEW's movescheck.py check_run counters, on given genome JSONs.
LNEW env = root of an l-new tree (needs experiments/new/box150, box139, box187). Prints per file: T, moves, state-sequence agreement,
movescheck counters (all must be 0). ALLS=1: also every start (2^N) when N <= 12.
Usage: LNEW=... xcheck.py f.json ..."""
import os, sys, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim
B = os.path.join(os.environ["LNEW"], "experiments", "new", "box187", "movescheck.py")
ns = {"__file__": B, "__name__": "lib"}; exec(open(B).read().split("\nif __name__")[0], ns)
Gen, check_run, C, is_lr = ns["Gen"], ns["check_run"], ns["C"], ns["is_lr"]
bad = 0; runs = 0
for p in sys.argv[1:]:
    G = json.load(open(p)); N = G["N"]; assert is_lr(G), p
    starts = [G["start"]]
    if os.environ.get("ALLS") and N <= 12: starts = [list(s) for s in itertools.product([0, 1], repeat=N)]
    for st in starts:
        S1 = sim.run(G, st); g = Gen(G); S2, _ = g.run(st)
        if [tuple(s) for s in S1] != [tuple(s) for s in S2]: bad += 1; print("MISMATCH", p, st)
        check_run(g, G, S2); runs += 1
    S = sim.run(G, G["start"]); m = sim.moves(S, N); Z = sim.xitargets(G)
    print(os.path.basename(p), "T", len(S) - 1, "muZ", max([m[z] for z in Z if G["lev"][z] >= 1], default=0), "moves", m)
print("RUNS", runs, "SIM-MISMATCH", bad, "MOVESCHECK", C)
