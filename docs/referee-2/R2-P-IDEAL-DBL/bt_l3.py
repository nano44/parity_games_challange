# REFEREE-2 succ. 30: byte test P-IDEAL-DBL L-2 -> L-3 (CHECKER C133 §5 R1-R6, in order; wrapped lines joined by one space)
import sys, hashlib
L2 = open(sys.argv[1], encoding='utf-8').read(); L3 = open(sys.argv[2], encoding='utf-8').read()
R = [("R1xx [refereed-only] In the IDEAL model of RESULTS R104", "In the IDEAL model of RESULTS R104"),
     (" (2026-11-07; source: packet P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md, which carries every proof)", " (P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md; L-SI successors 41-42)"),
     (" (DATA, experiments/si/box79/dblcheck.py, CORPUS = ", " (2026-11-07) — each statement is about the step sequence of R104's IDEAL model (MP-LIN about max-plus recursions); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/si/box79/dblcheck.py, CORPUS = "),
     ("; G-N5-TIME stays OPEN; not M3", "; DBL-EQ (b)'s window count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2); G-N5-TIME stays OPEN; not M3"),
     ("if the pair l + 1 never moves and starts split, then F(l + 1) = F(l)", "for 1 ≤ l ≤ d − 2, if the pair l + 1 never moves and starts split, then F(l + 1) = F(l)"),
     ("E_l is the set of steps at which some mover of the old chain", "on 𝓛^R_d, E_l is the set of steps at which some mover of the old chain")]
x = L2
for i, (a, b) in enumerate(R, 1): print('R%d old in current text %d, new in L-3 %d' % (i, x.count(a), L3.count(b))); x = x.replace(a, b)
d = m = 0
for c in L3: d += (c == '(') - (c == ')'); m = min(m, d)
print('L-2 + R1..R6 == L-3', x == L3, hashlib.sha1(x.encode()).hexdigest(), len(x.encode()), 'lines', L3.count('\n'), '(', L3.count('('), ')', L3.count(')'), '|', L3.count('|'), '—', L3.count(' — '), '[', L3.count('['), 'mindepth', m)
