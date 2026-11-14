#!/usr/bin/env python3
"""pend3.py in.pg scheme > out.pg  (regions of the original vertices are unchanged in every scheme)
 T0 / T1: ONE pendant with priority pmax+1 / pmax+2 (no predecessor), owner Even, edge to vertex 0
 D<q>: detour pads: for every Even vertex x and every successor y of x, a new vertex z (owner Even, priority q' , single edge to y) and an edge x -> z,
       where q' = the least ODD priority >= pmax + 1 if q == 1 (bad for Even), or the priority 0-parity... see code
 O<q>: the same for every Odd vertex x with a pad of the least EVEN priority >= pmax + 1 (bad for Odd)
 B: both D and O pads"""
import sys
V = []
for l in open(sys.argv[1]):
    l = l.strip()
    if not l or l.startswith('parity'): continue
    p = l.rstrip(';').split(); V.append([int(p[0]), int(p[1]), int(p[2]), [int(x) for x in p[3].split(',')]])
sch = sys.argv[2]
n = max(v[0] for v in V) + 1; pmax = max(v[1] for v in V)
odd_top = pmax + 1 if (pmax + 1) % 2 else pmax + 2
even_top = pmax + 1 if (pmax + 1) % 2 == 0 else pmax + 2
new = []
k = n
if sch in ('T0', 'T1'):
    new.append([k, pmax + 1 + int(sch[1]), 0, [0]]); k += 1
else:
    for v in V:
        x, pr, ow, succ = v
        if (ow == 0 and sch in ('D', 'B')) or (ow == 1 and sch in ('O', 'B')):
            extra = []
            for y in list(succ):
                new.append([k, odd_top if ow == 0 else even_top, ow, [y]]); extra.append(k); k += 1
            v[3] = succ + extra
V += new
print('parity %d;' % (k - 1))
for v in V: print('%d %d %d %s;' % (v[0], v[1], v[2], ','.join(map(str, v[3]))))
