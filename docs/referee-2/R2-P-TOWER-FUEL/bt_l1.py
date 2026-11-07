#!/usr/bin/env python3
"""REFEREE-2 succ. 31: byte test of my required L-1 changes W-2 (a)-(c), W-4 (a)-(c) on docs/lower/P-TOWER-FUEL-line-L1.txt (7f7ff6f5).
Usage: git show 7f7ff6f5:docs/lower/P-TOWER-FUEL-line-L1.txt | bt_l1.py"""
import sys, hashlib
s = sys.stdin.buffer.read().decode()
W = [
 ("W-2 (a)", "with its notation c_l, γ_l, flip, F(l))", "with its notation c_l, γ_l, flip, F(l) and cv)"),
 ("W-2 (b)", "violates PULSE, GAP ≥ 7 − j only at level 5, 30 times",
  "violates PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window; set = all 119 of them) only at level 5, 30 times"),
 ("W-2 (c)", "while 48 of its 127 6-windows fail, in each of which the crossed pair 6 is decided by the option (9, 1) of rank 87 (in none of the other 79)",
  "while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (crossed onto movers 22, 11), and in each of these 48 windows [a, e] the deciding element dec of mover 12 or 13 is the option (9, 1) of rank 87 at some state s_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the other 79)"),
 ("W-4 (a)", "on 24 runs from the stored start, 62 doubling levels, 757 j-windows",
  "on 24 runs from the stored start (the 15 genomes experiments/lower/l3/kill/*.json, the 7 genomes experiments/lower/l4/rec/*.json and the two instances), 62 doubling (run, level) pairs, 757 j-windows"),
 ("W-4 (b)", "DOUBLE-EQ 0 violations;",
  "DOUBLE-EQ 0 violations on 7,069 (step, doubling level) units for its first two clauses, on the 757 j-windows for the third and on the 62 doubling (run, level) pairs for the fourth;"),
 ("W-4 (c)", "0 on 65,885 equal-decider state pairs", "0 on 65,885 (consecutive-state, mover) pairs with equal deciders"),
]
for name, old, new in W:
    n = s.count(old); print(name, 'old occurs', n, 'time(s)'); assert n == 1
    s = s.replace(old, new)
b = s.encode(); d = m = 0
for ch in s: d += (ch == '(') - (ch == ')'); m = min(m, d)
print('L-1 + W-2 + W-4: sha1', hashlib.sha1(b).hexdigest(), len(b), 'B', s.count('\n'), 'line(s)', s.count('('), '«(»', s.count(')'), '«)»', 'min depth', m, s.count('|'), '«|»')
