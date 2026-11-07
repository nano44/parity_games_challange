#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): FUEL splice search at a dominated pair. Edits: one option m of a mover in the Xi-down-closure of pair J (movers
of pairs < J excluded) is re-targeted to a mover y from ACTIVE (movers that move inside the failing J-windows), and m's rank is swapped
with a random option of rank > RMIN; optionally (prob 1/2) m's parity flipped. Keeps results with >= H capped levels; reports best F(J).
Usage: fuelsplice.py G.txt FEV H J RMIN ACTIVE(comma) TRIALS SEED OUT"""
import sys, os, random, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revert import rd, wr, caps
G, FEV, H, J, RMIN = rd(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
ACT = [int(z) for z in sys.argv[6].split(',')]; TR = int(sys.argv[7]); rng = random.Random(int(sys.argv[8])); OUT = sys.argv[9]
N = 2 * G['d']; tmp = tempfile.mkdtemp()
clo = set(); st = [2*J, 2*J+1]
while st:
    u = st.pop()
    if u in clo: continue
    clo.add(u)
    for k in (0, 1):
        v = G['xt'][2*u+k]
        if v >= 0: st.append(v)
cand = [m for u in sorted(clo) if u >= 2*J for m in (2*u, 2*u+1)]
hi = [m for m in range(2*N) if G['br'][m] > RMIN]
print("closure movers >= pair J:", sorted(u for u in clo if u >= 2*J), "candidate options", len(cand), "high-rank options", len(hi), flush=True)
def cyc(D):
    col = [0]*N
    def dfs(u):
        col[u] = 1
        for k in (0, 1):
            v = D['xt'][2*u+k]
            if v >= 0 and (col[v] == 1 or (col[v] == 0 and dfs(v))): return True
        col[u] = 2; return False
    return any(col[u] == 0 and dfs(u) for u in range(N))
best = -1; done = 0
while done < TR:
    B = []
    while len(B) < 200:
        D = {a: list(b) if isinstance(b, list) else b for a, b in G.items()}
        m = rng.choice(cand); D['xt'][m] = rng.choice(ACT)
        if D['xt'][m] == m // 2: continue
        h = rng.choice(hi); D['br'][m], D['br'][h] = D['br'][h], D['br'][m]
        if rng.randrange(2): D['bp'][m] ^= 1
        if not cyc(D): B.append(D)
    fs = []
    for i, D in enumerate(B): p = os.path.join(tmp, f"g{i}.txt"); wr(D, p); fs.append(p)
    for D, line in zip(B, subprocess.run([FEV] + fs, capture_output=True, text=True).stdout.splitlines()):
        F = list(map(int, line.split()[3:3 + D['d']]))
        if caps(F) >= H and F[J] > best: best = F[J]; wr(D, OUT); print("trials", done, "F", ' '.join(map(str, F[:J+2])), flush=True)
    done += len(B)
print("done", done, "best F(J)", best)
