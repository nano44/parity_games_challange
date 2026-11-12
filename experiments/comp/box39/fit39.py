#!/usr/bin/env python3
"""L-COMP box 39 item 3: log-log least-squares fits of Q_(>1) (loud steps of loud depth > 1, depth39 scope all, one IDEAL-CYC run, total per
run) against N + M. Sets: (E) envelope = max Q_(>1) per size over every frozen k = 1 genome measured in box 39 at sizes with a climb or a
structured family point; (CW) the CW(n) family alone; (L) linear fit Q_(>1) = a (N + M) + b on (E). Exponent +- 1 standard error."""
import math
def fit(P):
    X = [math.log(a) for a, b in P]; Y = [math.log(b) for a, b in P]; n = len(P); mx = sum(X) / n; my = sum(Y) / n
    sxx = sum((x - mx) ** 2 for x in X); p = sum((x - mx) * (y - my) for x, y in zip(X, Y)) / sxx
    r = [y - my - p * (x - mx) for x, y in zip(X, Y)]; se = math.sqrt(sum(e * e for e in r) / (n - 2) / sxx) if n > 2 else float("nan")
    return p, se
def lin(P):
    n = len(P); mx = sum(a for a, b in P) / n; my = sum(b for a, b in P) / n
    a = sum((x - mx) * (y - my) for x, y in P) / sum((x - mx) ** 2 for x, y in P); return a, my - a * mx
E = [(145, 10), (303, 10), (612, 18), (1515, 29)]      # K1L10_n48; C300a best; C600a best; CW32_own
CW = [(157, 2), (303, 7), (643, 14), (1515, 29)]
C = [(303, 10), (612, 18)]                              # the two band maxima of this box's climbs
for name, P in (("E envelope", E), ("CW family", CW), ("CW n>=8", CW[1:])):
    p, se = fit(P); a, b = lin(P); print(f"{name}: points {P}  exponent {p:.3f} +- {se:.3f}  linear {a:.4f} (N+M) + {b:.2f}")
print("band maxima only (2 points, no error):", f"{math.log(18 / 10) / math.log(612 / 303):.3f}")
