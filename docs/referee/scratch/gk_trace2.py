#!/usr/bin/env python3
"""grouped trace of the IDEAL run on G_k: columns B_j = (u_j v_j), e_j, Y_j = (y_j yb_j), Y'_j = (yp_j ypb_j)."""
import sys
import gk_build as B
import gk_ideal as I
k = int(sys.argv[1])
G = B.genome(k)
nm = G['names']; ix = {n: i for i, n in enumerate(nm)}
L, why, S = I.run(G, keep=True)
def col(s, name): return str(s[ix[name]]) if name in ix else '-'
hdr = 'step | ' + ' '.join('B%d' % j for j in range(k)) + ' | ' + ' '.join('e%d' % j for j in range(2, k - 1)) + ' | ' + ' '.join('Y%d' % j for j in range(1, k)) + ' | ' + ' '.join("Y'%d" % j for j in range(2, k - 1))
print(hdr)
for t in range(L + 1):
    s = S[t]
    row = '%4d | ' % t + ' '.join(col(s, 'u%d' % j) + col(s, 'v%d' % j) for j in range(k)) + ' | ' + ' '.join(col(s, 'e%d' % j) + ' ' for j in range(2, k - 1)) + ' | ' + ' '.join(col(s, 'y%d' % j) + col(s, 'yb%d' % j) for j in range(1, k)) + ' | ' + ' '.join(col(s, 'yp%d' % j) + col(s, 'ypb%d' % j) + ' ' for j in range(2, k - 1))
    ch = [nm[x] for x in range(G['N']) if t > 0 and S[t][x] != S[t - 1][x]]
    print(row + '   ' + ' '.join(ch))
wires = [x for x in range(G['N']) if nm[x].startswith('w')]
print('wires ever move:', any(S[t][x] != S[0][x] for t in range(L + 1) for x in wires), ' wire states:', {nm[x]: S[0][x] for x in wires})
