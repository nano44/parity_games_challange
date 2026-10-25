#!/usr/bin/env python3
"""L-SI succ. 7, box 12: DATA for packet P-N5-LV2 (SAND, LV-NONE, SCOPE-FB). SAND: after the first in-scope state with r = -1, COARSE_{-1}(θ) is checked at every later state of the run. Per scope run (reltrace.runs_of): the number of in-scope
transitions with r = -1 (SAND's hypothesis), fallbacks by class (level >= 0 / level -1 with r >= 0 / r = -1 / EQ), and the largest ratio
#fallbacks / (4·n·n_E + 3). Usage: scopefb.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *
from mono import coarse

def main(files):
    C = Counter(); worst = (0, None)
    for p in files:
        g = load(p); o = odd_choice(g)
        if o is None: continue
        runs, d_o, exits, out = runs_of(g, os.path.basename(p)); nE = sum(1 for v in range(g.n) if g.owner[v] == 0)
        for S in runs:
            C["scope_runs"] += 1; nf = 0; base = None
            for e in S:
                for idx in (e["i"], e["i"] + 1):
                    th = coarse(out[idx]["Xi"][o], -1)
                    if base is not None:
                        C["SAND_checks"] += 1
                        if th != base: C["SAND_FAIL"] += 1
                if e["r"] == -1 and base is None: base = coarse(out[e["i"]]["Xi"][o], -1)
                if e["r"] == -1: C["transitions_r=-1"] += 1
                if e["k"] != "F": continue
                nf += 1; r, M = e["r"], e["M"]
                C["fb_EQ" if r <= -2 else ("fb_r=-1" if r == -1 else ("fb_M>=0" if M >= 0 else "fb_M=-1_r>=0"))] += 1
            C["max_fb_per_run"] = max(C["max_fb_per_run"], nf)
            ratio = nf / (4 * g.n * nE + 3)
            if ratio > worst[0]: worst = (ratio, (os.path.basename(p), nf, g.n, nE))
    print("TOTAL", dict(sorted(C.items()))); print("WORST ratio fallbacks/(4 n n_E + 3):", worst)

if __name__ == "__main__":
    main(sys.argv[1:])
