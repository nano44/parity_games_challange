#!/usr/bin/env python3
"""L-LOWER 10: build the stretched core target (pairs 0..J-1 states on the new time axis) and report: the 7-window (level H-1
window) lengths, and whether every idle step directly follows an o(H-2) change. Importable: target(D, H) -> (Sc, Oc, idle)."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
from stretch import stretch
def target(D, H):
    S, O = run(D); T = len(S) - 1; J = H - 1
    keep = [0] + [t for t in range(1, T + 1) if S[t][:2 * J] != S[t - 1][:2 * J]]
    S2 = [S[t][:2 * J] for t in keep]; O2 = [O[t][:J] for t in keep]
    tau, Tp, need = stretch(S2, O2, H)
    Sc = []; Oc = []; idle = []
    for i in range(len(S2)):
        while len(Sc) < tau[i]:
            Sc.append(S2[i - 1]); Oc.append(O2[i - 1]); idle.append(len(Sc) - 1)
        Sc.append(S2[i]); Oc.append(O2[i])
    while len(Sc) <= Tp: Sc.append(S2[-1]); Oc.append(O2[-1]); idle.append(len(Sc) - 1)
    return Sc, Oc, idle
if __name__ == '__main__':
    D = rd(sys.argv[1]); H = int(sys.argv[2]); Sc, Oc, idle = target(D, H); T = len(Sc) - 1
    ch = [t for t in range(1, T + 1) if Oc[t][H - 2] != Oc[t - 1][H - 2]]
    cuts = [0] + ch + [T + 1]; L = Counter(b - a for a, b in zip(cuts, cuts[1:]))
    after = sum(1 for i in idle if i - 1 in set(ch)); print('T', T, 'o(H-2) changes', len(ch), 'level-(H-1) window lengths', sorted(L.items()),
          'idle', len(idle), 'idle right after an o(H-2) change', after)
