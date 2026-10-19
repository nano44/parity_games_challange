#!/usr/bin/env python3
"""Box 8 item (4): n5.py (mode n5, best-reward start) on L-COMP's 2,000-game corpus (harness/gen.py corpus DIR 2000 20261018
--nmin 1 --nmax 120). Per game: sha1, iterations, fallbacks; regions checked against harness Zielonka and both strategies through
harness/verify.py; counts compared with L-COMP's n5b spec / orig CSVs (claude/l-comp experiments/n5-second/results/random_*.csv).
Usage: rand2k_cmp.py DIR spec.csv orig.csv OUT.csv [--jobs 2]"""
import sys, os, csv, hashlib
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, verify, n5
def one(p):
    text = open(p).read(); g = pg.parse(text); it, fb, win, ws, ev = n5.run(g, "n5")
    zw, _ = zielonka.solve_with_strategy(g); errs = verify.check(g, win, ws)
    return os.path.basename(p), hashlib.sha1(text.encode()).hexdigest(), g.n, it, fb, int(list(win) == list(zw)), len(errs)
if __name__ == "__main__":
    d, spec, orig, out = sys.argv[1:5]; jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 2
    S = {r['game']: r for r in csv.DictReader(open(spec))}; O = {r['game']: r for r in csv.DictReader(open(orig))}
    files = sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".pg"))
    with Pool(jobs) as P, open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["game", "sha1", "n", "n5_iterations", "n5_fallbacks", "regions_eq_zielonka", "verify_errors",
                                        "sha1_eq_lcomp", "spec_iterations", "spec_fallbacks", "orig_iterations", "orig_fallbacks"])
        for r in P.imap(one, files, chunksize=4):
            s, o = S[r[0]], O[r[0]]
            w.writerow(list(r) + [int(r[1] == s['sha1']), s['n5b_iterations'], s['n5b_fallbacks'], o['n5b_iterations'], o['n5b_fallbacks']]); f.flush()
