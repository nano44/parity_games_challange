#!/usr/bin/env python3
"""S5 §6: where L4's explicit bound B(n) = (sqrt(n)/(2 lg n))^(floor(lg(n)/2) - 2) (docs/struct/L4-proof.md) exceeds the
DATA formula F(n) = n + (h-1)(n-1), h = ceil(n/2) (s^V at d = n).  Prints the last n < N1 with B(n) <= F(n), and N1, the
least n with n^4/(256 lg^8 n) > (n^2+1)/2 (from N1 on, B(n) >= n^4/(256 lg^8 n) since the exponent is >= 8 and the base
>= 1, and the ratio to (n^2+1)/2 >= F(n) increases).  Floats: values ~1e12, margins ~1e5, double precision suffices."""
from math import log2, floor
B = lambda n: (n ** 0.5 / (2 * log2(n))) ** (floor(0.5 * log2(n)) - 2)
F = lambda n: n + ((n + 1) // 2 - 1) * (n - 1)
low = lambda n: n ** 4 / (256 * log2(n) ** 8)
a, b = 2 ** 10, 2 ** 30
while b - a > 1:
    m = (a + b) // 2
    a, b = (a, m) if low(m) > (m * m + 1) / 2 else (m, b)
N1 = b
assert floor(0.5 * log2(N1)) - 2 >= 8 and N1 ** 0.5 >= 2 * log2(N1)
last_bad = max(n for n in range(2_000_000, N1) if not B(n) > F(n))
print(f"N1 = {N1}; last n < N1 with B(n) <= F(n): {last_bad}; B > F for all n >= {last_bad + 1}")
print(f"at n = {last_bad + 1}: B = {B(last_bad + 1):.9e}, F = {F(last_bad + 1):.9e}")
