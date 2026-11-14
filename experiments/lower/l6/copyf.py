#!/usr/bin/env python3
"""L-LOWER 6: COPY-OF-F family on a text genome: the second mover q of pair J reads the first mover p's current option
(one option of q re-pointed to p), and one or both options of p re-ranked to a tier (new rank inserted just above old rank floor(tier))
with a chosen parity. Usage: copyf.py genome.txt FEV OUTDIR q p"""
import sys, os, copy, subprocess, itertools
from sim6 import rd, wr, caps
D0 = rd(sys.argv[1]); FEV, OD = sys.argv[2], sys.argv[3]; q, p = int(sys.argv[4]), int(sys.argv[5]); os.makedirs(OD, exist_ok=True)
def rerank(D, m, tier, par):
    br = D['br']; key = [float(r) for r in br]; key[m] = tier
    order = sorted(range(len(br)), key=lambda i: key[i])
    for r, i in enumerate(order): br[i] = r
    D['bp'][m] = par
tiers = [None] + [t + 0.5 for t in range(0, 112, 1)]
units = []
for kq in (0, 1):
    for kp in (0, 1):
        for t in tiers:
            for par in ((0, 1) if t is not None else (None,)):
                D = copy.deepcopy(D0); D['xt'][2*q+kq] = p
                if t is not None: rerank(D, 2*p+kp, t, par)
                units.append((f"{q}:{kq}->{p} rerank {p}:{kp} tier {t} par {par}", D))
files = []
for i, (lab, D) in enumerate(units):
    pth = os.path.join(OD, f"f{i}.txt"); wr(D, pth); files.append(pth)
out = []
for k in range(0, len(files), 400): out += subprocess.run([FEV] + files[k:k+400], capture_output=True, text=True).stdout.splitlines()
res = []
for (lab, _), line in zip(units, out):
    if line.startswith('CYCLIC'): continue
    w = line.split(); F = list(map(int, w[3:3 + D0['d']])); res.append((caps(F), F[J] if (J := 6) else 0, lab, F[:9]))
res.sort(reverse=True); print('genomes', len(units), 'acyclic', len(res))
print('caps histogram', {h: sum(1 for b in res if b[0] == h) for h in range(9)})
for b in res[:15]: print(b)
