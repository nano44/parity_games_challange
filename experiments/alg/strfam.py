#!/usr/bin/env python3
"""The sibling-trap family S_s (L-ALG): Even owns every vertex, Odd wins every vertex, and the Odd attractor decomposition
is a perfect binary tree of height s (Strahler number s, checked with experiments/attr/strahler.py where affordable).
S_1 = one vertex of priority 1 with a self-loop. S_{s+1} = two copies A, B of S_s plus a connector c (even priority M+1,
M = max priority of S_s) and a top vertex t (odd priority M+2): every vertex of A gets an extra edge to t, every vertex
of B an extra edge to c; c -> vertex 0 of A; t -> vertex 0 of B. S_2 is psolc_min_n4_m6.pg up to relabelling; |S_s| = 3*2^(s-1) - 2.
Prediction (T-ALG1 (c)): NE'(k) solves S_s iff k >= s - 1. Usage: strfam.py SMAX [--kmax K] [--write]"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "attr")); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, ne, zielonka, alglib


def S(s):
    if s == 1:
        return pg.Game([1], [0], [[0]])
    a = S(s - 1)
    n, M = a.n, max(a.prio)
    prio = list(a.prio) + list(a.prio) + [M + 1, M + 2]
    owner = [0] * (2 * n + 2)
    c, t = 2 * n, 2 * n + 1
    succ = [sorted(set(x) | {t}) for x in a.succ] + [sorted({w + n for w in x} | {c}) for x in a.succ] + [[0], [n]]
    return pg.Game(prio, owner, succ)


def main():
    smax = int(sys.argv[1]); kmax = int(sys.argv[sys.argv.index("--kmax") + 1]) if "--kmax" in sys.argv else 4
    ne.MODE = "h"
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    for s in range(1, smax + 1):
        g = S(s); ref = zielonka.solve(g)
        assert all(r == 1 for r in ref), "Odd must win everywhere"
        if "--write" in sys.argv:
            pg.write(g, os.path.join(HERE, "instances", f"strfam_S{s}_n{g.n}.pg"))
        st = "-"
        if g.n <= 12:
            from strahler import strahler
            st = strahler(g, win=ref)[0]
        row = []
        for k in range(0, min(kmax, s) + 1):
            t0 = time.time(); win, _, stats = ne.solve(g, k); dt = time.time() - t0
            u = sum(1 for w in win if w is None)
            assert alglib.status(win, ref) != "UNSOUND"
            row.append(f"k={k}:{'solved' if u == 0 else f'undec {u}/{g.n}'} ({dt:.1f}s)")
            if u == 0:
                break
        print(f"S_{s}: n={g.n} m={g.m} d={len(set(g.prio))} Strahler={st}  " + "  ".join(row), flush=True)


if __name__ == "__main__":
    main()
