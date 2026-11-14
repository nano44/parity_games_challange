#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): DELAY SPLICE search. In genome G (text), the option (x, k) whose Xi-target is the trigger y is re-pointed to a
splice mover w (a mover from the list W, re-initialised), and w gets one option with Xi-target y; all other data of w (its other option's
Xi-target among all movers or X, both ranks (inserted anywhere in the rank order), parities, gate order, start) are drawn at random.
Evaluated by fev in batches; reports the best by (capped levels, F(LEV)). Usage: splice.py G.txt FEV x k y W(comma) LEV TRIALS SEED OUT"""
import sys, os, random, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revert import rd, wr, caps
G, FEV = rd(sys.argv[1]), sys.argv[2]
x, k, y = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); W = [int(z) for z in sys.argv[6].split(',')]
LEV, TR, rng, OUT = int(sys.argv[7]), int(sys.argv[8]), random.Random(int(sys.argv[9])), sys.argv[10]
N = 2 * G['d']; M = 2 * N; tmp = tempfile.mkdtemp()
def cyc(D):
    col = [0] * N
    def dfs(u):
        col[u] = 1
        for kk in (0, 1):
            v = D['xt'][2*u+kk]
            if v >= 0 and (col[v] == 1 or (col[v] == 0 and dfs(v))): return True
        col[u] = 2; return False
    return any(col[u] == 0 and dfs(u) for u in range(N))
def make():
    D = {kk: list(v) if isinstance(v, list) else v for kk, v in G.items()}
    w = rng.choice(W); D['xt'][2*x+k] = w; kw = rng.randrange(2)
    D['xt'][2*w+kw] = y; z = rng.randrange(-1, N); D['xt'][2*w+1-kw] = z if z != w else -1
    order = sorted(range(M), key=lambda m: D['br'][m]); order = [m for m in order if m // 2 != w]
    for m in (2*w, 2*w+1): order.insert(rng.randrange(len(order) + 1), m)
    for r, m in enumerate(order): D['br'][m] = r
    for m in (2*w, 2*w+1): D['bp'][m] = rng.randrange(2)
    if rng.randrange(2): D['gate'][2*w], D['gate'][2*w+1] = D['gate'][2*w+1], D['gate'][2*w]
    D['start'][w] = rng.randrange(2)
    if rng.randrange(4) == 0: D['start'][x] ^= 1
    return D
best = (-1, -1); done = 0
while done < TR:
    batch = []
    while len(batch) < 200:
        D = make()
        if not cyc(D): batch.append(D)
    fs = []
    for i, D in enumerate(batch): p = os.path.join(tmp, f"g{i}.txt"); wr(D, p); fs.append(p)
    out = subprocess.run([FEV] + fs, capture_output=True, text=True).stdout.splitlines()
    for D, line in zip(batch, out):
        w_ = line.split(); F = list(map(int, w_[3:3 + D['d']])); key = (caps(F), F[LEV])
        if key > best: best = key; wr(D, OUT); print("trials", done, "caps", key[0], "F", ' '.join(map(str, F[:LEV+2])), flush=True)
    done += len(batch)
print("done", done, "best", best)
