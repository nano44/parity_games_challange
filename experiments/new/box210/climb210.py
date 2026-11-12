#!/usr/bin/env python3
"""Box 210 (L-NEW successor 72): hill-climb over small parity games towards long Howard runs (objective: T, then stalls), running every
counter of gen210.py on every game visited. Unsplit game = (prio, own, succ0, start); mutations: a priority, an owner, an edge added /
removed / redirected, a start choice. Restart after RESTART steps without improvement. Even top priority is kept (so H is not empty).
Usage: climb210.py SEED ITERS N0 D   (prints one totals line and the best game's T)"""
import sys, os, random, collections, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gen210
RESTART = 300
def new(rng, n0, d):
    while True:
        prio = [rng.randint(1, d) for _ in range(n0)]
        if max(prio) % 2 == 0: break
    return dict(prio=prio, own=[rng.randrange(2) for _ in range(n0)], succ=[sorted(rng.sample(range(n0), rng.randint(1, min(3, n0)))) for _ in range(n0)], seed=rng.randrange(10 ** 9))
def mutate(g, rng, d):
    g = copy.deepcopy(g); n0 = len(g["prio"]); i = rng.randrange(n0); r = rng.random()
    if r < 0.3:
        old = g["prio"][i]; g["prio"][i] = rng.randint(1, d)
        if max(g["prio"]) % 2: g["prio"][i] = old
    elif r < 0.45: g["own"][i] ^= 1
    elif r < 0.65:
        j = rng.randrange(n0)
        if j not in g["succ"][i]: g["succ"][i] = sorted(g["succ"][i] + [j])
    elif r < 0.8:
        if len(g["succ"][i]) > 1: g["succ"][i].remove(rng.choice(g["succ"][i]))
    elif r < 0.95:
        k = rng.randrange(len(g["succ"][i])); j = rng.randrange(n0)
        if j not in g["succ"][i]: g["succ"][i][k] = j; g["succ"][i].sort()
    else: g["seed"] = rng.randrange(10 ** 9)
    return g
def evaluate(g, tot):
    n, n0, pr, ow, succ = gen210.split(g["prio"], g["own"], g["succ"]); r2 = random.Random(g["seed"]); c = collections.Counter()
    gen210.run(n, n0, pr, ow, succ, [r2.choice(succ[v]) if ow[v] == 0 else -1 for v in range(n)], c, cap=3000)
    for k, v in c.items():
        if k in ("Tmax", "platmax", "tailmax"): tot[k] = max(tot[k], v)
        else: tot[k] += v
    return (c["Tmax"], c["stalls"])
if __name__ == "__main__":
    seed, iters, n0, d = (int(x) for x in sys.argv[1:5]); rng = random.Random(seed); tot = collections.Counter(); best = None; bs = None; since = 0; top = (0, 0)
    for it in range(iters):
        if best is None or since > RESTART: best = new(rng, n0, d); bs = evaluate(best, tot); since = 0; top = max(top, bs); continue
        g = mutate(best, rng, d); s = evaluate(g, tot)
        if s >= bs: since = 0 if s > bs else since + 1; best, bs = g, s
        else: since += 1
        top = max(top, bs)
    print("climb210 seed", seed, "iters", iters, "n0", n0, "d", d, "bestT", top[0], gen210.show(tot), flush=True)
