#!/usr/bin/env python3
"""L-RED R148: Even-edge RETURNS per Even vertex X in each W-run (P-N5-WRUN's definition: X enters g at k -> k + 1 having held g at an
earlier state of the W-run), on n5b SPEC traces. Prints the W-run with most returns, its length, and the top X by return count.
Usage: retx.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn
from collections import Counter
pg = xcn.pg; n5b = xcn.n5b
a = sys.argv[1:]; g = pg.read(a[0]); st = n5b.read_start(a[1], g) if len(a) > 1 else (None, None)
tr, fb = xcn.trace(g, *st); runs, _ = xcn.wruns(g, tr, fb); best = None
for F in runs:
    held = {}; rc = Counter()
    for v in range(g.n):
        if g.owner[v] == 0: held[v] = {tr[F[0]][0][v]}
    for k in F[:-1]:
        s, s2 = tr[k][0], tr[k + 1][0]
        for v in held:
            if s2[v] != s[v]:
                if s2[v] in held[v]: rc[v] += 1
                held[v].add(s2[v])
    r = (sum(rc.values()), len(F) - 1, rc)
    if best is None or r[:2] > best[:2]: best = r
tot, L, rc = best
print(f"RETX {os.path.basename(a[0])} n {g.n} F {L} returns {tot} topX {rc.most_common(6)}")
