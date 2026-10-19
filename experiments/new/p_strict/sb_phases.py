#!/usr/bin/env python3
"""Box 8: hand-built one-player family F(k, m) testing Conjecture SB1 (switch-best ≤ n steps). A shared path p_1..p_k (edges to both
neighbours and to the sink z); m cycle tops u_1 < ... < u_m (even, increasing relevance), C_j through the path in alternating
direction; for j ≥ 2 a blocker u_j -> b_j (odd, just above u_j) -> y_j (even self-loop with u_{j-2} < y_j < u_{j-1}). Start: path ->
z, u_j -> b_j. Counts switch-best steps (one-player = N5's Even step) and checks optimality (Zielonka). Usage: sb_phases.py k m [pvar]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, zielonka
from n5 import Engine
def build(k, m, pvar=0):
    V = {}; prio = []; succ = []
    def add(name, p): V[name] = len(prio); prio.append(p); succ.append([])
    add('z', 0)
    for i in range(1, k + 1): add(('p', i), 2 * i - 1 + (pvar if i % 2 else 0) * 0 + (1 if pvar and i % 2 == 0 else 0))
    base = 4 * k + 10
    # relevance ladder: y_2 < u_1 < y_3 < u_2 < b_2 < ... ; u_j at base + 10 j (even), b_j = u_j + 1 (odd), y_j = u_{j-1} - 4 (even)
    for j in range(1, m + 1):
        add(('u', j), base + 10 * j)
        if j >= 2: add(('b', j), base + 10 * j + 1); add(('y', j), base + 10 * (j - 1) - 4)
    E = lambda a, b: succ[V[a]].append(V[b])
    E('z', 'z')
    for i in range(1, k + 1):
        E(('p', i), 'z')
        if i < k: E(('p', i), ('p', i + 1))
        if i > 1: E(('p', i), ('p', i - 1))
    for j in range(1, m + 1):
        if j % 2: E(('u', j), ('p', 1)); E(('p', k), ('u', j))
        else: E(('u', j), ('p', k)); E(('p', 1), ('u', j))
        if j >= 2: E(('u', j), ('b', j)); E(('b', j), ('y', j)); E(('y', j), ('y', j))
    n = len(prio); g = pg.Game(prio, [0] * n, [sorted(set(s)) for s in succ])
    s = list(range(n))
    for v in range(n): s[v] = g.succ[v][0]
    for i in range(1, k + 1): s[V[('p', i)]] = V['z']
    for j in range(2, m + 1): s[V[('u', j)]] = V[('b', j)]
    if m >= 1: s[V[('u', 1)]] = V[('p', 1)]
    return g, s
def sb(g, s):
    E = Engine(g); k = 0
    while True:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        if not Is: return k, s, E
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n)}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) for v in range(g.n)])
        Eh = Engine(h); x, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(x); k += 1
k, m = int(sys.argv[1]), int(sys.argv[2]); pvar = int(sys.argv[3]) if len(sys.argv) > 3 else 0
g, s = build(k, m, pvar); steps, fin, E = sb(g, s)
win, ws = E.regions(tuple(fin)); ok = list(win) == list(zielonka.solve(g))
print(f"k={k} m={m} n={g.n} switch-best steps={steps} steps-n={steps - g.n} regions ok={ok}")
