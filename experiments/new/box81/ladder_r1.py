#!/usr/bin/env python3
"""L-NEW box 81 (R1-POLY), part 1: the UNGATED ladder_k (box80) under a RANKING-offer rule R1- (weaker than R1: no monotonicity, no X <= W):
at each step a ranking of the vertices is chosen freely; Even v is offered every successor w with rank(w) > rank(sigma(v)); the new
strategy is the one-player optimum of sigma + offers. In ladder_k every choice vertex at level j+1 (and T at level k+1) has successors
{u(j,0), u(j,1)}, so a ranking acts per level as a direction d_j in {none, 0->1, 1->0}: every vertex of that level holding the lower child
is offered the other, and takes it iff it is W-improving (one-player optimum; children values are distinct, so the optimum is unique).
Exhaustive DP over states and per-level directions: the longest chain of strict W(T)-rises from the all-copy-0 start, and from EVERY start.
Usage: ladder_r1.py K"""
import sys, functools, itertools
k = int(sys.argv[1])
def u(j, b): return (j, b)
# choosers: level j+1 vertices (j = 1..k-1) are (j+1, b); T reads level k. state: tuple of choices, index i -> chooser
chooser = [(j, b) for j in range(2, k + 1) for b in (0, 1)] + [("T",)]
def lvl(c): return k if c == ("T",) else c[0] - 1      # level read by chooser c
def aval(st, j, b):                                      # abstract value (box80 ladder.py): below-bits deep first, then own copy bit
    bits = [b]; jj, bb = j, b
    while jj >= 2:
        i = chooser.index((jj, bb)); bb = st[i]; jj -= 1; bits.append(bb)
    return tuple(reversed(bits))
def Tval(st): return aval(st, k, st[-1])
def succs(st):
    out = set()
    for dirs in itertools.product((None, 0, 1), repeat=k):   # dirs[j-1]: at level j, offer copy dirs to holders of 1-dirs
        ns = list(st)
        for i, c in enumerate(chooser):
            d = dirs[lvl(c) - 1]
            if d is None or st[i] == d: continue
            if aval(st, lvl(c), d) > aval(st, lvl(c), st[i]): ns[i] = d
        ns = tuple(ns)
        if ns != st: out.add(ns)
    return out
@functools.lru_cache(None)
def best(st):
    return max([best(ns) + (Tval(ns) != Tval(st)) for ns in succs(st)], default=0)
start0 = tuple([0] * len(chooser))
allbest = max(best(s) for s in itertools.product((0, 1), repeat=len(chooser)))
print(f"LADDER-R1 k {k} n {2 * k + 2} max-T-rises from all-0 start {best(start0)} from any start {allbest} (single-switch relaxation R0: {2 ** k - 1})")
