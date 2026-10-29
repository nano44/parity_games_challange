#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA + checks for docs/new/N5-READER-box49.md §3-§4. Per phase of N5, with Xi compared in SPEC S1's order (E.key):
- FLIPS: for every pair {y, z} of vertices, the number of transitions at which their strict order flips (y ◁ z at t and y ▷ z at t + 1, or the
  reverse; a tie on either side is not a flip). s(P) := the largest FLIPS of one pair; X(P) := the sum over pairs.
- SW(w): Even switches of w. PASS(w): the (t, y), y ∈ succ(w), with Xi_t(y) ⊴ Xi_t(σ_{t+1} w) and Xi_{t+1}(y) ▷ Xi_{t+1}(σ_{t+1} w) (an option
  passes w's choice). Lemma SW-AMORT says SW(w) <= PHI0(w) + PASS(w), PHI0(w) := #{y ∈ succ(w) : Xi(y) ▷ Xi(σ w)} at the phase's first state;
  CHECKED here at every Even w of every phase (violations must be 0). L <= Σ_w SW(w) (every in-phase transition switches an Even vertex):
  CHECKED (NOSW must be 0).
- ENV(u): for an Odd vertex u with >= 2 options, the sigma-bar changes of u, against the Davenport-Schinzel-type count: the pairs of options
  of u whose order flips (each sigma-bar change at a transition with no tie needs a flip between the old and new choice; counted, not
  asserted: ENVX = changes not matched by a flip of (old, new) at that transition).
Usage: cross.py STARTS SEED (--list FILE | files) [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from collections import Counter
C = Counter(); MAX = {}
def mx(k, v, tag):
    if v > MAX.get(k, (-1,))[0]: MAX[k] = (v, tag)

def run(g, st, nm):
    E, R = rows(g, st); n = g.n
    for i, j in phases(R):
        L = j - i; C["phases"] += 1; C["L"] += L
        key = [[E.key(R[k]["vs"][v]) for v in range(n)] for k in range(i, j + 1)]
        flips = Counter()
        for k in range(L):
            a, b = key[k], key[k + 1]
            for y in range(n):
                for z in range(y + 1, n):
                    if (a[y] < a[z] and b[y] > b[z]) or (a[y] > a[z] and b[y] < b[z]): flips[(y, z)] += 1
        s = max(flips.values(), default=0); X = sum(flips.values())
        sw, ps = Counter(), Counter(); nosw = 0
        for k in range(L):
            A, B = R[i + k], R[i + k + 1]; a, b = key[k], key[k + 1]
            if not any(g.owner[v] == 0 and A["s"][v] != B["s"][v] for v in range(n)): nosw += 1
            for w in range(n):
                if g.owner[w] != 0: continue
                if A["s"][w] != B["s"][w]: sw[w] += 1
                ch = B["s"][w]
                for y in g.succ[w]:
                    if a[y] <= a[ch] and b[y] > b[ch]: ps[w] += 1
        viol = 0; envx = 0; envc = 0
        for w in range(n):
            if g.owner[w] != 0: continue
            phi0 = sum(1 for y in g.succ[w] if key[0][y] > key[0][R[i]["s"][w]])
            if sw[w] > phi0 + ps[w]: viol += 1
        for k in range(L):
            A, B = R[i + k], R[i + k + 1]; a, b = key[k], key[k + 1]
            for u in range(n):
                if g.owner[u] == 1 and len(g.succ[u]) >= 2 and A["sb"][u] != B["sb"][u]:
                    envc += 1; y1, y2 = A["sb"][u], B["sb"][u]
                    if not ((a[y1] < a[y2] and b[y1] > b[y2]) or (a[y1] > a[y2] and b[y1] < b[y2])): envx += 1
        C["NOSW"] += nosw; C["SWAMORT_viol"] += viol; C["sbch"] += envc; C["ENVX"] += envx
        C["SW"] += sum(sw.values()); C["PASS"] += sum(ps.values()); C["X"] += X
        tag = (nm, (i, j), n)
        mx("s_over_n", s / n, tag + (s,)); mx("s", s, tag); mx("maxSW_over_n", max(sw.values(), default=0) / n, tag + (max(sw.values(), default=0),))
        mx("PASS_over_L", sum(ps.values()) / max(L, 1), tag + (sum(ps.values()), L)); mx("L", L, tag)

if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    files = [os.path.join(ROOT, l.split()[0]) for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else a
    for f in files:
        g = load(f)
        if g.n > nmax: continue
        sf = f[:-3] + ".start"
        sts = [readstart(sf) if os.path.exists(sf) else None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                                  {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, os.path.relpath(f, ROOT)); C["runs"] += 1
            except RecursionError: C["RECERR"] += 1
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for k, v in sorted(MAX.items()): print("max", k, v)
