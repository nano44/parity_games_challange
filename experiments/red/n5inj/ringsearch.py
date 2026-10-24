"""L-RED box 28 (produced on Opus 5.5): random priority search on a FIXED o-cyclic C^1O ring template (R58 §11).
Template ring(L, EXITS, BAIL): o = 0 (Odd), sink t = 1 (Even self-loop, priority 0); chain c_i = i + 1 (i = 1..L, Even) with
c_i -> c_{i-1} (c_0 := o) and a bail edge: to t (BAIL=0) or to its own vertex b_i = L + 1 + i (Even, b_i -> t; BAIL=1).
o's exits: the c_i with i in EXITS ('all', 'odd', 'even'). Only priorities are searched (uniform in 0..2n).
Fitness: theta-changes inside one joint lambda-phase of the canonical N5 run (thetaclimb.stats), then iterations.
Usage: ringsearch.py L EXITS BAIL TRIALS SEED [OUT]"""
import os, random, sys
args = sys.argv[1:]
sys.argv = [sys.argv[0], "1", "0", "0", "/dev/null"]       # thetaclimb parses argv at import: dummies
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thetaclimb  # noqa: E402
import pg  # noqa: E402
L, ex, bail, trials, seed = int(args[0]), args[1], int(args[2]), int(args[3]), int(args[4])
out = args[5] if len(args) > 5 else None
rng = random.Random(seed)
n = 2 + L + (L if bail else 0)
E = [i for i in range(1, L + 1) if ex == "all" or (ex == "odd" and i % 2) or (ex == "even" and i % 2 == 0)]
owner = [1] + [0] * (n - 1)
succ = [sorted(i + 1 for i in E), [1]]
for i in range(1, L + 1):
    succ.append(sorted({i if i > 1 else 0, (L + 1 + i) if bail else 1}))
for i in range(1, L + 1):
    if bail: succ.append([1])
best = (-1, 0, None)
for t in range(trials):
    prio = [rng.randrange(2 * n) for _ in range(n)]; prio[1] = 0
    g = pg.Game(prio, owner, [list(s) for s in succ])
    try:
        b, tot, it = thetaclimb.stats(g)
    except Exception:
        continue
    if (b, it) > best[:2]: best = (b, it, prio)
print(f"ring L {L} exits {ex} bail {bail} n {n}: best theta-changes in one phase {best[0]}, iterations {best[1]}, prio {best[2]}")
if out and best[2]:
    with open(out, "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {best[2][v]} {owner[v]} {','.join(map(str, succ[v]))};\n")
