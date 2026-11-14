#!/usr/bin/env python3
"""L-SI box 109: the lane's own attack on a rule of n6.py by hill-climbing over small games (start S3).
Usage: climb109.py MODE N SEED RESTARTS STEPS [OUT.json]
State: a parity game on N vertices (priorities 0..2N, owners, successor lists, out-degree 1..4). Moves: change one priority, flip
one owner, add one edge, delete one edge (out-degree stays >= 1), redirect one edge. Accept if the objective does not fall.
Objective: iterations of MODE from S3 (n6.run, cap 20,000). Env ONEP=1: one-player games (every vertex Even's; the owner move is skipped). Prints the best count per restart and the overall best; with OUT.json
the best game (prio, owner, succ, iterations). Reference column: the same game under mode howard."""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE] + [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import pg, n6
mode, N, seed, restarts, steps = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
out = sys.argv[6] if len(sys.argv) > 6 else None
rng = random.Random(seed); ONEP = os.environ.get("ONEP") == "1"
def score(prio, owner, succ):
    g = pg.Game(list(prio), list(owner), [sorted(s) for s in succ]); r = n6.run(g, mode, cap=20000); return r["its"]
def rnd():
    prio = [rng.randrange(2 * N + 1) for _ in range(N)]; owner = [0 if ONEP else rng.randrange(2) for _ in range(N)]
    succ = [set(rng.sample(range(N), rng.randint(1, min(3, N)))) for _ in range(N)]; return prio, owner, succ
def mutate(prio, owner, succ):
    prio, owner, succ = list(prio), list(owner), [set(s) for s in succ]; k = rng.randrange(5); v = rng.randrange(N)
    if k == 0: prio[v] = rng.randrange(2 * N + 1)
    elif k == 1:
        if not ONEP: owner[v] = 1 - owner[v]
    elif k == 2:
        if len(succ[v]) < 4: succ[v].add(rng.randrange(N))
    elif k == 3:
        if len(succ[v]) > 1: succ[v].discard(rng.choice(sorted(succ[v])))
    else:
        w = rng.choice(sorted(succ[v])); succ[v].discard(w); succ[v].add(rng.randrange(N))
    return prio, owner, succ
best = (-1, None)
for r in range(restarts):
    cur = rnd(); sc = score(*cur)
    for t in range(steps):
        c = mutate(*cur); s = score(*c)
        if s >= sc: cur, sc = c, s
    if sc > best[0]: best = (sc, cur)
    print(f"C109 mode {mode} N {N} seed {seed} restart {r} best {sc}", flush=True)
sc, (prio, owner, succ) = best
g = pg.Game(list(prio), list(owner), [sorted(s) for s in succ]); h = n6.run(g, "howard", cap=20000)["its"]
print(f"C109 mode {mode} N {N} seed {seed}{' ONEP' if ONEP else ''} restarts {restarts} steps {steps}: BEST iterations {sc} (ratio to N {sc / N:.2f}); the same game under howard {h}", flush=True)
if out: json.dump(dict(mode=mode, prio=prio, owner=owner, succ=[sorted(s) for s in succ], iterations=sc), open(out, "w"))
