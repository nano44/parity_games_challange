#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A attack on Claim P / (M)): hill-climb for a game in which, at an IDENTICAL depth-0 context (same
player, same remaining set R) in two searches, a vertex's pruning round DECREASES, or a stable call reverts to -1, or a stable
V* loses a vertex. Needs the PATCHED debug build (ENTER/EXIT, DomStable prints). Fitness = (P violations, Q violations,
recurring contexts, searches). Usage: dtl_pclimb.py PATCHED_OINK OUTDIR n seed steps [--seedgame G]"""
import sys, os, random, re, subprocess, collections
oink, outdir, n, seed, steps = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
os.makedirs(outdir, exist_ok=True); rng = random.Random(seed); INF = 10**9
def rand_game():
    return [rng.randint(0, n) for _ in range(n)], [rng.randint(0, 1) for _ in range(n)], [sorted(rng.sample(range(n), rng.randint(1, 3))) for _ in range(n)]
def mutate(g):
    pr, ow, succ = list(g[0]), list(g[1]), [list(s) for s in g[2]]
    for _ in range(rng.randint(1, 3)):
        v = rng.randrange(n); k = rng.random()
        if k < 0.3: pr[v] = rng.randint(0, n)
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
def analyse(out):
    calls = []; search = -1; player = None; depth = -1; unsolved = set(); removed = set(); dist = {}; mode = None
    for line in out.splitlines():
        line = re.sub(r"^\[ *[0-9.]*\] ", "", line.rstrip())
        m = re.match(r"iteration \d+-(even|odd)", line)
        if m: search += 1; player = m.group(1); depth = -1; removed = set(); dist = {}; continue
        m = re.match(r"ENTER depth (\d+)", line)
        if m: depth = int(m.group(1)); continue
        m = re.match(r"EXIT depth (\d+)", line)
        if m: depth = int(m.group(1)) - 1; continue
        m = re.match(r"current region:(.*)", line)
        if m and depth == 0 and not removed: unsolved = set(vid(t) for t in m.group(1).split()); continue
        if depth != 0: continue
        m = re.match(r"distance (\d+):(.*)", line)
        if m:
            for t in m.group(2).split(): dist[vid(t)] = int(m.group(1))
            continue
        if line.startswith("best vertices"):
            V = frozenset(int(t[1:]) for t in line.split()[2:] if t.startswith("v"))
            calls.append((search, player, frozenset(unsolved - removed), "S" if line.endswith("(stable)") else "m", V, dict(dist)))
            dist = {}; mode = "pending"; continue
        if line.startswith("X ∪= DomStable"): mode = "dom"; continue
        if line.startswith("X ∪= Dom(V)"): mode = "dis"; continue
        m = re.match(r"X ∪= attracted with threshold (\d+):(.*)", line)
        if m: removed |= set(vid(t) for t in m.group(2).split()); mode = None; continue
        m = re.match(r"domregion (\d+) (.*)", line)
        if m and mode == "dom": removed |= set(vid(t) for t in m.group(2).split()); continue
        m = re.match(r"region (\d+)(.*)", line)
        if m and mode == "dis": removed |= set(vid(t) for t in m.group(2).split()); continue
    by = collections.defaultdict(list)
    for c in calls: by[(c[1], c[2])].append(c)
    pv = qv = rec = 0
    for key, L in by.items():
        if len(L) < 2: continue
        rec += 1
        for a, b in zip(L, L[1:]):
            for v in key[1]:
                if b[5].get(v, INF) < a[5].get(v, INF): pv += 1
            if a[3] == "S" and b[3] == "m": qv += 1
            if a[3] == "S" and b[3] == "S": qv += len(a[4] - b[4])
    return pv, qv, rec, search + 1
def fitness(g, path):
    write(g, path)
    try: r = subprocess.run([oink, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", "-t", path], capture_output=True, text=True, timeout=60)
    except Exception: return (0, 0, 0, 0)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    return analyse(out)
cur = read_game(sys.argv[sys.argv.index("--seedgame") + 1]) if "--seedgame" in sys.argv else rand_game()
if "--seedgame" in sys.argv: n = len(cur[0])
path = os.path.join(outdir, f"p_n{n}_s{seed}.pg"); curf = fitness(cur, path); best = curf
print(f"start {curf}", flush=True)
for i in range(steps):
    cand = mutate(cur) if rng.random() < 0.97 else rand_game()
    f = fitness(cand, os.path.join(outdir, "cand.pg"))
    if f >= curf:
        cur, curf = cand, f
        if f > best: best = f; write(cur, os.path.join(outdir, f"best_n{n}_s{seed}.pg")); print(f"step {i}: {f}", flush=True)
print(f"final best {best}")
