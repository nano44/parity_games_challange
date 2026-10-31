#!/usr/bin/env python3
"""L-RED R152: check the tie analysis of R152 §2 on n5b SPEC traces. For every W-run F and every switch of an Even X not in C with
W(X) unchanged (a TIE switch): (T1) the cycle node c = lambda_W(X) parity; (T2) Omega(c) odd: index(new) < index(old) (IDX-MONO);
(T3) Omega(c) even: key_(k+1)(X) < key_k(X), key_t(v) = indices of v's (sigma_t, tau)-path read from c (LEX-BFS), lexicographic;
(T4) KEY-MON: for every v not in C with W_(k+1)(v) = W_k(v), key_(k+1)(v) <= key_k(v) (Omega(c) even) at every transition of F.
Usage: o1key.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg
def path(g, s, t, v, c):
    p = [v]
    while p[-1] != c:
        u = p[-1]; p.append(s[u] if g.owner[u] == 0 else t[u])
        if len(p) > g.n + 1: return None
    return p
def key(g, s, t, v, c):
    p = path(g, s, t, v, c); return None if p is None else tuple(reversed(p[:-1]))
if __name__ == "__main__":
    g = pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    tr, fb = xcn.trace(g, *st); runs, W = xcn.wruns(g, tr, fb)
    ties = {0: 0, 1: 0}; bad = []; km = kmbad = 0
    for F in runs:
        if len(F) < 2: continue
        t = tr[F[0]][1]
        for k in F[:-1]:
            s, s2 = tr[k][0], tr[k + 1][0]; w, w2 = W(s, t), W(s2, t)
            for v in range(g.n):
                if g.owner[v] != 0 or w[v][0] == v or w[v] != w2[v]: continue
                c = w[v][0]; par = g.prio[c] % 2
                if par == 0:
                    a, b = key(g, s, t, v, c), key(g, s2, t, v, c); km += 1
                    if not (b <= a): kmbad += 1; bad.append(("KEYMON", k, v, a, b))
                if s[v] != s2[v]:
                    ties[par] += 1
                    if par == 1 and not (s2[v] < s[v]): bad.append(("IDX", k, v, s[v], s2[v]))
                    if par == 0 and not (key(g, s2, t, v, c) < key(g, s, t, v, c)): bad.append(("KEY", k, v))
    for b in bad[:20]: print("  BAD", b)
    print(f"O1KEY {os.path.basename(sys.argv[1])} n {g.n} ties_even_c {ties[0]} ties_odd_c {ties[1]} keymon_checks {km} bad {len(bad)}")
