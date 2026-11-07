#!/usr/bin/env python3
"""L-SI box 77: PASS-FREEZE instance builder. From genome FILE and level L (pair L = movers 2L, 2L+1, not Xi-targets of any option):
both options of both movers get Xi-target X; the parity of each mover's start option is set even and of the other option odd (so each
mover prefers its start option forever); the start of the pair is set split (s(2L) = 0, s(2L+1) = 1 or the reverse, both tried).
Prints the F-profile before/after and writes the first variant whose levels < L keep their F and whose level L-1 is doubling."""
import sys, os, json, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import Sim, analyse, is_lr
def prof(G):
    sim = Sim(G); S = sim.run(tuple(G["start"])); a = analyse(sim, S); T = a["T"]; d = G["N"] // 2
    return T, [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)], \
        [sum(1 for t in range(1, T + 1) if y in a["Mv"][t]) for y in range(G["N"])]
f, L, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
G = json.load(open(f)); N = G["N"]; p, q = 2 * L, 2 * L + 1
assert all(G["opts"][x][k][1] not in (p, q) for x in range(N) for k in range(2))
T0, F0, _ = prof(G); print("before T %d F %s" % (T0, F0))
for sp in (0, 1):
    H2 = copy.deepcopy(G); H2["start"][p] = sp; H2["start"][q] = 1 - sp
    for x in (p, q):
        for k in range(2):
            H2["opts"][x][k][1] = -1; H2["bp"][H2["opts"][x][k][2]] = 0 if k == H2["start"][x] else 1
    assert is_lr(H2)
    T, F, mv = prof(H2)
    print("variant start(%d,%d) = (%d,%d): T %d F %s moves(p,q) %d %d" % (p, q, sp, 1 - sp, T, F, mv[p], mv[q]))
    if F[:L] == F0[:L] and F[L - 1] == 2 * F[L - 2] + 2 and mv[p] == mv[q] == 0 and F[L] == F[L - 1]:
        json.dump(H2, open(out, "w")); print("written", out); break
