#!/usr/bin/env python3
"""pend2.py in.pg scheme > out.pg ; pendant padding schemes (pendants have no predecessor: original regions unchanged).
 e<K>: K pendants (Even, pr 0) on every vertex;  o<K>: K pendants (Odd, pr 1) on every vertex;
 E<K>: K pendants (Even, pr 0) on every even-priority vertex; O<K>: K (Odd, pr 1) on every odd-priority vertex;
 X<K>: K pendants (Even, pr 0) on every odd-priority vertex; Y<K>: K (Odd, pr 1) on every even-priority vertex;
 t<K>: K pendants (Even, pr 0) on the top-priority vertex; u<K>: K (Odd, pr 1) on the top-priority vertex"""
import sys
V = []
for l in open(sys.argv[1]):
    l = l.strip()
    if not l or l.startswith('parity'): continue
    p = l.rstrip(';').split(); V.append((int(p[0]), int(p[1]), int(p[2]), p[3]))
sch = sys.argv[2]; K = int(sch[1:]); c = sch[0]
n = max(v[0] for v in V) + 1
top = max(V, key=lambda v: v[1])[0]
out = ['%d %d %d %s;' % v for v in V]
k = n
for (v, pr, ow, s) in V:
    if c in 'tu' and v != top: continue
    if c == 'E' and pr % 2: continue
    if c == 'O' and pr % 2 == 0: continue
    if c == 'X' and pr % 2 == 0: continue
    if c == 'Y' and pr % 2: continue
    for i in range(K):
        if c in 'eEXt': out.append('%d 0 0 %d;' % (k, v))
        else: out.append('%d 1 1 %d;' % (k, v))
        k += 1
print('parity %d;' % (k - 1))
print('\n'.join(out))
