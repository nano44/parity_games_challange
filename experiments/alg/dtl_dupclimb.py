#!/usr/bin/env python3
"""L-ALG (2026-10-15, DTL step 4, GAP-C shape β): hill-climb on random games with fitness = (#unsolved vertices) * 1000 +
(#"duplicate tangle" lines in the dtl trace). A duplicate extraction at a closed region is the signature of shape (β) in
docs/alg/DTL-proof.md §2.3; unsolved vertices would be a completeness failure. Release Oink prints "duplicate tangle" at -t.
Usage: dtl_dupclimb.py OINK OUTDIR STEPS SEED [n]. Writes the best game to OUTDIR/best_<seed>.pg and prints progress."""
import sys, os, re, random, subprocess
oink, outdir, steps, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
n = int(sys.argv[5]) if len(sys.argv) > 5 else 12
os.makedirs(outdir, exist_ok=True); rng = random.Random(seed)
def rand_game():
    return [(rng.randint(0, n), rng.randint(0, 1), sorted(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
def write(g, path):
    with open(path, "w") as f:
        f.write(f"parity {n};\n")
        for i, (p, o, succ) in enumerate(g): f.write(f"{i} {p} {o} {','.join(map(str, succ))};\n")
def fitness(g):
    path = os.path.join(outdir, f"cur_{seed}.pg"); write(g, path)
    r = subprocess.run([oink, "--dtl", "-t", "--no-single", "--no-wcwc", path, path + ".sol"], capture_output=True, text=True, timeout=60)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    dups = out.count("duplicate tangle")
    unsolved = 0
    try:
        lines = open(path + ".sol").read().split("\n")[1:]
        solved = sum(1 for l in lines if l.strip())
        unsolved = n - solved
    except Exception: unsolved = n
    return unsolved * 1000 + dups, dups, unsolved
def mutate(g):
    g = [(p, o, list(s)) for p, o, s in g]; i = rng.randrange(n); k = rng.randrange(4)
    if k == 0: g[i] = (rng.randint(0, n), g[i][1], g[i][2])
    elif k == 1: g[i] = (g[i][0], 1 - g[i][1], g[i][2])
    elif k == 2:
        t = rng.randrange(n)
        if t not in g[i][2]: g[i][2].append(t); g[i][2].sort()
    else:
        if len(g[i][2]) > 1: g[i][2].remove(rng.choice(g[i][2]))
    return g
g = rand_game(); best, bd, bu = fitness(g); print("start", best, bd, bu, flush=True)
for step in range(steps):
    g2 = mutate(g); f2, d2, u2 = fitness(g2)
    if f2 >= best:
        if f2 > best: print(f"step {step}: fitness {f2} (dups {d2}, unsolved {u2})", flush=True); write(g2, os.path.join(outdir, f"best_{seed}.pg"))
        g, best, bd, bu = g2, f2, d2, u2
    if step % 2000 == 0 and step: print(f"step {step}: best {best}", flush=True)
print("done", best, bd, bu)
