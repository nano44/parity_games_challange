#!/usr/bin/env python3
"""Validation of experiments/red/vj.py (L-RED):
  1. evaluate() == evaluate_bf() (pointwise minimum over ALL positional counterstrategies) on random games;
  2. final regions == harness zielonka.solve and strategies pass harness verify.check;
  3. MSF/LSF iteration counts and the switch sequence == L-SI's si.py (path given by --lsi DIR, read-only) on random games.
Usage: xcheck.py [--games N] [--nmax 8] [--lsi DIR] [--seed S]"""
import sys, os, random, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import vj, pg, zielonka, verify
ODD = vj.ODD
ap = argparse.ArgumentParser(); ap.add_argument("--games", type=int, default=2000); ap.add_argument("--nmax", type=int, default=8)
ap.add_argument("--lsi", default=""); ap.add_argument("--seed", type=int, default=0); ap.add_argument("--bfmax", type=int, default=7)
a = ap.parse_args()
rng = random.Random(a.seed)
si = None
if a.lsi:
    sys.path.insert(0, os.path.join(a.lsi, "experiments", "si")); import si
bad = {"bf": 0, "zlk": 0, "strat": 0, "lsi_iters": 0, "lsi_vals": 0}; nbf = 0; nlsi = 0; tot_it = 0
for gi in range(a.games):
    n = rng.randint(2, a.nmax)
    prio = [rng.randrange(n + 2) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(n, 3)))) for _ in range(n)]
    e = vj.VJ(prio, owner, succ); g = pg.Game(prio, owner, succ)
    for rule in ("msf", "lsf"):
        for start in ("best", "first"):
            sigma = e.initial(start)
            seq = []
            s, it, st = e.run(rule, sigma, hook=lambda it, sg, val, tau, v, w, lv, c, ch: seq.append((v, w)))
            tot_it += it
            win, strat = e.regions(s)
            ref = zielonka.solve(g)
            if list(win) != list(ref):
                bad["zlk"] += 1; print("ZLK MISMATCH", pg.dumps(g), rule, start)
            errs = verify.check(g, win, strat)
            if errs:
                bad["strat"] += 1; print("BAD STRATEGY", pg.dumps(g), rule, start, errs[:2])
            if si:
                es = si.Engine(g); ss = es.initial(start); seq2 = []; it2 = 0
                while True:
                    val, _ = es.evaluate(ss); imp = es.improving(ss, val)
                    if not imp: break
                    new = si.RULES[rule](es)(ss, val, imp, None)
                    v = [i for i in range(n) if new[i] != ss[i]][0]; seq2.append((v, new[v])); ss = new; it2 += 1
                nlsi += 1
                if seq != seq2:
                    bad["lsi_iters"] += 1; print("LSI SEQUENCE MISMATCH", pg.dumps(g), rule, start, seq, seq2)
    # brute-force valuation check on a few strategies per small game
    if n <= a.bfmax:
        for _ in range(3):
            sigma = tuple(-1 if owner[v] == ODD else rng.choice(succ[v]) for v in range(n))
            val, tau = e.evaluate(sigma); bf = e.evaluate_bf(sigma); nbf += 1
            if [e.key(x) for x in val] != [e.key(x) for x in bf]:
                bad["bf"] += 1; print("BF MISMATCH", pg.dumps(g), sigma, val, bf)
            # tau must realise val: play under (sigma, tau) gives exactly val
            tau2 = [tau[v] if owner[v] == ODD else None for v in range(n)]
            pv = [e.play_value(sigma, tau2, v) for v in range(n)]
            if [e.key(x) for x in pv] != [e.key(x) for x in val]:
                bad["bf"] += 1; print("TAU DOES NOT REALISE VAL", pg.dumps(g), sigma, val, pv)
            if si:
                es = si.Engine(g); v2, _ = es.evaluate(sigma)
                if [es.key(x) for x in v2] != [e.key(x) for x in val]:
                    bad["lsi_vals"] += 1; print("LSI VALUATION MISMATCH", pg.dumps(g), sigma, val, v2)
print(f"games {a.games}, runs {4 * a.games} ({tot_it} switches), brute-force valuation checks {nbf}, si.py run comparisons {nlsi}: mismatches {bad}")
sys.exit(1 if any(bad.values()) else 0)
