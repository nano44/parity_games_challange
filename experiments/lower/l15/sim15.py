#!/usr/bin/env python3
"""L-LOWER 15: independent replay of a decoded private cascade (ekr.py output) with integer ENC values (R105: value of option =
+-2^rank + value of its Xi-target's current option), movement (M3), keys (M4), o(7) = t mod 2; checks separation of the clients'
lists on rows 0..P. Usage: sim15.py CASCADE GENOME TARGET P CLIENTS"""
import sys, os, subprocess, ast
here = os.path.dirname(os.path.abspath(__file__))
D = {}
for ln in open(sys.argv[1]):
    w = ln.split(); D[w[0]] = w[1:]
K = int(D['k'][0]); H = 2 * K; xt = list(map(int, D['xt'])); rank = list(map(int, D['rank'])); even = list(map(int, D['even']))
gate = list(map(int, D['gate'])); s = [int(c) for c in D['start'][0]]
gen, tp, P, CL = sys.argv[2], sys.argv[3], int(sys.argv[4]), [int(c) for c in sys.argv[5].split(',')]
eps = [(1 if even[a] else -1) * 2 ** rank[a] for a in range(2 * H)]
def value(op, s):
    v = 0
    while True:
        v += eps[op]; z = xt[op]
        if z < 0: return v
        op = 2 * z + s[z]
S = [tuple(s)]
for t in range(P):
    bet = [1 if value(2 * y + 1, s) > value(2 * y, s) else 0 for y in range(H)]
    ns = list(s); c = (t + 1) % 2
    for i in range(K):
        for y in (2 * i, 2 * i + 1):
            if bet[y] != s[y] and s[y] != c: ns[y] = c
        a, b = ns[2 * i], ns[2 * i + 1]; c = (a ^ c) if a != b else gate[2 * i + a]
    s = ns; S.append(tuple(s))
ok = True
for x in CL:
    l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), gen, tp, str(x), str(P)], capture_output=True, text=True).stdout
    seen = {}
    for t, r in ast.literal_eval(l[l.index('['):l.index('] |') + 1]):
        if seen.setdefault(S[t], r) != r: ok = False; print('client', x, 'NOT separated at row', t)
print('REPLAY', os.path.basename(sys.argv[1]), 'K', K, 'P', P, 'clients', CL, 'separation', 'OK' if ok else 'FAILS', '| moves per helper', [sum(1 for t in range(1, len(S)) if S[t][y] != S[t - 1][y]) for y in range(H)])
