#!/usr/bin/env python3
"""Full sweep of a k-gate candidate (tables from a cegar5two *_candidate.json) over ALL 5-vertex two-player Büchi games
whose |P_2| lies in P2SIZES, pattern by pattern (owner mask x priority mask; 31^5 = 28 629 151 successor assignments each).
Prints the first failing games (as raw games) and the total. Usage: sweep_p2.py candidate.json k  (env P2SIZES=1)"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vec2

n = 5
if __name__ == "__main__":
    d = json.load(open(sys.argv[1])); k = int(sys.argv[2]); tables = d["tables"]
    sizes = [int(x) for x in os.environ.get("P2SIZES", "1").split(",")]
    vals = np.arange(1, 2 ** n, dtype=np.uint8)
    grids = np.meshgrid(*([vals] * n), indexing="ij"); S0 = np.stack([g.ravel() for g in grids], axis=1); M0 = len(S0)
    total_bad = 0; shown = 0; t0 = time.time(); pats = 0
    for p2m in range(2 ** n):
        if bin(p2m).count("1") not in sizes: continue
        for vem in range(2 ** n):
            ve = np.full(M0, vem, dtype=np.uint8); p2 = np.full(M0, p2m, dtype=np.uint8)
            W = vec2.ref_W(S0, ve, p2, n); out = vec2.eval_tables(tables, k, S0, ve, p2, n)
            bad = np.nonzero(out != W)[0]; total_bad += len(bad); pats += 1
            for gi in bad[:3]:
                if shown < 20: print("fail:", vec2.game_at(S0, ve, p2, int(gi), n), flush=True); shown += 1
            if pats % 8 == 0: print(f"  {pats} patterns, {total_bad} failing so far [{time.time()-t0:.0f}s]", flush=True)
    print(f"RESULT: {total_bad} failing games over all 5-vertex games with |P_2| in {sizes} ({pats} patterns x {M0} games)")
