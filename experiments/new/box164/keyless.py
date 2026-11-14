#!/usr/bin/env python3
"""L-NEW box 164 control: the record multiplicity WITHOUT the key rule. Improvement graph on the 2^N states of a degree-2
IDEAL-ACYC genome (W-data and gates ignored): s -> s' when s' flips a nonempty set of Xi-unhappy movers of s (single flips only if
SINGLE=1). Acyclic by MONO-FLIP (box 163 §1). For every record r = (x, decisive beta of the A-comparison), DP for the largest number
of r-moves on one improving path; prints the max over r (mu_free) and the longest path length.
Usage: keyless.py N count seed"""
import os, sys, json, random, itertools
from functools import lru_cache
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "rec.py")).read().split("\nif __name__")[0])
SINGLE = os.environ.get("SINGLE", "0") == "1"

def rand_g(N, rng):
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}; opts = []; M = 0
    for x in range(N):
        o = []
        for k in range(2):
            later = [v for v in range(N) if pos[v] > pos[x]]
            o.append([-1, rng.choice(later) if later and rng.random() < 0.85 else -1, M]); M += 1
        opts.append(o)
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": [0] * N, "opts": opts, "gate": [[0, 1]] * N, "br": br, "bp": [rng.randint(0, 1) for _ in range(M)],
            "start": [0] * N, "xorder": order}

def analyse(G):
    g = Gen(G); N = g.N; states = list(itertools.product((0, 1), repeat=N))
    succ = {}
    for s in states:
        U = [x for x in range(N) if len(g.avail(s, x)) == 2]
        rec = {x: (x, decisive(g, chain(g, s, x, 1 - s[x]), chain(g, s, x, s[x]))) for x in U}
        out = []
        subsets = [[x] for x in U] if SINGLE else [list(c) for r in range(1, len(U) + 1) for c in itertools.combinations(U, r)]
        for sub in subsets:
            t = list(s)
            for x in sub: t[x] ^= 1
            out.append((tuple(t), [rec[x] for x in sub]))
        succ[s] = out
    recs = set(r for s in states for _, rs in succ[s] for r in rs)
    @lru_cache(None)
    def longest(s):
        return max([1 + longest(t) for t, _ in succ[s]], default=0)
    L = max(longest(s) for s in states)
    mu = 0; arg = None
    for r in recs:
        memo = {}
        def f(s):
            if s in memo: return memo[s]
            v = max([(r in rs) + f(t) for t, rs in succ[s]], default=0); memo[s] = v; return v
        m = max(f(s) for s in states)
        if m > mu: mu, arg = m, r
    return L, mu, arg

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    N, cnt, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); best = (0, 0)
    for i in range(cnt):
        G = rand_g(N, rng); L, mu, arg = analyse(G)
        if (mu, L) > best:
            best = (mu, L); json.dump(G, open(os.path.join(H, "out", "keyless_N%d_mu%d%s.json" % (N, mu, "_single" if SINGLE else "")), "w"))
    print("KEYLESS N %d count %d single %s : max mu_free %d (longest path then %d)" % (N, cnt, SINGLE, best[0], best[1]))
