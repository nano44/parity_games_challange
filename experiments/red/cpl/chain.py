#!/usr/bin/env python3
"""L-RED successor 27 (STEP 1): the mutual release chain. Level i = 1..L:
  d_i (Odd): tau = D_i (marker) | o_{i-1};   a_i (Even): sigma = d_i | A_i;   f_i (Even): sigma = F_i | a_i;   o_i (Odd): tau = f_i | O_i.
Even-scale values: O_{i-1} < F_i < O_i < (all A, D), and D_1 > A_1 > D_2 > A_2 > ... > D_L > A_L (all even markers above the odd sink z; every play is a DAG path to z).
Intended cascade: o_{i-1} (tau) -> d_i (tau, U-menu) -> a_i (sigma, W-release) -> f_i (sigma, Xi-menu) -> o_i (tau, W-release).
Usage: chain.py L OUT.pg OUT.start"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import B
L = int(sys.argv[1]); b = B()
Z = 4 * L + 101; Z += 1 - Z % 2                   # odd sink priority, above all structural vertices
mk = lambda k: Z + 1 + 2 * k                      # even markers, increasing in k
b.add("z", 0, Z, ["z"])
# Even-scale ranks: F_i = 4i, O_i = 4i + 1; D_i = 4L + 11 + 2(L - i), A_i = D_i - 1; base: O_0 = 1, K0 above all
b.add("K0", 1, mk(10 * L + 20), ["z"]); b.add("O0", 1, mk(1), ["z"])
b.add("o0", 1, None, ["K0", "O0"], start="K0")
for i in range(1, L + 1):
    b.add(f"D{i}", 1, mk(4 * L + 10 + 2 * (L - i) + 1), ["z"]); b.add(f"A{i}", 1, mk(4 * L + 10 + 2 * (L - i)), ["z"])
    b.add(f"F{i}", 1, mk(4 * i), ["z"]); b.add(f"O{i}", 1, mk(4 * i + 1), ["z"])
    b.add(f"d{i}", 1, None, [f"D{i}", f"o{i - 1}"], start=f"D{i}")
    b.add(f"a{i}", 0, None, [f"d{i}", f"A{i}"], start=f"d{i}")
    b.add(f"f{i}", 0, None, [f"F{i}", f"a{i}"], start=f"F{i}")
    b.add(f"o{i}", 1, None, [f"f{i}", f"O{i}"], start=f"f{i}")
b.write(sys.argv[2], sys.argv[3]); print("n", len(b.V))
