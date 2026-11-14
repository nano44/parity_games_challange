#!/usr/bin/env python3
"""summ13.py: one line per (mode, family) from out/tables13.txt: N:jumps ...; then max(maxbits - wbits) and the CAP count."""
import collections
rows = collections.OrderedDict(); mx = -10 ** 9; cap = 0; nrows = 0
for l in open('out/tables13.txt'):
    if l.startswith('#'): continue
    p = l.split()
    if p[0] == 'gkk':
        rows.setdefault((p[0], p[1]), []).append('%s:%s' % (p[2], p[10]))      # iters
    else:
        rows.setdefault((p[0], p[1]), []).append('%s:%s' % (p[2], p[10]))      # jumps
        mx = max(mx, int(p[16]) - int(p[18])); nrows += 1
        if p[-1] != 'done': cap += 1
for (m, f), r in rows.items():
    print('%-5s %-16s %s' % (m, f, ' '.join(r)))
print('n13 rows %d, not done %d, max(maxbits - wbits) %d' % (nrows, cap, mx))
