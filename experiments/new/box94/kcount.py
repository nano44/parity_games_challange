#!/usr/bin/env python3
"""L-NEW box 94: number k of Odd choice vertices (out-degree >= 2) of each game file given; prints 'KCOUNT path n k'."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import load
for p in sys.argv[1:]:
    g = load(p); print(f"KCOUNT {p} n {g.n} k {sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)}")
