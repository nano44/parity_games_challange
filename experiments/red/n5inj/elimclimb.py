"""L-RED box 30 (produced on Opus 5.5): hill climb against L-SI's CONJECTURE (ELIM-n) (docs/si/N5-OR-lens.md): find a joint
lambda-phase of a canonical N5 run with a run of NON-ELIMINATING transitions longer than n. Measure: L-SI's
experiments/si/orlens/elim.py elim_g UNMODIFIED (noelimrun_both = longest run of transitions in which every sigma-edge and every Odd
best-reply edge abandoned is used again later in the phase; L-SI 316ed69 corrected definition). Games: any (at most K Odd vertices with a choice; K = n allows all), mutations as phaseclimb.py.
Fitness: (max noelimrun over phases, its phase length, -edges). Prints REFUTED when noelimrun > n and stops.
Usage: elimclimb.py n K SECONDS SEED OUT [--from G.pg]"""
import os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(R0, "experiments", "si", "orlens"))
import elim as EL  # noqa: E402
sys.path.insert(0, HERE)
import pg  # noqa: E402
n, K, secs, seed, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed)


def fix(G):
    pr, ow, su = G
    oc = [v for v in range(n) if ow[v] == 1 and len(su[v]) > 1]
    for v in oc[K:]: su[v] = su[v][:1]
    return (pr, ow, su)


def score(G):
    g = pg.Game(*[list(x) for x in G])
    try:
        _, it, rows = EL.elim_g(g, None, 'n5', cap=20000)
    except Exception:
        return (-1, 0, 0)
    key = "noelimrun_both"            # L-SI 316ed69 definition: sigma- OR Odd-best-reply-edge elimination (Lead 14:10Z)
    r = max(rows, key=lambda q: (q[key], q["trans"]))
    return (r[key], r["trans"], -sum(len(x) for x in g.succ))


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


def write(G, path):
    with open(path, "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n")


if "--from" in sys.argv:
    g0 = pg.parse(open(sys.argv[sys.argv.index("--from") + 1]).read()); m0 = g0.n
    best = fix((list(g0.prio) + [0] * (n - m0), list(g0.owner) + [0] * (n - m0), [sorted(set(s)) for s in g0.succ] + [[v] for v in range(m0, n)]))
else:
    best = rand_game()
bs = score(best); t0 = time.time(); steps = 0; print("start", bs, flush=True)
while time.time() - t0 < secs:
    steps += 1; c = mutate(best); cs = score(c)
    if cs >= bs:
        if cs[:2] > bs[:2]: print(f"step {steps} t {time.time() - t0:.0f}s: window {cs[0]} phase {cs[1]} (n {n})", flush=True); write(c, out + "_best.pg")
        best, bs = c, cs
        if bs[0] > n: print("REFUTED (ELIM-n): window", bs[0], "> n", n, flush=True); write(best, out + "_REFUTED.pg"); break
write(best, out + "_best.pg"); print(f"FINAL n {n} K {K} seed {seed}: window {bs[0]} phase {bs[1]} after {steps} steps", flush=True)
