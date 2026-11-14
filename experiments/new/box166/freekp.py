#!/usr/bin/env python3
"""L-NEW box 166: the FREE-KP relaxation (key preference KP_t(x) chosen freely each step) = key-free subset dynamics: s_t(x) =
KP_t(x) if x is Xi-unhappy at s_(t-1), else s_(t-1)(x). Extract, for a degree-2 genome and a mover x0, a path maximizing moves(x0)
(exact DP over 2^N states, single switches suffice for the max), and print the schedule: per step the unhappy set, the mover that
moves, and the movers HELD (unhappy, not moving) -> the KP pattern a keyed run would have to realize.
Usage: freekp.py file.json x0"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
G = json.load(open(sys.argv[1])); x0 = int(sys.argv[2]); g = Gen(G); N = g.N; R = reach(G)
states = list(itertools.product((0, 1), repeat=N))
unh = {s: [x for x in range(N) if len(g.avail(s, x)) == 2] for s in states}
memo = {}
def fm(s):
    if s not in memo:
        best = (0, None)
        for x in unh[s]:
            t = s[:x] + (1 - s[x],) + s[x + 1:]; v = (x == x0) + fm(t)[0]
            if v > best[0]: best = (v, t)
        memo[s] = best
    return memo[s]
s0 = max(states, key=lambda s: fm(s)[0]); print("x0", x0, "desc", sorted(R[x0]), "max moves", fm(s0)[0], "start", "".join(map(str, s0)))
s = s0; t = 0
while fm(s)[1] is not None:
    n = fm(s)[1]; x = [y for y in range(N) if n[y] != s[y]][0]; t += 1
    print("step %2d %s unhappy %s move x%d %d->%d held %s" % (t, "".join(map(str, s)), unh[s], x, s[x], n[x], [y for y in unh[s] if y != x]))
    s = n
print("end", "".join(map(str, s)), "unhappy", unh[s])
