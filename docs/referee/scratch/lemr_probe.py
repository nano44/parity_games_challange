#!/usr/bin/env python3
"""REFEREE probe for Lemma R of P-N5-U1 (§1): si.py's Engine.evaluate, with ONE hook inserted after the restriction loop (source of
experiments/si/si.py read at run time, the hook line added before 'dist = {}'; nothing else changed). At every cycle node v with
region R and restricted graph hs, for every optimiser (evaluated-game Odd) vertex x != v in R and every successor y of x in R:
  FULL  y fully optimal (ext(x, val[y]) == val[x], all three components)      => x -> y survives          (Lemma R)
  EXACT survivors y of x with dist[y] == dist[x] - 1                           == the fully optimal set  (Lemma R, 'Hence')
  CP    y with (c, P) of ext(x, val[y]) equal to val[x]'s but length different: counted, and whether it was deleted (the x = u corner)
Usage: lemr_probe.py N nmin nmax seed | lemr_probe.py corner"""
import sys, os, random, inspect, textwrap
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg, si

src = textwrap.dedent(inspect.getsource(si.Engine.evaluate))
assert src.count("dist = {}") == 1
src = src.replace("dist = {}", "self.HOOK(v, R, {x: list(hs[x]) for x in R}, gs); dist = {}", 1)
ns = {}; exec(compile(src, "si_evaluate_hooked", "exec"), si.__dict__, ns)

class HEngine(si.Engine):
    evaluate = ns["evaluate"]
    def HOOK(self, v, R, hs, gs): self.snap.append((v, set(R), hs, gs))

def check(g, strat, cnt):
    E = HEngine(g); E.snap = []; val, tau = E.evaluate(strat)
    for v, R, hs, gs in E.snap:
        for x in R:
            if x == v or g.owner[x] != 1: continue
            succR = [y for y in gs[x] if y in R]
            full = {y for y in succR if E.extend(x, val[y]) == val[x]}
            if not full: cnt["NOFULL"] += 1
            for y in full:
                cnt["FULL_cases"] += 1
                if y not in hs[x]: cnt["FULL_FAIL"] += 1
            d = lambda z: val[z][2]
            surv = {y for y in hs[x] if d(y) == d(x) - 1}
            cnt["EXACT_cases"] += 1
            if surv != full: cnt["EXACT_FAIL"] += 1
            for y in succR:
                e = E.extend(x, val[y])
                if e[:2] == val[x][:2] and e[2] != val[x][2]:
                    cnt["CP_corner"] += 1; cnt["CP_corner_deleted"] += y not in hs[x]
            if tau[x] not in full: cnt["CHOICE_not_full_FAIL"] += 1

def rand_game(rng, lo, hi):
    n = rng.randint(lo, hi); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3, 4)))))) for _ in range(n)]
    return pg.Game([rng.randrange(n + 2) for _ in range(n)], owner, succ)

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "corner":
        # vertices: 0 = c (Even, prio 1, self-loop), 1 = u (Odd optimiser, prio 2), 2 = y (Even forced, prio 0, y -> u); u -> c, u -> y
        g = pg.Game([1, 2, 0], [0, 1, 0], [[0], [0, 2], [1]])
        E = HEngine(g); E.snap = []; val, tau = E.evaluate((0, -1, 1))
        print("val", val, "tau", tau); print("restricted graph after restriction at c:", E.snap[0][2])
        print("ext(u, val[y]) =", E.extend(1, val[2]), " val[u] =", val[1]); check(g, (0, -1, 1), cnt); print(dict(cnt)); sys.exit()
    N, lo, hi, seed = map(int, a[:4]); rng = random.Random(seed)
    for _ in range(N):
        g = rand_game(rng, lo, hi)
        strat = tuple(rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n))
        cnt["games"] += 1; check(g, strat, cnt)
    print(dict(sorted(cnt.items())))
