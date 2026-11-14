#!/usr/bin/env python3
"""L-SI box 109: what RF does to the bits of Friedmann's counter G_n (arXiv 1106.0778v2 par. 6.2; L-LIT's T66 names), from iota.
A bit i is SET when sigma(d_i) = e_i. Counters per n: iterations; sets (unit: iterations at which some d_i moves onto e_i); resets
(unit: iterations at which some d_i leaves e_i; Howard's run resets lower bits at every carry); the largest number of switches of
one vertex, by letter class.  Usage: bits109.py n..   (env LLIT as fam109.py)"""
import sys, os, importlib.util, collections
av = sys.argv[1:]; sys.argv = [sys.argv[0]]
import fam109, rf109
spec = importlib.util.spec_from_file_location("t66", os.path.join(os.environ["LLIT"], "docs/lit/T66-depth-check.py")); t66 = importlib.util.module_from_spec(spec); spec.loader.exec_module(t66)
for n in map(int, av):
    _, _, names = t66.lmcs(n); H, s0 = fam109.lmcs_game(n); sigma = [s0[v] if H.owner[v] == 0 else -1 for v in range(H.n)]
    tr = []; r = rf109.run(H, start=list(sigma), trace=tr); sets = resets = 0; cnt = collections.Counter()
    for _, sel in tr:
        for v, w in sel:
            cnt[v] += 1
            if names[v][0] == "d":
                e = "e" + names[v][1:]
                sets += names[w] == e; resets += names[sigma[v]] == e
            sigma[v] = w
    cls = collections.defaultdict(int)
    for v, c in cnt.items(): cls[names[v][0]] = max(cls[names[v][0]], c)
    allset = all(names[sigma[v]] == "e" + names[v][1:] for v in range(H.n) if names[v][0] == "d")
    print(f"BITS109 fr {n}: iterations {r['its']} sets {sets} resets {resets} all bits set at the end {allset} max switches per vertex by class " + " ".join(f"{k}:{cls[k]}" for k in sorted(cls)), flush=True)
