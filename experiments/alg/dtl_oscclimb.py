#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A attack): hill-climb for a SMALL game in which one vertex's membership in one top's SCC oscillates
across searches (the F8/F9 mechanism), to dissect the flip-flop by hand. Needs the DEBUG build (true tops: the `region` line
before each `new tangle` line). Fitness = (max membership changes over (top, vertex) pairs, searches, tangles).
Usage: dtl_oscclimb.py DEBUG_OINK OUTDIR n seed steps [--pmax P] [--seedgame G]"""
import sys, os, random, re, subprocess, collections
oink, outdir, n, seed, steps = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
pmax = int(sys.argv[sys.argv.index("--pmax") + 1]) if "--pmax" in sys.argv else n
os.makedirs(outdir, exist_ok=True); rng = random.Random(seed)
def rand_game():
    return [rng.randint(0, pmax) for _ in range(n)], [rng.randint(0, 1) for _ in range(n)], [sorted(rng.sample(range(n), rng.randint(1, 3))) for _ in range(n)]
def mutate(g):
    pr, ow, succ = list(g[0]), list(g[1]), [list(s) for s in g[2]]
    for _ in range(rng.randint(1, 3)):
        v = rng.randrange(n); k = rng.random()
        if k < 0.3: pr[v] = rng.randint(0, pmax)
        elif k < 0.45: ow[v] ^= 1
        elif k < 0.75:
            w = rng.randrange(n)
            if w in succ[v]:
                if len(succ[v]) > 1: succ[v].remove(w)
            else: succ[v].append(w); succ[v].sort()
        else: succ[v] = sorted(rng.sample(range(n), rng.randint(1, 3)))
    return pr, ow, succ
def write(g, path):
    with open(path, "w") as f:
        f.write(f"parity {n};\n")
        for v in range(n): f.write(f"{v} {g[0][v]} {g[1][v]} {','.join(map(str, g[2][v]))} \"v{v}\";\n")
def read_game(path):
    pr, ow, succ = [], [], []
    for line in open(path):
        f = line.strip().rstrip(";").split()
        if len(f) >= 4 and f[0].isdigit(): pr.append(int(f[1])); ow.append(int(f[2])); succ.append(sorted(int(x) for x in f[3].split(",")))
    return pr, ow, succ
def vid(tok): return int(tok.split("->")[0][1:])
def fitness(g, path):
    write(g, path)
    try: r = subprocess.run([oink, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", path], capture_output=True, text=True, timeout=30)
    except Exception: return (0, 0, 0)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    searches = 0; top = None; seq = collections.defaultdict(list); ntang = 0
    for line in out.splitlines():
        line = re.sub(r"^\[ *[0-9.]*\] ", "", line)
        if re.match(r"iteration \d+-(even|odd)", line): searches += 1; continue
        m = re.match(r"region (\d+)(.*)", line)
        if m:
            vs = [vid(t) for t in m.group(2).split()]; top = vs[0] if vs else None; continue
        m = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
        if m: seq[top].append(frozenset(vid(t) for t in m.group(4).split())); ntang += 1
    best = 0
    for t, L in seq.items():
        for v in set().union(*L):
            bits = [v in St for St in L]; ch = sum(1 for a, b in zip(bits, bits[1:]) if a != b)
            best = max(best, ch)
    return (best, searches, ntang)
cur = read_game(sys.argv[sys.argv.index("--seedgame") + 1]) if "--seedgame" in sys.argv else rand_game()
if "--seedgame" in sys.argv: n = len(cur[0])
path = os.path.join(outdir, f"osc_n{n}_s{seed}.pg"); curf = fitness(cur, path); best = curf
print(f"start {curf}", flush=True)
for i in range(steps):
    cand = mutate(cur) if rng.random() < 0.97 else rand_game()
    f = fitness(cand, os.path.join(outdir, "cand.pg"))
    if f >= curf:
        cur, curf = cand, f
        if f > best: best = f; write(cur, os.path.join(outdir, f"best_n{n}_s{seed}.pg")); print(f"step {i}: {f}", flush=True)
print(f"final best {best}")
