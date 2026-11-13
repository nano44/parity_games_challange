#!/usr/bin/env python3
"""trace of the IDEAL run on G_k: per step, the movers that change and (optionally) availability."""
import sys
import gk_build as B
import gk_ideal as I
k = int(sys.argv[1])
G = B.genome(k)
nm = G['names']
L, why, S = I.run(G, keep=True)
print('G_%d L %d stop %s' % (k, L, why))
print('movers:', ' '.join('%s(l%d)' % (nm[x], G['lev'][x]) for x in range(G['N'])))
def show(s): return ''.join(str(c) for c in s)
print('  0 %s' % show(S[0]))
for j in range(1, L + 1):
    ch = [nm[x] + ':%d>%d' % (S[j - 1][x], S[j][x]) for x in range(G['N']) if S[j][x] != S[j - 1][x]]
    print('%3d %s  %s' % (j, show(S[j]), ' '.join(ch)))
# final availability
s = S[-1]
print('final avail (movers with |A| > 1):', ' '.join('%s%s' % (nm[x], I.avail(G, s, x)) for x in range(G['N']) if len(I.avail(G, s, x)) > 1))
