#!/usr/bin/env python3
"""L-RED R147: hill-climb (game, start) to maximise KEY in one W-run (KEY = CNmax, XCNmax, CN or XCN), tie-break by W-run length.
Mutations: redirect / add / drop an edge, swap two priorities, flip an owner, change a start choice. Writes the best to OUT.pg/.start.
Usage: xclimb.py KEY SEED N STEPS OUT"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import xcn
pg = xcn.pg
KEY = sys.argv[1]; seed, n, steps = map(int, sys.argv[2:5]); out = sys.argv[5]; rng = random.Random(seed)
def score(st):
    pr, ow, succ, s0, t0 = st
    g = pg.Game(pr, ow, succ)
    try: tr, fb = xcn.trace(g, [s0[v] if ow[v] == 0 else -1 for v in range(n)], [s0[v] if ow[v] == 1 else -1 for v in range(n)], cap=300)
    except Exception: return (-1, 0)
    r = xcn.analyse(g, tr, fb)
    return max((x[KEY], x["L"]) for x in r)
def rand():
    pr = rng.sample(range(2 * n + 2), n); ow = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    return [pr, ow, succ, [rng.choice(s) for s in succ], None]
def fix(st):
    pr, ow, succ, s0, _ = st
    for v in range(n):
        if s0[v] not in succ[v]: s0[v] = rng.choice(succ[v])
    return st
def mut(st):
    pr, ow, succ, s0, _ = st; pr, ow, succ, s0 = list(pr), list(ow), [list(s) for s in succ], list(s0)
    for _ in range(rng.randint(1, 3)):
        c = rng.randrange(6); v = rng.randrange(n)
        if c == 0: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
        elif c == 1 and len(succ[v]) < 4: succ[v].append(rng.randrange(n))
        elif c == 2 and len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
        elif c == 3: w = rng.randrange(n); pr[v], pr[w] = pr[w], pr[v]
        elif c == 4: ow[v] ^= 1
        else: s0[v] = rng.choice(succ[v])
        succ[v] = sorted(set(succ[v]))
    return fix([pr, ow, succ, s0, None])
best = None; bs = (-1, 0)
for restart in range(10**9):
    cur = fix(rand()); cs = score(cur)
    for it in range(steps):
        nx = mut(cur); ns = score(nx)
        if ns >= cs: cur, cs = nx, ns
    if cs > bs:
        bs, best = cs, cur
        pr, ow, succ, s0, _ = best; pg.write(pg.Game(pr, ow, succ), out + ".pg")
        with open(out + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(n) if ow[v] == 0) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{s0[v]}" for v in range(n) if ow[v] == 1) + "\n")
        print(f"restart {restart} best {KEY} {bs}", flush=True)
