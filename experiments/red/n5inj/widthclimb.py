"""L-RED box 26 (produced on Opus 5.5): hill climb for N5 runs that live at WIDE improving sets (R58 §5, (K1)+(K3)).
Search space as experiments/red/n5/symclimb.py (games invariant under mirror + dual; genome = half game on 0..h-1).
Fitness (lexicographic): W = number of N5 moves whose mover has |I| >= KMIN and refuses >= 2 of them while the opponent's |I| >= 1
(generosity of a NON-optimal opponent), then N5 iterations, then fewer edges. N5 = experiments/new/n5.py via declines.states
(loop replica, counts asserted = n5.run). Writes OUT_best.pg on every improvement of W or iterations.
Usage: widthclimb.py h SECONDS SEED OUT [KMIN] [--from G.pg]"""
import os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import pg  # noqa: E402
h, secs, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
KMIN = int(sys.argv[5]) if len(sys.argv) > 5 and not sys.argv[5].startswith("--") else 4
rng = random.Random(seed)


def full(H):
    prio, owner, succ = [], [], []
    for p, o, s in H: prio.append(p); owner.append(o); succ.append(sorted(set(s)))
    for p, o, s in H: prio.append(p + 1); owner.append(1 - o); succ.append(sorted({(w + h) % (2 * h) for w in s}))
    return pg.Game(prio, owner, succ)


def score(H):
    g = full(H)
    try:
        seq = declines.states(g)
    except Exception:
        return (-1, 0, 0)
    W = 0
    for t in range(len(seq) - 1):
        for k, I, J in ((0, 2, 3), (1, 3, 2)):
            s, s2 = seq[t][k], seq[t + 1][k]
            if s == s2 or len(seq[t][I]) < KMIN: continue
            r = len(seq[t][I]) - sum(1 for v in range(g.n) if s[v] != s2[v])
            if r >= 2 and len(seq[t][J]) >= 1: W += 1
    return (W, len(seq) - 1, -sum(len(s) for s in g.succ))


def rand_half():
    return [[rng.randrange(2 * h), rng.randrange(2), rng.sample(range(2 * h), rng.choice((1, 2, 2, 3)))] for _ in range(h)]


def mutate(H):
    H = [[p, o, list(s)] for p, o, s in H]
    v = rng.randrange(h); r = rng.random()
    if r < 0.25: H[v][0] = rng.randrange(2 * h + 2)
    elif r < 0.35: H[v][1] = 1 - H[v][1]
    elif r < 0.6 and len(H[v][2]) < 4: H[v][2].append(rng.randrange(2 * h))
    elif r < 0.8 and len(H[v][2]) > 1: H[v][2].pop(rng.randrange(len(H[v][2])))
    else: H[v][2][rng.randrange(len(H[v][2]))] = rng.randrange(2 * h)
    return H


def write(H, path):
    g = full(H)
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")


if "--from" in sys.argv:
    g0 = pg.parse("".join(l for l in open(sys.argv[sys.argv.index("--from") + 1]) if not l.lstrip().startswith("%")))
    assert g0.n == 2 * h
    best = [[g0.prio[v], g0.owner[v], list(g0.succ[v])] for v in range(h)]
else:
    best = rand_half()
bs = score(best); t0 = time.time(); steps = 0
print(f"start: W {bs[0]} iterations {bs[1]}", flush=True)
while time.time() - t0 < secs:
    steps += 1
    c = mutate(best); cs = score(c)
    if cs >= bs:
        if cs[:2] > bs[:2]:
            print(f"step {steps} t {time.time() - t0:.0f}s: W {cs[0]} iterations {cs[1]} (n {2 * h})", flush=True)
            write(c, out + "_best.pg")
        best, bs = c, cs
write(best, out + "_best.pg")
print(f"FINAL h {h} n {2 * h} seed {seed} KMIN {KMIN}: W {bs[0]} iterations {bs[1]} after {steps} steps")
