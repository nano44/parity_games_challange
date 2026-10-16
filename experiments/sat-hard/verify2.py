#!/usr/bin/env python3
"""Exhaustive, progress-measure-free verification of a weak separator for n <= 2, convention E, any d.
A graph on vertices {0,1}: loop label sets L0, L1, edge label sets A (0->1), B (1->0). Its simple cycles are the loops
and 0->1->0 (with optional loops, which do not create new maxima beyond max(a, b, l) of simple cycles). So it is
even iff every loop label is even and max(a, b) is even for all a in A, b in B (odd: the same with odd). We enumerate
ALL (A, B) pairs satisfying the condition (2^d x 2^d), keep the inclusion-maximal ones with loops = all letters of the
parity, add the 1-vertex graphs, and run check.violations on them (subgraphs of a checked graph are implied: W1 and W2
are monotone under taking subgraphs). Usage: verify2.py automaton.json"""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check


def maximal_2(d, win):
    L = [p for p in range(1, d + 1) if p % 2 == win]
    sets = []
    letters = list(range(1, d + 1))
    ok_pairs = {(a, b) for a in letters for b in letters if max(a, b) % 2 == win}
    allsub = [frozenset(c) for r in range(d + 1) for c in itertools.combinations(letters, r)]
    good = []
    for A in allsub:
        # largest B compatible with A: all b with max(a,b) of parity win for every a in A
        Bmax = frozenset(b for b in letters if all((a, b) in ok_pairs for a in A))
        good.append((A, Bmax))
    # keep pairs where A is also maximal given Bmax
    maxi = set()
    for A, B in good:
        Amax = frozenset(a for a in letters if all((a, b) in ok_pairs for b in B))
        if Amax == A:
            maxi.add((A, B))
    graphs = []
    for A, B in maxi:
        E = {(0, p, 0) for p in L} | {(1, p, 1) for p in L} | {(0, a, 1) for a in A} | {(1, b, 0) for b in B}
        graphs.append((2, frozenset(E)))
    graphs.append((1, frozenset((0, p, 0) for p in L)))
    return graphs


if __name__ == "__main__":
    aut = json.load(open(sys.argv[1]))
    aut = aut.get("automaton", aut)
    d = aut["d"]
    ev, od = maximal_2(d, 0), maximal_2(d, 1)
    bad = check.violations(aut, ev, od)
    print(f"d={d}: {len(ev)} maximal even, {len(od)} maximal odd graphs on <= 2 vertices (exhaustive); "
          f"violations: {bad if bad else 'none'} -> {'WEAK SEPARATOR' if not bad else 'NOT a separator'}")
