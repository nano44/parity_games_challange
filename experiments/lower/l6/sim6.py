#!/usr/bin/env python3
"""L-LOWER 6 (BOX L6): text-genome simulator (Python big integers, no overflow at any d), written from l5/fev.c's rules
(= l3/sim.py's, cross-checked there). Genome text format: d / xt / br / bp / gate / start. Importable: rd, wr, run, chain, dec, caps.
run(D) -> (S, O): S[t] = state tuple (t = 0..T), O[t] = key vector o(l) under S[t] (o at s_0 computed as in fev)."""
import sys
def rd(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] == 'd': D['d'] = int(w[1])
        if w and w[0] in ('xt', 'br', 'bp', 'gate', 'start'): D[w[0]] = list(map(int, w[1:]))
    return D
def wr(D, p):
    with open(p, 'w') as f:
        f.write(f"d {D['d']}\n")
        for k in ('xt', 'br', 'bp', 'gate', 'start'): f.write(k + ' ' + ' '.join(map(str, D[k])) + '\n')
def caps(F):
    h = 0
    for l, v in enumerate(F):
        if v == 2 ** (l + 2) - 2: h += 1
        else: break
    return h
def topo(D):
    N = 2 * D['d']; xt = D['xt']; vis = [0] * N; out = []
    def go(x):
        if vis[x] == 2: return True
        if vis[x] == 1: return False
        vis[x] = 1
        for k in (0, 1):
            y = xt[2 * x + k]
            if y >= 0 and not go(y): return False
        vis[x] = 2; out.append(x); return True
    sys.setrecursionlimit(10000)
    for x in range(N):
        if not go(x): return None
    return out
def bv(D, m): return -(1 << D['br'][m]) if D['bp'][m] else (1 << D['br'][m])
def okeys(D, s):
    d = D['d']; g = D['gate']; o = []; c = 0
    for l in range(d):
        if l == 0: ol = int(g[0 + s[0]] > g[2 + s[1]])
        else:
            a, b = s[2 * l], s[2 * l + 1]; ol = int(a != c) if a != b else int(g[4 * l + a] > g[4 * l + 2 + a])
        o.append(ol); c = ol
    return o
def values(D, s, order):
    v = {}
    for x in order:
        m = 2 * x + s[x]; y = D['xt'][m]; v[x] = bv(D, m) + (v[y] if y >= 0 else 0)
    return v
def run(D, cap=20000):
    d = D['d']; N = 2 * d; order = topo(D)
    if order is None: return None, None
    s = list(D['start']); S = [tuple(s)]; O = [okeys(D, s)]
    g = D['gate']
    while len(S) <= cap:
        v = values(D, s, order); av = []
        for x in range(N):
            m = 2 * x + 1 - s[x]; y = D['xt'][m]; ov = bv(D, m) + (v[y] if y >= 0 else 0); av.append(ov > v[x])
        if not any(av): break
        ns = list(s); c = 0
        for l in range(d):
            for q in (0, 1):
                x = 2 * l + q
                if l == 0:
                    if av[x] and g[2 * x + 1 - s[x]] < g[2 * x + s[x]]: ns[x] = 1 - s[x]
                elif av[x] and s[x] != c: ns[x] = c
            if l == 0: ol = int(g[0 + ns[0]] > g[2 + ns[1]])
            else:
                a, b = ns[2 * l], ns[2 * l + 1]; ol = int(a != c) if a != b else int(g[4 * l + a] > g[4 * l + 2 + a])
            c = ol
        if ns == s: break
        s = ns; S.append(tuple(s)); O.append(okeys(D, s))
    return S, O
def Fprof(D, O):
    return [sum(1 for t in range(1, len(O)) if O[t][l] != O[t - 1][l]) for l in range(D['d'])]
def chain(D, s, x, k):
    out = []
    while True:
        m = 2 * x + k; out.append((D['br'][m], D['bp'][m], x, k)); y = D['xt'][m]
        if y < 0: return out
        x, k = y, s[y]
def dec(D, s, x):
    a = set(chain(D, s, x, 0)); b = set(chain(D, s, x, 1)); t = max(a ^ b); return (t[0], t[2], t[3], 0 if t in a else 1)
if __name__ == '__main__':
    for p in sys.argv[1:]:
        D = rd(p); S, O = run(D)
        if S is None: print(p, 'CYCLIC'); continue
        F = Fprof(D, O); print(p, 'T', len(S) - 1, 'caps', caps(F), 'F', *F)
