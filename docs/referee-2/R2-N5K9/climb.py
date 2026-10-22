"""Hill-climb over one-player (+) games on n vertices to maximise the longest improvement chain (mode single|any|sa).
Game encoding: prio (0..n), owner, succ; Odd vertices have out-degree 1; Even out-degree 1..3. Mutations: change one priority,
one owner, one successor list. Accept if the objective does not decrease. Prints the best game found."""
import sys, os, random, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from onep import *
def rand_game(n, rnd):
    prio = [rnd.randint(0, n) for _ in range(n)]; owner = [rnd.randint(0, 1) for _ in range(n)]
    succ = [rnd.sample(range(n), 1 if owner[v] else rnd.randint(1, min(3, n))) for v in range(n)]
    return prio, owner, succ
def mutate(gm, n, rnd):
    prio, owner, succ = [list(x) for x in gm[:2]] + [[list(s) for s in gm[2]]]
    k = rnd.randint(0, 2); v = rnd.randrange(n)
    if k == 0: prio[v] = rnd.randint(0, n)
    elif k == 1:
        owner[v] = 1 - owner[v]
        if owner[v] == 1: succ[v] = [rnd.choice(succ[v])]
    if k == 2 or (k == 1 and owner[v] == 0):
        succ[v] = rnd.sample(range(n), 1 if owner[v] else rnd.randint(1, min(3, n)))
    return prio, owner, succ
def obj(gm, mode): return longest(OneP(Game(*gm)), mode)
n, mode, secs, seed = int(sys.argv[1]), sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
rnd = random.Random(seed); t0 = time.time()
best = rand_game(n, rnd); bv = obj(best, mode); cur, cv = best, bv
while time.time() - t0 < secs:
    if rnd.random() < 0.02: cur = rand_game(n, rnd); cv = obj(cur, mode)
    nx = mutate(cur, n, rnd); v = obj(nx, mode)
    if v >= cv: cur, cv = nx, v
    if cv > bv: best, bv = cur, cv
print('CLIMB n=%d mode=%s secs=%g seed=%d best=%d game=%r' % (n, mode, secs, seed, bv, best), flush=True)
