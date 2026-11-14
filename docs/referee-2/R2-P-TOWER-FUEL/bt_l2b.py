#!/usr/bin/env python3
"""REFEREE-2 succ. 31: byte test L-1 -> L-2 (P-TOWER-FUEL fix round 1, claude/l-lower 740f6c79) with the seven replacements M1-M7
written out literally here (OLD strings: L-1 / my report / REFEREE §5; NEW strings: as fixes entry 1 §5 describes them).
Also: my second-route quote in fixes entry 1 equals my report's text (wrapped lines joined by single spaces).
Usage: bt_l2b.py L1.txt L2.txt FIXES.md MYREPORT.md"""
import sys, re, hashlib
L1, L2, FX, MY = (open(p, encoding='utf-8').read() for p in sys.argv[1:5])
M = [
 ('M1', 'with its notation c_l, γ_l, flip, F(l))', 'with its notation c_l, γ_l, flip, F(l) and cv)'),
 ('M2', 'violates PULSE, GAP ≥ 7 − j only at level 5, 30 times',
  'violates PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window; set = all 119 of them) only at level 5, 30 times (unit = (5-window, PULSE or GAP); in 16 of its 63 5-windows)'),
 ('M3', 'while 48 of its 127 6-windows fail, in each of which the crossed pair 6 is decided by the option (9, 1) of rank 87 (in none of the other 79)',
  'while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (the movers 12 and 13, crossed onto movers 22, 11), and in each of these 48 windows [a, e] the option (9, 1) of rank 87 is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the other 79)'),
 ('M4', 'on 24 runs from the stored start, 62 doubling levels, 757 j-windows',
  'on 24 runs from the stored start (the 15 genomes experiments/lower/l3/kill/*.json, the 7 genomes experiments/lower/l4/rec/*.json and the two instances), 62 doubling (run, level) pairs, 757 j-windows'),
 ('M5', 'DOUBLE-EQ 0 violations;',
  'DOUBLE-EQ 0 violations (its first two clauses on 7,069 (step, doubling level) units, its third on the 757 j-windows, its fourth on the 62 doubling (run, level) pairs, 61 of them with F(j − 1) ≥ 1);'),
 ('M6', 'DOMINANCE-FREEZE 0 on 65,885 equal-decider state pairs and on 1,390 consecutive-move pairs;',
  'DOMINANCE-FREEZE 0 on 65,885 (consecutive-state pair, mover) units with equal deciders and on 1,390 (member of a doubling pair, pair of consecutive moves) units;'),
 ('M7', 'the largest rank in the symmetric difference of the chains of A_0 and A_1',
  'the largest rank in the symmetric difference of the Ξ-chains of the current options of A_0 and A_1'),
]
s = L1
for tag, o, n in M:
    print(tag, 'old in L-1:', L1.count(o), '| new in L-2:', L2.count(n)); assert L1.count(o) == 1 and L2.count(n) == 1
    s = s.replace(o, n)
print('L-1 + M1..M7 == L-2 byte for byte:', s == L2, '| sha1', hashlib.sha1(s.encode()).hexdigest(), len(s.encode()), 'B')
norm = lambda t: re.sub(r'\s*\n\s*', ' ', t)
i = MY.index('  - New: «(iii) 2j and 2j + 1'); mine = norm(MY[i:]).split('«', 1)[1].split('»', 1)[0]
print('my W-1 route quoted verbatim in fixes entry 1:', mine in norm(FX))
