#!/usr/bin/env python3
"""B-solo: one replayable chain level (L-RED CARRY box). bsolo.py mB mA out.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gadget import Game
mB, mA, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
G = Game()
G.v("z", 1, 1, ["z"])                       # Odd sink (Odd dominion)
G.v("x", 30, 0, ["q"])                       # piece-0 argmax top
G.v("q", 0, 0, [f"b{mB}"])                   # x forgiven while b_mB alive
G.v("s", 31, 0, ["x", "z"])                  # cut seed: attracts to X = Dom(x)
for i in range(1, mB + 1):
    G.v(f"b{i}", 2 * i + 2, 1, [])           # chain top, Odd-owned, even priority increasing in i
    for j in range(1, mA + 1):
        G.v(f"g{i}_{j}", 0, 0, [f"b{i}"])    # private witnesses
        G.e(f"b{i}", f"g{i}_{j}")
    G.e(f"b{i}", "s" if i == 1 else f"b{i-1}")
idx = G.dump(out)
print(" ".join(f"{k}={v}" for k, v in idx.items()), file=sys.stderr)
