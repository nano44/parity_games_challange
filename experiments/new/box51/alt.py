#!/usr/bin/env python3
"""L-NEW box 51: pairwise toggle alternation inside runs (fallback-free stretches of a phase). For edges e, f (Even, distinct vertices) the
toggle events (time k -> k+1 where presence in sigma changes) are merged in time order; alt(e, f) = number of maximal runs of equal letters
(simultaneous toggles of e and f ordered e first, e < f: the sequence of Lemma DS-VC). DS-PAIR(s): alt <= s + 1 for all pairs.
Usage: alt.py NAME... (a cached dump.py name, or GAME.pg with GAME.start beside it if present)"""
import sys, os, pickle
from itertools import combinations
HERE = os.path.dirname(os.path.abspath(__file__))

def runs_of(D):
    st = D["st"]
    for i, j in D["ph"]:
        a = i
        for k in range(i, j):
            if st[k]["fb"]:
                if k > a: yield a, k
                a = k + 1
        if j > a: yield a, j

def toggles(D, a, b):
    st = D["st"]; ev = [v for v in range(D["n"]) if D["owner"][v] == 0 and len(D["succ"][v]) >= 2]; T = {}
    for k in range(a, b):
        for v in ev:
            x, y = st[k]["s"][v], st[k + 1]["s"][v]
            if x != y: T.setdefault((v, x), []).append(k); T.setdefault((v, y), []).append(k)
    return T

def alt(te, tf):
    """runs of the merged toggle sequence, simultaneous toggles ordered e before f (e < f): Lemma DS-VC's sequence."""
    seq = [x for _, x in sorted([(k, 0) for k in te] + [(k, 1) for k in tf])]
    return sum(1 for q in range(len(seq)) if q == 0 or seq[q] != seq[q - 1])

if __name__ == "__main__":
    for name in sys.argv[1:]:
        if name.endswith(".pg"):
            sys.path.insert(0, HERE); from dump import dump
            D = dump(name, name[:-3] + ".start" if os.path.exists(name[:-3] + ".start") else None, save=False)
        else: D = pickle.load(open(os.path.join(HERE, "..", "out", "box51", name + ".pkl"), "rb"))
        best = (0,)
        for a, b in runs_of(D):
            T = toggles(D, a, b)
            for e, f in combinations(sorted(T), 2):
                if e[0] == f[0]: continue
                r = alt(T[e], T[f])
                if r > best[0]: best = (r, e, f, a, b)
        print(name, "max pairwise alt in a run:", best)
