#!/usr/bin/env python3
"""L-NEW box 183: upper-level activity of L^R_d runs (any Xi; ISO or not). For a run: U := #steps t with s_t != s_(t-1) on the levels >= 1
(R110's count in T_k), C := #steps at which b_0 = [g(0, s(0)) < g(1, s(1))] changes (the c-changes of R110 W-ONLY), Z := #steps moving
0 or 1. R110: for ISO genomes U <= T_C(d - 1) (W-ONLY: the levels >= 1 follow the iterated c-step). For non-ISO genomes this is
the open question. Prints, per d and ISO flag, the max U with its C, over every start for d <= 4 and stored starts otherwise.
Usage: upper.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
best = {}
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert fl["is_lr"](G)
    except Exception: continue
    d = G["N"] // 2; g = Gen(G); iso = fl["is_iso"](G)
    for st in (itertools.product((0, 1), repeat=G["N"]) if d <= 4 else [tuple(G["start"])]):
        S, _ = g.run(tuple(st)); T = len(S) - 1
        U = sum(1 for t in range(1, T + 1) if S[t][2:] != S[t - 1][2:])
        b = [int(G["gate"][0][s[0]] < G["gate"][1][s[1]]) for s in S]; C = sum(1 for t in range(1, T + 1) if b[t] != b[t - 1])
        Z = sum(1 for t in range(1, T + 1) if S[t][:2] != S[t - 1][:2])
        key = (d, iso, C)
        if U > best.get(key, (-1,))[0]: best[key] = (U, T, Z, os.path.basename(f), "".join(map(str, st)))
for k in sorted(best): print("d %d %-7s C %d: max U %d (T %d, Z %d) %s start %s" % (k[0], "ISO" if k[1] else "non-ISO", k[2], *best[k]))
