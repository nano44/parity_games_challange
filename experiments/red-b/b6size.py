#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: sizes of Gamma3(G_k) from the .pg files, against the formulas of P-N5-EXP, and the first k beyond a
polynomial bound.
Per file G_k_g3.pg: n (vertices), m (edges = sum of the successor counts), and sizediff = [n != 135k - 230] + [m != 176k - 300]
(must be 0). Then, for c = 2, 3, 4: the least k >= 3 with 2^k - 1 > n^c and the least k with 2^k - 1 > (n + m)^c, n = 135k - 230,
m = 176k - 300 (exact integer arithmetic), with both sides at that k.
Control B6SIZE_CTRL=1: the formula for m is tested as 176k - 299 (sizediff must fire).
Usage: b6size.py G_3_g3.pg ..."""
import sys, os, re
CTRL = os.environ.get("B6SIZE_CTRL", "0")
kof = lambda fn: int(re.search(r"G_(\d+)_g3", os.path.basename(fn)).group(1))
for fn in sorted(sys.argv[1:], key=kof):
    k = kof(fn)
    n = m = 0
    for line in open(fn):
        p = line.strip().rstrip(";").split()
        if len(p) >= 4 and p[0].isdigit():
            n += 1
            m += len(p[3].split(","))
    mm = 176 * k - (299 if CTRL == "1" else 300)
    print(f"{os.path.basename(fn)} ctrl {CTRL} k {k} n {n} m {m} sizediff {int(n != 135 * k - 230) + int(m != mm)}", flush=True)
for c in (() if CTRL == "1" else (2, 3, 4)):
    for label, size in (("n", lambda k: 135 * k - 230), ("n+m", lambda k: 311 * k - 530)):
        k = 3
        while 2 ** k - 1 <= size(k) ** c:
            k += 1
        print(f"first k with 2^k - 1 > ({label})^{c}: k {k} size {size(k)} iterations_bound {2 ** k - 1} poly {size(k) ** c}", flush=True)
