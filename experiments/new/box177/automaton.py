#!/usr/bin/env python3
"""L-NEW box 177: the key-side automaton of a level-l pair on L^R_d (Lemma ALIGN). State (a_p, a_q, b); gate constants gam0, gam1.
ord = a_p if a_p != a_q, else gam[c] for both aligned (c = 0 if b else 1), gam[1 - c] for both misaligned.
A step: optionally flip b (toggles a_p, a_q: alignment is relative to c(b)), then any subset of the misaligned movers moves (becomes
aligned); at least one event; a step with a b flip but no ord change is allowed. Values (Xi side) are ignored: any misaligned mover may
move (free availability = key-free in the Xi sense, as FREE-KP). Max #ord changes with exactly k b-flips, by DP over states.
Usage: automaton.py kmax"""
import sys, itertools
kmax = int(sys.argv[1])
def ordf(ap, aq, b, gam):
    c = 0 if b else 1
    if ap != aq: return ap
    return gam[c] if ap else gam[1 - c]
for gam in itertools.product((0, 1), repeat=2):
    best = {}
    for st in itertools.product((0, 1), repeat=3): best[(st, 0)] = 0
    res = []
    # BFS over (state, flips used) with value = max ord changes; steps bounded since without b flips each mover moves at most once
    frontier = dict(best)
    for it in range(4 * kmax + 6):
        new = {}
        for (st, k), val in frontier.items():
            ap, aq, b = st
            for fb in (0, 1):
                if k + fb > kmax: continue
                b2 = b ^ fb; ap2, aq2 = ap ^ fb, aq ^ fb
                for mp in ((0, 1) if ap2 == 0 else (0,)):
                    for mq in ((0, 1) if aq2 == 0 else (0,)):
                        if not (fb or mp or mq): continue
                        s2 = (ap2 | mp, aq2 | mq, b2); dv = int(ordf(*s2, gam) != ordf(ap, aq, b, gam))
                        key = (s2, k + fb)
                        if new.get(key, -1) < val + dv: new[key] = val + dv
        for kk, v in new.items():
            if best.get(kk, -1) < v: best[kk] = v
        frontier = new
    print("gam", gam, "max ord changes by k b-flips:", [max(v for (s, k), v in best.items() if k == kk) for kk in range(kmax + 1)])
