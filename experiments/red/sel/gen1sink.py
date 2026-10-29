#!/usr/bin/env python3
"""L-RED successor 23: random 1-sink W-attractor games in long121's style (R97 §3). Vertex 0 = gate o (Odd, 4-6 options incl. the sink);
vertex 1 = sink s (Odd, self-loop, even priority 10); vertices 2, 3 = two more Odd choice vertices (2-4 options); the rest Even, out-degree
2-4, priorities mostly odd in 11..2n+20 (penalties), some even. Usage (module): gen(n, rng) -> [prio, owner, succ]; CLI: gen1sink.py n seed OUT.pg"""
import sys, random

def gen(n, rng):
    prio = [0] * n; owner = [0] * n; succ = [[] for _ in range(n)]
    owner[0] = owner[1] = owner[2] = owner[3] = 1
    prio[1] = 10; succ[1] = [1]
    for v in range(n):
        if v == 1: continue
        if v == 0: prio[v] = 16
        else:
            p = rng.randrange(11, 2 * n + 20)
            prio[v] = p | 1 if rng.random() < 0.85 else p & ~1
        if v == 0: succ[v] = sorted(set(rng.sample(range(4, n), rng.randint(3, 5))) | {1})
        elif v in (2, 3): succ[v] = sorted(set(rng.sample(range(4, n), rng.randint(2, 4))))
        else: succ[v] = sorted(set(rng.sample([w for w in range(n) if w != v], rng.randint(2, 4))))
    return [prio, owner, succ]

if __name__ == "__main__":
    n, seed, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    prio, owner, succ = gen(n, random.Random(seed))
    with open(out, "w") as f:
        f.write("parity %d;\n" % (n - 1))
        for v in range(n): f.write("%d %d %d %s;\n" % (v, prio[v], owner[v], ",".join(map(str, succ[v]))))
