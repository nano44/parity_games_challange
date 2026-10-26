#!/usr/bin/env python3
"""Box 12: exhaustive small-n epoch census (census.analyse on every run), multiprocessing.
Families (canonical: priorities in id order, distinct, parity pattern par, as exh.py's prios):
  1O N   : exh.py's canonical C^1O games (--even-maxdeg 2 --o-deg 2 --no-forced, all o, all parity patterns), S3 start or --all-starts.
  2O N   : canonical C^2O games: two Odd choice vertices {a < b} of out-degree exactly 2, every other vertex Even with 1..2 successors
           (no forced Odd vertex), all parity patterns; S3 start or --all-starts.
Usage: exhk.py 1O|2O N [--all-starts] [--every K --offset J] [--jobs 4] --out FILE.json"""
import argparse
import itertools
import json
import multiprocessing as mp
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "n5-exhaustive"))
import census as C  # noqa: E402
from census import pg  # noqa: E402


def prios(par):
    out, p = [], -1
    for b in par:
        p += 1
        if p % 2 != b:
            p += 1
        out.append(p)
    return out


def subsets(n, lo, hi):
    return [list(c) for k in range(lo, hi + 1) for c in itertools.combinations(range(n), k)]


def games2(n, par):
    pr = prios(par); ev = subsets(n, 1, 2); od = subsets(n, 2, 2)
    for a, b in itertools.combinations(range(n), 2):
        others = [v for v in range(n) if v not in (a, b)]
        for combo in itertools.product(ev, repeat=len(others)):
            owner, succ = [0] * n, [None] * n
            owner[a] = owner[b] = 1
            for v, s in zip(others, combo):
                succ[v] = s
            for sa in od:
                for sb in od:
                    succ[a], succ[b] = sa, sb
                    yield pg.Game(pr, owner, [list(s) for s in succ])


class A1:
    even_maxdeg, o_deg, no_forced = 2, 2, True


def games1(n, o, par):
    import exh
    yield from exh.games(n, o, par, A1)


def allstarts(g):
    ch = [g.succ[v] for v in range(g.n)]
    for pick in itertools.product(*ch):
        yield [pick[v] if g.owner[v] == 0 else -1 for v in range(g.n)], [pick[v] if g.owner[v] == 1 else -1 for v in range(g.n)]


def task(args):
    fam, n, key, all_starts, every, offset = args
    S = C.Stats(); C.VIOL.clear(); gi = 0; ng = 0
    it = games2(n, key) if fam == "2O" else games1(n, key[0], key[1])
    for g in it:
        gi += 1
        if (gi - 1) % every != offset:
            continue
        ng += 1
        for s, t in (allstarts(g) if all_starts else [(None, None)]):
            states, fbs = C.run_states(g, s, t)
            nm = f"{fam}n{n} prio={g.prio} owner={g.owner} succ={g.succ} start={(s, t) if s else 'S3'}"
            C.analyse(g, nm, states, fbs, S)
    S.c["games"] += ng
    return S, list(C.VIOL)


def merge(T, S):
    T.c.update(S.c)
    for k, v in S.mx.items():
        T.mx[k] = max(T.mx.get(k, v), v)
    for k, v in S.top.items():
        T.best(k, *v)
    for d in (0, 1, 2):
        T.len_hist[d].update(S.len_hist[d])
    T.nep_hist.update(S.nep_hist)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fam"); ap.add_argument("n", type=int)
    ap.add_argument("--all-starts", action="store_true"); ap.add_argument("--every", type=int, default=1)
    ap.add_argument("--offset", type=int, default=0); ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    pars = list(itertools.product((0, 1), repeat=a.n))
    keys = pars if a.fam == "2O" else [(o, p) for o in range(a.n) for p in pars]
    tasks = [(a.fam, a.n, k, a.all_starts, a.every, a.offset) for k in keys]
    T = C.Stats(); V = []; t0 = time.time(); done = 0
    with mp.Pool(a.jobs) as pool:
        for S, vv in pool.imap_unordered(task, tasks):
            merge(T, S); V += vv; done += 1
            print(f"task {done}/{len(tasks)} games {T.c['games']} runs {T.c['runs']} viol {len(V)} {time.time() - t0:.0f}s", flush=True)
    rep = dict(counts=dict(T.c), maxima=dict(T.mx), top={k: list(v) for k, v in T.top.items()},
               len_hist={str(k): dict(sorted(v.items())) for k, v in T.len_hist.items()}, nep_hist=dict(sorted(T.nep_hist.items())),
               violations=V[:200], n_violations=len(V), options=vars(a), secs=round(time.time() - t0, 1), tasks_done=f"{done}/{len(tasks)}")
    json.dump(rep, open(a.out, "w"), indent=1, sort_keys=True)
    for k in sorted(T.c):
        print(f"{k}: {T.c[k]}")
    for k in sorted(T.mx):
        print(f"{k}: {T.mx[k]}")
    for k in sorted(T.top):
        print(f"top {k}: {T.top[k][0]} | {T.top[k][1]}")
    for d in (0, 1, 2):
        print(f"len_hist |D|{'>=2' if d == 2 else '=' + str(d)}: " + " ".join(f"{L}:{c}" for L, c in sorted(T.len_hist[d].items())))
    print("nep_hist:", " ".join(f"{k}:{v}" for k, v in sorted(T.nep_hist.items())))
    print("RESULT", "FAIL" if V else "OK", f"violations={len(V)}")


if __name__ == "__main__":
    main()
