#!/usr/bin/env python3
"""L-COMP box 23 (b): exhaustive / random tables of R*_F and FL_F per W-run of N5 (rstar.py definitions), over ALL start pairs.

Models (box 17's, experiments/n5-box17/exh17.py; README there states the assumptions): C(n) = ids in rank order, distinct minimal
priorities for each parity pattern, owners free, every nonempty successor set (self-loops allowed). Priorities matter only through
(Ω, id)-rank and parity (box 17 privar.py, 0 differences on 6,000 runs).
--maxdeg D restricts successor sets to size <= D. --random K draws K games uniformly from the model (seed --seed) instead of all.
Per game every state (σ, τ) (every positional pair) is a start. A transition x -> x' is "ok" (stays inside a W-run) iff τ' = τ, it is not
an S4c fallback, and λ_W(x') = λ_W(x). Every trajectory's W-run is a suffix of a maximal ok-chain from a HEAD (a state with an ok
out-edge and no ok in-edge); R*_F and FL_F of a suffix are at most those of the whole chain (its blocked sets and adoptions are
subsets), so the maxima over all start pairs are the maxima over the chains from heads, which is what is enumerated.
Usage: exh23.py N [--maxdeg D] [--every K --offset J] [--random K --seed S] [--maxstates M] [--jobs P] --out FILE.json"""
import argparse
import itertools
import json
import multiprocessing as mp
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rstar  # noqa: E402  (puts n5-box17, n5-second on the path)
import pg  # noqa: E402
from exh17 import prios  # noqa: E402

QK = ("rs", "fl", "F", "la", "sig0")


class Stats:
    def __init__(self):
        self.c = dict(games=0, states=0, heads=0, chains_rs_pos=0, chains_fl_pos=0, viol_freered=0, incl_ne_strict=0)
        self.best = {k: None for k in QK}
        self.hist = {k: {} for k in QK}

    def add(self, o):
        for k, v in o.c.items():
            self.c[k] = self.c.get(k, 0) + v
        for k in QK:
            if o.best[k] is not None and (self.best[k] is None or o.best[k][0] > self.best[k][0]):
                self.best[k] = o.best[k]
            for x, c in o.hist[k].items():
                self.hist[k][x] = self.hist[k].get(x, 0) + c


def game_iter(n, maxdeg, every, offset, shard):
    subs = [m for m in range(1, 1 << n) if bin(m).count("1") <= maxdeg]; gi = 0
    own = [(shard >> v) & 1 for v in range(n)]
    for parm in range(1 << n):
        pr = prios([(parm >> r) & 1 for r in range(n)])
        for masks in itertools.product(subs, repeat=n):
            gi += 1
            if (gi - 1) % every != offset:
                continue
            yield pg.Game(pr, own, [[w for w in range(n) if (m >> w) & 1] for m in masks])


def rand_games(n, maxdeg, k, seed, maxstates):
    R = random.Random(seed); out = []
    while len(out) < k:
        succ = [sorted(R.sample(range(n), R.randint(1, min(maxdeg, n)))) for _ in range(n)]
        if maxstates and eval("*".join(str(len(s)) for s in succ)) > maxstates:
            continue
        out.append(pg.Game(prios([R.randint(0, 1) for _ in range(n)]), [R.randint(0, 1) for _ in range(n)], succ))
    return out


def do_game(g, S):
    n = g.n; e = rstar.Eng(g); S.c["games"] += 1
    sts = [(tuple(p[v] if g.owner[v] == 0 else -1 for v in range(n)), tuple(p[v] if g.owner[v] == 1 else -1 for v in range(n)))
           for p in itertools.product(*g.succ)]
    D = {x: (e.sdata(*x), e.step(*x)) for x in sts}; S.c["states"] += len(sts)
    okn = {}
    for x, (d, nx) in D.items():
        if nx is not None:
            y = (nx[0], nx[1])
            if y[1] == x[1] and not nx[2] and D[y][0]["lw"] == d["lw"]:
                okn[x] = y
    tgt = set(okn.values())
    for h in okn:
        if h in tgt:
            continue
        S.c["heads"] += 1; ch = [h]; seen = {h}
        while ch[-1] in okn:
            y = okn[ch[-1]]
            if y in seen:
                raise RuntimeError("ok-cycle " + str(y))
            seen.add(y); ch.append(y)
        r = rstar.measure(e, ch, [D[x][0] for x in ch], 0, len(ch) - 1)
        S.c["chains_rs_pos"] += r["rs"] > 0; S.c["chains_fl_pos"] += r["fl"] > 0
        S.c["viol_freered"] += r["F"] > (n - 1) * (r["rs"] + 1) + r["fl"]; S.c["incl_ne_strict"] += r["ri"] != r["rs"]
        for k in QK:
            S.hist[k][r[k]] = S.hist[k].get(r[k], 0) + 1
            if S.best[k] is None or r[k] > S.best[k][0]:
                S.best[k] = (r[k], dict(prio=g.prio, owner=g.owner, succ=g.succ, start=[list(h[0]), list(h[1])], F=r["F"]))


def task(args):
    S = Stats()
    if args[0] == "exh":
        _, n, maxdeg, every, offset, shard = args
        for g in game_iter(n, maxdeg, every, offset, shard):
            do_game(g, S)
    else:
        for g in args[1]:
            do_game(pg.Game(*g), S)
    return S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("--maxdeg", type=int, default=99)
    ap.add_argument("--every", type=int, default=1); ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--split", type=int, default=1); ap.add_argument("--random", type=int, default=0); ap.add_argument("--seed", type=int, default=23)
    ap.add_argument("--maxstates", type=int, default=0); ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--out", required=True)
    a = ap.parse_args(); t0 = time.time()
    if a.random:
        gs = [(g.prio, g.owner, g.succ) for g in rand_games(a.n, a.maxdeg, a.random, a.seed, a.maxstates)]
        jobs = [("rand", gs[i::64]) for i in range(64)]
    else:
        jobs = [("exh", a.n, a.maxdeg, a.every * a.split, a.offset * a.split + k, sh) for sh in range(1 << a.n) for k in range(a.split)]
    S = Stats()
    with mp.Pool(a.jobs) as pool:
        for i, s in enumerate(pool.imap_unordered(task, jobs)):
            S.add(s)
            print(f"progress {i + 1}/{len(jobs)} games {S.c['games']} states {S.c['states']} max rs {S.best['rs'] and S.best['rs'][0]} "
                  f"fl {S.best['fl'] and S.best['fl'][0]} {time.time() - t0:.0f}s", flush=True)
    out = dict(model="C", n=a.n, maxdeg=a.maxdeg, random=a.random, seed=a.seed if a.random else None, maxstates=a.maxstates,
               every=a.every, offset=a.offset, counts=S.c, best=S.best,
               hist={k: {str(x): c for x, c in sorted(S.hist[k].items())} for k in QK}, seconds=round(time.time() - t0))
    json.dump(out, open(a.out, "w"), indent=1)
    print("RESULT", json.dumps(dict(n=a.n, maxdeg=a.maxdeg, random=a.random, counts=S.c,
                                    max={k: (S.best[k][0] if S.best[k] else None) for k in QK})))


if __name__ == "__main__":
    main()
