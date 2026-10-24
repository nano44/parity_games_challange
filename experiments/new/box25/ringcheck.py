#!/usr/bin/env python3
"""Box 25: at throttled states (θ ◁ w) of o-cyclic C^1O runs, where are the exits that Even's best reply against τ routes through o
(self-throttling exits, per box 24 §2)? Classify each such exit e ≠ σ̄(o) as ON (e lies on o's honest continuation, i.e. on
σ̄(o)'s σ-path) or OFF. ON exits cannot take a through-o route without closing a cycle through o.
Usage: ringcheck.py game.pg | ringcheck.py --random N nmin nmax seed"""
from common import *
from thtrace import Rset
from sbclass import path
def run(g, st, cnt):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g)
    for s, t in st[:-1]:
        Xi, sb = E.evaluate(s); _, W = wvals(g, s, t)
        if not E.key(Xi[o]) < E.key(W[o]): continue
        U, tbar = Ed.evaluate(t); cont = set(path(g, s, t, sb[o], o)); cnt["thr_states"] += 1
        for e in g.succ[o]:
            if e == sb[o] or g.owner[e] != 0: continue
            x, seen, thru = e, set(), False                # Even's best reply tbar against τ from e: does it pass o?
            nxt = [tbar[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]
            while x not in seen:
                if x == o: thru = True; break
                seen.add(x); x = nxt[x]
            if not thru: continue
            cnt["ON" if e in cont else "OFF"] += 1
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = {"thr_states": 0, "ON": 0, "OFF": 0}
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st, _ = trace(g, check=False); run(g, st, cnt)
    else:
        g = load(a[0]); st, _ = trace(g); run(g, st, cnt)
    print(cnt)
