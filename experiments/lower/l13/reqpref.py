#!/usr/bin/env python3
"""L-LOWER 13: required-preference sequence of a core mover X on target rows 0..P. At each row t < P where X is free
(level 0: gate rule; level l >= 1: s[X] != o(l-1) of row t+1's lower levels, R104: ns built level by level), the target's next
state ns[X] is X's required preference. Prints the list (t, required pref) and the number of changes R between consecutive
free pre-states. Core gates (levels 0..H-1) from GENOME. Usage: reqpref.py GENOME TARGET X P"""
import sys
L = None
G, tp, X, P = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
g = None
for ln in open(G):
    w = ln.split()
    if w and w[0] == 'gate': g = list(map(int, w[1:]))
T = open(tp).read().split(); S = [[int(c) for c in T[2 + i]] for i in range(int(T[0]))]
def okeys(row, upto):
    o = []; c = None
    for l in range(upto + 1):
        a, b = row[2 * l], row[2 * l + 1]
        if l == 0: ol = int(g[0 + a] > g[2 + b])
        else: ol = int(a != c) if a != b else int(g[4 * l + a] > g[4 * l + 2 + a])
        o.append(ol); c = ol
    return o
l = X // 2; seq = []
for t in range(P):
    s, ns = S[t], S[t + 1]
    if l == 0: free = g[2 * X + 1 - s[X]] < g[2 * X + s[X]]
    else: free = s[X] != okeys(ns, l - 1)[l - 1]
    if free: seq.append((t, ns[X]))
    elif s[X] != ns[X]: print('INCONSISTENT target: blocked mover moves at', t)
R = sum(1 for i in range(1, len(seq)) if seq[i][1] != seq[i - 1][1])
print('X', X, 'rows 0..%d' % P, 'free pre-states (t, required pref):', seq, '| changes R =', R)
