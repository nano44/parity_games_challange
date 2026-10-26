#!/usr/bin/env python3
"""L-SI succ. 10 (Lead 00:51Z item (2)): DATA for P-N5-1O's honest limits. Observed N5 iterations on C^1O games against n.
N5 = experiments/new/n5.py run() (SPEC; read-only import), from the S3 start and K random start pairs.
Corpus: lib41 (experiments/new/box41/lib41.txt, C^1O files only) and random o-cyclic C^1O games (REFEREE-2's RC.rand_game, read-only).
Prints per-n maxima and a least-squares fit of log(max ITER) on log n. Usage: iters.py lib K seed | rand N nmin nmax K seed"""
import sys, os, random, math
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(ROOT, "experiments", "new")); sys.path.insert(0, os.path.join(ROOT, "docs", "referee-2", "R2-N5-RE"))
import n5, pg
import re_check as RC

def one_odd(g):
    od = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    return od[0] if len(od) == 1 else None

def runs(g, K, rng):
    out = [n5.run(g, "n5")[0]]
    for _ in range(K):
        s = {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}
        t = {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}
        out.append(n5.run(g, "n5", (s, t))[0])
    return out

def fit(pts):
    xs = [math.log(n) for n, it in pts if it > 0 and n > 1]; ys = [math.log(it) for n, it in pts if it > 0 and n > 1]
    if len(xs) < 2: return None
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else None

def main():
    mode = sys.argv[1]; best = defaultdict(int); allp = []; cnt = 0
    if mode == "lib":
        K, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
        for f in open(os.path.join(ROOT, "experiments", "new", "box41", "lib41.txt")):
            f = f.strip(); p = f if os.path.exists(f) else os.path.join(ROOT, f)
            try: g = pg.parse("".join(l for l in open(p) if not l.lstrip().startswith("%")))
            except Exception: continue
            if one_odd(g) is None: continue
            for it in runs(g, K, rng): best[g.n] = max(best[g.n], it); allp.append((g.n, it)); cnt += 1
    else:
        N, nmin, nmax, K, seed = map(int, sys.argv[2:7]); rng = random.Random(seed)
        for i in range(N):
            gg, o = RC.rand_game(rng, rng.randint(nmin, nmax))
            g = pg.Game(list(gg.prio), list(gg.owner), [list(s) for s in gg.succ])
            for it in runs(g, K, rng): best[g.n] = max(best[g.n], it); allp.append((g.n, it)); cnt += 1
    print(f"runs {cnt}, distinct n {len(best)}")
    for n in sorted(best): print(f"n {n:4d}  max ITER {best[n]:4d}  max ITER / n {best[n] / n:.2f}")
    mpts = sorted(best.items())
    print(f"fit log(max ITER per n) ~ e*log n: e = {fit(mpts):.3f}" if fit(mpts) is not None else "fit: n/a")
    print(f"fit log(ITER) over all runs: e = {fit(allp):.3f}" if fit(allp) is not None else "")
    print(f"max ITER / n overall: {max(it / n for n, it in mpts):.2f};  max ITER / n^2: {max(it / n**2 for n, it in mpts):.3f}")
if __name__ == "__main__": main()
