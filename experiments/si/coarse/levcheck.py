#!/usr/bin/env python3
"""L-SI box 9: regression check for the level ∞ of mono.lev / mono.coarse (before box 9, ∞ was 99 and a genuine top rank >= 99,
possible at n >= 100, read as ∞). Run by experiments/si/check.sh."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mono
a, b = (5, 1 << 99, 3), (5, 0, 3)            # same cycle node, path sets differ at rank 99
assert mono.lev(a, b) == 99 and mono.lev(a, b) < mono.INF
assert mono.lev((5, 0, 3), (6, 0, 3)) == mono.INF > 10 ** 4  # different cycle nodes
assert mono.coarse(a, 99) == (5, 0) and mono.coarse(a, 98) == (5, 1) and mono.coarse(a, mono.INF) == ()
print("LEVCHECK PASS")
