#!/usr/bin/env python3
"""B_2 restricted to an owner class at n = 4: CEGAR (as sat2.cegar4) against all 4-vertex games whose Even-owner mask lies
in a given set. Usage: cegar_owner.py k mask1,mask2,... [per_round] [p2mask1,p2mask2,...]   (mask = bits of V_E; 0 = all vertices Odd;
optional p2 masks = bits of P_2 to restrict the class further)"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotient import build
from sat2 import Sub, encode2
import vec2

if __name__ == "__main__":
    k = int(sys.argv[1]); masks = [int(m) for m in sys.argv[2].split(",")]; per_round = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    p2masks = [int(m) for m in sys.argv[4].split(",")] if len(sys.argv) > 4 else None
    tag = f"b2_n4_k{k}_ve{'-'.join(map(str, masks))}" + (f"_p2{'-'.join(map(str, p2masks))}" if p2masks else "")
    S4, ve4, p24 = vec2.all_games(4); keep = np.isin(ve4, masks)
    if p2masks: keep &= np.isin(p24, p2masks)
    if os.environ.get("FILTER"):   # extra numpy filter on (S4, ve4, p24), e.g. "deg(3)==2" with deg(v) = out-degree of v
        deg = lambda v: np.array([bin(int(x)).count("1") for x in S4[:, v]])
        loop = lambda v: ((S4[:, v] >> v) & 1).astype(bool)
        keep &= eval(os.environ["FILTER"]); tag += "_" + os.environ.get("FTAG", "f")
    S4, ve4, p24 = S4[keep], ve4[keep], p24[keep]
    W4 = vec2.ref_W(S4, ve4, p24, 4); print(f"games with V_E in {masks}: {len(S4)}", flush=True)
    # small games of the same owner class (<= 3 vertices): all owner patterns whose vertices are all in the class are NOT a
    # subclass in general; use only the 4-vertex games themselves (lower bounds on a subclass are weaker, which is the point)
    sub = Sub(build(1, owners_set=(0, 1)))  # Q_1 (4 classes) as a harmless base
    sub.games = []
    rnd = 0; rng = np.random.default_rng(0)
    while True:
        rnd += 1
        S, W = sub.struct(); t0 = time.time()
        solver, decode, ncl = encode2(S, W, list(range(S.N)), k); ok = solver.solve()
        print(f"round {rnd}: {len(sub.games)} games, {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
        if not ok:
            print(f"RESULT: no {k}-gate program solves all 4-vertex games with V_E in {masks} (UNSAT core of {len(sub.games)} games)")
            json.dump({"k": k, "masks": masks, "result": "UNSAT", "subset_games": sub.games}, open(f"{tag}.json", "w")); sys.exit(1)
        tables = decode(solver.get_model()); solver.delete()
        out = vec2.eval_tables(tables, k, S4, ve4, p24, 4); bad = np.nonzero(out != W4)[0]
        print(f"   {len(bad)} failing", flush=True)
        if len(bad) == 0:
            print(f"RESULT: {k} gates solve all 4-vertex games with V_E in {masks}")
            json.dump({"k": k, "masks": masks, "result": "SAT", "tables": tables}, open(f"{tag}.json", "w")); sys.exit(0)
        pick = bad if len(bad) <= per_round else rng.choice(bad, per_round, replace=False)
        sub.games.extend(vec2.game_at(S4, ve4, p24, int(g), 4) for g in pick)
