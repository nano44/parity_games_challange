#!/usr/bin/env python3
"""L-LOWER 10: for a core mover x of the level-8 target, the required preference at its free pre-states as a Boolean function of
core movers' states: which single movers y (pref = s_y or 1 - s_y) and which pairs {y, z} determine it (consistent function), and
whether the pair function is XOR/XNOR (needs a third input by ONE-READ XOR). Core = movers 0..15 of the target (helpers excluded).
Usage: readers.py D28 D32 x [x ...]"""
import sys, os, itertools
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from build import *
def table(CT, O, x):
    l = x // 2; rows = []
    for t in range(1, len(CT)):
        s = CT[t - 1]; ns = CT[t]
        free = (s[x] != O[t][l - 1]) if l >= 1 else True
        if free and l >= 1: rows.append((s, ns[x]))
    return rows
if __name__ == '__main__':
    D28 = rd(sys.argv[1]); D = fixgates(rd(sys.argv[2])); CT = core8(D28); pad = (0,) * (2 * D['d'] - 16)
    O = [okeys(D, s + pad) for s in CT]
    for x in map(int, sys.argv[3:]):
        rows = table(CT, O, x)[1:]   # drop the initial step
        ys = [y for y in range(16) if y != x]
        single = [y for y in ys if len({(s[y], p) for s, p in rows}) == 2 and len({s[y] for s, p in rows}) == 2]
        pairs = []
        for y, z in itertools.combinations(ys, 2):
            f = {}
            ok = True
            for s, p in rows:
                k = (s[y], s[z])
                if f.setdefault(k, p) != p: ok = False; break
            if ok: pairs.append((y, z, ''.join(str(f.get(k, '-')) for k in ((0, 0), (0, 1), (1, 0), (1, 1)))))
        xorp = [p for p in pairs if p[2] in ('0110', '1001')]
        print(f'mover {x}: free pre-states {len(rows)}; single readers {single}; consistent pairs {len(pairs)}, of them XOR/XNOR {len(xorp)}; non-XOR pairs {[p for p in pairs if p not in xorp][:12]}')
