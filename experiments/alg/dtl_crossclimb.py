#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A attack): hill-climb for games where ONE top learns many pairwise-CROSSING tangles (a chain of
nested tangles at a top is bounded by n; crossing sequences at one top are the shape a counter needs), and secondarily for
many searches. Fitness = (max over tops of the size of the largest set of pairwise crossing tangles at that top,
max tangles at one top, searches, tangles). Release Oink, pinned command + -t -t to read the tangles.
Usage: dtl_crossclimb.py OINK OUTDIR n seed steps [--pmax P] [--cnew | --pertop | --restart | --searches | --chainbreak]  (--chainbreak: fitness led by in-search chain breaks at a top, the F3 test) [--seedgame GAME.pg] [--crossonly]  (--restart: fitness led by restart violations, then in-search chain breaks)  (--pertop: fitness led by the max number of tangles at one top)  (--cnew: fitness led by the number of (C-new) violations: tangles at a top covered by the union of the earlier tangles at that top)"""
import sys, os, random, re, subprocess, itertools, collections
oink, outdir, n, seed, steps = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
pmax = int(sys.argv[sys.argv.index("--pmax") + 1]) if "--pmax" in sys.argv else n
os.makedirs(outdir, exist_ok=True); rng = random.Random(seed)
def rand_game():
    pr = [rng.randint(0, pmax) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, 3))) for _ in range(n)]
    return pr, ow, succ
def mutate(g):
    pr, ow, succ = [list(x) for x in g[:2]] + [[list(s) for s in g[2]]]
    if "--crossonly" in sys.argv:   # only add/remove edges (cross edges between halves included); priorities and owners fixed
        for _ in range(rng.randint(1, 3)):
            v = rng.randrange(n); w = rng.randrange(n)
            if w in succ[v]:
                if len(succ[v]) > 1: succ[v].remove(w)
            else: succ[v].append(w); succ[v].sort()
        return pr, ow, succ
    for _ in range(rng.randint(1, 3)):
        v = rng.randrange(n); k = rng.random()
        if k < 0.3: pr[v] = rng.randint(0, pmax)
        elif k < 0.45: ow[v] ^= 1
        elif k < 0.75:
            w = rng.randrange(n)
            if w in succ[v]:
                if len(succ[v]) > 1: succ[v].remove(w)
            else: succ[v].append(w); succ[v].sort()
        else:
            succ[v] = sorted(rng.sample(range(n), rng.randint(1, 3)))
    return pr, ow, succ
def write(g, path):
    pr, ow, succ = g
    with open(path, "w") as f:
        f.write(f"parity {n};\n")
        for v in range(n): f.write(f"{v} {pr[v]} {ow[v]} {','.join(map(str, succ[v]))} \"v{v}\";\n")
def fitness(g, path):
    write(g, path); pr = g[0]
    try: r = subprocess.run([oink, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", path], capture_output=True, text=True, timeout=20)
    except Exception: return (0, 0, 0, 0, 0, 0)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    sets = []; searches = 0
    for line in out.splitlines():
        if re.search(r"iteration \d+-(even|odd)", line): searches += 1
        m = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
        if m: sets.append((frozenset(int(t.split("->")[0][1:]) for t in m.group(4).split()), searches))
    per_top = collections.defaultdict(list)
    for S, srch in sets: per_top[max(S, key=lambda v: (pr[v], v))].append((S, srch))
    best_cross = 0; cnew = 0; restart = 0; chainbreak = 0
    for tp, L in per_top.items():
        cov = set(); last = None; prev = None
        for S, srch in L:
            if S <= cov: cnew += 1
            if srch != last:
                if S <= cov: restart += 1
            elif not (prev < S): chainbreak += 1
            cov |= S; last = srch; prev = S
        # largest set of pairwise crossing tangles (greedy over subsets is fine for small L)
        k = len(L)
        for size in range(min(k, 6), 1, -1):
            found = False
            for comb in itertools.combinations(range(k), size):
                if all((L[a][0] & L[b][0]) and not (L[a][0] <= L[b][0]) and not (L[b][0] <= L[a][0]) for a, b in itertools.combinations(comb, 2)):
                    found = True; break
            if found: best_cross = max(best_cross, size); break
    if "--chainbreak" in sys.argv: return (chainbreak, restart, cnew, max((len(L) for L in per_top.values()), default=0), searches, len(sets))
    if "--searches" in sys.argv: return (searches, len(sets), max((len(L) for L in per_top.values()), default=0))
    if "--restart" in sys.argv: return (restart, chainbreak, cnew, max((len(L) for L in per_top.values()), default=0), searches, len(sets))
    if "--pertop" in sys.argv: return (max((len(L) for L in per_top.values()), default=0), cnew, searches, len(sets))
    if "--cnew" in sys.argv: return (cnew, best_cross, max((len(L) for L in per_top.values()), default=0), searches, len(sets))
    return (best_cross, max((len(L) for L in per_top.values()), default=0), searches, len(sets))
def read_game(path):
    pr, ow, succ = [], [], []
    for line in open(path):
        f = line.strip().rstrip(";").split()
        if len(f) >= 4 and f[0].isdigit(): pr.append(int(f[1])); ow.append(int(f[2])); succ.append(sorted(int(x) for x in f[3].split(",")))
    return pr, ow, succ
if "--seedgame" in sys.argv:
    cur = read_game(sys.argv[sys.argv.index("--seedgame") + 1]); n = len(cur[0])
else:
    cur = rand_game()
path = os.path.join(outdir, f"climb_n{n}_s{seed}.pg")
curf = fitness(cur, path); best = curf
print(f"start {curf}", flush=True)
for i in range(steps):
    cand = mutate(cur) if rng.random() < 0.97 else rand_game()
    f = fitness(cand, os.path.join(outdir, "cand.pg"))
    if tuple(f) >= tuple(curf):
        cur, curf = cand, f
        if f > best:
            best = f; write(cur, os.path.join(outdir, f"best_n{n}_s{seed}.pg")); print(f"step {i}: {f}", flush=True)
print(f"final best {best}")
