#!/usr/bin/env python3
"""Numerical check of docs/struct/L4-proof.md: optimised bound of Theorem L4 and the closed form of Corollary L4.3."""
from math import comb, floor, ceil, log2, sqrt
def optimised(n):
    return max((comb(floor(log2(n // dp)) + dp // 2 - 1, floor(log2(n // dp))), dp) for dp in range(2, n + 1, 2) if n // dp >= 1)
def closed(n):
    a0, b0 = floor(log2(n) / 2) - 2, ceil(sqrt(n) / 2) - 2
    return comb(a0 + b0, a0) if a0 >= 0 and b0 >= 0 else 0
if __name__ == '__main__':
    for n in [64, 256, 1024, 4096, 2**16]:
        v, dp = optimised(n); print(f"n={n}: optimised {v} (d'={dp}), closed form {closed(n)}")
    assert all(closed(n) <= optimised(n)[0] for n in range(2, 5001)), "closed form exceeds the optimised bound"
    print("closed form <= optimised bound for all n <= 5000: ok")
