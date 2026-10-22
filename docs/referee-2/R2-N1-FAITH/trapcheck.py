#!/usr/bin/env python3
"""Check alltrap structure: compare G_N against switchallexp(N); every Even vertex with >=2 succ has exactly one extra
successor t (Odd, even prio P, single succ c), c Odd odd prio q with only a self-loop; P = Bround+2+2k, q = Bround+1."""
import sys, re
def rd(p):
    V = {}
    for l in open(p):
        l = l.strip().rstrip(';')
        if not l or l.startswith('parity') or l.startswith('%'): continue
        m = re.match(r'^(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)', l); V[int(m.group(1))] = (int(m.group(2)), int(m.group(3)), sorted(set(int(x) for x in m.group(4).split(','))))
    return V
G, O = rd(sys.argv[1]), rd(sys.argv[2]); k = int(sys.argv[3])
B = max(p for p, _, _ in O.values()); B += B % 2
bad = 0; nt = 0
for v, (p, o, s) in O.items():
    gp, go, gs = G[v]
    assert gp == p and go == o
    extra = [w for w in gs if w not in s]
    if o == 0 and len(s) >= 2:
        if len(extra) != 1: bad += 1; continue
        t = extra[0]; tp, to, ts = G[t]
        if not (to == 1 and tp == B + 2 + 2 * k and len(ts) == 1): bad += 1; continue
        c = ts[0]; cp, co, cs = G[c]
        if not (co == 1 and cp == B + 1 and cs == [c]): bad += 1; continue
        nt += 1
    elif extra: bad += 1
print('original n', len(O), 'game n', len(G), 'traps', nt, 'bad', bad, 'B', B, 'P', B + 2 + 2 * k, 'q', B + 1, 'n check', len(G) == len(O) + 2 * nt)
