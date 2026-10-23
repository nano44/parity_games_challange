"""L-RED box 26 (produced on Opus 5.5): Conjecture BRIBE (R58 §5) on random games: N5 from best-reward start (declines.states,
counts asserted = n5.run); per move r = refused improving edges, o = opponent |I|. Prints the worst r / max(1, o) and the game.
Usage: bribebatch.py COUNT NMIN NMAX SEED"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import pg  # noqa: E402
cnt, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed); worst = (0, None); hist = {}
for i in range(cnt):
    n = rng.randint(nmin, nmax)
    prio = [rng.randint(0, n) for _ in range(n)]; owner = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) for _ in range(n)]
    g = pg.Game(prio, owner, succ); seq = declines.states(g)
    for t in range(len(seq) - 1):
        for k, I, J in ((0, 2, 3), (1, 3, 2)):
            s, s2 = seq[t][k], seq[t + 1][k]
            if s == s2: continue
            r = len(seq[t][I]) - sum(1 for v in range(n) if s[v] != s2[v]); o = len(seq[t][J])
            hist[(r > 0, o == 0)] = hist.get((r > 0, o == 0), 0) + 1
            q = r / max(1, o)
            if q > worst[0]: worst = (q, (r, o, prio, owner, succ))
print("moves by (refused>0, opponent I empty):", hist); print("worst ratio", worst)
