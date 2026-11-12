#!/usr/bin/env python3
"""L-LOWER 16: reader sets per helper level. For GENOME and each level L = 8..31: R(L) = movers r (not on level L) whose Xi-reach contains
a mover of level L (counter = movers; set = all 64; scope = the genome's fixed wiring); C(L) = R(L) restricted to the cluster {12, 13, 14, 15};
key activity = number of changes of o(L-1) on rows 0..P of the clamped run (core forced to TARGET). Usage: readers.py GENOME TARGET P"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
D = sim6.rd(sys.argv[1]); P = int(sys.argv[3]); xt = D['xt']
T = open(sys.argv[2]).read().split(); tg = [[int(c) for c in T[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16))); K = [sim6.okeys(D, list(s)) for s in S]
def reach(b):
    out = set(); st = [b]
    while st:
        y = st.pop()
        for k in (0, 1):
            z = xt[2 * y + k]
            if z >= 0 and z not in out: out.add(z); st.append(z)
    return out
RE = {b: reach(b) for b in range(64)}
print('READERS', os.path.basename(sys.argv[1]), 'rows 0..%d' % P)
for L in range(8, 32):
    sl = {2 * L, 2 * L + 1}; R = sorted(r for r in range(64) if r not in sl and RE[r] & sl); C = [r for r in R if 12 <= r <= 15]
    act = sum(1 for t in range(1, P + 1) if K[t][L - 1] != K[t - 1][L - 1])
    print('L %2d slots %s |R| %2d cluster readers %-14s key o(%d) changes %2d' % (L, sorted(sl), len(R), C, L - 1, act))
