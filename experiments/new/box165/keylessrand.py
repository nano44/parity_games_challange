#!/usr/bin/env python3
"""key-free PM screen on random acyclic degree-2 genomes (all 2^N states, single improving switches): max over genomes of
(max moves of x on one improving path) per desc(x). Usage: keylessrand.py N count seed"""
import os, sys, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "permover.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
N, cnt, seed = map(int, sys.argv[1:4]); rng = random.Random(seed); best = {}
for i in range(cnt):
    order = list(range(N)); rng.shuffle(order); pos = {v: j for j, v in enumerate(order)}; opts = []; M = 0
    for x in range(N):
        later = [v for v in range(N) if pos[v] > pos[x]]
        opts.append([[-1, rng.choice(later) if later and rng.random() < 0.85 else -1, 2 * x + k] for k in range(2)])
    br = list(range(2 * N)); rng.shuffle(br)
    G = {"N": N, "lev": [0] * N, "opts": opts, "gate": [[0, 1]] * N, "br": br, "bp": [rng.randint(0, 1) for _ in range(2 * N)], "start": [0] * N}
    g = Gen(G); R = reach(G); states = list(itertools.product((0, 1), repeat=N))
    succ = {s: [s[:x] + (1 - s[x],) + s[x + 1:] for x in range(N) if len(g.avail(s, x)) == 2] for s in states}
    for x in range(N):
        memo = {}
        def fm(s):
            if s not in memo: memo[s] = max([(t[x] != s[x]) + fm(t) for t in succ[s]], default=0)
            return memo[s]
        d = len(R[x]); m = max(fm(s) for s in states)
        if m > best.get(d, (0,))[0]:
            best[d] = (m, i)
            if m > 1 + d: json.dump(G, open(os.path.join(H, "out", "keyless_pmviol_N%d_d%d_m%d.json" % (N, d, m)), "w"))
print("KEYLESS-RAND N %d count %d: desc -> max moves %s" % (N, cnt, {d: best[d][0] for d in sorted(best)}))
