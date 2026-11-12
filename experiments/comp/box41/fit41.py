#!/usr/bin/env python3
"""L-COMP box 41 item 4: Deep_3 (= Σ_C Deep_3(C): internal-gate flips after t0(C) charged to depth > 3; deep41, scope all SCCs, one run
from S3 to the first fallback; total per run) against N + M. Envelope = max per size over every genome measured in box 41 (26 frozen
instances + the climb bests). Log-log least squares; exponent +- 1 standard error."""
import math
def fit(P):
    X = [math.log(a) for a, b in P]; Y = [math.log(b) for a, b in P]; n = len(P); mx = sum(X) / n; my = sum(Y) / n
    sxx = sum((x - mx) ** 2 for x in X); p = sum((x - mx) * (y - my) for x, y in zip(X, Y)) / sxx
    r = [y - my - p * (x - mx) for x, y in zip(X, Y)]; return p, math.sqrt(sum(e * e for e in r) / (n - 2) / sxx)
E = [(160, 2), (204, 3), (285, 10), (364, 9), (400, 24)]   # D150a best; C6G8_n54; D300b best; DWT20_2803; DHIB26_2804
p, se = fit(E); print("envelope", E, f"exponent {p:.2f} +- {se:.2f}")
C = [(160, 2), (285, 10)]; print("climb maxima only (2 points):", f"{math.log(10 / 2) / math.log(285 / 160):.2f}")
