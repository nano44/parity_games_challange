#!/usr/bin/env python3
"""L-NEW box 53: REVERSE PAIRS in an N5 run: transitions t < t' whose (sigma, tau) edge-bit changes are exact opposites (Delta_t = -Delta_t',
Delta = the change of the edge indicators [sigma(v) = w], [tau(v) = w]). Each one is a 2-transition Farkas circuit (y = (1, 1)): the game has
NO linear and no lexicographic-linear ranking function over the edge bits (T42 section 3's encoding), whatever the coefficients.
Usage: revpair.py --list FILE | GAME [START]   (prints per game: transitions, reverse pairs, first pair)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, load, readstart
def run(g, st, name):
    _, R = rows(g, st, cap=20000); D = {}; first = None; cnt = 0
    for t in range(len(R) - 1):
        ch = frozenset((v, R[t]["s"][v] if g.owner[v] == 0 else R[t]["t"][v], R[t + 1]["s"][v] if g.owner[v] == 0 else R[t + 1]["t"][v])
                       for v in range(g.n) if (R[t]["s"][v], R[t]["t"][v]) != (R[t + 1]["s"][v], R[t + 1]["t"][v]))
        rev = frozenset((v, b, a) for v, a, b in ch)
        if rev in D: cnt += 1; first = first or (D[rev], t, sorted(ch)[:3])
        D.setdefault(ch, t)
    print("REV", name, "n", g.n, "transitions", len(R) - 1, "reverse_pairs", cnt, "first", first)
    return cnt
a = sys.argv[1:]
if a[0] == "--list":
    tot = hit = 0
    for line in open(a[1]):
        p = line.split()
        if not p: continue
        X = lambda q: os.path.join(ROOT, q) if os.path.exists(os.path.join(ROOT, q)) else os.path.join(ROOT, "experiments", q)
        try: tot += 1; hit += run(load(X(p[0])), readstart(X(p[1])) if len(p) > 1 else None, p[0]) > 0
        except Exception as e: print("SKIP", p[0])
    print("SUMMARY games", tot, "with a reverse pair", hit)
else: run(load(a[0]), readstart(a[1]) if len(a) > 1 else None, a[0])
