#!/usr/bin/env python3
"""L-LOWER 10: essential core inputs. For core mover x of the level-8 target (initial step dropped): y is ESSENTIAL if the states
of all core movers except x and y do not determine x's required preference at its free pre-states. Then any x whose closure holds
only core movers must have every essential y in its closure (pref is a function of the closure's states). Usage: essential.py D28 D32"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from build import *
from readers import table
D28 = rd(sys.argv[1]); D = fixgates(rd(sys.argv[2])); CT = core8(D28); pad = (0,) * (2 * D['d'] - 16)
O = [okeys(D, s + pad) for s in CT]
def det(rows, Y):
    f = {}
    for s, p in rows:
        k = tuple(s[y] for y in Y)
        if f.setdefault(k, p) != p: return False
    return True
for x in range(2, 16):
    rows = table(CT, O, x)[1:]; others = [y for y in range(16) if y != x]
    alld = det(rows, others)
    ess = [y for y in others if not det(rows, [z for z in others if z != y])] if alld else None
    print(f'mover {x}: free pre-states {len(rows)}; all core determine: {alld}; essential {ess}')
