#!/usr/bin/env python3
"""Free-form hill-climb over small parity games maximising Oink DTL's learned-tangle count (L-RED, DTL box).
Fitness = tangles found by `oink --dtl --no-single --no-wcwc` (raw solver, no preprocessing). Mutations: add/remove an edge,
change a priority, flip an owner. Usage: dtl_search.py OINK n [--steps 20000] [--seed 0] [--maxpr P] [--even-min FRAC] [--fitness tangles|unsolved] [--out best.pg]"""
import sys, os, random, subprocess, tempfile, time, re
oink, n = sys.argv[1], int(sys.argv[2]); arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
steps, seed, maxpr = arg("--steps", 20000), arg("--seed", 0), arg("--maxpr", 2 * int(sys.argv[2])); rng = random.Random(seed)
evenmin = arg("--even-min", 0.0)
fitness = arg("--fitness", "tangles")   # tangles | unsolved (vertices DTL leaves unsolved: a completeness failure)      # reject games with fewer than this fraction of Even-owned vertices (two-player search)
tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name


def dumps(g):
    pr, ow, succ = g
    return f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, sorted(succ[v])))};\n" for v in range(n))


def score(g):
    open(tmp, "w").write(dumps(g))
    try:
        r = subprocess.run([oink, "--dtl", "--no-single", "--no-wcwc", tmp, tmp + ".sol"], capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        return 10 ** 6          # a timeout is interesting in itself
    if fitness == "unsolved":
        try: solved = sum(1 for l in open(tmp + ".sol") if l.strip() and not l.startswith("paritysol"))
        except FileNotFoundError: solved = n
        return n - solved
    m = re.search(r"found (\d+) dominions and (\d+) tangles", r.stdout + r.stderr)
    return int(m.group(2)) if m else -1


def random_game():
    pr = [rng.randrange(maxpr + 1) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    succ = [{rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))} for _ in range(n)]
    return pr, ow, succ


def mutate(g):
    pr, ow, succ = list(g[0]), list(g[1]), [set(s) for s in g[2]]
    v = rng.randrange(n); k = rng.random()
    if k < 0.4:
        w = rng.randrange(n)
        if w in succ[v] and len(succ[v]) > 1: succ[v].discard(w)
        else: succ[v].add(w)
    elif k < 0.75: pr[v] = rng.randrange(maxpr + 1)
    else: ow[v] ^= 1
    return pr, ow, succ


t0 = time.time(); g = random_game()
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
