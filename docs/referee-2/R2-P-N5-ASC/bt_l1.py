#!/usr/bin/env python3
"""REFEREE-2 succ. 31: P-N5-ASC fix round 1 (claude/l-new 19cc23e3): L-1 shape, the required strings (new once, old absent), my
proposed L-1 changes (old once), and the DATA sums from the re-run check193 output.
Usage: bt_l1.py L1.txt CHECK193.out"""
import sys, hashlib, re
L = open(sys.argv[1], encoding='utf-8').read(); O = open(sys.argv[2], encoding='utf-8').read()
b = L.encode(); d = m = 0
for ch in L: d += (ch == '(') - (ch == ')'); m = min(m, d)
print('L-1 sha1', hashlib.sha1(b).hexdigest(), len(b), 'B', L.count('\n'), 'newline(s)', L.count('('), '«(»', L.count(')'), '«)»', 'min depth', m, L.count('|'), '«|»')
for tag, old, new in [('W-1 §1', '(only for §6 UP-JUMP and UP-B)', '(only for §6 UP-JUMP, UP-B and NOUP)'),
                      ('W-1 table', 'UP-JUMP and UP-B under HYPOTHESIS [E-LEV]', 'UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]'),
                      ('W-1 title', 'in particular on genomes with boundedly many upward Ξ-edges (UP-B)',
                       'in particular, under the e-priority hypothesis [E-LEV], on genomes with boundedly many upward Ξ-edges (UP-B)')]:
    print(tag, '| new in L-1:', L.count(new), '| old in L-1:', L.count(old))
for s in ['under [E-LEV]: max ascents ≤ U(G) on all 13 instances', 'NOUP under [E-LEV]', 'NOT R and NOT any running time',
          'G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim', 'all pinned in asc.pins', 'M 6 and 7 re-run by check193.sh',
          'F′_0 = F_0 (DESC-POLY on the whole interval)', 'the number D_E(v) of distinct (Λ_t(v), E_t(v))', '«C ≤ n·(2M + 2).»',
          '(consecutive state pair, W-target with Λ fixed) pairs', 'UP-JUMP: violations 0 in 1,956 ascents of movers\' plays with Λ below every e']:
    print('L-1 contains', L.count(s), 'x:', s)
tot = {}
for ln in O.splitlines():
    if ln.split()[:1] and ln.split()[0].endswith('.json') and ' edomfail ' in ln:
        w = ln.split()
        for k in ('edomfail', 'decfail', 'tmonfail', 'upfail', 'asc', 'edomunits', 'decunits', 'tmonunits'):
            tot[k] = tot.get(k, 0) + int(w[w.index(k) + 1])
print('check193 sums over the 13 instance lines:', tot)
print('M 7 line:', [l for l in O.splitlines() if l.startswith('CS(M 7')])
print('ug193 lines:', sum(1 for l in O.splitlines() if 'U(G)' in l and 'max ascents' in l))
