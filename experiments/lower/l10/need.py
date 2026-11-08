#!/usr/bin/env python3
"""L-LOWER 10: the fuel bill of the minimal STRETCH (stretch.py). For each original core step t preceded by an inserted idle step:
M_t = movers of pairs 0..J-1 that move at t and were free at the idle step (key unchanged since t-1, i.e. wait >= 1); each needs a
non-core mover on its chain to change AT the idle step. Also H_t = movers free at the idle step that do not move at t (must keep
holding). Prints counts per mover and the number of idle steps with M_t empty (no trigger needed: pure filler steps).
Usage: need.py GENOME.txt H"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
from stretch import stretch
D = rd(sys.argv[1]); H = int(sys.argv[2]); S, O = run(D); T = len(S) - 1; J = H - 1
keep = [0] + [t for t in range(1, T + 1) if S[t][:2 * J] != S[t - 1][:2 * J]]
S2 = [S[t] for t in keep]; O2 = [O[t] for t in keep]
tau, Tp, need = stretch(S2, O2, H)
Mc = Counter(); Hc = Counter(); empty = 0; idle = 0; sizes = Counter()
for i in range(1, len(S2)):
    if tau[i] - tau[i - 1] < 2: continue
    idle += 1; pre = S2[i - 1]; post = S2[i]; o = O2[i - 1]
    free = [x for x in range(2, 2 * J) if pre[x] != o[x // 2 - 1]]
    M = [x for x in free if post[x] != pre[x]]; Hh = [x for x in free if post[x] == pre[x]]
    for x in M: Mc[x] += 1
    for x in Hh: Hc[x] += 1
    if not M: empty += 1
    sizes[len(M)] += 1
print('idle steps', idle, 'with no retrigger needed', empty, '|M_t| hist', sorted(sizes.items()))
print('retrigger events per mover', sorted(Mc.items()))
print('free-and-holding at idle steps per mover', sorted(Hc.items()))
