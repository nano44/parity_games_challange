#!/usr/bin/env python3
"""L-COMP box 24: exhaustive / random tables over model C(n) (box 17 / box 23 exh23.py: same games, same shards), every start pair, of
the W-run length |F| and the root-map quantities of casc.py (returns, CASC, PXR = max returns of one Even X per root, max children of a
RETURN node / a FRESH node, max root-chain depth). Every W-run of every trajectory is a suffix of a maximal ok-chain from a HEAD (exh23.py
docstring). Unlike R*_F, the root-map quantities of a suffix are NOT obviously bounded by those of the whole chain (an entry that is a
return in the chain can be fresh in the suffix), so EVERY suffix of every head chain with >= 2 transitions is analysed (a W-run with < 2
transitions has no return).
Usage: exh24.py N [--every K --offset J] [--random K --seed S] [--maxstates M] [--jobs P] --out FILE.json"""
import argparse
import itertools
import json
import multiprocessing as mp
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "n5-box23"))
import casc  # noqa: E402
import rstar  # noqa: E402
import pg  # noqa: E402
from exh23 import game_iter, rand_games  # noqa: E402

QK = ("F", "returns", "casc", "pxr", "kids_ret", "kids_fresh", "maxdepth")


class Stats:
    def __init__(self):
        self.c = dict(games=0, states=0, heads=0, suffixes=0, with_return=0, bad=0)
        self.best = {k: None for k in QK}
        self.hist = {k: {} for k in QK}

    def add(self, o):
        for k, v in o.c.items():
            self.c[k] += v
        for k in QK:
            if o.best[k] is not None and (self.best[k] is None or o.best[k][0] > self.best[k][0]):
                self.best[k] = o.best[k]
            for x, c in o.hist[k].items():
                self.hist[k][x] = self.hist[k].get(x, 0) + c


def do_game(g, S):
    n = g.n; e = rstar.Eng(g); S.c["games"] += 1
    sts = [(tuple(p[v] if g.owner[v] == 0 else -1 for v in range(n)), tuple(p[v] if g.owner[v] == 1 else -1 for v in range(n)))
           for p in itertools.product(*g.succ)]
    lw, nxt = {}, {}
    for x in sts:
        lw[x] = tuple(v[0] for v in e.wval(*x)); nxt[x] = e.step(*x)
    S.c["states"] += len(sts)
    okn = {}
    for x in sts:
        nx = nxt[x]
        if nx is not None:
            y = (nx[0], nx[1])
            if y[1] == x[1] and not nx[2] and lw[y] == lw[x]:
                okn[x] = y
    tgt = set(okn.values()); XS = {}
    for h in okn:
        if h in tgt:
            continue
        S.c["heads"] += 1; ch = [h]
        while ch[-1] in okn:
            ch.append(okn[ch[-1]])
            if len(ch) > len(sts) + 1:
                raise RuntimeError("ok-cycle")
        L = len(ch) - 1
        S.c["suffixes"] += L
        S.hist["F"][L] = S.hist["F"].get(L, 0) + 1
        if S.best["F"] is None or L > S.best["F"][0]:
            S.best["F"] = (L, dict(prio=g.prio, owner=g.owner, succ=g.succ, start=[list(h[0]), list(h[1])]))
        if L < 2:
            continue
        for x in ch:
            if x not in XS:
                XS[x] = e.N.SG.evaluate_choice(list(x[0]))
        XI = [XS[x][0] for x in ch]; SB = [XS[x][1] for x in ch]
        for a in range(0, L - 1):                       # every suffix [a, L] with >= 2 transitions
            r = casc.analyse_run(e, ch, XI, SB, a, L)
            S.c["bad"] += sum(r["bad"].values())
            if r["returns"] == 0:
                continue
            S.c["with_return"] += 1
            for k in QK[1:]:
                S.hist[k][r[k]] = S.hist[k].get(r[k], 0) + 1
                if S.best[k] is None or r[k] > S.best[k][0]:
                    S.best[k] = (r[k], dict(prio=g.prio, owner=g.owner, succ=g.succ, start=[list(ch[a][0]), list(ch[a][1])], F=L - a))


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
    ap.add_argument("--split", type=int, default=1); ap.add_argument("--random", type=int, default=0); ap.add_argument("--seed", type=int, default=24)
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
            print(f"progress {i + 1}/{len(jobs)} games {S.c['games']} states {S.c['states']} max " +
                  " ".join(f"{k} {S.best[k] and S.best[k][0]}" for k in QK) + f" {time.time() - t0:.0f}s", flush=True)
    out = dict(model="C", n=a.n, maxdeg=a.maxdeg, random=a.random, seed=a.seed if a.random else None, maxstates=a.maxstates,
               every=a.every, offset=a.offset, counts=S.c, best=S.best,
               hist={k: {str(x): c for x, c in sorted(S.hist[k].items())} for k in QK}, seconds=round(time.time() - t0))
    json.dump(out, open(a.out, "w"), indent=1)
    print("RESULT", json.dumps(dict(n=a.n, random=a.random, counts=S.c, max={k: (S.best[k][0] if S.best[k] else None) for k in QK})))


if __name__ == "__main__":
    main()
