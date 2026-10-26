#!/usr/bin/env python3
"""REFEREE succ. 11: hill-climb for two-sided fallbacks (any class), checking every dual_probe check on each candidate.
Score = two-sided fallbacks of the S3 run + random-start runs. Seeds: the lib41 games whose S3 run has one (or random games).
Any *_FAIL is printed and the game saved to dual_logs/. Usage: dual_climb.py SECONDS SEED [start.pg ...]"""
import sys, os, random, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D


def score(g, rng):
    c = Counter(); D.EX.clear()
    starts = [RE.best_reward_start(g), D.rand_start(g, rng)]
    for s in starts:
        try: D.check(g, s, c, "climb", rng)
        except RuntimeError: return -1, c
    return c["two_sided_fb"], c


def mutate(g, rng):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n
    for _ in range(rng.randint(1, 3)):
        v = rng.randrange(n); m = rng.random()
        if m < 0.5:
            if rng.random() < 0.5 and len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
            else: succ[v] = sorted(set(succ[v] + [rng.randrange(n)]))
        elif m < 0.85:
            u = rng.randrange(n); prio[v], prio[u] = prio[u], prio[v]
        else: owner[v] = 1 - owner[v]
    return RE.Game(prio, owner, succ)


def main(a):
    secs, seed = int(a[0]), int(a[1]); rng = random.Random(seed)
    starts = [RE.parse(f) for f in a[2:]]
    fresh = (lambda: rng.choice(starts)) if starts else (lambda: D.rand_ck(rng, rng.randint(6, 14), rng.randint(1, 3)))
    g = fresh(); best, _ = score(g, rng); tot = Counter(); ev = 0; t0 = time.time()
    while time.time() - t0 < secs:
        h = fresh() if rng.random() < 0.02 else mutate(g, rng)
        if h.n > 40: continue
        s, c = score(h, rng); ev += 1
        for k, v in c.items():
            if not k.startswith("max"): tot[k] += v
        f = {k: v for k, v in c.items() if k.endswith("_FAIL")}
        if f:
            p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dual_logs", "fail_%d_%d.pg" % (seed, ev))
            with open(p, "w") as fh:
                fh.write("parity %d;\n" % (h.n - 1))
                for v in range(h.n): fh.write("%d %d %d %s;\n" % (v, h.prio[v], h.owner[v], ",".join(map(str, h.succ[v]))))
            print("FAIL", f, p, D.EX[:3], flush=True)
        if s >= best: g, best = h, s
    tot["evals"] = ev; tot["best"] = best
    for k in sorted(tot): print("%-36s %d" % (k, tot[k]))
    print("FAILS", sum(v for k, v in tot.items() if k.endswith("_FAIL")))


if __name__ == "__main__":
    main(sys.argv[1:])
