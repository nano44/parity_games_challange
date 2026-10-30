import sys, random
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "new", "box21"))
from n5x import trace, Engine, dual
import pg
rnd = random.Random(int(sys.argv[1])); worst = 0; cnt = 0
for _ in range(int(sys.argv[2])):
    n = rnd.randint(4, 14)
    pr = rnd.sample(range(2, 3 * n + 2), n - 1); pr = [rnd.choice([0, 1])] + pr   # vertex 0 = sink (self-loop)
    own = [rnd.randint(0, 1) for _ in range(n)]
    succ = [[0]] + [sorted(set(rnd.sample(range(v), rnd.randint(1, min(3, v))))) for v in range(1, n)]   # edges go to lower index: DAG
    g = pg.Game(pr, own, succ)
    h = [0] * n
    for v in range(1, n): h[v] = 1 + max(h[w] for w in succ[v])
    states, fb = trace(g, None, check=False)
    tstar = states[-1][1]
    st = ({v: rnd.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: tstar[v] for v in range(n) if own[v] == 1})
    s2, fb2 = trace(g, st, check=False)
    it = len(s2) - 1; taus = len({x[1] for x in s2}); cnt += 1
    if it > max(h) + 1 or fb2 or taus > 1: print("VIOLATION", it, max(h), fb2, taus, pr, own, succ, st); break
    worst = max(worst, it - max(h))
print("done", cnt, "max(it - height)", worst)
