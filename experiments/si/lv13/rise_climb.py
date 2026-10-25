#!/usr/bin/env python3
"""L-SI succ. 8, box 13 item (3): hill-climb against CONJECTURE RISE-DROP (docs/si/N5-RISE-box13.md): after a rise at j (oldthreat.py's
definition), r_{j+1} <= L whenever j+1 is still in scope. Fitness: 10^6 per rise with S4a and r > L at j+1 (a counterexample, dumped to
logs/risedrop_cex_<seed>.pg, climb stops), 10^4 per rise with rise level < r_j, 100 per rise, + in-scope fallbacks with L >= 0.
Mutations / C^1O filter: REFEREE-2's R2-N5-FRZ/frz_climb.py (read only). Also counts OLD-THREAT failures (any = stop + dump).
Usage: rise_climb.py seed seconds R seed_game.pg"""
import sys, os, random, time
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import oldthreat as OT
sys.path.insert(0, os.path.join(OT.R2, "R2-N5-FRZ")); import frz_climb as FCL

def evaluate(g, o, R, seed):
    C = Counter(); bad = []; rng = random.Random(seed)
    starts = [OT.FC.s3_start(g)] + [OT.RC.rand_start(rng, g) for _ in range(R)]
    for i, (s, t) in enumerate(starts):
        for mode in ("own", "spec"):
            A, fbs = OT.OC.run_trace(g, o, s, t, rng, mode); OT.scan(g, o, A, fbs, C, bad, (i, mode))
            C["fbL"] += sum(1 for k in range(len(fbs)) if fbs[k] and OT.EC.M(A[k]) >= 0)
    f = 10 ** 6 * C["AT_j+1: S4a_with_r>L_at_j+1"] + 10 ** 4 * C["rise_level<r_j"] + 100 * C["rises"] + C["fbL"]
    return f, C, bad

def main():
    seed, secs, R, p = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(seed); g = OT.RC.parse(open(p).read()); o = OT.FC.odd_vertex(g)
    best, C, bad = evaluate(g, o, R, seed); t0 = time.time(); it = 0; tot = Counter(); os.makedirs(os.path.join(HERE, "logs"), exist_ok=True)
    while time.time() - t0 < secs:
        it += 1; h = FCL.mutate(g, o, rng)
        if not FCL.ok(h, o): continue
        f, C2, bad2 = evaluate(h, o, R, seed); tot["evals"] += 1
        for k, v in C2.items(): tot[k] += v
        if bad2 or C2["AT_j+1: S4a_with_r>L_at_j+1"]:
            FCL.dump(h, os.path.join(HERE, "logs", f"risedrop_cex_{seed}.pg")); print("FOUND", dict(C2), bad2[:3]); g, best, C = h, f, C2; break
        if f >= best: g, best, C = h, f, C2
    FCL.dump(g, os.path.join(HERE, "logs", f"rise_best_{seed}.pg"))
    print(f"climb seed={seed} n={g.n} iterations={it} best_fitness={best}")
    print("BEST", dict(sorted(C.items()))); print("ALL-EVALS", dict(sorted(tot.items())))
if __name__ == "__main__": main()
