#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5 step 1): revert each changed part of genome B (new) to genome A (old), one unit at a time, and record the
F-profile with fev (batch evaluator). Units: option Xi-target, option parity, option rank (by a swap inside B's rank permutation),
mover gate pair, mover start bit; and level blocks (all of xt/bp/gate/start of one level). Usage: revert.py A.txt B.txt FEV OUTDIR"""
import sys, copy, os, subprocess
def rd(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] == 'd': D['d'] = int(w[1])
        if w and w[0] in ('xt', 'br', 'bp', 'gate', 'start'): D[w[0]] = list(map(int, w[1:]))
    return D
def wr(D, p):
    with open(p, 'w') as f:
        f.write(f"d {D['d']}\n")
        for k in ('xt', 'br', 'bp', 'gate', 'start'): f.write(k + ' ' + ' '.join(map(str, D[k])) + '\n')
def caps(F):
    h = 0
    for l, v in enumerate(F):
        if v == 2 ** (l + 2) - 2: h += 1
        else: break
    return h
def main():
    A, B, FEV, OD = rd(sys.argv[1]), rd(sys.argv[2]), sys.argv[3], sys.argv[4]
    os.makedirs(OD, exist_ok=True); N = 2 * B['d']; units = []
    for m in range(2 * N):
        x, k = m // 2, m % 2
        for fld in ('xt', 'bp'):
            if A[fld][m] != B[fld][m]:
                C = copy.deepcopy(B); C[fld][m] = A[fld][m]; units.append((f"x{x} L{x//2} {fld}[{k}] {B[fld][m]}->{A[fld][m]}", C))
        if A['br'][m] != B['br'][m]:
            C = copy.deepcopy(B); i = C['br'].index(A['br'][m]); C['br'][i], C['br'][m] = C['br'][m], C['br'][i]
            units.append((f"x{x} L{x//2} br[{k}] {B['br'][m]}->{A['br'][m]} (swap with opt {i})", C))
    for x in range(N):
        if A['gate'][2*x:2*x+2] != B['gate'][2*x:2*x+2] and sorted(A['gate'][2*x:2*x+2]) == sorted(B['gate'][2*x:2*x+2]):
            C = copy.deepcopy(B); C['gate'][2*x:2*x+2] = A['gate'][2*x:2*x+2]; units.append((f"x{x} L{x//2} gate-order", C))
        if A['start'][x] != B['start'][x]:
            C = copy.deepcopy(B); C['start'][x] = A['start'][x]; units.append((f"x{x} L{x//2} start", C))
    for L in range(B['d']):
        C = copy.deepcopy(B)
        for x in (2*L, 2*L+1):
            for fld in ('xt', 'bp'): C[fld][2*x:2*x+2] = A[fld][2*x:2*x+2]
            C['start'][x] = A['start'][x]
        units.append((f"LEVEL {L} block xt/bp/start", C))
    files = []
    for i, (lab, C) in enumerate(units):
        p = os.path.join(OD, f"u{i}.txt"); wr(C, p); files.append(p)
    out = subprocess.run([FEV, sys.argv[2], sys.argv[1]] + files, capture_output=True, text=True).stdout.splitlines()
    def fmt(line):
        if line.startswith('CYCLIC'): return 'CYCLIC'
        w = line.split(); T = int(w[1]); F = list(map(int, w[3:3 + B['d']])); return f"T {T} caps {caps(F)} F {' '.join(map(str, F[:8]))}"
    print("B (new)", fmt(out[0])); print("A (old)", fmt(out[1]))
    for (lab, _), line in zip(units, out[2:]): print(lab, "|", fmt(line))

if __name__ == '__main__':
    main()
