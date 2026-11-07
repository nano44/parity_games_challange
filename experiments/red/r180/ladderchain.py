#!/usr/bin/env python3
"""L-RED R180: LADDERBF (r177) with chain output. For the best gate assignment over TRIALS, write JSON {d, gate, chain: [sigma_0, ...]}
of one longest chain of sigma-changing transitions (adversarial availability, lex-min tree). Usage: ladderchain.py d trials seed out.json"""
import sys, random, itertools, json
d, trials, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; N = 2 * d; rng = random.Random(seed)
lev = [i // 2 for i in range(N)]
def keys(s, gate):
    key = [None] * N
    for v in range(N): key[v] = ((gate[v][s[v]],) if lev[v] == 0 else key[2 * (lev[v] - 1) + s[v]] + (gate[v][s[v]],))
    return key
def solve(gate):
    def newsig(s, avail):
        key = [None] * N; ns = list(s)
        for v in range(N):
            opts = [0, 1] if avail >> v & 1 else [s[v]]
            def k(o): return ((gate[v][o],) if lev[v] == 0 else key[2 * (lev[v] - 1) + o] + (gate[v][o],))
            b = min(opts, key=k); ns[v] = b; key[v] = k(b)
        return tuple(ns)
    states = list(itertools.product([0, 1], repeat=N)); succ = {s: {newsig(s, a) for a in range(1 << N)} - {s} for s in states}
    memo = {}
    def lp(s):
        if s in memo: return memo[s]
        best = (0, None)
        for t in succ[s]:
            l = 1 + lp(t)[0]
            if l > best[0]: best = (l, t)
        memo[s] = best; return best
    s0 = max(states, key=lambda s: lp(s)[0]); chain = [s0]
    while lp(chain[-1])[1] is not None: chain.append(lp(chain[-1])[1])
    return len(chain) - 1, chain
best = None
for t in range(trials):
    perm = list(range(2 * N)); rng.shuffle(perm); gate = [(perm[2 * v], perm[2 * v + 1]) for v in range(N)]
    L, ch = solve(gate)
    if best is None or L > best[0]: best = (L, gate, ch)
json.dump(dict(d=d, gate=best[1], chain=[list(c) for c in best[2]]), open(out, "w"))
print("CHAIN d", d, "length", best[0], "moves per step", [sum(a != b for a, b in zip(x, y)) for x, y in zip(best[2], best[2][1:])])
