"""L-RED box 26 (produced on Opus 5.5): hill climb for long FROZEN N5 runs (L-NEW box 21 Theorem B (c): from (sigma_0, tau*) with
tau* honest-optimal, N5 = Even's run against a frozen tau*), steered toward WIDE gates (R58 §7, Corollary W2).
Game: n vertices, mutated freely (priority, owner, edges). Start: sigma_0 = S3 best-reward; tau* = Odd's optimum from Odd's
switch-all SI on G^d (si.py Engine, best-reward start; I_tau* = empty is asserted). N5 = experiments/new/n5.py via
declines.states (loop replica, counts asserted = n5.run).
Fitness (lexicographic, MODE): 'wide' = (# moves with gate |I_sigma| >= KMIN and >= 2 refused, iterations, -edges);
'len' = (iterations, # wide moves, -edges). Writes OUT_best.pg and OUT_best.start on every improvement.
Usage: frozenclimb.py n SECONDS SEED OUT MODE [KMIN]"""
import os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import declines  # noqa: E402
import frozen  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
n, secs, seed, out, mode = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
KMIN = int(sys.argv[6]) if len(sys.argv) > 6 else 3
rng = random.Random(seed)


def start_of(g):
    tau = frozen.odd_optimal(g); E = Engine(g); s0 = E.initial("best")
    return ({v: s0[v] for v in range(g.n) if g.owner[v] == 0}, {v: tau[v] for v in range(g.n) if g.owner[v] == 1})


def score(G):
    g = pg.Game(*[list(x) for x in G])
    try:
        st = start_of(g); seq = declines.states(g, st)
    except Exception:
        return (-1, 0, 0), None
    assert not seq[0][3], "tau* not honest-optimal"
    W = 0
    for t in range(len(seq) - 1):
        s, s2 = seq[t][0], seq[t + 1][0]
        if s == s2 or len(seq[t][2]) < KMIN: continue
        if len(seq[t][2]) - sum(1 for v in range(g.n) if s[v] != s2[v]) >= 2: W += 1
    it = len(seq) - 1; e = -sum(len(x) for x in g.succ)
    return ((W, it, e) if mode == "wide" else (it, W, e)), st


def rand_game():
    return ([rng.randrange(2 * n) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
            [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)])


def mutate(G):
    pr, ow, su = list(G[0]), list(G[1]), [list(x) for x in G[2]]
    v = rng.randrange(n); r = rng.random()
    if r < 0.25: pr[v] = rng.randrange(2 * n + 2)
    elif r < 0.35: ow[v] = 1 - ow[v]
    elif r < 0.6 and len(su[v]) < 4: su[v] = sorted(set(su[v] + [rng.randrange(n)]))
    elif r < 0.8 and len(su[v]) > 1: su[v].pop(rng.randrange(len(su[v])))
    else: su[v][rng.randrange(len(su[v]))] = rng.randrange(n); su[v] = sorted(set(su[v]))
    return (pr, ow, su)


def write(G, st):
    with open(out + "_best.pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n")
    with open(out + "_best.start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[0].items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[1].items())) + "\n")


best = rand_game(); bs, bst = score(best); t0 = time.time(); steps = 0
while time.time() - t0 < secs:
    steps += 1
    c = mutate(best); cs, cst = score(c)
    if cs >= bs:
        if cs[:2] > bs[:2]:
            print(f"step {steps} t {time.time() - t0:.0f}s: {mode} fitness {cs[:2]} (n {n})", flush=True)
            write(c, cst)
        best, bs, bst = c, cs, cst
if bst: write(best, bst)
print(f"FINAL n {n} seed {seed} mode {mode} KMIN {KMIN}: fitness {bs[:2]} after {steps} steps")
