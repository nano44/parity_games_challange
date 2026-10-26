#!/usr/bin/env python3
"""REFEREE succ. 15: hill climb for a G-interval (P-N5-ROOT-add §1.1) that outlives its freeze window, i.e. (e - s) - (|E_s| - 1) > 0, so that
FREEZE-G (b)'s freeze, (c) and RELAY-PIECE are exercised. Fitness = root_probe's FRGX_max_excess over S3 + RS random starts (own engine; every
root_probe check runs on every candidate, so a failure would surface). Usage: frg_climb.py seed iters nmin nmax outprefix"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, root_probe as RP


def fitness(g, rs):
    cnt = Counter(); r = random.Random(7)
    starts = [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(rs)]
    for s0 in starts:
        try: RP.analyse(g, s0, cnt, "c")
        except RuntimeError: return -99, cnt
    fails = sum(v for k, v in cnt.items() if k.endswith("_FAIL"))
    if fails: return 999, cnt
    return (cnt["FRGX_max_excess"] - 1000) if cnt["FRGX_max_excess"] else -99, cnt


def mutate(g, rng):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; k = rng.randrange(4)
    v = rng.randrange(n)
    if k == 0: prio[v] = rng.choice([p for p in range(2 * n + 2) if p not in prio] or [prio[v]])
    elif k == 1: owner[v] = 1 - owner[v]
    elif k == 2:
        w = rng.randrange(n)
        if w not in succ[v]: succ[v].append(w)
    else:
        if len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
    return RE.Game(prio, owner, succ)


def write(g, path):
    with open(path, "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))


def main(a):
    seed, iters, lo, hi, out = int(a[0]), int(a[1]), int(a[2]), int(a[3]), a[4]
    rng = random.Random(seed); rs = int(os.environ.get("RS", "6"))
    g = D.rand_ck(rng, rng.randint(lo, hi), rng.randint(1, 4)); fg, _ = fitness(g, rs); best = fg
    for it in range(iters):
        h = mutate(g, rng)
        if not (lo <= h.n <= hi): continue
        fh, cnt = fitness(h, rs)
        if fh == 999:
            write(h, out + "_FAIL.pg"); print("FAILURE", it, {k: v for k, v in cnt.items() if k.endswith("_FAIL")}, flush=True); return
        if fh >= fg:
            g, fg = h, fh
            if fg > best: best = fg; write(g, out + "_best.pg"); print("it", it, "excess", fg, flush=True)
        if it % 500 == 0 and fg < best - 3:   # restart
            g = D.rand_ck(rng, rng.randint(lo, hi), rng.randint(1, 4)); fg, _ = fitness(g, rs)
    print("done best", best, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
