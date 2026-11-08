#!/usr/bin/env python3
"""L-LOWER 11 (BOX L11): the TIGHT H-capped core target from a capped (H-1)-genome, the small-H analogue of l10/build.core8.
Pairs 0..H-2 follow l10/stmap.target(D, H) (minimal stretch under P-TOWER-FUEL Lemmas 2, 3 at H; o(H-2) changes at 3, 5, ...);
pair H-1 is added: f = 2(H-1)+1 moves to c = o(H-2) at the first step of every (H-1)-window (step 1 for the first), q = 2(H-1) at
the second step; pair H-1 starts joined at 1 - c(0). Core gates: the base genome's for levels 0..H-2, joined value 0 for level H-1.
target(D, H) -> (LS, core_gate): LS[t] = states of movers 0..2H-1; core_gate = the 4H gate values. CLI prints T and F(0..H-1)."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
for p in ('../l10', '../l6', '../l9'): sys.path.insert(0, os.path.join(here, p))
from sim6 import rd, okeys
import stmap
def target(D, H):
    Sc, Oc, idle = stmap.target(D, H); T = len(Sc) - 1
    c = [o[H - 2] for o in Oc]; f = q = 1 - c[0]; pend = None; out = []
    for t in range(T + 1):
        if t >= 1:
            if t == 1 or c[t] != c[t - 1]: f = c[t]; pend = t + 1
            elif pend == t: q = c[t]; pend = None
        out.append(tuple(Sc[t][:2 * (H - 1)]) + (q, f))
    g = list(D['gate'][:4 * (H - 1)]) + [4 * (H - 1) + 1000 + k for k in range(4)]
    return out, g
def F(LS, g, H):
    O = [okeys({'d': H, 'gate': g}, list(s)) for s in LS]
    return [sum(1 for t in range(1, len(O)) if O[t][l] != O[t - 1][l]) for l in range(H)]
if __name__ == '__main__':
    D = rd(sys.argv[1]); H = int(sys.argv[2]); LS, g = target(D, H); T = len(LS) - 1
    print('T', T, 'F', F(LS, g, H), 'tight caps', [2 ** (l + 2) - 2 for l in range(H)], 'gate', *g)
    if len(sys.argv) > 3:
        with open(sys.argv[3], 'w') as f:
            f.write('# tight target ' + ' '.join(sys.argv[1:3]) + '\ngate ' + ' '.join(map(str, g)) + '\n')
            for s in LS: f.write(' '.join(map(str, s)) + '\n')
