#!/usr/bin/env python3
"""L-COMP box 32: clamped replay for SUB-PROBLEM models (e.g. the f6 gadget). Core movers in CLAMP follow the target rows; every
other mover moves by the R104 rules (ENC preference: sign of the top-rank option of chain(x,0) xor chain(x,1); level 0 gate rule;
level l >= 1 free iff s[x] != o(l-1) of the new state). Written independently of enc32.py (no shared code).
Reports, for each core mover NOT clamped, the first step at which its state leaves the target (or OK through T), and whether the
clamped run is at a fixed point at T for the unclamped movers.
Usage: clampcheck.py GENOME TARGET H CLAMPLIST   (CLAMPLIST like 0-12,14-15)"""
import sys
def rng(sp):
    out = []
    for part in sp.split(','):
        if '-' in part: a, b = map(int, part.split('-')); out += list(range(a, b + 1))
        elif part: out.append(int(part))
    return out
def rd(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] == 'd': D['d'] = int(w[1])
        elif w and w[0] in ('xt', 'br', 'bp', 'gate', 'start'): D[w[0]] = list(map(int, w[1:]))
    return D
gp, tp, H, CL = sys.argv[1], sys.argv[2], int(sys.argv[3]), set(rng(sys.argv[4]))
D = rd(gp); d = D['d']; N = 2 * d; xt, br, bp, g = D['xt'], D['br'], D['bp'], D['gate']
L = open(tp).read().split(); rows = int(L[0]); S = [[int(c) for c in L[2 + i]] for i in range(rows)]; T = rows - 1; NC = 2 * H
def chain(s, x, k):
    out = []; y, j = x, k
    while True:
        m = 2 * y + j; out.append(m); y = xt[m]
        if y < 0: return out
        j = s[y]
def pref(s, x):
    A = set(chain(s, x, 0)); B = set(chain(s, x, 1)); Dl = A ^ B
    top = max(Dl, key=lambda m: br[m]); side = 1 if top in B else 0
    return side if bp[top] == 0 else 1 - side
def okey(s, l, c):
    if l == 0: return int(g[0 + s[0]] > g[2 + s[1]])
    a, b = s[2 * l], s[2 * l + 1]
    return int(a != c) if a != b else int(g[4 * l + a] > g[4 * l + 2 + a])
s = list(S[0][:NC]) + list(D['start'][NC:])
first_bad = {x: None for x in range(NC) if x not in CL}
for t in range(1, T + 2):
    ns = list(s); c = 0
    for l in range(d):
        for q in (0, 1):
            x = 2 * l + q
            if x in CL: ns[x] = S[min(t, T)][x]; continue
            p = pref(s, x)
            if l == 0:
                if p != s[x] and g[2 * x + 1 - s[x]] < g[2 * x + s[x]]: ns[x] = p
            elif p != s[x] and s[x] != c: ns[x] = c
        c = okey(ns, l, c)
    if t <= T:
        for x in first_bad:
            if first_bad[x] is None and ns[x] != S[t][x]: first_bad[x] = t
        s = ns
    else:
        fp = all(ns[x] == s[x] for x in range(N) if x not in CL)
for x, b in first_bad.items(): print(f'mover {x}: ' + ('follows the target through T %d' % T if b is None else 'leaves the target at t %d' % b))
print('fixed point at T for unclamped movers:', fp)
