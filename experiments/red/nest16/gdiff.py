"""L-RED box 17 (produced on Opus 5.5): what a climb changed. Compares SEED and RESULT on the common vertex ids 0..n_seed-1:
added vertices (owner, priority rank, successors), edge additions/removals, owner changes, and priority-ORDER changes
(ranks of the common vertices). Usage: gdiff.py SEED.pg RESULT.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "xctx"))
import xscore as X
a = X.distinct(X.pg.read(sys.argv[1])); b = X.distinct(X.pg.read(sys.argv[2])); n = a.n
ra = {v: r for r, v in enumerate(sorted(range(n), key=lambda v: a.prio[v]))}
rb = {v: r for r, v in enumerate(sorted(range(n), key=lambda v: b.prio[v]))}
print("seed n", a.n, "result n", b.n)
for v in range(n, b.n): print(f"  + vertex {v}: owner {b.owner[v]} prio {b.prio[v]} succ {b.succ[v]}")
for v in range(n):
    if a.owner[v] != b.owner[v]: print(f"  owner {v}: {a.owner[v]} -> {b.owner[v]}")
    if set(a.succ[v]) != set(b.succ[v]):
        print(f"  edges {v} (owner {b.owner[v]}, prio {b.prio[v]}): +{sorted(set(b.succ[v]) - set(a.succ[v]))} -{sorted(set(a.succ[v]) - set(b.succ[v]))}")
moved = [v for v in range(n) if ra[v] != rb[v]]
pairs = sum(1 for u in range(n) for v in range(u + 1, n) if (a.prio[u] < a.prio[v]) != (b.prio[u] < b.prio[v]))
print("  priority-order inversions among common vertices:", pairs)
if pairs:
    for u in range(n):
        for v in range(u + 1, n):
            if (a.prio[u] < a.prio[v]) != (b.prio[u] < b.prio[v]): print(f"    swapped {u} (prio {a.prio[u]}->{b.prio[u]}) and {v} ({a.prio[v]}->{b.prio[v]})")
