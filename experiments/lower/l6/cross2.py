#!/usr/bin/env python3
"""L-LOWER 6: CROSS-preserving supplier insertion on SL41. Family A: both 22-side options (12:0, 13:1) re-pointed to mover Y;
family B: both 11-side options (12:1, 13:0) re-pointed to Y; family C: the merge link 54:0 re-pointed to Y; each with Y's two option
ranks optionally swapped to the top ranks (Y's options become the two highest ranks, order and parities free).
Usage: cross2.py genome.txt FEV OUTDIR"""
import sys, os, copy, subprocess, itertools
from sim6 import rd, wr, caps
D0 = rd(sys.argv[1]); FEV, OD = sys.argv[2], sys.argv[3]; os.makedirs(OD, exist_ok=True); N = 2 * D0['d']
def toprank(D, y, hi, pa, pb):
    br = D['br']; R = len(br)
    for m, r in ((2*y, R-1-hi), (2*y+1, R-1-(1-hi))):
        i = br.index(r); br[i], br[m] = br[m], br[i]
    D['bp'][2*y], D['bp'][2*y+1] = pa, pb
units = []
fam = {'A': (2*12+0, 2*13+1), 'B': (2*12+1, 2*13+0), 'C': (2*54+0,)}
for f, ms in fam.items():
    for y in range(N):
        if y in (12, 13): continue
        for rk in [None] + list(itertools.product((0, 1), (0, 1), (0, 1))):
            D = copy.deepcopy(D0)
            for m in ms: D['xt'][m] = y
            if rk: toprank(D, y, *rk)
            units.append((f"{f} Y={y} rank={rk}", D))
files = []
for i, (lab, D) in enumerate(units):
    p = os.path.join(OD, f"c{i}.txt"); wr(D, p); files.append(p)
out = []
for k in range(0, len(files), 400): out += subprocess.run([FEV] + files[k:k+400], capture_output=True, text=True).stdout.splitlines()
best = []
for (lab, _), line in zip(units, out):
    if line.startswith('CYCLIC'): continue
    w = line.split(); F = list(map(int, w[3:3 + D0['d']])); best.append((caps(F), F[6], lab, F[:9]))
best.sort(reverse=True)
print('genomes', len(units), 'acyclic', len(best)); print('caps histogram', {h: sum(1 for b in best if b[0] == h) for h in range(8)})
for b in best[:12]: print(b)
