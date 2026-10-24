"""L-RED box 26 (produced on Opus 5.5): check of R58 §9 Proposition X (locality on C^1O). X = vertices that cannot reach the Odd
choice vertex o in the game graph (a subgame without Odd choices). Claim: the sequence of DISTINCT restrictions sigma|X along the
canonical N5 run of G equals the canonical N5 run of the one-player game G[X] (states, in order); hence #theta-changes <=
#X-changes when succ(o) is inside X. Random C^1O games (o = 0) with succ(o) inside X (o on no cycle), both runs via
declines.states (n5.py replica, counts asserted = n5.run). Usage: xlocal.py COUNT NMIN NMAX SEED"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
cnt, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
ok = bad = skipped = 0; worst = 0
for i in range(cnt):
    n = rng.randint(nmin, nmax)
    prio = [rng.randint(0, 2 * n) for _ in range(n)]; owner = [rng.randint(0, 1) for _ in range(n)]; owner[0] = 1
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    for v in range(1, n):
        if owner[v] == 1: succ[v] = succ[v][:1]
    if len(succ[0]) < 2: succ[0] = sorted(set(succ[0] + [rng.randrange(1, n)]))
    reach = {0}; ch = True                       # vertices that can reach o
    while ch:
        ch = False
        for v in range(n):
            if v not in reach and any(w in reach for w in succ[v]): reach.add(v); ch = True
    if any(w in reach for w in succ[0]): skipped += 1; continue      # o on a cycle: outside the claim
    X = [v for v in range(n) if v not in reach]
    g = pg.Game(prio, owner, succ); seq = declines.states(g)
    idx = {v: j for j, v in enumerate(X)}
    gx = pg.Game([prio[v] for v in X], [owner[v] for v in X], [[idx[w] for w in succ[v]] for v in X])
    sx = declines.states(gx)
    XE = [j for j, v in enumerate(X) if owner[v] == 0]
    a = [tuple(s[X[j]] for j in XE) for s, _, _, _ in seq]; da = [a[0]] + [a[k] for k in range(1, len(a)) if a[k] != a[k - 1]]
    b = [tuple(X[s[j]] for j in XE) for s, _, _, _ in sx]; db = [b[0]] + [b[k] for k in range(1, len(b)) if b[k] != b[k - 1]]
    E = Engine(g); th = [E.evaluate(s)[0][0] for s, _, _, _ in seq]
    tc = sum(th[k] != th[k - 1] for k in range(1, len(th)))
    if da == db and tc <= len(db) - 1: ok += 1; worst = max(worst, tc)
    else: bad += 1; print("MISMATCH", prio, owner, succ, len(da), len(db), tc)
print(f"checked {ok + bad} o-acyclic C^1O games (skipped {skipped} with o on a cycle): agree {ok}, mismatch {bad}; max theta-changes {worst}")
