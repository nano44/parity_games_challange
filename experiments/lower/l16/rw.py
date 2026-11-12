#!/usr/bin/env python3
"""L-LOWER 16: direct rewiring search for one client x on fixed trajectories. Clamped run of GENOME (core forced to TARGET) on rows
0..P. Candidate wiring: x's options point to z1, z2 (movers or exit), both of x's options ranked BELOW every other option; then
better_x(S) = ENC comparison of chain(z1) vs chain(z2) (top-ranked option of the symmetric difference; even = toward its side), and
x's own two options decide only when the chains coincide (sign / order choice). Checks better_x against x's required list on rows
lo..P. Sources reaching x (or in EXCL / reaching EXCL) are skipped (acyclicity). Usage: rw.py GENOME TARGET P x lo [EXCL]"""
import sys, os, subprocess, ast
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
G, tp, P, x, lo = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
EXCL = set(int(c) for c in sys.argv[6].split(',')) if len(sys.argv) > 6 and sys.argv[6] else set()
D = sim6.rd(G); T = open(tp).read().split(); tg = [[int(c) for c in T[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16))); xt = D['xt']
def reach(b):
    out = {b}; st = [b]
    while st:
        y = st.pop()
        for k in (0, 1):
            z = xt[2 * y + k]
            if z >= 0 and z not in out: out.add(z); st.append(z)
    return out
def chain(z, s):
    out = []
    while z >= 0:
        m = 2 * z + s[z]; out.append(m); z = xt[m]
    return out
l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), G, tp, str(x), str(P)], capture_output=True, text=True).stdout
req = [(t, r) for t, r in ast.literal_eval(l[l.index('['):l.index('] |') + 1]) if t >= lo]
cands = [-1] + [z for z in range(64) if z != x and x not in reach(z) and not (reach(z) & EXCL)]
hits = []
for z1 in cands:
    for z2 in cands:
        if z2 <= z1 and z1 >= 0: continue
        ok = {0: True, 1: True}   # 0: tie -> x's option 0 wins (better 0), 1: tie -> better 1
        vals = []
        for t, r in req:
            s = S[t]; A = set(chain(z1, s)) if z1 >= 0 else set(); B = set(chain(z2, s)) if z2 >= 0 else set()
            dset = A ^ B
            if not dset: v = None
            else:
                top = max(dset, key=lambda m: D['br'][m]); pos = D['bp'][top] == 0
                v = int(pos) if top in B else int(not pos)
            for tb in (0, 1):
                if (tb if v is None else v) != r: ok[tb] = False
        for tb in (0, 1):
            if ok[tb]: hits.append((z1, z2, tb))
print('client', x, 'rows', lo, '..', P, 'candidates', len(cands), 'hits', len(hits), hits[:10])
