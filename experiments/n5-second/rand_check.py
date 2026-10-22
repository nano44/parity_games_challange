#!/usr/bin/env python3
"""n5b.py on a seeded random corpus (harness/gen.py corpus): regions vs Oink zlk (tl if zlk fails) AND the independent
Python Zielonka (harness/zielonka.py); both players' strategies through harness/verify.py; iterations and fallbacks recorded
per game with the game's sha1, so L-NEW can run its n5.py on the same files and compare counts.
Usage: rand_check.py DIR --csv OUT.csv [--jobs 4] [--timeout 300] [--mode orig|spec]"""
import sys, os, csv, hashlib, argparse, signal, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify, zielonka, compare, n5b
from cmp_family import reference

FIELDS = ["game", "n", "m", "sha1", "n5b_iterations", "n5b_fallbacks", "ref", "secs", "status", "detail"]


class TO(Exception):
    pass


def _alarm(*_):
    raise TO()


def one(a):
    gp, timeout = a
    text = open(gp).read(); g = pg.parse(text)
    row = dict(game=os.path.basename(gp), n=g.n, m=g.m, sha1=hashlib.sha1(text.encode()).hexdigest())
    signal.signal(signal.SIGALRM, _alarm); signal.alarm(timeout); t0 = time.perf_counter()
    try:
        win, strat, it, fb = n5b.N5(g).run()
    except TO:
        return dict(row, status="timeout")
    except n5b.RepeatedState as e:
        signal.alarm(0); return dict(row, status="INCOMPLETE", detail=str(e))
    signal.alarm(0)
    refname, ref = reference(gp, g)
    zl = zielonka.solve(g)
    errs = verify.check(g, win, strat); bad = []
    if ref is not None and win != ref:
        bad.append("REGION vs Oink")
    if win != zl:
        bad.append("REGION vs py-zlk")
    if errs:
        bad.append("STRATEGY " + "; ".join(errs[:2]))
    return dict(row, n5b_iterations=it, n5b_fallbacks=fb, ref=refname, secs=f"{time.perf_counter() - t0:.2f}",
                status="INCORRECT" if bad else "ok", detail="; ".join(bad))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("dir"); ap.add_argument("--csv", required=True)
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--mode", default="orig", choices=["orig", "spec"])
    a = ap.parse_args()
    n5b.MODE = a.mode
    sys.setrecursionlimit(1000000)
    games = list(compare.games_of([a.dir]))
    rows = []
    with Pool(a.jobs) as p:
        for r in p.imap(one, [(gp, a.timeout) for gp in games], chunksize=4):
            if r["status"] != "ok":
                print("!!", r, flush=True)
            rows.append(r)
    with open(a.csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    from collections import Counter
    ok = [r for r in rows if r["status"] == "ok"]
    print(f"rand_check: {len(rows)} games {dict(Counter(r['status'] for r in rows))}; max iterations "
          f"{max((int(r['n5b_iterations']) for r in ok), default=0)}; fallbacks total {sum(int(r['n5b_fallbacks']) for r in ok)}")


if __name__ == "__main__":
    main()
