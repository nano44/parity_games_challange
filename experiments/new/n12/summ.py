#!/usr/bin/env python3
"""summ.py: one line per (config, family) from out/tables.txt and out/tables2.txt: N:calls ... ; then work and maxbits for the kill rows."""
import collections, sys
rows = collections.OrderedDict()
for fn in ('out/tables.txt', 'out/tables2.txt'):
    for l in open(fn):
        if l.startswith('#'): continue
        p = l.split()
        rows.setdefault((p[0], p[1]), []).append(p)
for (c, f), rs in rows.items():
    print('%-10s %-16s calls %s' % (c, f, ' '.join('%s:%s' % (r[2], r[6]) for r in rs)))
print()
for (c, f), rs in rows.items():
    if c.startswith('KILL') or (c, f) in (('P-Sbig', 'tc+'), ('P-topx', 'tc+'), ('P-Sbig', 'counter_symsi'), ('P-topx', 'counter_symsi')):
        print('%-10s %-16s n %s | work %s | maxbits %s | depth %s' % (c, f, ' '.join(r[3] for r in rs), ' '.join(r[13] for r in rs),
              ' '.join(r[14] for r in rs), ' '.join(r[12] for r in rs)))
