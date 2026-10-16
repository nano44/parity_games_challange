#!/usr/bin/env python3
"""REFEREE-2 numeric re-check of docs/struct/L4-proof.md (l-struct 50dc28b): Theorem L4's optimised bound, every
inequality of Corollary L4.3's chain, the quoted table values, and the range where the last closed form is < 1."""
from math import comb, floor, ceil, log2, sqrt, isqrt
def thm_L4(n):
    best = (0, None)
    for dp in range(2, n + 1, 2):
        k = n // dp
        v = comb(floor(log2(k)) + dp // 2 - 1, floor(log2(k)))
        if v > best[0]:
            best = (v, dp)
    return best
bad = []
for n in range(64, 20001):
    a0, b0 = floor(log2(n) / 2) - 2, ceil(sqrt(n) / 2) - 2
    dp = 2 * (isqrt(n) // 2)                     # d' = 2 floor(sqrt(n)/2)
    k = n // dp
    a, b = floor(log2(k)), dp // 2 - 1
    chain = [
        ("d' even, 2<=d'<=n", dp % 2 == 0 and 2 <= dp <= n),
        ("sqrt(n)-2 <= d' <= sqrt(n)", sqrt(n) - 2 <= dp <= sqrt(n)),
        ("k >= floor(sqrt n)", k >= isqrt(n)),
        ("floor(lg k) >= a0", a >= a0),
        ("d'/2-1 >= b0", b >= b0),
        ("a0 >= 1, b0 >= 2", a0 >= 1 and b0 >= 2),
        ("C(a+b,a) >= C(a0+b0,a0)", comb(a + b, a) >= comb(a0 + b0, a0)),
        ("C(a0+b0,a0) >= ((a0+b0)/a0)^a0", comb(a0 + b0, a0) >= ((a0 + b0) / a0) ** a0 - 1e-9),
        ("b0/a0 >= sqrt(n)/(2 lg n)", b0 / a0 >= sqrt(n) / (2 * log2(n)) - 1e-12),
        ("Thm L4 max >= C(a0+b0,a0)", thm_L4(n)[0] >= comb(a0 + b0, a0)),
    ]
    for name, ok in chain:
        if not ok:
            bad.append((n, name))
print("chain violations for 64 <= n <= 20000:", bad[:10] if bad else "none")
# quoted table (L4-proof.md section 4): optimised / closed form
for n in [64, 256, 1024, 4096, 2 ** 16]:
    a0, b0 = floor(log2(n) / 2) - 2, ceil(sqrt(n) / 2) - 2
    v, dp = thm_L4(n)
    last = (sqrt(n) / (2 * log2(n))) ** a0
    print(f"n={n}: Thm L4 max {v} at d'={dp} (d'/n^0.6={dp / n**0.6:.2f}); closed C(a0+b0,a0)={comb(a0+b0,a0)}; last form (sqrt n/(2 lg n))^a0 = {last:.3g}")
first_gt1 = next(n for n in range(64, 10**6) if (sqrt(n) / (2 * log2(n))) ** (floor(log2(n) / 2) - 2) > 1)
print("last closed form (sqrt n/(2 lg n))^{a0} exceeds 1 from n =", first_gt1, "on (it is < 1 at n = 64: 8/12)")
print("n < 64: closed form C(a0+b0,a0) <= 1?", all((lambda a0, b0: a0 < 0 or comb(a0 + b0, a0) <= 1)(floor(log2(n) / 2) - 2, ceil(sqrt(n) / 2) - 2) for n in range(2, 64)))
print("Theorem L4 at n = 1: the set of even d' in [2, 1] is empty; max undefined. n=2..8:", [thm_L4(n) for n in range(2, 9)])
# consistency with the lane's SAT table (unrefereed data, convention E s^E and V s^V): bound must not exceed the value
sE = {(2, 4): 3, (2, 6): 4, (2, 8): 5, (3, 4): 5, (3, 6): 7, (4, 4): 8, (1, 4): 1, (2, 2): 2}
print("CDFJLP Thm 5.1 bound vs s^E table:", all(comb(floor(log2(n)) + d // 2 - 1, floor(log2(n))) <= v for (n, d), v in sE.items()))
sV = {1: 1, 2: 2, 3: 5, 4: 7}
print("Thm L4 bound vs s^V(n,n) table:", {n: (thm_L4(n)[0], sV[n]) for n in range(2, 5)})
