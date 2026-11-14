#!/usr/bin/env python3
"""Box 191: condition X1 on GENERAL games: at each sigma-changing N5'-xi iteration, is sigma_new a Howard step of sigma (every Even
vertex with a strictly better successor goes to a VJ-best one, every other Even vertex keeps sigma)? Usage: x1gen191.py COUNT SEED n"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box190")]
import n5v
pg = n5v.pg
cnt, seed, n = map(int, sys.argv[1:4]); rng = random.Random(seed); tot = faith = games_all = 0
for i in range(cnt):
    g = pg.Game([rng.randrange(n + 1) for _ in range(n)], [rng.randrange(2) for _ in range(n)], [sorted(rng.sample(range(n), rng.randint(1, min(3, n)))) for _ in range(n)])
    st, fb, E = n5v.run(g, "xi"); allf = True
    for (s, t), (ns, nt) in zip(st, st[1:]):
        if ns == s: continue
        vs, _ = E.evaluate(s); tot += 1; ok = True
        for v in range(g.n):
            if g.owner[v] != 0: continue
            best = max(E.key(vs[w]) for w in g.succ[v]); cur = E.key(vs[s[v]])
            if best > cur: ok &= E.key(vs[ns[v]]) == best
            else: ok &= ns[v] == s[v]
        faith += ok; allf &= ok
    games_all += allf
print(f"general random games count {cnt} seed {seed} n {n}: sigma-changing iterations {tot}, Howard-faithful {faith}; games with every sigma-step faithful {games_all}")
