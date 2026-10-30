#!/usr/bin/env python3
"""L-RED R149: hill-climb (game, start) to maximise max over (Even X, EROOT e) of RET(X; e) - deg(X) (L-NEW box 101 CASC-EDGE kill if > 0),
scored by casc/retcause_br.py (L-NEW retcause.py @ 2311683e + XDEG) in a subprocess. Tie-break: total returns.
Usage: LNEW_BOX21=... xdclimb.py SEED N STEPS OUTPREFIX"""
import sys, os, random, subprocess, re, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
seed, n, steps = map(int, sys.argv[1:4]); out = sys.argv[4]; rng = random.Random(seed); tmp = tempfile.mkdtemp()
def write(st, p):
    pr, ow, succ, s0 = st
    with open(p + ".pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {pr[v]} {ow[v]} {','.join(map(str, succ[v]))};\n")
    with open(p + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(n) if ow[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{s0[v]}" for v in range(n) if ow[v] == 1) + "\n")
def score(st):
    p = os.path.join(tmp, "c"); write(st, p)
    try: o = subprocess.run([sys.executable, "-I", os.path.join(HERE, "retcause_br.py"), p + ".pg", p + ".start"], capture_output=True, text=True, timeout=60, env=dict(os.environ, TOP="1")).stdout
    except Exception: return (-99, 0)
    d = [int(x) for x in re.findall(r"XDEG max RET\(X;e\) - deg\(X\) (-?\d+)", o)]; r = [int(x) for x in re.findall(r"returns (\d+) edges", o)]
    return (max(d) if d else -99, max(r) if r else 0)
def rand():
    pr = rng.sample(range(2 * n + 2), n); ow = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    return [pr, ow, succ, [rng.choice(s) for s in succ]]
def mut(st):
    pr, ow, succ, s0 = [list(x) if not isinstance(x[0], list) else [list(y) for y in x] for x in st]
    for _ in range(rng.randint(1, 3)):
        c = rng.randrange(6); v = rng.randrange(n)
        if c == 0: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
        elif c == 1 and len(succ[v]) < 4: succ[v].append(rng.randrange(n))
        elif c == 2 and len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
        elif c == 3: w = rng.randrange(n); pr[v], pr[w] = pr[w], pr[v]
        elif c == 4: ow[v] ^= 1
        else: s0[v] = rng.choice(succ[v])
        succ[v] = sorted(set(succ[v]))
    for v in range(n):
        if s0[v] not in succ[v]: s0[v] = rng.choice(succ[v])
    return [pr, ow, succ, s0]
bs = (-100, 0)
for restart in range(10 ** 9):
    cur = rand(); cs = score(cur)
    for it in range(steps):
        nx = mut(cur); ns = score(nx)
        if ns >= cs: cur, cs = nx, ns
    if cs > bs:
        bs = cs; write(cur, out); print(f"restart {restart} best {bs}", flush=True)
