#!/usr/bin/env python3
"""L-LOWER 10: smallest sets of core movers (0..15, minus excluded) whose states determine a core mover's required preference
at its free pre-states (initial step dropped) in the level-8 target. Usage: minset.py D28 D32 x kmax [excluded,...]"""
import sys, os, itertools
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from build import *
from readers import table
D28 = rd(sys.argv[1]); D = fixgates(rd(sys.argv[2])); CT = core8(D28); pad = (0,) * (2 * D['d'] - 16)
O = [okeys(D, s + pad) for s in CT]; x = int(sys.argv[3]); kmax = int(sys.argv[4])
exc = set(map(int, sys.argv[5].split(','))) if len(sys.argv) > 5 and sys.argv[5] else set()
rows = table(CT, O, x)[1:]; ys = [y for y in range(16) if y != x and y not in exc]
for k in range(1, kmax + 1):
    sols = []
    for Y in itertools.combinations(ys, k):
        f = {}; ok = True
        for s, p in rows:
            key = tuple(s[y] for y in Y)
            if f.setdefault(key, p) != p: ok = False; break
        if ok: sols.append(Y)
    if sols: print(f'mover {x} excl {sorted(exc)}: k = {k}, {len(sols)} sets, e.g. {sols[:8]}'); break
else: print(f'mover {x} excl {sorted(exc)}: none up to k = {kmax}')
