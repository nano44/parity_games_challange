#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): single targeted edits at the SL41 dominator: (a) swap the rank of option m (default 19 = mover 9 option 1) with
every other option; (b) re-target the option (x, k) (default 11:1, the link 11 -> 9) to every mover / X. Report the results with >= H
capped levels, by F(J). Usage: domfix.py G.txt FEV H J [m] [x:k]"""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revert import rd, wr, caps
G, FEV, H, J = rd(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
m0 = int(sys.argv[5]) if len(sys.argv) > 5 else 19; xk = sys.argv[6] if len(sys.argv) > 6 else "11:1"
x, k = map(int, xk.split(':')); N = 2 * G['d']; tmp = tempfile.mkdtemp(); C = []
for m in range(2 * N):
    if m == m0: continue
    D = {a: list(b) if isinstance(b, list) else b for a, b in G.items()}; D['br'][m], D['br'][m0] = D['br'][m0], D['br'][m]; C.append((f"swap rank opt{m0}<->opt{m} (rank {G['br'][m0]}->{G['br'][m]})", D))
for y in range(-1, N):
    if y == x or y == G['xt'][2*x+k]: continue
    D = {a: list(b) if isinstance(b, list) else b for a, b in G.items()}; D['xt'][2*x+k] = y; C.append((f"retarget {x}:{k} -> {y}", D))
fs = []
for i, (_, D) in enumerate(C): p = os.path.join(tmp, f"g{i}.txt"); wr(D, p); fs.append(p)
out = subprocess.run([FEV] + fs, capture_output=True, text=True).stdout.splitlines()
res = []
for (lab, D), line in zip(C, out):
    if line.startswith('CYCLIC'): continue
    F = list(map(int, line.split()[3:3 + D['d']])); 
    if caps(F) >= H: res.append((F[J], lab, ' '.join(map(str, F[:J+2]))))
res.sort(reverse=True)
print("edits tried", len(C), "keeping >=", H, "capped:", len(res))
for r in res[:12]: print(" F(J)", r[0], "|", r[1], "| F", r[2])
