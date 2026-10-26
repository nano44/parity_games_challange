#!/usr/bin/env python3
"""Shrink harder, preserving a RULER RE-RUN: objective = (reuse count at the best Odd choice vertex >= R) and longest phase >= THR.
reuse(q) = #path-set changes of Xi(q) in the longest phase at levels already used earlier in that phase. Deletes edges (out-degree >= 1),
then reports reachable vertex count. Usage: shrink2.py GAME START THR R OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x, pg
from phclimb import save
def measure(g, st):
    try: E, rows = n3x.trace(g, st)
    except Exception: return None
    keys = [(r["lam"], r["tau"]) for r in rows]; best = (0, 0, 0); i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
        if j - i > best[0]: best = (j - i, i, j)
        i = j + 1
    T, i, j = best; ru = 0
    for q in range(g.n):
        if g.owner[q] != 1 or len(set(g.succ[q])) < 2: continue
        used, r = set(), 0
        for k in range(i, j):
            a, b = rows[k]["vs"][q], rows[k + 1]["vs"][q]
            if a[1] != b[1]:
                L = (a[1] ^ b[1]).bit_length() - 1; r += L in used; used.add(L)
        ru = max(ru, r)
    return T, ru
g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]); thr, R, out = int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
print("start", measure(g, st))
changed = True
while changed:
    changed = False
    for v in range(g.n):
        for w in list(g.succ[v]):
            if len(g.succ[v]) == 1: break
            succ = [list(x) for x in g.succ]; succ[v] = [x for x in succ[v] if x != w]
            h = pg.Game(list(g.prio), list(g.owner), succ)
            s = ({a: b for a, b in st[0].items() if b in h.succ[a]}, {a: b for a, b in st[1].items() if b in h.succ[a]})
            m = measure(h, s)
            if m and m[0] >= thr and m[1] >= R: g, st, changed = h, s, True
print("end", measure(g, st), "edges", sum(len(s) for s in g.succ)); save(g, st, out)
