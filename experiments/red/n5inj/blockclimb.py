"""L-RED box 27 (produced on Opus 5.5): climb for L-NEW's kill target (b) (N5-1O-box22.md §6-§7, Lead relay 02:16Z): a long
PURE-Y BLOCK on o-acyclic C^1O. Games: o = 0 (the only Odd choice vertex) has exits to K terminal sinks (self-loops; X = the sinks,
no choices, so sigma|X never changes and theta is constant once tau is), Y = the other vertices (Even, or Odd with one successor),
whose edges may enter o. So after tau's last change the canonical N5 run is ONE pure-Y block: L-NEW's static problem (STAT).
Fitness: (iterations after tau's last change, iterations, -edges). Run via declines.states (n5.py replica, counts asserted).
Usage: blockclimb.py NY K SECONDS SEED OUT [--from G.pg (must have this layout: o = 0, sinks 1..K)]"""
import os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import pg  # noqa: E402
ny, K, secs, seed, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
n = 1 + K + ny; rng = random.Random(seed)
Y = list(range(1 + K, n))


def fix(G):
    pr, ow, su = G
    ow[0] = 1; su[0] = sorted(set(w for w in su[0] if 1 <= w <= K)) or [1]
    if len(su[0]) < 2: su[0] = sorted(set(su[0] + [1 + (su[0][0] % K)]))
    for s in range(1, K + 1): ow[s] = 0; su[s] = [s]
    for v in Y:
        su[v] = sorted(set(w for w in su[v] if w != v or True))
        if ow[v] == 1: su[v] = su[v][:1]
    return (pr, ow, su)


def rand_game():
    return fix(([rng.randrange(2 * n) for _ in range(n)], [0] + [0] * K + [rng.choice((0, 0, 0, 1)) for _ in Y],
                [rng.sample(range(1, K + 1), min(K, 3))] + [[s] for s in range(1, K + 1)] +
                [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in Y]))


def mutate(G):
    pr, ow, su = list(G[0]), list(G[1]), [list(x) for x in G[2]]
    r = rng.random()
    if r < 0.1:
        v = 0; su[0] = sorted(set(su[0] + [rng.randint(1, K)])) if rng.random() < 0.5 or len(su[0]) <= 2 else su[0][1:]
    elif r < 0.3:
        v = rng.randrange(n); pr[v] = rng.randrange(2 * n + 2)
    else:
        v = rng.choice(Y); q = rng.random()
        if q < 0.15: ow[v] = 1 - ow[v]
        elif q < 0.45 and len(su[v]) < 4: su[v] = sorted(set(su[v] + [rng.randrange(n)]))
        elif q < 0.7 and len(su[v]) > 1: su[v].pop(rng.randrange(len(su[v])))
        else: su[v][rng.randrange(len(su[v]))] = rng.randrange(n); su[v] = sorted(set(su[v]))
    return fix((pr, ow, su))


def score(G):
    g = pg.Game(*[list(x) for x in G])
    try:
        seq = declines.states(g)
    except Exception:
        return (-1, 0, 0)
    last = max([k for k in range(1, len(seq)) if seq[k][1] != seq[k - 1][1]], default=0)
    return (len(seq) - 1 - last, len(seq) - 1, -sum(len(x) for x in g.succ))


def write(G):
    with open(out + "_best.pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n")


if "--from" in sys.argv:
    g0 = pg.parse(open(sys.argv[sys.argv.index("--from") + 1]).read()); best = fix((list(g0.prio), list(g0.owner), [list(s) for s in g0.succ]))
else:
    best = rand_game()
bs = score(best); t0 = time.time(); steps = 0
print(f"start {bs[:2]} (|Y| {ny}, K {K})", flush=True)
while time.time() - t0 < secs:
    steps += 1
    c = mutate(best); cs = score(c)
    if cs >= bs:
        if cs[:2] > bs[:2]:
            print(f"step {steps} t {time.time() - t0:.0f}s: block {cs[0]}, iterations {cs[1]} (|Y| {ny})", flush=True); write(c)
        best, bs = c, cs
write(best)
print(f"FINAL |Y| {ny} K {K} seed {seed}: block {bs[0]}, iterations {bs[1]} after {steps} steps")
