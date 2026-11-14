#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): two-edit search at a dominated pair: first edit = one closure option re-targeted to a supplier Y (list);
second edit = any single closure re-target (to any mover or X) or any rank swap of the first-edited option with an option of rank > RMIN.
Closure = Xi-closure of pair J minus pairs < J. Keep >= H capped; report best by F(J). Usage: retall2.py G.txt FEV H J Y(comma) RMIN"""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revert import rd, wr, caps
G, FEV, H, J = rd(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); Y = [int(z) for z in sys.argv[5].split(',')]
RMIN = int(sys.argv[6]); N = 2 * G['d']
clo = set(); st = [2*J, 2*J+1]
while st:
    u = st.pop()
    if u in clo: continue
    clo.add(u); st += [v for v in (G['xt'][2*u], G['xt'][2*u+1]) if v >= 0]
cand = [m for u in sorted(clo) if u >= 2*J for m in (2*u, 2*u+1)]
hi = [m for m in range(2*N) if G['br'][m] > RMIN]
def cp(D): return {a: list(b) if isinstance(b, list) else b for a, b in D.items()}
tmp = tempfile.mkdtemp(); best = []; n = 0
def flush(C):
    global n
    fs = []
    for j, (_, D) in enumerate(C): p = os.path.join(tmp, f"g{j}.txt"); wr(D, p); fs.append(p)
    for (lab, D), line in zip(C, subprocess.run([FEV] + fs, capture_output=True, text=True).stdout.splitlines()):
        n += 1
        if line.startswith('CYCLIC'): continue
        F = list(map(int, line.split()[3:3 + D['d']]))
        if caps(F) >= H: best.append((F[J], lab, ' '.join(map(str, F[:J+2]))))
C = []
for m1 in cand:
    for y in Y:
        if y == m1 // 2 or G['xt'][m1] == y: continue
        D1 = cp(G); D1['xt'][m1] = y
        for m2 in cand:
            if m2 == m1: continue
            for z in range(-1, N):
                if z == m2 // 2 or z == D1['xt'][m2]: continue
                D = cp(D1); D['xt'][m2] = z; C.append((f"{m1//2}:{m1%2}->{y} & {m2//2}:{m2%2}->{z}", D))
                if len(C) >= 400: flush(C); C = []
        for h in hi:
            D = cp(D1); D['br'][m1], D['br'][h] = D['br'][h], D['br'][m1]; C.append((f"{m1//2}:{m1%2}->{y} & rank {G['br'][m1]}<->{G['br'][h]}", D))
    if C: flush(C); C = []
    best.sort(reverse=True); best[:] = best[:20]
    print("after first-edit option", m1, "evaluated", n, "best", best[0] if best else None, flush=True)
print("done", n); [print(" ", b) for b in best[:10]]
