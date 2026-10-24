"""L-RED box 25 (produced on Opus 5.5): hill climb for N5 iterations over SYMMETRIC games (R57 §6, requirement R-a).
A genome is a half-game H on vertices 0..h-1 whose successors range over 0..2h-1. The full game has 2h vertices: v (as in H) and its
mirror m(v) = v + h (or v - h) with owner 1 - owner(v), priority prio(v) + 1, and successors m(succ). So the game is invariant under
mirror + dual, and both players face the same structure.
Mutations (on H, mirrored automatically): change a priority; flip an owner; add, remove or redirect an edge.
Fitness: N5 iterations from the best-reward start (n5.run, experiments/new/n5.py, read-only); ties broken toward fewer edges.
Every improved best is written to OUT_best.pg; the final best is checked with Oink zlk + verify.py by the caller (check_sol2.py).
Usage: symclimb.py h SECONDS SEED OUT"""
import os
import random
import sys
import time

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("new", "si", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import n5  # noqa: E402
import pg  # noqa: E402

h, secs, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed)


def full(H):
    prio, owner, succ = [], [], []
    for v in range(h):
        p, o, s = H[v]
        prio.append(p); owner.append(o); succ.append(sorted(set(s)))
    for v in range(h):
        p, o, s = H[v]
        prio.append(p + 1); owner.append(1 - o); succ.append(sorted({(w + h) % (2 * h) for w in s}))
    return pg.Game(prio, owner, succ)


def score(H):
    g = full(H)
    try:
        it, fb, *_ = n5.run(g, "n5", None, 10 ** 5)
    except Exception:
        return (-1, 0)
    return (it, -sum(len(s) for s in g.succ))


def rand_half():
    H = []
    for v in range(h):
        k = rng.choice((1, 2, 2, 3))
        H.append([rng.randrange(2 * h), rng.randrange(2), rng.sample(range(2 * h), k)])
    return H


def mutate(H):
    H = [[p, o, list(s)] for p, o, s in H]
    v = rng.randrange(h); r = rng.random()
    if r < 0.25:
        H[v][0] = rng.randrange(2 * h + 2)
    elif r < 0.35:
        H[v][1] = 1 - H[v][1]
    elif r < 0.6 and len(H[v][2]) < 4:
        H[v][2].append(rng.randrange(2 * h))
    elif r < 0.8 and len(H[v][2]) > 1:
        H[v][2].pop(rng.randrange(len(H[v][2])))
    else:
        H[v][2][rng.randrange(len(H[v][2]))] = rng.randrange(2 * h)
    return H


def write(H, path):
    g = full(H)
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n):
            f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")


best = rand_half(); bs = score(best)
t0 = time.time(); steps = 0
while time.time() - t0 < secs:
    steps += 1
    c = mutate(best); cs = score(c)
    if cs >= bs:
        if cs[0] > bs[0]:
            print(f"step {steps} t {time.time() - t0:.0f}s: iterations {cs[0]} (n {2 * h})", flush=True)
            write(c, out + "_best.pg")
        best, bs = c, cs
write(best, out + "_best.pg")
print(f"FINAL h {h} n {2 * h} seed {seed}: iterations {bs[0]} after {steps} steps")
