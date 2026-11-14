#!/usr/bin/env python3
"""REFEREE-2 succ. 31: byte test L-2 + C134 §5 R1-R4 (applied in order) == L-3 (P-TOWER-FUEL, claude/l-lower 4f25ae6f). Strings copied
from docs/checker/C134.md §5 (claude/checker 23871f48), wrapped lines joined by one space. Usage: bt_l3.py L2.txt L3.txt"""
import sys, hashlib
L2, L3 = (open(p, encoding='utf-8').read() for p in sys.argv[1:3])
R = [('R1', ' (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md; L-LOWER successor 5)',
      ' (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md with its fixes entry 1, docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6)'),
     ('R2', '; G-N5-TIME stays OPEN; not M3, not a gauntlet step',
      "; the proof of record of CROSS-ECONOMY's sign-change clause is referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second route), signed by both referees; G-N5-TIME stays OPEN; not M3, not a gauntlet step"),
     ('R3', 'not a gauntlet step', 'not a step-4 pass'),
     ('R4', 'meets PULSE, GAP ≥ 7 − j at levels 1-5 while', 'meets PULSE, GAP ≥ 7 − j at levels 1-5 (unit = j-window; set = all 119 of them) while')]
s = L2
for tag, o, n in R:
    c = s.count(o); print(tag, 'old occurs', c, 'time(s) in the text it is applied to'); assert c == 1
    s = s.replace(o, n)
b = s.encode(); d = m = 0
for ch in s: d += (ch == '(') - (ch == ')'); m = min(m, d)
print('L-2 + R1..R4 == L-3:', s == L3, '| sha1', hashlib.sha1(b).hexdigest(), len(b), 'B', s.count('\n'), 'newline(s)', s.count('('), '«(»', s.count(')'), '«)»',
      'min depth', m, s.count('|'), '«|»', s.count(' — '), '« — »', s.count('gauntlet'), '«gauntlet»')
