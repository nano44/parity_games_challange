#!/usr/bin/env python3
"""L-NEW: route (B) via traps (N1-killer-sketch.md): every Even vertex with >= 2 successors gets an extra edge to its own
trap t_v -> c_v (t_v Odd single-successor of even priority P = B + 2 + 2k, c_v Odd self-loop of odd priority B + 1,
B = max original priority rounded up to even). Traps lose for Even, so regions on the original vertices are unchanged.
All traps are revealed at the same phase (~ (2k + 1) log2 n); best-reward start = all traps for plain VJ Howard too.
Usage: alltrap.py game.pg k [--q Q] > out.pg   (--q: odd priority of the trap cycles; default B + 1; --q 1 = latest reveal)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); k = int(sys.argv[2])
B = max(g.prio); B += B % 2
Q = int(sys.argv[sys.argv.index('--q') + 1]) if '--q' in sys.argv else B + 1; assert Q % 2 == 1
prio = list(g.prio); owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
for v in range(g.n):
    if g.owner[v] != 0 or len(succ[v]) < 2: continue
    t, c = len(prio), len(prio) + 1
    prio += [B + 2 + 2 * k, Q]; owner += [1, 1]; succ += [[c], [c]]; succ[v] = sorted(succ[v] + [t])
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
