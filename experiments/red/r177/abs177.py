#!/usr/bin/env python3
"""L-RED R177 ABS: the idealised TWO-FIX dynamics on a two-face game (docs/red/R177-tiebreak.md §3).
Even vertices x (low priority) choose among gates g (Odd, low). G_W: gate -> its W-target (one level down, graded, so every
option of x has the same W-value; c_W = top even self-loop => BFS lex-min regime). G_X: gate -> beta(target) -> X-target
(beta = Xi-only weight vertex), plays end at c_X. Dynamics = N5's S4a with tau = W-faces and sigma-bar = X-faces held FIXED:
  A_j(x) = {sigma_j(x)} u {Xi-improving options in G_X};  sigma_(j+1) = S1 optimum of the arena of G_W restricted to A_j.
No claim that tau / sigma-bar would stay fixed in N5 (that is the stabiliser question). Returns the run length (steps with sigma
changing) and whether W stayed constant (FL)."""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg, n5
from si import Engine
dual = n5.dual

def build(gen):
    """gen: dict levels: list of level per Even vertex (1..), opts: per x list of (wt, xt) with wt a vertex at level-1 (or 'W'),
    xt a vertex index or 'X'; bpar: per Even vertex (beta of target) parity/rank: brank[t] (distinct ints), bpar[t] in {0,1};
    order: permutation giving the index of each Even vertex and each gate."""
    N = len(gen["levels"]); opts = gen["opts"]
    names = [("x", i) for i in range(N)] + [("g", i, k) for i in range(N) for k in range(len(opts[i]))]
    perm = gen.get("perm") or list(range(len(names)))
    idx = {names[i]: perm[i] for i in range(len(names))}
    base = len(names)
    per = gen.get("bper", False)
    gl = [(i, k) for i in range(N) for k in range(len(opts[i]))]
    nb = len(gl) if per else N
    beta = {t: base + t for t in range(nb)}; cW = base + nb; cX = cW + 1; n = cX + 1
    prio = [0] * n; owner = [0] * n
    for i in range(N): prio[idx[("x", i)]] = 0; owner[idx[("x", i)]] = 0
    for i in range(N):
        for k in range(len(opts[i])): prio[idx[("g", i, k)]] = 1; owner[idx[("g", i, k)]] = 1
    for t in range(nb): prio[beta[t]] = 4 + 2 * gen["brank"][t] + gen["bpar"][t]; owner[beta[t]] = 0
    top = max(prio) + 2; top += top % 2
    prio[cW] = top; prio[cX] = 2
    sW = [[] for _ in range(n)]; sX = [[] for _ in range(n)]
    for i in range(N):
        x = idx[("x", i)]
        sW[x] = sorted(idx[("g", i, k)] for k in range(len(opts[i]))); sX[x] = list(sW[x])
        for k, (wt, xt) in enumerate(opts[i]):
            gg = idx[("g", i, k)]
            sW[gg] = [cW if wt == "W" else idx[("x", wt)]]
            if per:
                b = beta[gl.index((i, k))]; sX[gg] = [b]; tgt = cX if xt == "X" else idx[("x", xt)]; sW[b] = [tgt]; sX[b] = [tgt]
            else:
                sX[gg] = [cX if xt == "X" else beta[xt]]
    if not per:
        for t in range(N): sW[beta[t]] = [idx[("x", t)]]; sX[beta[t]] = [idx[("x", t)]]
    sW[cW] = [cW]; sX[cW] = [cW]; sW[cX] = [cX]; sX[cX] = [cX]
    return n, prio, owner, sW, sX, idx

def simulate(gen, cap=100000, start=None):
    n, prio, owner, sW, sX, idx = build(gen)
    GW = pg.Game(prio, owner, sW); GX = pg.Game(prio, owner, sX); EX = Engine(GX); EWfull = Engine(GW)
    sig = [-1] * n
    N = len(gen["levels"])
    for i in range(N):
        x = idx[("x", i)]; k = (start or gen.get("start"))[i]; sig[x] = idx[("g", i, k)]
    for v in range(n):
        if owner[v] == 0 and sig[v] == -1: sig[v] = sX[v][0]
    steps = 0; flsteps = 0; Wprev = EWfull.evaluate(tuple(sig))[0]; hist = []
    while steps < cap:
        vx, _ = EX.evaluate(tuple(sig)); Is = EX.improving(tuple(sig), vx)
        if not Is: return steps, flsteps, "opt", hist
        opt = {v: {sig[v]} for v in range(n) if owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if owner[v] == 0 else list(sW[v]) for v in range(n)]
        Er = Engine(dual(pg.Game(prio, owner, succ)))
        _, best = Er.evaluate(tuple(sW[v][0] if owner[v] == 1 else -1 for v in range(n)))
        ns = [best[v] if owner[v] == 0 else -1 for v in range(n)]
        if ns == sig:
            if os.environ.get("FB") != "1": return steps, flsteps, "stuck", hist
            ns = list(sig)
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (EX.key(vx[w]), w))
        Wn = EWfull.evaluate(tuple(ns))[0]
        steps += 1; flsteps += (Wn == Wprev); Wprev = Wn
        hist.append(sum(ns[v] != sig[v] for v in range(n)))
        sig = ns
    return steps, flsteps, "cap", hist

def randgen(N, L, deg, rng):
    levels = [1 + i * L // N for i in range(N)]
    bylev = {}
    for i, l in enumerate(levels): bylev.setdefault(l, []).append(i)
    opts = []
    for i in range(N):
        l = levels[i]; o = []
        for k in range(deg):
            wt = "W" if l == 1 else rng.choice(bylev[l - 1])
            xt = rng.choice(["X"] + [j for j in range(N) if j != i])
            o.append((wt, xt))
        opts.append(o)
    nn = N + N * deg
    perm = list(range(nn)); rng.shuffle(perm)
    br = list(range(N)); rng.shuffle(br)
    return dict(levels=levels, opts=opts, perm=perm, brank=br, bpar=[rng.randint(0, 1) for _ in range(N)],
                start=[rng.randrange(deg) for _ in range(N)])

def score(gen):
    try:
        s, f, why, _ = simulate(gen, cap=2000)
    except RuntimeError:
        return -1
    return f

def mutate(gen, rng, deg):
    g = json.loads(json.dumps(gen)); N = len(g["levels"])
    bylev = {}
    for i, l in enumerate(g["levels"]): bylev.setdefault(l, []).append(i)
    r = rng.random()
    if r < 0.35:
        i = rng.randrange(N); k = rng.randrange(deg); wt, xt = g["opts"][i][k]
        g["opts"][i][k] = [wt, rng.choice(["X"] + [j for j in range(N) if j != i])]
    elif r < 0.5:
        i = rng.randrange(N); k = rng.randrange(deg); wt, xt = g["opts"][i][k]; l = g["levels"][i]
        g["opts"][i][k] = ["W" if l == 1 else rng.choice(bylev[l - 1]), xt]
    elif r < 0.7:
        a, b = rng.randrange(len(g["perm"])), rng.randrange(len(g["perm"])); g["perm"][a], g["perm"][b] = g["perm"][b], g["perm"][a]
    elif r < 0.8:
        M = len(g["brank"]); a, b = rng.randrange(M), rng.randrange(M); g["brank"][a], g["brank"][b] = g["brank"][b], g["brank"][a]
    elif r < 0.9:
        i = rng.randrange(len(g["bpar"])); g["bpar"][i] ^= 1
    else:
        i = rng.randrange(N); g["start"][i] = rng.randrange(deg)
    return g

if __name__ == "__main__":
    N, L, deg, iters, seed = (int(a) for a in sys.argv[1:6])
    rng = random.Random(seed); best = randgen(N, L, deg, rng); bs = score(best)
    for it in range(iters):
        c = mutate(best, rng, deg); cs = score(c)
        if cs >= bs:
            if cs > bs: print("IT", it, "FL", cs, flush=True)
            best, bs = c, cs
    out = os.environ.get("OUT")
    if out: json.dump(best, open(out, "w"))
    print("BEST", N, L, deg, bs, simulate(best)[:3])

def laddergen(d, rng):
    """W = ladder: levels 1..d, two Even vertices per level (a_l = 2(l-1), b_l = 2(l-1)+1); options k = 0 (W -> a_(l-1)), 1 (W -> b_(l-1));
    level 1: both options -> c_W. Xi-targets random (any other Even vertex or X)."""
    N = 2 * d; levels = [1 + i // 2 for i in range(N)]; opts = []
    for i in range(N):
        l = levels[i]; o = []
        for k in range(2):
            wt = "W" if l == 1 else 2 * (l - 2) + k
            o.append((wt, rng.choice(["X"] + [j for j in range(N) if j != i])))
        opts.append(o)
    nn = N + 2 * N; perm = list(range(nn)); rng.shuffle(perm); br = list(range(N)); rng.shuffle(br)
    return dict(levels=levels, opts=opts, perm=perm, brank=br, bpar=[rng.randint(0, 1) for _ in range(N)],
                start=[rng.randrange(2) for _ in range(N)])
