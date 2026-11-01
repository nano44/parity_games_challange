#!/usr/bin/env python3
"""L-RED R177 LADDERBF: ceiling for the BFS lex-min rule (Lemma TB, even regime) on the W-ladder, availability ADVERSARIAL.
Ladder: levels 1..d, vertices a_l, b_l; option k of a level-l vertex goes (through its own gate) to vertex k of level l-1 (level 1:
both options to c_W). key(v) = (key(target), gate index of v's chosen option); level-1 key = (gate index,).
Transition sigma -> sigma': choose for every v an availability set {sigma(v)} or {0,1}; sigma' = lex-min tree of that arena
(keys of parents taken in the new tree). Longest chain of sigma-changing transitions = longest path in the state DAG (keys strictly
decrease at movers, so it is a DAG). Gate indices: random permutations (best over TRIALS) or 'nat'. Usage: ladderbf.py d trials seed"""
import sys, random, itertools
from functools import lru_cache
d, trials, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); N = 2 * d; rng = random.Random(seed)
lev = [i // 2 for i in range(N)]
def solve(gate):
    def newsig(s, avail):
        key = [None] * N; ns = list(s)
        for v in range(N):
            opts = [0, 1] if avail >> v & 1 else [s[v]]
            def k(o): return ((gate[v][o],) if lev[v] == 0 else key[2 * (lev[v] - 1) + o] + (gate[v][o],))
            best = min(opts, key=k); ns[v] = best; key[v] = k(best)
        return tuple(ns)
    succ = {}
    states = list(itertools.product([0, 1], repeat=N))
    for s in states:
        succ[s] = {newsig(s, a) for a in range(1 << N)} - {s}
    sys.setrecursionlimit(100000)
    memo = {}
    def lp(s):
        if s in memo: return memo[s]
        memo[s] = 0
        r = 0
        for t in succ[s]: r = max(r, 1 + lp(t))
        memo[s] = r; return r
    return max(lp(s) for s in states)
best = 0
for t in range(trials):
    perm = list(range(2 * N)); rng.shuffle(perm); gate = [(perm[2 * v], perm[2 * v + 1]) for v in range(N)]
    best = max(best, solve(gate))
print("LADDERBF d", d, "N", N, "trials", trials, "max chain", best)
