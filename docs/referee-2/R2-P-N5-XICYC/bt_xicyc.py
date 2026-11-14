# REFEREE-2 succ. 30: (1) byte test L-1 -> L-2 (fixes entry 1 R-1, strings taken from the fixes file); (2) my required W-2..W-4 on L-2
import sys, hashlib, re
L1 = open(sys.argv[1], encoding='utf-8').read(); L2 = open(sys.argv[2], encoding='utf-8').read(); F = open(sys.argv[3], encoding='utf-8').read()
old = F.split('- R-1, exact old string (in L-1, once):\n«', 1)[1].split('»\n- R-1, exact new string', 1)[0]
new = F.split('- R-1, exact new string (in L-2, once):\n«', 1)[1].split('»\n- Pins:', 1)[0]
print('R-1 old in L-1', L1.count(old), 'new in L-2', L2.count(new), 'L-1 + R-1 == L-2', L1.replace(old, new) == L2)
def shape(L):
    d = m = 0
    for c in L: d += (c == '(') - (c == ')'); m = min(m, d)
    return 'sha1 %s %d B lines %d ( %d ) %d | %d mindepth %d' % (hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), L.count('\n'), L.count('('), L.count(')'), L.count('|'), m)
print('L-2', shape(L2))
W = [("and DEAD ODD-FIXED (those three runs contain 1, 8 and 6 R-steps respectively)",
      "and DEAD ODD-FIXED («σ̄ is constant on every run of Λ-keeping steps» fails: those three runs contain 1, 8 and 6 R-steps respectively, each a Λ-keeping step at which σ̄ changes)"),
     ("ONEP-POLY: in the one-player model, a Λ-keeping run longer than N, or C > N·M, in 0 of 300 genomes (seg1p191.py 300 11);",
      "ONEP-POLY: in the one-player model, a Λ-keeping run longer than N, or C > N·M, in 0 of 300 genomes (seg1p191.py 300 11; R is not counted, R = 0 has no separate DATA);"),
     ("H0 itself is not checked by the tool, which counts 555 steps in these runs where some switching Even vertex is its own cycle node",
      "H0 is not checked by the tool, and these runs include steps at which H0 fails")]
x = L2
for i, (a, b) in enumerate(W, 2): print('W-%d old in L-2' % i, L2.count(a)); x = x.replace(a, b)
print('L-2 + W-2..W-4', shape(x))
