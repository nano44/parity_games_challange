#!/usr/bin/env python3
"""Self-test engines with KNOWN rows: N5 (SPEC S1-S5 from SPEC's default start S3) and N5'-xi ([N5XI], RESULTS R118), through
L-COMP's own implementation experiments/comp/box44/n5xi44.py (on n5-second/n5b.py's SpecSI). Both candidates are DEAD as
polynomial algorithms (N5: P-N5-EXP, 2^k + 1 iterations on Gamma3(G_k); N5'-xi: R130, the wrapper family); they are here
because their iteration counts are known exactly, so the battery can be checked against them.
Usage: n5.py [--mode spec|xi] GAME.pg -> one JSON line. iterations = passes through SPEC steps 2-5 (n5b reading A8); steps = null."""
import sys, os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "comp", "box44"))
import n5xi44, pg
mode = sys.argv[sys.argv.index("--mode") + 1] if "--mode" in sys.argv else "spec"
r = n5xi44.run(pg.read(sys.argv[-1]), mode)
print(json.dumps({"winner": r["win"], "strategy": {str(v): w for v, w in enumerate(r["strat"]) if w is not None}, "iterations": r["Ttot"], "steps": None}))
