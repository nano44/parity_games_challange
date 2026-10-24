"""L-RED box 26 (produced on Opus 5.5): hill climb on C^1O (exactly one Odd vertex o = 0 with out-degree > 1; every other Odd vertex has
one successor) for MANY CHANGES of the throttle theta = Xi_sigma(o) inside one joint lambda-phase (L-NEW box 21 Lemma G, §3.5-§3.6;
Lead routing 01:47Z). Run: canonical N5 (S3 best-reward start), via declines.states (n5.py replica, counts asserted = n5.run).
Fitness (lexicographic): max over joint lambda-phases of the theta-changes inside that phase; then total theta-changes; then
iterations; then fewer edges. Writes OUT_best.pg on every improvement. Usage: thetaclimb.py n SECONDS SEED OUT [--from G.pg]  (--from: start from G, whose Odd choice vertex is relabelled to 0)"""
import os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
n, secs, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed)


def stats(g):
    seq = declines.states(g); E, Ed = Engine(g), Engine(n5.dual(g))
    th, lam = [], []
    for s, t, _, _ in seq:
        X, _ = E.evaluate(s); th.append(X[0])
        lam.append((tuple(x[0] for x in X), tuple(y[0] for y in Ed.evaluate(t)[0])))
    best = cur = tot = 0
    for k in range(1, len(seq)):
        if lam[k] != lam[k - 1]: cur = 0
        if th[k] != th[k - 1]:
            tot += 1
            if lam[k] == lam[k - 1]: cur += 1
        best = max(best, cur)
    return best, tot, len(seq) - 1


def score(G):
    g = pg.Game(*[list(x) for x in G])
    try:
        b, t, it = stats(g)
    except Exception:
        return (-1, 0, 0, 0)
    return (b, t, it, -sum(len(x) for x in g.succ))


def fix(G):
    pr, ow, su = G
    ow[0] = 1
    if len(su[0]) < 2: su[0] = sorted(set(su[0] + [rng.randrange(n)]))
    for v in range(1, n):
        if ow[v] == 1 and len(su[v]) > 1: su[v] = [su[v][0]]
    return (pr, ow, su)


def rand_game():
    return fix(([rng.randrange(2 * n) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]))


def mutate(G):
    pr, ow, su = list(G[0]), list(G[1]), [list(x) for x in G[2]]
    v = rng.randrange(n); r = rng.random()
    if r < 0.25: pr[v] = rng.randrange(2 * n + 2)
    elif r < 0.35 and v: ow[v] = 1 - ow[v]
    elif r < 0.6 and len(su[v]) < 4: su[v] = sorted(set(su[v] + [rng.randrange(n)]))
    elif r < 0.8 and len(su[v]) > 1: su[v].pop(rng.randrange(len(su[v])))
    else: su[v][rng.randrange(len(su[v]))] = rng.randrange(n); su[v] = sorted(set(su[v]))
    return fix((pr, ow, su))


def write(G):
    with open(out + "_best.pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n")


def load(path):
    g0 = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    assert g0.n == n
    o = [v for v in range(n) if g0.owner[v] == 1 and len(set(g0.succ[v])) > 1][0]
    perm = list(range(n)); perm[0], perm[o] = o, 0          # swap o and 0
    pr = [g0.prio[perm[v]] for v in range(n)]; ow = [g0.owner[perm[v]] for v in range(n)]
    su = [sorted({perm[w] for w in g0.succ[perm[v]]}) for v in range(n)]
    return fix((pr, ow, su))


best = load(sys.argv[sys.argv.index("--from") + 1]) if "--from" in sys.argv else rand_game(); bs = score(best)
print(f"start: {bs[:3]}", flush=True); t0 = time.time(); steps = 0
while time.time() - t0 < secs:
    steps += 1
    c = mutate(best); cs = score(c)
    if cs >= bs:
        if cs[:3] > bs[:3]:
            print(f"step {steps} t {time.time() - t0:.0f}s: theta-changes in one phase {cs[0]}, total {cs[1]}, iterations {cs[2]} (n {n})", flush=True)
            write(c)
        best, bs = c, cs
write(best)
print(f"FINAL n {n} seed {seed}: theta-changes in one phase {bs[0]}, total {bs[1]}, iterations {bs[2]} after {steps} steps")
