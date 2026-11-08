#!/usr/bin/env python3
"""L-LOWER 6: READ-NEST test on SL41. Step 1: re-route 10's read path around 12 (option 55:0 or 10:0 re-pointed to each mover y / X)
and keep those that leave levels 0-5 capped. Step 2: on each kept re-route, let 12 read 13 (12:1 -> 13 or 12:0 -> 13) with option
(13, k) re-ranked to every tier and parity; record caps and F(6). Usage: readnest.py genome.txt FEV OUTDIR"""
import sys, os, copy, subprocess
from sim6 import rd, wr, caps
D0 = rd(sys.argv[1]); FEV, OD = sys.argv[2], sys.argv[3]; os.makedirs(OD, exist_ok=True); N = 2 * D0['d']
def rerank(D, m, tier, par):
    br = D['br']; key = [float(r) for r in br]; key[m] = tier
    for r, i in enumerate(sorted(range(len(br)), key=lambda i: key[i])): br[i] = r
    D['bp'][m] = par
def fev(Ds):
    fs = []
    for i, D in enumerate(Ds): p = os.path.join(OD, f"g{i}.txt"); wr(D, p); fs.append(p)
    out = []
    for k in range(0, len(fs), 400): out += subprocess.run([FEV] + fs[k:k+400], capture_output=True, text=True).stdout.splitlines()
    res = []
    for line in out:
        if line.startswith('CYCLIC'): res.append(None); continue
        w = line.split(); res.append(list(map(int, w[3:3 + D0['d']])))
    return res
step1 = []
for m in (2*55+0, 2*10+0):
    for y in list(range(N)) + [-1]:
        if y == D0['xt'][m]: continue
        D = copy.deepcopy(D0); D['xt'][m] = y; step1.append(((m, y), D))
r1 = fev([D for _, D in step1]); kept = [(lab, D) for (lab, D), F in zip(step1, r1) if F and caps(F) >= 6]
print('step 1: re-routes tried', len(step1), 'acyclic', sum(F is not None for F in r1), 'keep 6 capped', len(kept), [lab for lab, _ in kept])
step2 = []
for lab, Db in kept + [(('none', None), D0)]:
    for qm in (2*12+1, 2*12+0):
        for km in (2*13+0, 2*13+1):
            for t in [x + 0.5 for x in range(-1, 112, 2)]:
                for par in (0, 1):
                    D = copy.deepcopy(Db); D['xt'][qm] = 13; rerank(D, km, t, par); step2.append(((lab, qm, km, t, par), D))
r2 = fev([D for _, D in step2]); best = sorted(((caps(F), F[6], str(lab)) for (lab, _), F in zip(step2, r2) if F), reverse=True)
print('step 2: genomes', len(step2), 'acyclic', sum(F is not None for F in r2))
print('caps histogram', {h: sum(1 for b in best if b[0] == h) for h in range(8)})
for b in best[:10]: print('  ', b)
# Step 3: PARALLEL variant: 12:1 -> 13 and 13's targets swapped (13:0 -> 22, 13:1 -> 11), so in joined states 10 -> 12 -> 13 reaches the
# original target; both options of 13 re-ranked over tiers and parities (independently, coarse grid).
step3 = []
tiers = [-0.5] + [x + 0.5 for x in range(1, 112, 6)]
for t0 in tiers:
    for t1 in tiers:
        for p0 in (0, 1):
            for p1 in (0, 1):
                D = copy.deepcopy(D0); D['xt'][25] = 13; D['xt'][26], D['xt'][27] = D0['xt'][27], D0['xt'][26]
                rerank(D, 26, t0, p0); rerank(D, 27, t1 + 0.25, p1); step3.append(((t0, p0, t1, p1), D))
r3 = fev([D for _, D in step3]); best3 = sorted(((caps(F), F[6], str(lab)) for (lab, _), F in zip(step3, r3) if F), reverse=True)
print('step 3 (parallel 13, 12:1 -> 13): genomes', len(step3), 'acyclic', sum(F is not None for F in r3))
print('caps histogram', {h: sum(1 for b in best3 if b[0] == h) for h in range(8)})
for b in best3[:6]: print('  ', b)
