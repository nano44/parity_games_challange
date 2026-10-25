#!/usr/bin/env python3
"""Box 41: FB-CAP attack. Random 𝒞^1O games (n in [nmin, nmax]) × random start pairs (ex16.trace); per phase g − max(1, |U| − 2) and
per θ-run f − max(1, |U| − 2) (FB-CAP: ≤ 0). Saves games + starts with a positive value as OUT_k.json and prints them.
Usage: rstart17.py seed secs nmin nmax starts OUT"""
import sys, os, random, time, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import ex16, sox, pg
seed, secs, nmin, nmax, K, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed); t0 = time.time(); runs = 0; best = {}; hits = 0
while time.time() - t0 < secs:
    n = rng.randint(nmin, nmax)
    prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
    o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
    try: g = pg.Game(prio, owner, succ)
    except Exception: continue
    if len(sox.oddchoice(g)) != 1: continue
    for _ in range(K):
        st = [rng.choice(g.succ[v]) for v in range(n)]
        try: S, FB, E = ex16.trace(g, st)
        except Exception: continue
        runs += 1; o = sox.oddchoice(g)[0]
        X = [E.evaluate(tuple(s))[0] for s, t in S]; N = len(S); a = 0
        while a < N:
            b = a
            while b + 1 < N and [x[0] for x in X[b + 1]] == [x[0] for x in X[a]] and S[b + 1][1] == S[a][1]: b += 1
            ct = X[a][o][0]; u = sum(1 for z in range(n) if X[a][z][0] == ct)
            gph = sum(1 for k in range(a, b) if FB[k] and S[k][0] != S[k + 1][0]); e = gph - max(1, u - 2)
            best[u] = max(best.get(u, -99), e)
            if e > 0 and hits < 20:
                hits += 1; json.dump(dict(prio=prio, owner=owner, succ=succ, start=st, phase=a, u=u, g=gph), open(f"{out}_{hits}.json", "w"))
                print("HIT", hits, n, u, gph, flush=True)
            a = b + 1
print("runs", runs, "best g - max(1,u-2) by u", sorted(best.items()), flush=True)
