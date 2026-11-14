#!/usr/bin/env python3
"""B7: RF on K^s_n from the generator; one line per n: iterations against the law 7*2^(n-1) - 2n - 3.
Usage: runks.py N1 N2 ... [--tie high|low]"""
import sys, time
import rfc2
from si7 import Engine, root_first
tie = "high"
a = sys.argv[1:]
if "--tie" in a:
    k = a.index("--tie"); tie = a[k + 1]; a = a[:k] + a[k + 2:]
for n in map(int, a):
    g, s0 = rfc2.build(n, True); E = Engine(g); t0 = time.time()
    k, sg, val, tau = E.run(s0, root_first(tie)); law = 7 * 2 ** (n - 1) - 2 * n - 3
    print(f"B7 Ks n {n} |V| {g.n} |E| {g.m} RF tie-{tie} iterations {k} law {law} diff {k - law} odd-won {E.regions(val).count(1)} final [{rfc2.state(g, sg, n)}] secs {time.time() - t0:.0f}", flush=True)
