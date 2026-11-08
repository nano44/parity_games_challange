#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): exhaustive single re-targets: every option of a mover in the Xi-closure of pair J (movers of pairs < J excluded)
re-targeted to every mover in ACTIVE (or all movers if ACTIVE = all) and X; keep >= H capped; report by F(J).
Usage: retall.py G.txt FEV H J ACTIVE|all"""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revert import rd, wr, caps
G, FEV, H, J = rd(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); N = 2 * G['d']
ACT = list(range(-1, N)) if sys.argv[5] == 'all' else [-1] + [int(z) for z in sys.argv[5].split(',')]
clo = set(); st = [2*J, 2*J+1]
while st:
    u = st.pop()
    if u in clo: continue
    clo.add(u); st += [v for v in (G['xt'][2*u], G['xt'][2*u+1]) if v >= 0]
cand = [m for u in sorted(clo) if u >= 2*J for m in (2*u, 2*u+1)]
tmp = tempfile.mkdtemp(); C = []
for m in cand:
    for y in ACT:
        if y == m // 2 or y == G['xt'][m]: continue
        D = {a: list(b) if isinstance(b, list) else b for a, b in G.items()}; D['xt'][m] = y; C.append((f"{m//2}:{m%2} {G['xt'][m]}->{y}", D))
res = []; base = None
for i in range(0, len(C), 300):
    fs = []
    for j, (_, D) in enumerate(C[i:i+300]): p = os.path.join(tmp, f"g{j}.txt"); wr(D, p); fs.append(p)
    for (lab, D), line in zip(C[i:i+300], subprocess.run([FEV] + fs, capture_output=True, text=True).stdout.splitlines()):
        if line.startswith('CYCLIC'): continue
        F = list(map(int, line.split()[3:3 + D['d']]))
        if caps(F) >= H: res.append((F[J], lab, ' '.join(map(str, F[:J+2]))))
res.sort(reverse=True)
print("re-targets tried", len(C), "acyclic and >=", H, "capped:", len(res))
for r in res[:10]: print(" F(J)", r[0], "|", r[1], "| F", r[2])
