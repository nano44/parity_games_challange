#!/usr/bin/env python3
"""Parity game on HIJ's arena G_n (arXiv 1304.1888, Fig. 2 / Theorem 21): vertex 0 self-loop priority 1, vertex 1 self-loop priority 2,
every vertex i >= 2 (owner Even) has edges to 0 and 1 and priority i + 1 (so d = n). Even wins everywhere (go to 1). The JS matrix of
this arena has kappa = Theta(n/(1-gamma)^2) whatever the priorities. Usage: gen_hij.py n > game.pg"""
import sys
n = int(sys.argv[1]); print(f"parity {n - 1};")
print('0 1 1 0;'); print('1 2 0 1;')
for i in range(2, n): print(f"{i} {i + 1} 0 0,1;")
