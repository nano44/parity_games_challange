"""L-RED box 17 (produced on Opus 5.5): a NEST* witness chain (p, first index, last index) per level. Usage: witness.py 0 1 6 9 ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "xctx"))
from comb.neststar import nest_star


def wit(Q):
    best = None
    for p in sorted({x for x, _ in Q}):
        idx = [i for x, i in Q if x == p]
        if len(idx) < 2: continue
        gap = [(x, i) for x, i in Q if idx[0] < i < idx[-1] and x > p]
        d = 1 + (nest_star(tuple(x for x, _ in gap)) if gap else 0)
        if best is None or d > best[0]: best = (d, p, idx[0], idx[-1], gap)
    if best is None: return [("any", [i for _, i in Q])] if Q else []
    return [(best[1], best[2], best[3])] + wit(best[4])


P = [int(x) for x in sys.argv[1:]]; print("NEST*", nest_star(tuple(P)), "witness", wit(list(zip(P, range(len(P))))))
