#!/usr/bin/env python3
"""L-RED: per-Odd-vertex count of sigma-bar changes along N5-SF's run (between consecutive recorded states), plus the per-Even-vertex
sigma switch counts. Usage: pervtx.py GAME.pg [--start F]   prints n, iterations, SBC, max/sum of per-vertex sigma-bar changes and the top 8."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sf2, pg, n5b, sftrace
a = sys.argv[1:]; g = pg.read(a[0]); L = sftrace.labels(a[0]); nm = lambda v: L.get(v, str(v))
start = a[a.index("--start") + 1] if "--start" in a else None
s = sf2.SF(g); rec = []; sig, tau = n5b.read_start(start, g) if start else (None, None)
s.run_sf(sig, tau, rec=rec)
cb = [0] * g.n; cs = [0] * g.n
for x, y in zip(rec, rec[1:]):
    for v in range(g.n):
        if g.owner[v] == 1 and x["sb"][v] != y["sb"][v]: cb[v] += 1
        if g.owner[v] == 0 and x["s"][v] != y["s"][v]: cs[v] += 1
sc, sbc, tc, tbc, lam = sf2.stats(rec)
top = sorted(range(g.n), key=lambda v: -cb[v])[:8]; tops = sorted(range(g.n), key=lambda v: -cs[v])[:5]
print(f"n {g.n} it {len(rec)-1} SBC {sbc} max-sbar-changes/vertex {max(cb)} sum {sum(cb)} top {[(nm(v), cb[v]) for v in top]} "
      f"max-sigma-switches/vertex {max(cs)} top {[(nm(v), cs[v]) for v in tops]}")
