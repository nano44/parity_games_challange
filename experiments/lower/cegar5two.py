#!/usr/bin/env python3
"""Two-player Büchi, n = 5, lower bound by CEGAR against RANDOM 5-vertex games (no full sweep: an UNSAT core is a proof,
a SAT candidate is only 'not refuted by the sample'). Subset starts from Q_3 + the n=4 core games (successor-closed).
Usage: cegar5two.py k [sample_per_round] [per_round_added] [seed]   (checkpoint b2_n5_k<k>.subset.json, resumable)"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotient import build
from sat2 import Sub, encode2
import vec2


def random_games(k, M, rng):
    S = rng.integers(1, 2 ** k, size=(M, k), dtype=np.uint8)
    ve = rng.integers(0, 2 ** k, size=M, dtype=np.uint8)
    p2 = rng.integers(0, 2 ** k, size=M, dtype=np.uint8)
    return S, ve, p2


if __name__ == "__main__":
    k = int(sys.argv[1]); M = int(sys.argv[2]) if len(sys.argv) > 2 else 2000000
    per_round = int(sys.argv[3]) if len(sys.argv) > 3 else 200; seed = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    n = 5; tag = f"b2_n5_k{k}"
    q3 = build(3, owners_set=(0, 1), verbose=True)
    sub = Sub(q3)
    ckpt = f"{tag}.subset.json"
    if os.path.exists(ckpt):
        sub.games = [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(ckpt))]
        print(f"resumed {len(sub.games)} games", flush=True)
    else:
        core4 = [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open("b2_n4_k6_core3.json"))["games"]]
        sub.games = [g for g in core4 if len(g[0]) == 4]
        print(f"seeded with {len(sub.games)} four-vertex core games", flush=True)
    rng = np.random.default_rng(seed); rnd = 0
    while True:
        rnd += 1
        json.dump(sub.games, open(ckpt, "w"))
        S, W = sub.struct(); t0 = time.time()
        solver, decode, ncl = encode2(S, W, list(range(S.N)), k)
        ok = solver.solve()
        print(f"round {rnd}: subset {S.N} nodes ({len(sub.games)} games), {ncl} clauses -> {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
        if not ok:
            print(f"RESULT: no program with {k} Cpre gates solves all two-player Büchi games with <= {n} vertices (UNSAT on a successor-closed subset): B_2({n}) >= {k+1}")
            json.dump({"k": k, "n": n, "result": "UNSAT", "subset_games": sub.games}, open(f"{tag}.json", "w")); sys.exit(1)
        tables = decode(solver.get_model()); solver.delete()
        t0 = time.time(); bad_total = 0; picked = []
        for chunk in range(4):
            S5, ve5, p25 = random_games(n, M // 4, rng)
            W5 = vec2.ref_W(S5, ve5, p25, n)
            out = vec2.eval_tables(tables, k, S5, ve5, p25, n)
            bad = np.nonzero(out != W5)[0]; bad_total += len(bad)
            for gi in bad[: max(1, per_round // 4)]:
                picked.append(vec2.game_at(S5, ve5, p25, int(gi), n))
            if len(picked) >= per_round: break
        print(f"   sample of {M} random 5-vertex games: {bad_total} failing (in the chunks seen) [{time.time()-t0:.1f}s]", flush=True)
        if bad_total == 0:
            print(f"candidate with {k} gates passes {M} random games; NOT a proof of an upper bound (no full sweep). Saving.")
            json.dump({"k": k, "n": n, "result": "SAT-sampled", "tables": tables, "subset_games": sub.games}, open(f"{tag}_candidate.json", "w")); sys.exit(0)
        sub.games.extend(picked[:per_round])
