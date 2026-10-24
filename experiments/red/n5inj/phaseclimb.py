"""L-RED box 28 (produced on Opus 5.5): hill climb for the LONGEST JOINT lambda-PHASE of the canonical N5 run on games with at most
K Odd vertices of out-degree > 1 (Lead box-28 fallback: K = 2). Run via declines.states (n5.py replica, counts asserted = n5.run);
phases as in phaselen.py. Fitness: (longest phase, iterations, -edges). Usage: phaseclimb.py n K SECONDS SEED OUT [--from G.pg]
(--returns: fitness = (max returns at one vertex inside one joint lambda-phase, longest phase, -edges).
--from: G is padded with inert self-loop vertices up to n; Odd choice vertices beyond K are cut to one successor)"""
import os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
n, K, secs, seed, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed)
RET = "--returns" in sys.argv


def fix(G):
    pr, ow, su = G
    oc = [v for v in range(n) if ow[v] == 1 and len(su[v]) > 1]
    for v in oc[K:]: su[v] = su[v][:1]
    return (pr, ow, su)


def score(G):
    g = pg.Game(*[list(x) for x in G])
    try:
        seq = declines.states(g)
    except Exception:
        return (-1, 0, 0)
    E, Ed = Engine(g), Engine(n5.dual(g))
    lam = [(tuple(x[0] for x in E.evaluate(s)[0]), tuple(y[0] for y in Ed.evaluate(t)[0])) for s, t, _, _ in seq]
    best = cur = 0
    for k in range(1, len(seq)):
        cur = cur + 1 if lam[k] == lam[k - 1] else 1
        best = max(best, cur)
    if RET:
        mr = 0; used = {}; ret = {}
        for k in range(len(seq) - 1):
            if k == 0 or lam[k] != lam[k - 1]: used = {}; ret = {}
            for v in range(n):
                x, y = (seq[k][0][v], seq[k + 1][0][v]) if g.owner[v] == 0 else (seq[k][1][v], seq[k + 1][1][v])
                u = used.setdefault(v, set()); u.add(x)
                if x != y and lam[k + 1] == lam[k]:
                    if y in u: ret[v] = ret.get(v, 0) + 1; mr = max(mr, ret[v])
                    u.add(y)
        return (mr, best, -sum(len(x) for x in g.succ))
    return (best, len(seq) - 1, -sum(len(x) for x in g.succ))


def rand_game():
    return fix(([rng.randrange(2 * n) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]))


def mutate(G):
    pr, ow, su = list(G[0]), list(G[1]), [list(x) for x in G[2]]
    v = rng.randrange(n); r = rng.random()
    if r < 0.25: pr[v] = rng.randrange(2 * n + 2)
    elif r < 0.35: ow[v] = 1 - ow[v]
    elif r < 0.6 and len(su[v]) < 4: su[v] = sorted(set(su[v] + [rng.randrange(n)]))
    elif r < 0.8 and len(su[v]) > 1: su[v].pop(rng.randrange(len(su[v])))
    else: su[v][rng.randrange(len(su[v]))] = rng.randrange(n); su[v] = sorted(set(su[v]))
    return fix((pr, ow, su))


def write(G):
    with open(out + "_best.pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n")


if "--from" in sys.argv:
    g0 = pg.parse(open(sys.argv[sys.argv.index("--from") + 1]).read()); m0 = g0.n
    best = fix((list(g0.prio) + [0] * (n - m0), list(g0.owner) + [0] * (n - m0),
                [sorted(set(s)) for s in g0.succ] + [[v] for v in range(m0, n)]))
else:
    best = rand_game()
bs = score(best); t0 = time.time(); steps = 0
print(f"start {bs[:2]}", flush=True)
while time.time() - t0 < secs:
    steps += 1
    c = mutate(best); cs = score(c)
    if cs >= bs:
        if cs[:2] > bs[:2]:
            print(f"step {steps} t {time.time() - t0:.0f}s: longest phase {cs[0]}, iterations {cs[1]} (n {n}, K {K})", flush=True); write(c)
        best, bs = c, cs
write(best)
print(f"FINAL n {n} K {K} seed {seed}: longest phase {bs[0]}, iterations {bs[1]} after {steps} steps")
