#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §29 Lemma BF-F_D (every game). At every in-phase S4a transition k -> k+1 (fb = 0), for every
class c, Even v in U_c := lambda^-1(c), v != c, with v in F_D(k) and v in F_D(k+1) (F_D := the vertices whose (sigma, tau)-play avoids
D := {Odd u : sigma-bar(u) != tau(u)}), and every successor x of v in U_c:   M_k+1(v) >= wt_c(v) + M_k(x)   (M := signed path weight).
Counted: checks, BFFD_V (violations). WCHK: W = Xi on F_D (R55 (a)); WPLAY_V counts failures of wplay against h1.wvals on the first run.
Variants: ONLYK1 (v in F_D(k+1) only): reported, not claimed. Control MUT=1: flag equality too (lhs <= rhs), i.e. claim
the bound is never tight (must bite: it is tight at the chosen edge). Usage: bffd.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *
C = Counter(); VIOL = []; MUT = os.environ.get("MUT") == "1"

def run(g, name, start=None):
    E, R = rows(g, start)
    if C["wplay_checked"] == 0:
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); from h1 import wvals
        for A in R[:5]:
            _, Wv = wvals(g, A["s"], A["t"])
            C["wplay_checked"] += 1
            if [E.key(x) for x in Wv] != [E.key(x) for x in A["W"]]: C["WPLAY_V"] += 1; VIOL.append(("WPLAY", name))
    for i, j in phases(R):
        C["phases"] += 1
        for k in range(i, j):
            A, B = R[k], R[k + 1]
            if A["fb"] == 1: continue
            FA, FB = avoid(A["wn"], Dset(g, A), g.n), avoid(B["wn"], Dset(g, B), g.n)
            for v in FA:
                C["wchk"] += 1
                if E.key(A["vs"][v]) != E.key(A["W"][v]): C["W_NE_XI_ON_F"] += 1; VIOL.append(("WF", name, k, v))
            for v in range(g.n):
                if g.owner[v] != 0: continue
                c = A["vs"][v][0]
                if v == c or v not in FB: continue
                both = v in FA
                for x in set(g.succ[v]):
                    if A["vs"][x][0] != c: continue
                    lhs, rhs = M(E, B["vs"][v]), wt(E, v, c) + M(E, A["vs"][x])
                    if both:
                        C["checks"] += 1
                        bad = (lhs <= rhs) if MUT else (lhs < rhs)
                        if bad: C["BFFD_V"] += 1; VIOL.append(("BFFD", name, k - i, v, x, lhs, rhs))
                    else:
                        C["onlyk1_checks"] += 1
                        if lhs < rhs: C["ONLYK1_fail"] += 1

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); run(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 1
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("BFFD PASS" if not VIOL else "BFFD FAIL")

if __name__ == "__main__":
    main()
