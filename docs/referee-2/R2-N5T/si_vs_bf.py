"""Cross-check of the object under test: si.py Engine.evaluate / improving (SPEC S1/S2) against vjbf.omega (VJ00 brute force).
Usage: python3 -I si_vs_bf.py REPO_ROOT N SEED"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vjbf
root = sys.argv[1]
sys.path.insert(1, os.path.join(root, 'experiments', 'si')); sys.path.insert(1, os.path.join(root, 'experiments', 'harness'))
import si, pg
N, seed = int(sys.argv[2]), int(sys.argv[3]); rnd = random.Random(seed)
DUAL = len(sys.argv) > 4 and sys.argv[4] == "dual"   # test on G^d (prio + 1, owners swapped), i.e. the Odd side of N5
bad_val = bad_imp = strats = 0; ex = None
for _ in range(N):
    n = rnd.randint(2, 7)
    prio = [rnd.randint(0, n) for _ in range(n)]; owner = [rnd.randint(0, 1) for _ in range(n)]
    succ = [rnd.sample(range(n), rnd.randint(1, min(3, n))) for _ in range(n)]
    if DUAL: prio = [p + 1 for p in prio]; owner = [1 - o for o in owner]
    g = vjbf.Game(prio, owner, succ)
    E = si.Engine(pg.Game(prio, owner, [sorted(set(s)) for s in succ]))
    for sigma in vjbf.strategies(g):
        strats += 1
        Om = vjbf.omega(g, sigma)
        st = tuple(sigma[v] if owner[v] == 0 else -1 for v in range(n))
        val, _ = E.evaluate(st)
        for v in range(n):
            l, B, k = Om[v]; mask = sum(1 << g.rank[u] for u in B)
            if val[v] != (l, mask, k):
                bad_val += 1; ex = ex or (prio, owner, succ, sigma, v, Om[v], val[v])
        if sorted(E.improving(st, val)) != sorted(vjbf.improvements(g, sigma, Om)): bad_imp += 1
print('dual' if DUAL else 'primal', 'games', N, 'strategies', strats, 'valuation mismatches', bad_val, 'improvement-set mismatches', bad_imp)
if ex: print('example', ex)
