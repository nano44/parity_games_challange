"""L-RED box 29 (produced on Opus 5.5): random priority search on a RE-ROOTED RING template (R58 §12), testing whether k roots
re-arm an absorbing chain k times inside one joint lambda-phase (in-phase count ~ k*L).
Template rr(L, k), o-cyclic C^1O: o = 0 (Odd); sink t = 1 (Even self-loop, priority 0);
  chain c_1..c_L (Even): c_i -> {c_{i-1}, b_i}, c_1 -> {h, b_1}; bails b_i (Even) -> t;
  hub h (Even) -> {r_1..r_k}; roots r_j (Even) -> {o, a_j}; root bails a_j (Even) -> t;
  o's exits: every chain vertex c_i with i in EXITS ('all' | 'odd') plus every a_j (so Odd can punish a root's bail).
Only priorities are searched. Fitness: longest joint lambda-phase of the canonical N5 run (phaseclimb's measure), then iterations.
Usage: rootsearch.py L k EXITS TRIALS SEED [OUT] [--climb]  (--climb: TRIALS = seconds of hill climbing over priorities)"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
L, k, ex, trials, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
out = sys.argv[6] if len(sys.argv) > 6 else None
rng = random.Random(seed)
O, T = 0, 1
C = list(range(2, 2 + L)); B = list(range(2 + L, 2 + 2 * L)); H = 2 + 2 * L
R = list(range(H + 1, H + 1 + k)); A = list(range(H + 1 + k, H + 1 + 2 * k)); n = H + 1 + 2 * k
owner = [0] * n; owner[O] = 1
succ = [None] * n
succ[T] = [T]
for i in range(L):
    succ[C[i]] = sorted({C[i - 1] if i else H, B[i]}); succ[B[i]] = [T]
succ[H] = sorted(R)
for j in range(k):
    succ[R[j]] = sorted({O, A[j]}); succ[A[j]] = [T]
succ[O] = sorted([C[i] for i in range(L) if ex == "all" or i % 2 == 0] + A)


def longest_phase(g):
    seq = declines.states(g); E, Ed = Engine(g), Engine(n5.dual(g))
    lam = [(tuple(x[0] for x in E.evaluate(s)[0]), tuple(y[0] for y in Ed.evaluate(t)[0])) for s, t, _, _ in seq]
    best = cur = 0
    for i in range(1, len(seq)):
        cur = cur + 1 if lam[i] == lam[i - 1] else 1
        best = max(best, cur)
    return best, len(seq) - 1


import time
if "--climb" in sys.argv:
    cur = [rng.randrange(2 * n) for _ in range(n)]; cur[T] = 0
    cs = longest_phase(pg.Game(cur, owner, [list(x) for x in succ])); t0 = time.time()
    while time.time() - t0 < trials:
        c = list(cur); v = rng.randrange(n)
        if v == T: continue
        c[v] = rng.randrange(2 * n + 2)
        try:
            sc = longest_phase(pg.Game(c, owner, [list(x) for x in succ]))
        except Exception:
            continue
        if sc >= cs:
            if sc > cs: print(f"t {time.time() - t0:.0f}s: longest phase {sc[0]}, iterations {sc[1]}", flush=True)
            cur, cs = c, sc
    trials = 0
    best = (cs[0], cs[1], cur)
else:
    best = (-1, 0, None)
for _ in range(trials):
    prio = [rng.randrange(2 * n) for _ in range(n)]; prio[T] = 0
    g = pg.Game(prio, owner, [list(s) for s in succ])
    try:
        b, it = longest_phase(g)
    except Exception:
        continue
    if (b, it) > best[:2]: best = (b, it, prio)
print(f"rr L {L} k {k} exits {ex} n {n}: best longest phase {best[0]}, iterations {best[1]}")
if out and best[2]:
    with open(out, "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {best[2][v]} {owner[v]} {','.join(map(str, succ[v]))};\n")
