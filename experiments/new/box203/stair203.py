#!/usr/bin/env python3
"""Box 203 part 2 (L-NEW successor 68): the STAIRCASE genome ST(m), k = 1, one option per mover (so the IDEAL-CYC run has T = 0 and
state 0 is the genome's start). Movers: y_0 .. y_(m-1) (y_j at level j), x_1 .. x_m (x_i at level i), f (level m).
  x_i: one option (W-target y_(i-1), Xi-target X = escape to u);
  y_j: one option (W-target y_(j-1), or c_W at level 0; Xi-target x_(j+2), and f for j = m - 1);
  f:   one option (W-target y_(m-1), Xi-target f: a Xi self-loop), its beta odd and of top beta rank, so the beta-cycle at f is
       Odd's best cycle node (reward below K1's).
Xi-graph: y_j -> x_(j+2) (strictly up), y_(m-1) -> f, f -> f: its only cycle is f's self-loop, k = 1. Odd's optimal play from x_1:
x_1 -e-> y_0 -beta-> x_2 -e-> y_1 -beta-> x_3 ... x_m -e-> y_(m-1) -beta-> f (cycle), e-sequence e(x_1) < e(x_2) < ... < e(x_m) under
[E-LEV]: m - 1 ascents in one play (if the engine agrees). Usage: stair203.py m OUT.json"""
import sys, json
m = int(sys.argv[1]); N = 2 * m + 1
Y = list(range(m)); X = [None] + list(range(m, 2 * m)); F = 2 * m          # y_j = j, x_i = m + i - 1, f = 2m
lev = [0] * N; opts = [None] * N
for j in range(m): lev[Y[j]] = j
for i in range(1, m + 1): lev[X[i]] = i
lev[F] = m
for i in range(1, m + 1): opts[X[i]] = [[Y[i - 1], -1, 0]]
for j in range(m):
    xt = X[j + 2] if j + 2 <= m else F
    opts[Y[j]] = [[Y[j - 1] if j else -1, xt, 0]]
opts[F] = [[Y[m - 1], F, 0]]
M = N; b = 0; gate = []
for x in range(N):
    opts[x][0][2] = b; gate.append([b]); b += 1
br = list(range(M)); bp = [0] * M
br[F], br[M - 1] = br[M - 1], br[F]; bp[F] = 1                                  # f's beta: top rank, odd
G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [0] * N}
json.dump(G, open(sys.argv[2], "w"))
