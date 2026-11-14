#!/usr/bin/env python3
"""REFEREE-2 succ. 31: L-1 -> L-2 diff for P-TOWER-FUEL fix round 1 (claude/l-lower 740f6c79), own code (difflib on characters,
segments printed with context); L-2 shape (bytes, chars, parens, depth, «|»). Usage: bt_l2.py L1.txt L2.txt"""
import sys, difflib, hashlib
a = open(sys.argv[1], encoding='utf-8').read(); b = open(sys.argv[2], encoding='utf-8').read()
bb = b.encode(); d = m = 0
for ch in b: d += (ch == '(') - (ch == ')'); m = min(m, d)
print('L-2 sha1', hashlib.sha1(bb).hexdigest(), len(bb), 'B', len(b), 'chars', b.count('\n'), 'newline(s)', b.count('('), '«(»', b.count(')'), '«)»', 'min depth', m, b.count('|'), '«|»')
sm = difflib.SequenceMatcher(None, a, b, autojunk=False); n = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': continue
    n += 1; print('--- segment', n, op, 'L-1 [%d:%d] -> L-2 [%d:%d]' % (i1, i2, j1, j2))
    print('  context: …' + a[max(0, i1 - 60):i1] + '⟦'); print('  OLD: «' + a[i1:i2] + '»'); print('  NEW: «' + b[j1:j2] + '»')
print('segments', n)
