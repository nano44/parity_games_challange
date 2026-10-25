#!/usr/bin/env python3
"""L-SI succ. 10, box 15: random C^1O games and hill-climbs for kwcheck.py's checks (REFEREE-2's games, mutations and tracer, read only).
  kwclimb.py random N nmin nmax seed          N random o-cyclic C^1O games (RC.rand_game), S3 start + 2 random starts, SPEC mode
  kwclimb.py climb FIT seed nmin nmax secs    hill-climb; FIT: kind (c_w > c_theta, not H2 runs: post-freeze length, kind changes,
                                              c_w switches), wonce (Xi-flat non-fallback pairs), long (Xi-changes on R per run)
Any check failure stops and dumps the game to kw15/climb/viol_<FIT>_<seed>.pg; the best game goes to kw15/climb/best_<FIT>_<seed>.pg."""
import sys, os, random, time
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kwcheck as KW
OC, FC, RC = KW.OC, KW.FC, KW.RC
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "docs", "referee-2", "R2-N5-FRZ"))
import frz_climb as FCL

def evaluate(g, o, seed, C=None, M=None):
    C = Counter() if C is None else C; M = Counter() if M is None else M; bad = []
    rng = random.Random(seed)
    for r in range(3):
        s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
        A, fbs = OC.run_trace(g, o, s, t, rng, "spec"); C["traces"] += 1; C["transitions"] += len(fbs)
        KW.scan(g, o, A, fbs, C, M, bad, r)
    return C, M, bad

def fitness(C, M, fit):
    if fit == "kind":
        return 50 * C["KIND changes"] + 30 * M["max c_w switches / run"] + 10 * C["KIND runs"] + 5 * M["max post-freeze length"]
    if fit == "wonce":
        return 20 * C["WONCE checks"] + M["max Xi-changes on R / run"]
    if fit == "long":
        return 10 * M["max Xi-changes on R / run"] + 3 * M["max W-changes on R / run"] + M["max post-freeze length"]

def main():
    if sys.argv[1] == "random":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed); C, M = Counter(), Counter(); allbad = []
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
            _, _, bad = evaluate(g, o, f"{seed}:{i}", C, M)
            if bad:
                allbad += bad; FCL.dump(g, os.path.join(HERE, "climb", f"viol_random_{seed}_{i}.pg"))
        for k in sorted(C): print(f"{k:45s} {C[k]}")
        for k in sorted(M): print(f"MAX {k:41s} {M[k]}")
        print("FAILURES (first 20):", allbad[:20]); print("KWCHECK", "PASS" if not allbad else "FAIL"); return
    fit, seed, nmin, nmax, secs = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    rng = random.Random(seed); os.makedirs(os.path.join(HERE, "climb"), exist_ok=True)
    while True:
        g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
        if FCL.ok(g, o): break
    C, M, bad = evaluate(g, o, seed); best = fitness(C, M, fit); bestCM = (C, M)
    tot, totM = Counter(), Counter(); t0 = time.time(); it = acc = 0
    while time.time() - t0 < secs:
        it += 1
        h = FCL.mutate(g, o, rng)
        if not FCL.ok(h, o): continue
        C, M, bad = evaluate(h, o, seed)
        for k, v in C.items(): tot[k] += v
        for k, v in M.items(): totM[k] = max(totM[k], v)
        tot["climb evaluations"] += 1
        if bad:
            FCL.dump(h, os.path.join(HERE, "climb", f"viol_{fit}_{seed}.pg")); print("VIOLATION", bad[:5]); break
        f = fitness(C, M, fit)
        if f >= best:
            if f > best: acc += 1
            g, best, bestCM = h, f, (C, M)
    FCL.dump(g, os.path.join(HERE, "climb", f"best_{fit}_{seed}.pg"))
    print(f"climb FIT={fit} seed={seed} n={g.n} iterations={it} improvements={acc} best_fitness={best}")
    print("BEST counters:", {k: v for k, v in sorted(bestCM[0].items()) if v}); print("BEST maxima:", dict(bestCM[1]))
    for k in sorted(tot): print(f"TOTAL {k:41s} {tot[k]}")
    for k in sorted(totM): print(f"TOTALMAX {k:38s} {totM[k]}")
    print("KWCLIMB", "PASS" if not bad else "FAIL")
if __name__ == "__main__": main()
