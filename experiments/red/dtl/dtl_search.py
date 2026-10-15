#!/usr/bin/env python3
"""Free-form hill-climb over small parity games maximising Oink DTL's learned-tangle count (L-RED, DTL box).
Fitness = tangles found by `oink --dtl --no-single --no-wcwc --no-loops` (raw solver, no preprocessing, self-loops kept;
before 16:02Z the runs used --no-single --no-wcwc only). Mutations: add/remove an edge,
change a priority, flip an owner. Usage: dtl_search.py OINK n [--steps 20000] [--seed 0] [--maxpr P] [--even-min FRAC] [--fitness tangles|unsolved|wrong|perhead|perheadsearch|persearch] [--injective] [--loops] [--solver dtl|idtl] [--from game.pg] [--out best.pg]"""
import sys, os, random, subprocess, tempfile, time, re
oink, n = sys.argv[1], int(sys.argv[2]); arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
steps, seed, maxpr = arg("--steps", 20000), arg("--seed", 0), arg("--maxpr", 2 * int(sys.argv[2])); rng = random.Random(seed)
evenmin = arg("--even-min", 0.0)
SOLVER = "--" + arg("--solver", "dtl")         # dtl | idtl
OINKFLAGS = ["--no-single", "--no-wcwc", "--no-loops"]   # the pinned algorithm (CHECKER C3): no preprocessing, self-loops kept
loops = "--loops" in sys.argv                  # bias mutations toward self-loops and toward renumbering equal-priority vertices
fitness = arg("--fitness", "tangles")   # tangles | unsolved (vertices DTL leaves unsolved) | perhead (max tangles learned at one top priority; use --injective)
injective = "--injective" in sys.argv    # priorities = a permutation of 0..n-1, so a tangle's priority names its top      # reject games with fewer than this fraction of Even-owned vertices (two-player search)
tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name


def dumps(g):
    pr, ow, succ = g
    return f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, sorted(succ[v])))};\n" for v in range(n))


def score(g):
    open(tmp, "w").write(dumps(g))
    try:
        r = subprocess.run([oink, SOLVER] + OINKFLAGS + (["-t", "-t"] if fitness.startswith("per") else []) + (["-v"] if fitness == "wrong" else []) + [tmp, tmp + ".sol"], capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        return 10 ** 6          # a timeout is interesting in itself
    if fitness in ("unsolved", "wrong"):
        try: solved = sum(1 for l in open(tmp + ".sol") if l.strip() and not l.startswith("paritysol"))
        except FileNotFoundError: solved = n
        bad = 0
        if fitness == "wrong":      # Oink's own verifier (-v): a failed verification or a solver error counts 1000
            out = r.stdout + r.stderr
            bad = 1000 if ("error" in out.lower() or "verified" not in out) else 0
        return n - solved + bad
    if fitness in ("perhead", "perheadsearch", "persearch"):
        import collections
        c = collections.Counter(); it = 0
        for line in re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr).splitlines():
            if "iteration" in line: it += 1
            m2 = re.search(r"new tangle (\d+) \(", line)
            if m2: c[("*" if fitness == "persearch" else m2.group(1), 0 if fitness == "perhead" else it)] += 1
        return max(c.values(), default=0)
    m = re.search(r"found (\d+) dominions and (\d+) tangles", r.stdout + r.stderr)
    return int(m.group(2)) if m else -1


def random_game():
    pr = rng.sample(range(n), n) if injective else [rng.randrange(maxpr + 1) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    succ = [{rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))} for _ in range(n)]
    return pr, ow, succ


def mutate(g):
    pr, ow, succ = list(g[0]), list(g[1]), [set(s) for s in g[2]]
    v = rng.randrange(n); k = rng.random()
    if loops and k < 0.3:                      # self-loop on/off (never removed as the only edge)
        if v in succ[v] and len(succ[v]) > 1: succ[v].discard(v)
        else: succ[v].add(v)
        return pr, ow, succ
    if loops and k < 0.45:                     # swap the ids of two vertices of equal priority (tie order of the sort)
        same = [w for w in range(n) if pr[w] == pr[v] and w != v]
        if same:
            w = rng.choice(same)
            def sw(x): return w if x == v else v if x == w else x
            pr[v], pr[w] = pr[w], pr[v]; ow[v], ow[w] = ow[w], ow[v]
            succ = [set(map(sw, succ[sw(x)])) for x in range(n)]
        return pr, ow, succ
    if k < 0.4:
        w = rng.randrange(n)
        if w in succ[v] and len(succ[v]) > 1: succ[v].discard(w)
        else: succ[v].add(w)
    elif k < 0.75:
        if injective: w = rng.randrange(n); pr[v], pr[w] = pr[w], pr[v]
        else: pr[v] = rng.randrange(maxpr + 1)
    else: ow[v] ^= 1
    return pr, ow, succ


t0 = time.time(); g = random_game()
if "--from" in sys.argv:      # start from a given game (perturbation search); n is taken from the file
    pr, ow, succ = [], [], []
    for line in open(sys.argv[sys.argv.index("--from") + 1]):
        m = re.match(r"^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line.strip())
        if m: pr.append(int(m.group(2))); ow.append(int(m.group(3))); succ.append({int(x) for x in m.group(4).split(",")})
    n = len(pr); maxpr = max(maxpr, max(pr)); g = (pr, ow, succ)
while evenmin and g[1].count(0) < evenmin * n: g = random_game()
cur = score(g); best = (cur, g)
for i in range(steps):
    h = mutate(g)
    if evenmin and h[1].count(0) < evenmin * n: continue
    sc = score(h)
    if sc >= cur:
        g, cur = h, sc
        if sc > best[0]:
            best = (sc, h); print(f"step {i}: {sc} tangles ({time.time() - t0:.0f}s)", flush=True)
            if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(dumps(h))
if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(dumps(best[1]))
os.unlink(tmp)
print(f"n={n} seed={seed}: best {best[0]} tangles after {steps} steps ({time.time() - t0:.0f}s)")
