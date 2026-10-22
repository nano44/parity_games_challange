#!/usr/bin/env python3
"""Family K_n at n = 5 (the localised hard class of L2-theory §3): vertex 4 = e is Even with priority 1; vertices 0..3 are
Odd; vertex 0 has priority 2, vertex 1 priority 2 or 1 (two patterns), vertices 2, 3 priority 1; every vertex has exactly
two successors (DEG env: '2' exact, '12' = one or two). Exact CEGAR against ALL games of the class (no sampling).
Usage: cegar_class5.py k [per_round]  (checkpoint k5_k<k>.subset.json)"""
import sys, os, time, json, itertools
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sat2 import encode2
from coremin import struct_only
import vec2

n = 5

def class_arrays():
    deg = os.environ.get("DEG", "2")
    masks = [m for m in range(1, 32) if (bin(m).count("1") == 2 if deg == "2" else bin(m).count("1") in (1, 2))]
    vals = np.array(masks, dtype=np.uint8)
    grids = np.meshgrid(*([vals] * n), indexing="ij")
    S0 = np.stack([g.ravel() for g in grids], axis=1); M0 = len(S0)
    S = np.tile(S0, (2, 1)); ve = np.full(2 * M0, 16, dtype=np.uint8)
    p2 = np.concatenate([np.full(M0, 1, dtype=np.uint8), np.full(M0, 3, dtype=np.uint8)])
    return S, ve, p2

if __name__ == "__main__":
    k = int(sys.argv[1]); per_round = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    tag = f"k5_deg{os.environ.get('DEG','2')}_k{k}"
    S5, ve5, p25 = class_arrays(); W5 = vec2.ref_W(S5, ve5, p25, n)
    print(f"class K_5: {len(S5)} games", flush=True)
    games = []; ckpt = f"{tag}.subset.json"
    if os.path.exists(ckpt):
        games = [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(ckpt))]; print(f"resumed {len(games)}", flush=True)
    rng = np.random.default_rng(0); rnd = 0
    while True:
        rnd += 1; json.dump(games, open(ckpt, "w"))
        if games:
            S, W = struct_only(games); t0 = time.time()
            solver, decode, ncl = encode2(S, W, list(range(S.N)), k); ok = solver.solve()
            print(f"round {rnd}: {len(games)} games, {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
            if not ok:
                print(f"RESULT: no {k}-gate program solves K_5 (UNSAT core of {len(games)} games)")
                json.dump({"k": k, "n": n, "result": "UNSAT", "subset_games": games}, open(f"{tag}.json", "w")); sys.exit(1)
            tables = decode(solver.get_model()); solver.delete()
            out = vec2.eval_tables(tables, k, S5, ve5, p25, n); bad = np.nonzero(out != W5)[0]
        else:
            bad = np.arange(len(S5))
        print(f"   {len(bad)} failing", flush=True)
        if len(bad) == 0:
            print(f"RESULT: {k} gates solve all of K_5"); json.dump({"k": k, "result": "SAT", "tables": tables}, open(f"{tag}.json", "w")); sys.exit(0)
        pick = bad if len(bad) <= per_round else rng.choice(bad, per_round, replace=False)
        games.extend(vec2.game_at(S5, ve5, p25, int(g), n) for g in pick)
