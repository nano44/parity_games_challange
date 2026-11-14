#!/usr/bin/env python3
"""L-SI box 109: RF from RANDOM starts (the start is the adversary's: a wrapper can force S3 to pick any strategy, P-N5-WRAP S3-W).
Usage: starts109.py FAMILY ARG COUNT SEED   prints the minimum, mean and maximum of RF's iterations over COUNT uniformly random
Even strategies, the count from the family's own start, and Howard's maximum over the same starts (cap 20,000 iterations)."""
import sys, random
sys.argv, av = [sys.argv[0]], sys.argv
import fam109, rf109, n6
fam, a, cnt, seed = av[1], int(av[2]), int(av[3]), int(av[4]); rng = random.Random(seed)
g, sp = fam109.family(fam, a); own = rf109.run(g, start=(sp[0] if sp else None))["its"]
E = n6.Engine(g); res = []; hw = 0
for i in range(cnt):
    st = [rng.choice(sorted(set(g.succ[v]))) if g.owner[v] == 0 else -1 for v in range(g.n)]
    res.append(rf109.run(g, start=st)["its"])
    if i < 20: hw = max(hw, n6.run(g, "howard", cap=20000, start_pair=(st, list(n6.Engine(n6.dual(g)).initial("best"))))["its"])
print(f"ST109 {fam} {a} n {g.n}: RF from the family's start {own}; over {cnt} random starts (seed {seed}): min {min(res)} mean {sum(res) / cnt:.1f} max {max(res)}; Howard max over the first 20 of them {hw}", flush=True)
