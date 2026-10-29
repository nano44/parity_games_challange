#!/usr/bin/env python3
"""L-COMP box 17: exhaustive tables of the four L-SI quantities over ALL games of a model, from ALL start pairs (or S3 only).

Model C(n) (canonical): vertices 0..n-1; owner Even/Odd free; priorities distinct, increasing in the vertex id, minimal values for the
parity pattern (rank r has parity par[r]); every vertex has a nonempty successor set (any subset of V, self-loops allowed, no multi-edges).
Games: 2^n owners x 2^n parity patterns x (2^n - 1)^n successor sets; no further dedup (see README: N5 depends on ids only through its
tie-breaks, and with ids in rank order no relabelling preserves the rank order, so C(n) has no nontrivial symmetry to quotient).
Model L(n) (--labelled): as C(n) but the rank order is any permutation of the ids (vertex v gets the canonical priority of rank perm[v]):
every game with arbitrary priorities is Engine-equivalent to one of these (N5 reads priorities through (Omega, id)-rank and parity).
Start pairs: every (sigma0, tau0), i.e. prod_v |succ(v)| (--all-starts), or the S3 start. Each state's step and data are computed once
per game (all start pairs are states), then every start's trajectory is analysed (box17.analyse).
Usage: exh17.py N [--labelled] [--all-starts] [--every K --offset J] [--jobs P] --out FILE.json"""
import argparse
import itertools
import json
import multiprocessing as mp
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import box17 as B  # noqa: E402
import pg  # noqa: E402

QK = ("exc", "seg", "segn", "gap", "f")


def prios(par):
    out, p = [], -1
    for b in par:
        p += 1
        if p % 2 != b:
            p += 1
        out.append(p)
    return out


def enc(g, st):
    return dict(prio=g.prio, owner=g.owner, succ=g.succ, start=None if st is None else [list(st[0]), list(st[1])])


class Stats:
    def __init__(self):
        self.c = dict(games=0, runs=0, starts=0, trajs_with_run=0, phases=0, segs=0, gaps=0, states=0)
        self.best = {k: None for k in QK}         # (value, instance, place)
        self.viol = []
        self.hist = {k: {} for k in QK}

    def add(self, other):
        for k, v in other.c.items():
            self.c[k] = self.c.get(k, 0) + v
        for k in QK:
            o = other.best[k]
            if o is not None and (self.best[k] is None or o[0] > self.best[k][0]):
                self.best[k] = o
            for x, c in other.hist[k].items():
                self.hist[k][x] = self.hist[k].get(x, 0) + c
        self.viol += other.viol[: max(0, 50 - len(self.viol))]

    def put(self, k, val, inst, place):
        self.hist[k][val] = self.hist[k].get(val, 0) + 1
        if self.best[k] is None or val > self.best[k][0]:
            self.best[k] = (val, inst, place)


def games(n, labelled, every, offset, shard):
    """the games of shard (owner pattern index) with global index % every == offset."""
    subs = list(range(1, 1 << n)); gi = 0
    owners = [[(o >> v) & 1 for v in range(n)] for o in range(1 << n)]
    perms = list(itertools.permutations(range(n))) if labelled else [tuple(range(n))]
    own = owners[shard]
    for parm in range(1 << n):
        par = [(parm >> r) & 1 for r in range(n)]; cp = prios(par)
        for perm in perms:
            pr = [cp[perm[v]] for v in range(n)]
            for masks in itertools.product(subs, repeat=n):
                gi += 1
                if (gi - 1) % every != offset:
                    continue
                succ = [[w for w in range(n) if (m >> w) & 1] for m in masks]
                yield pg.Game(pr, own, succ)


def task(args):
    n, labelled, all_starts, every, offset, shard = args
    S = Stats()
    for g in games(n, labelled, every, offset, shard):
        do_game(g, all_starts, S)
    return S


def do_game(g, all_starts, S):
        n = g.n; S.c["games"] += 1; e = B.Eng(g); cache = {}
        if all_starts:
            starts = [(tuple(p[v] if g.owner[v] == 0 else -1 for v in range(n)), tuple(p[v] if g.owner[v] == 1 else -1 for v in range(n)))
                      for p in itertools.product(*g.succ)]
        else:
            starts = [e.start()]
        for st in starts:
            S.c["starts"] += 1
            R = B.trajectory(e, st, cache); a = B.analyse(e, R)
            S.c["runs"] += a["runs"]; S.c["phases"] += a["phases"]; S.c["segs"] += a["segs"]; S.c["gaps"] += a["gaps"]
            inst = enc(g, st if all_starts else None)
            if a["phases"]:
                S.put("f", a["f"], inst, a["f_at"])
                if a["f"] > n:
                    S.viol.append(("FB-LIN", a["f"], inst, a["f_at"]))
            if a["runs"]:
                S.c["trajs_with_run"] += 1
                S.put("seg", a["seg"], inst, a["seg_at"]); S.put("gap", a["gap"], inst, a["gap_at"])
                if a["gap"] > n - 1:
                    S.viol.append(("L-WAVE'", a["gap"], inst, a["gap_at"]))
            if a["exc"] is not None:
                S.put("exc", a["exc"], inst, a["exc_at"])
                if a["exc"] > 0:
                    S.viol.append(("SEG-COUNT", a["exc"], inst, a["exc_at"]))
        S.c["states"] += len(cache)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("--labelled", action="store_true"); ap.add_argument("--all-starts", action="store_true")
    ap.add_argument("--every", type=int, default=1); ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--split", type=int, default=1, help="sub-shards per owner pattern (parallelism)")
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--out", required=True)
    a = ap.parse_args(); t0 = time.time()
    jobs = [(a.n, a.labelled, a.all_starts, a.every * a.split, a.offset * a.split + k, sh) for sh in range(1 << a.n) for k in range(a.split)]
    S = Stats()
    with mp.Pool(a.jobs) as pool:
        for i, s in enumerate(pool.imap_unordered(task, jobs)):
            S.add(s)
            for v in s.viol[:3]:
                print("VIOLATION", json.dumps(v), flush=True)
            print(f"progress {i + 1}/{len(jobs)} games {S.c['games']} starts {S.c['starts']} {time.time() - t0:.0f}s", flush=True)
    out = dict(model=("L" if a.labelled else "C"), n=a.n, all_starts=a.all_starts, every=a.every, offset=a.offset, counts=S.c,
               best={k: S.best[k] for k in QK if k != "segn"}, hist={k: {str(x): c for x, c in sorted(S.hist[k].items())} for k in QK if k != "segn"},
               violations=S.viol, seconds=round(time.time() - t0))
    json.dump(out, open(a.out, "w"), indent=1)
    print("RESULT", json.dumps(dict(n=a.n, model=out["model"], all_starts=a.all_starts, counts=S.c,
                                    max={k: (S.best[k][0] if S.best[k] else None) for k in QK if k != "segn"}, violations=len(S.viol))))


if __name__ == "__main__":
    main()
