#!/usr/bin/env python3
"""abstract-model trace with derived quantities. Columns per j: B_j=(u v), Y_j=(y yb), e_j, Y'_j, and Wn(j) z(j) z'(j) kap(j) (new state)."""
import sys
import gk_abs as A
k = int(sys.argv[1])
s = A.start(k)
t = 0
def g(s, n): return str(s[n]) if n in s else '-'
print('t | per level j=0..k-1:  [u v | y yb | e | yp ypb]   then  Wn(0..k-1) | z(1..k-1) | zp | kap(0..k-1) of the step computed FROM this state')
while True:
    n, p, kap = A.step(k, s)
    Wn, z, zp = A.xi_side(k, s)
    row = ' '.join('[%s%s|%s%s|%s|%s%s]' % (g(s, 'u%d' % j), g(s, 'v%d' % j), g(s, 'y%d' % j), g(s, 'yb%d' % j), g(s, 'e%d' % j), g(s, 'yp%d' % j), g(s, 'ypb%d' % j)) for j in range(k))
    ch = [x for x in s if n[x] != s[x]]
    print('%3d %s  Wn %s z %s zp %s kap %s   -> %s' % (t, row, ''.join(Wn[j] for j in range(k)), ''.join('Y' if z[j] == 'y' else 'b' for j in range(1, k)), ''.join(('P' if zp[j] == 'yp' else 'b') for j in sorted(zp)), ''.join(kap[j] for j in range(k)), ' '.join(ch)))
    if n == s: break
    s = n; t += 1
