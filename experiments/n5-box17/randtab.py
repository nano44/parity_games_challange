#!/usr/bin/env python3
"""Box 17 random tables (DATA, NOT exhaustive): COUNT games drawn uniformly from model C(n) (exh17.py; owners, parity pattern and
every successor set uniform; --labelled: also a uniform rank permutation) with random.Random(SEED + n * 1000003 + chunk), every start
pair (exh17.do_game), same Stats as exh17. Usage: randtab.py N COUNT SEED [--labelled] [--maxstarts M] --out FILE.json"""
import argparse, json, multiprocessing as mp, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exh17 as X, pg


def chunk(args):
    n, cnt, seed, labelled, k, maxst = args; rnd = random.Random(seed + n * 1000003 + k); S = X.Stats()
    for _ in range(cnt):
        while True:
            own = [rnd.randint(0, 1) for _ in range(n)]; cp = X.prios([rnd.randint(0, 1) for _ in range(n)])
            perm = list(range(n))
            if labelled: rnd.shuffle(perm)
            succ = []
            for v in range(n):
                m = rnd.randint(1, (1 << n) - 1); succ.append([w for w in range(n) if (m >> w) & 1])
            st = 1
            for s in succ: st *= len(s)
            if st <= maxst: break
        X.do_game(pg.Game([cp[perm[v]] for v in range(n)], own, succ), True, S)
    return S


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("n", type=int); ap.add_argument("count", type=int); ap.add_argument("seed", type=int)
    ap.add_argument("--labelled", action="store_true"); ap.add_argument("--maxstarts", type=int, default=10 ** 9)
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--out", required=True); a = ap.parse_args(); t0 = time.time()
    K = 4 * a.jobs; per = (a.count + K - 1) // K; S = X.Stats()
    with mp.Pool(a.jobs) as pool:
        for s in pool.imap_unordered(chunk, [(a.n, per, a.seed, a.labelled, k, a.maxstarts) for k in range(K)]):
            S.add(s)
            for v in s.viol[:3]: print("VIOLATION", json.dumps(v), flush=True)
    out = dict(model=("L" if a.labelled else "C") + "-random", n=a.n, seed=a.seed, games_drawn=per * K, maxstarts=a.maxstarts, counts=S.c,
               best={k: S.best[k] for k in X.QK if k != "segn"}, hist={k: {str(x): c for x, c in sorted(S.hist[k].items())} for k in X.QK if k != "segn"},
               violations=S.viol, seconds=round(time.time() - t0))
    json.dump(out, open(a.out, "w"), indent=1)
    print("RESULT", json.dumps(dict(n=a.n, model=out["model"], counts=S.c, max={k: (S.best[k][0] if S.best[k] else None) for k in X.QK if k != "segn"}, violations=len(S.viol))))


if __name__ == "__main__":
    main()
