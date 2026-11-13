#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: fits with residuals for the rule G_k, from the generated outputs (no number typed by hand).
Reads sim.out (b6sim.py lines) and n5.out (b6n5.py lines). For each of T_key, max sw (against N + M) and N5 iterations (against n):
  model E (the closed form): T_key = 2^k - 2, maxsw = 2^(k-2), its = 2^k + 1 with k = (N + M + 48) / 27 = (n + 230) / 135;
          printed: the residual value - closed form at every point (must be 0 for the claim «exact on these points»);
  model X (free exponential): least squares of log2(value) on the size; slope, intercept, largest |residual| in log2 units;
  model P (free power law):   least squares of log2(value) on log2(size); exponent, largest |residual|, and the local exponents
          between consecutive points (a polynomial would keep them bounded; here they grow).
Usage: b6fit.py sim.out n5.out"""
import sys, math


def lsq(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    return a, b, max(abs(y - (a + b * x)) for x, y in zip(xs, ys))


def field(line, name):
    p = line.split()
    return int(p[p.index(name) + 1])


def report(label, sizes, vals, closed):
    print(f"{label}: points {len(vals)} sizes {sizes[0]}..{sizes[-1]}")
    print("  model E residuals (value - closed form): " + " ".join(str(v - c) for v, c in zip(vals, closed)))
    a, b, r = lsq(sizes, [math.log2(v) for v in vals])
    print(f"  model X log2(value) = {a:.4f} + {b:.6f} * size; max |residual| {r:.4f}")
    a, b, r = lsq([math.log2(s) for s in sizes], [math.log2(v) for v in vals])
    loc = [(math.log2(vals[i + 1]) - math.log2(vals[i])) / (math.log2(sizes[i + 1]) - math.log2(sizes[i])) for i in range(len(vals) - 1)]
    print(f"  model P log2(value) = {a:.4f} + {b:.4f} * log2(size); max |residual| {r:.4f}; local exponents " + " ".join(f"{x:.2f}" for x in loc))


sim = [l for l in open(sys.argv[1]) if l.startswith("G_") and " ctrl 0 " in l]
n5 = [l for l in open(sys.argv[2]) if l.startswith("G_") and " ctrl 0 " in l]
NM = [field(l, "N") + field(l, "M") for l in sim]
ks = [(s + 48) // 27 for s in NM]
assert all((s + 48) % 27 == 0 for s in NM)
report("T_key against N + M", NM, [field(l, "T") for l in sim], [2 ** k - 2 for k in ks])
report("max sw against N + M", NM, [field(l, "maxsw") for l in sim], [2 ** (k - 2) for k in ks])
nn = [field(l, "n") for l in n5]
kn = [(n + 230) // 135 for n in nn]
assert all((n + 230) % 135 == 0 for n in nn)
report("N5 iterations (engine 1) against n", nn, [field(l, "its") for l in n5], [2 ** k + 1 for k in kn])
report("N5 iterations (engine 2) against n", nn, [field(l, "its2") for l in n5], [2 ** k + 1 for k in kn])
