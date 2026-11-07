#!/usr/bin/env python3
"""P-TOWER-FUEL fix round 1 (L-LOWER successor 6): build line L-2 from L-1 by the merged replacements of fixes entry 1.
Every OLD string and every referee-supplied NEW string is copied from byte copies of the two reports (wrapped report lines joined
by single spaces); the merged NEW strings (Lead rulings 15:18Z) are this lane's text. Asserts: each old once in L-1, each new once in
L-2, «(» = «)», depth never negative, no «|». Usage: mkL2_tf.py R1.md R2.md L1.txt OUT_L2.txt"""
import sys, re, hashlib
R1, R2, L1 = (open(p, encoding='utf-8').read() for p in sys.argv[1:4]); OUT = sys.argv[4]
def norm(s): return re.sub(r'\s*\n\s*', ' ', s)
def grab(src, anchor, which):
    """the which-th «…» string (0 = Old, 1 = New) in the item that begins at the first occurrence of anchor"""
    i = src.index(anchor); seg = src[i:]
    q = re.findall(r'«(.*?)»', seg, flags=re.S)
    return norm(q[which])
def grab_after(src, anchor, label):
    i = src.index(anchor); j = src.index(label, i); k = src.index('«', j) + 1; e = src.index('»', k)
    return norm(src[k:e])
# REFEREE 27 (R1) items, §5
TFL1_old = grab_after(R1, '- TF-L1 (required).', 'Old:'); TFL2_old = grab_after(R1, '- TF-L2 (required).', 'Old:')
TFL2_new = grab_after(R1, '- TF-L2 (required).', 'New:'); TFL3_old = grab_after(R1, '- TF-L3 (required).', 'Old:')
TFL4_old = grab_after(R1, '- TF-L4 (optional).', 'Old:'); TFL4_new = grab_after(R1, '- TF-L4 (optional).', 'New:')
TFL5_old = grab_after(R1, '- TF-L5 (optional).', 'Old:')
# REFEREE-2 31 (R2) items, «Required changes»
def w2(tag, which):
    i = R2.index('- ' + tag + ': «'); q = re.findall(r'«(.*?)»', R2[i:], flags=re.S); return norm(q[which])
W2a_old, W2a_new = w2('W-2 (a)', 0), w2('W-2 (a)', 1); W2b_old = w2('W-2 (b)', 0); W2c_old = w2('W-2 (c)', 0)
W4a_old, W4a_new = w2('W-4 (a)', 0), w2('W-4 (a)', 1); W4b_old = w2('W-4 (b)', 0); W4c_old = w2('W-4 (c)', 0)
assert TFL1_old == W4b_old and TFL3_old == W2c_old and TFL5_old == W2b_old and W4c_old in TFL2_old, 'targets differ'
REPL = [
 ('M1 notation (W-2 (a))', W2a_old, W2a_new),
 ('M2 I-ROOM (TF-L5 + W-2 (b) + TF-3 unit)', TFL5_old,
  'violates PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window; set = all 119 of them) only at level 5, 30 times (unit = '
  '(5-window, PULSE or GAP); in 16 of its 63 5-windows)'),
 ('M3 I-FUEL (TF-L3 + W-2 (c))', TFL3_old,
  'while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (the movers 12 and 13, crossed onto movers '
  '22, 11), and in each of these 48 windows [a, e] the option (9, 1) of rank 87 is dec_s(12) or dec_s(13) at some state s among '
  's_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the other 79)'),
 ('M4 corpus (W-4 (a))', W4a_old, W4a_new),
 ('M5 DOUBLE-EQ (TF-L1 + W-4 (b))', TFL1_old,
  'DOUBLE-EQ 0 violations (its first two clauses on 7,069 (step, doubling level) units, its third on the 757 j-windows, its fourth '
  'on the 62 doubling (run, level) pairs, 61 of them with F(j − 1) ≥ 1);'),
 ('M6 DOMINANCE-FREEZE (TF-L2 + W-4 (c))', TFL2_old, TFL2_new),
 ('M7 CROSS-ECONOMY chains (TF-L4)', TFL4_old, TFL4_new),
]
line = L1.rstrip('\n'); assert L1.endswith('\n') and '\n' not in line
for tag, o, n in REPL: assert line.count(o) == 1, (tag, line.count(o), o)
L2 = line
for tag, o, n in REPL: L2 = L2.replace(o, n)
for tag, o, n in REPL: assert L2.count(n) == 1, (tag, L2.count(n))
dep = 0
for ch in L2:
    dep += (ch == '(') - (ch == ')'); assert dep >= 0
assert dep == 0 and '|' not in L2
open(OUT, 'w', encoding='utf-8').write(L2 + '\n')
b = (L2 + '\n').encode('utf-8')
for tag, o, n in REPL: print(tag, '\n   OLD «' + o + '»\n   NEW «' + n + '»')
print('L-2:', OUT, 'sha1', hashlib.sha1(b).hexdigest(), len(b), 'bytes,', len(L2) + 1, 'characters,', L2.count('('), '«(» =', L2.count(')'), '«)»; 0 «|»')
