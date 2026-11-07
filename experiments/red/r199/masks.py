#!/usr/bin/env python3
"""L-RED R199 MASKS: three-level stacks with PARTIAL doubling. genk-style period-B targets (NPER base intervals), level j prompt at every
carry of level j-1 (and step 1), late at offset B / 2^j only in the intervals selected by a mask (levels 1, 2; level 3 full). Keeps the
W-feasible targets (r199/build.py) whose F satisfies F_l >= r * F_(l-1) for l = 1..3 (r = RATIO, default 1.5) and writes them.
Usage: masks.py nper B ratio outdir"""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build
NP, B, r, od = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; os.makedirs(od, exist_ok=True); L = NP * B
def level(m, l, cs, o, mask):
    pr, la = set(), set()
    for i, c in enumerate(cs):
        nxt = cs[i + 1] if i + 1 < len(cs) else L + 1; pr.add(c)
        if mask[i] and c + o < nxt and c + o <= L: la.add(c + o)
    m[2 * l] = pr; m[2 * l + 1] = la; return sorted(pr | la)
idx = []
for m1 in itertools.product((0, 1), repeat=NP):
    base = {0: {B + 1}, 1: ({2 * B + 1} if NP == 3 else set())}; cs0 = sorted([1] + [B * i + 1 for i in range(1, NP)])
    m = dict(base); c1 = level(m, 1, cs0, B // 2, m1)
    for m2 in itertools.product((0, 1), repeat=len(c1)):
        mm = dict(m); c2 = level(mm, 2, c1, B // 4, m2); level(mm, 3, c2, 1, [1] * len(c2))
        T = build.build(L, 4, mm)
        if T["bad"]: continue
        F = T["F"]
        if not all(F[l] >= r * F[l - 1] for l in (1, 2, 3)): continue
        name = "mk_p%d_B%d_%s_%s" % (NP, B, "".join(map(str, m1)), "".join(map(str, m2)))
        json.dump(T, open(os.path.join(od, name + ".json"), "w")); idx.append((name, F))
print("MASKS nper", NP, "B", B, "ratio", r, "targets", len(idx))
for n, F in idx: print(" ", n, "F", F)
