#!/usr/bin/env python3
"""L-LOWER 16: independent replay of an ekr2.py design. Integer ENC (value of a chain = sum of +-2^rank over its options; rank =
position in the decoded total order; fixed options keep their base order there), cascade movement (M3) with keys (M4), o(7)(S_t) =
t mod 2; EXT chains walked on the base genome's clamped run (own walk, not ekr2's table). Checks the client's better against its
required list at every free pre-state t <= P. env LEVEL=L as in ekr2.py (clock = base o(L-1) on the clamped run).
Usage: sim2.py DESIGN GENOME TARGET P CLIENT"""
import sys, os, subprocess, ast
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
des, gen, tp, P, X = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
D = sim6.rd(gen); TR = open(tp).read().split(); tg = [[int(c) for c in TR[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
SB = clamp.runclamp(D, tgt, set(range(16)))
xt = {}; ev = {}; order = []; gate = []; start = []
for ln in open(des):
    w = ln.split()
    if w[0] == 'opt': xt[int(w[1])] = w[3]; ev[int(w[1])] = int(w[5])
    elif w[0] == 'rank_order_ascending': order = w[1:]
    elif w[0] == 'gate': gate = list(map(int, w[1:]))
    elif w[0] == 'start': start = [int(c) for c in w[1]]
H = len(start); K = H // 2; NC = 2 * H
LEV = int(os.environ.get('LEVEL', '8'))
pos = {a: i for i, a in enumerate(order)}
# sanity: fixed options appear in base order
fx = [a for a in order if a.startswith('f')]
assert all(D['br'][int(fx[i][1:])] < D['br'][int(fx[i + 1][1:])] for i in range(len(fx) - 1)), 'fixed order broken'
def extval(e, S):
    v = 0
    while e >= 0:
        m = 2 * e + S[e]; key = 'f%d' % m
        v += (1 if D['bp'][m] == 0 else -1) * 2 ** pos[key]; e = D['xt'][m]
    return v
def val(op, s, S):
    v = (1 if ev[op] else -1) * 2 ** pos[str(op)]; z = xt[op]
    if z == 'exit': return v
    if z.startswith('e'): return v + extval(int(z[1:]), S)
    z = int(z); return v + val(2 * z + s[z], s, S)
l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), gen, tp, str(X), str(P)], capture_output=True, text=True).stdout
req = dict(ast.literal_eval(l[l.index('['):l.index('] |') + 1]))
s = list(start); bad = []; traj = [''.join(map(str, s))]
for t in range(P + 1):
    S = SB[t]
    if t in req:
        b = 1 if val(NC + 1, s, S) > val(NC, s, S) else 0
        if b != req[t]: bad.append(t)
    if t == P: break
    bet = [1 if val(2 * y + 1, s, S) > val(2 * y, s, S) else 0 for y in range(H)]
    ns = list(s); c = sim6.okeys(D, list(SB[t + 1]))[LEV - 1]
    for i in range(K):
        for y in (2 * i, 2 * i + 1):
            if bet[y] != s[y] and s[y] != c: ns[y] = c
        a, b2 = ns[2 * i], ns[2 * i + 1]; c = (a ^ c) if a != b2 else gate[2 * i + a]
    s = ns; traj.append(''.join(map(str, s)))
print('SIM2', os.path.basename(des), 'P', P, 'client', X, 'free rows', len(req), 'mismatches', bad, '|', 'OK' if not bad else 'FAILS', '| traj', ' '.join(traj))
