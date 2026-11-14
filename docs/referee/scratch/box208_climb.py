#!/usr/bin/env python3
"""REFEREE s32: adversarial climb for box 208. Hill-climbs genomes (own mutate() of box208_replay) to long IDEAL-CYC runs / many stalls
/ long plateaus, running EVERY must-be-0 counter of box208_replay.one() on every genome visited. Prints, per seed: evaluations, the
best objective reached, and the sum of all must-be-0 counters over all genomes visited.
usage: box208_climb.py OBJ(T|stalls|maxplat) SEED RESTARTS ITERS FAMILY(tiny|noX|big|rand)"""
import sys, os, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import box208_replay as B, end_replay
obj, seed, restarts, iters, fam = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
g = random.Random(seed); rng = random.Random(seed + 1); tot = B.Ctr(); evals = 0; best_overall = (-1, None)
def score(G):
    global evals
    c = B.Ctr(); B.one("climb", G, c, rng, verbose=False); evals += 1
    for k in B.MUST0: tot.inc(k, c.get(k, 0))
    bad = sum(c.get(k, 0) for k in B.MUST0)
    val = {"T": c.get("maxT", 0), "stalls": c.get("stalls", 0), "maxplat": c.get("maxplat", 0)}[obj]
    return val, bad, c.get("maxT", 0)
for r in range(restarts):
    G = B.own_gen(g, fam) if fam in ("tiny", "noX", "big") else end_replay.gen(g, fam)
    cur, bad, T = score(G)
    for i in range(iters):
        H = B.mutate(G, g, g.randint(1, 3)); v, bad, T = score(H)
        if bad:
            fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "box208_logs", "CLIMB_FAIL_%s_%d_%d_%d.json" % (obj, seed, r, i))
            json.dump(H, open(fn, "w")); print("FAIL: a must-be-0 counter fired; genome saved to", fn)
        if v >= cur: G, cur = H, v
    if cur > best_overall[0]: best_overall = (cur, G)
    print("restart %d: best %s %d (N %d, M %d)" % (r, obj, cur, G["N"], sum(len(o) for o in G["opts"])))
print("objective %s family %s seed %d: evaluations %d, best %d, sum of the %d must-be-0 counters over all genomes visited: %d" %
      (obj, fam, seed, evals, best_overall[0], len(B.MUST0), sum(tot.get(k, 0) for k in B.MUST0)))
fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "box208_logs", "climb_best_%s_%s_%d.json" % (obj, fam, seed))
json.dump(best_overall[1], open(fn, "w"))
