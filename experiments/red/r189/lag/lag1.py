#!/usr/bin/env python3
"""L-RED R189 LAG1: the one-shot lag gadget by hand (docs/red/R189-lag.md section 1). 2-wide ladder, d = 3, deg 2:
level 0: a0 (moves once: the lower key flip), a1 (static); level 1: y1 (released at once), y2 (its new face reads y1: lags one step);
level 2: z (W-targets y1 / y2; its faces leapfrog: Z2 reads y1); z' static. Writes lag1.json. Usage: lag1.py out.json"""
import sys, json
# movers: 0 a0, 1 a1, 2 y1, 3 y2, 4 z, 5 z'      option = [wt, xt, beta-id];  X = -1
opts = [[[-1, -1, 0], [-1, -1, 1]],      # a0: A0 (gate 10), A0' (gate 0)
        [[-1, -1, 2], [-1, -1, 3]],      # a1: static
        [[0, -1, 4], [1, -1, 5]],        # y1: P1 (wt a0), Q1 (wt a1)
        [[0, 2, 6], [1, -1, 7]],         # y2: P2 (wt a0, xt y1), Q2 (wt a1)
        [[2, -1, 8], [3, 2, 9]],         # z : Z1 (wt y1), Z2 (wt y2, xt y1)
        [[2, -1, 10], [2, -1, 11]]]      # z': static
G = dict(N=6, lev=[0, 0, 1, 1, 2, 2], opts=opts, deg=2, cyc=False,
         gate=[[10, 0], [5, 6], [8, 7], [3, 1], [2, 4], [9, 11]],
         br=[7, 8, 6, 5, 11, 10, 3, 2, 9, 4, 1, 0], bp=[1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
         start=[0, 0, 1, 1, 1, 0])
json.dump(G, open(sys.argv[1], "w"))
