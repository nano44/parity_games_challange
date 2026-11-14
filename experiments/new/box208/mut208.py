#!/usr/bin/env python3
"""Box 208 (L-NEW successor 72): kill-side sweep for level208's must-0 counters on LONG runs. From a frozen genome BASE, each sample
applies d random mutations (d uniform in 1..DMAX; the mutations of box203 aclimb203.mutate with AC_FREE: a Xi-edge to any mover or to X,
a W-target, a beta parity, a beta rank swap, a start option, a gate index swap) and runs level208.census on the mutant (any Xi-feedback
number; the window counters need k <= 3). Prints the totals of the must-0 counters, how many mutants had k = 0 / 1 / 2-3 / more, and
the maxima of T, levels, phivals, platmax, wmax. Usage: mut208.py SEED COUNT DMAX BASE.json"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "box203")]
os.environ["AC_FREE"] = "1"
import level208, aclimb203
seed, cnt, dmax, base = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed); G0 = json.load(open(base)); tot = collections.Counter(); mx = collections.Counter(); kk = collections.Counter()
for i in range(cnt):
    G = G0
    for _ in range(rng.randint(1, dmax)): G = aclimb203.mutate(G, -1, rng)
    c = level208.census(level208.prep(G))
    for key in level208.MUST0 + ("stalls", "stallloud", "plat", "windows"): tot[key] += c[key]
    for key in ("T", "levels", "phivals", "platmax", "wmax", "wlev"): mx[key] = max(mx[key], c[key])
    kk["k0" if c["k"] == 0 else "k1" if c["k"] == 1 else "k2-3" if c["k"] <= 3 else "k4+"] += 1
print("mut", os.path.basename(base), "seed", seed, "samples", cnt, "dmax", dmax, " ".join("%s %d" % (k, kk[k]) for k in ("k0", "k1", "k2-3", "k4+")),
      "TOTALS", " ".join("%s %d" % (key, tot[key]) for key in level208.MUST0 + ("stalls", "stallloud", "plat", "windows")),
      "MAX", " ".join("%s %d" % (key, mx[key]) for key in ("T", "levels", "phivals", "platmax", "wmax", "wlev")), flush=True)
