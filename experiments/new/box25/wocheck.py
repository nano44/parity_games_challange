#!/usr/bin/env python3
"""Box 26, Lemma Wo check: at consecutive states with τ unchanged and (h) at both, is w = W(o) non-decreasing?
Usage: wocheck.py N lo hi seed [--randstart] | wocheck.py game.pg [start]"""
from common import *
from wdrop_h import oncycle
from collections import Counter
def run(g, start, cnt):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); prev = None
    while True:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        cur = (tuple(t), h, E.key(W[o]))
        if prev and prev[0] == cur[0] and prev[1] and cur[1]:
            cnt["pairs"] += 1
            if cur[2] < prev[2]: cnt["W_o_DECREASE"] += 1
        prev = cur
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = list(r[0]), list(r[1])
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0].endswith(".pg"):
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(a[0], dict(cnt))
    else:
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[0:4]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.1)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            run(g, st, cnt)
        print(dict(cnt))
