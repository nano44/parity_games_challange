#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5 step 1): greedy walk from genome B (new, h capped) back toward genome A (old): passes over all single parts
(option Xi-target, parity, rank swap; mover start, gate order) in a seeded random order; a revert is kept iff the result is acyclic and
still has >= H capped levels (fev). Stops when a pass keeps nothing. Prints the kept count, the remaining differences (the part not
reverted = an upper bound on the forced core for this order) and writes the final genome. Usage: greedyback.py A.txt B.txt FEV H SEED OUT"""
import sys, os, random, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revert import rd, wr, caps
A, B, FEV, H, seed, OUT = rd(sys.argv[1]), rd(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed); N = 2 * B['d']; tmp = tempfile.mkdtemp()
def ev(C):
    p = os.path.join(tmp, 'g.txt'); wr(C, p); o = subprocess.run([FEV, p], capture_output=True, text=True).stdout.split()
    if o[0] == 'CYCLIC': return -1, None
    F = list(map(int, o[3:3 + C['d']])); return caps(F), F
def diffs(C):
    U = []
    for m in range(2 * N):
        for f in ('xt', 'bp', 'br'):
            if A[f][m] != C[f][m]: U.append((f, m))
    for x in range(N):
        if A['start'][x] != C['start'][x]: U.append(('start', x))
        if (A['gate'][2*x] < A['gate'][2*x+1]) != (C['gate'][2*x] < C['gate'][2*x+1]): U.append(('gord', x))
    return U
def apply(C, u):
    f, m = u; D = {k: list(v) if isinstance(v, list) else v for k, v in C.items()}
    if f in ('xt', 'bp'): D[f][m] = A[f][m]
    elif f == 'br': i = D['br'].index(A['br'][m]); D['br'][i], D['br'][m] = D['br'][m], D['br'][i]
    elif f == 'start': D['start'][m] = A['start'][m]
    else: D['gate'][2*m], D['gate'][2*m+1] = D['gate'][2*m+1], D['gate'][2*m]
    return D
C = B; kept = 0; c0, F0 = ev(C); assert c0 >= H, (c0, F0)
while True:
    U = diffs(C); rng.shuffle(U); k = 0
    for u in U:
        D = apply(C, u); c, F = ev(D)
        if c >= H: C = D; k += 1
    kept += k
    if k == 0: break
U = diffs(C); c, F = ev(C); wr(C, OUT)
from collections import Counter
print("seed", seed, "kept", kept, "remaining", len(U), dict(Counter(f for f, _ in U)), "caps", c, "F", ' '.join(map(str, F[:9])))
print("remaining Xi-target changes (mover:opt old->new):", ' '.join(f"{m//2}:{m%2} {A['xt'][m]}->{C['xt'][m]}" for f, m in U if f == 'xt'))
